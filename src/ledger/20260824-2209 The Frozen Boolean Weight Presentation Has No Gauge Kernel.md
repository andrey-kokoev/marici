---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2209 — The Frozen Boolean Weight Presentation Has No Gauge Kernel

## Integral uniqueness

In subset order the Boolean zeta matrix is unitriangular. Therefore

\[
\det Z=1
\]

and \(Z\) is invertible over \(\mathbb Z\). Consequently

\[
\boxed{
\ker Z=0.
}
\]

No nonzero redistribution of the eight overlap coefficients preserves every
resolved-cell weight. In particular, once the source's Boolean cover and
cell orientation function are frozen, the coefficients \((-2)^{|S|}\) and
their edge tangents are uniquely determined.

## Distinction from scalar-route gauge

Entry 2194 found a redistribution ambiguity after projecting to the scalar
correlator. Entry 2209 shows that this ambiguity is not present in the full
weighted-cell geometry. It is created by forgetting resolved cell weights,
not by a redundancy of the source subdivision itself.

Thus the selector is intrinsic to the weighted Boolean geometry even though
it does not descend to the scalar readout.

## Evidence

- Entries 2194 and 2206–2208
- `research/benincasa/checkers/boolean_zeta_unimodular.rs`
