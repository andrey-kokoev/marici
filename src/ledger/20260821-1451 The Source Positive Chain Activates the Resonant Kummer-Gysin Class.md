---
author: marici.Benincasa
---

# 1451 — The Source Positive Chain Activates the Resonant Kummer–Gysin Class

## Status

Exact local physical pairing for Entries 1448 and 1450. The source's positive
site-weight chain and analytic regularization select a nonzero generic excess
period and a nonzero resonant logarithmic finite part.

## Local source chain

At the first singleton collision set

\[
u=x_1-X_1,
\qquad
\delta=X_1+y,
\qquad
\alpha=\beta_1-1.
\]

The source site-weight occurrence has

\[
u\in\mathbb R_+.
\]

The Gysin denominator is

\[
x_1+y=u+\delta.
\]

All other factors in the two-site universal integrand are regular and nonzero
at a generic point of \(\delta=0\). Freezing them to their corner value reduces
the singular part of the physical pairing to

\[
J_\alpha(\delta)
=
\int_0^\infty
\frac{u^\alpha}{u+\delta}du.
\]

## Exact Euler--Mellin period

For \(-1<\operatorname{Re}\alpha<0\), substitution \(u=\delta v\) gives

\[
\begin{aligned}
J_\alpha(\delta)
&=
\delta^\alpha
\int_0^\infty\frac{v^\alpha}{1+v}dv\\
&=
\frac{\pi}{\sin\pi(\alpha+1)}\delta^\alpha\\
&=
-\frac{\pi}{\sin\pi\alpha}\delta^\alpha.
\end{aligned}
\]

The primary source already admits analytic continuation of its Mellin
parameters, so this formula defines the same period outside the convergence
strip. The energy-space \(i\epsilon\) prescription fixes the branch of
\(\delta^\alpha\).

For generic nonintegral \(\alpha\), the coefficient is nonzero. Therefore the
source positive chain pairs nontrivially with Entry 1448's rank-one exceptional
Kummer--Gysin line.

## Resonant finite part

Write

\[
\alpha=m+s,
\qquad m\in\mathbb Z.
\]

Then

\[
-\frac{\pi}{\sin\pi(m+s)}
=
(-1)^{m+1}
\left(\frac1s+O(s)\right)
\]

and

\[
\delta^{m+s}
=
\delta^m
\left(1+s\log\delta+O(s^2)\right).
\]

Consequently

\[
\boxed{
J_{m+s}(\delta)
=
(-1)^{m+1}\delta^m
\left(
\frac1s+\log\delta+O(s)
\right).
}
\]

Subtracting the analytic-regularization pole can change a local polynomial
finite term. It cannot remove the coefficient of

\[
\delta^m\log\delta.
\]

Thus Entry 1450's resonant torsion class is physically activated by the
source chain: its dual period is the logarithmic finite part.

## Classification

\[
\boxed{
\text{existing singleton-energy support}
+
\text{source-selected logarithmic Kummer--Gysin coefficient}.
}
\]

No additional physical current was chosen by hand. The positive ray,
\(i\epsilon\) branch, and analytic regularization all come from the frozen
cosmological integral.

This is stronger than an associated-grade existence result: the physical
period pairing is nonzero. It remains local to a generic point of the
singleton-energy divisor.

## Next falsifier

At the double collision

\[
X_1+y=0,
\qquad
X_2+y=0,
\]

compute the two-variable positive-chain period and determine whether it is the
tensor/Koszul assembly of the two singleton logarithmic classes or carries a
new extension between them.

## Durable evidence

- `research/benincasa/big-bang-fourier-laplace-comparison.md`;
- allocator claim `seqclaim-b7d9dcaa2ad794ada499da92`.
- epistemic event `ev-000000001545-d7f25643-478a-4e66-a209-136a31eded16`.
