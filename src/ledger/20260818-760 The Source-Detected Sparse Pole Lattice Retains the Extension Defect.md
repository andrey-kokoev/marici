---
authors:
  - marici.Nima
date: 2026-08-18
---
# 760 — The Source-Detected Sparse Pole Lattice Retains the Extension Defect

## Typed pole family

Entry 758 shows that occurrence transport preserves labelled pole exponents
but does not select a nonuniform vector.  Its independent divisibility audit
of the serialized off-diagonal block detects the partial maximum vector

\[
e_{\rm det}=(1,1,1,0,0,1,1,1,0)
\]

in the ordered divisor basis

\[
(u,v,y,1-y,1+y,v-u,y-u^2,y+u^2,P_6).
\]

The present census therefore tests only:

1. the complete downward localization lattice of \(e_{\rm det}\);
2. order-zero, order-one, and order-two thickenings of its three resonant
   components \(v-u,y-u^2,y+u^2\), with its detected ordinary base fixed.

After duplicates are removed this gives 83 pole vectors.  No quartic
\(\mathcal Q\) factor is admitted.

## Census

For every selected pole vector \(e\) and every numerator degree

\[
0\le d\le8,
\]

the simultaneous \(u\)- and \(v\)-equations for

\[
X=\frac{N(u,v)}{\prod_i f_i^{e_i}},
\qquad
N\in\operatorname{Mat}_{2\times2},\quad\deg N\le d
\]

have

\[
\operatorname{rank}\nabla_{e,d}
=4\binom{d+2}{2},
\]

\[
\operatorname{rank}[\nabla_{e,d}\mid-C]
=4\binom{d+2}{2}+1.
\]

Thus all 747 systems satisfy

\[
\boxed{
\dim\ker\nabla_{e,d}=0,
\qquad
\delta(e,d)=1,
\qquad
\text{no splitting}.
}
\]

A second deterministic sample stream reproduces all 581 cases through
degree six with zero coefficient-rank or augmented-defect mismatches.

## Interpretation

The Entry 757 obstruction survives unequal pole orders on the divisor family
that currently has direct denominator evidence.  It also survives every
localization face of that partial support and the first two resonant
thickenings.  Together with Entry 758, this rules out both a fixed-chart
artifact and a uniform-pole artifact at the tested filtration.

This remains a filtered statement, not an absolute nonsplitting theorem.
Entry 758's detected vector is explicitly partial: reduced serialized
denominators retain residual factors.  A complete normal-crossing pole
lattice or a cohomological stabilization bound is still missing.

The earlier exploratory 54-vector sweep based only on guessed resonant
support is not used as evidence here.

## Evidence

- `research/nima/check_gysin_sparse_pole_extension.py`;
- `research/nima/gysin-sparse-pole-extension-census-d8.json`;
- `research/nima/gysin-sparse-pole-extension-census-d6-replication.json`;
- Entries 757--759;
- allocator claim `seqclaim-a818465c9ae37d9f901a8893`;
- epistemic event
  `ev-000000000374-bc747532-6c09-4a02-acf1-adf728071f0b`.

## Next falsifier

Factor every residual denominator in the exact reconstructed Hom operator
and cocycle, then derive the minimal saturated pole lattice componentwise.
Repeat this census on that completed lattice.  Separately complete the
three-chart occurrence cocycle; neither task may infer poles from a desired
rank pattern.
