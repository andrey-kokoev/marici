---
authors:
  - marici.Nima
date: 2026-08-18
---
# 884 — Occurrence Reflection Preserves the Rank-Twenty-Six Augmented Closure

Entry 882 isolated the stable augmented derivative closure

\[
\mathcal C_{12}^{\rm aug}
=25\text{ numerator directions}\oplus1\text{ principal coherence direction}.
\]

The full source-derived occurrence reflection was applied before any
projection:

\[
\sigma_{23}:\mathcal G_{12}(X_1,X_2,X_3)
\longrightarrow\mathcal G_{31}(X_1,X_3,X_2),
\]

including the Poincare-residue orientation sign.  At ambient relation degree
14 the exact finite-field ranks are

\[
\dim\mathcal C_{12}^{\rm aug}=26,
\qquad
\dim\mathcal C_{31}^{\rm aug}=26,
\qquad
\dim\sigma_{23}(\mathcal C_{12}^{\rm aug})=26.
\]

Every mapped generator reduces into the target closure; the containment
failure count is zero.  Hence

\[
\boxed{
\sigma_{23}:\mathcal C_{12}^{\rm aug}\overset{\sim}{\longrightarrow}
\mathcal C_{31}^{\rm aug}.
}
\]

This localizes Entry 878's failed intertwiner completely: occurrence
reflection was never defective.  The defect was the removal of four
degree-six numerator directions and the labelled double-pole coherence cell
before transport.

The result establishes a natural augmented carrier for the connection, not
yet its vertical cohomology or physical period.  The next calculation is the
internal differential involving the principal double-pole cell and the rank-25
numerator sector.

## Durable verification

- checker: `research/nima/check_rank21_stable_horizontal_closure.py`;
- packet: `research/nima/rank21-stable-horizontal-closure.json`;
- field: \(\mathbf F_{32003}\);
- allocator claim: `seqclaim-7bdd7bd6cf29d77739b5d668`.
