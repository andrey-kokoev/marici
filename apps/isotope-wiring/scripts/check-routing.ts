import { neon20 } from "../src/examples/neon20.js";
import { syntheticExample } from "../src/examples/synthetic.js";
import { traceRoute } from "../src/domain/route.js";
import { DiagramDocumentSchema } from "../src/schemas/document.js";
import { createPinia, setActivePinia } from "pinia";
import { ROUTE_EDGE_MS, useInspection } from "../src/vue/stores/inspection.js";
import { useDiagramInspection } from "../src/vue/useDiagramInspection.js";
import { pointAtFraction } from "../src/presentation/diagram.js";
function expect(value: boolean, message: string): void {
  if (!value) throw new Error(message);
}
const document = neon20(),
  original = JSON.stringify(document);
for (const preference of ["left", "right"] as const) {
  const throughCenter = traceRoute(document, "edge.ne20.26", preference, true);
  expect(
    throughCenter.steps[1]?.edgeId === "edge.ne20.25" &&
      throughCenter.steps[1]?.pendingTurn === preference,
    "26 must continue straight to green 25 before turning to 23/24, preserving the pending turn",
  );
}
const greenThroughColor = DiagramDocumentSchema.parse({
  ...document,
  layout: {
    ...document.layout,
    edges: document.layout.edges.map((edge) =>
      edge.edgeId === "edge.ne20.19" ? { ...edge, color: "red" } : edge,
    ),
  },
  graph: {
    ...document.graph,
    edges: document.graph.edges.map((edge) =>
      ["edge.ne20.19", "edge.ne20.21", "edge.ne20.15"].includes(edge.id)
        ? { ...edge, direction: "to-from" }
        : edge,
    ),
  },
});
expect(
  traceRoute(greenThroughColor, "edge.ne20.8")
    .steps.slice(3, 8)
    .map((step) => step.edgeId)
    .join(",") === "edge.ne20.3,edge.ne20.19,edge.ne20.26,edge.ne20.25,edge.ne20.15",
  "26 must continue to 25 then eligible 15, not exit onto eligible red 21",
);
// Last red 14 arrives at bottom-left. Both green 6 and 17 are available;
// Outward blue 18 must outrank green at the handoff too.
const lastRed14 = DiagramDocumentSchema.parse({
  ...document,
  graph: {
    ...document.graph,
    edges: document.graph.edges.map((edge) =>
      ["edge.ne20.14", "edge.ne20.15"].includes(edge.id) ? { ...edge, direction: "to-from" } : edge,
    ),
  },
  layout: {
    ...document.layout,
    edges: document.layout.edges.map((edge) => ({
      ...edge,
      color: edge.edgeId === "edge.ne20.14" ? "red" : edge.color === "green" ? "green" : "blue",
    })),
  },
});
const switchedAt14 = traceRoute(lastRed14, "edge.ne20.14", "left");
expect(
  switchedAt14.steps[0]?.pendingTurn === "right" &&
    switchedAt14.steps[1]?.edgeId === "edge.ne20.18",
  "The turn flips, but eligible own-blue 18 still outranks green 6",
);
const inward18 = DiagramDocumentSchema.parse({
  ...lastRed14,
  graph: {
    ...lastRed14.graph,
    edges: lastRed14.graph.edges.map((edge) =>
      edge.id === "edge.ne20.18" ? { ...edge, direction: "to-from" } : edge,
    ),
  },
});
expect(
  traceRoute(inward18, "edge.ne20.14", "left").steps[1]?.edgeId === "edge.ne20.6",
  "14 selects green 6 when blue 18 is not direction-eligible",
);
// Balanced minimal color phase: 13 is the last red, 14 the blue continuation.
// Green 24 is more-left at the tip but must not steal the newly active blue exit.
const lastRed13 = DiagramDocumentSchema.parse({
  ...document,
  graph: {
    ...document.graph,
    edges: document.graph.edges.map((edge) =>
      edge.id === "edge.ne20.14" ? { ...edge, direction: "to-from" } : edge,
    ),
  },
  layout: {
    ...document.layout,
    edges: document.layout.edges.map((edge) => ({
      ...edge,
      color:
        edge.edgeId === "edge.ne20.13" ? "red" : edge.edgeId === "edge.ne20.14" ? "blue" : "green",
    })),
  },
});
const switchedAt13 = traceRoute(lastRed13, "edge.ne20.13", "right");
expect(
  switchedAt13.status === "completed" &&
    switchedAt13.colorBalance.balanced &&
    switchedAt13.steps[0]?.pendingTurn === "left" &&
    switchedAt13.steps[1]?.edgeId === "edge.ne20.14",
  "At the phase switch, 13 must choose eligible blue 14 before more-left green 24",
);
// Operator's balanced configuration reproduces the reported 14 → 17 defect
// unless the phase change flips the preference exactly once.
const operatorPhase = DiagramDocumentSchema.parse({
  ...document,
  graph: {
    ...document.graph,
    edges: document.graph.edges.map((edge) =>
      ["edge.ne20.19", "edge.ne20.15", "edge.ne20.21", "edge.ne20.14"].includes(edge.id)
        ? { ...edge, direction: "to-from" }
        : edge,
    ),
  },
  layout: {
    ...document.layout,
    edges: document.layout.edges.map((edge) => ({
      ...edge,
      color:
        edge.color === "green"
          ? "green"
          : [
                "edge.ne20.8",
                "edge.ne20.10",
                "edge.ne20.3",
                "edge.ne20.19",
                "edge.ne20.15",
                "edge.ne20.18",
                "edge.ne20.21",
                "edge.ne20.13",
              ].includes(edge.edgeId)
            ? "red"
            : "blue",
    })),
  },
});
const phasePath = traceRoute(operatorPhase, "edge.ne20.8");
expect(
  phasePath.colorBalance.balanced &&
    phasePath.steps
      .slice(0, 15)
      .map((step) => step.edgeId.replace("edge.ne20.", ""))
      .join(",") === "8,12,10,3,19,26,25,15,18,21,7,22,13,14,6",
  "The reported balanced path must retain its prefix and continue 13 → 14 → 6",
);
expect(
  phasePath.steps[12]?.pendingTurn === "right" && phasePath.steps[13]?.pendingTurn === "right",
  "The phase-switch preference must not immediately flip back on 13 → 14",
);
const path = traceRoute(document, "edge.ne20.8");
const outward19 = DiagramDocumentSchema.parse({
  ...document,
  layout: {
    ...document.layout,
    edges: document.layout.edges.map((edge) =>
      edge.edgeId === "edge.ne20.19" ? { ...edge, color: "red" } : edge,
    ),
  },
  graph: {
    ...document.graph,
    edges: document.graph.edges.map((edge) =>
      edge.id === "edge.ne20.19" ? { ...edge, direction: "to-from" } : edge,
    ),
  },
});
expect(
  traceRoute(outward19, "edge.ne20.8").steps[4]?.edgeId === "edge.ne20.19",
  "Direction-eligible red 19 must outrank green 7 after red 3",
);
expect(
  path.steps
    .slice(0, 4)
    .map((step) => step.edgeId)
    .join(",") === "edge.ne20.8,edge.ne20.12,edge.ne20.10,edge.ne20.3",
  "Required 8 → 12 → 10 → 3 route failed",
);
expect(
  path.steps
    .slice(0, 4)
    .map((step) => step.pendingTurn)
    .join(",") === "left,right,left,right",
  "Turns did not alternate",
);
expect(
  path.steps[4]?.edgeId === "edge.ne20.7" &&
    path.steps[4].from === "vertex.middle-right" &&
    path.steps[4].to === "vertex.middle-left",
  "3 must continue along undirected 7, not 2",
);
for (const number of [6, 7, 12, 17, 22, 23, 24, 25, 26, 27]) {
  const id = `edge.ne20.${number}`;
  expect(
    document.graph.edges.find((edge) => edge.id === id)?.direction === "undirected",
    "Green segment must be undirected",
  );
  const forward = traceRoute(document, id),
    backward = traceRoute(document, id, "left", true);
  expect(
    forward.steps[0]?.from === backward.steps[0]?.to &&
      forward.steps[0]?.to === backward.steps[0]?.from &&
      backward.steps.length > 0,
    "Undirected start must allow both orientations",
  );
}
expect(
  document.layout.aliases.length === 26 &&
    document.layout.aliases
      .map((value) => value.number)
      .sort((a, b) => a - b)
      .every((value, index) => value === index + (index < 4 ? 1 : 2)),
  "Keep labels 1–27 except retired 5; do not renumber",
);
expect(
  document.graph.vertices.length === 12 && document.graph.edges.length === 26,
  "Adding top-shell connector 27 must not create a crossing vertex",
);
const topBar = document.graph.edges.find((edge) => edge.id === "edge.ne20.27");
expect(
  topBar?.from === "vertex.upper-tip" &&
    topBar.to === "vertex.top-junction" &&
    topBar.direction === "undirected" &&
    document.layout.edges.find((edge) => edge.edgeId === topBar.id)?.color === "green",
  "Top-shell bar must be an undirected green edge between the existing tips",
);
const horizontalTop = traceRoute(document, "edge.ne20.12");
expect(
  horizontalTop.steps[0]?.to === "vertex.upper-right" &&
    horizontalTop.steps[1]?.edgeId !== "edge.ne20.27",
  "The crossing of 12 and 27 must not create incidence",
);
for (const number of [23, 24, 25, 26]) {
  const edge = document.graph.edges.find((value) => value.id === `edge.ne20.${number}`);
  const from =
    number === 23 ? "vertex.top-junction" : number === 25 ? "vertex.left-tip" : "vertex.center";
  const to =
    number === 24 ? "vertex.bottom-tip" : number === 26 ? "vertex.right-tip" : "vertex.center";
  expect(
    edge?.from === from && edge.to === to && edge.direction === "undirected",
    `Wrong shell-2 diagonal ${number}`,
  );
  expect(
    document.layout.edges.find((value) => value.edgeId === `edge.ne20.${number}`)?.color ===
      "green",
    `Diagonal ${number} must be green`,
  );
}
function unchangedShell1(label: number, from: string, to: string, color: string): void {
  const edge = document.graph.edges.find((value) => value.id === `edge.ne20.${label}`);
  expect(
    edge?.from === from &&
      edge.to === to &&
      edge.direction === "from-to" &&
      document.layout.edges.find((value) => value.edgeId === edge.id)?.color === color,
    "Shell 1 must remain unchanged",
  );
}
unchangedShell1(8, "vertex.upper-tip", "vertex.upper-left", "red");
unchangedShell1(9, "vertex.upper-right", "vertex.upper-tip", "blue");
unchangedShell1(10, "vertex.upper-right", "vertex.top-junction", "red");
unchangedShell1(11, "vertex.top-junction", "vertex.upper-left", "blue");
for (const label of [2, 4]) {
  const edge = document.graph.edges.find((value) => value.id === `edge.ne20.${label}`);
  const from = "vertex.center";
  const to = label === 2 ? "vertex.middle-right" : "vertex.bottom-right";
  expect(
    edge?.from === from && edge.to === to && edge.direction === "from-to",
    `Edge ${label} direction was not reversed`,
  );
  expect(
    document.layout.edges.find((value) => value.edgeId === `edge.ne20.${label}`)?.color ===
      (label === 2 ? "blue" : "red"),
    `Edge ${label} must follow the shell-2 color rule`,
  );
  const route = traceRoute(document, `edge.ne20.${label}`);
  expect(
    route.steps[0]?.from === from && route.steps[0].to === to,
    `Routing ignores edge ${label} reversal`,
  );
  expect(
    traceRoute(document, `edge.ne20.${label}`, "left", true).status === "invalid-start",
    `Edge ${label} still permits the old direction`,
  );
}
for (const label of [1, 2, 3, 4, 13, 14, 15, 16, 18, 19, 20, 21]) {
  const edge = document.graph.edges.find((value) => value.id === `edge.ne20.${label}`);
  if (edge === undefined) throw new Error("Missing shell-2 edge");
  const from = document.layout.vertices.find((value) => value.vertexId === edge.from)?.position;
  const to = document.layout.vertices.find((value) => value.vertexId === edge.to)?.position;
  if (
    from === undefined ||
    to === undefined ||
    typeof from.x !== "number" ||
    typeof from.y !== "number" ||
    typeof to.x !== "number" ||
    typeof to.y !== "number"
  )
    throw new Error("Expected exact integer fixture");
  const dx = to.x - from.x,
    dy = to.y - from.y;
  expect(
    ([13, 15, 19].includes(label) ? dx < 0 : dx > 0) &&
      Math.abs(dx) === Math.abs(dy) &&
      edge.direction === "from-to",
    "Shell-2 side must point east along its diagonal",
  );
  expect(
    document.layout.edges.find((value) => value.edgeId === edge.id)?.color ===
      ([4, 15, 19, 16, 20].includes(label)
        ? "red"
        : [2, 13, 14].includes(label)
          ? "blue"
          : dy > 0
            ? "red"
            : "blue"),
    "Shell-2 color must respect the explicit 13/14 blue, 16/20 red overrides",
  );
}
expect(
  document.graph.edges.find((edge) => edge.id === "edge.ne20.13")?.from === "vertex.bottom-right" &&
    document.graph.edges.find((edge) => edge.id === "edge.ne20.13")?.to === "vertex.bottom-tip",
  "13 must be reversed, from bottom-right to bottom-tip",
);
expect(
  document.graph.edges.find((edge) => edge.id === "edge.ne20.14")?.from === "vertex.bottom-left" &&
    document.graph.edges.find((edge) => edge.id === "edge.ne20.14")?.to === "vertex.bottom-tip",
  "14 must point from bottom-left to bottom-tip",
);
for (const label of [17, 22]) {
  const edge = document.graph.edges.find((value) => value.id === `edge.ne20.${label}`);
  if (edge === undefined) throw new Error("Missing vertical edge");
  const from = document.layout.vertices.find((value) => value.vertexId === edge.from),
    to = document.layout.vertices.find((value) => value.vertexId === edge.to);
  expect(
    from !== undefined &&
      to !== undefined &&
      from.position.x === to.position.x &&
      from.position.y !== to.position.y,
    "Required edge not vertical",
  );
}
expect(
  document.layout.edges.find((value) => value.edgeId === "edge.ne20.16")?.color === "red",
  "16 must be red after the approved swap",
);
expect(
  document.layout.edges.find((value) => value.edgeId === "edge.ne20.18")?.color === "blue",
  "18 must now be blue",
);
expect(
  traceRoute(document, "edge.ne20.3", "right").steps[1]?.edgeId === "edge.ne20.7",
  "Keep right must select the rightmost exit, not the nearest",
);
expect(
  traceRoute(document, "edge.ne20.7", "left", true).steps[1]?.edgeId === "edge.ne20.21",
  "Keep left must select the leftmost exit",
);
expect(
  path.steps[5]?.edgeId === "edge.ne20.21",
  "Route must continue after 7 without a false ambiguity",
);
expect(
  !DiagramDocumentSchema.safeParse({
    ...document,
    policy: { ...document.policy, continuations: [] },
  }).success,
  "Edge-specific continuation overrides must not be accepted",
);
const reordered = DiagramDocumentSchema.parse({
  ...document,
  graph: {
    ...document.graph,
    vertices: [...document.graph.vertices].reverse(),
    edges: [...document.graph.edges].reverse(),
  },
  layout: {
    ...document.layout,
    vertices: [...document.layout.vertices].reverse(),
    edges: [...document.layout.edges].reverse(),
    aliases: [...document.layout.aliases].reverse(),
  },
});
expect(
  JSON.stringify(traceRoute(reordered, "edge.ne20.8")) === JSON.stringify(path),
  "Array order changed route",
);
const recolored = DiagramDocumentSchema.parse({
  ...document,
  layout: {
    ...document.layout,
    edges: document.layout.edges.map((value) => ({ ...value, color: "green" })),
  },
});
expect(
  JSON.stringify(traceRoute(recolored, "edge.ne20.8")) !== JSON.stringify(path),
  "Authored color classes must now govern visit eligibility",
);
const scaled = DiagramDocumentSchema.parse({
  ...document,
  layout: {
    ...document.layout,
    vertices: document.layout.vertices.map((value) => {
      if (typeof value.position.x !== "number" || typeof value.position.y !== "number")
        throw new Error("Fixture must use integers");
      return {
        ...value,
        position: {
          x: { numerator: value.position.x, denominator: 3 },
          y: { numerator: value.position.y, denominator: 3 },
        },
      };
    }),
  },
});
expect(
  JSON.stringify(traceRoute(scaled, "edge.ne20.8")) === JSON.stringify(path),
  "Exact rational scaling changed route",
);
const mirrored = DiagramDocumentSchema.parse({
  ...document,
  layout: {
    ...document.layout,
    vertices: document.layout.vertices.map((value) => {
      if (typeof value.position.x !== "number") throw new Error("Expected integer fixture");
      return { ...value, position: { ...value.position, x: -value.position.x } };
    }),
  },
});
expect(
  traceRoute(mirrored, "edge.ne20.8", "right")
    .steps.map((step) => step.edgeId)
    .join(",") === path.steps.map((step) => step.edgeId).join(","),
  "Keep-left/right choices must exchange under reflection",
);
expect(traceRoute(document, "edge.missing").status === "invalid-start", "Missing start accepted");
expect(
  traceRoute(document, "edge.ne20.8", "left", true).status === "invalid-start",
  "Directed edge reversed",
);
expect(
  traceRoute(syntheticExample(), "edge.diagonal").status === "unresolved",
  "Unresolved diagram routed",
);
// Distinct edges on the same extreme ray are a genuine tie, never resolved by array order.
const third = document.graph.edges.find((value) => value.id === "edge.ne20.3"),
  style = document.layout.edges.find((value) => value.edgeId === "edge.ne20.3");
