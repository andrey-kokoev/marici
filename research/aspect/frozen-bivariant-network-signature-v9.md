# Frozen parameterized-resolvent network signature v9

## Status

Version 9 is a new frozen local candidate. Version 8 remains unchanged and falsified.

v9 replaces the zero-only spectral germ with a holomorphic resolvent sheaf over a declared complex spectral domain.

## Repair of the v8 hostile

For the non-normal finite sections

\[
A_N=2I+S_N,
\]

the point (z=5/2) is outside every finite spectrum, but a resolvent entry grows as (2^N). In the unilateral-shift completion, (5/2) becomes spectral.

v9 requires finite-section resolvents to be locally uniformly bounded on every compact subset promoted as part of the completed resolvent domain. The exponential sequence fails that gate and becomes a retained pseudospectral defect.

Finite spectral sets cannot promote without a vanishing resolvent-comparison cone.

## Resolvent sheaf

The spectral domain is declared explicitly. Local sections

\[
R(z)=(A-zI)^{-1}
\]

must be holomorphic and satisfy the resolvent identity

\[
R(z)-R(w)=(z-w)R(z)R(w).
\]

They must glue under restriction and intertwine both holonomy and specialization.

For each positive tolerance, unbounded finite resolvents define a pseudospectral defect set. Nonvanishing limits of those sets are included in the completed spectral support.

## First unused hostile

Take bounded scalar samples

\[
R(0)=1,
\qquad
R(1)=1.
\]

They are individually harmless but violate the resolvent identity:

\[
R(0)-R(1)=0,
\qquad
(0-1)R(0)R(1)=-1.
\]

v9 rejects them. Pointwise bounded response data are not automatically a resolvent family.

## Frozen exclusions

v9 forbids:

- promoting finite spectra without locally uniform resolvent bounds;
- promoting pointwise response samples without the resolvent identity;
- promoting zero-point control to a parameterized spectral claim;
- discarding pseudospectral blow-up because every finite shifted operator is invertible;
- promoting strong operator convergence to spectral convergence without resolvent control;
- replacing topological cone accounting with a spectral gate.

## Next falsifier

Attack analytic continuation. A spectral family with branch points may possess valid local resolvent sheets whose continuation has nontrivial monodromy. If v9 treats those sections as a single-valued sheaf, it will need a covering, stack, or gerbe of spectral frames.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_frozen_bivariant_signature_v9.py
```
