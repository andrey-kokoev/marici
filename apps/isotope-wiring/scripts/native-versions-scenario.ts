import { nextTick } from "vue";
import { ScreenPointSchema, type ScreenPoint } from "../src/schemas/inspection.js";
import { useInspection } from "../src/vue/stores/inspection.js";
import { useVersions } from "../src/vue/stores/versions.js";
function expect(value: boolean, message: string): void {
  if (!value) throw new Error(message);
}
async function target(selector: string): Promise<ScreenPoint> {
  await nextTick();
  const node = document.querySelector(selector);
  if (!(node instanceof HTMLElement)) throw new Error("Missing target: " + selector);
  node.scrollIntoView({ block: "nearest", inline: "nearest" });
  await new Promise<void>((resolve) =>
    requestAnimationFrame(() => requestAnimationFrame(() => resolve())),
  );
  const bounds = node.getBoundingClientRect();
  const point = ScreenPointSchema.parse({
    x: bounds.x + bounds.width / 2,
    y: bounds.y + bounds.height / 2,
  });
  const hit = document.elementFromPoint(point.x, point.y);
  expect(
    hit === node || (hit !== null && node.contains(hit)),
    "Pointer target obscured: " + selector + " by " + hit?.tagName + "#" + hit?.id,
  );
  return point;
}
export async function summary(): Promise<ScreenPoint> {
  return target("#versions-toggle");
}
export async function name(): Promise<ScreenPoint> {
  await nextTick();
  expect(
    document.activeElement?.id === "version-name",
    "Opening Versions must focus the name field",
  );
  return target("#version-name");
}
export async function save(): Promise<ScreenPoint> {
  expect(
    document.activeElement?.id === "version-name",
    "Native typing did not focus the name input",
  );
  const input = document.getElementById("version-name");
  expect(
    input instanceof HTMLInputElement && input.value === "Native baseline",
    "Native typing did not update the input",
  );
  return target("#save-version");
}
export async function saved(): Promise<void> {
  await nextTick();
  const select = document.getElementById("saved-version");
  expect(
    select instanceof HTMLSelectElement && select.value === "Native baseline",
    "Native save failed: " + document.getElementById("version-error")?.textContent,
  );
  expect(document.activeElement?.id === "version-name", "Save stranded focus");
  // Change through the owning store, then restore using an actual native dialog.
  useInspection().cycleEdge("edge.ne20.4");
  await nextTick();
}
export async function load(): Promise<ScreenPoint> {
  return target("#load-version");
}
export async function loaded(): Promise<void> {
  await nextTick();
  const panel = document.getElementById("named-versions");
  expect(
    panel instanceof HTMLDialogElement &&
      !panel.open &&
      document.activeElement instanceof SVGSVGElement,
    "Load did not close and focus the graph",
  );
  expect(
    useInspection().activeDocument?.layout.edges.find((edge) => edge.edgeId === "edge.ne20.4")
      ?.color === "red",
    "Native confirmed load failed: " +
      document.getElementById("version-error")?.textContent +
      " " +
      useInspection().editError,
  );
}
export async function remove(): Promise<ScreenPoint> {
  return target("#delete-version");
}
export async function removed(): Promise<void> {
  await nextTick();
  expect(
    ["saved-version", "load-version", "delete-version"].every(
      (id) => document.getElementById(id) === null,
    ),
    "Deleting the last version must remove saved-version controls",
  );
  expect(
    document.activeElement?.id === "version-name" &&
      document.getElementById("versions-empty") !== null,
    "Delete must focus name and explain empty state",
  );
}
let beforeOutside = "";
export function outside(): ScreenPoint {
  const panel = document.getElementById("named-versions");
  if (!(panel instanceof HTMLDialogElement)) throw new Error("Missing dialog");
  const bounds = panel.getBoundingClientRect();
  beforeOutside = JSON.stringify([useInspection().activeDocument, useInspection().state.selection]);
  for (const edge of useInspection().activeDocument?.layout.edges ?? []) {
    if (edge.color !== "red" && edge.color !== "blue") continue;
    const box = document.getElementById("inspection-label-" + edge.edgeId)?.getBoundingClientRect();
    if (box === undefined || box.width === 0) continue;
    const x = box.x + box.width / 2,
      y = box.y + box.height / 2;
    if (
      x > 0 &&
      x < innerWidth &&
      y > 0 &&
      y < innerHeight &&
      (x < bounds.left || x > bounds.right || y < bounds.top || y > bounds.bottom)
    )
      return ScreenPointSchema.parse({ x, y });
  }
  throw new Error("No exposed colored edge for dismissal test");
}
export function closed(): void {
  const panel = document.getElementById("named-versions");
  expect(
    panel instanceof HTMLDialogElement &&
      !panel.open &&
      document.activeElement?.id === "versions-toggle",
    "Dismissal must close and return focus",
  );
}
function compactBounds(): void {
  const panel = document.getElementById("named-versions");
  if (!(panel instanceof HTMLDialogElement)) throw new Error("Missing dialog");
  const bounds = panel.getBoundingClientRect();
  expect(
    bounds.left >= 0 &&
      bounds.top >= 0 &&
      bounds.right <= innerWidth &&
      bounds.bottom <= innerHeight,
    "Compact dialog outside viewport",
  );
}
export async function compact(): Promise<void> {
  const longName = "Long snapshot name ".repeat(4).trim();
  expect(useVersions().save(longName), "Could not create populated long-name fixture");
  await nextTick();
  compactBounds();
  const badge = document.querySelector("#version-working-state .version-status");
  expect(
    badge instanceof HTMLElement && badge.offsetWidth >= badge.scrollWidth,
    "Status badge was truncated with the name",
  );
  for (const id of [
    "version-name",
    "save-version",
    "saved-version",
    "load-version",
    "delete-version",
    "refresh-versions",
  ]) {
    const node = document.getElementById(id);
    if (node === null) throw new Error("Missing populated control: " + id);
    node.scrollIntoView({ block: "nearest" });
    await target("#" + id);
  }
  await target('[aria-label="Close versions"]');
  const feedback = document.getElementById("version-notice")?.getBoundingClientRect();
  expect(
    feedback !== undefined && feedback.top >= 0 && feedback.bottom <= innerHeight,
    "Feedback hidden on short viewport",
  );
  expect(useVersions().remove(longName), "Could not clean up long-name fixture");
}
export async function compactEmpty(): Promise<void> {
  compactBounds();
  expect(
    ["saved-version", "load-version", "delete-version"].every(
      (id) => document.getElementById(id) === null,
    ),
    "Empty compact dialog offered snapshot actions",
  );
  expect(document.getElementById("versions-empty") !== null, "Missing compact empty state");
  for (const id of ["version-name", "save-version", "refresh-versions"]) {
    document.getElementById(id)?.scrollIntoView({ block: "nearest" });
    await target("#" + id);
  }
}
let beforeMorse = "";
function morseState(): string {
  return JSON.stringify([
    useInspection().state,
    document.querySelector(".active-diagram svg")?.getAttribute("viewBox"),
    Object.keys(localStorage)
      .sort()
      .map((key) => [key, localStorage.getItem(key)]),
  ]);
}
export async function morseOpen(): Promise<ScreenPoint> {
  beforeMorse = morseState();
  return target("#morse-toggle");
}
export async function morseCheck(): Promise<void> {
  await nextTick();
  const panel = document.getElementById("morse-surface");
  expect(panel instanceof HTMLDialogElement && panel.open, "Morse surface did not open");
  const values = Array.from(document.querySelectorAll("#morse-invariants dd")).map((node) =>
    node.textContent?.trim(),
  );
  expect(
    values.join(",") === "1,5,6,-14,15,10 / 24 / 0",
    "Incorrect live Morse surface invariants",
  );
  expect(
    document.getElementById("morse-cancellations")?.textContent?.includes("Edges 8 and 9") === true,
    "Reduced decomposition must explain its cancellations",
  );
}
export async function morseClose(): Promise<ScreenPoint> {
  return target('[aria-label="Close Morse surface"]');
}
export function morseClosed(): void {
  const panel = document.getElementById("morse-surface");
  expect(
    panel instanceof HTMLDialogElement &&
      !panel.open &&
      document.activeElement?.id === "morse-toggle",
    "Morse close did not return focus",
  );
  expect(
    beforeMorse === morseState(),
    "Morse inspection changed the diagram, route, camera or storage",
  );
}
export function outsideClosed(): void {
  closed();
  expect(
    beforeOutside ===
      JSON.stringify([useInspection().activeDocument, useInspection().state.selection]),
    "Outside dismissal edited the graph",
  );
}
