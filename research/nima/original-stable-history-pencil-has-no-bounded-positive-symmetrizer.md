# Original stable-history pencil has no bounded positive symmetrizer

Let `A_st` be the direct sum of the two stable half-line differentiation generators used by the Xi Rosenbrock pencil. Each component generates a unilateral translation semigroup with a stable boundary condition. Its spectrum contains a nonreal half-plane rather than lying on the real axis.

Suppose there were a bounded strictly positive invertible carrier metric `G` satisfying

$$
A_{\rm st}^*G=GA_{\rm st}.
$$

Then

$$
H=G^{1/2}A_{\rm st}G^{-1/2}
$$

would be self-adjoint on the transported domain. Bounded similarity preserves spectrum, so

$$
\sigma(A_{\rm st})=\sigma(H)\subset\mathbb R.
$$

This contradicts the half-plane spectrum of the stable unilateral generators.

Therefore the exact stable-history Xi pencil cannot possess a bounded positive symmetrizer on its original state carrier. An indefinite metric may encode reciprocal symmetry, but it does not give positive confinement.

This also clarifies why unitary tail-plus-seam coordinate conjugation is insufficient: unitary equivalence preserves the same nonreal generator spectrum. A positive realization requires a genuine conservative dilation on a larger bilateral carrier, not merely a re-expression of the stable pencil.

The remaining constructor must satisfy two conditions simultaneously:

1. compress or reduce to the original stable Rosenbrock kernel characteristic, preserving `ker R_Xi(z) iff tau(z)=0`;
2. carry a positive self-adjoint ambient pencil whose active spectral coefficient is positive.

This is a conservative dilation with characteristic preservation, not a positive metric on the original pencil.

Status: bounded positive symmetrizer on the original stable-history carrier ruled out; divisor-preserving conservative dilation is the corrected RH-bearing gate.
