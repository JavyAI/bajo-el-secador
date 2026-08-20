(() => {
  const SAVE = "http://localhost:8878/select";
  const KEY = "secador-plate-picks";

  const el = {
    chips: document.getElementById("chips"),
    rooms: document.getElementById("rooms"),
    picks: document.getElementById("picks"),
    lock: document.getElementById("lock"),
    count: document.getElementById("lock-count"),
    status: document.getElementById("status"),
    lightbox: document.getElementById("lightbox"),
    lightboxImg: document.getElementById("lightbox-img"),
  };

  let catalog = { rooms: [] };
  let picks = {};

  function loadPicks() {
    try {
      picks = JSON.parse(localStorage.getItem(KEY) || "{}") || {};
    } catch {
      picks = {};
    }
  }

  function saveLocal() {
    localStorage.setItem(KEY, JSON.stringify(picks));
  }

  function pickedCount() {
    return catalog.rooms.filter((room) => picks[room.id]).length;
  }

  function findImage(roomId, imageId) {
    const room = catalog.rooms.find((r) => r.id === roomId);
    return room ? room.images.find((img) => img.id === imageId) : null;
  }

  function renderChips() {
    el.chips.replaceChildren(
      ...catalog.rooms.map((room) => {
        const a = document.createElement("a");
        a.href = `#${room.id}`;
        a.textContent = room.name.replace("En el ", "").replace("En la ", "");
        if (picks[room.id]) a.classList.add("is-picked");
        return a;
      })
    );
  }

  function renderRooms() {
    el.rooms.replaceChildren(
      ...catalog.rooms.map((room) => {
        const section = document.createElement("section");
        section.className = "room";
        section.id = room.id;

        const head = document.createElement("div");
        head.className = "room__head";
        const titles = document.createElement("div");
        const h2 = document.createElement("h2");
        h2.className = "room__name";
        h2.textContent = room.name;
        const meta = document.createElement("p");
        meta.className = "room__meta";
        meta.textContent = `${room.kicker} · ${room.conversation} · ${room.images.length} plates`;
        titles.append(h2, meta);
        head.append(titles);

        const grid = document.createElement("div");
        grid.className = "grid";
        for (const image of room.images) {
          grid.append(card(room, image));
        }
        section.append(head, grid);
        return section;
      })
    );
  }

  function card(room, image) {
    const btn = document.createElement("button");
    btn.type = "button";
    btn.className = "card";
    btn.dataset.room = room.id;
    btn.dataset.id = image.id;
    if (image.wired) btn.classList.add("is-wired");
    if (picks[room.id] === image.id) btn.classList.add("is-on");

    const img = document.createElement("img");
    img.src = image.thumb;
    img.alt = image.label;
    img.loading = "lazy";

    const cap = document.createElement("div");
    cap.className = "card__cap";
    const name = document.createElement("span");
    name.className = "card__name";
    name.textContent = image.label;
    const size = document.createElement("span");
    size.textContent = `${image.w}×${image.h}`;
    cap.append(name, size);

    if (image.wired || picks[room.id] === image.id) {
      const badge = document.createElement("span");
      badge.className = "badge";
      badge.textContent = picks[room.id] === image.id ? "Tu pick" : "En el site";
      btn.append(badge);
    }

    btn.append(img, cap);
    btn.addEventListener("click", (event) => {
      if (event.altKey || event.metaKey) {
        el.lightboxImg.src = image.src;
        el.lightboxImg.alt = image.label;
        el.lightbox.showModal();
        return;
      }
      picks[room.id] = image.id;
      saveLocal();
      paint();
    });
    return btn;
  }

  function renderDock() {
    el.picks.replaceChildren(
      ...catalog.rooms.map((room) => {
        const wrap = document.createElement("button");
        wrap.type = "button";
        wrap.title = room.name;
        wrap.addEventListener("click", () => {
          document.getElementById(room.id)?.scrollIntoView({ behavior: "smooth" });
        });
        const picked = findImage(room.id, picks[room.id]);
        if (picked) {
          const img = document.createElement("img");
          img.src = picked.thumb;
          img.alt = room.name;
          wrap.append(img);
        } else {
          const empty = document.createElement("span");
          empty.className = "empty";
          empty.textContent = room.name.split(" ").pop();
          wrap.append(empty);
        }
        return wrap;
      })
    );
    const n = pickedCount();
    el.count.textContent = String(n);
    el.lock.disabled = n !== catalog.rooms.length;
  }

  function paint() {
    renderChips();
    renderRooms();
    renderDock();
  }

  function payload() {
    const rooms = {};
    for (const room of catalog.rooms) {
      const image = findImage(room.id, picks[room.id]);
      if (!image) continue;
      rooms[room.id] = {
        file: image.file,
        abs: image.abs,
        src: image.src,
        thumb: image.thumb,
        conversation: room.conversation,
      };
    }
    return { lockedAt: new Date().toISOString(), rooms };
  }

  async function lockIn() {
    const data = payload();
    el.status.hidden = false;
    try {
      const res = await fetch(SAVE, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data),
      });
      if (!res.ok) throw new Error(String(res.status));
      el.status.textContent = "Locked. Tell me to wire these and I’ll put them on the site.";
    } catch {
      const blob = new Blob([JSON.stringify(data, null, 2)], { type: "application/json" });
      const a = document.createElement("a");
      a.href = URL.createObjectURL(blob);
      a.download = "selection.json";
      a.click();
      el.status.textContent = "Saved a selection.json download. Tell me to wire these.";
    }
  }

  el.lock.addEventListener("click", () => {
    if (!el.lock.disabled) lockIn();
  });

  fetch("catalog.json")
    .then((res) => res.json())
    .then((data) => {
      catalog = data;
      loadPicks();
      paint();
    });
})();
