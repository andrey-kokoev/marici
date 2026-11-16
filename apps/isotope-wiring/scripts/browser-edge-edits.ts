import {
  EDGE_EDITS_PREFIX,
  encodeEdgeEdits,
  decodeEdgeEditsExact,
} from "../src/edge-edit-storage.js";
import { SavedEdgeEditsSchema } from "../src/schemas/edge-edits.js";
import { neon20 } from "../src/examples/neon20.js";
const storageKey = EDGE_EDITS_PREFIX + "diagram.ne20";
const pause = () => new Promise<void>((resolve) => setTimeout(resolve, 50));
let failure = "Edge-edit persistence workflow did not finish";
function expect(value: boolean, message: string): void {
  if (!value) {
    failure = message;
    throw new Error(message);
  }
}
function button(selector: string): HTMLButtonElement {
  const node = document.querySelector(selector);
  if (!(node instanceof HTMLButtonElement)) throw new Error("Missing button " + selector);
  return node;
}
function line(id: number): SVGPolylineElement {
  const node = document.getElementById(`inspection-edge.ne20.${id}`)?.querySelector("polyline");
  if (node === null || node === undefined) throw new Error("Missing line");
  return node;
}
function arrowX(id: number): number {
  const node = document
    .getElementById(`inspection-edge.ne20.${id}`)
    ?.querySelector(".direction-arrow");
  if (!(node instanceof SVGPathElement)) throw new Error("Missing arrow");
  return node.transform.baseVal.consolidate()?.matrix.a ?? 0;
}
async function clickEdge(id: number, label = false): Promise<void> {
  const node = document.getElementById(
    label ? `inspection-label-edge.ne20.${id}` : `inspection-edge.ne20.${id}`,
  );
  if (node === null) throw new Error("Missing edge click target");
  const select = document.getElementById("start-edge");
  if (!(select instanceof HTMLSelectElement)) throw new Error("Missing start selector");
  const startEdge = select.value;
  node.dispatchEvent(new MouseEvent("click", { bubbles: true }));
  await pause();
  if (id !== 22) expect(select.value === startEdge, "Editing must preserve the chosen start edge");
}
async function scenario(): Promise<boolean> {
  for (let i = 0; i < 100 && document.getElementById("inspection-edge.ne20.4") === null; i += 1)
    await pause();
  expect(
    document.getElementById("inspection-edge.ne20.4") !== null,
    "Active diagram did not mount within the readiness budget",
  );
  // Let mount/Teleport listeners settle before the first synthetic click.
  await pause();
  const stage = new URL(location.href).searchParams.get("stage") ?? "edit";
  if (stage === "edit") {
    expect(localStorage.getItem(storageKey) === null, "Test profile is not isolated");
    expect(
      document.getElementById("color-balance-error")?.textContent?.includes("9 red, 7 blue") ===
        true,
      "An unbalanced loaded diagram must show its counts immediately",
    );
    await clickEdge(22, true);
    expect(
      decodeEdgeEditsExact(localStorage.getItem(storageKey) ?? "").edges.length === 0,
      "Green selection must not create a color/direction override",
    );
    const originalSet = Object.getOwnPropertyDescriptor(Storage.prototype, "setItem");
    if (originalSet === undefined) throw new Error("Missing native storage descriptor");
    try {
      Storage.prototype.setItem = () => {
        throw new DOMException("Test quota denial", "QuotaExceededError");
      };
      await clickEdge(4);
      expect(
        line(4).getAttribute("stroke") === "var(--red)" &&
          document.getElementById("edge-edit-error") !== null,
        "Failed save must be visible without changing the model",
      );
    } finally {
      Object.defineProperty(Storage.prototype, "setItem", originalSet);
    }
    const select = document.getElementById("start-edge");
    if (!(select instanceof HTMLSelectElement)) throw new Error("Missing start selector");
    select.value = "edge.ne20.8";
    select.dispatchEvent(new Event("change", { bubbles: true }));
    await pause();
    if (document.getElementById("catalog") === null) {
      button("#catalog-toggle").click();
      await pause();
    }
    button('[aria-label="Pin active isotope as reference"]').click();
    await pause();
    button("#play-pause").click();
    await pause();
    button('[aria-label="Zoom in"]').click();
    await pause();
    const box = document.querySelector(".active-diagram svg")?.getAttribute("viewBox");
    const geometry = Array.from(document.querySelectorAll(".active-diagram svg g"))
      .map((group) => group.querySelector("polyline")?.getAttribute("points"))
      .join("|");
    await clickEdge(4);
    expect(
      line(4).getAttribute("stroke") === "var(--blue)" && arrowX(4) > 0,
      "First click must change only color",
    );
    expect(
      document.getElementById("color-balance-error") === null,
      "Balance warning must clear when an edit restores 8 red / 8 blue",
    );
    expect(
      document.getElementById("edge-edit-error") === null &&
        document.getElementById("route-marker") === null &&
        button("#play-pause").getAttribute("aria-label") === "Start",
      "Successful edit must clear error and invalidate playback",
    );
    expect(
      document
        .querySelector('.reference-card svg g[id$="edge.ne20.4"] polyline')
        ?.getAttribute("stroke") === "var(--red)",
      "Editing active model changed a pinned snapshot",
    );
    await clickEdge(2, true);
    expect(
      line(2).getAttribute("stroke") === "var(--red)" && arrowX(2) > 0,
      "A second edge must independently start with color",
    );
    expect(
      document.getElementById("color-balance-error") !== null,
      "An edit that unbalances counts must immediately restore the validation warning",
    );
    await clickEdge(4, true);
    expect(
      line(4).getAttribute("stroke") === "var(--blue)" && arrowX(4) < 0,
      "Second click on 4 must reverse direction, not color",
    );
    expect(
      document.querySelector(".active-diagram svg")?.getAttribute("viewBox") === box,
      "Color/direction edits reset framing",
    );
    expect(
      Array.from(document.querySelectorAll(".active-diagram svg g"))
        .map((group) => group.querySelector("polyline")?.getAttribute("points"))
        .join("|") === geometry,
      "Editing rewired or moved edge geometry",
    );
    expect(localStorage.getItem(storageKey) !== null, "Successful edit was not persisted");
    return true;
  }
  if (stage === "reload") {
    expect(
      line(4).getAttribute("stroke") === "var(--blue)" &&
        arrowX(4) < 0 &&
        line(2).getAttribute("stroke") === "var(--red)" &&
        arrowX(2) > 0,
      "Colors/directions did not survive actual page reload",
    );
    await clickEdge(2);
    expect(
      line(2).getAttribute("stroke") === "var(--red)" && arrowX(2) < 0,
      `Edge 2 next-operation state did not survive reload: ${line(2).getAttribute("stroke")}, ${arrowX(2)}, ${document.getElementById("edge-edit-error")?.textContent ?? "no save error"}`,
    );
    await clickEdge(4);
    expect(
      line(4).getAttribute("stroke") === "var(--red)" && arrowX(4) < 0,
      "Edge 4 next-operation state did not survive reload",
    );
    await clickEdge(4);
    expect(
      line(4).getAttribute("stroke") === "var(--red)" && arrowX(4) > 0,
      "Four-click cycle did not restore 4",
    );
    await clickEdge(2);
    await clickEdge(2);
    expect(
      line(2).getAttribute("stroke") === "var(--blue)" && arrowX(2) > 0,
      "Four-click cycle did not restore 2",
    );
    localStorage.setItem(storageKey, "invalid saved edits");
    return true;
  }
  if (stage === "invalid") {
    expect(
      document.getElementById("edge-edit-error")?.textContent?.includes("editing is disabled") ===
        true,
      "Invalid saved edits must be reported",
    );
    await clickEdge(4);
    expect(
      line(4).getAttribute("stroke") === "var(--red)" &&
        localStorage.getItem(storageKey) === "invalid saved edits",
      "Invalid saved data was silently replaced",
    );
    const base = neon20();
    localStorage.setItem(
      storageKey,
      encodeEdgeEdits(
        SavedEdgeEditsSchema.parse({
          version: "1",
          documentId: base.id,
          revision: 4,
          edges: base.graph.edges
            .filter((edge) =>
              ["edge.ne20.13", "edge.ne20.14", "edge.ne20.16", "edge.ne20.20"].includes(edge.id),
            )
            .map((edge) => ({
              edgeId: edge.id,
              from: edge.from,
              to: edge.to,
              color: ["edge.ne20.13", "edge.ne20.14"].includes(edge.id) ? "red" : "blue",
              direction: edge.id === "edge.ne20.14" ? "to-from" : edge.direction,
              nextOperation: "color",
            })),
        }),
      ),
    );
    return true;
  }
  if (stage === "approved") {
    expect(
      line(13).getAttribute("stroke") === "var(--blue)" &&
        line(14).getAttribute("stroke") === "var(--blue)" &&
        line(16).getAttribute("stroke") === "var(--red)" &&
        line(20).getAttribute("stroke") === "var(--red)" &&
        arrowX(14) < 0,
      "Approved color swap did not migrate old saves while retaining arrows",
    );
    await clickEdge(13);
    expect(
      line(13).getAttribute("stroke") === "var(--red)",
      "Migration changed the next operation",
    );
    return true;
  }
  if (stage === "approved-reload") {
    expect(
      line(13).getAttribute("stroke") === "var(--red)" &&
        line(14).getAttribute("stroke") === "var(--blue)" &&
        line(16).getAttribute("stroke") === "var(--red)" &&
        line(20).getAttribute("stroke") === "var(--red)" &&
        arrowX(14) < 0,
      "Swap migration overwrote a later operator color edit",
    );
    localStorage.removeItem(storageKey);
    return true;
  }
  throw new Error("Unexpected edit-test stage");
}
const output = document.getElementById("browser-result");
if (!(output instanceof HTMLOutputElement)) throw new Error("Missing test result");
try {
  if (await scenario()) {
    output.dataset["status"] = "pass";
    output.textContent =
      "PASS: click cycles, persisted reload, per-edge phases, playback invalidation, pins, camera and storage failure";
  }
} catch {
  output.dataset["status"] = "fail";
  output.textContent = "FAIL: " + failure;
}
