import { computed, readonly, shallowRef } from "vue";
import { defineStore } from "pinia";
import {
  InspectionStateSchema,
  PlaybackSchema,
  SelectionSchema,
  type Selection,
} from "../../schemas/inspection.js";
import { syntheticExample } from "../../examples/synthetic.js";
import { createDiagram } from "../../examples/diagrams.js";
import { traceRoute } from "../../domain/route.js";
import { inspectColorBalance } from "../../domain/color-balance.js";
import { type Turn } from "../../schemas/traversal.js";
import { SavedEdgeEditsSchema, type SavedEdgeEdits } from "../../schemas/edge-edits.js";
import { type NamedVersion } from "../../schemas/named-versions.js";
import {
  captureNamedVersion,
  restoreNamedVersion,
  namedVersionContent,
} from "../../domain/named-versions.js";
import { emptyEdgeEdits, applyEdgeEdits, cycleEdgeEdit } from "../../domain/edge-edits.js";
import { readEdgeEdits, saveEdgeEdits } from "../../edge-edit-storage.js";

export const ROUTE_EDGE_MS = 800;

export const useInspection = defineStore("inspection", () => {
  const current = shallowRef(
    InspectionStateSchema.parse({
      document: null,
      selection: { kind: "none" },
      showEdgeLabels: true,
      route: null,
      playback: { elapsedMs: 0, playing: false },
    }),
  );
  const activeDocument = computed(() => current.value.document);
  const activeSelection = computed(() => current.value.selection);
  const edgeEdits = shallowRef<SavedEdgeEdits | null>(null);
  const editError = shallowRef("");
  let editsBlocked = false;
  function loadExample(): void {
    edgeEdits.value = null;
    editError.value = "";
    editsBlocked = false;
    current.value = InspectionStateSchema.parse({
      ...current.value,
      document: syntheticExample(),
      route: null,
      playback: { elapsedMs: 0, playing: false },
      selection: { kind: "none" },
    });
  }
  function showNeon(): void {
    loadDiagram("Neon-20");
  }
  function loadDiagram(name: string): void {
    const choice = createDiagram(name);
    if (choice === null) {
      unload();
      return;
    }
    let document = choice.document;
    editError.value = "";
    editsBlocked = false;
    edgeEdits.value = emptyEdgeEdits(document);
    if (typeof window !== "undefined") {
      try {
        const saved = readEdgeEdits(window.localStorage, document);
        if (
          saved.startEdge !== undefined &&
          saved.startEdge !== null &&
          !document.graph.edges.some((edge) => edge.id === saved.startEdge)
        )
          throw new Error("Saved start edge is missing");
        document = applyEdgeEdits(document, saved);
        edgeEdits.value = saved;
      } catch {
        editsBlocked = true;
        editError.value =
          "Saved edge edits could not be loaded or no longer match this diagram. Showing the base diagram; editing is disabled and saved data has not been overwritten.";
      }
    }
    current.value = InspectionStateSchema.parse({
      ...current.value,
      document,
      selection:
        edgeEdits.value?.startEdge === null
          ? { kind: "none" }
          : {
              kind: "edge",
              edgeId: edgeEdits.value?.startEdge ?? choice.initialEdgeId,
              document: { documentId: document.id, revision: document.revision },
            },
      route: null,
      playback: { elapsedMs: 0, playing: false },
    });
  }
  function unload(): void {
    edgeEdits.value = null;
    editError.value = "";
    editsBlocked = false;
    current.value = InspectionStateSchema.parse({
      ...current.value,
      document: null,
      selection: { kind: "none" },
      route: null,
      playback: { elapsedMs: 0, playing: false },
    });
  }
  function run(initialTurn: Turn = "left"): void {
    const document = current.value.document,
      selection = current.value.selection;
    if (document === null || selection.kind !== "edge") return;
    const route = traceRoute(document, selection.edgeId, initialTurn);
    current.value = {
      ...current.value,
      route,
      playback: { elapsedMs: 0, playing: route.steps.length > 0 },
    };
  }
  function clearRoute(): void {
    current.value = {
      ...current.value,
      route: null,
      playback: { elapsedMs: 0, playing: false },
    };
  }
  const routeFinished = computed(
    () =>
      current.value.route !== null &&
      current.value.playback.elapsedMs >= current.value.route.steps.length * ROUTE_EDGE_MS,
  );
  function advancePlayback(deltaMs: number): void {
    if (
      !current.value.playback.playing ||
      current.value.route === null ||
      !Number.isFinite(deltaMs) ||
      deltaMs <= 0
    )
      return;
    const duration = current.value.route.steps.length * ROUTE_EDGE_MS;
    const elapsedMs = Math.min(duration, current.value.playback.elapsedMs + deltaMs);
    current.value = {
      ...current.value,
      playback: PlaybackSchema.parse({ elapsedMs, playing: elapsedMs < duration }),
    };
  }
  function stepBack(): void {
    if (current.value.route === null) return;
    current.value = {
      ...current.value,
      playback: PlaybackSchema.parse({
        elapsedMs: Math.max(
          0,
          (Math.ceil(current.value.playback.elapsedMs / ROUTE_EDGE_MS) - 1) * ROUTE_EDGE_MS,
        ),
        playing: false,
      }),
    };
  }
  function stepForward(initialTurn: Turn = "left"): void {
    if (current.value.route === null) run(initialTurn);
    if (current.value.route === null) return;
    current.value = {
      ...current.value,
      playback: PlaybackSchema.parse({
        elapsedMs: Math.min(
          current.value.route.steps.length * ROUTE_EDGE_MS,
          (Math.floor(current.value.playback.elapsedMs / ROUTE_EDGE_MS) + 1) * ROUTE_EDGE_MS,
        ),
        playing: false,
      }),
    };
  }
  function pause(): void {
    current.value = { ...current.value, playback: { ...current.value.playback, playing: false } };
  }
  function resume(): void {
    if (current.value.route === null || routeFinished.value) return;
    current.value = { ...current.value, playback: { ...current.value.playback, playing: true } };
  }
  function persistControls(startEdge: SavedEdgeEdits["startEdge"], initialTurn?: Turn): boolean {
    const previous = edgeEdits.value;
    if (previous === null || editsBlocked) return true;
    const next = SavedEdgeEditsSchema.parse({
      ...previous,
      startEdge,
      ...(initialTurn === undefined ? {} : { initialTurn }),
    });
    if (next.startEdge === previous.startEdge && next.initialTurn === previous.initialTurn)
      return true;
    try {
      if (typeof window !== "undefined") saveEdgeEdits(window.localStorage, previous, next);
      edgeEdits.value = next;
      editError.value = "";
      return true;
    } catch {
      editError.value =
        "Could not save start/turn settings; no change was applied. Check browser storage or reload if another tab changed this diagram.";
      return false;
    }
  }
  function setInitialTurn(turn: Turn): boolean {
    return persistControls(
      current.value.selection.kind === "edge" ? current.value.selection.edgeId : null,
      turn,
    );
  }
  function select(selection: Selection): void {
    const checked = SelectionSchema.safeParse(selection);
    if (!checked.success) return;
    const value = checked.data;
    const document = activeDocument.value;
    if (value.kind !== "none") {
      if (
        document === null ||
        value.document.documentId !== document.id ||
        value.document.revision !== document.revision
      )
        return;
      if (value.kind === "edge" && !document.graph.edges.some((edge) => edge.id === value.edgeId))
        return;
      if (
        value.kind === "vertex" &&
        !document.graph.vertices.some((vertex) => vertex.id === value.vertexId)
      )
        return;
    }
    if (!persistControls(value.kind === "edge" ? value.edgeId : null)) return;
    current.value = { ...current.value, selection: value };
  }
  function matchesVersion(snapshot: NamedVersion, initialTurn: Turn): boolean {
    const document = activeDocument.value,
      previous = edgeEdits.value;
    if (document === null || previous === null) return false;
    try {
      return (
        namedVersionContent(
          captureNamedVersion(
            snapshot.name,
            document,
            previous,
            activeSelection.value,
            initialTurn,
          ),
        ) === namedVersionContent(snapshot)
      );
    } catch {
      return false;
    }
  }
  function captureVersion(name: string, initialTurn: Turn): NamedVersion | null {
    const document = current.value.document,
      previous = edgeEdits.value;
    if (document === null || previous === null || editsBlocked) return null;
    try {
      return captureNamedVersion(name, document, previous, current.value.selection, initialTurn);
    } catch {
      editError.value =
        "Could not capture this version. Check its name and resolved edge directions.";
      return null;
    }
  }
  function restoreVersion(snapshot: NamedVersion): boolean {
    const document = current.value.document,
      previous = edgeEdits.value;
    if (document === null || previous === null || editsBlocked) return false;
    let failure =
      "This saved version is incompatible with the current diagram geometry or edge identities. No changes were made; the saved version was retained.";
    try {
      const result = restoreNamedVersion(document, previous, snapshot);
      const nextState = InspectionStateSchema.parse({
        ...current.value,
        document: result.document,
        selection:
          snapshot.startEdge === null
            ? { kind: "none" }
            : {
                kind: "edge",
                edgeId: snapshot.startEdge,
                document: { documentId: result.document.id, revision: result.document.revision },
              },
        route: null,
        playback: { elapsedMs: 0, playing: false },
      });
      failure =
        "Could not persist the loaded version. Check browser storage or reload if another tab changed this diagram. No changes were made.";
      if (typeof window === "undefined") throw new Error("Browser storage unavailable");
      saveEdgeEdits(window.localStorage, previous, result.edits);
      edgeEdits.value = result.edits;
      current.value = nextState;
      editError.value = "";
      return true;
    } catch {
      editError.value = failure;
      return false;
    }
  }
  function cycleEdge(edgeId: string): void {
    const document = current.value.document,
      previous = edgeEdits.value;
    if (document === null || previous === null || editsBlocked) return;
    try {
      const result = cycleEdgeEdit(document, previous, edgeId);
      if (result === null) return;
      if (typeof window === "undefined") throw new Error("Browser storage unavailable");
      const nextState = InspectionStateSchema.parse({
        ...current.value,
        document: result.document,
        selection:
          current.value.selection.kind === "none"
            ? current.value.selection
            : {
                ...current.value.selection,
                document: { documentId: result.document.id, revision: result.document.revision },
              },
        route: null,
        playback: { elapsedMs: 0, playing: false },
      });
      saveEdgeEdits(window.localStorage, previous, result.edits);
      edgeEdits.value = result.edits;
      current.value = nextState;
      editError.value = "";
    } catch {
      editError.value =
        "Could not save the edge edit; no change was applied. Check browser storage, or reload if another tab changed this diagram.";
    }
  }
  function edgeEditHint(edgeId: string): string {
    const edge = current.value.document?.graph.edges.find((value) => value.id === edgeId);
    const style = current.value.document?.layout.edges.find((value) => value.edgeId === edgeId);
    if (
      style?.color === "green" ||
      edge === undefined ||
      (edge.direction !== "from-to" && edge.direction !== "to-from")
    )
      return "Select edge; connector or unresolved direction is not edited";
    if (editsBlocked) return "Editing disabled: saved edits could not be loaded";
    return edgeEdits.value?.edges.find((value) => value.edgeId === edgeId)?.nextOperation ===
      "direction"
      ? "Click to reverse direction (saved in this browser)"
      : "Click to change color (saved in this browser)";
  }
  function toggleLabels(): void {
    current.value = {
      ...current.value,
      showEdgeLabels: !current.value.showEdgeLabels,
    };
  }
  showNeon();
  return {
    state: readonly(current),
    activeDocument: computed(() =>
      activeDocument.value === null ? null : readonly(activeDocument.value),
    ),
    loadExample,
    showNeon,
    loadDiagram,
    unload,
    run,
    clearRoute,
    routeFinished,
    advancePlayback,
    pause,
    resume,
    stepBack,
    stepForward,
    select,
    toggleLabels,
    cycleEdge,
    captureVersion,
    restoreVersion,
    matchesVersion,
    setInitialTurn,
    savedInitialTurn: computed(() => edgeEdits.value?.initialTurn),
    edgeEditHint,
    editError: readonly(editError),
    colorBalance: computed(() =>
      activeDocument.value === null ? null : inspectColorBalance(activeDocument.value),
    ),
  };
});
