# Unbounded Weil positivity as a regular prime-transfer dilation

## Question

How can the universal Weil-form identity be attacked without assuming its global positivity?

## Local positive blocks

Short-support Weil positivity gives unconditional positive form blocks on logarithmic cells narrower than the first prime displacement. After quotienting each local radical, let `H_0` be the local Weil Hilbert block. Translation identifies copies of this block along the intrinsic multiplicative lattice.

For each prime `p`, the complete archimedean-plus-prime cross form at displacement `log p` defines, when bounded, a normalized transfer

`C_p = A^(-1/2) B_p A^(-1/2)`

on `H_0`, interpreted at form level. Two-cell positivity is exactly `||C_p||<=1`. The first test is `p=2`.

## One-prime completion

If the prime-power cross forms obey exact composition, the `p`-tower Gram kernel is

`K_p(i,j)=C_p^(j-i)`

with the adjoint convention for reversed order. A contraction dilation then makes every finite one-prime block positive. The scalar specialization is the exact Toeplitz kernel `r^|i-j|` with determinant `(1-r^2)^n`.

Thus unbounded positivity along one prime is not infinitely many unrelated inequalities: it is one edge contraction plus a source composition law, or more generally contractive Schur defects.

## Mixed-prime completion

Unique factorization makes the exponent lattice the free commutative monoid on intrinsic primes. Global positivity follows from a regular positive-definite representation of this monoid if the normalized transfers admit a compatible regular dilation. A sufficient source theorem is:

1. every `C_p` is contractive;
2. prime-power transfers compose;
3. transfers for distinct primes doubly commute, including adjoints;
4. the full cross kernel factorizes through the resulting regular dilation;
5. finite-support cores converge to the complete Weil form without a new radical.

The mixed-prime rectangle is the first coherence test:

`C_p C_q = C_q C_p`,

`C_p* C_q = C_q C_p*`.

Ordinary commutation alone is insufficient for a regular unitary dilation.

## Exact obstruction from prior work

The isolated negative prime block has eigenvalues of both signs, so `C_p` must include the archimedean, endpoint, seam, and mixed completion; prime incidence alone cannot be a positive transfer.

At prime two, the level-44 continuum operator is rigorously positive. Nima's directed proof combines the certified odd weighted-Schur bound, symmetric Riccati reduction, endpoint inertia, and pole exclusion. Level 43 has a directed negative even eigenvalue, so level 44 is the first separated crossing. The negative secular sign at level 44 is also rigorous and is compatible with positivity: the rank-one repair converts an operator with exactly one negative direction into the positive level-44 operator.

Every omitted gamma channel is positive semidefinite, so positivity of the level-44 truncation implies positivity of the full archimedean gamma tower for this support-constrained prime-two block. This passes the first complete prime-two edge model. It does not prove prime-power composition or mixed-prime dilation. Edge positivity still does not imply global positivity unless the composition, mixed-prime, and completion conditions hold.

## Decision

The most concrete noncircular route to unbounded positivity is a regular-dilation theorem for complete normalized prime transfers. Its first executable gates are:

1. prove the prime-power composition law for the complete normalized transfers;
2. test the `2 x 3` mixed-prime double-commutation rectangle;
3. prove convergence to the universal Weil form.

Failure at any gate localizes which proposed identity is false without using zero data.
