import { z } from "zod";
import { createPinia, setActivePinia } from "pinia";
import { createDiagram } from "../src/examples/diagrams.js";
import { isotopeCatalog } from "../src/examples/catalog.js";
import { neon20 } from "../src/examples/neon20.js";
import { DiagramDocumentSchema } from "../src/schemas/document.js";
import { traceRoute } from "../src/domain/route.js";
import { constructMorseSurface } from "../src/domain/morse-surface.js";
import { emptyEdgeEdits, cycleEdgeEdit, applyEdgeEdits } from "../src/domain/edge-edits.js";
import { projectDiagram } from "../src/presentation/diagram.js";
import { useCatalog } from "../src/vue/stores/catalog.js";
import { useInspection } from "../src/vue/stores/inspection.js";
function expect(value: boolean, message: string): void {
  if (!value) throw new Error(message);
}
// Independently enumerated fixture sizes, not calculated from the constructors.
const cases = z.array(z.tuple([z.string(), z.string(), z.int(), z.int()])).parse([
  ["Hydrogen-1", "h1", 3, 2],
  ["Hydrogen-2", "h2", 3, 3],
  ["Helium-3", "he3", 4, 5],
  ["Helium-4", "he4", 4, 6],
  ["Lithium-6", "li6", 6, 8],
  ["Lithium-7", "li7", 6, 10],
  ["Beryllium-9", "be9", 7, 12],
  ["Boron-10", "b10", 9, 13],
  ["Boron-11", "b11", 9, 15],
  ["Carbon-12", "c12", 10, 15],
  ["Carbon-13", "c13", 10, 17],
  ["Nitrogen-14", "n14", 12, 18],
  ["Nitrogen-15", "n15", 12, 20],
  ["Oxygen-16", "o16", 13, 20],
  ["Oxygen-17", "o17", 13, 22],
  ["Oxygen-18", "o18", 13, 24],
  ["Fluorine-19", "f19", 15, 27],
]);
const baseline = JSON.stringify(neon20());
setActivePinia(createPinia());
const catalog = useCatalog(),
  inspection = useInspection();
for (const [name, key, vertices, edges] of cases) {
  const choice = createDiagram(name),
    entry = isotopeCatalog.find((e) => e.name === name);
  if (choice === null || entry === undefined) throw new Error(`Missing ${name}`);
  const doc = choice.document,
    before = JSON.stringify(doc);
  expect(
    doc.id === `diagram.${key}` &&
      doc.graph.vertices.length === vertices &&
      doc.graph.edges.length === edges,
    `${name}: wrong graph`,
  );
  expect(
    doc.isotope?.protons === entry.protons && doc.isotope.neutrons === entry.neutrons,
    `${name}: inventory mismatch`,
  );
  expect(
    doc.isotope?.electrons.status === "unspecified" && doc.isotope.charge.status === "unspecified",
    `${name}: fabricated electronic state`,
  );
  expect(
    doc.policy.status === "alternating" &&
      doc.graph.edges.every((e) => e.direction === "from-to" || e.direction === "undirected"),
    `${name}: missing authored directions`,
  );
  expect(
    doc.layout.edges.filter((e) => e.color === "red").length === entry.protons &&
      doc.layout.edges.filter((e) => e.color === "blue").length === entry.protons,
    `${name}: wrong fixture colors`,
  );
  expect(
    new Set(doc.layout.aliases.map((a) => a.number)).size === edges,
    `${name}: missing/duplicate labels`,
  );
  for (const e of doc.graph.edges)
    expect(
      (e.direction === "undirected") ===
        (doc.layout.edges.find((s) => s.edgeId === e.id)?.color === "green"),
      `${name}: connector direction`,
    );
  const box = doc.layout.viewBox;
  expect(
    [
      ...doc.layout.vertices.map((v) => v.position),
      ...doc.layout.edges.flatMap((e) => e.via),
    ].every(
      (p) =>
        typeof p.x === "number" &&
        typeof p.y === "number" &&
        p.x >= box.x &&
        p.x <= box.x + box.width &&
        p.y >= box.y &&
        p.y <= box.y + box.height,
    ),
    `${name}: geometry outside authored framing`,
  );
  const projection = projectDiagram(doc);
  expect(
    projection.edges.length === edges && projection.vertices.length === vertices,
    `${name}: projection dropped records`,
  );
  const route = traceRoute(doc, choice.initialEdgeId);
  expect(route.status !== "unresolved" && route.steps.length > 0, `${name}: traversal not enabled`);
  if (["h1", "h2", "he3", "he4"].includes(key))
    expect(
      route.status === "completed",
      `${name}: authored light-isotope route should cover its colored edges`,
    );
  const first = cycleEdgeEdit(doc, emptyEdgeEdits(doc), choice.initialEdgeId);
  if (first === null) throw new Error(`${name}: initial edge is not editable`);
  const second = cycleEdgeEdit(first.document, first.edits, choice.initialEdgeId);
  if (second === null) throw new Error(`${name}: direction edit unavailable`);
  expect(
    second.edits.edges[0]?.nextOperation === "color" &&
      second.document.graph.edges.find((e) => e.id === choice.initialEdgeId)?.direction ===
        "to-from",
    `${name}: click phase/arrow failed`,
  );
  expect(
    JSON.stringify(applyEdgeEdits(doc, second.edits)) === JSON.stringify(second.document),
    `${name}: edits did not restore`,
  );
  expect(JSON.stringify(doc) === before, `${name}: editing mutated the template`);
  expect(
    JSON.stringify(createDiagram(name)?.document) === before,
    `${name}: fresh activation inherited another instance's edits`,
  );
  const surface = constructMorseSurface(doc);
  expect(
    surface.darts.length === 2 * edges && surface.eulerCharacteristic === vertices - edges,
    `${name}: Morse construction lost incidence`,
  );
  const bad = {
    ...doc,
    graph: { ...doc.graph, edges: doc.graph.edges.map((e) => ({ ...e, direction: "unresolved" })) },
  };
  expect(
    !DiagramDocumentSchema.safeParse(bad).success,
    `${name}: unresolved arrows accepted for alternating traversal`,
  );
  catalog.select(name);
  expect(inspection.activeDocument?.id === doc.id, `${name}: activation failed`);
  catalog.pin();
  const pin = catalog.state.references.find((r) => r.id === doc.id);
  if (pin === undefined) throw new Error("Missing reference");
  const snapshot = JSON.stringify(pin);
  catalog.select("Sodium-23");
  expect(
    inspection.activeDocument === null && JSON.stringify(pin) === snapshot,
    `${name}: missing diagram or pin isolation failed`,
  );
  catalog.unpin(doc.id);
}
const he3 = createDiagram("Helium-3");
if (he3 === null) throw new Error("Missing He-3");
const bar = he3.document.graph.edges.find((e) => e.id === "edge.he3.5");
expect(
  bar?.from === "vertex.he3.left" &&
    bar.to === "vertex.he3.right" &&
    bar.direction === "undirected",
  "He-3 must have an undirected left-to-right bar",
);
expect(
  he3.document.layout.edges.filter((e) => e.color === "green").length === 1 &&
    he3.document.layout.edges.find((e) => e.edgeId === bar?.id)?.color === "green",
  "He-3 must have exactly one green connector",
);
expect(
  !he3.document.graph.vertices.some((v) => v.id.includes("outer-")),
  "He-3 outer triangle vertices remain",
);
const he = createDiagram("Helium-4"),
  o18 = createDiagram("Oxygen-18"),
  f19 = createDiagram("Fluorine-19");
