---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2155 — Restriction, Residue, and Kummer Pullback Do Not Construct the Edge-Deletion Arrow

## Hard-to-vary claim

For the labelled edge (12), none of the three predeclared operations

1. ordinary restriction at (y_{12}=0);
2. logarithmic residue/Gysin at (y_{12}=0);
3. endpoint translation followed by multiplication by (y_{12}^{-1});

constructs a morphism between adjacent correlator deletion sectors.

## Exact audit

Let

\[
K_{12}f
=
\frac{f(x_1+y_{12},x_2+y_{12},x_3)}{y_{12}}.
\]

Ordinary restriction is undefined because (K_{12}f) has a simple pole.
After multiplying by (y_{12}), restriction returns (f|_{y_{12}=0}), the
boundary value of the same sector.

Logarithmic residue is well typed:

\[
\operatorname{Res}_{y_{12}=0}
\left(\frac{dy_{12}}{y_{12}}\tau_{12}^*f\right)=f.
\]

It likewise returns a same-sector boundary value. The source gives no
identification of this (f) with the independent graph function in the
adjacent deletion sector.

Finally, the Kummer pullback is horizontal with its forced connection,

\[
(\partial_{y_{12}}+y_{12}^{-1})K_{12}
=K_{12}(\partial_{x_1}+\partial_{x_2}),
\]

but it maps a deletion sector into the common correlator readout. It does not
map one graph-sector module into another.

## Classification

\[
\boxed{
\text{the edge-12 inter-grade deletion arrow remains source-absent.}
}
\]

The failure is one of variance and target typing. It is not a nonzero
cohomological obstruction, and it licenses neither a fitted map nor a new
Carrier cell.

By cyclic relabelling the same source-level diagnosis applies to edges (23)
and (31), although no claim is made that their independently derived period
systems are equal.

## Next falsifier

The only remaining admissible route is an independently existing comparison
between the two graph-sector period systems—for example a source-derived
deletion–restriction triangle whose connecting morphism has the required
domain and codomain. Without it, the Boolean deletion object is an indexing
carrier for a signed sum, not a coefficient complex.

## Provenance

- `research/benincasa/edge12-intergrade-localization-audit.md`
- `research/benincasa/checkers/dashed_edge_kummer_adapter.rs`
- allocator claim `seqclaim-62ce54b273adc1bcd0b9033d`
