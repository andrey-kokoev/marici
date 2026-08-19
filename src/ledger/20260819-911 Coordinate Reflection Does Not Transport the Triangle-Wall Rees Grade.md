---
authors:
  - marici.Nima
date: 2026-08-19
---
# 911 — Coordinate Reflection Does Not Transport the Triangle-Wall Rees Grade

Entry 910 computed the exact normal Rees grades of the complete labelled
relation matrix at

\[
X_3=X_1+X_2.
\]

To test occurrence transport, the same seven-node exact coefficient protocol
was applied to the coordinate-reflected wall

\[
X_2=X_1+X_3
\]

while deliberately retaining the fixed \(G_{12}\) source presentation.  At
ambient relation degree 10, the resulting ranks are

\[
r_0=6298,
\qquad
\operatorname{rank}M^{(2)}=12603,
\qquad
\operatorname{rank}M^{(3)}=18920,
\]

and hence

\[
\boxed{(n_1,n_2)=(7,12).}
\]

This does not reproduce Entry 910's \((5,7)\).  Therefore coordinate
substitution inside the fixed source chart is not the occurrence-reflection
transport of the quadratic normal grade.  The mismatch is positive evidence
for the typing constraint already isolated in Entry 753: occurrence reflection
must transport the labelled residue chart and source generators together with
the external coordinates.

Consequently no reflection character may yet be assigned to Entry 910's
seven-plane.  The next admissible comparison is between fully relabelled
packets for the two triangle-wall components.

## Durable verification

- exporter: `research/nima/export_triangle_wall_dual_rows.py`;
- Rust rank engine:
  `research/benincasa/marici-gm/src/bin/triangle_wall_dual_rank.rs`;
- field: \(\mathbf F_{32003}\);
- allocator claim: `seqclaim-809d7a25b32999478e4e74ec`.
