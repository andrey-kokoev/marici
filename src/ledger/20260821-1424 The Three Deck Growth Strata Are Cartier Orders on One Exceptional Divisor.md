# 1424 — The Three Deck Growth Strata Are Cartier Orders on One Exceptional Divisor

## Status

Exact exceptional-order reconstruction on Entry 1422’s two-normal blowup.

## Exceptional coefficient

On the chart

\[
w=x\tau,
\qquad
\tau=\frac zR,
\]

a non-total-energy marked wall has the form

\[
q
=
x^{-1}\frac{L(\tau,r)}{\tau}.
\]

Its inverse contributes

\[
q^{-1}
=
x\frac{\tau}{L(\tau,r)}.
\]

If the signed radial constant in (L) is nonzero, this gives one factor of (\tau) at (\tau=0). If the signed constants cancel, (L) itself contains a factor of (\tau), and the zero is removed.

Therefore the (\tau)-vanishing order of an OFPT term is exactly its loop-radial denominator-growth valuation.

## Complete sheet census

Minimizing over all (180) source terms gives

\[
\boxed{
\begin{array}{c|c|c}
\tau\text{-order}&\text{sheet count}&C_5\text{ orbit representatives}\\
\hline
2&10&5,11\\
4&20&1,3,7,15\\
9&2&0,31
\end{array}
}
\]

This exactly reproduces the independent radial valuation census retained after Entry 1343’s retraction.

## Geometric interpretation

The three deck strata are not three infinity divisors. They are three Cartier depths on the same exceptional divisor

\[
E_{x,w}\subset\operatorname{Bl}_{(x,w)}.
\]

Equivalently, the exceptional coefficient object carries the filtration

\[
F^9\subset F^4\subset F^2.
\]

The growth-four complex of Entries 1411–1423 is the middle supported grade. Orbit representatives (5,11) were absent there because they belong to order two, while uniform sheets belong to order nine.

## Consequence for the physical comparison

The physical total-energy asymptotic and the auxiliary loop-radial classes now live on one two-normal compactification, but at different levels:

- the physical form has transverse (x)-order seven;
- deck occurrence data supply (\tau)-orders two, four, and nine.

Thus the natural coefficient object is bifiltered:

\[
\boxed{
\operatorname{gr}_{x}^{7}
\operatorname{gr}_{\tau}^{\{2,4,9\}}
\mathcal V_{C_5}.
}
\]

No direct equality between these grades is implied.

## Next finite falsifier

Compute the leading exceptional coefficient on each of the three (\tau)-grades and the extension data in

\[
F^9\subset F^4\subset F^2.
\]

Do not assume canonical maps between distinct associated grades. Test whether the physical mixed-Tate coefficient (C_5) lands only in the uniform order-nine quotient or requires nontrivial extension data in the filtered object.

Artifacts:

- `research/benincasa/marici-gm/src/bin/five_site_two_normal_rees.rs`
- `research/benincasa/results/five-site-two-normal-rees.json`

Allocator claim: `seqclaim-87ef1b19df0beb65b925010d`.
