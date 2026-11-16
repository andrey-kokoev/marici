import { z } from "zod";
import { DiagramDocumentSchema } from "./document.js";
import { DocumentReferenceSchema, EdgeIdSchema, VertexIdSchema } from "./primitives.js";
import { EdgeDirectionSchema } from "./graph.js";
import { EdgeColorSchema } from "./layout.js";
import { RouteResultSchema } from "./traversal.js";
export const SelectionSchema = z.discriminatedUnion("kind", [
  z.strictObject({ kind: z.literal("none") }),
  z.strictObject({
    kind: z.literal("edge"),
    document: DocumentReferenceSchema,
    edgeId: EdgeIdSchema,
  }),
  z.strictObject({
    kind: z.literal("vertex"),
    document: DocumentReferenceSchema,
    vertexId: VertexIdSchema,
  }),
]);
export type Selection = z.infer<typeof SelectionSchema>;

export const PlaybackSchema = z.strictObject({
  elapsedMs: z.number().finite().nonnegative(),
  playing: z.boolean(),
});

export const InspectionStateSchema = z
  .strictObject({
    document: DiagramDocumentSchema.nullable(),
    selection: SelectionSchema,
    showEdgeLabels: z.boolean(),
    route: RouteResultSchema.nullable(),
    playback: PlaybackSchema,
  })
  .superRefine((state, ctx) => {
    const document = state.document;
    if (
      state.route !== null &&
      (document === null ||
        state.route.document.documentId !== document.id ||
        state.route.document.revision !== document.revision)
    )
      ctx.addIssue({ code: "custom", message: "Route belongs to a different document snapshot" });
    const selection = state.selection;
    if (selection.kind === "none") return;
    if (
      document === null ||
      selection.document.documentId !== document.id ||
      selection.document.revision !== document.revision
    ) {
      ctx.addIssue({ code: "custom", message: "Selection is not bound to the active snapshot" });
      return;
    }
    if (
      selection.kind === "edge" &&
      !document.graph.edges.some((value) => value.id === selection.edgeId)
    )
      ctx.addIssue({ code: "custom", message: "Selected edge does not exist" });
    if (
      selection.kind === "vertex" &&
      !document.graph.vertices.some((value) => value.id === selection.vertexId)
    )
      ctx.addIssue({ code: "custom", message: "Selected vertex does not exist" });
  });
export const ScreenPointSchema = z.strictObject({ x: z.number().finite(), y: z.number().finite() });
export const RenderEdgeSchema = z.strictObject({
  id: EdgeIdSchema,
  direction: EdgeDirectionSchema,
  color: EdgeColorSchema,
  points: z.string(),
  polyline: z.array(ScreenPointSchema).min(2),
  midpoint: ScreenPointSchema,
  arrowAngle: z.number().finite().nullable(),
  labelPoint: ScreenPointSchema,
  label: z.string(),
});
export const RenderVertexSchema = z.strictObject({ id: VertexIdSchema, point: ScreenPointSchema });
export const DiagramProjectionSchema = z.strictObject({
  viewBox: z.string(),
  edges: z.array(RenderEdgeSchema),
  vertices: z.array(RenderVertexSchema),
});
export type ScreenPoint = z.infer<typeof ScreenPointSchema>;
export type DiagramProjection = z.infer<typeof DiagramProjectionSchema>;
