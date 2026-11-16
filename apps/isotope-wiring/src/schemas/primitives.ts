import { z } from "zod";

export const NonEmptyTextSchema = z.string().trim().min(1);
export const SafeIntegerSchema = z.number().int().safe();
export const CountSchema = SafeIntegerSchema.nonnegative();
export const PositiveCountSchema = SafeIntegerSchema.positive();
const IdentifierSchema = z.string().regex(/^[A-Za-z][A-Za-z0-9._:-]*$/);
export const IsotopeIdSchema = IdentifierSchema.brand<"IsotopeId">();
export const DocumentIdSchema = IdentifierSchema.brand<"DocumentId">();
export const VertexIdSchema = IdentifierSchema.brand<"VertexId">();
export const EdgeIdSchema = IdentifierSchema.brand<"EdgeId">();
export const RoleIdSchema = IdentifierSchema.brand<"RoleId">();
export const RevisionSchema = CountSchema.brand<"Revision">();
export const ReviewSchema = z.discriminatedUnion("status", [
  z.strictObject({ status: z.literal("unreviewed"), questions: z.array(NonEmptyTextSchema) }),
  z.strictObject({ status: z.literal("reviewed"), evidence: NonEmptyTextSchema }),
]);
export const DocumentReferenceSchema = z.strictObject({
  documentId: DocumentIdSchema,
  revision: RevisionSchema,
});
