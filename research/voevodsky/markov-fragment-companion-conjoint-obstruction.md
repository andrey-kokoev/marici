# Companion and conjoint obstruction in the Markov fragment

## Question

Is the strict scalar Markov partial double category already an equipment?

## Claim boundary

This packet audits companions and conjoints for the fragment's current horizontal and vertical arrow classes. It does not rule out an enlarged equipment with additional horizontal gauge correspondences.

## Current arrow classes

A horizontal arrow is a seam-compatible chain extension or contiguous inclusion. Its underlying action changes the ordered vertex interval unless it is the empty extension, which is the horizontal identity.

A vertical arrow on a fixed chain is a vertex-sign gauge isometry

\[
f_\varepsilon:G\to D_\varepsilon GD_\varepsilon.
\]

For nonconstant \(\varepsilon\), this changes at least one edge sign and is not the identity Green isometry.

## Obstruction

A companion of \(f_\varepsilon:A\to B\) must be a horizontal arrow \(f_*:A\rightsquigarrow B\), equipped with unit and counit squares satisfying the companion identities. In the current horizontal class, an arrow between chains with the same ordered vertex set can add no vertices or edges. It is therefore the empty extension and acts as the identity on the full Gram certificate.

If \(f_\varepsilon\) is nontrivial, then

\[
D_\varepsilon GD_\varepsilon\ne G.
\]

The empty extension cannot have target certificate \(D_\varepsilon GD_\varepsilon\), so the required horizontal arrow is absent before the unit and counit equations are considered. The conjoint obstruction is identical in the reversed horizontal direction.

Only the all-positive gauge has the horizontal identity as both companion and conjoint.

## Hostile fixture

For one edge \(a=1/2\) and signs \((1,-1)\),

\[
\begin{pmatrix}1&1/2\\1/2&1\end{pmatrix}
\longmapsto
\begin{pmatrix}1&-1/2\\-1/2&1\end{pmatrix}.
\]

The only same-length horizontal extension is identity and cannot connect these certificates.

## Disposition

The scalar Markov structure is a strict partial double category but not an equipment under its current arrow signature. An equipment extension must add a separately typed horizontal gauge-correspondence class and prove its unit, counit, triangle, interchange, and completion laws. Relabelling a vertical gauge as an existing horizontal extension is prohibited.

## Verification

- `research/voevodsky/checkers/check_markov_companion_conjoint_obstruction.py`
- `research/voevodsky/results/markov_companion_conjoint_obstruction.json`
