# RH as conditional negative definiteness of the Li sequence

## Statement

Let `lambda_0=0` and extend the Li coefficients evenly to the integers by
`lambda_(-n)=lambda_n`. Subject to the standard Li criterion and the standard
paired-zero formula, the following are equivalent:

1. the Riemann hypothesis;
2. `lambda_n >= 0` for every positive integer `n`;
3. `n -> lambda_n` is conditionally negative definite on `Z`;
4. there is a real Hilbert space and a `Z`-cocycle `b_n` for an orthogonal
   representation such that `lambda_n=||b_n||^2`.

Here conditional negative definiteness means that, for every finite family
of integers `n_i` and reals `c_i` with `sum_i c_i=0`,

`sum_(i,j) c_i c_j lambda_(n_i-n_j) <= 0`.

Equivalently, for every finite list of positive integers, the anchored
kernel

`K(m,n)=(lambda_m+lambda_n-lambda_(|m-n|))/2`

is positive semidefinite.

## Proof architecture

`3 => 2` follows by testing the two points `0,n` with coefficients `1,-1`.
The equivalence `2 <=> 1` is Li's criterion.

Under RH, each functional-equation pair has
`u_rho=1-1/rho` on the unit circle and contributes

`|1-u_rho^n|^2`.

For any fixed unit complex number `u`, the function
`n -> |1-u^n|^2` is conditionally negative definite: it is the squared
displacement of the cocycle `b_n=1-u^n`. Positive convergent sums preserve
conditional negative definiteness. This gives `1 => 3` through the paired
zero formula. The equivalence `3 <=> 4` is the standard Hilbert embedding
theorem for conditionally negative definite kernels.

This is a reformulation, not a proof of RH and not a novelty claim.

## Why this improves Gate C

Individual Li positivity hides the compatibility required between different
orders. The CND formulation exposes all mixed inner products:

`<b_m,b_n> = K(m,n)`.

It therefore supplies exact finite falsifiers: one negative eigenvalue of an
anchored Li Gram matrix disproves the proposed cocycle architecture at that
rank. Conversely, a source construction of the whole CND kernel would prove
all Li inequalities simultaneously rather than one coefficient at a time.

The remaining noncircular problem is to derive `K` as a positive arithmetic
energy kernel from primes, the archimedean completion, and endpoint terms,
without assuming the zero fibres lie on the unit circle.

## Numerical reconnaissance

`checkers/li_cocycle_gram_probe.py` computes the first twelve Li coefficients
from derivatives of the completed zeta function and tests the anchored Gram
matrices at high precision. This is hostile reconnaissance only; it is not a
proof at any rank unless accompanied by certified error bounds.