if (third === undefined || style === undefined) throw new Error("Missing edge 3");
const ambiguous = DiagramDocumentSchema.parse({
  ...document,
  graph: {
    ...document.graph,
    edges: [...document.graph.edges, { ...third, id: "edge.duplicate" }],
  },
  layout: {
    ...document.layout,
    edges: [...document.layout.edges, { ...style, edgeId: "edge.duplicate" }],
  },
});
const stopped = traceRoute(ambiguous, "edge.ne20.8");
expect(
  stopped.status === "ambiguous" && stopped.steps.at(-1)?.edgeId === "edge.ne20.10",
  "Ambiguous exit not stopped at 10",
);
// Coincident placement does not turn a disconnected vertex into a junction.
const disconnected = DiagramDocumentSchema.parse({
  ...document,
  graph: {
    ...document.graph,
    vertices: [...document.graph.vertices, { id: "vertex.disconnected" }],
    edges: document.graph.edges.map((value) =>
      value.id === third.id ? { ...value, from: "vertex.disconnected" } : value,
    ),
  },
  layout: {
    ...document.layout,
    vertices: [
      ...document.layout.vertices,
      { vertexId: "vertex.disconnected", position: { x: 0, y: 34 } },
    ],
  },
});
expect(
  !traceRoute(disconnected, "edge.ne20.8").steps.some((value) => value.edgeId === third.id),
  "Coincident geometry created incidence",
);
expect(JSON.stringify(document) === original, "Routing mutated source model");
setActivePinia(createPinia());
const store = useInspection();
store.showNeon();
store.run();
const behavior = useDiagramInspection();
expect(
  behavior.routeLabels.value === "8" &&
    behavior.marker.value?.x === 0 &&
    behavior.marker.value.y === -66,
  "Playback must begin at edge 8 source",
);
store.advancePlayback(ROUTE_EDGE_MS / 2);
expect(
  behavior.marker.value?.x === -25 && behavior.marker.value.y === -41,
  "Marker failed halfway interpolation",
);
store.pause();
const paused = store.state.playback.elapsedMs;
store.advancePlayback(ROUTE_EDGE_MS);
expect(store.state.playback.elapsedMs === paused, "Paused playback advanced");
store.resume();
store.advancePlayback(ROUTE_EDGE_MS / 2);
expect(
  behavior.routeLabels.value === "8 → 12" && behavior.marker.value?.x === -50,
  "Readout did not advance with marker",
);
store.advancePlayback(2 * ROUTE_EDGE_MS);
expect(behavior.routeLabels.value === "8 → 12 → 10 → 3", "Animated path missed required junction");
store.advancePlayback(100 * ROUTE_EDGE_MS);
expect(store.routeFinished && !store.state.playback.playing, "Playback did not stop at route end");
const completedPosition = JSON.stringify(behavior.marker.value);
store.advancePlayback(ROUTE_EDGE_MS);
store.resume();
expect(
  !store.state.playback.playing && JSON.stringify(behavior.marker.value) === completedPosition,
  "Finished playback restarted itself",
);
expect(
  pointAtFraction(
    [
      { x: 0, y: 0 },
      { x: 0, y: 10 },
      { x: 30, y: 10 },
    ],
    0.5,
  ).x === 10,
  "Playback must follow polyline arc length",
);
const saved = JSON.stringify(store.state.route);
store.toggleLabels();
expect(JSON.stringify(store.state.route) === saved, "Display toggles changed route");
store.clearRoute();
expect(
  store.state.route === null && behavior.marker.value === null && !store.state.playback.playing,
  "Clear did not reset path and marker",
);
store.stepBack();
expect(store.state.route === null, "Back must not create a route");
store.stepForward("left");
expect(
  store.state.route !== null &&
    store.state.playback.elapsedMs === ROUTE_EDGE_MS &&
    !store.state.playback.playing,
  "Forward must initialize a paused route at the next boundary",
);
store.advancePlayback(ROUTE_EDGE_MS);
expect(store.state.playback.elapsedMs === ROUTE_EDGE_MS, "Stepping must pause animation");
store.stepBack();
store.stepBack();
expect(store.state.playback.elapsedMs === 0, "Back must clamp at the beginning");
store.resume();
store.advancePlayback(ROUTE_EDGE_MS / 2);
store.stepForward();
expect(
  store.state.playback.elapsedMs === ROUTE_EDGE_MS && !store.state.playback.playing,
  "Forward mid-segment must snap to its end and pause",
);
store.resume();
store.advancePlayback(ROUTE_EDGE_MS / 2);
store.stepBack();
expect(
  store.state.playback.elapsedMs === ROUTE_EDGE_MS && !store.state.playback.playing,
  "Back mid-segment must snap to its start and pause",
);
store.resume();
store.advancePlayback(100 * ROUTE_EDGE_MS);
const endTime = store.state.playback.elapsedMs;
store.stepForward();
expect(
  store.state.playback.elapsedMs === endTime && !store.state.playback.playing,
  "Forward must clamp at route end",
);
store.stepBack();
expect(
  store.state.playback.elapsedMs === endTime - ROUTE_EDGE_MS && !store.routeFinished,
  "Back from completion must restore a paused inspectable route",
);
store.clearRoute();
store.run();
store.loadExample();
expect(store.state.route === null, "Diagram change retained old route");
expect(
  traceRoute(document, "edge.ne20.15").steps[0]?.from === "vertex.bottom-left" &&
    traceRoute(document, "edge.ne20.15").steps[0]?.to === "vertex.left-tip",
  "15 must now point from bottom-left to left-tip",
);
expect(
  path.status === "no-continuation" &&
    path.activeColor === "blue" &&
    path.steps.map((step) => step.edgeId).join(",") ===
      "edge.ne20.8,edge.ne20.12,edge.ne20.10,edge.ne20.3,edge.ne20.7,edge.ne20.21,edge.ne20.4,edge.ne20.20,edge.ne20.19,edge.ne20.7,edge.ne20.17,edge.ne20.15,edge.ne20.16,edge.ne20.1,edge.ne20.11,edge.ne20.12,edge.ne20.9,edge.ne20.27,edge.ne20.23,edge.ne20.24",
  "The updated base colors must exhaust red before the blocked blue phase",
);
const firstBlue = path.steps.findIndex(
  (step) => document.layout.edges.find((edge) => edge.edgeId === step.edgeId)?.color === "blue",
);
expect(
  firstBlue === -1 ||
    document.layout.edges
      .filter((edge) => edge.color === "red")
      .every((edge) => path.steps.slice(0, firstBlue).some((step) => step.edgeId === edge.edgeId)),
  "Every red must be visited before blue unlocks",
);
expect(
  path.steps
    .map((step) => step.edgeId)
    .join(",")
    .includes("edge.ne20.21,edge.ne20.4,edge.ne20.20"),
  "Eligible red 4 must outrank green 25 after red 21",
);
expect(
  traceRoute(document, "edge.ne20.26")
    .steps.map((step) => step.edgeId)
    .join(",")
    .includes("edge.ne20.26,edge.ne20.19"),
  "Reversed red 19 must be traversed after green 26",
);
expect(
  document.graph.edges.find((edge) => edge.id === "edge.ne20.19")?.from === "vertex.right-tip" &&
    document.graph.edges.find((edge) => edge.id === "edge.ne20.19")?.to === "vertex.middle-right",
  "19 must point right-tip to middle-right",
);
const coloredVisits = path.steps
  .filter(
    (step) => document.layout.edges.find((edge) => edge.edgeId === step.edgeId)?.color !== "green",
  )
  .map((step) => step.edgeId);
