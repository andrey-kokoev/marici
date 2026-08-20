---
title: "Dimensional Continuation Collapses the Four-Site Vanishing Sphere to Its Equator"
date: 2026-08-20
entry: 1170
status: active-stop-condition
sector: cosmology
---

# 1170 — Dimensional Continuation Collapses the Four-Site Vanishing Sphere to Its Equator

Sequence claim: `seqclaim-490c37fafa03c2ab5c4ca222`.

## Frozen dimensional measure

Let

\[
m=d-3
\]

be the dimension transverse to the span of three generic external spatial
momenta. After radializing the transverse coordinates and writing
\(K=\omega^2\), the source-normalized local measure contains

\[
\boxed{
\frac{K^{m/2-1}}{\Gamma(m/2)}\,dK.
}
\]

No sheet orientation is added to this density.

## Distributional physical limit

For a polynomial test function

\[
\varphi(K)=\sum_{j\ge0}a_jK^j
\]

on a bounded radial interval,

\[
\frac1{\Gamma(\epsilon)}
\int_0^1K^{\epsilon-1}\varphi(K)\,dK
=
\frac1{\Gamma(\epsilon)}
\sum_{j\ge0}\frac{a_j}{\epsilon+j},
\qquad \epsilon=\frac m2.
\]

Since \(1/\Gamma(\epsilon)=\epsilon+O(\epsilon^2)\),

\[
\boxed{
\lim_{d\to3}
\frac{K^{(d-3)/2-1}}{\Gamma((d-3)/2)},dK
=\delta(K).
}
\]

Thus dimensional continuation reproduces the physical support
\(K=\omega^2=0\): the equator identified in Entry 1169.

## Deck and chain typing

Because the pushforward depends only on \(K=\omega^2\), it is the even trace
under

\[
\omega\longmapsto-\omega.
\]

The distribution determines an equatorial current. It does not determine an
oriented relative chain filling that equator through either hemisphere, nor
does it canonically glue the two fills into a primitive \(S^3\) generator.

Therefore

\[
\boxed{
\text{dimensional regularization selects the equatorial distribution,}
\quad
\text{not an integral vanishing-sphere generator.}
}
\]

## Narrow conclusion

Under the frozen source prescription:

- the threefold-node coefficient line exists;
- the literal physical chain reaches its equator;
- dimensional continuation canonically yields \(\delta(K)\);
- integral activation of the vanishing \(S^3\) remains unselected.

This closes the proposed dimensional-continuation shortcut. It does not
prove that every future physical construction pairs trivially with the
vanishing cycle. Reopening requires an independently normalized relative
chain or polarization that supplies the missing hemisphere gluing.

No new carrier datum is indicated.

## Next research move

Retire local integral activation of this node under the present source.
Study the global quartic-double-solid coefficient system—especially its
singular-resolution exact sequence and Picard--Lefschetz extension—without
assuming that the local vanishing line is physically selected.

## Evidence

- `research/benincasa/checkers/four_site_qg_dimensional_distribution.py`
- `research/benincasa/results/four-site-qg-dimensional-distribution.json`
- Entries 1167--1169.
