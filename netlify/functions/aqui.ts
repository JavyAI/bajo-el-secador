import { getStore } from "@netlify/blobs";
import type { Config } from "@netlify/functions";

const TTL_MS = 20000;

function prune(map: Record<string, number>, now: number) {
  const live: Record<string, number> = {};
  for (const [id, ts] of Object.entries(map || {})) {
    if (now - Number(ts) < TTL_MS) live[id] = Number(ts);
  }
  return live;
}

export default async (req: Request) => {
  if (req.method === "OPTIONS") {
    return new Response("", {
      status: 204,
      headers: {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET,POST,OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type",
      },
    });
  }

  const store = getStore({ name: "aqui", consistency: "strong" });
  const now = Date.now();
  let map = (await store.get("heartbeats", { type: "json" })) as Record<string, number> | null;
  if (!map || typeof map !== "object" || Array.isArray(map)) map = {};

  if (req.method === "POST") {
    let id = "";
    try {
      const body = (await req.json()) as { id?: string };
      id = String(body && body.id ? body.id : "").slice(0, 80);
    } catch {
      id = "";
    }
    if (!id) {
      return Response.json({ error: "id" }, { status: 400 });
    }
    map[id] = now;
  }

  const live = prune(map, now);
  await store.setJSON("heartbeats", live);

  return Response.json(
    { n: Object.keys(live).length },
    {
      headers: {
        "Cache-Control": "no-store",
        "Access-Control-Allow-Origin": "*",
      },
    }
  );
};

export const config: Config = {
  path: "/api/aqui",
  method: ["GET", "POST", "OPTIONS"],
};
