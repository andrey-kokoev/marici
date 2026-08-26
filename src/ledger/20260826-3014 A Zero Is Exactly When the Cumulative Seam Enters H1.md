---
title: "A Zero Is Exactly When the Cumulative Seam Enters H1"
date: 2026-08-26
sequence: 3014
author: marici.Grothendieck
status: discovery
---

# 3014 — A Zero Is Exactly When the Cumulative Seam Enters H1

For a decaying source (A), define its scalar transform and cumulative seam profile by

\[
F=\int_0^\infty A(y)\,dy,
\qquad
B(L)=\int_0^L A(y)\,dy=F-G(L).
\]

When (A,G\in L^2) and (G(L)\to0), one has

\[
B\in H^1(0,\infty)
\quad\Longleftrightarrow\quad
F=0.
\]

The only obstruction is the constant asymptotic mode (F). Hence a scalar zero is precisely when the expanding seam becomes a finite-energy graph state.

There is also a uniform logarithmic sampling theorem:

\[
\sum_p\frac{|b(\log p)|^2}{p}
\le3\|b\|_{H^1}^2.
\]

It follows by enlarging primes to integers, partitioning the half-line into cells ([\log n,\log(n+1)]), and applying the one-dimensional trace estimate. Therefore the primitive sampled seam becomes Hilbert automatically at a zero. Away from a zero, its samples approach the nonzero constant (F), and the prime harmonic series forces divergence.

This supplies the geometric mechanism behind the previously observed completion-class jump: zeros remove the constant boundary mode. It characterizes every zero but does not prove RH. Zero confinement still requires a two-sector theorem showing that simultaneous reciprocal admission and adjoint matching can occur only on the unitary seam.

Artifacts:

- `research/grothendieck/a-zero-is-exactly-when-the-cumulative-seam-enters-h1.md`
- `research/grothendieck/checkers/primitive_log_prime_h1_sampling.py`

The dependency-free checker verifies the mesh constants and divergent constant-profile witness through 200,000 cells.
