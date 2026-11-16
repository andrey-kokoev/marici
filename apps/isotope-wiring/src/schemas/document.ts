import { z } from "zod";
import { DiagramGraphSchema } from "./graph.js";
import { DiagramLayoutSchema } from "./layout.js";
import { DocumentIdSchema, NonEmptyTextSchema, RevisionSchema } from "./primitives.js";
import { TraversalPolicySchema } from "./traversal.js";
import { IsotopeRecordSchema } from "./inventory.js";

export const DiagramDocumentSchema = z
  .strictObject({
    schemaVersion: z.literal(1),
    id: DocumentIdSchema,
    revision: RevisionSchema,
    title: NonEmptyTextSchema,
    isotope: IsotopeRecordSchema.nullable(),
    graph: DiagramGraphSchema,
    layout: DiagramLayoutSchema,
    policy: TraversalPolicySchema,
  })
  .superRefine((document, ctx) => {
    if (
      document.policy.status === "alternating" &&
      document.graph.edges.some((edge) => edge.direction === "unresolved")
    )
      ctx.addIssue({
        code: "custom",
        message: "Alternating traversal requires resolved edge directions",
        path: ["policy"],
      });
    const vertexIds = new Set(document.graph.vertices.map((vertex) => vertex.id));
    const edgeIds = new Set(document.graph.edges.map((edge) => edge.id));
    const placedVertices = new Set<string>();
    const styledEdges = new Set<string>();
    const aliasedEdges = new Set<string>();
    const aliasNumbers = new Set<number>();
    for (const placement of document.layout.vertices) {
      if (!vertexIds.has(placement.vertexId) || placedVertices.has(placement.vertexId))
        ctx.addIssue({
          code: "custom",
          message: "Missing or duplicate layout vertex reference",
          path: ["layout", "vertices"],
        });
      placedVertices.add(placement.vertexId);
    }
    for (const vertexId of vertexIds) {
      if (!placedVertices.has(vertexId))
        ctx.addIssue({
          code: "custom",
          message: "Vertex has no authored placement",
          path: ["layout", "vertices"],
        });
    }
    for (const presentation of document.layout.edges) {
      if (!edgeIds.has(presentation.edgeId) || styledEdges.has(presentation.edgeId))
        ctx.addIssue({
          code: "custom",
          message: "Missing or duplicate edge presentation reference",
          path: ["layout", "edges"],
        });
      styledEdges.add(presentation.edgeId);
    }
    for (const edgeId of edgeIds) {
      if (!styledEdges.has(edgeId))
        ctx.addIssue({
          code: "custom",
          message: "Edge has no presentation",
          path: ["layout", "edges"],
        });
    }
    for (const alias of document.layout.aliases) {
      if (
        !edgeIds.has(alias.edgeId) ||
        aliasedEdges.has(alias.edgeId) ||
        aliasNumbers.has(alias.number)
      )
        ctx.addIssue({
          code: "custom",
          message: "Invalid or ambiguous edge alias",
          path: ["layout", "aliases"],
        });
      aliasedEdges.add(alias.edgeId);
      aliasNumbers.add(alias.number);
    }
  });

export type DiagramDocument = z.infer<typeof DiagramDocumentSchema>;
export type DiagramDocumentInput = z.input<typeof DiagramDocumentSchema>;
