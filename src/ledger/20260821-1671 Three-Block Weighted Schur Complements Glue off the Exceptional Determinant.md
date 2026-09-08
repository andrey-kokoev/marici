# 1671 — Three-Block Weighted Schur Complements Glue off the Exceptional Determinant

## Overlap falsifier

Entry 1670 identifies the coefficient-Rees direction required by singular
two-block conditioning. Test whether nested three-block conditioning creates an
overlap obstruction on the generic weighted chart.

Use

\[
\Sigma(t)=
\begin{pmatrix}
a&tx&ty\\
tx&t^2b&t^2z\\
ty&t^2z&t^2d
\end{pmatrix}.
\]

When

\[
\Delta_E=bd-z^2\ne0,
\]

joint conditioning on the last two blocks gives

\[
S_{m joint}
=a-\frac{dx^2-2zxy+by^2}{bd-z^2}.
\]

Eliminating the (b)-block first gives

\[
a-\frac{x^2}{b}
-
\frac{(y-xz/b)^2}{d-z^2/b},
\]

while eliminating the (d)-block first gives

\[
a-\frac{y^2}{d}
-
\frac{(x-yz/d)^2}{b-z^2/d}.
\]

Exact reduction identifies both expressions with (S_{m joint}).

The checker verifies 854 invertible exceptional blocks, 93,638 positive
covariance families, and 187,276 elimination-order comparisons.

## Narrow result

\[
\boxed{
\text{weighted three-block Gaussian conditioning has no generic overlap obstruction.}
}
\]

The coefficient-Rees charts glue by ordinary Schur-complement transitivity.
No supported secondary class and no new carrier incidence appears away from

\[
\Delta_E=bd-z^2=0.
\]

This result does not extend through that determinant locus, where the
exceptional covariance block itself becomes singular.

## Durable artifacts

- `research/benincasa/checkers/three_block_weighted_schur_overlap.rs`
- `research/benincasa/results/three-block-weighted-schur-overlap.json`
- `research/benincasa/three-block-weighted-schur-overlap.md`

## Next falsifier

Resolve the rank-one exceptional block (bd-z^2=0). Determine whether
positivity forces the cross vector ((x,y)) into its image and whether the
resulting Moore--Penrose/relative Schur limit is intrinsic on the labelled
rank-one stratum. If a further approach ratio is required, identify its
weighted coefficient chart without adjoining a carrier cell.