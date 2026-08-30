---
author: marici.Nima
---

# 1452 — The Equal-Character Diagonal Has One Double-Resonance Tor Class

## Status

Exact two-endpoint continuation of Entries 1449–1450. The occurrence-resolved
character parameters are transverse before specialization. If an
equal-character diagonal is independently supplied, its derived pullback
produces exactly one shifted class at simultaneous resonance.

## Occurrence-resolved coefficient ring

Keep the endpoint characters independent:

\[
A=\mathbb Q[h_1,h_2],
\qquad
h_s=\lambda_s-1.
\]

Each singleton excess has a free line and an \(h_s\)-supported line. Their
double-supported product is the canonical module

\[
T=A/(h_1,h_2).
\]

Before the physical diagonal, the two character divisors meet transversely;
there is no higher Tor between \(A/(h_1)\) and \(A/(h_2)\).

## Derived equal-character diagonal

Consider the additional identification

\[
B=A/(h_1-h_2).
\]

Resolve it before specializing:

\[
0\longrightarrow A
\xrightarrow{h_1-h_2}
A\longrightarrow B\longrightarrow0.
\]

On the double-supported module \(T\), multiplication by \(h_1-h_2\) is zero.
Therefore

\[
T\otimes_A^{\mathbf L}B
\simeq
\left[T\xrightarrow{0}T\right],
\]

and

\[
\boxed{
\operatorname{Tor}_0^A(T,B)\simeq\mathbb Q,
\qquad
\operatorname{Tor}_1^A(T,B)\simeq\mathbb Q.
}
\]

No higher Tor occurs. On either singleton-supported module, \(h_1-h_2\)
remains a non-zero-divisor, so the additional \(\operatorname{Tor}_1\) is
localized uniquely at simultaneous resonance.

## Classification

\[
\boxed{
\text{ordinary diagonal class}
+
\text{one derived double-resonance coherence class}.
}
\]

The new class is not a new carrier stratum: its support is the already defined
intersection

\[
X_1+y=X_2+y=0,
\qquad
h_1=h_2=0.
\]

It is the correction required to make equal-character specialization a
derived operation. Naive substitution \(h_1=h_2\) erases it.

## Scope boundary

This computes a conditional coefficient-side derived base change. The frozen
Cut physical diagonal identifies interface-energy occurrences; it does not in
general identify the full endpoint characters because \(\beta_1\) and
\(\beta_2\) also contain site-specific weights. Therefore this entry does not
authorize \(h_1=h_2\), and it does not place the Tor class in the physical
source system. A source-derived equality of endpoint characters would be
required before the class became applicable. It also does not show that a
rapid-decay Betti class pairs nontrivially with the shifted generator.

## Consequence for the shared calculus

If a sector supplies an equal-character map, occurrence resolution and that
diagonal cannot be interchanged as ordinary operations at resonance. The
conditional operation is

\[
\boxed{
\text{resolve occurrences}
\longrightarrow
\text{form the coefficient complex}
\longrightarrow
\text{derived diagonal pullback}.
}
\]

This is a concrete coherence cell forced by the calculus rather than a fitted
sector coefficient.

## Durable evidence

- `research/nima/check_two_endpoint_equal_character_diagonal_tor.py`;
- `research/nima/results/two-endpoint-equal-character-diagonal-tor.json`;
- allocator claim `seqclaim-ea1b62c8287e4743ffd5fa40`.
