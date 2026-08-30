# Attack surface: positivity of the arithmetic Li Toeplitz functional

## Finite test objects

Let `p(z)=sum_(j=0)^d a_j z^j`. Define

`E(p)=sum_(i,j=0)^d conjugate(a_i) a_j c_(|i-j|)`,

where

`c_0=lambda_1`,

`c_k=(lambda_(k+1)-2lambda_k+lambda_(k-1))/2`.

Every coefficient is determined arithmetically by the completed zeta
function. Thus `E(p)` is a source-computable finite quadratic form; no zero
locations are required to state or evaluate it.

The Gate C theorem is exactly

`E(p) >= 0 for every complex polynomial p`.

At degree `d`, this is positivity of the `(d+1)`-by-`(d+1)` Toeplitz matrix
`(c_(|i-j|))`. A negative polynomial witness is a finite falsifier.

## Conditional spectral interpretation

Under RH the form becomes, with the appropriate functional-pair convention,

`E(p)=sum_rho |rho|^(-2) |p(1-1/rho)|^2`,

which is manifestly positive. This formula specifies the target but is not
allowed as the source-side proof.

## Chosen attack direction

Expand each `c_k` through the arithmetic formula for the Li coefficients and
keep four contributions separate:

1. the pole/endpoint normalization;
2. the archimedean gamma factor;
3. the prime-power term;
4. the interaction terms created by the Toeplitz quadratic assembly.

The earlier isolated-prime test already shows that item 3 need not be
positive alone. Therefore the sought explanation must exhibit a coupled
completion identity, not a sum of independently positive prime blocks.

The immediate finite objective is degree two. Write

`p(z)=a+bz+cz^2`.

Derive `E(p)` explicitly from `lambda_1,lambda_2,lambda_3`, split it by the
four sources above, and identify the minimal completion term that repairs the
indefinite prime contribution. A successful degree-two identity must then
generalize by Toeplitz locality; a fitted three-by-three factorization does
not count.

## Hard falsifiers

- A certified negative Toeplitz minor.
- A claimed local decomposition that drops endpoint or gamma cross-terms.
- Positivity obtained only after inserting critical-line phases.
- A factorization whose generators depend on the chosen degree.
- Failure of the proposed local rule at the next Toeplitz rank.

This is the current charge: derive the first universal coupled positivity
identity on the arithmetic side, beginning with the degree-two Toeplitz
form, while preserving a rule capable of extending to every degree.
