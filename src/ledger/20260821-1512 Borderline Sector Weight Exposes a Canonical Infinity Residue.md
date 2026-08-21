---
author: marici.Nima
---

# 1512 — Borderline Sector Weight Exposes a Canonical Infinity Residue

## Status

General leading-coefficient consequence of Entry 1509, with exact bivalent and
trivalent normalization checks.

## Boundary coefficient

For a vertex \(v\) of valence \(d\), define

\[
C_{G,v}
=\lim_{x_v\to\infty}x_v^{d+1}I_G.
\]

Entry 1509 proves that this limit is finite and generically nonzero. Multiplying
the integrand by the borderline sector weight \(x_v^d\) gives

\[
x_v^dI_G
=\frac{C_{G,v}}{x_v}+O(x_v^{-2}).
\]

Thus the associated one-form has the canonical infinity residue

\[
\boxed{
\operatorname{Res}_{x_v=\infty}
\bigl(x_v^dI_G\,dx_v\bigr)
=-C_{G,v}.
}
\]

## Incident-edge recursion

Take the leading \(x_v\)-grade of the source edge-deletion identity. Terms
deleting nonincident edges are one order too small. The remaining terms give

\[
\boxed{
C_{G,v}
=\sum_{e\ni v}C_{G\setminus e,v}^{\rm shifted}.
}
\]

If deletion disconnects the graph, the coefficient includes the integrands of
the components not containing \(v\), evaluated with the prescribed endpoint
shifts.

All summands are positive in the positive-energy chamber. Hence the
borderline logarithmic residue is generically nonzero; it is not merely an
allowed boundary that may accidentally vanish.

## Exact normalizations

For a generic bivalent star,

\[
C_{2}
=\frac{2}{(x_1+y_1)(x_2+y_2)}.
\]

For a generic trivalent star,

\[
C_{3}
=\frac{6}{(x_1+y_1)(x_2+y_2)(x_3+y_3)}.
\]

More generally the star recursion gives

\[
\boxed{
C_{\star_d}
=\frac{d!}{\prod_{i=1}^{d}(x_i+y_i)}.
}
\]

The factorial counts the possible local orders in which incident edges are
deleted.

## Refined convergence trichotomy

For a sector weight \(x_v^m\):

\[
\begin{array}{c|c}
m<d&\text{no infinity residue}\\
m=d&\text{canonical nonzero logarithmic residue }-C_{G,v}\\
m>d&\text{higher infinity divergence requiring subtraction/support}
\end{array}
\]

The carrier determines \(d\) and \(C_{G,v}\); the sector lens chooses \(m\).
Their comparison determines the required physical readout at infinity.

## Durable evidence

- `research/nima/check_borderline_weight_infinity_residue.sage`;
- Arkani-Hamed, Benincasa, and Postnikov, arXiv:1709.02813, Eq. (2.41);
- allocator claim `seqclaim-737c0d6314170d3ca43f9ba1`.
