---
author: marici.Nima
---

# 1484 — Path Reversal Closes the Two-Insertion Collision Alphabet

## Status

Exact coherence completion of Entry 1483 at the level of finite pole–log
collisions. A complete weight-two antiderivative is still not claimed.

## Reversal identity

Let \(I_2(x_1,w_1,w_2,x_2;y)\) be the source-derived two-white-site path
integrand of Entry 1479. Direct symbolic reduction proves

\[
\boxed{
I_2(x_1,w_1,w_2,x_2;y)
=I_2(x_2,w_2,w_1,x_1;y).
}
\]

This is an equality of rational functions over
\(\mathbb Q(x_1,w_1,w_2,x_2,y)\), not a numerical or integrated symmetry.

## Consequence for sequential pushforwards

Entry 1483 showed that integrating \(w_2\) first leaves the second-stage
collision letters

\[
2y,
\qquad
x_2+y,
\qquad
x_2-y.
\]

Path reversal therefore proves that the opposite order leaves

\[
2y,
\qquad
x_1+y,
\qquad
x_1-y.
\]

Hence the order-independent finite collision alphabet is contained in

\[
\boxed{
\mathcal A_2
=\{2y,x_1-y,x_1+y,x_2-y,x_2+y\}.
}
\]

Neither sequential order generates \(x_1+x_2-2y\). The cancellation is
therefore not an artifact of choosing the right-hand white site first.

## Interpretation

At two insertions, source time ordering, Kummer pushforward, and path reversal
close on the pre-existing edge and signed-energy coefficient arrangement.
The rational denominator arrangement is larger, but its numerator removes the
extra collision letter coherently in both orders.

This supplies the first nontrivial evidence that the mass-insertion
coefficient calculus is an order-coherent iterated pushforward rather than a
generic hyperlogarithmic integral on every available denominator divisor.

## Next falsifier

Assemble endpoint terms and compute the complete weight-two symbol. The claim
fails beyond the collision audit if an endpoint contribution introduces a
letter outside \(\mathcal A_2\), or if the two sequential symbols disagree.

## Durable evidence

- `research/nima/derive_mass_insertion_path_integrand.sage`;
- allocator claim `seqclaim-6535023a7d649bda67575dfb`.
