import { z } from "zod";
import { DocumentIdSchema, EdgeIdSchema } from "./primitives.js";
import { SavedEdgeEditsSchema } from "./edge-edits.js";
import { TurnSchema } from "./traversal.js";

export const VersionNameSchema = z.string().trim().min(1).max(80);
export const NamedVersionSchema = z
  .strictObject({
    name: VersionNameSchema,
    documentId: DocumentIdSchema,
    geometry: z.string().min(1),
    edits: SavedEdgeEditsSchema,
    startEdge: EdgeIdSchema.nullable(),
    initialTurn: TurnSchema,
  })
  .refine((value) => value.documentId === value.edits.documentId, "Snapshot document mismatch");
export const VersionLibrarySchema = z
  .strictObject({
    format: z.literal("1"),
    documentId: DocumentIdSchema,
    entries: z.array(NamedVersionSchema).max(100),
  })
  .superRefine((value, ctx) => {
    if (
      new Set(value.entries.map((entry) => entry.name.toLowerCase())).size !== value.entries.length
    )
      ctx.addIssue({ code: "custom", message: "A version with this name already exists" });
    if (value.entries.some((entry) => entry.documentId !== value.documentId))
      ctx.addIssue({ code: "custom", message: "Version belongs to another diagram" });
  });
export type NamedVersion = z.infer<typeof NamedVersionSchema>;
export type VersionLibrary = z.infer<typeof VersionLibrarySchema>;
