# 1836 — Generic Active-Soft Endpoints Begin at Second Normal Order

## Occurrence-resolved radial chart

The pair \((g_{123},g_{125})\) contains four distinct active edge distances.
At a soft boundary \(y_e=0\), write

\[
\ell-C_e=r n,
\qquad
r\ge0,\quad n\in S^2.
\]

If \(u\) is the unit direction toward the other focus in the same region
wall, then the active denominator has local form

\[
q=\delta+r(1+u\cdot n)+O(r^2).
\]

The physical loop measure is

\[
d^3\ell=r^2dr\,d\Omega.
\]

## Generic exceptional direction

Away from

\[
c(n)=1+u\cdot n=0,
\]

the radial quotient obeys

\[
\frac{r^2}{\delta+cr}
=
\frac r c
-\frac{\delta}{c^2}
+\frac{\delta^2}{c^2(\delta+cr)}.
\]

Therefore the first nonanalytic term is

\[
\boxed{\delta^2\log\delta.}
\]

The zeroth and first ordinary normal logarithmic grades vanish.  A generic
active-soft endpoint is visible first at second Rees order.

## Classification

The carrier object is the already existing occurrence-resolved edge-soft
radial blowup.  The new local datum is a second-Rees logarithmic coefficient,
not a new carrier stratum.

For fixed boundary geometry, the positive-multiplier exceptional direction is
also finite: if \(v\) is the other wall gradient, then

\[
n=-u-\lambda v,
\qquad
\lambda=-\frac{2u\cdot v}{|v|^2},
\]

with positivity requiring \(u\cdot v<0\).

## Polar qualification

The section

\[
c(n)=0
\]

is not covered by the generic division above.  There the linear radial
coefficient vanishes and the \(O(r^2)\) term becomes leading.  It requires a
separate weighted blowup; no conclusion about its Rees order is imported from
the generic chart.

## Next falsifier

Resolve the polar section \(n=-u\) with weights derived from the quadratic
distance expansion.  Test whether its exceptional coefficient is generated
by the existing soft Cartier/Gysin calculus or leaves a residual class.

## Evidence

- `research/benincasa/checkers/five_site_region_pair_active_soft_blowup.py`
- `research/benincasa/results/five-site-region-pair-active-soft-blowup.json`
- Entries 1834--1835
- allocator claim: `seqclaim-063a2c7081e34c9d345b5d78`
