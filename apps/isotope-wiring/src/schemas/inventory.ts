import { z } from "zod";
import {
  CountSchema,
  IsotopeIdSchema,
  NonEmptyTextSchema,
  SafeIntegerSchema,
} from "./primitives.js";

export const ElectronCountSchema = z.discriminatedUnion("status", [
  z.strictObject({ status: z.literal("unspecified") }),
  z.strictObject({ status: z.literal("specified"), value: CountSchema }),
]);
export const ChargeSchema = z.discriminatedUnion("status", [
  z.strictObject({ status: z.literal("unspecified") }),
  z.strictObject({ status: z.literal("specified"), value: SafeIntegerSchema }),
]);
/** Basic authored facts and source citations; not an attestation workflow. */
export const IsotopeRecordSchema = z
  .strictObject({
    id: IsotopeIdSchema,
    name: NonEmptyTextSchema,
    symbol: z.string().regex(/^[A-Z][a-z]?$/),
    protons: CountSchema,
    neutrons: CountSchema,
    electrons: ElectronCountSchema,
    charge: ChargeSchema,
    sources: z.array(NonEmptyTextSchema),
  })
  .superRefine((record, ctx) => {
    if (!Number.isSafeInteger(record.protons + record.neutrons))
      ctx.addIssue({ code: "custom", message: "Mass number exceeds exact integer representation" });
    if (
      record.electrons.status === "specified" &&
      record.charge.status === "specified" &&
      record.protons - record.electrons.value !== record.charge.value
    )
      ctx.addIssue({ code: "custom", message: "Specified electron count and charge disagree" });
  });
export type IsotopeRecord = z.infer<typeof IsotopeRecordSchema>;
