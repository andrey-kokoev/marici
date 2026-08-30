# 1881 — The Surviving Triple Fold Has a Noncancelling Source Residue

## Question

Entry 1880 leaves one positive-loop-sheet, common-multiplier-sign \(A_1\)
fold, represented by

\[
g_{12}\mid g_{34}\mid g_5.
\]

Can this local singularity disappear because an uncut source denominator
vanishes or because the frozen OFPT terms cancel after taking the triple
residue?

## Exact positive-sheet box

At the surviving \(+\sqrt5\) root, exact rational interval arithmetic gives

\[
\frac{19}{10}<\frac{y_1}{-t}<2,
\qquad
1<\frac{y_3}{-t}<\frac{11}{10},
\qquad t<0,
\]

while

\[
\frac{(y_2,y_4,y_5)}{-t}
=
\left(\frac32,\frac12,\frac12\right).
\]

The inequalities are certified by evaluating the quadratic-field rational
functions for \(y_1^2/t^2\) and \(y_3^2/t^2\) on the rational isolating box;
they are not decimal root fits.

## Frozen source terms

Exactly eight of the 180 frozen five-cycle OFPT terms contain all three
active walls.  In every one, all seven uncut denominators are nonzero on the
box.  Their products have the same sign:

\[
\operatorname{sgn}
\prod_{q\notin\{q_{12},q_{34},q_5\}}q
=-1
\]

for each of the eight terms.  Therefore all eight triple-residue
coefficients have the same sign and cannot cancel in the frozen source sum.

## Narrow result

\[
\boxed{
\operatorname{Res}_{q_{12}=q_{34}=q_5=0}
\Omega_{\rm OFPT}
\neq0
\quad\text{at the surviving }D_4\text{ fold,}
}
\]

at the level of the uncut rational source coefficient.

Together with Entries 1878--1880, the survivor now satisfies:

- real positive signed loop coordinates;
- nonzero common-sign projective Landau multipliers;
- ordinary \(A_1\) nondegeneracy;
- no uncut-denominator collision;
- no cancellation among the eight frozen source terms.

This still does not manufacture the global Betti pairing.  The
Cayley--Menger measure orientation and the analytically continued relative
cycle must be retained to determine the source-normalized discontinuity.

## Consequence

The remaining candidate is no longer merely a solution of the Landau
equations.  It carries a nonzero local source residue on an existing
three-wall carrier incidence.  Any failure of physical activation must now
come from the global contour pairing, not from local algebraic cancellation.

## Durable verification

- `research/benincasa/marici-gm/src/bin/five_site_cyclic_triple_d4_source_residue.rs`
- `research/benincasa/results/five-site-cyclic-triple-d4-source-residue.json`
- allocator claim: `seqclaim-064bfc467592d3ec20c52cc8`
- epistemic event: `ev-000000002239-93d499d5-108e-4b2c-9408-c166fe2ea6cf`
