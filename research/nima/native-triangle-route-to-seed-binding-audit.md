# Concrete native triangle trace: existing executor, missing seed binding

## Existing formal instance found and freshly checked

`agda/ThreeRecordTriangleRegression.agda` instantiates `NativeNormalizationRouteCompiler` with distinct Boolean-carrying presentation types ARecord, BRecord and CRecord. This is an actual ordered route compiler, not merely the generic arbitrary-arity resolution interface.

The supplied equivalences abIso and bcIso flip Boolean payloads. The independently written direct map raw-ac preserves the Boolean; it receives its coherent certificate only after the two flips are proved to cancel. The explicit route `via` is AB followed by BC. The route `direct` is AC.

For x=false the trace is A(false)->B(true)->C(false); for x=true it is A(true)->B(false)->C(true). These are formal presentation values, not an identification with the original seed's physical vertices.

## Actual compilation path

For a supplied coherent map f and input x:

1. `at P x` and `at R (fst (f x))` give complete endpoint packages.
2. `map-equiv f` certifies the actual supplied function as an equivalence.
3. `edge-rule f x` is the native comparison rule between these pointed packages.
4. `native-edge` applies that rule with canonical endpoint derivations under the compiler's declared seed basis.
5. `Slots`, `packages` and `native-steps` enumerate the ordered supplied route recursively.
6. `compile` packages these comparison derivations by a Pi rule; `compile-leaves` proves their canonical-leaf structure.
7. `execute` applies the maps in route order, and `execution-agrees` proves agreement with route evaluation.

The first execution has two steps and the direct route one. Their results agree, but a step-count argument proves the route syntax distinct. Both are retained in the promoted comparison, and the second compiler cycle preserves them.

This refines the earlier generic emission audit: an ordered finite executor DOES already exist for a supplied coherent route. We need not invent a new scheduler for that fragment. Its route order and link laws are inputs, not derived from the six-arrow seed. Pure evaluation/compilation also does not allocate the fresh runtime IDs of the Python execution ledger or assert positive physical traversal cost.

## Why this is not yet the requested seed loop

The instance is AB,BC,AC, not AB,BC,CA. It compares two A-to-C routes; it does not execute the closed seed triangle. Inverting a certified AC equivalence could mathematically construct a C-to-A map, but identifying that inverse with the separately supplied primitive CA would be another binding premise. It must not be silently inserted.

The exact missing premises are:

- a typed interpretation of the original seed's A,B,C packages in these presentation types;
- evidence that its AB and BC occurrences are these supplied flip maps;
- its actual CA map/witness, and any justified relation to the inverse direct AC;
- the source admission of that closed route as an execution, plus the occurrence-instance binding if fresh execution receipts are required.

The D branch and shared BA occurrence would then need the same kind of binding before extending to both triangles. No physical readout, reset authority, costs or timescale follow from the Boolean route calculation.

## Fresh verification

    pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module ThreeRecordTriangleRegression -Fresh

Passed with safe/cubical/guardedness and fresh interface checking. Existing receipt: `results/agda-ThreeRecordTriangleRegression.json`. No Agda source was changed. The existing negative theorems reject the conflicting direct link and prove retained route distinction.

## Productive stopping point

We now have a concrete native executor to reuse, rather than another conditional scheduling prototype. The next required evidence is the seed-to-route binding above. Constructing an arbitrary Boolean CA inverse would produce another consistent example, not derive that binding.
