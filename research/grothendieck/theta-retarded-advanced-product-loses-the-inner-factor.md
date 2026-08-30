# Theta retarded--advanced product loses the inner factor

## Bounded question

Are the reciprocal theta/Tate sectors retarded and advanced Hardy factors
whose product determines the zero-bearing causal factor?

## Native Hardy pair

For a one-sided completed source \(f\), define

\[
F_+(z)=\int_0^\infty f(q)e^{izq}\,dq
\]

in its retarded half-plane. The reciprocal real structure supplies

\[
F_-(z)=\overline{F_+(\bar z)}
\]

in the opposite half-plane, with the precise sign convention fixed by the
Fourier--Tate normalization.

On the real boundary,

\[
F_+(x)F_-(x)=|F_+(x)|^2.
\]

Thus the two reciprocal sectors are a genuine retarded--advanced pair for the
one-sided cross-transfer channel.

## Two-sided correlation

The inverse Fourier transform of the boundary product is the autocorrelation

\[
C(t)=
\int_0^\infty
f(q+t)\overline{f(q)}\,dq
\]

for positive \(t\), with the reflected expression for negative \(t\).
Therefore the product is necessarily two-sided even though \(F_+\) itself is
causal. This closes the inference from a positive boundary density to a
one-sided delay kernel.

## Inner-factor ambiguity

Let \(I\) be any upper-half-plane inner function. Its boundary values satisfy

\[
|I(x)|=1
\]

almost everywhere. Define

\[
\widetilde F_+(z)=I(z)F_+(z)
\]

and use the reciprocal lower-half-plane partner. Then

\[
\widetilde F_+(x)\widetilde F_-(x)
=
F_+(x)F_-(x).
\]

The full exterior delay density and its two-sided correlation are unchanged.
But a Blaschke factor

\[
I_a(z)=\frac{z-a}{z-\bar a},
\qquad
\operatorname{Im}a>0,
\]

inserts a zero at \(a\) into the retarded factor while preserving its Hardy
typing and the boundary product.

Hence product data do not determine the zero divisor, causal phase, or
source orientation of either factor.

## What source sewing does establish

The original theta integral fixes one particular \(F_+\) before the product is
formed. Reciprocal sewing then fixes its advanced partner. This provides
provenance of the factorization, but not a zero-free theorem.

To exclude hostile inner factors, the source must prove one of the following:

1. \(F_+\) is outer in its Hardy class;
2. every admitted inner factor is a nowhere-zero constant;
3. labelled primitive, square, and archimedean residues determine the complete
   inner divisor;
4. a constructor law forbids modification of the retarded factor while
   preserving all boundary data.

Proving outerness by assuming zero-freeness is circular. It must follow from
the theta/Tate constructor repertoire.

## Residue and completion scope

Primitive, prime-square, archimedean, and pole residues can constrain the
admissible factor if they are retained as labelled boundary coordinates.
Their scalar sum or exterior density cannot do so: an inner factor is
invisible to boundary modulus.

Completion support also does not resolve the ambiguity. Multiplication by an
inner function is an isometry of the Hardy space, so norm completion preserves
the hostile factor unless the source-labelled boundary channels reject it.

## Relation to the Hermite form

The Hermite form of the bordered numerator retains divisor information that
the retarded--advanced product loses. A theta-labelled Gram factorization of
that form would therefore be stronger than positivity of the exterior delay
density. It must retain phase-sensitive cross-label data rather than only
autocorrelation.

## Result

The reciprocal theta/Tate sectors are naturally retarded and advanced factors
of the cross-transfer autocorrelation. Their product is not faithful to either
factor's zeros. The eighth rotation therefore reaches a canonical
phase-retrieval boundary: RH-bearing information lies in source authority over
the inner factor, not in the positive two-sided density.

## Sharp falsifier

Choose any nonconstant upper-half-plane Blaschke factor \(I_a\). The pair

\[
(I_aF_+,\ I_a^\#F_-)
\]

has the same boundary product and Hardy support typing but a changed retarded
zero divisor. Any proposed causal-kernel theorem that cannot reject this pair
from labelled source data supplies no zero-confinement information.
