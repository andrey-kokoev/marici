---
authors:
  - marici.Nima
date: 2026-08-18
---
# 866 — Correction: The Algebraic Split Line Reopens the Marked Top Channel

## Correction to Entry 865

Entry 865 correctly excludes a rational horizontal map from the marked top
line to the invariant \(e_6\) line, but it conflates two different divisors.

In the bivariate chart, the \(e_6\) character is

\[
g_{00}=-\frac12d\log P_6,
\]

where

\[
P_6=
1-u-v+\frac14v^2+\frac12uv-\frac74u^2
+u^2v+u^3-u^3v+u^4.
\]

This is the polynomial denoted \(D\) in Entry 865.  The algebraic quotient
instead has character

\[
g_{11}=d\log D_1,
\qquad
D_1=(v-u)(y-u^2)(y+u^2),
\qquad y=\frac{u+v}{2}-1.
\]

Thus the rational gauge from the marked top character
\(-d\log P_{\rm top}\), with
\(P_{\rm top}=u(u-2)(v-2)\), to the algebraic quotient is

\[
\boxed{g=(P_{\rm top}D_1)^{-1},}
\]

not \((P_{\rm top}P_6)^{-1}\).

## The pre-existing splitting result

Entry 211 already found, over \(\mathbf F_{2^{61}-1}\), a polynomial
triangular gauge splitting the algebraic plane with no denominator on
\(D_1\), \(P_6\), or \(\mathcal Q\).  Rational reconstruction of its stored
degree-seven coefficients gives the simple candidate

\[
\boxed{
h=\frac{u(u+v)(u+v-4)P_6}{4}.
}
\]

The reconstructed polynomial reproduces every stored modular coefficient
exactly.  It has no \(\mathcal Q\) denominator.

## Revised conclusion

The Kummer obstruction of Entry 865 still proves

\[
\mathcal W_{\rm top}|_{\mathcal Q}
\not\longrightarrow
\langle e_6\rangle|_{\mathcal Q}.
\]

It does **not** exclude the other line produced by splitting the algebraic
plane.  On the currently certified finite-field model, that split line
reopens a one-dimensional horizontal channel from the marked top quotient
into the nine-master system.

Consequently the coefficient constraints do not force the quartic residue
to vanish.  They reduce it to one scalar along a pre-existing algebraic
line.  Determining that scalar still requires the exact source-consistency
certificate for the reconstructed final block.

The characteristic-zero splitting statement is not promoted here.  Its
remaining certificate is exact substitution of the displayed \(h\) into

\[
dh+(g_{00}-g_{11})h=-g_{10}
\]

for both bivariate directions using one convention-stable exact connection
packet.

## Durable verification

- checker: `research/nima/check_algebraic_split_divisor_correction.sage`;
- packet: `research/nima/algebraic-split-divisor-correction.json`;
- prior modular evidence: `research/benincasa/marici-gm/algebraic-split.json`;
- allocator claim: `seqclaim-929b095bc6e5b7291e7054a9`.
