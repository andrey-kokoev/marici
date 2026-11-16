import {
  VERSION_LIBRARY_PREFIX,
  decodeVersionLibrary,
  encodeVersionLibrary,
} from "../src/named-version-storage.js";
import { VersionLibrarySchema } from "../src/schemas/named-versions.js";
import { useInspection } from "../src/vue/stores/inspection.js";
import { useVersions } from "../src/vue/stores/versions.js";
const pause = () => new Promise<void>((resolve) => setTimeout(resolve, 50));
let failure = "Named-version scenario did not finish";
function expect(value: boolean, message: string): void {
  if (!value) {
    failure = message;
    throw new Error(message);
  }
}
function button(id: string): HTMLButtonElement {
  const node = document.getElementById(id);
  if (!(node instanceof HTMLButtonElement)) throw new Error("Missing " + id);
  return node;
}
function select(id: string): HTMLSelectElement {
  const node = document.getElementById(id);
  if (!(node instanceof HTMLSelectElement)) throw new Error("Missing " + id);
  return node;
}
async function openPanel(): Promise<void> {
  const panel = document.getElementById("named-versions");
  if (!(panel instanceof HTMLDialogElement)) throw new Error("Missing versions dialog");
  if (!panel.open) button("versions-toggle").click();
  await pause();
}
async function choose(id: string, value: string): Promise<void> {
  if (id === "saved-version") await openPanel();
  const node = select(id);
  node.value = value;
  node.dispatchEvent(new Event("change", { bubbles: true }));
  await pause();
}
async function save(name: string): Promise<void> {
  await openPanel();
  const node = document.getElementById("version-name");
  if (!(node instanceof HTMLInputElement)) throw new Error("Missing name");
  node.value = name;
  node.dispatchEvent(new Event("input", { bubbles: true }));
  await pause();
  button("save-version").click();
  await pause();
}
function color4(): string | null {
  return (
    document
      .getElementById("inspection-edge.ne20.4")
      ?.querySelector("polyline")
      ?.getAttribute("stroke") ?? null
  );
}
function arrow4(): number {
  const node = document.getElementById("inspection-edge.ne20.4")?.querySelector(".direction-arrow");
  if (!(node instanceof SVGPathElement)) throw new Error("Missing arrow");
  return node.transform.baseVal.consolidate()?.matrix.a ?? 0;
}
async function edit4(): Promise<void> {
  const panel = document.getElementById("named-versions");
  if (panel instanceof HTMLDialogElement) panel.close();
  await pause();
  document
    .getElementById("inspection-label-edge.ne20.4")
    ?.dispatchEvent(new MouseEvent("click", { bubbles: true }));
  await pause();
}
function names(): string[] {
  if (document.getElementById("saved-version") === null) return [];
  return Array.from(select("saved-version").options)
    .map((option) => option.value)
    .filter(Boolean);
}
async function scenario(): Promise<void> {
  for (let i = 0; i < 100 && !document.getElementById("named-versions"); i++) await pause();
  await pause();
  const panel = document.getElementById("named-versions");
  if (!(panel instanceof HTMLDialogElement)) throw new Error("Missing versions");
  await openPanel();
  const status = document.getElementById("version-working-state");
  expect(status === null || panel.contains(status), "Version status must stay inside the dialog");
  const bounds = panel.getBoundingClientRect();
  expect(
    bounds.left >= 0 &&
      bounds.right <= innerWidth &&
      bounds.top >= 0 &&
      bounds.bottom <= innerHeight,
    "Version controls are outside the viewport",
  );
  const key = VERSION_LIBRARY_PREFIX + "diagram.ne20";
  const stage = new URL(location.href).searchParams.get("stage");
  if (stage === "save") {
    expect(localStorage.getItem(key) === null, "Version test profile not isolated");
    expect(
      ["saved-version", "load-version", "delete-version"].every(
        (id) => document.getElementById(id) === null,
      ) && document.getElementById("versions-empty") !== null,
      "Empty library must not offer saved-version controls",
    );
    await choose("start-edge", "edge.ne20.3");
    await choose("first-turn", "right");
    await save("Baseline");
    expect(names().join(",") === "Baseline", "Save did not create a named version");
    expect(document.activeElement?.id === "version-name", "Save stranded keyboard focus");
    expect(
      document
        .getElementById("version-working-state")
        ?.textContent?.includes("Matches saved version") === true,
      "Save status missing",
    );
    await edit4();
    expect(color4() === "var(--blue)" && arrow4() > 0, "Edit fixture failed");
    expect(
      document
        .getElementById("version-working-state")
        ?.textContent?.includes("Differs from saved versions") === true,
      "Edits not marked modified",
    );
    await choose("start-edge", "edge.ne20.8");
    await choose("first-turn", "left");
    await save("Trial");
    expect(names().join(",") === "Baseline,Trial", "Second version missing");
    await save("baseline");
    expect(
      document.getElementById("version-error")?.textContent?.includes("already exists") === true &&
        names().length === 2,
      "Duplicate name overwritten",
    );
    const descriptor = Object.getOwnPropertyDescriptor(Storage.prototype, "setItem");
    if (descriptor === undefined) throw new Error("Missing storage descriptor");
    const before = localStorage.getItem(key);
    try {
      Storage.prototype.setItem = () => {
        throw new DOMException("Denied", "QuotaExceededError");
      };
      await save("Denied");
    } finally {
      Object.defineProperty(Storage.prototype, "setItem", descriptor);
    }
    expect(
      document.getElementById("version-error") !== null && localStorage.getItem(key) === before,
      "Failed save changed the library or hid the error",
    );
    return;
  }
  if (stage === "reload") {
    expect(names().join(",") === "Baseline,Trial", "Names did not survive browser restart");
    window.confirm = () => true;
    await choose("saved-version", "Trial");
    button("load-version").click();
    await pause();
    expect(color4() === "var(--blue)" && arrow4() > 0, "Snapshot color/direction not restored");
    expect(
      !panel.open && document.activeElement instanceof SVGSVGElement,
      "Load must dismiss and focus the graph",
    );
    await edit4();
    expect(color4() === "var(--blue)" && arrow4() < 0, "Snapshot click phase not restored");
    const zoom = document.querySelector('[aria-label="Zoom in"]');
    if (!(zoom instanceof HTMLButtonElement)) throw new Error("Missing zoom");
    zoom.click();
    await pause();
    const box = document.querySelector(".active-diagram svg")?.getAttribute("viewBox");
    button("play-pause").click();
    await pause();
    await choose("saved-version", "Baseline");
    window.confirm = () => false;
    button("load-version").click();
    await pause();
    expect(color4() === "var(--blue)" && arrow4() < 0, "Cancel load changed active edits");
    window.confirm = () => true;
    const descriptor = Object.getOwnPropertyDescriptor(Storage.prototype, "setItem");
    if (descriptor === undefined) throw new Error("Missing storage descriptor");
    try {
      Storage.prototype.setItem = () => {
        throw new DOMException("Denied", "QuotaExceededError");
      };
      button("load-version").click();
      await pause();
    } finally {
      Object.defineProperty(Storage.prototype, "setItem", descriptor);
    }
    expect(
      color4() === "var(--blue)" &&
        arrow4() < 0 &&
        document.getElementById("edge-edit-error") !== null,
      "Failed load must preserve model and report save failure",
    );
    button("load-version").click();
    await pause();
    expect(
      color4() === "var(--red)" &&
        arrow4() > 0 &&
        select("start-edge").value === "edge.ne20.3" &&
        select("first-turn").value === "right",
      "Load did not restore colors, arrows and start/turn controls",
    );
    expect(
      document.getElementById("route-marker") === null &&
        button("play-pause").getAttribute("aria-label") === "Start",
      "Load retained stale playback",
    );
    expect(
      document.querySelector(".active-diagram svg")?.getAttribute("viewBox") === box,
      "Loading version reset the camera",
    );
    await choose("saved-version", "Trial");
    button("load-version").click();
    await pause();
    expect(
      color4() === "var(--blue)" && arrow4() > 0,
      "Editing a loaded version mutated its saved snapshot",
    );
    await openPanel();
    window.confirm = () => false;
    button("delete-version").click();
    await pause();
    expect(names().length === 2, "Cancel delete removed a version");
    window.confirm = () => true;
    button("delete-version").click();
    await pause();
    expect(
      names().join(",") === "Baseline" && color4() === "var(--blue)",
      "Delete must remove only the saved version, not active edits",
    );
    return;
  }
  if (stage === "delete-reload") {
    expect(names().join(",") === "Baseline", "Deleted version returned after restart");
    window.confirm = () => true;
    await choose("saved-version", "Baseline");
    button("load-version").click();
    await pause();
    expect(
      color4() === "var(--red)" &&
        select("start-edge").value === "edge.ne20.3" &&
        select("first-turn").value === "right",
      "Remaining snapshot was damaged",
    );
    return;
  }
  if (stage === "active-reload") {
    // Do not click Load here: the previous loaded working state must itself persist.
    expect(
      color4() === "var(--red)" &&
        arrow4() > 0 &&
        select("start-edge").value === "edge.ne20.3" &&
        select("first-turn").value === "right",
      "Reload lost the active version start edge or turn setting",
    );
    localStorage.setItem(key, "broken library");
    button("refresh-versions").click();
    await pause();
    await save("Must not overwrite");
    expect(
      localStorage.getItem(key) === "broken library" &&
        document.getElementById("version-library-error") !== null &&
        button("save-version").disabled,
      "Corrupt library was silently overwritten or Save remained enabled",
    );
    localStorage.removeItem(key);
    return;
  }
  if (stage === "ux") {
    const model = useInspection().activeDocument;
    if (model === null) throw new Error("Missing model");
    await save("Fixture");
    const library = decodeVersionLibrary(localStorage.getItem(key), model.id);
    const snapshot = library.entries[0];
    if (snapshot === undefined) throw new Error("Missing fixture snapshot");
    const full = VersionLibrarySchema.parse({
      ...library,
      entries: Array.from("x".repeat(100), (_, i) => ({ ...snapshot, name: `Version ${i + 1}` })),
    });
    const peer = document.createElement("iframe");
    peer.hidden = true;
    document.body.append(peer);
    const other = peer.contentWindow;
    if (other === null) throw new Error("Missing peer browsing context");
    try {
      // A real storage event from a second same-origin browsing context.
      other.localStorage.setItem(key, encodeVersionLibrary(full));
      await pause();
      expect(
        names().length === 100 &&
          button("save-version").disabled &&
          document.getElementById("version-save-blocked")?.textContent?.includes("100") === true,
        "External library/capacity change not reflected",
      );
      const before = localStorage.getItem(key);
      expect(
        !useVersions().save("Overflow") && localStorage.getItem(key) === before,
        "Capacity guard changed the library",
      );
      expect(useVersions().remove("Version 100"), "Could not free capacity");
      await pause();
      expect(
        document.getElementById("version-save-blocked") === null,
        "Save did not recover after freeing capacity",
      );
      await save("Recovered");
      expect(names().length === 100, "Save after freeing capacity failed");
      other.localStorage.setItem(key, "broken library");
      await pause();
      expect(
        document.getElementById("version-library-error") !== null &&
          document.getElementById("versions-empty") === null &&
          button("save-version").disabled,
        "Unreadable library confused with empty library",
      );
      expect(
        document.activeElement?.id === "refresh-versions",
        "Unreadable library must focus Retry",
      );
      other.localStorage.setItem(
        key,
        encodeVersionLibrary(VersionLibrarySchema.parse({ ...library, entries: [] })),
      );
      await pause();
      expect(
        document.getElementById("version-library-error") === null &&
          document.getElementById("versions-empty") !== null,
        "Library recovery failed",
      );
      await save("Remote removal");
      button("delete-version").focus();
      other.localStorage.setItem(
        key,
        encodeVersionLibrary(VersionLibrarySchema.parse({ ...library, entries: [] })),
      );
      await pause();
      expect(
        document.activeElement?.id === "version-name" &&
          document.getElementById("delete-version") === null,
        "External deletion stranded focus",
      );
    } finally {
      peer.remove();
    }
    await save("Reopen");
    panel.close();
    await pause();
    localStorage.setItem(
      key,
      encodeVersionLibrary(
        VersionLibrarySchema.parse({ ...library, entries: [{ ...snapshot, name: "External" }] }),
      ),
    );
    await openPanel();
    expect(
      names().join(",") === "External" && document.getElementById("version-notice") === null,
      "Opening retained stale list or feedback",
    );
    expect(
      document
        .getElementById("versions-title")
        ?.textContent?.includes(model.isotope?.name ?? model.title) === true,
      "Dialog lacks diagram context",
    );
    expect(
      select("saved-version").options[0]?.textContent === "Select a saved version",
      "Chooser implies only Load",
    );
    await save("External");
    expect(document.getElementById("version-error") !== null, "Duplicate fixture failed");
    const input = document.getElementById("version-name");
    if (!(input instanceof HTMLInputElement)) throw new Error("Missing name input");
    input.value = "Different";
    input.dispatchEvent(new Event("input", { bubbles: true }));
    await pause();
    expect(
      document.getElementById("version-error") === null,
      "Editing name retained obsolete error",
    );
    await edit4();
    await openPanel();
    expect(
      document
        .getElementById("version-working-state")
        ?.textContent?.includes("Differs from saved versions") === true &&
        document.getElementById("version-notice") === null,
      "Modified wiring status/feedback inconsistent",
    );
    return;
  }
  if (stage === "ux-reload") {
    expect(
      document
        .getElementById("version-working-state")
        ?.textContent?.includes("Differs from saved versions") === true,
      "Reload changed the meaning of modified status",
    );
    return;
  }
  throw new Error("Unexpected named-version stage");
}
const output = document.getElementById("browser-result");
if (!(output instanceof HTMLOutputElement)) throw new Error("Missing output");
try {
  await scenario();
  output.dataset["status"] = "pass";
  output.textContent =
    "PASS: named-version save/load/delete, browser persistence, controls, click phases, cancellation and storage failures";
} catch {
  output.dataset["status"] = "fail";
  output.textContent = "FAIL: " + failure;
}
