import { z } from "zod";
import {
  DocumentIdSchema,
  RevisionSchema,
  VertexIdSchema,
  EdgeIdSchema,
  CountSchema,
  SafeIntegerSchema,
} from "./primitives.js";
import { RationalCoordinateSchema } from "./layout.js";
export const DartIdSchema = z.string().min(1).brand<"DartId">();
export const SurfaceDartSchema = z.strictObject({
  id: DartIdSchema,
  edgeId: EdgeIdSchema,
  vertexId: VertexIdSchema,
  mate: DartIdSchema,
});
export const SurfaceRotationSchema = z.strictObject({
  vertexId: VertexIdSchema,
  darts: z.array(DartIdSchema),
});
export const SurfaceComponentSchema = z.strictObject({
  vertices: z.array(VertexIdSchema),
  edges: z.array(EdgeIdSchema),
  boundaries: z.array(z.array(DartIdSchema)),
  eulerCharacteristic: SafeIntegerSchema,
  genus: CountSchema,
  firstBettiNumber: CountSchema,
});
export const MorseSurfaceSchema = z.strictObject({
  documentId: DocumentIdSchema,
  revision: RevisionSchema,
  convention: z.enum([
    "clockwise-authored-tangents-untwisted",
    "clockwise-authored-tangents-untwisted-contracted",
  ]),
  contractedEdges: z.array(EdgeIdSchema),
  darts: z.array(SurfaceDartSchema),
  rotations: z.array(SurfaceRotationSchema),
  components: z.array(SurfaceComponentSchema),
  minima: z.array(
    z.strictObject({
      vertexId: VertexIdSchema,
      sourceVertices: z.array(VertexIdSchema).min(1),
      level: RationalCoordinateSchema,
    }),
  ),
  saddles: z.array(z.strictObject({ edgeId: EdgeIdSchema, level: RationalCoordinateSchema })),
  boundaryLevel: z.literal(3),
  maxima: z.literal(0),
  eulerCharacteristic: SafeIntegerSchema,
  genus: CountSchema,
  boundaryCount: CountSchema,
  firstBettiNumber: CountSchema,
  directedCycle: z.array(EdgeIdSchema),
  unresolvedArrows: z.array(EdgeIdSchema),
});
export type DartId = z.infer<typeof DartIdSchema>;
export type SurfaceDart = z.infer<typeof SurfaceDartSchema>;
export type SurfaceRotation = z.infer<typeof SurfaceRotationSchema>;
export type SurfaceComponent = z.infer<typeof SurfaceComponentSchema>;
export type MorseSurface = z.infer<typeof MorseSurfaceSchema>;
