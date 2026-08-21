# The Li cocycle gate is a Toeplitz increment problem

## Exact factorization

Let `lambda_0=0`, extend `lambda` evenly, and define the anchored kernel

`K(m,n)=(lambda_m+lambda_n-lambda_(|m-n|))/2`, for `m,n>=1`.

Define the increment correlations

`c_0=lambda_1`,

`c_k=(lambda_(k+1)-2 lambda_k+lambda_(k-1))/2`, for `k>=1`.

For rank `N`, let `T_N=(c_(|i-j|))_(0<=i,j<N)` and let `S_N` be the lower
triangular matrix whose entries on and below the diagonal are one. Then

`K_N = S_N T_N S_N^T`.

Since `S_N` is invertible with determinant one,

`K_N >= 0` if and only if `T_N >= 0`.

## Proof

If `b_n=sum_(j=0)^(n-1) x_j`, then the stationary correlation assignment
`<x_i,x_j>=c_(|i-j|)` gives `Gram(b_1,...,b_N)=S_N T_N S_N^T`.
Expanding the double sums telescopes twice and yields
`<b_m,b_n>=K(m,n)`. Conversely, applying the discrete difference matrix to
`K_N` recovers `T_N`.

The symbolic checker verifies this identity with independent formal
variables through rank seven. The displayed telescoping argument proves it
at every rank.

## Research consequence

The RH-equivalent CND gate can be attacked through a stationary sequence:
prove that the second-difference sequence `c_k` is positive definite on
`Z`. By the Herglotz theorem, this is equivalent to a positive measure on the
unit circle having `c_k` as Fourier coefficients.

This is a smaller source target than constructing all mixed Li vectors
directly. Arithmetic locality should produce one increment correlation
function—or its positive spectral measure—and discrete integration then
produces the entire Li Gram system.

It also gives sharper finite falsifiers: any negative Toeplitz minor of the
second differences kills the homogeneous cocycle proposal. Unlike checking
only `lambda_n>=0`, these minors test compatibility across orders.

No source-positive measure has yet been constructed. Invoking the
critical-line zero phases supplies the conditional target but assumes the
spectral conclusion.
