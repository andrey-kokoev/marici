# 3328 — The Two-Soft No-Infinity Condition Leaves One Logarithmic Extension Line

## Question

Entries 3323 and 3326 identify the primitive (e_6) form as an (A_2)
boundary cocycle. How much freedom remains after imposing its actual support
and regularity conditions?

This classifies the admissible logarithmic forms. It does not infer which
rank-twelve coordinate carries one.

## Logarithmic base

Use the homogeneous base (mathbf P^1_v) with labelled boundary

\[
D=\{v=0\}\cup\{v=2\}\cup\{v=\infty\}.
\]

The finite points are the existing soft divisors

\[
v=0\iff X_3=0,
\qquad
v=2\iff X_2=0.
\]

A logarithmic one-form with finite poles only at these points is

\[
\omega=
r_0\frac{dv}{v}
+r_2\frac{dv}{v-2}.
\]

Its residue at infinity is

\[
r_\infty=-r_0-r_2.
\]

## No-infinity condition

The source candidate has no infinity pole. Therefore

\[
r_0+r_2=0.
\]

The two-dimensional finite-pole space consequently collapses to the unique
line

\[
\mathbb Q\left\langle
d\log\frac{v}{v-2}
\right\rangle.
\]

Its primitive integral residue vector, ordered by (0,2,\infty), is

\[
(1,-1,0).
\]

The source double-pole coefficient fixes the candidate scale:

\[
C_2=-\frac18,
\qquad
C_2d\log\frac{v}{v-2}
=\frac{dv}{4v(v-2)}.
\]

## Result

Once the following conditions are frozen,

- logarithmic poles only at (X_3=0) and (X_2=0);
- no residue at infinity;
- primitive opposite boundary orientation;

there is exactly one admissible logarithmic extension line. Entry 3323's
cyclic Leray cocycle generates it, and (C_2) supplies its source scale.

## Non-identifiability boundary

Uniqueness of the line does not identify its location inside a larger
extension matrix. A closed triangle of transition functions can arise from
different moving blocks, as emphasized independently by Aspect's moving-fiber
interferometer audit.

Therefore this result establishes:

- the unique admissible logarithmic class;
- its integral residue lattice;
- its source normalization.

It does not establish:

- that (B_{e_6,q_0}) is nonzero;
- that another rank-twelve coordinate does not carry the same class;
- that the physical relative chain pairs nontrivially with it.

## Next falsifier

Derive the complete rank-twelve transition between two labelled occurrence
charts and compute its triangular logarithmic block. The source selects the
(e_6) torsor only if the boundary-preserving transition places this unique
class in the ((e_6,q_0)) coordinate independently of splitting choices.

## Verification

The checker is
`research/benincasa/checkers/audit_soft_logarithmic_ext_line.py`; its packet is
`research/benincasa/results/soft_logarithmic_ext_line.json`.

Allocator claim: `seqclaim-2181be5a80f7dc7ac351d566`.
