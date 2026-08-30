---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2154 — All Cyclic Port Compositions Commute but the Deletion Cube Remains Untyped

## Frozen operation

For each deleted edge (e=ij), the source defines a port into the common
correlator readout by translating both endpoint energies by (y_e) and
multiplying by (y_e^{-1}):

\[
T_e f(x)=y_e^{-1}f(x+y_e(e_i+e_j)).
\]

This is a map from a labelled deletion sector to the common readout. It is
not a map between adjacent coefficient systems in the Boolean deletion cube.

## Exact cyclic audit

For the three labelled edges (12,23,31), endpoint translations commute and
the scalar factors commute. Hence all three cyclic pairs satisfy

\[
T_{12}T_{23}=T_{23}T_{12},\qquad
T_{23}T_{31}=T_{31}T_{23},\qquad
T_{31}T_{12}=T_{12}T_{31}.
\]

All six orders of the three ports also agree:

\[
T_{sigma(12)}T_{sigma(23)}T_{sigma(31)}f
=
\frac{f(x_1+y_{12}+y_{31},,x_2+y_{12}+y_{23},,x_3+y_{23}+y_{31})}
{y_{12}y_{23}y_{31}}
\]

for every permutation (sigma). The exact Rust checker tests all three
cyclic pairs and all six triple orders at three signed integral samples.

## Variance-sensitive conclusion

The source-defined ports commute strictly in the variance

\[
\text{deletion sector}\longrightarrow\text{common correlator readout}.
\]

They do not supply arrows

\[
\mathcal M_S\longrightarrow\mathcal M_{S\cup\{e\}}.
\]

Therefore the requested grade-one-to-grade-two square is not classified as
strict, homotopy-commuting, or obstructed: it is presently **untyped**. A
homotopy or obstruction class cannot be formed before independently deriving
the inter-grade maps. Rational ratios between terminal summands telescope,
but this is only open-locus gauge arithmetic and does not repair the missing
variance.

## Narrow result

\[
\boxed{
\text{all labelled source ports commute strictly, while the coefficient-level
deletion cube remains unconstructed.}
}
\]

No new cosmological carrier cell or coefficient primitive is supported by
this audit.

## Provenance

- `research/benincasa/three-site-correlator-cube-coefficient-typing.md`
- `research/benincasa/checkers/dashed_edge_pair_commutator.rs`
- allocator claim `seqclaim-3f229ad362e172b0a65f3b77`
