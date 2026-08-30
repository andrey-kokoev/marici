---
title: "The P6 Relative-Sign Extension Residue Is Gauge Removable"
entry: 1766
date: 2026-08-21
status: established-local-indicial
---

# 1766 — The (P_6) Relative-Sign Extension Residue Is Gauge Removable

## Question

Entry 1765 finds intrinsic relative monodromy

\[
\operatorname{diag}(-1,+1)
\]

on the split algebraic submodule, but no diagonal lift through the marked
extension.  Can a nonsplit triangular nearby-cycle extension intrinsically
attach the marked quotient to the (-1)-monodromy line?

## Frozen diagonal residues

The source-derived wall quotient connection of Entry 855 has denominators

\[
u, u-2, v-2, u+v-2, D, H,
\]

all coprime to (P_6).  Hence at generic (P_6=0),

\[
R_{W_3}=0_3.
\]

Entry 867 gives

\[
R_{\mathcal A}
=
\operatorname{diag}\left(-\frac12,0\right)
\]

in the ordered split algebraic lines

\[
\left(
\mathcal L_{P_6^{-1/2}},
\mathcal L_{D_1}
\right).
\]

## Hom-indicial calculation

For a regular triangular gauge

\[
h:W_3\longrightarrow\mathcal A,
\]

the degree-zero residue operator is

\[
L_0(h)=R_{\mathcal A}h-hR_{W_3}.
\]

Its linewise ranks and kernels are

\[
\begin{array}{c|cc}
&\mathcal L_{P_6^{-1/2}}&\mathcal L_{D_1}\\
\hline
\operatorname{rank}L_0&3&0\\
\dim\ker L_0&0&3.
\end{array}
\]

Therefore (L_0) is invertible on every residue column landing in the
(-1)-monodromy line.  Such a residue can always be removed by a regular
triangular gauge.

## Result

\[
\boxed{
\text{No intrinsic logarithmic extension at }P_6
\text{ can live on the relative-sign line.}
}
\]

The only resonant local extension slot is the rank-three space landing in
the (+1)-monodromy line (mathcal L_{D_1}).  It cannot implement the
selective companion deletion of Entry 1761.

Thus both proposed lifts of the relative sign are closed:

- diagonal lift: obstructed by Entry 1765;
- triangular logarithmic lift: gauge-trivial on the relative-sign line by
  this entry.

This is local at generic (P_6=0).  Deeper intersections may have different
indicial spectra, but they must be tested as existing-carrier intersections,
not as new carrier strata.

## Durable artifacts

- checker: `research/benincasa/checkers/p6_hom_indicial_gate.rs`;
- result: `research/benincasa/results/p6-hom-indicial-gate.json`;
- convention note: `research/benincasa/p6-hom-indicial-gate.md`;
- allocator claim: `seqclaim-8de3b82fb0f9ff13d8cbe1ca`.

