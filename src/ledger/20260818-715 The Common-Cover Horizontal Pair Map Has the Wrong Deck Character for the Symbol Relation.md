---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 715 — The Common-Cover Horizontal Pair Map Has the Wrong Deck Character for the Symbol Relation

## Common cover

Entry 713 identifies

\[
R=\frac{\Delta_{23}^-}{\Delta_{23}^+}
=\frac{\ell_2\ell_3}{\ell_1\ell_4},
\qquad \rho^2=R,
\]

as the common splitting cover for the signed pair systems and the mixed
triple normal quadratic.

## Horizontal comparison

For rank-one quadratic Kummer lines, a scalar comparison between the minus
and plus systems is horizontal only when its logarithmic derivative is

\[
\frac12d\log R.
\]

Therefore the horizontal scalar on the common cover is, up to a constant,

\[
\boxed{f_{\rm hor}=\rho.}
\]

Its signed-energy exponent vector is

\[
\frac12(-1,1,1,-1),
\]

so it is unavailable as a rational function on the base and is odd under the
deck involution.

## Comparison with the symbol relation

Entry 707's weighted signed-pair relation uses

\[
\frac{C_{23}^-}{C_{23}^+}=R=\rho^2.
\]

This weight is deck-even, but its logarithmic derivative is \(d\log R\),
twice the required horizontal derivative. Hence

\[
\boxed{
\text{the polynomial symbol relation is not the horizontal pair comparison
on the common cover}.}
\]

The mismatch itself is the half-character

\[
\frac12d\log R.
\]

## Consequence

The common cover genuinely unifies the pair and triple Kummer characters,
but it does not upgrade Entry 707's weighted discriminant relation to a
Gauss--Manin morphism. The two objects differ both by horizontality and deck
character:

\[
\begin{array}{c|c|c}
&\text{weight}&\text{deck character}\\
\hline
\text{horizontal comparison}&\rho&-\\
\text{symbol relation}&\rho^2&+
\end{array}
\]

No rational horizontal map descends to the frozen base.

This does not exclude a derived extension carrying the odd character. It
excludes identification of that extension with the existing even polynomial
symbol relation.

## Evidence

- `research/benincasa/check_common_cover_pair_horizontality.py`;
- Entries 707, 709, 712, and 713;
- allocator claim `seqclaim-30c4090991068830ba9d0dd4`.

## Next falsifier

Determine whether the physical relative integration chain carries the odd
deck character needed to pair with \(f_{\rm hor}=\rho\). If it does, compute
the descended extension class. If the physical chain is deck-even, the common
cover cannot supply the missing comparison and the lower-normal route is
fully closed before any \(\mathcal Q\) test.
