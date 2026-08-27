# The Source-Evaluation Square Commutes but Unilateral Tail Propagation Leaves a Seam Cocycle

## The square before tail propagation

For a real Fourier-fixed theta forcing `f`, source evaluation is covariant:

\[
B_f^\times(\mathcal F'\nu)
=
\overline{B_f^\times(\nu)}
\]

with the appropriate conjugate reciprocal transport.  Thus the Euler-current
to scalar-control square closes before any tail boundary condition is chosen.

## Two inequivalent tail routes

On the positive scale chart define the outgoing tail

\[
G_z(q)=e^{-zq}\int_q^\infty f(v)e^{zv}\,dv,
\qquad
(\partial_q+z)G_z=-f.
\]

Its seam value is

\[
A(z)=G_z(0)=\int_0^\infty f(v)e^{zv}\,dv.
\]

There are now two paths to a reciprocal seam value.

1. Transport the already constructed tail by conjugate reflection.  Its seam
   value is `conjugate(A(z))`.
2. Reverse the centered spectral parameter first and reconstruct the native
   reciprocal outgoing tail.  Its seam value is `A(-conjugate(z))`.

Their mate-square residual is

\[
C_f(z)
=
A(-\overline z)-\overline{A(z)}.
\]

For real `f`, this is

\[
C_f(z)
=
\int_0^\infty
f(q)\left(e^{-\overline zq}-e^{\overline zq}\right)dq.
\]

It is generally nonzero.  The two routes agree only after an additional
bilateral or modular endpoint constructor supplies this difference.

## Smallest exact hostile

Take `f(q)=exp(-alpha q)` with positive `alpha`.  Then

\[
A(z)=\frac1{\alpha-z}
\]

and

\[
C_f(z)
=
\frac1{\alpha+\overline z}
-
\frac1{\alpha-\overline z}
=
\frac{-2\overline z}{\alpha^2-\overline z^2}.
\]

This residual is nonzero for generic `z`, including generic nonzero points on
the critical seam.  Consequently neither half-density centering nor
conjugate reflection closes the tail mate square.

## Correct zero condition

For an even bilateral source, the completed scalar readout has the form

\[
X(z)=A(z)+A(-z)
\]

up to the already retained completion units and endpoint terms.  Therefore a
zero gives the anti-diagonal trace relation

\[
A(-z)=-A(z),
\]

not two independent zero-trace conditions.  This corrects the earlier
one-sided zero-to-state slogan.  The zero-state belongs to a relative
two-endpoint domain whose trace lies in the anti-diagonal kernel of
augmentation.

The anti-diagonal relation makes the oriented endpoint norm difference
vanish, but it does not cancel `C_f(z)`: the latter compares transport of a
chosen unilateral tail with reconstruction of the reciprocal unilateral
tail.

## Interpretation

The shared augmentation port has two jobs:

1. impose the anti-diagonal completed zero condition;
2. carry the moving-endpoint cocycle between transported and reconstructed
   tails.

The first is now exact.  The second remains the live obstruction.  It must be
supplied by bilateral theta/Poisson sewing or by the declared primitive,
square, and archimedean boundary packet.  Defining it as the antiderivative of
the observed residual would be circular.

## Result

The Fourier–Tate mate square closes through source evaluation but fails after
unilateral tail propagation by the explicit seam cocycle `C_f(z)`.  This is
the first typed residual of the corrected multi-tower correspondence.  The
next theorem must derive `C_f` as the boundary of an independently constructed
modular sewing cell, at every finite cutoff, or the conservation route closes.

