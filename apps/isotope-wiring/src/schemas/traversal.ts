import { z } from "zod";
import {
  NonEmptyTextSchema,
  CountSchema,
  DocumentReferenceSchema,
  EdgeIdSchema,
  VertexIdSchema,
} from "./primitives.js";

import { EdgeColorSchema } from "./layout.js";

export const ActiveColorSchema = EdgeColorSchema.exclude(["green"]);
export type ActiveColor = z.infer<typeof ActiveColorSchema>;
export const ColorBalanceSchema = z
  .strictObject({
    red: CountSchema,
    blue: CountSchema,
    balanced: z.boolean(),
  })
  .refine(
    (value) => value.balanced === (value.red === value.blue),
    "Incorrect color-balance result",
  );
export type ColorBalance = z.infer<typeof ColorBalanceSchema>;
export const TurnSchema = z.enum(["left", "right"]);
export const TraversalPolicySchema = z.discriminatedUnion("status", [
  z.strictObject({
    status: z.literal("unresolved"),
    questions: z.array(NonEmptyTextSchema).min(1),
  }),
  z.strictObject({
    status: z.literal("alternating"),
    version: z.literal(14),
    coloredEdges: z.literal("visit-once-finish-active-color"),
    initialTurn: TurnSchema,
    orientation: z.literal("authored-plane-y-down"),
    straight: z.literal("preserve-turn"),
    greenContinuation: z.literal("straight-before-colored"),
    exitSelection: z.literal("own-color-first-angular-extreme"),
    ambiguity: z.literal("stop"),
  }),
]);
export const RouteStepSchema = z.strictObject({
  edgeId: EdgeIdSchema,
  from: VertexIdSchema,
  to: VertexIdSchema,
  pendingTurn: TurnSchema,
});
export const RouteResultSchema = z
  .strictObject({
    document: DocumentReferenceSchema,
    policyVersion: z.literal(14).nullable(),
    activeColor: ActiveColorSchema.nullable(),
    colorBalance: ColorBalanceSchema,
    remainingColoredEdges: z.array(EdgeIdSchema),
    initialTurn: TurnSchema,
    steps: z.array(RouteStepSchema),
    status: z.enum([
      "unresolved",
      "completed",
      "invalid-start",
      "invalid-color-balance",
      "ambiguous",
      "no-continuation",
      "repeated-state",
      "degenerate-geometry",
    ]),
    message: z.string(),
    candidates: z.array(EdgeIdSchema),
  })
  .superRefine((value, ctx) => {
    if (value.status === "completed" && !value.colorBalance.balanced)
      ctx.addIssue({ code: "custom", message: "An unbalanced diagram cannot be marked completed" });
  });
export type Turn = z.infer<typeof TurnSchema>;
export type RouteStep = z.infer<typeof RouteStepSchema>;
export type RouteResult = z.infer<typeof RouteResultSchema>;
