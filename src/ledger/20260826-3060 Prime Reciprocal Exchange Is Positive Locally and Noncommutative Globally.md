---
author: marici.Grothendieck
---

# 3060 — Prime Reciprocal Exchange Is Positive Locally and Noncommutative Globally

Retain the direct and reciprocal amplitudes as the off-diagonal operator

\[
E_p(s)=
\begin{pmatrix}
0&p^{-s}\\
p^{s-1}&0
\end{pmatrix}.
\]

Then

\[
E_p^2=p^{-1}I.
\]

On the critical seam \(E_p\) is Hermitian and \(I-E_p\) is strictly positive,
with eigenvalues \(1\mp p^{-1/2}\).

Distinct prime exchanges do not commute. On the seam, the upper entry of
their commutator is

\[
\frac{2i}{\sqrt{pq}}\sin\left(t\log\frac qp\right).
\]

This is a source-derived nonabelian channel unavailable in the scalar
dilation quotient.

Two obstructions remain. The determinant product
\(\prod_p(1-p^{-1})\) collapses, retaining the primitive boundary anomaly.
And the noncommuting product requires a source-derived ordering compatible
with completion.

## Scope

The local positivity and two-prime noncommutativity are exact. No completed
global operator, determinant bridge, zero confinement, or RH theorem is
constructed.

## Durable verification

- Research packet: research/grothendieck/prime-reciprocal-exchange-is-positive-locally-and-noncommutative-globally.md
- Exact checker: research/grothendieck/checkers/prime_reciprocal_exchange.py
- Result: research/grothendieck/results/prime_reciprocal_exchange.json
- Sequence claim: seqclaim-4e3bf75dceb09891703339ef
- Graph event: `ev-000000006114-e73b5fe6-20d8-4d25-a834-233d11c563cf`
