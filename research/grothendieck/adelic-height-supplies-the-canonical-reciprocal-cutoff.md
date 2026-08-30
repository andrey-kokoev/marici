# Adelic Height Supplies the Canonical Reciprocal Cutoff

## Absolute multiplicative height

For \(r\in\mathbb Q^\times\), define the normalized adelic height

\[
H(r)
=
\prod_v
\max(1,|r|_v),
\]

where \(v\) runs over the archimedean and all prime places.

The product formula gives

\[
\prod_v |r|_v=1.
\]

Therefore

\[
\begin{aligned}
H(r^{-1})
&=
\prod_v\max(1,|r|_v^{-1})\\
&=
\prod_v
\frac{\max(1,|r|_v)}{|r|_v}\\
&=
H(r).
\end{aligned}
\]

Adelic height is exactly invariant under reciprocal inversion.

## Recovery of the Euler cutoff

For a positive integer \(n\),

\[
|n|_\infty=n,
\qquad
|n|_p\leq1
\]

at every finite place. Hence

\[
H(n)=n.
\]

Consequently, the familiar Euler cutoff

\[
n\leq N
\]

is precisely the restriction of the adelic height cutoff

\[
H(r)\leq N
\]

to positive integral labels.

The reciprocal label \(1/n\) has the same height:

\[
H(1/n)=H(n)=n.
\]

## Closure of the cutoff-synchronization gate

The direct and reciprocal zero-germs therefore do not require independently
chosen regulator clocks. Their common cutoff is induced by a single
source-native function on the diagonal rational labels.

The cofinal diagonal is

\[
H(r)leq N
\quad\longmapsto\quad
igl(
H(r)leq N,
H(r^{-1})leq N
igr).
\]

Reciprocal sewing preserves this filtration exactly, not merely up to bounded
distortion.

This closes the principal ambiguity in the boundary-grade theorem. The
same-cutoff comparison is not fitted to select the critical line.

## Strengthened conditional theorem

Let a completed zero event determine nonzero direct and reciprocal leading
Euler boundary classes. Suppose theta/Tate sewing:

1. compares them through reciprocal inversion on diagonal rational labels;
2. preserves the adelic-height filtration;
3. acts by a uniformly invertible morphism on their leading boundary classes.

Then the forced comparator

\[
R_s(N)
=
\frac{s}{1-s}N^{1-2s}
\]

is uniformly invertible, and therefore

\[
\Re s=\frac12.
\]

The cutoff premise is now proved. The remaining premise is uniform
invertibility on the leading boundary class.

## What remains unresolved

A scalar functional equation may identify only the finite parts of the two
relative germs. It need not imply that the source sewing preserves their
nonzero leading boundary classes as an invertible map.

The final construction must derive this boundary action from the full
theta/Tate correspondence. In particular, it must show that completion does
not:

- quotient out the leading Euler class;
- mix it with primitive or square currents of another grade;
- replace it by a noninvertible correspondence;
- retain only the scalar finite part.

## Hostile multiplier test

An off-line symmetric multiplier preserves scalar reciprocity and the adelic
height function. It can survive only by breaking invertibility or provenance
of the leading boundary-class comparison.

This sharply identifies where the hostile factor must fail: not at the cutoff,
not at scalar symmetry, but at the source action on the associated graded
boundary object.

## Explanatory gain

The two reciprocal sectors really do share one clock. It is the adelic height,
and its invariance is a consequence of the product formula.

The half-line is selected because a reversible comparison of two boundary
meanings, measured at the same adelic resolution, is neutral only at
\(\Re s=1/2\).

