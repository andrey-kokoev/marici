# The faithful theta packet is a Wick-rotated hyperbolic moment pair

## Positive half-source coordinates

Write

\[
z=s-\frac12,
\qquad
q=\frac12\log t,
\]

and define the positive density on the completed half-source

\[
\rho(q)=2e^{q/2}\Psi(e^{2q}),
\qquad q\geq0.
\]

Then the two reciprocal half-Mellin channels are

\[
I_+(z)=\int_0^\infty\rho(q)e^{zq}\,dq,
\qquad
I_-(z)=\int_0^\infty\rho(q)e^{-zq}\,dq.
\]

Their symmetric and antisymmetric coordinates are

\[
M(z)=\frac{I_+(z)+I_-(z)}2
=\int_0^\infty\rho(q)\cosh(zq)\,dq,
\]

\[
N(z)=\frac{I_+(z)-I_-(z)}2
=\int_0^\infty\rho(q)\sinh(zq)\,dq.
\]

With

\[
P(z)=\frac{z^2-1/4}{2},
\]

the faithful coordinates from the preceding packet become

\[
S(z)=\frac12+2P(z)M(z),
\qquad
A(z)=2P(z)N(z).
\]

Thus the scalar readout and its discarded residual are the symmetric and
antisymmetric projections of one positive hyperbolic moment pair.

## The exact Lorentz invariant

The pair has the source identity

\[
M(z)^2-N(z)^2=I_+(z)I_-(z).
\]

Expanding the product gives

\[
M(z)^2-N(z)^2
=\int_0^\infty\!\int_0^\infty
\rho(q)\rho(r)\cosh(z(q-r))\,dq\,dr.
\]

For real (z), this quantity is strictly positive. The reciprocal channels
are then light-cone coordinates, while (M) and (N) are the corresponding
time-like and space-like coordinates. This is a source-derived hyperbolic
geometry, not an analogy imposed after taking the scalar readout.

## The quarter-turn at the critical seam

On the critical line (z=i\tau),

\[
M(i\tau)=\int_0^\infty\rho(q)\cos(\tau q)\,dq,
\]

\[
-iN(i\tau)=\int_0^\infty\rho(q)\sin(\tau q)\,dq.
\]

Both coordinates are real, and the Lorentz invariant rotates into the
Euclidean Fourier norm

\[
M(i\tau)^2-N(i\tau)^2
=M(i\tau)^2+[-iN(i\tau)]^2
=|I_+(i\tau)|^2.
\]

This makes the operator's proposed ninety-degree rotation literal. The two
open reciprocal sectors use boost coordinates; the seam uses the two Fourier
quadratures. The circle seen after correcting the plotting metric is the
level set of the half-Mellin amplitude norm in the plane with coordinates

\[
\bigl(M(i\tau),-iN(i\tau)\bigr).
\]

Its radius is not generally constant as \(\tau\) varies. What is canonical is
the Euclidean norm at each seam point, not one fixed global circle.

## The zero residual is a projective rapidity

Where \(I_++I_-\neq0\), define the projective comparison

\[
r(z)=\frac{I_+(z)-I_-(z)}{I_+(z)+I_-(z)}=\frac{N(z)}{M(z)}.
\]

Equivalently, after choosing a local logarithm,

\[
\chi(z)=\frac12\log\frac{I_+(z)}{I_-(z)},
\qquad
r(z)=\tanh\chi(z).
\]

At a scalar zero, \(2PM=-1/2\), so the surviving faithful coordinate is

\[
A(z)=-\frac12r(z)=-\frac12\tanh\chi(z).
\]

The two cancelled sector amplitudes are consequently

\[
U=-\frac14(1+r),
\qquad
V=-\frac14(1-r).
\]

Thus the quarter split and the antisymmetric residual are not separate
facts. They are the affine and projective parts of the same reciprocal
two-channel packet. For real \(z\), positivity of the half-density gives

\[
|r(z)|<1,
\]

so a hypothetical real-axis zero would have \(|A|<1/2\). On the critical
seam, reciprocal conjugation makes \(I_+/I_-\) unimodular, hence \(\chi\) and
\(A\) are purely imaginary. The Wick rotation therefore acts simultaneously
on the ambient moment metric and on the zero fiber's rapidity coordinate.

## What this explains and what it does not

The critical seam is special before any zero is inspected: it is where the
hyperbolic reciprocal comparison becomes an ordinary two-quadrature Fourier
comparison. A general point \(z=a+i\tau\) combines a boost by \(a\) with a
rotation by \(\tau\). In these coordinates RH asks for the source curve to
meet

\[
S(z)=0
\]

only when the boost component vanishes.

Positive \(\rho\) alone does not imply that confinement. Hostile positive or
Fourier-fixed carriers can preserve this kinematic Wick rotation and still
have off-seam zeros. Therefore this packet explains the geometry and the
meaning of the seam, but it does not prove RH.

The next hard theorem must use a property specific to the minimal theta
density and constrain the affine cancellation

\[
\frac12+2P(z)M(z)=0
\]

under nonzero boost. The smallest honest falsifier is another positive
half-density with the same reciprocal construction for which this equation
has a solution with \(\Re z\neq0\). Such witnesses test the missing dynamical
law without disputing the exact hyperbolic-to-Fourier reduction.

## Operator stimulus

This reduction was prompted by the operator's repeated proposal that the two
half-planes are shadows of two genuinely distinct sectors and that the
critical line is a ninety-degree change of comparison geometry. The faithful
\((S,A)\) chart made the statement calculable: centering at \(1/2\) exposes
the reciprocal exponentials as light-cone components, and restriction to the
seam turns their cosh/sinh coordinates into cosine/sine quadratures.
