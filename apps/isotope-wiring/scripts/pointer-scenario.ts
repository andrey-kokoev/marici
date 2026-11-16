import { nextTick } from "vue";
import { ScreenPointSchema, type ScreenPoint } from "../src/schemas/inspection.js";
let initialBox: string | null = null;
let capturedId: number | null = null;
let surface: SVGSVGElement | null = null;
function expect(value: boolean, message: string): void {
  if (!value) throw new Error(message);
}
function button(label: string): HTMLButtonElement {
  const value = Array.from(document.querySelectorAll("button")).find(
    (item) => item.textContent?.trim() === label || item.getAttribute("aria-label") === label,
  );
  if (value === undefined) throw new Error(`Missing ${label}`);
  return value;
}
export function ready(): boolean {
  return document.querySelector(".active-diagram svg") instanceof SVGSVGElement;
}
export async function prepare(): Promise<ScreenPoint> {
  if (document.querySelector("#catalog") !== null) button("Close isotope catalog").click();
  button("Fit graph").click();
  if (button("Move").getAttribute("aria-pressed") !== "true") button("Move").click();
  await nextTick();
  const svg = document.querySelector(".active-diagram svg");
  if (!(svg instanceof SVGSVGElement)) throw new Error("Missing SVG");
  if (surface !== svg)
    svg.addEventListener("gotpointercapture", (event) => {
      capturedId = event.pointerId;
    });
  surface = svg;
  capturedId = null;
  initialBox = svg.getAttribute("viewBox");
  svg.focus();
  const bounds = svg.getBoundingClientRect();
  return ScreenPointSchema.parse({
    x: Math.round(bounds.x + bounds.width / 2),
    y: Math.round(bounds.y + bounds.height / 2),
  });
}
export function captured(): void {
  expect(
    surface !== null &&
      capturedId !== null &&
      surface.hasPointerCapture(capturedId) &&
      surface.classList.contains("dragging"),
    "Native pointer not captured",
  );
}
export function released(): void {
  expect(
    surface !== null &&
      capturedId !== null &&
      !surface.hasPointerCapture(capturedId) &&
      !surface.classList.contains("dragging"),
    "Pointer capture/drag state not released",
  );
}
export function moved(): void {
  released();
  expect(surface?.getAttribute("viewBox") !== initialBox, "Native drag did not pan");
  const select = document.querySelector("#start-edge");
  expect(
    select instanceof HTMLSelectElement && select.value === "edge.ne20.8",
    "Drag changed selected edge",
  );
}
export function disableMove(): void {
  button("Move").click();
}
export async function removeDiagram(): Promise<void> {
  const picker = document.getElementById("catalog-toggle");
  if (!(picker instanceof HTMLButtonElement)) throw new Error("Missing catalog toggle");
  picker.click();
  await nextTick();
  const entry = Array.from(document.querySelectorAll(".catalog-item>button")).find(
    (value) => value.querySelector("strong")?.textContent === "Sodium-23",
  );
  if (!(entry instanceof HTMLButtonElement)) throw new Error("Missing Sodium-23");
  entry.click();
}
export function removed(): void {
  expect(document.querySelector(".active-diagram svg") === null, "Diagram not removed");
  expect(
    surface !== null && capturedId !== null && !surface.hasPointerCapture(capturedId),
    "Removed SVG retained pointer capture",
  );
}
