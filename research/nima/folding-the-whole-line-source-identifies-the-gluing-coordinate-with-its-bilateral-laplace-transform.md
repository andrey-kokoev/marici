# Folding the whole-line source identifies the gluing coordinate with its bilateral Laplace transform

## Question

Does folding the explicit whole-line reflected pair source into the conservative radial double make the free gluing coordinate vanish?

## Claim boundary

No. The folding comparison is canonical and metric, but it identifies the gluing coordinate with the bilateral Laplace transform of the whole-line source. Entire vanishing therefore forces the source itself to vanish. Whole-line reflection correctly constructs the reciprocal source geometry; it does not cancel the free homogeneous tail of a nonzero source. The productive route is consequently G4 boundary-feature retention, not source cancellation.

## Canonical fold

For a whole-line source \(q\), define

\[
(\mathcal F_uq)_+(r)=q(r),
\qquad
(\mathcal F_uq)_-(r)=u q(-r),
\qquad r\ge0,
\]

with \(|u|=1\). This is unitary from \(L^2(\mathbb R)\) to \(L^2(\mathbb R_+)^{\oplus2}\). It intertwines

\[
\partial_t
\quad\text{with}\quad
\partial_r\oplus(-\partial_r),
\]

and continuity at the origin becomes the sewn wall relation

\[
(\mathcal F_uq)_-(0)=u(\mathcal F_uq)_+(0).
\]

Thus the carrier, differential, metric, and wall phase all fold without a fitted comparison.

## Folded gluing coordinate

Apply the explicit gluing functional

\[
A_z(g_+,g_-)=\ell_z(g_+)+u^{-1}\ell_{-z}(g_-).
\]

Direct substitution gives

\[
A_z(\mathcal F_uq)
=\int_0^\infty e^{-zr}q(r)\,dr
+\int_0^\infty e^{zr}q(-r)\,dr.
\]

Changing variables \(t=-r\) in the second term yields

\[
A_z(\mathcal F_uq)
=\int_{-\infty}^{\infty}e^{-zt}q(t)\,dt
=:\mathcal L_{\mathbb R}q(z).
\]

The sewing phase cancels from the coordinate exactly; it cannot be tuned to alter the result.

## Injectivity obstruction

For the superexponentially decaying completed-theta pair source, \(\mathcal L_{\mathbb R}q\) is entire. If

\[
A_z(\mathcal F_uq)=0
\]

for every \(z\), then on the seam \(z=i\xi\) the Fourier transform of \(q\) vanishes. Fourier injectivity gives

\[
q=0.
\]

Therefore no nonzero whole-line ordered-pair source can make the two free oriented Green factors equal for all parameters. The earlier negative-support source construction supplies the reciprocal half of \(q\), but does not change this injectivity result.

## Correct interpretation of the free gluing cell

The rank-one homogeneous difference is a boundary response coordinate, not an error to be cancelled universally. For the completed-theta radial source it must retain the bilateral transform and then decompose through the known source identity into wall, endpoint, and Wronskian features. Any cancellation relevant to an Evans divisor can occur only on a declared spectral locus or after coupling to nonfree arithmetic boundary data; it cannot be an entire free-source identity.

## Direction rescore

- Universal source cancellation, whether by a second half-line or whole-line reflection: 0/10.
- Canonical whole-line folding: completed as a free comparison.
- Identification of \(A_z\) with a G4 boundary feature: 10/10 and now uniquely prioritized.
- Spectral-locus cancellation after arithmetic loading: 8/10, but only after the boundary feature and full polarized block are constructed.

## Disposition

The folding map closes the free source comparison and eliminates the universal-cancellation branch. The next depth-first objective is to factor the bilateral pair transform represented by \(A_z\) through the retained wall, endpoint, Wronskian, and arithmetic G4 feature carrier, with no scalarization before the full jet family. No RH conclusion is authorized.
