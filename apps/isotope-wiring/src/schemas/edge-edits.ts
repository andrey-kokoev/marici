import { z } from "zod";
import { CountSchema, DocumentIdSchema, EdgeIdSchema, VertexIdSchema } from "./primitives.js";
import { DiagramDocumentSchema } from "./document.js";
import { TurnSchema } from "./traversal.js";

export const EdgeEditSchema = z.strictObject({
  edgeId: EdgeIdSchema,
  from: VertexIdSchema,
  to: VertexIdSchema,
  color: z.enum(["red", "blue"]),
  direction: z.enum(["from-to", "to-from"]),
  nextOperation: z.enum(["color", "direction"]),
});
export const SavedEdgeEditsSchema = z
  .strictObject({
    version: z.enum(["1", "2", "3"]),
    documentId: DocumentIdSchema,
    revision: CountSchema,
    startEdge: EdgeIdSchema.nullable().optional(),
    initialTurn: TurnSchema.optional(),
    edges: z.array(EdgeEditSchema),
  })
  .superRefine((value, ctx) => {
    if (new Set(value.edges.map((edge) => edge.edgeId)).size !== value.edges.length)
      ctx.addIssue({ code: "custom", message: "Duplicate edge edits" });
    if (value.revision < value.edges.length)
      ctx.addIssue({ code: "custom", message: "Invalid edit revision" });
  });
export const EdgeEditResultSchema = z.strictObject({
  document: DiagramDocumentSchema,
  edits: SavedEdgeEditsSchema,
});
export type SavedEdgeEdits = z.infer<typeof SavedEdgeEditsSchema>;
export type EdgeEditResult = z.infer<typeof EdgeEditResultSchema>;
