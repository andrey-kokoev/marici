# The moving-seam conservation law is maximally blind on the zero-state

## Source-derived seam flow

Let

\[
r_s(L)=f(L)e^{sL},
\]

and split the completed half-line transform at the moving cut `L`:

\[
T_s(L)=\int_L^\infty f(v)e^{sv}\,dv,
\qquad
B_s(L)=\int_0^L f(v)e^{sv}\,dv.
\]

These are the retained tail and the finite seam window. Their flows are exact:

\[
T_s'=-r_s,
\qquad
B_s'=r_s.
\]

Therefore

\[
T_s(L)+B_s(L)=F(s)
\]

is independent of the cut. This is the native moving-endpoint conservation
law; no auxiliary coordinate has been fitted.

## Zero-state geometry

At an Evans zero, `F(s)=0`. Hence for every cut,

\[
B_s(L)=-T_s(L).
\]

The complete seam trajectory lies in the anti-diagonal line

\[
\{(T,B):T+B=0\}.
\]

Its tangent is also anti-diagonal:

\[
(T_s',B_s')=(-r_s,r_s).
\]

Thus the conserved sum is not merely insufficiently conditioned on a
zero-state. It is identically blind to the whole zero-state trajectory and to
its motion.

## Common and relative channels

Introduce

\[
C_s=T_s+B_s,
\qquad
D_s=T_s-B_s.
\]

Then

\[
C_s'=0,
\qquad
D_s'=-2r_s.
\]

The common channel `C_s` is exactly the scalar completed transform. The
relative channel `D_s` retains the moving source incidence erased by scalar
completion. On a zero-state,

\[
C_s=0,
\qquad
D_s=2T_s=-2B_s,
\]

which is generally nonzero.

This is the smallest exact explanation of why seam retention alone did not
orient the zero problem: retaining `(T,B)` is faithful, but the known
conservation law acts only on its common-mode quotient.

## Quadratic consequence

The conserved quadratic quantity

\[
|C_s|^2=|T_s+B_s|^2
\]

also vanishes identically on a zero-state, even though the faithful seam
energy

\[
|T_s|^2+|B_s|^2
=\frac12\bigl(|C_s|^2+|D_s|^2\bigr)
\]

is strictly positive whenever the state is nonzero. Conservation of the
common mode therefore cannot be substituted for positivity of the full seam
state.

## Multi-tower interpretation

The first cross-tower coherence cell conserves the common scalar channel. The
zero-state lives entirely in the relative channel that this cell forgets.
Therefore the coherence cell itself needs a higher comparison:

- first cell: `T+B`, invariant under moving the cut;
- second cell: `T-B`, recording the oriented incidence across the cut;
- next coherence: a Green or Clifford relation coupling the relative channel
  to the direct--dual sheet exchange.

This is the requested additional comparison channel in exact source form. It
is a flux channel, not another copy of the scalar value.

## Falsifier for the next rung

Any proposed modular current that depends only on `C_s` is automatically zero
on every Evans zero and cannot distinguish the zero state from the zero
vector. A viable next current must depend faithfully on `D_s` or on an
equivalent oriented seam derivative.

The next calculation is to apply Fourier--Tate reciprocal sewing to the pair
`(C_s,D_s)` and determine whether it supplies a source-derived bilinear form
whose restriction to `C_s=0` is nondegenerate in `D_s`.
