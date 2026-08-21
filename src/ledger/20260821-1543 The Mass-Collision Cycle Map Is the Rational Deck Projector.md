---
author: marici.Nima
---

# 1543 — The Mass-Collision Cycle Map Is the Rational Deck Projector

## Status

Exact trace/transfer and pairing-compatibility packet for the two small cycles
of Entry 1540.

## Cycle spaces

Let

\[
V_{\rm split}
=\mathbb Q\langle\gamma_+,\gamma_-\rangle,
\qquad
V_{\rm coll}
=\mathbb Q\langle\gamma_0\rangle.
\]

The deck involution on the split fiber is

\[
\sigma=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
\]

Define transfer and specialization by

\[
\boxed{
T=
\begin{pmatrix}1\\1\end{pmatrix},
\qquad
S=\frac12
\begin{pmatrix}1&1\end{pmatrix}.
}
\]

Then

\[
\boxed{
ST=1,
\qquad
TS=\frac{1+\sigma}{2}.
}
\]

Thus \(TS\) is the idempotent projector onto the invariant trace line, and
the anti-invariant line is its kernel.

## Pairing compatibility

Let the generic small-pole residue be

\[
r=\frac1{B-A}.
\]

The generic pairing row and collided pairing scalar are

\[
R_{\rm split}=(r\;\;r),
\qquad
R_{\rm coll}=2r.
\]

They obey the exact descent square

\[
\boxed{
R_{\rm coll}S=R_{\rm split}.
}
\]

Equivalently, transferring the collided cycle and evaluating upstairs gives
the same record:

\[
R_{\rm split}T=R_{\rm coll}.
\]

## Coefficient requirement

The specialization map uses \(1/2\). Hence this splitting is canonical over
coefficients in which the deck order is invertible, such as \(\mathbb Q\), but
not as an integral direct-summand decomposition without further data.

The integral cycle pair still has an invariant sum and anti-invariant
difference; what requires rationalization is the normalized projector.

## Meaning

The physical mass collision realizes the full typed interaction contract:

\[
\boxed{
\text{deck cover}
\;\rightleftarrows\;
\text{collided carrier}
\quad+\quad
\text{compatible residue pairing}.
}
\]

The physical kernel is not fitted from scalar data. It is the
deck-anti-invariant cycle line, selected by the canonical rational
trace/transfer calculus.

## Durable evidence

- research/nima/check_supercritical_infinity_jet.sage;
- Entry 1540;
- allocator claim seqclaim-c73042278ba4ecf67720c6ee.
