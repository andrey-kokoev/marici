# Elementary abelian p-kernels have augmentation-ideal norm homology

Epistemic-graph event: 1364.

## General theorem

Let `E=(C_p)^n` and work over `F_p`.  With `epsilon_i=g_i-1`,

`F_p[E]=F_p[epsilon_1,...,epsilon_n]/(epsilon_i^p)`.

For a rank-`k` coordinate kernel on a subset `B`, its group norm is

`N_B=product_(i in B) epsilon_i^(p-1)`.

This is the top socle monomial of the kernel algebra `A_B`.  Multiplication
by `N_B` is nonzero only on collapsed monomials of degree zero, so it is
square-zero and

`H(A,N_B) congruent (I_B/Soc(A_B)) tensor A_(B^c)`.

Its total dimension is

`p^(n-k)(p^k-2)`.

## Grading and Loewy length

The Hilbert series is

`(1+t+...+t^(p-1))^(n-k)`

times

`((1+t+...+t^(p-1))^k-1-t^(k(p-1)))`.

Under the collapsed-kernel augmentation ideal, the nonzero module has Loewy
length

`k(p-1)-1`.

The special vanishing occurs only for `(p,k)=(2,1)`.  Already a one-bit
`C_p` quotient for odd `p` has residual norm homology of dimension `p-2` per
fiber.

## Controls

- `C2` in characteristic two: zero homology, recovering the one-bit
  five-site exception.
- `C3` in characteristic three: one residual class represented by `epsilon`;
  the norm image removes `epsilon^2`.
- `(C2)^k`: the theorem specializes to Ledgers 1340--1342.

## Scope

The result is intrinsic modular group-algebra structure for an elementary
abelian kernel.  It does not assert a physical relative-chain trace or that a
geometric source realizes such a kernel.  It predicts the bad-prime module
that any admitted physical Mackey realization would have to compare against.
