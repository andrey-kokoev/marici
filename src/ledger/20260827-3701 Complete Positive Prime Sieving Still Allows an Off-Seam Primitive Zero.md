---
author: marici.Grothendieck
date: 2026-08-27
---

# 3701 — Complete Positive Prime Sieving Still Allows an Off-Seam Primitive Zero

## Result

For any positive primitive seed \(g\), the arithmetic completion

\[
\Psi(u)=\sum_{n\ge1}n^{-1/2}g(u+\log n)
\]

satisfies the full positive prime-sieve hierarchy.

Choosing \(g=\phi_2+\phi_1\) gives an off-seam primitive-transform zero

\[
z_0=\sqrt\pi e^{-i\pi/4}
\]

inside the absolute Euler chamber. There

\[
\widehat\Psi(z)
=
\widehat g(z)\zeta(1/2+iz),
\]

so the primitive zero survives while the zeta factor is finite and nonzero.

## Consequence

Complete positive prime sieving supplies arithmetic provenance but no
zero-orientation theorem. The next indispensable structure is reciprocal
Poisson sewing of the primitive cell with the moving archimedean endpoint.

## Durable verification

- `research/grothendieck/complete-positive-prime-sieving-still-allows-an-off-seam-primitive-zero.md`;
- `research/grothendieck/checkers/check_full_positive_sieve_off_seam_hostile.py`.

Allocator authority: `grothendieck-full-positive-sieve-off-seam-hostile-20260827`.
