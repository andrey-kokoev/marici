# Returning edits through families of families

## Induced metric of a promoted mean

Let x be the leaf member vector with Euclidean edit cost ||delta x||^2 and
let y=A x be the promoted family means. For disjoint families of sizes n_i,

    A A^T = diag(1/n_i),
    W = (A A^T)^-1 = diag(n_i).

The least leaf cost of a family-mean edit delta y is delta y^T W delta y.
The metric is therefore transported from retained membership; equal cost per
fresh label generally changes the return operation.

Let z=B y be a higher-level readout. Its minimum-cost staged return is

    delta y = W^-1 B^T (B W^-1 B^T)^-1 delta z,
    delta x = A^T W delta y.

Substituting W^-1=A A^T gives

    delta x = (B A)^T [(B A)(B A)^T]^-1 delta z,

the direct least-change leaf return. These inverse formulas assume the displayed
readouts have full row rank; compatible redundant readouts use pseudoinverses
and restrictions to their images.

For arithmetic means over unions of disjoint families, B weights each child
mean by its original member count divided by the union count. This preserves
the underlying leaf readout as well as its edit metric.

## Overlapping families

For the joint source/target mean map O,64 readout coordinates have rank47.
The correct edit metric is (O O^T)^+ on image(O). Its off-diagonal terms retain
family overlaps. Replacing it by diagonal group sizes ignores coupling and
compatibility constraints. Minimum-cost return through this image again equals
direct return for the same compatible upper readout.

## Executable fixtures

Use137 leaf slots,32 source families, eight upper families grouped by block
and first source, then one global mean. The same member data and readout are
used in the direct and staged tests.

- Direct and correctly weighted staged updates agree to4.44e-16.
- Treating promoted means with a fresh Euclidean metric changes the leaf update
  by norm0.428218972061 while still reaching the requested upper means.
- Its squared edit cost is16.933371488, versus16.75 for direct return.
- A global mean increase of0.7 shifts every leaf by0.7 through all three levels.
- Source-indexed and target-indexed routes to the same arrow/state block-mean
  request yield the same leaf update.
- The joint overlapping64-family route also reproduces direct return when its
  full quotient metric and compatible-image constraint are used.

These are linear readout/return tests. Full record identity/version management,
next-level endpoint selection, and nonlinear aggregation are not implemented.

## Structural consequence

For the declared mean/minimum-change contract, promotion can preserve both read
and return semantics. Retaining members transports the readout weights; the
induced metric transports the cost of changing them. With both carried forward,
returning an edit is independent of the intermediate indexing route whenever
those routes represent the same final leaf readout.

This is a concrete criterion for a coherent recursive software architecture.
The resulting metric coefficients and gains follow from membership and overlap
under the chosen leaf metric. Their physical meaning and absolute normalization
remain separate questions. The statement does not make all distinct readouts
or incompatible edits equivalent.

## Verification

    OPENBLAS_NUM_THREADS=1 uv run research/nima/checkers/check_family_return_composition.py

Checks weighted readout composition, direct/staged minimum-change returns,
a naive-metric negative control, three-level global return, source/target route
agreement, and an overlapping quotient-metric return. NumPy with explicit
tolerances; deterministic fixture; no physical constants.
