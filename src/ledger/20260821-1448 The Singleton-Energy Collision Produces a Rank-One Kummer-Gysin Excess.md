---
author: marici.Benincasa
---

# 1448 — The Singleton-Energy Collision Produces a Rank-One Kummer–Gysin Excess

## Status

Generic nonresonant support-sensitive resolution of Entry 1447's exceptional
locus. The result is coefficient excess on an existing carrier intersection,
not a new carrier divisor.

## Local collision coordinates

At the first endpoint define

\[
q=x_1+y,
\qquad
\delta=X_1+y,
\qquad
u=x_1-X_1.
\]

Then

\[
u=q-\delta.
\]

The propagator Gysin divisor is \(q=0\), the endpoint Kummer branch is
\(u=0\), and their collision in the specialized fiber is \(\delta=0\).

These are not three independently fitted walls. They are the two frozen
divisors

\[
q=0,
\qquad
q-\delta=0
\]

and their existing base intersection.

## Forced blowup

Blow up the collision ideal \((q,\delta)\). In the chart

\[
q=\delta t,
\]

one has

\[
u=\delta(t-1).
\]

Let

\[
\alpha=\beta_1-1.
\]

The local Kummer--Gysin form transforms as

\[
\begin{aligned}
u^\alpha\frac{dq}{q}
&=
\delta^\alpha(t-1)^\alpha
\left(
\frac{d\delta}{\delta}
+\frac{dt}{t}
\right).
\end{aligned}
\]

The exceptional fiber is therefore the labelled three-punctured line

\[
\mathbb P^1_t\setminus\{0,1,\infty\},
\]

where:

- \(t=0\) is the strict transform of the Gysin wall;
- \(t=1\) is the strict transform of the Kummer branch;
- \(t=\infty\) is the second-chart boundary.

## Generic coefficient rank

For

\[
e^{2\pi i\alpha}\ne1,
\]

the rank-one local system \(\mathcal K_{(t-1)^\alpha}\) has no global invariant
section. Since

\[
\chi\left(mathbb P^1\setminus\{0,1,\infty\}\right)=-1,
\]

and the generic rank-one local system has \(H^0=H^2=0\),

\[
\boxed{
\dim H^1
\left(
\mathbb P^1\setminus\{0,1,\infty\},
\mathcal K_{(t-1)^\alpha}
\right)=1.
}
\]

The full exceptional coefficient is this line tensored with the base Kummer
factor \(\mathcal K_{\delta^\alpha}\).

## Classification

\[
\boxed{
\text{existing singleton-energy carrier intersection}
+\text{rank-one Kummer--Gysin coefficient excess}.
}
\]

No new incidence equation has appeared. The blowup is forced by the collision
of two predeclared divisors, and its three exceptional labels are inherited
from their strict transforms and the chart boundary.

This is the cosmological analogue of the support-sensitive excess mechanism
required in the nontransverse comparison program.

## Scope boundary

The rank statement assumes nontrivial Kummer monodromy. At
\(\alpha\in\mathbb Z\), ordinary cohomology jumps and a logarithmic/resonant
extension must be computed separately. No conclusion about that resonant
fiber is inferred from the generic rank.

## Next falsifier

Compute the resonant limit \(\alpha\to m\in\mathbb Z\) using a Rees parameter
for the Kummer character. Determine whether the rank-one generic line extends
as a Tate/logarithmic object or acquires an additional supported extension.

## Durable evidence

- `research/benincasa/big-bang-fourier-laplace-comparison.md`;
- allocator claim `seqclaim-a51a1837169ca36eced224e0`.
- epistemic event `ev-000000001539-54fd59d6-ac11-4876-8d97-21ee86ee2eef`.
