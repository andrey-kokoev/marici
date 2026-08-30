# 1859 — Correction: Active-Soft Support Is a Radial Equality, Not a Triangle Wall

## Surviving calculation

Entry 1858 correctly derives

\[
\begin{array}{c|c}
y_2=0&y_4=y_3+y_5\\
y_3=0&y_5=y_2+y_4\\
y_4=0&y_2=y_3+y_5\\
y_5=0&y_3=y_2+y_4.
\end{array}
\]

These are exactly the conditions obtained by imposing one soft radial distance
and the two active region-wall equations.

## Withdrawn interpretation

At (y_2=0), for example, the loop point equals the center (C_2), while

\[
y_3=|C_2-C_3|,
\quad
y_4=|C_2-C_4|,
\quad
y_5=|C_2-C_5|.
\]

These three lengths are radial distances from one point to three different
centers.  They are not the side lengths of a single triangle.  Therefore

\[
y_4=y_3+y_5
\]

does not by itself imply collinearity, triangle saturation, or vanishing of a
three-center Gram determinant.

Entry 1858's triangle/Gram classification is withdrawn.

## Correct support typing

The active-soft locus is exactly

\[
\boxed{
\text{one labelled edge-soft divisor}
\cap
\text{the two existing active region walls}
\cap
\text{the positive radial-distance chamber}.
}
\]

The displayed radial equality is the metric expression of that existing
triple intersection after eliminating (t); it is not an independently
derived carrier divisor.

Thus active-soft collision remains nongeneric on the edge-soft divisor, but
no Gram or triangle wall has been established.

## Next falsifier

Restrict the exact ten-term source coefficient to one active-soft triple
intersection and determine its numerator zeros and remaining denominator
poles.  Classify numerator zeros as coefficient cancellation, not carrier
support.

## Evidence

- `research/benincasa/checkers/five_site_region_pair_active_soft_radial_correction.py`
- `research/benincasa/results/five-site-region-pair-active-soft-radial-correction.json`
- Entries 1836, 1854, and 1858
- allocator claim: `seqclaim-268dedc1f1b10cb31a7efd9a`
