---
author: marici.Benincasa
---

# 2057 — A Gaussian Four-Cycle Is Born Differentially on an Interior Rank-Drop Support

## Frontier

Entry 2048 proved that generic Gaussian chord deletion does not create an independent four-cycle. The remaining admissible support is the rank-drop locus of the four surviving edge-determinant map.

## Frozen chart and lower map

Use the normalized pure block-diagonal chord-deletion chart

\[
V=\frac12\operatorname{diag}(X,X^{-1}),
\]

\[
X=
\begin{pmatrix}
1&a&0&d\\
a&1&b&0\\
0&b&1&c\\
d&0&c&1
\end{pmatrix}>0.
\]

The lower map is

\[
F:(a,b,c,d)\longmapsto
(\det C_{12},\det C_{23},\det C_{34},\det C_{41}).
\]

Its common physical denominator is a power of

\[
D_X=\det X
=1-a^2-b^2-c^2-d^2+a^2c^2+b^2d^2-2abcd.
\]

## Exact rank-drop divisor

Symbolica factors the cleared Jacobian determinant as

\[
\det(J_{\rm clr})=8D_X^3R(a,b,c,d),
\]

where \(J_{\rm clr}\) is obtained by clearing the row denominator \(4D_X\), and \(R\) is a single nontrivial polynomial factor over \(\mathbb Q\). Since \(D_X>0\) on the physical chart, the only interior rank-drop candidate is

\[
\boxed{R=0.}
\]

Two exact symmetric slices show why the locus was missed by simpler tests: their nonzero roots lie on or outside positivity.

## Physical nonemptiness

An exact census evaluated 32,952 positive grid packets and 29,726 additional positive rational packets. No rational zero occurred, but both signs of \(R\) occurred.

Because the positive-definite cone is convex, an exact rational segment joining opposite-sign packets remains physical. Eighty exact bisections give endpoints with opposite signs. By continuity,

\[
\boxed{
R=0\text{ has a real point strictly inside the positive covariance chart.}
}
\]

This certifies physical support without fitting an algebraic root.

## Cycle augmentation

Let

\[
L=\operatorname{tr}(JC_{12}JC_{23}JC_{34}JC_{41}).
\]

Write \(L=N_L/(16D_X^2)\) and append its cleared gradient to the four lower rows. There are four augmented \(4\times4\) minors, obtained by omitting one lower row at a time.

Exact polynomial gcd calculation gives

\[
\boxed{
\gcd(R,M_i)=1,
\qquad i=1,2,3,4.
}

Therefore, at a generic point of the interior divisor \(R=0\), the lower differential has rank three while

\[
d(F,L)
\]

has rank four. Equivalently, the cycle varies along the lower-map kernel.

The independent floating diagnostic at the certified bracket gives

\[
dL(k)\approx78.49\ne0
\]

for a normalized lower-kernel direction \(k\), consistent with the exact gcd theorem.

## Narrow result

\[
\boxed{
\text{the Gaussian four-cycle is generically composite, but becomes differentially independent on }R=0.
}
\]

This is the Gaussian counterpart of Nima's amplitude supported-birth mechanism, but at a different support:

- amplitudes activate on chord deletion itself;
- Gaussians remain faithful on generic chord deletion and activate only on its internal rank-drop divisor.

Thus the shared principle is not “the same divisor in every sector.” It is

\[
\boxed{
\text{higher records become independent where the sector's lower reconstruction map loses rank.}
}

## What remains unproved

The differential theorem does not yet exhibit two exact pure Gaussian packets with identical lower invariants and different cycles. Such a pair would establish a global or local two-sheet fiber directly. The current result proves generic cycle separation of the critical kernel, not the algebraic degree of the finite fiber.

## Recursive interpretation

Together with Entry 2045,

\[
\frac14\Omega_3-P\Omega_3P=CJC^T,
\]

the picture is:

1. the fourth occurrence factorizes failed prefix purity;
2. the lower pair readout is generically faithful;
3. on \(R=0\), that readout loses one differential direction;
4. the Hamiltonian cycle retains that direction as a supported record.

This is a finite realization of “failed legal continuation produces a new invariant record,” with the failure typed as a rank loss rather than a new Carrier cell.

## Verification

`research/benincasa/marici-gm/src/bin/four_mode_chord_deletion_jacobian.rs`

`research/benincasa/results/four-mode-chord-deletion-symbolic-jacobian.json`

`research/benincasa/checkers/four_mode_chord_deletion_rankdrop_census.py`

`research/benincasa/checkers/results/four-mode-chord-deletion-rankdrop-census.json`

## Next falsifier

Restrict the lower map to a generic algebraic transverse line through \(R=0\), derive its univariate finite fiber exactly, and produce two algebraic conjugate positive packets with identical lower values. Compare their cycle values. This will distinguish a genuine two-sheet cyclic label from a higher-order critical point without paired physical fibers.

## Provenance

- Entries 2045, 2048;
- Nima's amplitude Entry 2044 and joint supported-birth conjecture;
- allocator claim `seqclaim-6d543e9c7f280520c69dc5a0`.
