# A Positive Seam-Matched Primitive Split

## Canonical bounded repair coordinate

Use the primitive radial variable

\[
y=e^{2u}.
\]

The bounded displacement from the seam is

\[
q(u)
=
\frac{1-e^{-2u}}2.
\]

It satisfies

\[
q(0)=0,
\qquad
q'(0)=1,
\qquad
0\le q(u)<\frac12.
\]

Unlike an arbitrary bump, \(q\) is a rational coordinate in the same radial
variable that defines the primitive polynomial--Gaussian profile.

Let

\[
\beta=\frac{\phi_1'(0)}{\phi_1(0)}
=
\frac52+\frac{4\pi}{2\pi-3}-2\pi.
\]

Elementary bounds on \(\pi\) give

\[
0<\beta<0.045.
\]

## Exact split

Define

\[
R(u)=\phi_1(u)\left(1-\beta q(u)\right),
\]

and, with \(\tau=\Phi-\phi_1\),

\[
E(u)=\tau(u)+\beta q(u)\phi_1(u).
\]

Then

\[
\Phi=R+E.
\]

Both pieces are positive because \(0\le\beta q<0.0225\).

Their seam derivatives vanish separately:

\[
R'(0)
=
\phi_1'(0)-\beta\phi_1(0)
=
0,
\]

and

\[
E'(0)
=
\tau'(0)+\beta\phi_1(0)
=
0.
\]

Thus the cancellation formerly spread between the primitive and the entire
higher-label tail has been internalized into a seam-matched positive
reference and a seam-matched positive remainder.

## Uniform remainder size

Using

\[
0<\tau<\delta\phi_1,
\qquad
\delta=0.006001,
\]

one gets

\[
\frac{E}{R}
<
\frac{\delta+\beta/2}{1-\beta/2}
<
0.0292.
\]

Hence

\[
0<E(u)<0.0292\,R(u)
\qquad
(u\ge0).
\]

The corrected reference retains more than \(97.08\%\) of the completed source
pointwise, while both reference and remainder have the correct first
seam-derivative type.

## Consequence for collision analysis

Replacing \(\phi_1+\tau\) by \(R+E\) improves the primitive perturbation
scheme in two ways:

1. the remainder remains uniformly small in value;
2. the leading \(x^{-2}\) seam-derivative asymptotic no longer requires a
   cancellation between reference and remainder.

The same absolute transform argument now localizes a full collision to a
\(2.92\%\) near-collision of the seam-matched reference coordinates. This is
a weaker compact-frequency percentage than \(0.6001\%\), but it has the
correct high-frequency type.

## Next rung

Evenness kills every odd derivative of \(\Phi\) at the seam. Matching only the
first derivative does not automatically match the third, fifth, and higher
odd jets. Repeated integration by parts can expose those channels at
successive orders.

The next audit is therefore exact:

\[
R'''(0)
\stackrel{?}{=}
0.
\]

If it is nonzero, construct the next bounded radial repair coordinate and
determine whether positivity and a useful remainder ratio survive. The
resulting sequence is a seam-jet repair tower, not an arbitrary asymptotic
expansion.

## Falsifier

The split fails if \(R\) or \(E\) becomes negative, if either first derivative
at the seam is nonzero, or if the displayed ratio reaches \(0.0292\).

A global collision proof still fails if it assumes first-jet matching implies
matching of the complete even seam germ.
