# Doubled-tail forcing is the odd transform of a positive autocorrelation measure

## Question

The corrected doubled Green identity leaves one forcing integral.  Is that
term an arbitrary analytic remainder, or does it have a canonical positive
source measure?

## Expanding the half-tail difference

For the transported tails

\[
H_+(q,z)
=
\int_q^\infty f(v)e^{z(v-q)}\,dv,
\qquad
H_-(q,z)
=
\int_q^\infty f(v)e^{-z(v-q)}\,dv,
\]

their difference is

\[
H_+(q,z)-H_-(q,z)
=
2\int_q^\infty
f(v)\sinh(z(v-q))
\,dv.
\]

Therefore the complex forcing functional is

\[
\mathcal K(z)
=
\int_0^\infty
f(q)
\left(
H_+(q,z)-H_-(q,z)
\right)
\,dq
\]

and Fubini's theorem gives

\[
\mathcal K(z)
=
2
\int_{0\le q<v<\infty}
f(q)f(v)\sinh(z(v-q))
\,dq\,dv.
\]

## Positive autocorrelation measure

Define

\[
\rho(d)
=
2\int_0^\infty
f(q)f(q+d)
\,dq,
\qquad d\ge0.
\]

For the completed theta kernel, (f\ge0), so

\[
\rho(d)\ge0.
\]

Changing variables from ((q,v)) to ((q,d=v-q)) yields the exact
factorization

\[
\mathcal K(z)
=
\int_0^\infty
\rho(d)\sinh(zd)
\,dd.
\]

Thus the remaining doubled forcing is the odd Laplace transform of a
canonical positive autocorrelation measure.

## Real orientation

Write

\[
z=\sigma+it.
\]

Then

\[
\Re\mathcal K(\sigma+it)
=
\int_0^\infty
\rho(d)
\sinh(\sigma d)
\cos(td)
\,dd.
\]

The Green identity for a zero-state becomes

\[
\sigma
\int_0^\infty
\left(
|H_+|^2+|H_-|^2
\right)
\,dq
=
-\Re\mathcal K(z).
\]

Every off-seam zero must therefore satisfy

\[
\sigma\,\Re\mathcal K(z)<0.
\]

The inequality is strict because the bulk norm is positive for a nonzero
state.

## Exact zero-confinement target

A sufficient source theorem is now explicit:

for every zero-state candidate with \(\sigma\ne0\), prove

\[
\sigma
\int_0^\infty
\rho(d)
\sinh(\sigma d)
\cos(td)
\,dd
\ge0.
\]

That inequality contradicts the Green identity and confines zeros to the
seam.

It is important not to claim it merely from \(\rho\ge0\).  The cosine factor
oscillates, so positive measures can have either transform sign.  The missing
force must come from the special modular structure of the theta
autocorrelation or from the simultaneous zero constraint on the even
transform.

## Relation to the curvature programme

The order-two logarithmic curvature was previously expressed through a
positive squared-separation measure.  The present forcing uses the unsquared
separation autocorrelation measure and its odd transform.  They are two
moments of the same ordered source-pair geometry:

- even squared separation controls curvature;
- odd ordered separation controls sector flux.

This explains why the curvature and Green-current lanes repeatedly collapsed
onto the same obstruction.  They are different readouts of one positive
pair-source measure, with oscillatory orientation still missing.

## Falsifiers

The strongest local falsifier is a candidate zero constraint and a point
\(z=\sigma+it\) for which the theta autocorrelation gives

\[
\sigma\,\Re\mathcal K(z)<0.
\]

That sign is necessary for an off-seam zero and therefore does not itself
produce one; it shows only that the autocorrelation-orientation theorem cannot
exclude it there.

A source theorem based solely on positivity of \(\rho\) is rejected by any
positive finite atomic measure whose cosine transform changes sign.

## Result

The last forcing term is not arbitrary.  It is the odd transform of the
positive theta autocorrelation measure.  The remaining RH-bearing statement
is exactly an oscillatory orientation theorem for this measure under the
simultaneous theta-zero constraint.
