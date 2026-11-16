import { z } from "zod";
import { neon20 } from "./neon20.js";
import { hydrogen1, hydrogen2, helium3, helium4 } from "./light-isotopes.js";
import {
  lithium6,
  lithium7,
  beryllium9,
  boron10,
  boron11,
  carbon12,
  carbon13,
  nitrogen14,
  nitrogen15,
  oxygen16,
  oxygen17,
  oxygen18,
  fluorine19,
} from "./pre-neon-isotopes.js";
import { DiagramDocumentSchema } from "../schemas/document.js";
import { EdgeIdSchema } from "../schemas/primitives.js";
const DiagramChoiceSchema = z
  .strictObject({ document: DiagramDocumentSchema, initialEdgeId: EdgeIdSchema })
  .refine(
    (choice) => choice.document.graph.edges.some((edge) => edge.id === choice.initialEdgeId),
    "Initial edge must belong to the diagram",
  );
export type DiagramChoice = z.infer<typeof DiagramChoiceSchema>;
// Availability and activation both use this single collection of implemented diagrams.
const diagrams: ReadonlyMap<string, () => DiagramChoice> = new Map([
  [
    "Hydrogen-1",
    () => DiagramChoiceSchema.parse({ document: hydrogen1(), initialEdgeId: "edge.h1.2" }),
  ],
  [
    "Hydrogen-2",
    () => DiagramChoiceSchema.parse({ document: hydrogen2(), initialEdgeId: "edge.h2.1" }),
  ],
  [
    "Helium-3",
    () => DiagramChoiceSchema.parse({ document: helium3(), initialEdgeId: "edge.he3.1" }),
  ],
  [
    "Helium-4",
    () => DiagramChoiceSchema.parse({ document: helium4(), initialEdgeId: "edge.he4.1" }),
  ],
  [
    "Lithium-6",
    () => DiagramChoiceSchema.parse({ document: lithium6(), initialEdgeId: "edge.li6.1" }),
  ],
  [
    "Lithium-7",
    () => DiagramChoiceSchema.parse({ document: lithium7(), initialEdgeId: "edge.li7.1" }),
  ],
  [
    "Beryllium-9",
    () => DiagramChoiceSchema.parse({ document: beryllium9(), initialEdgeId: "edge.be9.1" }),
  ],
  [
    "Boron-10",
    () => DiagramChoiceSchema.parse({ document: boron10(), initialEdgeId: "edge.b10.9" }),
  ],
  [
    "Boron-11",
    () => DiagramChoiceSchema.parse({ document: boron11(), initialEdgeId: "edge.b11.9" }),
  ],
  [
    "Carbon-12",
    () => DiagramChoiceSchema.parse({ document: carbon12(), initialEdgeId: "edge.c12.9" }),
  ],
  [
    "Carbon-13",
    () => DiagramChoiceSchema.parse({ document: carbon13(), initialEdgeId: "edge.c13.9" }),
  ],
  [
    "Nitrogen-14",
    () => DiagramChoiceSchema.parse({ document: nitrogen14(), initialEdgeId: "edge.n14.9" }),
  ],
  [
    "Nitrogen-15",
    () => DiagramChoiceSchema.parse({ document: nitrogen15(), initialEdgeId: "edge.n15.9" }),
  ],
  [
    "Oxygen-16",
    () => DiagramChoiceSchema.parse({ document: oxygen16(), initialEdgeId: "edge.o16.9" }),
  ],
  [
    "Oxygen-17",
    () => DiagramChoiceSchema.parse({ document: oxygen17(), initialEdgeId: "edge.o17.9" }),
  ],
  [
    "Oxygen-18",
    () => DiagramChoiceSchema.parse({ document: oxygen18(), initialEdgeId: "edge.o18.9" }),
  ],
  [
    "Fluorine-19",
    () => DiagramChoiceSchema.parse({ document: fluorine19(), initialEdgeId: "edge.f19.9" }),
  ],
  [
    "Neon-20",
    () => DiagramChoiceSchema.parse({ document: neon20(), initialEdgeId: "edge.ne20.8" }),
  ],
]);
export function hasDiagram(name: string): boolean {
  return diagrams.has(name);
}
export function createDiagram(name: string): DiagramChoice | null {
  return diagrams.get(name)?.() ?? null;
}
