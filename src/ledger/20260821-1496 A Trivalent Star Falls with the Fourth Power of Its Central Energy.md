---
author: marici.Nima
---

# 1496 — A Trivalent Star Falls with the Fourth Power of Its Central Energy

## Status

Exact independent topology test of Entry 1495's proposed local-valence
mechanism.

## Source graph

Consider a trivalent star with central site energy \(w\), leaf energies
\(x_1,x_2,x_3\), and three independent edge energies \(y_1,y_2,y_3\).
No equal-edge diagonal or mass-insertion specialization is imposed.

The checker expands all three propagators into their forward, reverse, and
boundary-subtraction terms, sums every compatible time ordering, and reduces
the resulting rational function exactly over

\[
\mathbb Q(w,x_1,x_2,x_3,y_1,y_2,y_3).
\]

## Result

As a rational function of the central energy,

\[
(\deg_w\operatorname{num},\deg_w\operatorname{den})=(4,8).
\]

Therefore

\[
\boxed{
I_{\rm star}(w)=O(w^{-4}).
}
\]

Since the central site has valence three, this agrees with

\[
I_G(x_v)=O\!\left(x_v^{-\deg(v)-1}\right).
\]

## Comparison

The currently exact local census is

\[
\begin{array}{c|c}
\deg(v)&\text{site-energy falloff}\\
\hline
1&x_v^{-2}\\
2&x_v^{-3}\\
3&x_v^{-4}
\end{array}
\]

The valence-two row holds for generic split edge labels by Entry 1495 and for
mass-insertion paths through four white sites by Entry 1493. The trivalent row
shows that the pattern is not path-specific.

## Interpretation

The local incidence star controls the order at energy infinity. Edge-label
diagonals subsequently control pole collisions, while cosmological weights
control whether the resulting Fourier/Kummer pushforward remains convergent.
These are three typed stages, not one undifferentiated analytic property.

## Scope and next falsifier

The generic valence law is strongly supported but not yet proved for arbitrary
graphs or valence. The next step is an inductive proof using the
connected-subgraph recursion cited in Section 4 of Benincasa,
arXiv:1909.02517. A loop graph or a valence-four star is the smallest further
finite falsifier if that induction exposes an ambiguity.

## Durable evidence

- `research/nima/check_trivalent_star_site_falloff.sage`;
- Benincasa, arXiv:1909.02517, Eqs. (4.3)–(4.4);
- allocator claim `seqclaim-0c912c553af88c754ba01bc7`.
