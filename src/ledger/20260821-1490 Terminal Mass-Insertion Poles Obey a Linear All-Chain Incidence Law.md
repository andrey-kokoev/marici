---
author: marici.Nima
---

# 1490 — Terminal Mass-Insertion Poles Obey a Linear All-Chain Incidence Law

## Status

All-chain carrier theorem obtained by combining the connected-subgraph facet
rule for cosmological-polytope integrands with the elementary interval
combinatorics of a path. Entries 1479 and 1488 provide independent direct
source derivations at two and three insertions.

## Path notation

Consider

\[
x_1--w_1--\cdots--w_r--x_2
\]

with common edge energy \(y\), and put

\[
W_{a:b}=\sum_{i=a}^{b}w_i,
\qquad
W_{a:b}=0\quad(a>b).
\]

A connected subgraph of a path is an interval. A denominator depends on the
terminal variable \(w_r\) exactly when its interval contains that vertex.

## Complete terminal list

For every \(1\le a\le r\), the intervals beginning at \(w_a\) and ending at
\(w_r\) or \(x_2\) give

\[
w_r+W_{a:r-1}+2y,
\qquad
w_r+W_{a:r-1}+x_2+y.
\]

The two intervals beginning at \(x_1\) give

\[
w_r+x_1+W_{1:r-1}+y,
\qquad
w_r+x_1+W_{1:r-1}+x_2.
\]

Therefore the terminal pole count is

\[
\boxed{N_r^{\rm terminal}=2r+2.}
\]

After removing \(w_r\), the positive shifts are precisely

\[
\boxed{
\begin{aligned}
\mathcal L_r={}&
\{W_{a:r-1}+2y,\ W_{a:r-1}+x_2+y:1\le a\le r\}\\
&\cup
\{x_1+W_{1:r-1}+y,\ x_1+W_{1:r-1}+x_2\}.
\end{aligned}
}
\]

## Verification

The combinatorial checker enumerates all connected intervals containing
\(w_r\) and verifies equality with this formula, together with the count
\(2r+2\), for \(1\le r\le100\). At \(r=1,2,3\) it reproduces the pole counts
\(4,6,8\) from the independently derived rational integrands.

## Meaning

The time-order expansion contains \(3^{r+1}\) propagator-state words before
chamber expansion, but its terminal carrier support grows only linearly:

\[
\boxed{
\text{exponential presentation complexity}
\longrightarrow
\text{linear connected-incidence support}.
}
\]

This cleanly separates carrier and coefficient complexity. The carrier
supplies the \(2r+2\) allowed nested subpath poles; the numerator and Kummer
pushforward decide which higher-weight combinations of those poles survive.

## Scope

The theorem identifies allowed terminal poles. It does not prove that every
residue is nonzero after the de Sitter weight, nor that all iterated symbol
letters remain within the same list. Entries 1483–1484 show that numerator
cancellations can make the realized coefficient alphabet strictly smaller.

## Durable evidence

- `research/nima/check_all_mass_insertion_terminal_poles.py`;
- `research/nima/derive_mass_insertion_path_integrand.sage`;
- `research/nima/check_three_mass_insertion_first_pushforward.sage`;
- Arkani-Hamed, Benincasa, and Postnikov, arXiv:1709.02813;
- Benincasa, arXiv:1909.02517;
- allocator claim `seqclaim-41682c72e4400c0b85b86252`.
