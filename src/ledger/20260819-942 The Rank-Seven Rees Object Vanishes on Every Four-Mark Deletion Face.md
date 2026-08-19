---
authors:
  - marici.Nima
date: 2026-08-19
---
# 942 — The Rank-Seven Rees Object Vanishes on Every Four-Mark Deletion Face

Entry 938 constructs the functorial exact-valuation-two object

\[
E_2(C)=
\frac{\ker\Lambda\cap\Lambda C}
     {\ker\Lambda\cap\Lambda^2C},
\qquad
\dim E_2(C)=7.
\]

To test whether this object is induced from a lower marked-incidence sector,
delete each marked-divisor relation family in turn:

\[
q_{g_1},\quad q_{g_2},\quad q_{g_3},\quad q_{g_{23}},\quad q_{g_{31}}.
\]

Each deletion is computed without choosing a seven-basis: move the selected
family to the final filtration step and evaluate \(E_2\) on the preceding
four-family Rees complex.

At ambient degree 10,

\[
\bigl(dim E_2(C_{\widehat g})\bigr)_{g}
=(0,0,0,0,0).
\]

The complete audit repeats at ambient degree 11:

\[
\boxed{
\bigl(dim E_2(C_{\widehat g})\bigr)_{g}
=(0,0,0,0,0).
}
\]

Restoring the fifth marked family gives rank seven in every ordering.  Hence

\[
\boxed{
E_2(C_{\rm full})\cong\mathbf F^7,
\qquad
E_2(C_{\widehat g})=0
\text{ for every codimension-one deletion face}.
}
\]

This makes the seven-dimensional sector a genuine five-mark interaction at
the deletion-face level.  It cannot be induced from any single four-mark
face.  The statement does not assert vanishing on every smaller subcomplex,
because the exact-valuation functor is not assumed monotone or exact under
further deletion.

The next canonical object is the total homotopy cofiber of the five deletion
maps.  If its exact-valuation-two part remains rank seven, the sector is the
top cross-effect of the marked incidence cube.

## Durable verification

- reorderable exporter:
  `research/nima/export_triangle_wall_dual_rows.py`;
- sparse Rees engine:
  `research/benincasa/marici-gm/src/bin/triangle_wall_dual_rank.rs`;
- packet: `research/nima/triangle-wall-dual-relation-rank.json`;
- field: \(\mathbf F_{32003}\);
- allocator claim: `seqclaim-d00d8589fb00b5901af17283`.
