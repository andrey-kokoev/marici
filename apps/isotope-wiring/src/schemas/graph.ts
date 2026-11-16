import { z } from "zod";
import {
  EdgeIdSchema,
  NonEmptyTextSchema,
  ReviewSchema,
  RoleIdSchema,
  VertexIdSchema,
} from "./primitives.js";

export const EdgeDirectionSchema = z.enum([
  "from-to",
  "to-from",
  "both",
  "undirected",
  "unresolved",
]);
export const EdgeEndSchema = z.enum(["from", "to"]);
export const EdgeEndReferenceSchema = z.strictObject({ edgeId: EdgeIdSchema, end: EdgeEndSchema });
export const VertexSchema = z.strictObject({
  id: VertexIdSchema,
  label: NonEmptyTextSchema.optional(),
});
export const EdgeRoleSchema = z.strictObject({
  id: RoleIdSchema,
  description: NonEmptyTextSchema,
  review: ReviewSchema,
});
export const EdgeSchema = z.strictObject({
  id: EdgeIdSchema,
  from: VertexIdSchema,
  to: VertexIdSchema,
  direction: EdgeDirectionSchema,
  roleId: RoleIdSchema.optional(),
});
// An authored rotation system, not one recovered from a drawing.
export const JunctionOrderSchema = z.discriminatedUnion("status", [
  z.strictObject({
    vertexId: VertexIdSchema,
    status: z.literal("unresolved"),
    question: NonEmptyTextSchema,
  }),
  z.strictObject({
    vertexId: VertexIdSchema,
    status: z.literal("specified"),
    orientation: z.enum(["clockwise", "counterclockwise"]),
    ends: z.array(EdgeEndReferenceSchema).min(1),
    review: ReviewSchema,
  }),
]);
export const DiagramGraphSchema = z
  .strictObject({
    vertices: z.array(VertexSchema).min(1),
    edges: z.array(EdgeSchema),
    roles: z.array(EdgeRoleSchema),
    junctionOrders: z.array(JunctionOrderSchema),
    review: ReviewSchema,
  })
  .superRefine((graph, ctx) => {
    const vertices = new Set<string>();
    const edges = new Map<string, z.infer<typeof EdgeSchema>>();
    const roles = new Set<string>();
    for (const vertex of graph.vertices) {
      if (vertices.has(vertex.id))
        ctx.addIssue({ code: "custom", message: "Duplicate vertex ID", path: ["vertices"] });
      vertices.add(vertex.id);
    }
    for (const role of graph.roles) {
      if (roles.has(role.id))
        ctx.addIssue({ code: "custom", message: "Duplicate role ID", path: ["roles"] });
      roles.add(role.id);
    }
    for (const edge of graph.edges) {
      if (edges.has(edge.id))
        ctx.addIssue({ code: "custom", message: "Duplicate edge ID", path: ["edges"] });
      edges.set(edge.id, edge);
      if (!vertices.has(edge.from) || !vertices.has(edge.to))
        ctx.addIssue({
          code: "custom",
          message: "Edge endpoint vertex does not exist",
          path: ["edges"],
        });
      if (edge.roleId !== undefined && !roles.has(edge.roleId))
        ctx.addIssue({ code: "custom", message: "Edge role does not exist", path: ["edges"] });
    }
    const ordered = new Set<string>();
    for (const order of graph.junctionOrders) {
      if (!vertices.has(order.vertexId))
        ctx.addIssue({
          code: "custom",
          message: "Junction vertex does not exist",
          path: ["junctionOrders"],
        });
      if (ordered.has(order.vertexId))
        ctx.addIssue({
          code: "custom",
          message: "Duplicate junction order",
          path: ["junctionOrders"],
        });
      ordered.add(order.vertexId);
      if (order.status !== "specified") continue;
      const ends = new Set<string>();
      for (const endpoint of order.ends) {
        const key = `${endpoint.edgeId}/${endpoint.end}`;
        if (ends.has(key))
          ctx.addIssue({
            code: "custom",
            message: "Duplicate ordered edge end",
            path: ["junctionOrders"],
          });
        ends.add(key);
        const edge = edges.get(endpoint.edgeId);
        if (edge === undefined || edge[endpoint.end] !== order.vertexId)
          ctx.addIssue({
            code: "custom",
            message: "Ordered edge end is not incident at this vertex",
            path: ["junctionOrders"],
          });
      }
      for (const edge of graph.edges) {
        if (edge.from === order.vertexId && !ends.has(`${edge.id}/from`))
          ctx.addIssue({
            code: "custom",
            message: "Junction order omits an incident from-end",
            path: ["junctionOrders"],
          });
        if (edge.to === order.vertexId && !ends.has(`${edge.id}/to`))
          ctx.addIssue({
            code: "custom",
            message: "Junction order omits an incident to-end",
            path: ["junctionOrders"],
          });
      }
    }
  });

export type EdgeDirection = z.infer<typeof EdgeDirectionSchema>;
export type EdgeEnd = z.infer<typeof EdgeEndSchema>;
export type EdgeEndReference = z.infer<typeof EdgeEndReferenceSchema>;
export type Vertex = z.infer<typeof VertexSchema>;
export type EdgeRole = z.infer<typeof EdgeRoleSchema>;
export type Edge = z.infer<typeof EdgeSchema>;
export type JunctionOrder = z.infer<typeof JunctionOrderSchema>;
export type DiagramGraph = z.infer<typeof DiagramGraphSchema>;
