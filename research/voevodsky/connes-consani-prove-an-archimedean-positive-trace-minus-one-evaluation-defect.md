# Connes--Consani prove an archimedean positive trace minus one evaluation defect

## Primary source

Alain Connes and Caterina Consani, *Weil positivity and trace formula, the archimedean place*, Selecta Mathematica 27 (2021), article 77, arXiv:2006.13771.

The primary PDF was downloaded to `temp/connes-consani-weil-archimedean.pdf` and audited directly.

## Exact positive trace

Let `S` be the orthogonal projection onto the even Sonin space consisting of functions that, together with their Fourier transforms, vanish on `[-1,1]`. For a multiplicative test function `f`, the paper defines

\[
\operatorname{Tr}(\vartheta(f)S).
\]

For a convolution square `f=g*g^*`,

\[
\operatorname{Tr}(\vartheta(f)S)
=
\operatorname{Tr}(\vartheta(g)S\vartheta(g)^*)
\ge0.
\]

This is a genuine source-derived positive trace factorization.

## Exact archimedean comparison

Theorem 4.7 proves

\[
\boxed{
\operatorname{Tr}(\vartheta(f)S)
=W_\infty(f)+E(f),
}
\]

where

\[
E(f)=\int f(\lambda^{-1})\epsilon(\lambda)d^*\lambda
\]

is an explicit remainder built from prolate spectral coefficients. Thus

\[
W_\infty=
\text{positive Sonin trace}
-
E.
\]

This is the archimedean analogue of the positive-minus-defect decomposition sought in the Suzuki complex.

## The defect is essentially one-dimensional on the restricted support

Theorem 6.11 proves that for `g` supported in

\[
[2^{-1/2},2^{1/2}]
\]

and satisfying the endpoint/Mellin conditions at `plus-or-minus i/2`,

\[
\boxed{
W_\infty(g*g^*)
\ge
\operatorname{Tr}(\vartheta(g)S\vartheta(g)^*)
-c\,|\widehat g(0)|^2,
\qquad
c=\frac4{\log2}.
}
\]

The proof is not formal. It studies a compact self-adjoint operator, isolates one eigenvalue above the positive threshold, and repairs the corresponding codimension-one defect using a rank-one quadratic form (Lemma 6.9).

If additionally

\[
\widehat g(0)=0,
\]

then

\[
W_\infty(g*g^*)
\ge
\operatorname{Tr}(\vartheta(g)S\vartheta(g)^*)
\ge0.
\]

This gives a noncircular positive result on a compact-support, codimension-constrained archimedean test space.

## Relation to the minimal Suzuki endpoint

The paper supplies precisely the mechanism missing from the formal mapping cone:

1. a source-defined orthogonal projection `S`;
2. an automatically positive trace;
3. an exact trace--Weil remainder identity;
4. compact-operator control reducing the hostile sector to codimension one;
5. a source evaluation `g-hat(0)` that controls that sector.

This is stronger than declaring the endpoint to equal an abstract cokernel. The correcting coordinate is independently identified as a Mellin evaluation.

However, it applies only to the archimedean functional under a support restriction excluding rational primes. The paper explicitly chooses support inside `(1/2,2)` so prime terms are absent. It therefore does not identify the cokernel of Suzuki's full completed-zeta Toeplitz operator.

## Why it does not globalize formally

For the complete Weil functional, enlarging multiplicative support introduces prime terms. The archimedean positive trace and rank-one evaluation defect do not control:

- the negative prime atoms;
- deterministic cross-prime polarization;
- growth of defect rank as the finite place set expands;
- compatibility of the prolate remainder with Suzuki's generalized-inner denominator;
- a uniform constant under support exhaustion.

The later semilocal prolate paper describes this extension as a strategy and constructs stable Sonin carriers, but does not prove the corresponding positive-trace comparison with all finite-place Weil terms.

## Exact bridge target

For each finite place set `Sigma`, seek

\[
W_\Sigma(g*g^*)
=
\operatorname{Tr}(\vartheta_\Sigma(g)S_\Sigma\vartheta_\Sigma(g)^*)
-E_\Sigma(g*g^*)
\]

and a source-defined finite-rank map `R_Sigma` such that

\[
E_\Sigma(g*g^*)
\le
\|R_\Sigma g\|^2,
\]

with the combined positive trace dominating the correction on the desired test subspace. Transition maps must preserve the exact forms as `Sigma` grows.

The archimedean theorem realizes this pattern with one evaluation coordinate. No theorem found realizes it after primes enter.

## Disposition

A nontrivial positive source factorization does exist at the archimedean place:

\[
\boxed{
W_\infty(g*g^*)
=
\text{positive Sonin trace}
-
\text{one controlled evaluation defect}.
}
\]

It proves positivity after the zero-mean constraint on a compact support window. This is the strongest prior constructor found in the present Suzuki/prolate aperture, but its prime-bearing semilocal extension remains exactly the missing theorem.
