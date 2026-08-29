# The Canonical Theta Route Wronskian Measures Interference Crossing

## Source-framed routes

Let \(\Phi(u)\) be the completed even theta source on the real logarithmic
line. Split its transform at the source-fixed seam \(u=0\):

\[
A(z)
=
\int_0^\infty
\Phi(u)e^{zu}\,du,
\]

\[
B(z)
=
\int_0^\infty
\Phi(u)e^{-zu}\,du
=
A(-z).
\]

The completed scalar section is

\[
X(z)=A(z)+B(z).
\]

The two routes are defined before inspecting zeros. Their order is fixed by the
positive and negative logarithmic orientations, and \(z\) is the genuine
Mellin/dilation parameter. Thus differentiation with respect to \(z\) has
source authority.

## Framed Wronskian

Define

\[
\Omega(z)
=
A(z)B'(z)-B(z)A'(z).
\]

Under route exchange, \(\Omega\) changes sign. Under reciprocal parameter
reflection, it satisfies

\[
\Omega(-z)=\Omega(z).
\]

Reality of \(\Phi\) gives

\[
\Omega(\overline z)
=
\overline{\Omega(z)}.
\]

Thus \(\Omega\) is an even, real-entire framed crossing observable.

## Source integral

Differentiating the two routes gives

\[
A'(z)
=
\int_0^\infty
u\Phi(u)e^{zu}\,du,
\]

\[
B'(z)
=
-
\int_0^\infty
v\Phi(v)e^{-zv}\,dv.
\]

Therefore

\[
\Omega(z)
=
-
\int_0^\infty
\int_0^\infty
(u+v)
\Phi(u)\Phi(v)
e^{z(u-v)}
\,du\,dv.
\]

For real \(z\), a nonnegative nonzero source makes

\[
\Omega(z)<0.
\]

This is a genuine orientation on the real Mellin axis. At complex \(z\), the
oscillatory phase removes automatic sign control.

## Value at a scalar zero

Suppose

\[
X(z_0)=0.
\]

Then \(B(z_0)=-A(z_0)\), and hence

\[
\Omega(z_0)
=
A(z_0)X'(z_0).
\]

Consequently:

- if \(A(z_0)\neq0\) and the scalar zero is simple, then
  \(\Omega(z_0)\neq0\);
- if \(\Omega(z_0)=0\), then either both route amplitudes vanish or the
  scalar crossing is multiple.

The Wronskian therefore distinguishes a nondegenerate interference crossing
from route collapse or tangency without promoting the scalar zero to a full
kernel.

## Relation to the full character lift

The complete residue-character packet proves that the labelled arithmetic
state remains distinguishable at every finite cutoff. The Wronskian supplies
the next datum: orientation of the two-route scalar projection as the Mellin
parameter moves.

These are independent certificates:

- the character lift proves presence of the hidden packet;
- the Wronskian measures how its trivial-character projection crosses zero.

## No confinement yet

Reciprocal symmetry makes \(\Omega\) even, not seam-supported. Reality pairs
its values at conjugate points. Neither property forces a nondegenerate
crossing to occur on the imaginary \(z\)-axis.

A hostile self-dual carrier also admits the same half-line split and
Wronskian. Therefore the existence and nonvanishing of \(\Omega\) do not
imply RH.

The remaining source theorem must constrain the phase or character of
\(\Omega\) at a zero using genuinely arithmetic radial--angular coupling.

## Arithmetic lift target

The full framed crossing should refine to character components

\[
\Omega_\chi
=
A_\chi B_\chi'
-
B_\chi A_\chi',
\]

with conductor-compatible analysis and primitive/square boundary terms.

The first useful question is whether the trivial-character Wronskian is
determined by a cyclic product of nontrivial character routes. If so, a hostile
scalar divisor may fail that cycle even while preserving \(X(z)=X(-z)\).

## Falsifiers

The crossing programme fails if:

- route ordering is not source-fixed;
- differentiation depends on a fitted parameter chart;
- the Wronskian is unchanged under every hostile divisor-bearing
  modification;
- characterwise refinement leaves its phase unconstrained;
- completion destroys continuity of the route derivatives.

## Disposition

The canonical Wronskian is the correct lift of scalar darkness from a value to
an oriented crossing. It is fully source-derived and avoids fitted
kernelization.

Its sign is automatic only on the real axis, not on the RH seam. The next
advance must be an arithmetic cycle law for its complex phase.

