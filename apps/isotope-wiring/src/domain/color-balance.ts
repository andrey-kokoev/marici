import { type DiagramDocument } from "../schemas/document.js";
import { ColorBalanceSchema, type ColorBalance } from "../schemas/traversal.js";

/** Count distinct model edges, not route steps or rendered arrowheads. */
export function inspectColorBalance(document: DiagramDocument): ColorBalance {
  const red = document.layout.edges.filter((edge) => edge.color === "red").length;
  const blue = document.layout.edges.filter((edge) => edge.color === "blue").length;
  return ColorBalanceSchema.parse({ red, blue, balanced: red === blue });
}
