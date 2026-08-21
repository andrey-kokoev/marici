---
author: marici.Nima
---

# 1544 — Characteristic Two Turns the Deck Projector into a Nilpotent Extension

## Status

Exact coefficient-change audit of the trace/transfer packet in Entry 1543.

## Rational coefficients

Over \(\mathbb Q\), the order-two deck action splits:

\[
\frac{1+\sigma}{2}
\qquad\text{and}\qquad
\frac{1-\sigma}{2}
\]

project onto invariant and anti-invariant cycle lines. The normalized
specialization satisfies \(ST=1\).

## Characteristic two

Over \(\mathbf F_2\), define the norm

\[
N=1+\sigma.
\]

For the same swap matrix,

\[
\boxed{
\operatorname{rank}N=1,
\qquad
N^2=0.
}
\]

The invariant and anti-invariant vectors coincide because

\[
\begin{pmatrix}1\\-1\end{pmatrix}
=
\begin{pmatrix}1\\1\end{pmatrix}.
\]

With unnormalized transfer and trace

\[
T=\begin{pmatrix}1\\1\end{pmatrix},
\qquad
\operatorname{tr}=\begin{pmatrix}1&1\end{pmatrix},
\]

their composition is

\[
\boxed{\operatorname{tr}T=2=0.}
\]

There is no normalized idempotent projector because \(2\) is not invertible.

## Meaning

The carrier, its two-sheet deck action, and the underlying cycle pair are
unchanged. What changes is the coefficient realization:

\[
\boxed{
\begin{array}{c|c}
\mathbb Q & \text{semisimple trace/anti-trace splitting}\\
\mathbf F_2 & \text{non-split nilpotent norm extension}
\end{array}
}
\]

This is an exact demonstration of shared carrier calculus with
sector-specific coefficient behavior. The coefficient ring determines
whether physical descent is a direct-summand projection or a derived
extension.

It also supplies a warning for arithmetic interpretations: reducing a
rational physical projector modulo a prime dividing the deck order changes
its categorical type; it is not ordinary specialization of an idempotent.

## Durable evidence

- research/nima/check_supercritical_infinity_jet.sage;
- Entry 1543;
- allocator claim seqclaim-d180e15e1c00b5ecf99981b1.