expect(new Set(coloredVisits).size === coloredVisits.length, "Colored edges must never repeat");
const cycle = DiagramDocumentSchema.parse({
  ...document,
  isotope: null,
  graph: {
    vertices: [{ id: "vertex.a" }, { id: "vertex.b" }, { id: "vertex.c" }],
    edges: [
      { id: "edge.a", from: "vertex.a", to: "vertex.b", direction: "from-to" },
      { id: "edge.b", from: "vertex.b", to: "vertex.c", direction: "from-to" },
      { id: "edge.c", from: "vertex.c", to: "vertex.a", direction: "from-to" },
    ],
    roles: [],
    junctionOrders: [],
    review: { status: "unreviewed", questions: ["Route test fixture"] },
  },
  layout: {
    ...document.layout,
    aliases: [],
    vertices: [
      { vertexId: "vertex.a", position: { x: 0, y: 0 } },
      { vertexId: "vertex.b", position: { x: 10, y: 0 } },
      { vertexId: "vertex.c", position: { x: 20, y: -10 } },
    ],
    edges: [
      { edgeId: "edge.a", color: "green", via: [], labelPosition: "midpoint" },
      { edgeId: "edge.b", color: "green", via: [{ x: 10, y: -10 }], labelPosition: "midpoint" },
      {
        edgeId: "edge.c",
        color: "green",
        via: [
          { x: 20, y: 0 },
          { x: -10, y: 0 },
        ],
        labelPosition: "midpoint",
      },
    ],
  },
});
expect(
  traceRoute(cycle, "edge.a", "right").steps[1]?.edgeId === "edge.b",
  "A sole opposite-side exit must remain available",
);
const fan = DiagramDocumentSchema.parse({
  ...cycle,
  graph: {
    ...cycle.graph,
    vertices: [{ id: "vertex.a" }, { id: "vertex.b" }, { id: "vertex.c" }, { id: "vertex.d" }],
    edges: [
      { id: "edge.a", from: "vertex.a", to: "vertex.b", direction: "from-to" },
      { id: "edge.b", from: "vertex.b", to: "vertex.c", direction: "from-to" },
      { id: "edge.c", from: "vertex.b", to: "vertex.d", direction: "from-to" },
    ],
  },
  layout: {
    ...cycle.layout,
    vertices: [
      { vertexId: "vertex.a", position: { x: 0, y: 0 } },
      { vertexId: "vertex.b", position: { x: 10, y: 0 } },
      { vertexId: "vertex.c", position: { x: 20, y: -10 } },
      { vertexId: "vertex.d", position: { x: 0, y: -10 } },
    ],
    edges: cycle.layout.edges.map((edge) => ({ ...edge, via: [] })),
  },
});
expect(
  traceRoute(fan, "edge.a", "right").steps[1]?.edgeId === "edge.b",
  "Rightmost among left-turning exits must remain the globally rightmost ray",
);
expect(
  traceRoute(fan, "edge.a", "left").steps[1]?.edgeId === "edge.c",
  "Keep left must choose the most-left ray",
);
const reflectedFan = DiagramDocumentSchema.parse({
  ...fan,
  layout: {
    ...fan.layout,
    vertices: fan.layout.vertices.map((vertex) => {
      if (typeof vertex.position.y !== "number") throw new Error("Expected integer fixture");
      return { ...vertex, position: { ...vertex.position, y: -vertex.position.y } };
    }),
  },
});
expect(
  traceRoute(reflectedFan, "edge.a", "left").steps[1]?.edgeId === "edge.b",
  "Leftmost among right-turning exits must remain the globally leftmost ray",
);
const shuffledFan = DiagramDocumentSchema.parse({
  ...fan,
  graph: { ...fan.graph, edges: [...fan.graph.edges].reverse() },
});
expect(
  JSON.stringify(traceRoute(shuffledFan, "edge.a", "right")) ===
    JSON.stringify(traceRoute(fan, "edge.a", "right")),
  "Global extremes must not depend on edge order",
);
const ownFirst = DiagramDocumentSchema.parse({
  ...fan,
  layout: {
    ...fan.layout,
    edges: fan.layout.edges.map((edge) => ({
      ...edge,
      color: edge.edgeId === "edge.c" ? "green" : "red",
    })),
  },
});
expect(
  traceRoute(ownFirst, "edge.a", "left").steps[1]?.edgeId === "edge.b",
  "Eligible red must outrank a more-left green",
);
const blueFirst = DiagramDocumentSchema.parse({
  ...ownFirst,
  layout: {
    ...ownFirst.layout,
    edges: ownFirst.layout.edges.map((edge) => ({
      ...edge,
      color: edge.color === "red" ? "blue" : edge.color,
    })),
  },
});
expect(
  traceRoute(blueFirst, "edge.a", "left").steps[1]?.edgeId === "edge.b",
  "Eligible blue must outrank a more-left green",
);
for (const colored of [ownFirst, blueFirst]) {
  const oppositeSide = DiagramDocumentSchema.parse({
    ...colored,
    layout: {
      ...colored.layout,
      vertices: colored.layout.vertices.map((vertex) =>
        vertex.vertexId === "vertex.c" ? { ...vertex, position: { x: 20, y: 10 } } : vertex,
      ),
    },
  });
  expect(
    traceRoute(oppositeSide, "edge.a", "left").steps[1]?.edgeId === "edge.b",
    "Same-color right turn must beat green left turn even with keep-left preference",
  );
}
const exhaustedRed = DiagramDocumentSchema.parse({
  ...ownFirst,
  layout: {
    ...ownFirst.layout,
    edges: ownFirst.layout.edges.map((edge) =>
      edge.edgeId === "edge.b" ? { ...edge, color: "blue" } : edge,
    ),
  },
});
expect(
  traceRoute(exhaustedRed, "edge.a", "left").steps[1]?.edgeId === "edge.b",
  "After the last red, flipped keep-right selects the less-left blue exit",
);
const blueNotOutbound = DiagramDocumentSchema.parse({
  ...exhaustedRed,
  graph: {
    ...exhaustedRed.graph,
    edges: exhaustedRed.graph.edges.map((edge) =>
      edge.id === "edge.b" ? { ...edge, direction: "to-from" } : edge,
    ),
  },
});
const waitingForBlue = traceRoute(blueNotOutbound, "edge.a", "left");
expect(
  waitingForBlue.activeColor === "blue" &&
    waitingForBlue.steps.map((step) => step.edgeId).join(",") === "edge.a,edge.c",
  "Blue becomes own color before its first traversal, persists across green, and still obeys arrowheads",
);
const incomingOwn = DiagramDocumentSchema.parse({
  ...ownFirst,
  graph: {
    ...ownFirst.graph,
    edges: ownFirst.graph.edges.map((edge) =>
      edge.id === "edge.b" ? { ...edge, from: edge.to, to: edge.from } : edge,
    ),
  },
});
expect(
  traceRoute(incomingOwn, "edge.a", "left").steps[1]?.edgeId === "edge.c",
  "An incoming-only own-color edge must not block an eligible green",
);
const allOwn = DiagramDocumentSchema.parse({
  ...fan,
  layout: { ...fan.layout, edges: fan.layout.edges.map((edge) => ({ ...edge, color: "red" })) },
});
expect(
  traceRoute(allOwn, "edge.a", "left").steps[1]?.edgeId === "edge.c" &&
    traceRoute(allOwn, "edge.a", "right").steps[1]?.edgeId === "edge.b",
  "Angular preference must still rank multiple own-color continuations",
);
const closed = traceRoute(cycle, "edge.a");
expect(
  closed.status === "repeated-state" && closed.steps.length === 3,
  "Via tangents, straight preference or cycle termination failed",
);
// Authored color classes are semantic; CSS palette/display settings remain independent.
const phases = DiagramDocumentSchema.parse({
  ...fan,
  graph: {
    ...fan.graph,
    edges: [
      ...fan.graph.edges,
      { id: "edge.d", from: "vertex.d", to: "vertex.c", direction: "from-to" },
    ],
  },
  layout: {
    ...fan.layout,
    edges: [
      ...fan.layout.edges.map((edge) => ({
        ...edge,
        color: edge.edgeId === "edge.b" ? "blue" : "red",
      })),
      { edgeId: "edge.d", color: "blue", via: [], labelPosition: "midpoint" },
    ],
  },
});
const lockedExtreme = DiagramDocumentSchema.parse({
  ...phases,
  layout: {
    ...phases.layout,
    edges: phases.layout.edges.map((edge) => ({
      ...edge,
      color: edge.edgeId === "edge.c" ? "blue" : edge.edgeId === "edge.b" ? "red" : edge.color,
    })),
  },
});
expect(
  traceRoute(lockedExtreme, "edge.a", "right").steps[1]?.edgeId === "edge.b",
  "A locked blue ray must be excluded before angular ranking",
);
const phased = traceRoute(phases, "edge.a", "right");
expect(
  phased.steps.map((step) => step.edgeId).join(",") === "edge.a,edge.c,edge.d",
  "Eligibility must override preferred blue ray until both reds are visited, then allow blue",
);
expect(
  phased.activeColor === "blue" && phased.remainingColoredEdges.join(",") === "edge.b",
  "Color switch must retain visitation across phases",
);
const swappedPhases = DiagramDocumentSchema.parse({
  ...phases,
  layout: {
    ...phases.layout,
    edges: phases.layout.edges.map((edge) => ({
      ...edge,
      color: edge.color === "red" ? "blue" : "red",
    })),
  },
});
expect(
  traceRoute(swappedPhases, "edge.a", "right")
    .steps.map((step) => step.edgeId)
    .join(",") === phased.steps.map((step) => step.edgeId).join(","),
  "Blue-first traversal must obey the same strict rule",
);
const finishedColors = DiagramDocumentSchema.parse({
  ...cycle,
  layout: {
    ...cycle.layout,
    edges: cycle.layout.edges.map((edge) => ({
      ...edge,
      color: edge.edgeId === "edge.a" ? "red" : edge.edgeId === "edge.b" ? "blue" : "green",
    })),
  },
});
const finished = traceRoute(finishedColors, "edge.a");
expect(
  finished.status === "completed" &&
    finished.steps.length === 2 &&
    finished.remainingColoredEdges.length === 0,
  "Completion requires all colored edges, each once",
);
const locked = DiagramDocumentSchema.parse({
  ...finishedColors,
  layout: {
    ...finishedColors.layout,
    edges: finishedColors.layout.edges.map((edge) => ({
      ...edge,
      color: edge.edgeId === "edge.c" ? "red" : edge.color,
    })),
  },
});
expect(
  traceRoute(locked, "edge.a").steps.length === 1 &&
    traceRoute(locked, "edge.a").status === "no-continuation",
  "An unreachable remaining red must not authorize an early blue switch",
);
const reusedGreen = DiagramDocumentSchema.parse({
  ...cycle,
  graph: {
    ...cycle.graph,
    vertices: [...cycle.graph.vertices, { id: "vertex.d" }, { id: "vertex.e" }],
    edges: [
      ...cycle.graph.edges,
      { id: "edge.d", from: "vertex.d", to: "vertex.e", direction: "from-to" },
    ],
  },
  layout: {
    ...cycle.layout,
    vertices: [
      ...cycle.layout.vertices,
      { vertexId: "vertex.d", position: { x: 30, y: 0 } },
      { vertexId: "vertex.e", position: { x: 40, y: 0 } },
    ],
    edges: [
      ...cycle.layout.edges.map((edge) => ({
        ...edge,
        color: edge.edgeId === "edge.b" ? "red" : "green",
      })),
      { edgeId: "edge.d", color: "red", via: [], labelPosition: "midpoint" },
    ],
  },
});
const reused = traceRoute(reusedGreen, "edge.a");
expect(
  reused.steps.map((step) => step.edgeId).join(",") === "edge.a,edge.b,edge.c,edge.a" &&
    reused.status === "no-continuation",
  "Green-start runs adopt the first colored edge and may reuse green, never red",
);
const activeBeforeLoop = DiagramDocumentSchema.parse({
  ...reusedGreen,
  graph: {
    ...reusedGreen.graph,
    vertices: [...reusedGreen.graph.vertices, { id: "vertex.s" }],
    edges: [
      ...reusedGreen.graph.edges,
      { id: "edge.s", from: "vertex.s", to: "vertex.a", direction: "from-to" },
    ],
  },
  layout: {
    ...reusedGreen.layout,
    vertices: [
      ...reusedGreen.layout.vertices,
      { vertexId: "vertex.s", position: { x: -10, y: 0 } },
    ],
    edges: [
      ...reusedGreen.layout.edges,
      { edgeId: "edge.s", color: "red", via: [], labelPosition: "midpoint" },
    ],
  },
});
expect(
  traceRoute(activeBeforeLoop, "edge.s")
    .steps.map((step) => step.edgeId)
    .join(",") === "edge.s,edge.a,edge.b,edge.c,edge.a",
  "Same-phase connector state must remain revisitable after the visited set changes",
);
const blueOnce = DiagramDocumentSchema.parse({
  ...activeBeforeLoop,
  layout: {
    ...activeBeforeLoop.layout,
    edges: activeBeforeLoop.layout.edges.map((edge) => ({
      ...edge,
      color: edge.color === "red" ? "blue" : edge.color,
    })),
  },
});
expect(
  traceRoute(blueOnce, "edge.s")
    .steps.map((step) => step.edgeId)
    .join(",") === "edge.s,edge.a,edge.b,edge.c,edge.a",
  "Blue edges must be visit-once too",
);
const formerBlueTie = traceRoute(document, "edge.ne20.6", "right", true);
expect(
  formerBlueTie.steps[1]?.edgeId === "edge.ne20.18" &&
    !document.graph.edges.some((edge) => edge.id === "edge.ne20.5"),
  "Only edge 18 must remain on the former duplicate connection",
);
const zero = DiagramDocumentSchema.parse({
  ...cycle,
  layout: {
    ...cycle.layout,
    edges: cycle.layout.edges.map((value) =>
      value.edgeId === "edge.b" ? { ...value, via: [{ x: 10, y: 0 }] } : value,
    ),
  },
});
expect(
  traceRoute(zero, "edge.a").status === "degenerate-geometry",
  "Zero-length tangent was silently routed",
);
const reversedStorage = DiagramDocumentSchema.parse({
  ...cycle,
  graph: {
    ...cycle.graph,
    edges: cycle.graph.edges.map((value) =>
      value.id === "edge.a"
        ? { ...value, from: value.to, to: value.from, direction: "to-from" }
        : value,
    ),
  },
});
expect(
  JSON.stringify(traceRoute(reversedStorage, "edge.a")) === JSON.stringify(closed),
  "to-from arrow direction ignored",
);
console.log(
  `PASS: Ne-20 labels/colors/orientation, 10 → 3 alternation, exact geometry, incidence, ambiguity, invariance and route lifecycle (${path.steps.length} steps; ${path.status})`,
);
