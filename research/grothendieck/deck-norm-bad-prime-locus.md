# Deck-norm bad-prime locus

## Theorem

Let \(K\) be the kernel of a finite deck quotient and let

\[
N_K=\sum_{k\in K}k
\]

act on the integral regular lattice.  The paired Mackey theorem gives

\[
N_K^2=|K|N_K.
\]

Consequently

\[
e_K=\frac{1}{|K|}N_K
\]

is an idempotent after base change to \(\mathbf Z[1/|K|]\).  No scalar
multiple of \(N_K\) is the normalized projector over \(\mathbf Z\) when
\(|K|>1\).  The obstruction is supported on

\[
V(|K|)\subset\operatorname{Spec}\mathbf Z.
\]

More sharply, for every prime \(p\mid |K|\), reduction modulo \(p\) gives

\[
N_K^2=0
\]

while \(N_K\ne0\) on the regular module.  Away from those primes,
\(|K|^{-1}N_K\) is again an idempotent.  Thus the same multiplicity that
obstructs integral normalized ambidexterity canonically identifies its
bad-characteristic support.

For the smallest branch quotient \(C_2\to1\), the sole bad locus is \(V(2)\):
the invariant projector exists away from characteristic two, while the norm
becomes a nonzero square-zero operator in characteristic two.

## Scope

This is a genuine arithmetic consequence of the integral deck lattice and
its derived multiplicity.  It is **not** a derivation of \(\operatorname{Spec}
\mathbf Z\), primes, or arithmetic from the bare Carrier: the integral
coefficient base is independently present.  It also does not admit a
physical relative-chain pushforward.  Therefore it supplies a conditional
bad-prime shadow, not an Euler product, Frobenius theory, or Phase-II
arithmetic geometry.

## Verification

`checkers/deck_norm_bad_prime_locus.py` verifies \(N_K^2=|K|N_K\) for cyclic
regular lattices of orders 2 through 12.  At every tested good prime it
checks the normalized idempotent; at every prime divisor it checks that the
unscaled norm is nonzero and square-zero.
