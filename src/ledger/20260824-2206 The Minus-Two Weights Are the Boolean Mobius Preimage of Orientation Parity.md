---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2206 — The Minus-Two Weights Are the Boolean Möbius Preimage of Orientation Parity

## Exact incidence transform

The overlapping subdivision piece indexed by \(S\) contains the cell indexed
by \(T\) precisely when \(S\subseteq T\). Hence its cumulative cell weight is
the Boolean zeta transform

\[
W(T)=\sum_{S\subseteq T}\mu(S).
\]

The weighted geometry requires orientation parity

\[
W(T)=(-1)^{|T|}.
\]

Boolean Möbius inversion gives uniquely

\[
\begin{aligned}
\mu(S)
&=\sum_{U\subseteq S}(-1)^{|S|-|U|}(-1)^{|U|}\\
&=2^{|S|}(-1)^{|S|}\\
&=(-2)^{|S|}.
\end{aligned}

Thus

\[
\boxed{
(-2)^{|S|}
=\zeta_{B_3}^{-1}\bigl((-1)^{|T|}\bigr)(S).
}

The factor two is not a branch multiplicity or probability odds. It is the
incidence-theoretic cost of pulling a sign character on disjoint cells back
to an overlapping Boolean cover.

## Architectural consequence

The native datum is orientation parity on the resolved cells. The signed
subdivision coefficients and their Jordan dilation are derived
presentations. This is another instance of the Marici rule that occurrence-
resolved geometry precedes coarse coefficient arithmetic.

## Evidence

- Entry 2205
- Benincasa–Dian equation (4.69), using the binomial identity at (4.70)
- `research/benincasa/checkers/boolean_mobius_orientation.rs`

