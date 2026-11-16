import { createPinia, setActivePinia } from "pinia";
import { isReadonly } from "vue";
import { isotopeCatalog } from "../src/examples/catalog.js";
import { createDiagram, hasDiagram } from "../src/examples/diagrams.js";
import { useCatalog } from "../src/vue/stores/catalog.js";
import { useInspection } from "../src/vue/stores/inspection.js";
function expect(value: boolean, message: string): void {
  if (!value) throw new Error(message);
}
expect(
  isotopeCatalog.length === 96 && new Set(isotopeCatalog.map((entry) => entry.name)).size === 96,
  "Catalog count/uniqueness failed",
);
expect(
  isotopeCatalog.every((entry) => entry.name.endsWith(`-${entry.protons + entry.neutrons}`)),
  "Catalog mass mismatch",
);
setActivePinia(createPinia());
const catalog = useCatalog(),
  inspection = useInspection();
const original = JSON.stringify(inspection.state.document);
expect(
  Object.isFrozen(isotopeCatalog) && isotopeCatalog.every(Object.isFrozen),
  "Catalog snapshot is mutable",
);
const selected = catalog.selected;
if (selected === undefined) throw new Error("Missing selection");
expect(
  !Reflect.set(selected, "protons", 999) && selected.protons === 10,
  "Selected catalog entry can be corrupted",
);
expect(isReadonly(catalog.results) && isReadonly(catalog.elements), "Catalog results are mutable");
for (const entry of isotopeCatalog) {
  const choice = createDiagram(entry.name);
  expect(
    entry.hasDiagram === hasDiagram(entry.name) && entry.hasDiagram === (choice !== null),
    "Availability differs from activation",
  );
  if (choice !== null)
    expect(choice.document.isotope?.name === entry.name, "Registry returned wrong isotope");
}
catalog.setFilter("query", "  nEoN ");
expect(catalog.results.length === 1, "Case/whitespace search failed");
catalog.resetFilters();
catalog.setFilter("element", "Oxygen");
expect(catalog.results.length === 3, "Element filter failed");
catalog.setFilter("mass", "18");
expect(
  catalog.results.length === 1 && catalog.results[0]?.name === "Oxygen-18",
  "Mass filter failed",
);
catalog.setFilter("mass", "99");
expect(catalog.results.length === 0, "Empty result failed");
catalog.resetFilters();
catalog.pin();
expect(catalog.state.references.length === 1, "Pin failed");
const reference = JSON.stringify(catalog.state.references[0]);
const pinned = catalog.state.references[0];
catalog.setFilter("query", "Neon");
catalog.resetFilters();
catalog.setFilter("mass", "20");
catalog.resetFilters();
expect(catalog.state.references[0] === pinned, "Filtering cloned pinned document");
const active = inspection.state.document;
inspection.toggleLabels();
inspection.run();
expect(inspection.state.document === active, "Labels/run cloned active document");
const route = inspection.state.route;
inspection.select({ kind: "none" });
expect(
  inspection.state.document === active && inspection.state.route === route,
  "Selection cloned document or route",
);
inspection.clearRoute();
expect(inspection.state.document === active, "Clear cloned active document");
inspection.showNeon();
inspection.run();
catalog.select("Sodium-23");
expect(
  inspection.activeDocument === null &&
    !inspection.state.playback.playing &&
    inspection.state.route === null,
  "Isotope switch retained graph/playback",
);
catalog.pin();
expect(catalog.state.references.length === 1, "Unavailable graph was pinned");
expect(
  JSON.stringify(catalog.state.references[0]) === reference,
  "Selection mutated pinned reference",
);
catalog.navigate(-1);
expect(JSON.stringify(inspection.state.document) === original, "Back did not restore Ne-20");
catalog.navigate(1);
expect(catalog.state.selected === "Sodium-23", "Forward failed");
catalog.navigate(-1);
catalog.select("Hydrogen-1");
expect(catalog.state.history.length === 2, "History branch not truncated");
catalog.select("invented");
expect(catalog.state.selected === "Hydrogen-1", "Invalid isotope accepted");
catalog.select("Neon-20");
catalog.pin();
expect(catalog.state.references.length === 0, "Pin toggle duplicated reference");
catalog.setSpeed("0");
expect(catalog.state.speed === "1", "Invalid speed accepted");
catalog.setSpeed("2");
expect(catalog.state.speed === "2", "Speed selector failed");
catalog.setTurn("right");
expect(catalog.state.initialTurn === "right", "Turn selector failed");
catalog.toggleDock();
catalog.toggleCounts();
expect(JSON.stringify(inspection.state.document) === original, "UI controls changed model");
console.log(
  "PASS: 96 catalog entries, filters, history, reference pins, unavailable diagrams and playback reset",
);
