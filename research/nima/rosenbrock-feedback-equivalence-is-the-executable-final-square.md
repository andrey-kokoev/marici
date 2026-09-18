# Rosenbrock-feedback equivalence is the executable final square

A pointwise kernel injection is insufficient for multiplicity unless its parameter dependence and root-chain action are controlled. The robust target is a holomorphic block equivalence.

Seek holomorphic invertible operator families `E(z)` and `F(z)` such that

$$
E(z)\mathcal R_\Xi(z)F(z)
=
\begin{pmatrix}
I-CG(\lambda(z))&0\\
0&H_{\rm aux}(z)
\end{pmatrix},
$$

where `H_aux(z)` is holomorphically invertible on the declared chart.

Then

$$
\ker\mathcal R_\Xi(z)
\cong
\ker(I-CG(\lambda(z))),
$$

and holomorphic equivalence preserves local algebraic multiplicity and parameter root chains. At determinant-class cutoffs,

$$
\det\mathcal R_\Xi(z)
=u(z)\det(I-CG(\lambda(z))),
$$

where

$$
u(z)=\det E(z)^{-1}\det F(z)^{-1}\det H_{\rm aux}(z)
$$

is nowhere zero.

The block operations must be sourced from:

1. the fixed-forcing one-leg lift;
2. the one-sided sum/difference Hadamard transform;
3. the pair-to-bordered crossing;
4. reciprocal Fourier–Tate sewing;
5. seam resegmentation and the declared boundary traces.

No operation may divide by `tau` or use zero locations.

This identity is finite-packet executable: write both Rosenbrock system matrices in the same labelled basis and perform symbolic block Gaussian elimination. A mismatch in any wall, endpoint, linking, or direct-feedthrough block rejects the comparison before spectral specialization.

Status: final source coherence converted to one holomorphic block-equivalence test; explicit common-basis matrices remain to be materialized.
