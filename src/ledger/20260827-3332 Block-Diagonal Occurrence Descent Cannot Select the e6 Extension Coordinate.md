# 3332 — Block-Diagonal Occurrence Descent Cannot Select the e6 Extension Coordinate

## Question

Entries 3323–3328 identify and classify the unique source-normalized
two-soft logarithmic class. Can the cyclic occurrence transition alone place
that class in the rank-twelve coordinate (B_{e_6,q_0})?

## Frozen filtration

The source localization sequence is

\[
0\longrightarrow M_9
\longrightarrow M_{12}
\longrightarrow W_3
\longrightarrow0.
\]

Entry 851 fixes the source basis

\[
(\Omega_{111},\Omega_{101},\Omega_{110},e_1,\ldots,e_9).
\]

Labelled occurrence relabelling preserves the two source-form types:

- wall-lift forms map to wall-lift forms;
- absolute (q)-residue masters map to absolute masters.

The raw occurrence transition therefore preserves (W_3\oplus M_9). Entry
756 independently derives the same property for the larger labelled residue
presentation: source-labelled forms transport by relabelling and the forced
Poincaré-residue sign, without adding lower-filtration forms.

## Exact block calculation

Restrict to the relevant corner with quotient line (q_0) and absolute line
(e_6). A block-diagonal transition is

\[
D=
\begin{pmatrix}
g_q&0\\
0&g_e
\end{pmatrix}.
\]

Its connection gauge term is

\[
dD\,D^{-1}
=
\begin{pmatrix}
d\log g_q&0\\
0&d\log g_e
\end{pmatrix}.
\]

Hence its lower-left entry is identically zero. A logarithmic change of a
diagonal Leray frame cannot manufacture (B_{e_6,q_0}).

The first transition capable of changing that coordinate is triangular:

\[
T=
\begin{pmatrix}
g_q&0\\
h&g_e
\end{pmatrix}.
\]

Its lower-left gauge term is

\[
\frac{dh}{g_q}-\frac{h,dg_e}{g_eg_q}.
\]

Thus a nonzero extension coordinate requires either:

- a source-derived triangular shear (h); or
- the independently reduced source connection block (B).

Neither is supplied by diagonal cyclic-frame descent.

## Result

The cyclic Leray cocycle explains the unique logarithmic class, its soft
support, and its normalization. It does not select the rank-twelve
((e_6,q_0)) insertion.

This is the algebraic version of Aspect's moving-fiber warning: triangle
closure certifies consistent relative motion but does not identify which
internal block moved.

The status is therefore:

- class provenance: established;
- support lattice: established;
- source scale (C_2): established;
- placement in (B_{e_6,q_0}): unproved;
- new carrier structure: none.

## Next falsifier

There are now only two admissible routes:

1. derive a triangular occurrence transition directly from the common
   rank-twelve source forms and prove it is independent of exact-lift choices;
2. certify the characteristic-zero source (B)-block sufficiently to extract
   its unique two-soft logarithmic cohomology class.

A diagonal occurrence transition cannot substitute for either calculation.

## Verification

The checker is
`research/benincasa/checkers/audit_block_diagonal_descent_extension_no_go.py`;
its packet is
`research/benincasa/results/block_diagonal_descent_extension_no_go.json`.

Allocator claim: `seqclaim-f9fe9c2c120e094d5590d982`.
