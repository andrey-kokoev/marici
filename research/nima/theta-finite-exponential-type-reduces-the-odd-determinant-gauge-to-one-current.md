# Finite exponential type reduces the odd determinant gauge to one current

## Conditional reduction

The reflected denominator product

\[
F(z)=u(z)D_+(z)D_+(-z)
\]

is invariant under

\[
D_+(z)\longmapsto e^{g(z)}D_+(z)
\]

for every odd entire (g). Without a growth law this is an
infinite-dimensional frame gauge.

Suppose, however, that the admitted refactoring multiplier (e^g) is required
to have finite exponential type. Then (g) is a polynomial of degree at most
one. Since (g) is odd,

\[
g(z)=az
\]

for one constant (a).

Thus the source growth class reduces the infinite odd gauge to a
one-parameter linear gauge.

## Proof

If (g) is entire and (e^g) has finite order, standard entire-function
growth theory forces (g) to be a polynomial. The order of (e^g) is the
degree of that polynomial. Finite exponential type has order at most one, so
(g) is affine. Oddness removes the constant term.

The conclusion is conditional on the multiplier itself belonging to the
admitted finite-type class. A scalar product identity alone does not establish
that condition.

## The one-jet frame coordinate

Under the remaining transformation

\[
\widetilde D_+(z)=e^{az}D_+(z),
\]

the centered logarithmic derivative changes by exactly (a):

\[
\frac{\widetilde D_+'(0)}{\widetilde D_+(0)}
=
\frac{D_+'(0)}{D_+(0)}+a.
\]

Therefore one source-derived first jet fixes the entire residual gauge.
Basepoint value alone cannot do so.

For cutoffs (X\subset Y), naturality requires

\[
a_Y-a_X
\]

to equal the first-jet contribution of the newly added labelled source block.
If that increment is not derived, linear frame drift can accumulate even when
every reflected product is exact.

## Arithmetic interpretation

The primitive current is the natural candidate for this missing first-jet
coordinate. Its role would not be to provide a separately positive port. Its
role would be to normalize the sector determinant frame by fixing the linear
exponential ambiguity left by reflection sewing.

This gives a new possible interpretation of the previously unavoidable first
current:

- the trace-class tail controls determinant existence;
- the prime-square current participates in the first admissible
  regularization;
- the primitive current fixes the determinant's linear frame anomaly;
- seam and archimedean currents enforce the reciprocal boundary comparison.

This interpretation must be derived from finite Euler cutoffs. It cannot be
assigned by matching the known Hadamard exponential afterward.

## Stronger growth outcomes

If the admitted multiplier has order strictly below one, then the linear term
is also forbidden and the gauge is trivial.

If only finite order (ho>1) is known, the surviving odd gauge is a finite
odd polynomial whose degree does not exceed (ho). The required source frame
then consists of finitely many odd jets rather than one.

Thus growth converts an infinite coherence problem into a finite jet problem.

## Finite falsifier

At cutoff (X), compute the proposed source determinant and its centered
logarithmic first jet. Apply the hostile refactoring

\[
D_{+,X}(z)\longmapsto e^{c_Xz}D_{+,X}(z).
\]

The reflected scalar product, center value, divisor, and exponential type are
unchanged. Only the first jet shifts by (c_X).

If the source packet contains no independent equation fixing that jet, the
determinant frame remains unauthorized. If the primitive boundary current
fixes it and the cutoff increments telescope, the odd-gauge obstruction is
removed.

## Next decisive calculation

For the labelled theta/Tate cutoff, calculate the first logarithmic jet of the
sector denominator before reflection sewing. Determine whether its cutoff
increment is exactly the retained primitive current together with the required
endpoint normalization.

An exact identity would supply the first genuinely source-derived determinant
frame law in the programme. A residual term or dependence on arbitrary
regularization closes this repair.
