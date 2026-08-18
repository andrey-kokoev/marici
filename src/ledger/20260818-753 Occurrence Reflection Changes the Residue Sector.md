---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 753 — Occurrence Reflection Changes the Residue Sector

## Gate after Entries 720 and 752

Entry 720 leaves a finite occurrence-reflection test: compare the rank-twenty-one
relative connection at \((X_1,X_2,X_3)=(2,3,4)\) with the reflected point
\((2,4,3)\). Before computing connection matrices, the source-labelled
residue divisor must be transported.

## Source permutation

Write the loop edges as

\[
(a,b,c)=(y_{23},y_{31},y_{12}).
\]

The site transposition \(\sigma_{23}\) acts by

\[
X_2\leftrightarrow X_3,\qquad
y_{12}\leftrightarrow y_{31},\qquad
y_{23}\mapsto y_{23}.
\]

Applying this to the source definitions of all denominators gives

\[
\begin{aligned}
q_{g_1}&\mapsto q_{g_1},&
q_{g_2}&\leftrightarrow q_{g_3},\\
q_{g_{12}}&\leftrightarrow q_{g_{31}},&
q_{g_{23}}&\mapsto q_{g_{23}},
\end{aligned}
\]

and, crucially,

\[
\boxed{
q_{\mathcal G_{12}}\longleftrightarrow q_{\mathcal G_{31}},
\qquad
q_{\mathcal G_{23}}\longmapsto q_{\mathcal G_{23}}.
}
\]

Thus the two physical \(q_{\mathcal G_{12}}\)-summands map to

\[
\{q_{g_1},q_{g_3},q_{g_2},q_{\mathcal G_{31}},q_{g_{23}}\}
\]

and

\[
\{q_{g_1},q_{g_3},q_{g_2},q_{\mathcal G_{31}},q_{g_{12}}\}.
\]

They do not map to the original \(q_{\mathcal G_{12}}\)-residue union.

## Narrow conclusion

\[
\boxed{
\text{kinematic swapping inside the fixed }q_{\mathcal G_{12}}\text{ chart
does not type the occurrence-reflection intertwiner.}
}
\]

The comparison demanded by Entry 720 must first construct a residue-chart
transition

\[
M^{(G_{12})}_{(2,3,4)}
\longrightarrow
M^{(G_{31})}_{(2,4,3)}
\]

with the displayed denominator permutation, Poincare-residue orientation,
and retained-pivot basis transport. Only then can connection matrices be
tested for intertwining or reflection eigensectors be formed.

This is a correction of the proposed implementation route, not a rejection
of occurrence symmetry. It also does not reopen \(\mathcal Q\): the issue
is ordinary labelled global gluing, exactly the frontier of Entry 752.

## Classification

- carrier: unchanged cyclic energy/Cut incidence carrier;
- coefficient datum: transition between labelled residue charts;
- new carrier datum: none;
- present obstruction: the required chart transition has not yet been
  constructed.

## Evidence

- frozen source denominator definition;
- Entry 590's labelled physical residue pair;
- Entries 719--720 and 752;
- exact Rust certificate
  `research/benincasa/marici-gm/src/bin/occurrence_reflection_residue_sector.rs`;
- machine-readable packet
  `research/benincasa/marici-gm/occurrence-reflection-residue-sector.json`;
- allocator claim `seqclaim-051d2b910f1645c04f961d2e`.
- epistemic event
  `ev-000000000367-0b6e3565-41b0-4ea2-b8e6-4b613fcc0603`.

## Next falsifier

Construct the \(q_{\mathcal G_{31}}\)-residue retained-pivot presentation
directly from the full three-variable source, including its residue
orientation. Transport every labelled generator under \(\sigma_{23}\),
reduce in the target presentation, and test the two Gauss--Manin
intertwining equations. Do not identify the two residue charts by an
unlabelled rank count.
