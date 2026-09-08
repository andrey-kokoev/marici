# Complex triangulation-weight factorability

## Question

What changes when nonzero triangulation weights and facet scales are complex rather than positive real?

## Claim boundary

The character-lattice criterion is generic for a fixed incidence matrix. Smith invariants are computed only for polygon sizes four through seven.

The monomial map from channel scales to triangulation weights is a morphism of complex algebraic tori. A nonzero complex weight vector lies in its image exactly when every integer left-kernel character is trivial:

\[
A^Tz=0\quad\Longrightarrow\quad
\prod_Tw_T^{z_T}=1.
\]

These are the same integer binomials used for positive magnitudes. Complex reconstruction can have finite root ambiguity determined by the nonzero Smith invariants of `A`.

Exact Smith forms for `n=4..7` have one nontrivial invariant equal to `n-3`, with kernel orders `1,2,3,4`. This has a visible diagonal subgroup: multiplying every facet scale by a common `(n-3)`rd root of unity fixes every triangulation weight because every triangulation contains exactly `n-3` channels. The finite computation shows this diagonal subgroup exhausts the kernel at these stages; it does not prove the pattern for all `n`.

The complex character-relation counts are `0,0,5,28`, matching the rational magnitude gate. Real signs see only the order-two part of the root kernel: this explains the extra `F2` parity relation at tested odd polygon sizes, while six points have a complex cubic branch ambiguity but no global real-sign ambiguity.

## Disposition

For complex source coefficients, test the integer binomials and retain a Smith-determined root branch when reconstructing facet scales. At tested stages the branch is a common `(n-3)`rd root of unity. No unbounded Smith classification is asserted.
