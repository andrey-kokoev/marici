# Common-center form of the coupled rank-two cone

## Question

How should rank-two positivity be certified after one sector zeroth moment changes sign and the positive-mixture interpretation ceases to apply?

## Claim boundary

A polynomial common-center identity gives a robust coupled certificate without sector positivity. Source interval values have not been inserted.

## Total cone

Let the gamma and prime moment triples be

\[
g=(g_0,g_1,g_2),
\qquad
p=(p_0,p_1,p_2),
\]

and write

\[
A_k=g_k+p_k.
\]

The coupled determinant is

\[
D_2=A_0A_2-A_1^2.
\]

For any real center \(r\), exact completion of the square gives

\[
D_2
=
A_0\left(A_2-2rA_1+r^2A_0\right)
-
\left(A_1-rA_0\right)^2.
\]

Define the centered coupled term

\[
C_r=A_2-2rA_1+r^2A_0.
\]

Then

\[
D_2=A_0C_r-(A_1-rA_0)^2.
\]

## Sector linearity before the final square

The centered term splits linearly:

\[
C_r
=
\left(g_2-2rg_1+r^2g_0\right)
+
\left(p_2-2rp_1+r^2p_0\right).
\]

No positivity of \(g_0\) or \(p_0\) is needed. Gamma and prime contributions are combined at one common center before the final nonnegative residual is subtracted.

This is the appropriate rank-two chart after the gamma zeroth moment crosses zero.

## Optimal and rational centers

If \(A_0>0\), the optimal center is

\[
r_*=\frac{A_1}{A_0}.
\]

It annihilates the residual square:

\[
D_2=A_0C_{r_*}.
\]

For interval certification, dividing two uncertain intervals to define \(r_*\) inside the proof is unnecessary. First obtain an approximate total slope, choose a nearby rational number \(r\), and certify

\[
A_0C_r>(A_1-rA_0)^2.
\]

The identity is polynomial in the enclosed source values and the chosen rational center.

## Rank-one prerequisite

The common-center interpretation still requires

\[
A_0>0.
\]

If \(A_0<0\), the rank-one Hankel gate already fails. If \(A_0=0\), positivity forces \(A_1=0\) before \(A_2\) becomes relevant. No variance language is valid in either case.

## Relation to the sector-slope chart

When \(g_0,p_0>0\), the earlier sector-slope decomposition isolates between-sector variance. When either sector mass becomes negative, that interpretation must stop.

The common-center chart remains valid because it uses only total rank-one positivity and exact polynomial identities. It is therefore the primary coupled certificate over parameter regions crossing a sector sign change.

## Current numerical interface

The accelerated gamma backend reportedly bounds its truncation by:

- approximately \(2.858\times10^{-14}\) at \(t=0.001\);
- approximately \(1.363\times10^{-27}\) at \(t=0.08\).

Those figures are not yet outward-rounded source intervals. Once directed enclosures are available, the common-center certificate needs only bounds for

\[
A_0,
\qquad
C_r,
\qquad
A_1-rA_0.
\]

This can reduce dependency inflation relative to independently enclosing \(A_0A_2-A_1^2\).

## Exact fixture

The checker verifies:

- the arbitrary-center identity;
- linear splitting of \(C_r\) across sectors;
- a positive coupled determinant with negative gamma zeroth moment;
- stability of the certificate under replacement of the optimal center by a nearby rational center.

## Disposition

Primitive gamma--prime coupling at rank two is represented by one common-center quadratic form. The next source computation should choose a rational center from the numerical total slope and outward-enclose the three displayed quantities. Sectorwise positivity is neither required nor available across the gamma sign crossing.

## Verification

- `research/voevodsky/rank-two-common-center-coupled-cone-v1.json`
- `research/voevodsky/checkers/check_rank_two_common_center_coupled_cone.py`
- `research/voevodsky/results/rank_two_common_center_coupled_cone.json`
