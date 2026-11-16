import { z } from "zod";
let failure = "Browser scenario did not finish";
function expect(value: boolean, message: string): void {
  if (!value) {
    failure = message;
    throw new Error(message);
  }
}
function button(label: string): HTMLButtonElement {
  const value = Array.from(document.querySelectorAll("button")).find(
    (item) => item.textContent?.trim() === label || item.getAttribute("aria-label") === label,
  );
  if (value === undefined) {
    failure = `Missing button: ${label}`;
    throw new Error(failure);
  }
  return value;
}
function click(selector: string): void {
  const node = document.querySelector(selector);
  if (!(node instanceof HTMLButtonElement)) {
    failure = `Missing ${selector}`;
    throw new Error(failure);
  }
  node.click();
}
function value(selector: string, text: string): void {
  const node = document.querySelector(selector);
  if (!(node instanceof HTMLInputElement || node instanceof HTMLSelectElement)) {
    failure = `Missing ${selector}`;
    throw new Error(failure);
  }
  node.value = text;
  node.dispatchEvent(
    new Event(node instanceof HTMLSelectElement ? "change" : "input", { bubbles: true }),
  );
}
function expectSeparatedLabels(selector: string): void {
  const labels = Array.from(document.querySelectorAll(selector));
  expect(labels.length === 26, "Missing labels in collision check");
  for (let i = 0; i < labels.length; i += 1) {
    const a = labels[i];
    if (a === undefined) throw new Error("Missing label");
    const geometry = a.closest("svg")?.querySelectorAll("polyline");
    const lastLine = geometry?.item(geometry.length - 1);
    expect(
      lastLine !== undefined &&
        (a.compareDocumentPosition(lastLine) & Node.DOCUMENT_POSITION_PRECEDING) !== 0,
      "A later edge stroke can cover a label",
    );
    const box = a.getBoundingClientRect();
    expect(box.width > 0 && box.height > 0, "Label is not visible");
    for (const b of labels.slice(i + 1)) {
      const other = b.getBoundingClientRect();
      expect(
        box.right <= other.left ||
          other.right <= box.left ||
          box.bottom <= other.top ||
          other.bottom <= box.top,
        `Rendered labels overlap: ${a.textContent}/${b.textContent}`,
      );
    }
  }
}
function expectMidpointArrows(selector: string): void {
  const svg = document.querySelector(selector);
  if (svg === null) throw new Error("Missing arrow-check graph");
  expect(svg.querySelector("[marker-start], [marker-end]") === null, "Endpoint arrow remains");
  expect(svg.querySelectorAll(".direction-arrow").length === 16, "Wrong directed arrow count");
  for (const group of svg.querySelectorAll("g")) {
    const line = group.querySelector("polyline");
    if (line === null) throw new Error("Missing edge line");
    const arrow = group.querySelector(".direction-arrow");
    if (line.getAttribute("stroke") === "var(--green)") {
      expect(arrow === null, "Green edge has a direction arrow");
      continue;
    }
    if (!(arrow instanceof SVGPathElement)) throw new Error("Missing centered arrow");
    const a = line.points.getItem(0),
      b = line.points.getItem(line.points.numberOfItems - 1);
    const matrix = arrow.transform.baseVal.consolidate()?.matrix;
    const length = Math.hypot(b.x - a.x, b.y - a.y);
    expect(
      matrix !== undefined &&
        Math.abs(matrix.e - (a.x + b.x) / 2) < 1e-9 &&
        Math.abs(matrix.f - (a.y + b.y) / 2) < 1e-9 &&
        Math.abs(matrix.a - (b.x - a.x) / length) < 1e-9 &&
        Math.abs(matrix.b - (b.y - a.y) / length) < 1e-9,
      "Arrow must be centered and follow the authored direction",
    );
  }
}
function expectStableGraph(bounds: DOMRect): void {
  const current = document.querySelector(".active-diagram svg")?.getBoundingClientRect();
  const viewport = document.querySelector(".active-diagram")?.getBoundingClientRect();
  expect(
    document.querySelector(
      ".active-diagram button, .active-diagram select, .active-diagram input",
    ) === null,
    "All toolbar controls, including playback actions, must be in the appbar",
  );
  expect(button("Clear path").closest(".appbar") !== null, "Playback toolbar is outside appbar");
  expect(
    document.querySelector(".appbar #diagram-toolbar .toolbar") !== null &&
      document.querySelector(".active-diagram .toolbar") === null,
    "Toolbar must live in the appbar, not the viewport",
  );
  expect(
    current !== undefined &&
      viewport !== undefined &&
      Math.abs(current.x - viewport.x) < 1 &&
      Math.abs(current.y - viewport.y) < 1 &&
      Math.abs(current.width - viewport.width) < 1 &&
      Math.abs(current.height - viewport.height) < 1,
    "Title or controls reserved space outside the drawing viewport",
  );
  for (const selector of [".diagram-title", ".route-readouts"]) {
    const overlay = document.querySelector(selector);
    if (!(overlay instanceof HTMLElement) || viewport === undefined)
      throw new Error("Missing viewport overlay");
    const box = overlay.getBoundingClientRect();
    expect(
      getComputedStyle(overlay).position === "absolute" &&
        box.left >= viewport.left &&
        box.right <= viewport.right + 1 &&
        box.top >= viewport.top &&
        box.bottom <= viewport.bottom + 1,
      "Controls must stay inside the full drawing viewport",
    );
  }
  expect(
    current !== undefined &&
      current.x === bounds.x &&
      current.y === bounds.y &&
      current.width === bounds.width &&
      current.height === bounds.height,
    "Playback shifted or resized diagram",
  );
}
const pause = () => new Promise<void>((resolve) => setTimeout(resolve, 50));
async function scenario(): Promise<void> {
  const scale = new URL(window.location.href).searchParams.get("scale");
  expect(scale === "1" || scale === "2", "Missing browser configuration");
  expect(window.devicePixelRatio === Number(scale), "Device-scale flag not applied");
  expect(
    scale === "1" ? window.innerWidth >= 900 : window.innerWidth <= 600,
    "Viewport flag not applied",
  );
  for (let i = 0; i < 100 && document.querySelector("#diagram-heading") === null; i += 1)
    await pause();
  expect(getComputedStyle(document.documentElement).colorScheme === "dark", "Dark theme missing");
  expect(
    getComputedStyle(document.documentElement).getPropertyValue("--paper").trim() === "#1b1b1f",
    "Legacy dark palette changed",
  );
  expect(document.querySelectorAll("svg g").length === 26, "Ne-20 must render immediately");
  expect(document.querySelectorAll("svg circle").length === 12, "Missing vertices");
  expect(document.querySelectorAll("svg text").length === 26, "Missing labels");
  for (const label of [1, 2, 3, 4, 13, 14, 15, 16, 18, 19, 20, 21]) {
    const line = document
      .getElementById(`inspection-edge.ne20.${label}`)
      ?.querySelector("polyline");
    if (!(line instanceof SVGPolylineElement)) throw new Error("Missing shell-2 side");
    expect(line.points.numberOfItems === 2, "Unexpected shell-2 polyline");
    const start = line.points.getItem(0),
      end = line.points.getItem(1);
    expect(
      ([13, 15, 19].includes(label) ? end.x < start.x : end.x > start.x) &&
        Math.abs(end.x - start.x) === Math.abs(end.y - start.y) &&
        line.getAttribute("stroke") ===
          ([4, 15, 19, 16, 20].includes(label)
            ? "var(--red)"
            : [2, 13, 14].includes(label)
              ? "var(--blue)"
              : end.y > start.y
                ? "var(--red)"
                : "var(--blue)") &&
        !line.hasAttribute("marker-end") &&
        !line.hasAttribute("marker-start"),
      `Shell-2 edge ${label} color/direction must respect the existing 13/14 blue, 16/20 red overrides`,
    );
  }
  for (const label of [6, 7, 12, 17, 22, 23, 24, 25, 26, 27]) {
    const line = document
      .getElementById(`inspection-edge.ne20.${label}`)
      ?.querySelector("polyline");
    expect(
      line !== undefined &&
        line !== null &&
        !line.hasAttribute("marker-start") &&
        !line.hasAttribute("marker-end"),
      "Undirected green segment has arrowheads",
    );
  }
  expect(
    document.querySelector("#record-inspector, pre, input[type=file], a[download]") === null,
    "Removed panels returned",
  );
  expect(
    !/scientific review|offline readiness|under construction|authoritative records|coincident positions|proposed conventions/i.test(
      document.querySelector("main")?.textContent ?? "",
    ),
    "Disclaimer text returned",
  );
  for (const label of [23, 24, 25, 26]) {
    value("#start-edge", `edge.ne20.${label}`);
    await pause();
    expect(
      document
        .getElementById(`inspection-edge.ne20.${label}`)
        ?.querySelector("polyline")
        ?.getAttribute("stroke-width") === "4",
      `Diagonal ${label} cannot be selected independently`,
    );
  }
  value("#start-edge", "edge.ne20.8");
  await pause();
  click('[aria-label="Pin active isotope as reference"]');
  await pause();
  expect(document.querySelectorAll("svg g").length === 52, "Pin did not create reference graph");
  for (const line of document.querySelectorAll('.reference-card polyline[stroke="var(--green)"]'))
    expect(
      !line.hasAttribute("marker-start") && !line.hasAttribute("marker-end"),
      "Reference green segment has arrows",
    );
  expect(
    document.querySelectorAll(".reference-card svg circle").length === 12,
    "Pinned graph omitted vertices",
  );
  expect(
    document.querySelector(".reference-card svg [tabindex]") === null,
    "Reference graph acquired editing/selection tab stops",
  );
  const activePoints = Array.from(document.querySelectorAll(".active-diagram svg g")).map((edge) =>
    edge.querySelector("polyline")?.getAttribute("points"),
  );
  const referencePoints = Array.from(document.querySelectorAll(".reference-card svg g")).map(
    (edge) => edge.querySelector("polyline")?.getAttribute("points"),
  );
  expect(
    JSON.stringify(activePoints) === JSON.stringify(referencePoints),
    "Pinned graph differs from active geometry",
  );
  expectMidpointArrows(".active-diagram svg");
  expectMidpointArrows(".reference-card svg");
  expectSeparatedLabels(".active-diagram svg text");
  expectSeparatedLabels(".reference-card svg text");
  const label22 = document.getElementById("inspection-label-edge.ne20.22");
  if (label22 === null) throw new Error("Missing label 22");
  label22.dispatchEvent(new MouseEvent("click", { bubbles: true }));
  await pause();
  expect(
    document
      .getElementById("inspection-edge.ne20.22")
      ?.querySelector("polyline")
      ?.getAttribute("stroke-width") === "4",
    "Displaced label must still select its own edge",
  );
  value('[aria-label="Search isotope catalog"]', "Neon");
  await pause();
  expect(document.querySelectorAll(".catalog-item").length === 1, "Search failed");
  value('[aria-label="Search isotope catalog"]', "");
  value('[aria-label="Element"]', "Oxygen");
  value('[aria-label="Mass number"]', "18");
  await pause();
  expect(document.querySelectorAll(".catalog-item").length === 1, "Element/mass filters failed");
  click(".catalog-item button");
  await pause();
  expect(
    document.querySelector("#diagram-heading")?.textContent === "Oxygen-18",
    "Catalog selection failed",
  );
  expect(
    document.querySelectorAll(".active-diagram svg g").length === 24 &&
      document.querySelectorAll("svg g").length === 50,
    "Oxygen-18 graph or retained Ne20 reference is missing",
  );
  click('[aria-label="Previous isotope"]');
  await pause();
  expect(document.querySelectorAll("svg g").length === 52, "Back navigation lost graph or pin");
  click('[aria-label="Unpin Neon-20 reference"]');
  await pause();
  expect(document.querySelectorAll("svg g").length === 26, "Unpin failed");
  if (document.querySelector("#catalog") === null) {
    click("#catalog-toggle");
    await pause();
  }
  button("Reset filters").click();
  await pause();
  expect(document.querySelectorAll(".catalog-item").length === 96, "Reset filters failed");
  click("#catalog-pin");
  await pause();
  expect(
    document.querySelector("#catalog")?.classList.contains("floating") === true,
    "Undock failed",
  );
  click("#catalog-pin");
  await pause();
  click('[aria-label="Close isotope catalog"]');
  await pause();
  expect(document.activeElement?.id === "catalog-toggle", "Catalog close lost keyboard focus");
  expect(
    document.getElementById("inspection-edge.ne20.5") === null &&
      document.getElementById("inspection-label-edge.ne20.5") === null,
    "Duplicate edge 5 must not be rendered",
  );
  for (const label of ["18"]) {
    value("#start-edge", `edge.ne20.${label}`);
    await pause();
    expect(
      document
        .getElementById(`inspection-edge.ne20.${label}`)
        ?.querySelector("polyline")
        ?.getAttribute("stroke-width") === "4",
      "Overlapping edge cannot be selected",
    );
  }
  value("#playback-speed", "2");
  await pause();
  value("#playback-speed", "1");
  value("#start-edge", "edge.ne20.8");
  await pause();
  const graphBounds = document.querySelector(".active-diagram svg")?.getBoundingClientRect();
  if (graphBounds === undefined) throw new Error("Missing graph bounds");
  expect(
    button("Start").textContent?.trim() === "|>" &&
      button("step back").disabled &&
      button("step back").title === "step back" &&
      button("step forward").title === "step forward",
    "Initial playback icons/stepper titles are wrong",
  );
  button("step forward").click();
  await pause();
  expect(
    button("Resume").textContent?.trim() === "|>" &&
      document.querySelector("#path-taken")?.textContent?.includes("8 → 12") === true,
    "Forward must initialize a paused route and advance one segment",
  );
  button("step back").click();
  await pause();
  expect(
    button("step back").disabled &&
      document.querySelector("#path-taken")?.textContent?.trim() === "Path taken: 8",
    "Back must return to the initial boundary",
  );
  button("Clear path").click();
  await pause();
  button("Start").click();
  await pause();
  expect(
    button("Pause").textContent?.trim() === "||" &&
      document.querySelectorAll("#play-pause").length === 1,
    "Playback must use one state-dependent button",
  );
  expectStableGraph(graphBounds);
  expect(
    document.querySelector("#path-taken")?.textContent?.trim() === "Path taken: 8",
    "Readout revealed future edges",
  );
  const startX = document.querySelector("#route-marker")?.getAttribute("cx");
  await pause();
  expect(
    startX !== undefined && document.querySelector("#route-marker")?.getAttribute("cx") !== startX,
    "Marker did not move",
  );
  button("Pause").click();
  await pause();
  expectStableGraph(graphBounds);
  const pausedX = document.querySelector("#route-marker")?.getAttribute("cx");
  await pause();
  expect(
    document.querySelector("#route-marker")?.getAttribute("cx") === pausedX,
    "Pause did not freeze marker",
  );
  const graph = document.querySelector(".active-diagram svg");
  if (!(graph instanceof SVGSVGElement)) throw new Error("Missing camera surface");
  const fitBox = graph.getAttribute("viewBox"),
    pausedPath = document.querySelector("#path-taken")?.textContent;
  click('[aria-label="Zoom in"]');
  await pause();
  expect(graph.getAttribute("viewBox") !== fitBox, "Zoom control failed");
  const zoomedBox = graph.getAttribute("viewBox");
  for (const modifier of ["ctrlKey", "metaKey", "altKey"])
    for (const key of ["f", "+", "-"]) {
      const event = new KeyboardEvent("keydown", {
        key,
        [modifier]: true,
        bubbles: true,
        cancelable: true,
      });
      graph.dispatchEvent(event);
      await pause();
      expect(
        !event.defaultPrevented && graph.getAttribute("viewBox") === zoomedBox,
        "Camera hijacked modified shortcut",
      );
    }
  button("Move").click();
  await pause();
  graph.focus();
  graph.dispatchEvent(
    new KeyboardEvent("keydown", { key: "ArrowRight", bubbles: true, cancelable: true }),
  );
  await pause();
  expect(graph.getAttribute("viewBox") !== zoomedBox, "Keyboard pan failed");
  document
    .getElementById("inspection-edge.ne20.18")
    ?.dispatchEvent(new MouseEvent("click", { bubbles: true }));
  await pause();
  const startSelector = document.querySelector("#start-edge");
  expect(
    startSelector instanceof HTMLSelectElement && startSelector.value === "edge.ne20.8",
    "Move selected an edge",
  );
  graph.dispatchEvent(new KeyboardEvent("keydown", { key: "Escape", bubbles: true }));
  await pause();
  expect(button("Move").getAttribute("aria-pressed") === "false", "Escape did not leave Move mode");
  click('[aria-label="Fit graph"]');
  await pause();
  expect(graph.getAttribute("viewBox") === fitBox, "Fit failed");
  const matrix = graph.getScreenCTM();
  if (matrix === null) throw new Error("Missing SVG transform");
  const pointer = new DOMPoint(
    Math.round(graphBounds.x + graphBounds.width / 3),
    Math.round(graphBounds.y + graphBounds.height / 3),
  );
  const beforeWheel = pointer.matrixTransform(matrix.inverse());
  graph.dispatchEvent(
    new WheelEvent("wheel", {
      clientX: pointer.x,
      clientY: pointer.y,
      deltaY: -120,
      bubbles: true,
      cancelable: true,
    }),
  );
  await pause();
  const afterMatrix = graph.getScreenCTM();
  if (afterMatrix === null) throw new Error("Missing zoom transform");
  // SVG viewBox storage is float precision; compare the retained anchor in screen pixels.
  const retainedAnchor = beforeWheel.matrixTransform(afterMatrix);
  expect(
    graph.getAttribute("viewBox") !== fitBox &&
      Math.abs(retainedAnchor.x - pointer.x) < 0.01 &&
      Math.abs(retainedAnchor.y - pointer.y) < 0.01,
    "Wheel zoom did not preserve cursor anchor within 0.01 screen pixels",
  );
  const pixelBox = graph.getAttribute("viewBox");
  click('[aria-label="Fit graph"]');
  await pause();
  graph.dispatchEvent(
    new WheelEvent("wheel", {
      clientX: pointer.x,
      clientY: pointer.y,
      deltaY: -7.5,
      deltaMode: WheelEvent.DOM_DELTA_LINE,
      bubbles: true,
      cancelable: true,
    }),
  );
  await pause();
  expect(graph.getAttribute("viewBox") === pixelBox, "Wheel deltaMode was ignored");
  expect(
    document.querySelector("#path-taken")?.textContent === pausedPath &&
      document.querySelector("#route-marker")?.getAttribute("cx") === pausedX,
    "Camera changed playback",
  );
  click('[aria-label="Fit graph"]');
  await pause();
  expectStableGraph(graphBounds);
  value("#playback-speed", "4");
  button("Resume").click();
  await pause();
  for (
    let i = 0;
    i < 200 &&
    Array.from(document.querySelectorAll("button")).some(
      (value) => value.getAttribute("aria-label") === "Pause",
    );
    i += 1
  )
    await pause();
  expect(
    !Array.from(document.querySelectorAll("button")).some(
      (value) => value.getAttribute("aria-label") === "Pause",
    ),
    "Playback did not stop",
  );
  expectStableGraph(graphBounds);
  expect(
    button("Restart").textContent?.trim() === "|>" && button("step forward").disabled,
    "Completed playback must offer restart and disable forward",
  );
  button("step back").click();
  await pause();
  expect(
    !button("step forward").disabled && button("Resume").textContent?.trim() === "|>",
    "Back from completion must allow paused inspection",
  );
  button("step forward").click();
  await pause();
  const status = document.querySelector("#route-status");
  expect(
    status instanceof HTMLElement &&
      status.tabIndex === 0 &&
      getComputedStyle(status).overflowY === "auto" &&
      getComputedStyle(status).whiteSpace === "normal",
    "Stop reason is clipped or not keyboard-scrollable",
  );
  const trace = document.querySelector("#path-taken")?.textContent;
  expect(
    trace?.includes("8 → 12 → 10 → 3 → 7 → 21") === true,
    "Keep-left/right must continue through 7 to 21",
  );
  expect(
    trace?.trim() ===
      "Path taken: 8 → 12 → 10 → 3 → 7 → 21 → 4 → 20 → 19 → 7 → 17 → 15 → 16 → 1 → 11 → 12 → 9 → 27 → 23 → 24",
    "Playback must take eligible same-color arrows before green connectors",
  );
  expect(
    status?.textContent?.includes("unvisited blue edges") === true,
    "The blocked blue phase must be reported honestly",
  );
  const checkbox = document.querySelector("#edge-labels");
  if (!(checkbox instanceof HTMLInputElement)) throw new Error("Missing labels checkbox");
  checkbox.click();
  await pause();
  expect(
    document.querySelectorAll("svg text").length === 0 &&
      document.querySelectorAll("svg g").length === 26,
    "Label toggle changed graph",
  );
  expect(
    document.querySelector("#path-taken")?.textContent === trace,
    "Label toggle changed route",
  );
  checkbox.click();
  await pause();
  expect(document.querySelectorAll("svg text").length === 26, "Labels did not return");
  button("Clear path").click();
  await pause();
  expect(
    document.querySelector("#path-taken")?.textContent?.includes("—") === true,
    "Path not cleared",
  );
  expectStableGraph(graphBounds);
  expect(document.querySelector("#route-marker") === null, "Clear left marker behind");
  value("#playback-speed", "1");
  button("Start").click();
  await pause();
  expect(
    document.querySelector("#path-taken")?.textContent?.trim() === "Path taken: 8",
    "Restart did not reset playback",
  );
  expect(document.querySelector("#route-marker") !== null, "Restart did not restore marker");
  button("Clear path").click();
  await pause();
  expect(document.querySelector("#route-marker") === null, "Clear during playback failed");
  const drawings = z.array(z.tuple([z.string(), z.string(), z.int(), z.int(), z.int()])).parse([
    ["Hydrogen-1", "h1", 2, 3, 2],
    ["Hydrogen-2", "h2", 3, 3, 2],
    ["Helium-3", "he3", 5, 4, 4],
    ["Helium-4", "he4", 6, 4, 4],
    ["Lithium-6", "li6", 8, 6, 6],
    ["Lithium-7", "li7", 10, 6, 6],
    ["Beryllium-9", "be9", 12, 7, 8],
    ["Boron-10", "b10", 13, 9, 10],
    ["Boron-11", "b11", 15, 9, 10],
    ["Carbon-12", "c12", 15, 10, 12],
    ["Carbon-13", "c13", 17, 10, 12],
    ["Nitrogen-14", "n14", 18, 12, 14],
    ["Nitrogen-15", "n15", 20, 12, 14],
    ["Oxygen-16", "o16", 20, 13, 16],
    ["Oxygen-17", "o17", 22, 13, 16],
    ["Oxygen-18", "o18", 24, 13, 16],
    ["Fluorine-19", "f19", 27, 15, 18],
  ]);
  for (const [name, key, edges, vertices, arrows] of drawings) {
    if (document.querySelector("#catalog") === null) {
      click("#catalog-toggle");
      await pause();
    }
    value('[aria-label="Search isotope catalog"]', name);
    await pause();
    click(".catalog-item button");
    await pause();
    expect(
      document.querySelector("#diagram-heading")?.textContent === name,
      `${name}: wrong selection`,
    );
    expect(
      document.querySelectorAll(".active-diagram svg g").length === edges &&
        document.querySelectorAll(".active-diagram svg circle").length === vertices,
      `${name}: missing geometry`,
    );
    expect(
      document.querySelectorAll(".active-diagram svg text").length === edges,
      `${name}: labels missing`,
    );
    expect(
      document.querySelectorAll(".active-diagram .direction-arrow").length === arrows,
      `${name}: missing authored arrows`,
    );
    expect(
      Array.from(document.querySelectorAll(".appbar .toolbar button")).some(
        (button) => button.getAttribute("aria-label") === "Start",
      ),
      `${name}: route controls are missing`,
    );
    if (name === "Helium-4")
      for (const label of [5, 6]) {
        value("#start-edge", `edge.he4.${label}`);
        await pause();
        expect(
          document
            .getElementById(`inspection-edge.he4.${label}`)
            ?.querySelector("polyline")
            ?.getAttribute("stroke-width") === "4",
          "He-4 crossing edge cannot be selected independently",
        );
      }
    expect(
      document.querySelector("#route-marker") === null &&
        document
          .querySelector("#route-status")
          ?.textContent?.includes("Traversal is unavailable") !== true,
      `${name}: stale animation or unresolved policy`,
    );
    if (document.querySelector("#catalog") === null) {
      click("#catalog-toggle");
      await pause();
    }
    click('[aria-label="Pin active isotope as reference"]');
    await pause();
    expect(
      document.querySelectorAll(".reference-card svg circle").length === vertices &&
        document.querySelectorAll(".reference-card .direction-arrow").length === arrows,
      `${name}: reference mismatch`,
    );
    const referenceBefore = document.querySelector(".reference-card svg")?.innerHTML;
    const edited = document.getElementById(`inspection-edge.${key}.1`);
    if (edited === null) throw new Error(`${name}: missing editable edge`);
    const stroke = edited.querySelector("polyline")?.getAttribute("stroke");
    const arrow = edited.querySelector(".direction-arrow")?.getAttribute("transform");
    edited.dispatchEvent(new MouseEvent("click", { bubbles: true }));
    await pause();
    expect(
      edited.querySelector("polyline")?.getAttribute("stroke") !== stroke,
      `${name}: color click failed`,
    );
    edited.dispatchEvent(new MouseEvent("click", { bubbles: true }));
    await pause();
    expect(
      edited.querySelector(".direction-arrow")?.getAttribute("transform") !== arrow,
      `${name}: arrow reversal failed`,
    );
    expect(
      document.querySelector(".reference-card svg")?.innerHTML === referenceBefore,
      `${name}: editing mutated pinned reference`,
    );
    click(`[aria-label="Unpin ${name} reference"]`);
    await pause();
  }
}
const output = document.querySelector("#browser-result");
if (!(output instanceof HTMLOutputElement)) throw new Error("Missing browser result element");
try {
  await scenario();
  output.dataset["status"] = "pass";
  output.textContent = "PASS: diagram, selection, labels, routing and removed UI regressions";
} catch {
  output.dataset["status"] = "fail";
  output.textContent = `FAIL: ${failure}`;
}
