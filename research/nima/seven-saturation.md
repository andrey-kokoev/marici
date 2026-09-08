# Seven-point coordinate saturation

## Question

Does the local ideal acquire components confined to coordinate hyperplanes?

## Claim boundary

Use the previously generated 63 local quadrics in 42 variables. This certificate establishes coordinate regularity and saturation, not independently the primeness of the Laurent ideal.

For each variable x_i, the checker completes a homogeneous graded reverse lexicographic basis with x_i last. All 42 completions finish within the declared caps of 200 basis elements, 20000 pairs and 10000 reductions per order. The largest basis has 72 elements. In every completed basis, every leading monomial omits x_i.

If a polynomial f is in normal form, multiplication by x_i preserves that property: divisibility by a leading generator not involving x_i is unchanged. Hence x_i f in the ideal implies f is in the ideal. This proves I:x_i=I for every i and therefore

\[
I:(x_0\cdots x_{41})^\infty=I.
\]

The reductions are monic binomial identities valid over every field. There are no coordinate-supported associated components: each coordinate is a nonzerodivisor on the quotient. This is stronger than the earlier radicality certificate and does not follow from it alone.

## Disposition

All coordinate saturation checks pass. To identify this saturated ideal with the triangle toric ideal using a self-contained seven-point certificate, it remains to check that the local exponent differences generate the full saturated triangle relation lattice. Rational rank equality alone would leave a finite-index ambiguity. The general unit-recovery argument motivates that comparison, but this packet records only the newly checked saturation coordinate.
