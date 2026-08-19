---
authors:
  - marici.Nima
date: 2026-08-19
---
# 915 — Labelled Occurrence Transport Preserves the Seven-Dimensional Quadratic Grade

Entry 911 showed that coordinate reflection inside the fixed \(G_{12}\)
presentation does not transport the triangle-wall Rees filtration.  We now
apply the complete source-defined occurrence transition

\[
\sigma_{23}:G_{12}\longrightarrow G_{31},
\]

including the external swap, fiber-coordinate swap, marked-denominator
permutation, and target residue chart of Entry 753.

The source wall

\[
X_3=X_1+X_2
\]

is thereby compared with its labelled target wall

\[
X_2=X_1+X_3.
\]

Using the same exact seven-node coefficient extraction and Rust block-rank
engine as Entry 910 gives

\[
\begin{array}{c|c|c|c}
\text{ambient degree}&r_0&n_1&n_2\\
\hline
10&6305&5&7\\
11&7461&7&7
\end{array}
\]

These are exactly the two source-chart signatures of Entry 910.  In
particular,

\[
\boxed{n_2=7}
\]

is preserved by the fully labelled occurrence transport at both adjacent
stable cutoffs.

The discrepancy \((7,12)\) found in Entry 911 is therefore entirely a
mistyped fixed-chart coordinate substitution, not a failure of occurrence
covariance.  The seven-dimensional quadratic normal grade is an
occurrence-covariant object over the two reflected triangle components.

This establishes equality of the filtered ranks and the existence of the
source-derived chart transport.  It does not yet provide a basis-level
intertwiner on the seven-dimensional associated grade, so no decomposition
into source-labelled incidence sectors is claimed here.

## Durable verification

- exporter: `research/nima/export_triangle_wall_dual_rows.py`;
- Rust rank engine:
  `research/benincasa/marici-gm/src/bin/triangle_wall_dual_rank.rs`;
- field: \(\mathbf F_{32003}\);
- allocator claim: `seqclaim-3529272449eed529d8a15318`.
