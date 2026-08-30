# Spectral growth is an explicit-output cost, not a total complexity law

## Question

Is the growth of the integral constructor state forced in every exact
presentation?

## Exact spectral structure

The neutral commutator response has characteristic polynomial

\[
\chi_C(x)
=x^4-147460x^3+294918x^2-147460x+1
=(x-1)^2(x^2-147458x+1).
\]

The fixed-space dimension is one, although the root \(1\) has algebraic
multiplicity two. Thus the rational response contains:

- a two-dimensional parabolic sector with one fixed direction and one
  generalized fixed direction;
- a reciprocal hyperbolic sector with eigenvalues
  \(\lambda,\lambda^{-1}\).

The expanding root obeys

\[
\lambda+\lambda^{-1}=147458,
\]

so

\[
\lambda>147457.
\]

## Basis-invariant explicit-output lower bound

Every authorized integral basis change replaces \(C\) by \(P^{-1}CP\) and
preserves its spectrum. For any such explicit four-by-four matrix output,

\[
\rho(C^n)
\leq
\lVert C^n\rVert_\infty
\leq
4\max_{i,j}|(C^n)_{ij}|.
\]

Therefore

\[
\max_{i,j}|(C^n)_{ij}|
>
\frac{147457^n}{4}.
\]

The bit length of at least one explicit entry grows at least linearly in
\(|n|\). This lower bound cannot be removed by an integral change of basis.

At \(n=32\), the current presentation has a 551-bit largest entry, while the
spectral argument already forces at least 548 bits in every conjugate explicit
matrix presentation.

## Falsification of a total-cost conservation law

The compact packet

\[
(n,C)
\]

does not materialize \(C^n\). Its variable input requires only order
\(\log(|n|+1)\) bits, and repeated squaring gives a compact constructor
circuit.

Hence spectral growth does not force every exact encoding to store linearly
many bits. It forces linear bit growth only when the interface demands the
explicit integral matrix.

There is no representation-independent conservation law for total storage
across arbitrary output types.

## Explanation

The cost is attached to a requested interface:

\[
\text{compact constructor}
\longrightarrow
\text{explicit matrix materialization}.
\]

The hyperbolic factor forces the expansion at that interface. The parabolic
factor records a separate generalized-fixed response that cannot explain the
exponential growth.

Thus the invariant explanatory object is:

\[
(\text{source action},\text{requested output type},\text{cost model}).
\]

Spectrum constrains the explicit-output component. It does not determine the
cost of a compact circuit presentation.

## Theorem status

The factorization, fixed-space dimension, and spectral lower bound are exact.
The inequality applies to every conjugate matrix presentation, not merely the
four bounded basis fixtures.

The checker verifies:

- the exact reciprocal factorization;
- a separate trace-power spectral witness;
- six explicit matrix powers through \(n=32\);
- four unimodular conjugacy fixtures;
- the compact-encoding hostile that refutes a universal storage law.

## Claim boundary

This does not prove an optimal circuit lower bound or a physical cost law. It
proves an explicit-matrix output lower bound and identifies why that theorem
cannot be promoted to arbitrary exact encodings.
