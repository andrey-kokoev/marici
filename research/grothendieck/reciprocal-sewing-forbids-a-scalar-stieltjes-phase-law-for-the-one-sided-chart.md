# Reciprocal sewing forbids a scalar Stieltjes phase law for the one-sided chart

## The tempting phase mechanism

After the moving-incidence audit, the scalar zero condition is

\[
K(-z)=-K(z),
\qquad
K(z)=\int_0^\infty k(u)e^{zu}\,du.
\]

A natural shortcut would be to prove that \(K\) is a Stieltjes or Pick
function with a source-positive representing measure. Such a representation
would constrain its phase and might prevent the two one-sided charts from
becoming opposite away from the reciprocal seam.

## Sewing-point obstruction

The completed Haar-deficit kernel satisfies

\[
k(-u)=k(u).
\]

It is smooth at the sewing point, so

\[
k'(0)=0.
\]

It is also strictly positive, nonconstant, and tends to zero as
\(u\to+\infty\).

Suppose that the raw one-sided chart had a positive Stieltjes representation

\[
K(z)=\int_0^\infty\frac{d\nu(a)}{a-z},
\qquad d\nu(a)\geq0,
\]

in a domain where Laplace inversion is valid. Then its inverse Laplace kernel
would be

\[
k(u)=\int_0^\infty e^{-au}\,d\nu(a).
\]

Hence \(k\) would be completely monotone. In particular,

\[
k'(0+)=-\int_0^\infty a\,d\nu(a).
\]

The left side is zero. Positivity forces the representing measure to be
supported at \(a=0\), making \(k\) constant. This contradicts its decay.
If the first moment is infinite, the right derivative is negative infinite,
which is also incompatible with smooth reciprocal sewing.

Therefore the raw one-sided chart admits no positive Stieltjes
representation of this kind.

## Scope

This no-go concerns \(K\) itself. It does not refute a Stieltjes
representation for a derived logarithmic derivative, curvature transform, or
order-two resolvent. Differentiation and quotient formation change the
inverse-Laplace kernel and may remove the sewing-point obstruction.

It does rule out the simplest scalar explanation of the cross-chart phase.
The phase law cannot come from placing each one-sided chart independently in
a positive scalar resolvent cone.

## Why a higher-rank comparison is forced

The zero slope at the seam is not accidental missing information. It is the
first coherence imposed by reciprocal evenization. A scalar order cone sees
that coherence as degeneracy. To retain orientation, the comparison must lift
at least to a state carrying complementary data, such as value and normal
current, before the two charts are compressed.

The moving-incidence Ward identity shows that the normal current contains the
weighted endpoint distribution. But its scalar Mellin transform is affine in
\(K\), so transforming that channel separately still adds no phase
information. The endpoint current must remain inside a matrix-valued Green or
Clifford pairing across the two charts.

Thus the next admissible target is not another scalar transform. It is a
source-derived cross-chart bilinear form whose two entries are complementary
under reciprocal sewing and whose scalar codiagonal is the completed Mellin
readout.

## Operator stimulus

The operator instructed us to continue through the obstacle. Testing the
most economical scalar phase law exposed why the apparent degeneracy occurs:
the reciprocal seam forces zero normal slope. The resulting failure points
directly to a higher-rank comparison rather than to a stronger scalar
positivity ansatz.
