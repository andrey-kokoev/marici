# On a rank-one tail module, linear boundary rows are syzygies or new boundary conditions

## Terminal parametrization

After decay at infinity and diagonal control sewing, the source-tail solution
module is a line. Write its amplitude as `c`. Its terminal state is

\[
v_s(c)=\bigl(G_s(0),c\bigr)=\bigl(F(s)c,c\bigr).
\]

The Evans row is projection onto the first coordinate. A zero-state with
`c` nonzero therefore satisfies `F(s)=0`.

## Classification of linear terminal rows

Every complex-linear terminal row has the form

\[
L_s(G(0),c)=\alpha(s)G(0)+\beta(s)c.
\]

On the constructible line,

\[
L_sv_s(c)=c\bigl(\alpha(s)F(s)+\beta(s)\bigr).
\]

There are only three logically distinct cases.

### Universal source identity

If `L_s v_s(c)=0` for every amplitude and every parameter in an open domain,
then

\[
\alpha(s)F(s)+\beta(s)=0.
\]

The row is a syzygy of the already constructed terminal graph. It does not
shrink the constructible module.

### Evans-derived row

If `beta=0`, then `L_s` is a multiple of the Evans row. It vanishes whenever
`F(s)=0` and adds no exclusion force.

### Independent boundary condition

At an Evans zero, a row with `beta(s)` nonzero gives

\[
L_sv_s(c)=\beta(s)c.
\]

Requiring it to vanish excludes every nonzero amplitude. But this is a new
boundary condition. It cannot be inferred from the tail equation or the Evans
condition; its source authority and compatibility must be derived separately.

## Exact hostile

Take `F=0`, `c=1`, and the terminal vector `(0,1)`. Every Evans-derived row
`alpha G(0)` vanishes. The identity observer sees the state perfectly. The row
`c=0` excludes it, but only by declaring a second endpoint condition.

The checker also verifies that the apparent row

\[
G(0)-F(s)c=0
\]

is a universal graph syzygy and is identically zero on every constructible
state, including every zero-state.

## Consequence

The search for more linear primitive, square, seam, or archimedean endpoint
ports is exhausted unless one of them is independently proved to be an
additional boundary condition on zero-states. Merely rewriting the terminal
graph or observing it more faithfully cannot orient `F(s)`.

The surviving possibility is nonlinear in the state: a bilinear Green,
Wronskian, or Clifford current whose integrated identity couples
`2 Re(s-1/2)` to a faithful nonnegative full-state energy. Such a current is
not another terminal observer. Its force comes from a conservation law and
from independently derived endpoint flux cancellation.

## Next falsifier

For every proposed completed current `J`, restrict its endpoint contribution
to the rank-one constructible line and compute its coefficient `j(s)`.

- If `j(s)` is identically zero by the terminal graph relation, the current is
  a syzygy.
- If `j(s)` is divisible by `F(s)` for a source-derived reason, it vanishes at
  zeros but supplies no transverse constraint by itself.
- If `j(s)` is not Evans-derived and zero-states must make it vanish, its
  boundary authority is the real theorem and must be exposed explicitly.

This is the appropriate typed audit for the declared primitive, square, seam,
and archimedean currents.
