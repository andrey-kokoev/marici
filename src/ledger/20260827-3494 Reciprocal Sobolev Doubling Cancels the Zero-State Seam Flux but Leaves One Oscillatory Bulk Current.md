# Reciprocal Sobolev Doubling Cancels the Zero-State Seam Flux but Leaves One Oscillatory Bulk Current

The reciprocal completed tails satisfy

\[
(\partial_q+z)G_+=-f,
\qquad
(-\partial_q+z)G_-=f.
\]

A completed scalar zero imposes

\[
G_-(0)=-G_+(0),
\]

so their oppositely oriented seam norms cancel exactly. The summed Green
identity nevertheless retains

\[
2\Re(z)(\|G_+\|^2+\|G_-\|^2)
=2\Re\langle f,G_--G_+\rangle.
\]

Before aggregation, the surviving current is

\[
-4\int_{q<v}f(q)f(v)
\sinh(\Re(z)(v-q))
\cos(\Im(z)(v-q))\,dq\,dv.
\]

Thus completion and seam closure are no longer the obstruction. All remaining
zero-confinement content lies in one theta-specific oscillatory bulk current.

Research packet:
`research/grothendieck/reciprocal-sobolev-doubling-cancels-the-zero-state-seam-flux-but-leaves-one-oscillatory-bulk-current.md`

Checker:
`research/grothendieck/checkers/check_reciprocal_sobolev_bulk_current.py`

The checker passes 5/5 gates.
