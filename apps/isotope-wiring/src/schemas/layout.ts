import { z } from "zod";
import {
  CountSchema,
  EdgeIdSchema,
  NonEmptyTextSchema,
  PositiveCountSchema,
  ReviewSchema,
  SafeIntegerSchema,
  VertexIdSchema,
} from "./primitives.js";

// Authored exact values, including fractional coordinates; never used to infer incidence.
export const RationalCoordinateSchema = z.strictObject({
  numerator: SafeIntegerSchema,
  denominator: PositiveCountSchema,
});
export const LogicalCoordinateSchema = z.union([SafeIntegerSchema, RationalCoordinateSchema]);
export const LogicalPointSchema = z.strictObject({
  x: LogicalCoordinateSchema,
  y: LogicalCoordinateSchema,
});
export const ViewBoxSchema = z.strictObject({
  x: SafeIntegerSchema,
  y: SafeIntegerSchema,
  width: PositiveCountSchema,
  height: PositiveCountSchema,
});
export const EdgeColorSchema = z.enum(["red", "blue", "green"]);
export const VertexPlacementSchema = z.strictObject({
  vertexId: VertexIdSchema,
  position: LogicalPointSchema,
});
export const EdgePresentationSchema = z.strictObject({
  edgeId: EdgeIdSchema,
  color: EdgeColorSchema,
  via: z.array(LogicalPointSchema),
  labelPosition: z.literal("midpoint"),
});
export const EdgeAliasSchema = z.strictObject({
  edgeId: EdgeIdSchema,
  number: CountSchema,
  source: NonEmptyTextSchema,
  review: ReviewSchema,
});
export const DiagramLayoutSchema = z.strictObject({
  coordinateSystem: z.literal("authored-exact-plane"),
  viewBox: ViewBoxSchema,
  vertices: z.array(VertexPlacementSchema),
  edges: z.array(EdgePresentationSchema),
  aliases: z.array(EdgeAliasSchema),
});

export type RationalCoordinate = z.infer<typeof RationalCoordinateSchema>;
export type LogicalCoordinate = z.infer<typeof LogicalCoordinateSchema>;
export type LogicalPoint = z.infer<typeof LogicalPointSchema>;
export type ViewBox = z.infer<typeof ViewBoxSchema>;
export type EdgeColor = z.infer<typeof EdgeColorSchema>;
export type VertexPlacement = z.infer<typeof VertexPlacementSchema>;
export type EdgePresentation = z.infer<typeof EdgePresentationSchema>;
export type EdgeAlias = z.infer<typeof EdgeAliasSchema>;
export type DiagramLayout = z.infer<typeof DiagramLayoutSchema>;
