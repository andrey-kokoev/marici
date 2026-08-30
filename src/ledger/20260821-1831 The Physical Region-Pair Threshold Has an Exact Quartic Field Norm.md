# 1831 — The Physical Region-Pair Threshold Has an Exact Quartic Field Norm

## Elimination on the symmetry line

Let \(q\) be Entry 1827's fixed-line parameter and set \(z=t^2\).  The
unsquared stationarity relation gives the distance ratio directly.  With

\[
d^2=\frac{5+\sqrt5}{8},
\qquad
b^2=\frac{21+\sqrt5}{8},
\]

the wall sum obeys

\[
9z=d^2+\frac{b^2}{q^2}.
\]

Eliminating \(q\) against Entry 1827's quadratic produces a quadratic over
\(\mathbb Q(\sqrt5)\).  Taking its field norm gives the primitive rational
quartic

\[
\boxed{
104976z^4
-174960z^3
+94932z^2
-18540z
+1121=0.
}
\]

The physical root is isolated by

\[
0.7464<z<0.7468,
\qquad
t=-\sqrt z,
\]

where the negative sign is forced by positive internal energies in the two
partial-energy equations.

## Meaning

This quartic is not a new carrier wall.  It is the homogeneous algebraic
threshold of the logarithmic coefficient object supported on the already
existing labelled incidence

\[
g_{123}=g_{125}=0.
\]

Thus the first corrected five-site physical pinch exhibits precisely the
architecture

\[
\boxed{
\text{simple existing pair carrier}
+
\text{algebraically nontrivial coefficient threshold}.
}
\]

The quartic degree arises from eliminating the physical loop critical point
and taking the \(\mathbb Q(\sqrt5)/\mathbb Q\) norm; it is not evidence for a
quartic carrier primitive.

## Scope

This is the exact threshold on the frozen homogeneous regular-pentagon slice.
It does not provide the multivariate Landau divisor, global chain activation,
or an exclusion theorem for the other six disjoint-cut profiles.

## Next falsifier

Dehomogenize the representative while preserving its labelled cut pairs and
derive the multivariate critical-value discriminant.  Test whether its support
remains the coefficient discriminant of the same two-wall incidence.  A need
for an additional incidence equation, rather than a more complicated
coefficient discriminant, would be the carrier-level failure.

## Evidence

- `research/benincasa/checkers/five_site_region_pair_threshold_polynomial.py`
- `research/benincasa/results/five-site-region-pair-threshold-polynomial.json`
- Entries 1827--1830
- allocator claim: `seqclaim-41bb23c4b6d428c1d0ae5dfa`
