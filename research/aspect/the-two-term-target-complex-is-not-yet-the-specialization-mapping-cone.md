# The two-term target complex is not yet the specialization mapping cone

## What the proposed checker constructs

The candidate checker builds two two-term complexes and a chain map between them:

\[
[R\longrightarrow N]
\longrightarrow
[B\longrightarrow S].
\]

It checks that the source relation space has rank two, the Bockstein line has rank one, the target differential is injective, its image is the rank-one sheet defect, and the chain square commutes. It also checks invariance under one relation-basis change.

These are substantive results. If they pass, the former sheet defect is explicitly the boundary of the target generator in (B).

## What it does not construct

The checker does not assemble the block differential of the mapping cone of the chain map. Consequently it does not:

1. verify that consecutive cone differentials compose to zero;
2. compute kernels and images of the cone differential;
3. report specialization-cone homology dimensions;
4. export the primitive as a typed element and transport it across charts.

Target-complex exactness and mapping-cone cohomology are different statements. The former may hold while the latter retains classes from the source, target, kernel, or cokernel of the induced map.

## Admission boundary

The current checker may establish:

> The gamma-Bockstein line supplies an injective target differential whose image is exactly the rank-one weighted-sheet defect, and the displayed chain square commutes.

It may not yet establish:

> The specialization mapping-cone cohomology has been computed or vanishes.

The successor must export the full block cone matrices, their square-zero residuals, graded homology ranks, and the explicit transported primitive.

## Verification

```text
uv run python research/aspect/checkers/check_specialization_cone_checker_scope.py
```
