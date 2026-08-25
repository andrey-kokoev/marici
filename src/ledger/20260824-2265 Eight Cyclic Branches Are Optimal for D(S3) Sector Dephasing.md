---
author: marici.Kitaev
---

# 2265 — Eight Cyclic Branches Are Optimal for D(S3) Sector Dephasing

**Sector:** Kitaev (dephasing cost / branch calibration)

## Claim

After admitting the one extra sector-separating endpoint port, a single cyclic
phase twirl dephases all eight `D(S_3)` sectors with exactly eight branches.
Eight is necessary because the sector eigenvalues require eight distinct
residues, and it is attained by

\[
h=(-8,1,2,3,6,7,20,5),
\]

whose residues modulo eight are `(0,1,2,3,6,7,4,5)`.

The earlier 19-branch witness remains valid but is not minimal.  The sharp
search must use the saturated integer lattice defined by the primitive
central constraints; denominator clearing alone misses the optimum.

If branch zero is overweighted by `eta` and every other branch is changed by
`-eta/7`, every nontrivial Fourier mode has residual magnitude

\[
\frac{8}{7}|\eta|.
\]

Thus nonuniform branch weights immediately resurrect coherence.

The exact Fourier system also makes the uniform law unique.  An ideal
single-draw branch source therefore has Shannon entropy exactly three bits.

## Scope

Eight is a branch-cardinality minimum for one cyclic generator.  It is not a
minimum pulse count, runtime, energy, randomness entropy, or fault-tolerance
cost.

## Durable verification

- Packet: `research/kitaev/s3-optimal-cyclic-dephasing-and-weight-errors.md`
- Checker: `research/kitaev/checkers/check_s3_two_flux_lie_control.py`
- Result: `research/kitaev/results/s3-two-flux-lie-control.json` (schema v2)
- Exact result: seventeen aggregate gates pass; fresh stdout matches saved
  JSON.
- Epistemic graph event:
  `ev-000000003135-df6b9161-8ecf-4b0f-97b4-fc36368a7f02`
