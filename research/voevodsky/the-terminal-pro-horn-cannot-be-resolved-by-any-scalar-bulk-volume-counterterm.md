# The terminal pro-horn cannot be resolved by any scalar bulk-volume counterterm

Let

\[
B(m)=\int_{\mathbb R}|m(t)|^2dt,
\qquad
A_\gamma(m)=|m(\gamma)|^2+|m(-\gamma)|^2.
\]

The ordinary geometric subtraction in the terminal `6 -> 7` slab is a scalar
multiple of `B`, whereas the hostile rank-two rotor grows with coefficient
`A_gamma`.  These quadratic forms are not proportional on the
Mellin--Schwartz observer core.

For `gamma != 0`, take

\[
f(t)=e^{-t^2},\qquad g(t)=(t^2-\gamma^2)e^{-t^2}.
\]

Then `B(f),B(g)>0`, `A_gamma(f)>0`, and `A_gamma(g)=0`.  Rescaling `f` and `g`
to have equal bulk norm proves that no observer-independent scalar `c` can
satisfy

\[
A_\gamma(m)=c B(m)
\]

for all observers.  For `gamma=0`, the same argument uses
`g(t)=t e^{-t^2}`.  Consequently no choice of coefficient multiplying the
existing Plancherel-volume row can cancel the terminal atomic growth for all
source observers.

The executable exact fixture

`checkers/check_bulk_volume_cannot_cancel_terminal_atomic_rotor.py`

verifies the instance `gamma=1` symbolically.

This closes one proposed resolution route negatively.  A successful terminal
filler must instead provide either:

1. a crossing-specific finite-rank geometric/index row carrying the same
   point-evaluation functional `A_gamma`; or
2. a source-derived common density normalization applied compatibly to both
   opposite edges, rather than an ad hoc rescaling of the spectral face.

The result does not prove that either remaining mechanism exists.