if (he === null || o18 === null || f19 === null) throw new Error("Missing crossing controls");
expect(
  !he.document.layout.vertices.some((v) => v.position.x === 0 && v.position.y === 0),
  "He4 diagonal crossing became a vertex",
);
expect(
  he.document.graph.edges.find((e) => e.id === "edge.he4.5")?.to === "vertex.he4.right" &&
    he.document.graph.edges.find((e) => e.id === "edge.he4.6")?.to === "vertex.he4.bottom",
  "He4 crossing endpoints changed",
);
expect(
  o18.document.layout.edges.find((e) => e.edgeId === "edge.o18.23")?.via.length === 2,
  "O18 wrapper bends lost",
);
expect(
  f19.document.graph.edges.find((e) => e.id === "edge.f19.23")?.from === "vertex.f19.lower-left" &&
    f19.document.graph.edges.find((e) => e.id === "edge.f19.23")?.to === "vertex.f19.fluorine-left",
  "F19 wrapper endpoints wrong",
);
expect(
  !f19.document.graph.edges
    .filter((e) => e.id === "edge.f19.23")
    .some((e) => e.from === "vertex.f19.nitrogen-left" || e.to === "vertex.f19.nitrogen-left"),
  "Wrapper acquired an intermediate junction",
);
const referenceArrows = z.array(z.tuple([z.string(), z.string(), z.string(), z.string()])).parse([
  ["Lithium-6", "edge.li6.6", "vertex.li6.center", "vertex.li6.lower-right"],
  ["Beryllium-9", "edge.be9.11", "vertex.be9.bottom", "vertex.be9.lower-right"],
  ["Boron-10", "edge.b10.1", "vertex.b10.top", "vertex.b10.right"],
  ["Boron-10", "edge.b10.9", "vertex.b10.upper-tip", "vertex.b10.upper-left"],
  ["Carbon-12", "edge.c12.14", "vertex.c12.lower-right", "vertex.c12.bottom"],
  ["Nitrogen-14", "edge.n14.16", "vertex.n14.bottom", "vertex.n14.nitrogen-right"],
  ["Oxygen-16", "edge.o16.19", "vertex.o16.oxygen-bottom", "vertex.o16.nitrogen-right"],
  ["Fluorine-19", "edge.f19.25", "vertex.f19.oxygen-bottom", "vertex.f19.fluorine-left"],
]);
for (const [name, id, from, to] of referenceArrows) {
  const edge = createDiagram(name)?.document.graph.edges.find((e) => e.id === id);
  expect(
    edge?.from === from && edge.to === to && edge.direction === "from-to",
    `${name}: named-recipe reflection or arrow changed`,
  );
}
const wrapperVia = o18.document.layout.edges.find((e) => e.edgeId === "edge.o18.23")?.via;
expect(
  wrapperVia?.[0]?.x === -60 &&
    wrapperVia[0].y === 84 &&
    wrapperVia[1]?.x === -60 &&
    wrapperVia[1].y === 284,
  "O18 wrapper reference points changed",
);
expect(isotopeCatalog.filter((e) => e.hasDiagram).length === 18, "Wrong catalog coverage");
expect(
  isotopeCatalog.slice(0, 17).every((e) => cases.some(([name]) => name === e.name)),
  "Missing pre-Ne20 catalog entry",
);
expect(JSON.stringify(neon20()) === baseline, "Ne20 changed");
console.log(
  "PASS: all 17 pre-Ne20 diagrams, explicit topology, inventory, arrows, edits/restoration, isolated templates/pins, Morse construction and non-junction crossings; Ne20 preserved",
);
