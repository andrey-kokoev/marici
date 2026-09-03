# A Sobolev gap gives computable Galerkin tail rates for local Weil operators

## Question

How can compactness of the fixed-support Weil operator be converted into quantitative Galerkin error bounds?

## Nested Sobolev factorization

Fix `L` and choose two positive orders

`0<r<s`.

The completed Weil form is bounded on `H_0^r((-L,L))`. Let `B_(L,r)` denote its bounded representing operator at that level. On `H_0^s`, the representing operator factors as

`A_(L,s)=J_(s,r)^* B_(L,r) J_(s,r)`,

where

`J_(s,r):H_0^s -> H_0^r`

is the compact Sobolev embedding. This factorization is source-side and does not assume positivity.

## Sine-basis approximation numbers

For the Dirichlet sine basis on an interval of length `2L`, the Sobolev weights scale as

`omega_n=1+(pi n/(2L))^2`.

If `P_M` projects onto the first `M` modes, then

`||J_(s,r)(I-P_M)|| <= omega_(M+1)^(-(s-r)/2)`.

Consequently

`||A_(L,s)-P_M A_(L,s) P_M||`

is bounded by

`2 ||B_(L,r)|| omega_(M+1)^(-(s-r)/2)`

up to the smaller quadratic tail term obtained by expanding `J^*BJ-P_MJ^*BJP_M`. The exact constant depends only on the declared projection convention.

Thus any strict Sobolev gap gives an explicit algebraic convergence rate. For example, `r=1/2` and `s=1` gives an operator-norm rate of order `M^(-1/2)`.

## Sector refinement

The canonical sectors permit sharper bookkeeping:

- endpoint terms are finite rank; adjoining their Riesz representers to the trial space removes their tail exactly;
- prime terms factor through `H_0^s -> L^2`, giving rate governed by the full gap `s`;
- the archimedean term can use any intermediate `r>0`, giving rate arbitrarily close to `M^(-s)` but with constants worsening as `r` approaches zero because the logarithmic multiplier is not `L^2` bounded.

This tradeoff is explicit: a smaller `r` improves asymptotic rate but enlarges the digamma domination constant.

## One-sided certified spectral consequence

Let `A_M=P_M A P_M` and let `epsilon_M` bound `||A-A_M||`, with `A_M` extended by zero on the orthogonal complement. The spectrum of that extended compression contains zero. Hence spectral variation gives only

`inf spectrum(A) >= min(0,lambda_min(A_M))-epsilon_M`.

Therefore, if `lambda_min(A_M)+epsilon_M<0`, a negative eigenvalue is certified. A positive finite matrix and a nonzero norm tail do not certify full nonnegativity: the unresolved complement may contain a negative eigenvalue arbitrarily close to zero.

Full positivity requires a signed tail argument, such as `C_M>=0` plus a valid Schur control of the off-diagonal block. Compactness and norm convergence alone provide falsification, not verification.

## Missing constants

An executable certificate still needs:

1. a fixed Fourier and Sobolev normalization;
2. explicit `||B_(L,r)||` bounds from endpoint, digamma, and prime coefficients;
3. interval enclosures for the finite Galerkin matrix;
4. augmentation by endpoint representers or an explicit finite-rank tail bound.

No positive spectral measure is used in these requirements.

## Disposition

The local Sobolev programme now has a quantitative finite-falsification architecture. The first implementation target is one modest support window and `r=1/2,s=1`, with source-derived constants and interval-enclosed matrix entries. A proof route additionally needs sign-preserving tail structure; norm-smallness is insufficient.
