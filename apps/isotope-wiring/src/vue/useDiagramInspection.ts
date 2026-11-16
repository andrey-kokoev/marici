import { computed } from "vue";
import { ROUTE_EDGE_MS, useInspection } from "./stores/inspection.js";
import { DiagramDocumentSchema } from "../schemas/document.js";
import { SelectionSchema } from "../schemas/inspection.js";
import { pointAtFraction, projectDiagram } from "../presentation/diagram.js";

/** Derived presentation and identity-based selection; owns no document copy or listeners. */
export function useDiagramInspection() {
  const store = useInspection();
  const projection = computed(() =>
    store.activeDocument === null
      ? null
      : projectDiagram(DiagramDocumentSchema.parse(store.activeDocument)),
  );
  function selectEdge(edgeId: string): void {
    const document = store.activeDocument;
    if (document !== null)
      store.select(
        SelectionSchema.parse({
          kind: "edge",
          edgeId,
          document: { documentId: document.id, revision: document.revision },
        }),
      );
  }
  function selectVertex(vertexId: string): void {
    const document = store.activeDocument;
    if (document !== null)
      store.select(
        SelectionSchema.parse({
          kind: "vertex",
          vertexId,
          document: { documentId: document.id, revision: document.revision },
        }),
      );
  }
  const routeIndex = computed(() =>
    Math.min(
      Math.floor(store.state.playback.elapsedMs / ROUTE_EDGE_MS),
      (store.state.route?.steps.length ?? 0) - 1,
    ),
  );
  const visitedSteps = computed(
    () => store.state.route?.steps.slice(0, routeIndex.value + 1) ?? [],
  );
  const marker = computed(() => {
    const step = store.state.route?.steps[routeIndex.value];
    if (step === undefined) return null;
    const rendered = projection.value?.edges.find((edge) => edge.id === step.edgeId);
    const source = store.activeDocument?.graph.edges.find((edge) => edge.id === step.edgeId);
    if (rendered === undefined || source === undefined) return null;
    const points = step.from === source.from ? rendered.polyline : [...rendered.polyline].reverse();
    return pointAtFraction(
      points,
      Math.min(1, store.state.playback.elapsedMs / ROUTE_EDGE_MS - routeIndex.value),
    );
  });
  const routeLabels = computed(
    () =>
      visitedSteps.value
        .map(
          (step) =>
            store.activeDocument?.layout.aliases.find((alias) => alias.edgeId === step.edgeId)
              ?.number ?? step.edgeId,
        )
        .join(" → ") || "—",
  );
  return { store, projection, selectEdge, selectVertex, routeLabels, marker, visitedSteps };
}
