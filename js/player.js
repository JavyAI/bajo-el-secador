(() => {
  const RESTART_SEC = 3;
  const POLL_MS = 250;
  const FADE_OUT_MS = 1100;
  const FADE_IN_MS = 1300;
  const FADE_REDUCED_MS = 200;

  const ROOMS = {
    salon: {
      name: "Bajo el secador",
      lockup: ["Bajo el", "secador"],
      kicker: "Baladas y merengue",
      theme: "#1a3538",
      tracks: "public/salon.json",
      lista: "https://www.youtube.com/playlist?list=PLHGerkzq-_SQ",
    },
    barberia: {
      name: "En la silla",
      lockup: ["En la", "silla"],
      kicker: "Bachata",
      theme: "#102848",
      tracks: "public/barberia.json",
      lista: "https://www.youtube.com/playlist?list=PLUXmVaLcUP14",
    },
    colmado: {
      name: "En la esquina",
      lockup: ["En la", "esquina"],
      kicker: "Salsa y merengue",
      theme: "#4e5540",
      tracks: "public/colmado.json",
      lista: "https://www.youtube.com/playlist?list=PLHayRTekRcmM",
    },
  };

  const el = {
    cover: document.getElementById("cover"),
    title: document.getElementById("title"),
    artist: document.getElementById("artist"),
    lista: document.getElementById("lista-link"),
    play: document.getElementById("btn-play"),
    prev: document.getElementById("btn-prev"),
    next: document.getElementById("btn-next"),
    seek: document.getElementById("seek"),
    elapsed: document.getElementById("elapsed"),
    duration: document.getElementById("duration"),
    status: document.getElementById("status"),
    clock: document.getElementById("clock"),
    clockHi: document.getElementById("clock-hi"),
    clockTime: document.getElementById("clock-time"),
    clockDate: document.getElementById("clock-date"),
    online: document.getElementById("online"),
    wordmark: document.getElementById("wordmark"),
    kicker: document.getElementById("kicker"),
    heroA: document.getElementById("hero-a"),
    heroB: document.getElementById("hero-b"),
    rooms: Array.from(document.querySelectorAll(".rooms a")),
    themes: Array.from(document.querySelectorAll('meta[name="theme-color"]')),
    dbg: document.getElementById("dbg"),
    dbgBody: document.getElementById("dbg-body"),
    dbgClose: document.getElementById("dbg-close"),
  };

  const state = {
    room: "salon",
    catalog: [],
    catalogs: {},
    queue: [],
    index: 0,
    loop: true,
    playing: false,
    wanted: "idle",
    player: null,
    players: { a: null, b: null },
    activeSlot: "a",
    apiReady: false,
    apiLoading: null,
    duration: 0,
    seeking: false,
    poll: null,
    announced: "",
    armed: false,
    frontHero: "a",
    loadGen: 0,
    fadeGen: 0,
    mixing: false,
    masterVolume: 100,
    volumeWorks: null,
    advancing: false,
    expectIncoming: null,
    lastFailAt: 0,
    loadedAt: 0,
    startedAt: 0,
    nudgeCount: 0,
    failHits: {},
    debug: false,
    debugLog: [],
    watchdog: null,
  };

  const YT_NAME = {
    "-1": "unstarted",
    0: "ended",
    1: "playing",
    2: "paused",
    3: "buffering",
    5: "cued",
  };

  function debugOn() {
    const params = new URLSearchParams(location.search);
    return params.get("debug") === "1" || localStorage.getItem("bes-debug") === "1";
  }

  function setDebug(on) {
    state.debug = on;
    try {
      localStorage.setItem("bes-debug", on ? "1" : "0");
    } catch {
      /* private mode */
    }
    if (el.dbg) el.dbg.hidden = !on;
    if (on) renderDebug();
  }

  function dbg(kind, detail) {
    const track = current();
    const row = {
      t: new Date().toLocaleTimeString("es-DO", { hour12: false }),
      kind,
      detail: detail || "",
      yt: YT_NAME[String(ytState())] || String(ytState()),
      want: state.wanted,
      mix: state.mixing ? 1 : 0,
      song: track ? `${track.artist} — ${track.title}` : "",
    };
    state.debugLog.push(row);
    if (state.debugLog.length > 40) state.debugLog.shift();
    if (state.debug) renderDebug();
  }

  function renderDebug() {
    if (!el.dbgBody) return;
    const track = current();
    const head = [
      `want ${state.wanted}   yt ${YT_NAME[String(ytState())] || ytState()}   slot ${state.activeSlot}`,
      `mix ${state.mixing ? "yes" : "no"}   iframes ${document.querySelectorAll("#yt-host iframe").length}   nudge ${state.nudgeCount}`,
      `volWorks ${state.volumeWorks}   idx ${state.index + 1}/${state.queue.length}`,
      track ? `${track.title}` : "(no track)",
      "— Shift+D to hide —",
    ].join("\n");
    const lines = state.debugLog
      .slice(-14)
      .map((r) => `${r.t}  ${r.kind}${r.detail ? " " + r.detail : ""}`)
      .join("\n");
    el.dbgBody.textContent = `${head}\n${lines}`;
  }

  function nudgePlay(player, why) {
    if (!player || state.wanted !== "play" || state.mixing) return;
    state.nudgeCount += 1;
    dbg("nudge", `${why} #${state.nudgeCount}`);
    try {
      if (player.unMute) player.unMute();
      setVol(player, state.masterVolume);
      player.playVideo();
    } catch {
      /* ignore */
    }
  }

  function startWatchdog() {
    if (state.watchdog) return;
    state.watchdog = setInterval(() => {
      if (state.wanted !== "play" || state.mixing || state.seeking) return;
      const player = state.player;
      if (!player) return;
      const s = ytState(player);
      if (s === 1 || s === 3) {
        if (s === 1) state.nudgeCount = 0;
        return;
      }
      if (s === 0 && isRealEnd(player)) return;
      nudgePlay(player, `watchdog:${YT_NAME[String(s)] || s}`);
    }, 1600);
  }

  function isRealEnd(player) {
    try {
      const dur = player.getDuration() || 0;
      const cur = player.getCurrentTime() || 0;
      return dur >= 8 && cur >= Math.max(5, dur - 2);
    } catch {
      return false;
    }
  }

  function reducedMotion() {
    return window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  }

  function idleSlot() {
    return state.activeSlot === "a" ? "b" : "a";
  }

  function slotPlayer(slot) {
    return state.players[slot] || null;
  }

  function sleep(ms) {
    return new Promise((resolve) => setTimeout(resolve, ms));
  }

  async function waitUntil(player, test, ms) {
    const start = Date.now();
    while (Date.now() - start < ms) {
      try {
        if (player && test(player)) return true;
      } catch {
        /* player not ready */
      }
      await sleep(70);
    }
    return false;
  }

  function setVol(player, n) {
    if (!player) return;
    try {
      if (player.unMute) player.unMute();
      if (player.setVolume) player.setVolume(Math.max(0, Math.min(100, Math.round(n))));
    } catch {
      /* ignore */
    }
  }

  function probeVolume(player) {
    if (state.volumeWorks !== null || !player || !player.setVolume) return;
    try {
      const before = player.getVolume ? player.getVolume() : 100;
      player.setVolume(0);
      const after = player.getVolume ? player.getVolume() : before;
      player.setVolume(before);
      state.volumeWorks = after === 0;
    } catch {
      state.volumeWorks = false;
    }
  }

  function stopPlayer(player) {
    if (!player) return;
    try {
      if (player.pauseVideo) player.pauseVideo();
    } catch {
      /* ignore */
    }
    setVol(player, 0);
  }

  function cancelMix() {
    state.fadeGen += 1;
    state.mixing = false;
  }

  function fmt(sec) {
    if (!Number.isFinite(sec) || sec < 0) return "0:00";
    const s = Math.floor(sec);
    const m = Math.floor(s / 60);
    const r = s % 60;
    return `${m}:${r.toString().padStart(2, "0")}`;
  }

  function current() {
    return state.queue[state.index] || null;
  }

  function sequentialAvoidingRepeat(tracks) {
    const remaining = tracks.slice();
    const out = [];
    while (remaining.length) {
      const last = out.length ? out[out.length - 1].artist : null;
      const idx = remaining.findIndex((t) => t.artist !== last);
      const take = idx === -1 ? 0 : idx;
      out.push(remaining.splice(take, 1)[0]);
    }
    return out;
  }

  function buildQueue() {
    state.queue = state.catalog.slice();
    state.index = 0;
  }

  function setTheme(color) {
    document.documentElement.style.setProperty("--theme", color);
    for (const meta of el.themes) meta.setAttribute("content", color);
  }

  function crossfadeScene(id) {
    const front = state.frontHero === "a" ? el.heroA : el.heroB;
    const back = state.frontHero === "a" ? el.heroB : el.heroA;
    if (front.dataset.scene === id) return;
    back.dataset.scene = id;
    back.classList.add("is-on");
    front.classList.remove("is-on");
    state.frontHero = state.frontHero === "a" ? "b" : "a";
  }

  function setPlayingUi(on) {
    state.playing = on;
    document.body.classList.toggle("is-playing", on);
    el.play.setAttribute("aria-label", on ? "Pausar" : "Reproducir");
    el.play.setAttribute("aria-pressed", on ? "true" : "false");
  }

  function announce(text) {
    if (text === state.announced) return;
    state.announced = text;
    el.status.textContent = text;
  }

  function ytThumb(id, kind) {
    return `https://i.ytimg.com/vi/${id}/${kind}.jpg`;
  }

  function coverCandidates(track) {
    const local = track.artwork && !track.artwork.includes("ytimg.com") ? track.artwork : null;
    const listed = track.artwork && track.artwork.includes("mqdefault") ? track.artwork : null;
    return [
      local,
      listed,
      ytThumb(track.id, "mqdefault"),
      ytThumb(track.id, "hqdefault"),
    ].filter(Boolean);
  }

  function setCover(track) {
    const urls = coverCandidates(track);
    el.cover.dataset.step = "0";
    el.cover.src = urls[0];
  }

  function fallbackCover(track) {
    const urls = coverCandidates(track);
    const step = Number(el.cover.dataset.step || "0") + 1;
    if (step >= urls.length) return;
    const next = urls[step];
    if (!next || el.cover.src.includes(next)) {
      el.cover.dataset.step = String(step);
      fallbackCover(track);
      return;
    }
    el.cover.dataset.step = String(step);
    el.cover.src = next;
  }

  function paint(track) {
    if (!track) {
      el.title.textContent = "En la espera";
      el.artist.textContent = state.room;
      el.cover.removeAttribute("src");
      return;
    }
    el.title.textContent = track.title;
    el.artist.textContent = track.artist;
    setCover(track);
    el.elapsed.textContent = "0:00";
    el.duration.textContent = "0:00";
    el.seek.value = "0";
    announce(`${track.artist}. ${track.title}.`);
    document.title = `${track.title} · ${ROOMS[state.room].name}`;
  }

  function greetingFor(hour) {
    if (hour >= 5 && hour < 12) return "Buenos días";
    if (hour >= 12 && hour < 19) return "Buenas tardes";
    return "Buenas noches";
  }

  function tickClock() {
    const now = new Date();
    el.clockHi.textContent = greetingFor(now.getHours());
    el.clockTime.textContent = now.toLocaleTimeString("es-DO", {
      hour: "numeric",
      minute: "2-digit",
    });
    el.clockDate.textContent = now.toLocaleDateString("es-DO", {
      weekday: "long",
      day: "numeric",
      month: "long",
    });
  }

  function roomFromHash() {
    const id = (location.hash || "#salon").slice(1);
    return ROOMS[id] ? id : "salon";
  }

  function paintRoomChrome(id) {
    const room = ROOMS[id];
    document.body.dataset.room = id;
    setTheme(room.theme);
    el.wordmark.replaceChildren(
      ...(room.lockup || [room.name]).map((line) => {
        const span = document.createElement("span");
        span.textContent = line;
        return span;
      })
    );
    el.kicker.textContent = room.kicker;
    el.lista.href = room.lista;
    crossfadeScene(id);
    for (const a of el.rooms) {
      a.classList.toggle("is-on", a.dataset.room === id);
    }
  }

  function normalizeTracks(data) {
    const seen = new Set();
    const catalog = [];
    for (const t of (data && data.tracks) || []) {
      if (!t || !t.id || seen.has(t.id)) continue;
      if (!/^[A-Za-z0-9_-]{11}$/.test(t.id)) continue;
      seen.add(t.id);
      catalog.push({
        id: t.id,
        artist: t.artist || "",
        title: t.title || "",
        youtube: t.youtube || `https://www.youtube.com/watch?v=${t.id}`,
        artwork: t.artwork || `https://i.ytimg.com/vi/${t.id}/mqdefault.jpg`,
        artworkLarge: t.artworkLarge || t.artwork || `https://i.ytimg.com/vi/${t.id}/mqdefault.jpg`,
      });
    }
    return { catalog, loop: !data || data.loop !== false };
  }

  async function fetchRoom(id) {
    if (state.catalogs[id]) return state.catalogs[id];
    const room = ROOMS[id];
    const res = await fetch(room.tracks, { cache: "no-store" });
    if (!res.ok) throw new Error(String(res.status));
    const parsed = normalizeTracks(await res.json());
    state.catalogs[id] = parsed;
    return parsed;
  }

  function prefetchRooms() {
    for (const id of Object.keys(ROOMS)) {
      if (state.catalogs[id]) continue;
      fetchRoom(id).catch(() => {});
    }
  }

  async function loadRoom(id, autoplay) {
    const room = ROOMS[id];
    if (!room) return;
    if (id === state.room) {
      if (state.catalog.length) {
        if (autoplay) await playCurrent();
        return;
      }
      if (state.loadGen) return;
    }
    const gen = ++state.loadGen;
    const fromRoom = state.room;
    state.room = id;
    paintRoomChrome(id);
    let parsed;
    try {
      parsed = await fetchRoom(id);
    } catch {
      if (gen !== state.loadGen) return;
      announce("No se pudo cargar la lista.");
      return;
    }
    if (gen !== state.loadGen) return;
    state.catalog = parsed.catalog;
    state.loop = parsed.loop;
    buildQueue();
    paint(current());
    if (autoplay && current()) {
      state.wanted = "play";
      const live = state.playing || ytState() === 1;
      if (live && fromRoom !== id) await mixInto(current(), gen);
      else await ensurePlayer();
    }
  }

  function ytState(player) {
    const p = player || state.player;
    if (!p || !p.getPlayerState) return -1;
    try {
      return p.getPlayerState();
    } catch {
      return -1;
    }
  }

  function audiblePlayer() {
    if (state.mixing) {
      const incoming = slotPlayer(idleSlot());
      if (incoming && ytState(incoming) === 1) return incoming;
    }
    return state.player;
  }

  function readTime() {
    const player = audiblePlayer();
    if (!player || state.seeking) return;
    let cur = 0;
    let dur = 0;
    try {
      cur = player.getCurrentTime() || 0;
      dur = player.getDuration() || 0;
    } catch {
      return;
    }
    state.duration = dur;
    el.elapsed.textContent = fmt(cur);
    el.duration.textContent = fmt(dur);
    el.seek.disabled = dur <= 0;
    if (dur > 0) el.seek.value = String(Math.round((cur / dur) * 1000));
  }

  function startPoll() {
    if (state.poll) return;
    state.poll = setInterval(readTime, POLL_MS);
  }

  function hideIframe(player) {
    const p = player || state.player;
    if (!p || !p.getIframe) return;
    const iframe = p.getIframe();
    if (!iframe) return;
    iframe.setAttribute("tabindex", "-1");
    iframe.setAttribute("aria-hidden", "true");
    iframe.style.pointerEvents = "none";
    iframe.style.width = "480px";
    iframe.style.height = "270px";
  }

  function onPlayerState(slot, event) {
    const YTref = window.YT;
    if (!YTref) return;
    const isActive = slot === state.activeSlot;
    dbg(`yt:${YT_NAME[String(event.data)] || event.data}`, isActive ? "live" : "idle");
    if (event.data === YTref.PlayerState.PLAYING) {
      state.nudgeCount = 0;
      state.startedAt = Date.now();
      if (current()) state.failHits[current().id] = 0;
      if (state.mixing && !isActive) {
        setPlayingUi(true);
        startPoll();
        readTime();
        return;
      }
      if (isActive && !state.mixing) {
        setPlayingUi(true);
        state.wanted = "play";
        startPoll();
        readTime();
        syncMediaSession();
      }
    } else if (event.data === YTref.PlayerState.PAUSED) {
      if (isActive && !state.mixing && state.wanted === "play") {
        dbg("fake-pause", "resume");
        nudgePlay(event.target, "pause");
        return;
      }
      if (isActive && !state.mixing) {
        setPlayingUi(false);
        state.wanted = "pause";
        readTime();
      }
    } else if (event.data === YTref.PlayerState.ENDED) {
      if (isActive && !state.mixing) {
        if (isRealEnd(event.target)) {
          dbg("real-end", "");
          go(1, { fromEnd: true });
        } else if (state.wanted === "play") {
          dbg("fake-end", "resume");
          nudgePlay(event.target, "ended");
        }
      }
    } else if (event.data === YTref.PlayerState.CUED && state.wanted === "play") {
      const p = slotPlayer(slot);
      if (p && (isActive || state.mixing)) {
        try {
          p.playVideo();
        } catch {
          /* ignore */
        }
      }
    }
  }

  function videoIdOf(player) {
    try {
      const data = player && player.getVideoData ? player.getVideoData() : null;
      return (data && data.video_id) || null;
    } catch {
      return null;
    }
  }

  function failForward(reason) {
    const track = current();
    if (!track) return;
    const now = Date.now();
    if (now - state.lastFailAt < 1500) {
      dbg("fail-dup", reason);
      return;
    }
    state.lastFailAt = now;
    const hits = (state.failHits[track.id] || 0) + 1;
    state.failHits[track.id] = hits;
    dbg("fail", `${reason} ${hits}`);
    if (hits < 3) {
      const player = state.player;
      if (player && player.loadVideoById) {
        state.loadedAt = Date.now();
        try {
          player.loadVideoById(track.id);
          setVol(player, state.masterVolume);
          player.playVideo();
        } catch {
          /* ignore */
        }
      }
      return;
    }
    if (state.advancing) return;
    dbg("skip", reason);
    announce(`No se pudo reproducir ${track.title}.`);
    go(1, { fromEnd: true });
  }

  function onPlayerError(slot) {
    const player = slotPlayer(slot);
    const vid = videoIdOf(player);
    if (slot !== state.activeSlot) {
      if (state.mixing && state.expectIncoming && vid === state.expectIncoming) {
        failForward("incoming-error");
      }
      return;
    }
    if (state.mixing) return;
    failForward("active-error");
  }

  function createPlayer(slot, videoId) {
    const player = new window.YT.Player(`yt-player-${slot}`, {
      width: 480,
      height: 270,
      videoId,
      host: "https://www.youtube.com",
      playerVars: {
        autoplay: slot === state.activeSlot ? 1 : 0,
        controls: 0,
        disablekb: 1,
        fs: 0,
        modestbranding: 1,
        rel: 0,
        playsinline: 1,
        iv_load_policy: 3,
        origin: location.origin,
      },
      events: {
        onReady(event) {
          hideIframe(event.target);
          const incoming = slot !== state.activeSlot;
          setVol(event.target, incoming ? 0 : 100);
          if (state.wanted === "play" && !incoming) {
            setVol(event.target, state.masterVolume);
            event.target.playVideo();
          }
        },
        onStateChange: (event) => onPlayerState(slot, event),
        onError: (event) => onPlayerError(slot, event),
      },
    });
    state.players[slot] = player;
    if (slot === state.activeSlot) state.player = player;
    hideIframe(player);
    return player;
  }

  function loadApi() {
    if (state.apiReady) return Promise.resolve();
    if (state.apiLoading) return state.apiLoading;
    state.apiLoading = new Promise((resolve) => {
      const ready = () => {
        state.apiReady = true;
        resolve();
      };
      if (window.YT && window.YT.Player) {
        ready();
        return;
      }
      const prev = window.onYouTubeIframeAPIReady;
      window.onYouTubeIframeAPIReady = () => {
        if (typeof prev === "function") prev();
        ready();
      };
      const tag = document.createElement("script");
      tag.src = "https://www.youtube.com/iframe_api";
      tag.async = true;
      tag.onerror = () => {
        state.apiLoading = null;
        announce("No se pudo abrir YouTube.");
      };
      document.head.appendChild(tag);
    });
    return state.apiLoading;
  }

  async function ensurePlayer() {
    const track = current();
    if (!track) return;
    await loadApi();
    if (!state.player) {
      state.loadedAt = Date.now();
      createPlayer(state.activeSlot, track.id);
      return;
    }
    const loaded = state.player.getVideoData ? state.player.getVideoData() : null;
    if (!loaded || loaded.video_id !== track.id) {
      state.loadedAt = Date.now();
      state.player.loadVideoById(track.id);
      if (state.wanted === "play") state.player.playVideo();
    } else if (state.wanted === "play") {
      state.player.playVideo();
    }
    setVol(state.player, state.masterVolume);
    hideIframe(state.player);
  }

  async function rampTo(player, fromV, toV, ms, token) {
    const t0 = performance.now();
    return new Promise((resolve) => {
      const frame = (now) => {
        if (token !== state.fadeGen) {
          resolve(false);
          return;
        }
        const t = Math.min(1, (now - t0) / Math.max(1, ms));
        const curved = fromV > toV
          ? Math.cos(t * Math.PI * 0.5)
          : Math.sin(t * Math.PI * 0.5);
        const lo = Math.min(fromV, toV);
        const hi = Math.max(fromV, toV);
        setVol(player, lo + (hi - lo) * curved);
        if (t < 1) requestAnimationFrame(frame);
        else {
          setVol(player, toV);
          resolve(true);
        }
      };
      requestAnimationFrame(frame);
    });
  }

  async function cueIncoming(track) {
    const slot = idleSlot();
    await loadApi();
    let incoming = slotPlayer(slot);
    if (!incoming) incoming = createPlayer(slot, track.id);
    else {
      try {
        if (incoming.cueVideoById) incoming.cueVideoById(track.id);
        else incoming.loadVideoById(track.id);
      } catch {
        return { slot, incoming: null };
      }
    }
    setVol(incoming, 0);
    hideIframe(incoming);
    try {
      if (incoming.pauseVideo) incoming.pauseVideo();
    } catch {
      /* idle must not play under the outgoing song */
    }
    state.expectIncoming = track.id;
    await waitUntil(incoming, (p) => typeof p.playVideo === "function", 1500);
    return { slot, incoming };
  }

  function adoptIncoming(slot, incoming) {
    const outgoing = state.player;
    state.activeSlot = slot;
    state.player = incoming;
    setVol(incoming, 100);
    stopPlayer(outgoing);
    setVol(outgoing, 100);
    hideIframe(incoming);
    setPlayingUi(true);
    startPoll();
    readTime();
    syncMediaSession();
  }

  function skipIncoming() {
    const now = Date.now();
    if (now - state.lastFailAt < 700) return;
    state.lastFailAt = now;
    const len = state.queue.length;
    if (len < 2) return;
    let next = state.index + 1;
    if (next >= len) next = state.loop ? 0 : state.index;
    if (next === state.index) return;
    state.index = next;
    const track = current();
    paint(track);
    state.expectIncoming = track ? track.id : null;
    const incoming = slotPlayer(idleSlot());
    if (!track || !incoming) return;
    try {
      incoming.loadVideoById(track.id);
      incoming.playVideo();
    } catch {
      /* ignore */
    }
    setVol(incoming, 0);
  }

  async function mixInto(track, gen) {
    if (!track) return;
    if (gen !== state.loadGen) return;
    const outgoing = state.player;
    if (!outgoing) {
      await ensurePlayer();
      return;
    }

    cancelMix();
    const token = state.fadeGen;
    state.mixing = true;
    const outMs = reducedMotion() ? FADE_REDUCED_MS : FADE_OUT_MS;
    const inMs = reducedMotion() ? FADE_REDUCED_MS : FADE_IN_MS;

    const { slot, incoming } = await cueIncoming(track);
    if (token !== state.fadeGen || gen !== state.loadGen) return;

    const fadedOut = state.volumeWorks === false
      ? true
      : await rampTo(outgoing, state.masterVolume, 0, outMs, token);
    if (!fadedOut || token !== state.fadeGen || gen !== state.loadGen) return;
    stopPlayer(outgoing);

    if (!incoming) {
      state.mixing = false;
      setVol(outgoing, state.masterVolume);
      await ensurePlayer();
      return;
    }

    setVol(incoming, 0);
    try {
      incoming.playVideo();
    } catch {
      /* ignore */
    }
    const started = await waitUntil(incoming, (p) => p.getPlayerState() === 1, 4000);
    if (token !== state.fadeGen || gen !== state.loadGen) return;
    if (!started) {
      skipIncoming();
      const retry = current();
      if (retry && retry.id !== track.id) {
        try {
          incoming.loadVideoById(retry.id);
          incoming.playVideo();
        } catch {
          /* ignore */
        }
        const ok = await waitUntil(incoming, (p) => p.getPlayerState() === 1, 3500);
        if (!ok || token !== state.fadeGen) {
          state.mixing = false;
          setVol(outgoing, state.masterVolume);
          try {
            outgoing.playVideo();
          } catch {
            /* keep whatever is audible */
          }
          return;
        }
      } else {
        state.mixing = false;
        setVol(outgoing, state.masterVolume);
        try {
          outgoing.playVideo();
        } catch {
          /* ignore */
        }
        return;
      }
    }

    setPlayingUi(true);
    startPoll();
    if (state.volumeWorks !== false) {
      setVol(incoming, 0);
      const fadedIn = await rampTo(incoming, 0, state.masterVolume, inMs, token);
      if (!fadedIn || token !== state.fadeGen) return;
    } else {
      setVol(incoming, state.masterVolume);
    }
    if (token !== state.fadeGen || gen !== state.loadGen) return;
    adoptIncoming(slot, incoming);
    state.expectIncoming = null;
    state.mixing = false;
  }

  async function playCurrent() {
    const track = current();
    if (!track) return;
    state.wanted = "play";
    paint(track);
    try {
      await ensurePlayer();
    } catch {
      announce("No se pudo abrir YouTube.");
      setPlayingUi(false);
    }
    syncMediaSession();
  }

  function pauseCurrent() {
    state.wanted = "pause";
    if (state.mixing) {
      const incoming = slotPlayer(idleSlot());
      if (incoming) adoptIncoming(idleSlot(), incoming);
      cancelMix();
    }
    setPlayingUi(false);
    if (state.player && state.player.pauseVideo) state.player.pauseVideo();
    const other = slotPlayer(idleSlot());
    stopPlayer(other);
  }

  async function togglePlay() {
    if (state.playing || (state.player && ytState() === 1)) {
      pauseCurrent();
      return;
    }
    await playCurrent();
  }

  async function go(step, opts = {}) {
    const fromEnd = Boolean(opts.fromEnd);
    const len = state.queue.length;
    if (!len) return;
    if (fromEnd && state.advancing) return;
    if (fromEnd) state.advancing = true;
    if (state.mixing) {
      const incoming = slotPlayer(idleSlot());
      if (incoming && ytState(incoming) === 1) adoptIncoming(idleSlot(), incoming);
      cancelMix();
    }

    if (step < 0 && state.player && !fromEnd) {
      let cur = 0;
      const player = audiblePlayer();
      try {
        cur = player && player.getCurrentTime ? player.getCurrentTime() || 0 : 0;
      } catch {
        cur = 0;
      }
      if (cur > RESTART_SEC) {
        player.seekTo(0, true);
        if (state.wanted === "play") player.playVideo();
        return;
      }
    }

    let next = state.index + step;
    if (next >= len) {
      if (!state.loop && fromEnd) {
        state.wanted = "pause";
        setPlayingUi(false);
        state.advancing = false;
        return;
      }
      buildQueue();
      next = 0;
    } else if (next < 0) {
      next = state.loop ? len - 1 : 0;
    }
    state.index = next;
    paint(current());
    try {
      if (state.wanted === "play" || fromEnd) {
        state.wanted = "play";
        await ensurePlayer();
      }
      syncMediaSession();
    } finally {
      if (fromEnd) state.advancing = false;
    }
  }

  function syncMediaSession() {
    if (!("mediaSession" in navigator)) return;
    const track = current();
    if (!track) return;
    navigator.mediaSession.metadata = new MediaMetadata({
      title: track.title,
      artist: track.artist,
      album: ROOMS[state.room].name,
      artwork: [
        { src: track.artwork, sizes: "480x360", type: "image/jpeg" },
        { src: track.artworkLarge || track.artwork, sizes: "1280x720", type: "image/jpeg" },
      ],
    });
    navigator.mediaSession.playbackState = state.playing ? "playing" : "paused";
  }

  function startPresence() {
    const channel = "bes-presence";
    const id = `${Date.now()}-${Math.random().toString(36).slice(2, 8)}`;
    const peers = new Map();
    const bc = "BroadcastChannel" in window ? new BroadcastChannel(channel) : null;

    function render() {
      el.online.textContent = String(1 + peers.size);
    }

    function ping() {
      if (bc) bc.postMessage({ type: "here", id });
    }

    if (bc) {
      bc.onmessage = (event) => {
        const msg = event.data || {};
        if (!msg.id || msg.id === id) return;
        if (msg.type === "here" || msg.type === "hello") {
          peers.set(msg.id, Date.now());
          if (msg.type === "hello") ping();
          render();
        }
        if (msg.type === "bye") {
          peers.delete(msg.id);
          render();
        }
      };
      bc.postMessage({ type: "hello", id });
      ping();
      setInterval(() => {
        const cut = Date.now() - 8000;
        for (const [peer, at] of peers) {
          if (at < cut) peers.delete(peer);
        }
        ping();
        render();
      }, 2500);
      window.addEventListener("pagehide", () => {
        bc.postMessage({ type: "bye", id });
      });
    }
    render();
  }

  function bind() {
    const arm = () => {
      state.armed = true;
    };
    document.addEventListener("pointerdown", arm, { once: true });
    window.addEventListener("keydown", (event) => {
      if (event.key === "D" && event.shiftKey && !event.metaKey && !event.ctrlKey && !event.altKey) {
        event.preventDefault();
        setDebug(!state.debug);
      }
    });
    if (el.dbgClose) {
      el.dbgClose.addEventListener("click", () => setDebug(false));
    }
    el.play.addEventListener("click", () => {
      arm();
      togglePlay();
    });
    el.prev.addEventListener("click", () => {
      if (state.wanted === "idle") state.wanted = "play";
      go(-1);
    });
    el.next.addEventListener("click", () => {
      if (state.wanted === "idle") state.wanted = "play";
      go(1);
    });
    el.seek.addEventListener("pointerdown", () => {
      state.seeking = true;
    });
    el.seek.addEventListener("pointerup", () => {
      state.seeking = false;
    });
    el.seek.addEventListener("change", () => {
      const player = audiblePlayer();
      if (!player || !state.duration) return;
      const t = (Number(el.seek.value) / 1000) * state.duration;
      player.seekTo(t, true);
      el.elapsed.textContent = fmt(t);
      state.seeking = false;
    });
    el.cover.addEventListener("load", () => {
      if (el.cover.naturalWidth && el.cover.naturalWidth <= 120) {
        const track = current();
        if (track) fallbackCover(track);
      }
    });
    el.cover.addEventListener("error", () => {
      const track = current();
      if (track) fallbackCover(track);
    });
    for (const a of el.rooms) {
      a.addEventListener("click", () => {
        const id = a.dataset.room;
        if (!ROOMS[id]) return;
        state.armed = true;
        if (id !== state.room) loadRoom(id, true);
      });
    }
    window.addEventListener("hashchange", () => {
      const next = roomFromHash();
      if (next !== state.room) loadRoom(next, state.armed);
    });
    if ("mediaSession" in navigator) {
      const bindSession = (action, handler) => {
        try {
          navigator.mediaSession.setActionHandler(action, handler);
        } catch {
          /* unsupported */
        }
      };
      bindSession("play", () => playCurrent());
      bindSession("pause", () => pauseCurrent());
      bindSession("previoustrack", () => go(-1));
      bindSession("nexttrack", () => go(1));
    }
  }

  async function boot() {
    bind();
    tickClock();
    setInterval(tickClock, 1000);
    startPresence();
    startWatchdog();
    setDebug(debugOn());
    await loadRoom(roomFromHash(), false);
    prefetchRooms();
  }

  boot();
})();
