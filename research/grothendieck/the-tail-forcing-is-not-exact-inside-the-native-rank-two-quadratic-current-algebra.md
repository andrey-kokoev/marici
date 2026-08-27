# The tail forcing is not exact inside the native rank-two quadratic-current algebra

## Native real tail system

Consider the real form of the source tail equation

\[
G'=-sG-cf,
\qquad c'=0,
\]

where `s` is nonzero and the source `f` is not identically zero. The doubled
Green calculation leaves a forcing channel proportional to `fGc`. The first
closure question is whether that channel is already the derivative of a local
quadratic current built only from the native state variables `G` and `c`.

## Constant-coefficient quadratic no-go

Take the most general such current

\[
J=A G^2+B Gc+C c^2,
\]

with coefficients independent of `q`. Along the tail flow,

\[
J'
=-2AsG^2-(2Af+Bs)Gc-Bfc^2.
\]

To reproduce `2fGc` without additional bulk channels, the coefficients of
`G^2` and `c^2` must vanish. Since `s` is nonzero and `f` is nontrivial, this
forces

\[
A=0,
\qquad B=0.
\]

The remaining `Gc` coefficient is then zero, contradicting the required
coefficient `2f`. Hence no constant-coefficient quadratic current in the
native rank-two variables differentiates to the forcing channel alone.

The coefficient `C` is irrelevant because `c` is constant.

## Meaning of the obstruction

This is a finite algebraic obstruction, not a failure to guess the right
quadratic expression. The native tail block does not contain enough state to
make its forcing exact while leaving no residual bulk term.

A successful modular current must therefore use at least one of:

- an independent seam or boundary state;
- a source primitive whose derivative is `f`;
- explicitly `q`-dependent coefficients derived from modular geometry;
- a nonlocal integral current;
- cancellation against the reciprocal sheet before restricting to the native
  block.

The first three are legitimate only if derived before inspecting the desired
identity. The nonlocal antiderivative of the residual is formally available
for every source and has no explanatory force.

## Relation to the independent seam sector

The earlier completion obstruction showed that the seam cannot be recovered
boundedly from the retained tail. The present calculation supplies the local
algebraic counterpart: even before completion, the native tail variables do
not possess a quadratic primitive for the forcing channel.

Thus retaining the seam as an independent state is not merely a topological
convenience. It is a candidate minimal extension of the differential algebra
in which the forcing may become exact.

## Next construction

Adjoin one real seam coordinate `h` with a source-derived flow

\[
h'=aG+bc+df
\]

and repeat the quadratic-current coefficient audit in `(G,c,h)`. The goal is
not to fit `a,b,d`; they must be inherited from the actual moving-endpoint or
primitive-current equation. The exact question is whether that independently
derived extension makes `2fGc` exact without leaving a new indefinite bulk
term.

This is now the smallest live modular-current calculation.
