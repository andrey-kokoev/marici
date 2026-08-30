# Theta native first-order bulk exactly controls the endpoint

## Exact identity

The source flow gives

\[
 G+f=-\partial_qG+(1-s)G.
\]

Write

\[
 1-s=a+ib
\]

and gauge away the imaginary part by

\[
 G(q)=e^{ibq}h(q).
\]

Then

\[
 -\partial_qG+(1-s)G
 =e^{ibq}(-h'+ah).
\]

For `h` in `H1(0,infinity)` with `h(infinity)=0`, integration by parts gives

\[
 \boxed{
 \lVert G+f\rVert_2^2
 =\lVert h'\rVert_2^2
 +a^2\lVert h\rVert_2^2
 +a|h(0)|^2.}
\]

Indeed,

\[
 -2a\Re\int_0^\infty h'\overline h\,dq
 =a|h(0)|^2.
\]

## Critical-strip consequence

For `0<Re(s)<1`,

\[
 a=1-\Re(s)>0.
\]

Therefore

\[
 \boxed{
 |G(0)|^2
 \le\frac{1}{1-\Re(s)}\lVert G+f\rVert_2^2.}
\]

The bound is independent of `Im(s)`.  On every compact subset of the
critical strip bounded away from `Re(s)=1`, it is uniform.

## Meaning

The positive square already present in the native two-sheet Clark bulk is not
merely a formal Gram term.  It is exactly the graph energy of the scale-flow
operator and contains the endpoint trace with a positive coefficient.

Consequently a sequence cannot satisfy

\[
 \lVert G_X+f_X\rVert_2\longrightarrow0
\]

while retaining a nonzero endpoint `G_X(0)`, at any fixed `s` in the critical
strip.  The scalar zero boundary condition therefore survives completion in
this graph channel.

## Scope boundary

This does not prove RH.  It closes only the endpoint-continuity gate.  The
remaining global burden is still to prove that the complete doubled Green
identity has no undeclared typed residual and that its total endpoint flux
vanishes for the completed zero-state.

The estimate also degenerates as `Re(s)->1`.  That is the natural boundary of
this orientation of the first-order tail operator, not the RH seam.

## Durable correction chain

1. Bulk tail--seam `L2` energy alone does not control the endpoint.
2. The Clark `z`-derivative was not the justified repair.
3. The already present `q`-flow square `|G+f|^2` supplies the exact repair.

Thus the source did contain the necessary boundary regularity, but in the
operator direction rather than the spectral-parameter direction.
