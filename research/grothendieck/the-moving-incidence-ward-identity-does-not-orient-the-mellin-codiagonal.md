# The moving-incidence Ward identity does not orient the Mellin codiagonal

## From the incidence connection to the theta current

Write

\[
A(u)=\int_0^\infty
\{re^{-u}\}\,r e^{-\pi r^2}\,dr
\]

and

\[
k(u)=8\pi e^{u/2}A(u).
\]

The moving-incidence connection gives

\[
\partial_u\{re^{-u}\}
=-e^{-u}r
+e^u\sum_{n\geq1}n\delta(r-ne^u).
\]

Since

\[
\int_0^\infty r^2e^{-\pi r^2}\,dr=\frac1{4\pi},
\]

we obtain

\[
A'(u)
=-\frac{e^{-u}}{4\pi}
+e^{2u}\sum_{n\geq1}n^2e^{-\pi n^2e^{2u}}.
\]

Therefore

\[
k'(u)=\frac12k(u)+B(u),
\]

where the complete endpoint-current readout is

\[
B(u)
=-2e^{-u/2}
+8\pi e^{5u/2}
\sum_{n\geq1}n^2e^{-\pi n^2e^{2u}}.
\]

This is a genuine source-derived Ward identity. It retains the moving integer
endpoints and is not inferred from the zero set.

## One-sided Mellin charts

Define, initially in the common convergence strip,

\[
K(z)=\int_0^\infty k(u)e^{zu}\,du.
\]

Integration by parts gives

\[
\int_0^\infty B(u)e^{zu}\,du
=-k(0)-(z+1/2)K(z).
\]

The reciprocal completion does not use either one-sided chart alone. Its
scalar readout is the codiagonal

\[
F(z)=\frac12\bigl(K(z)+K(-z)\bigr)
=\int_0^\infty k(u)\cosh(zu)\,du.
\]

Thus a scalar zero is exactly the cross-chart cancellation

\[
K(-z)=-K(z).
\]

Both one-sided Ward identities remain valid when this occurs. Substituting
the cancellation creates no contradiction, no missing endpoint, and no
failure of the moving-incidence connection.

## The no-go result

The incidence connection is faithful upstream but not divisor-confining
downstream. It distinguishes the canonical integer source from the positive
denominator-three hostile, yet it does not orient the codiagonal projection
of the authentic source.

This failure is unavoidable at the present rung. The canonical source itself
has critical-line zeros, so source horizontality cannot forbid scalar
cancellation in general. Fourier reciprocity makes the two charts into a
matched pair but permits them to be opposite after scalar projection.

Consequently, no argument using only

- source provenance,
- the moving-incidence connection,
- its scalar Ward identity, and
- reciprocal evenization

can distinguish an allowed seam cancellation from a hypothetical off-seam
cancellation.

## Required next comparison channel

The missing object must compare the phases or orientations of \(K(z)\) and
\(K(-z)\) before their codiagonal compression. It must be derived from the
source and depend on the half-plane type. Merely retaining both values is not
enough; the comparison needs a conservation, order, or positivity law whose
failure is forced when the two charts become opposite away from the seam.

In the multi-tower language, the input-incidence tower is now closed. The
unresolved cell belongs to the comparison tower between the two completed
output charts. This is the precise location where a Green, Clifford, or
determinant current would have to enter.

## Operator stimulus

The operator directed us to continue after the hostile was rejected. Following
the connection through the Mellin transform exposed the obstruction: the
source remains meaningful while its scalar codiagonal loses one grade of
meaning. The missing structure is therefore not another source label but a
typed relation between the two one-sided completed charts.
