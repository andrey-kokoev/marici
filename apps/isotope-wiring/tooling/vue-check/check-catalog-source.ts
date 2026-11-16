import ts from "typescript";
import { fileURLToPath } from "node:url";
import { z } from "zod";

// Use the already-pinned compiler's JSON grammar, not JSON.parse or a regex decoder.
const path = fileURLToPath(
  new URL("../../../../research/matter/isotope-reference.resource.json", import.meta.url),
);
const catalogPath = fileURLToPath(new URL("../../src/examples/catalog.ts", import.meta.url));
const program = ts.createProgram([path, catalogPath], {
  resolveJsonModule: true,
  noEmit: true,
  module: ts.ModuleKind.NodeNext,
  moduleResolution: ts.ModuleResolutionKind.NodeNext,
});
const source = program.getSourceFile(path);
if (source === undefined || program.getSyntacticDiagnostics(source).length > 0)
  throw new Error("Invalid canonical isotope JSON");
const statement = source.statements[0];
if (
  statement === undefined ||
  !ts.isExpressionStatement(statement) ||
  !ts.isObjectLiteralExpression(statement.expression)
)
  throw new Error("Expected isotope resource object");
const property = statement.expression.properties.find(
  (item) =>
    ts.isPropertyAssignment(item) && ts.isStringLiteral(item.name) && item.name.text === "data",
);
if (
  property === undefined ||
  !ts.isPropertyAssignment(property) ||
  !ts.isArrayLiteralExpression(property.initializer)
)
  throw new Error("Missing isotope data array");
const RowSchema = z.tuple([z.string(), z.int().positive(), z.int().nonnegative()]);
function rows(array: ts.ArrayLiteralExpression): Array<z.infer<typeof RowSchema>> {
  return array.elements.map((row) => {
    if (!ts.isArrayLiteralExpression(row)) throw new Error("Invalid isotope row");
    const name = row.elements[0],
      protons = row.elements[1],
      neutrons = row.elements[2];
    if (
      name === undefined ||
      protons === undefined ||
      neutrons === undefined ||
      !ts.isStringLiteral(name) ||
      !ts.isNumericLiteral(protons) ||
      !ts.isNumericLiteral(neutrons)
    )
      throw new Error("Invalid isotope identity/count fields");
    return RowSchema.parse([name.text, Number(protons.text), Number(neutrons.text)]);
  });
}
const expected = rows(property.initializer);
const catalogSource = program.getSourceFile(catalogPath);
if (catalogSource === undefined || program.getSyntacticDiagnostics(catalogSource).length > 0)
  throw new Error("Invalid catalog snapshot");
const declaration = catalogSource.statements
  .flatMap((statement) =>
    ts.isVariableStatement(statement) ? [...statement.declarationList.declarations] : [],
  )
  .find((declaration) => ts.isIdentifier(declaration.name) && declaration.name.text === "rows");
const initializer = declaration?.initializer;
if (initializer === undefined || !ts.isCallExpression(initializer))
  throw new Error("Missing catalog rows");
const array = initializer.arguments[0];
if (array === undefined || !ts.isArrayLiteralExpression(array))
  throw new Error("Catalog rows must be a literal array");
const actual = rows(array);
if (JSON.stringify(actual) !== JSON.stringify(expected))
  throw new Error(
    "Bundled catalog differs from research/matter/isotope-reference.resource.json; update the catalog snapshot",
  );
console.log("PASS: all bundled isotope names/counts match the canonical repository resource");
