# Executable neutral-B flavor-current instrument

## Instrument and admitted packet

WP511 uses the pinned `flavio` 2.7.0 likelihood surface with `particle` 0.25.4.
The admitted source coordinates are two real correlated WET rays at 160 GeV,

\[
(C_{VLL},C_{VRR},C_{VLR})_q=x_q(1,1,2),
\qquad q=d,s,
\]

in the `bdbd` and `bsbs` sectors. This chiral ray is fixed by the vectorlike
source-current grammar; its numerical coefficients are not fitted to the
oscillation data.

The executable observables are \(\Delta M_d\) and \(\Delta M_s\). Both carry
the bundled `HFAG osc summer 2015` measurement. The code records their central
values and experimental standard deviations in the native `flavio` units.

## Common detector and theory frame

Experimental covariance alone would overstate the constraint because the
hadronic and CKM prediction uncertainties are much larger. WP511 therefore
freezes a joint `flavio.sm_covariance` transport with seed 511, 200 draws, and
one worker. The detector metric is the inverse of the sum of this theory
covariance and the experimental covariance.

The resulting covariance is positive definite and retains its off-diagonal
theory correlation. No diagonalization, nuisance removal, or normalization is
fitted from a desired source answer.

## Exact local response rank

A symmetric source perturbation gives the local Jacobian

\[
J_B=
\begin{pmatrix}
0.33957858&0\\
0&0.67615136
\end{pmatrix}.
\]

The zeros are executable cross-sector zeros: the `bsbs` coefficient does not
change \(\Delta M_d\), and the `bdbd` coefficient does not change
\(\Delta M_s\). The detector-weighted Gram

\[
G_B=J_B^TV^{-1}J_B
\]

is positive definite with nonzero determinant. Hence the physical instrument
is locally faithful on the two-real-coordinate packet.

The frozen local Gaussian readout is

\[
\widehat x_d=-3.5658\mathbin{\cdot}10^{-14}\ \mathrm{GeV}^{-2},
\qquad
\sigma_d=6.5467\mathbin{\cdot}10^{-14}\ \mathrm{GeV}^{-2},
\]

\[
\widehat x_s=4.0675\mathbin{\cdot}10^{-13}\ \mathrm{GeV}^{-2},
\qquad
\sigma_s=7.4231\mathbin{\cdot}10^{-13}\ \mathrm{GeV}^{-2}.
\]

Their coefficient correlation is approximately 0.56624. These are local
Gaussian instrument coordinates under the frozen theory sampler, not a global
model exclusion.

## Redundant ratio and contextual partition

The registered \(\Delta M_d/\Delta M_s\) response obeys the quotient chain
rule from the two primary observables. Appending it leaves the response rank
equal to two. Treating it as an independent third source direction would
double-count the underlying oscillation information unless a distinct joint
experimental covariance were supplied.

Relative to \((x_d,x_s)\), contextual equivalence classes are locally
singletons: the two calibrated ports separate the two real current directions.
This repairs the CP-even instrument gap that remained in the kaon-only
likelihood.

## Source and pole boundary

The instrument constrains realized low-energy current coefficients; it does
not select them or the WP510 dimensionless source coefficients. The missing
constructor is the common-vacuum mass-basis map from the dynamical messenger
Yukawas into \((x_d,x_s)\). WP450 allows arbitrary Yukawa coefficients and
therefore does not yet freeze that orientation.

The zero-momentum mixing experiment also sums over the heavy poles. It cannot
separate the individual WP509 residues or widths even though those quantities
are independently source-frozen. A distinct on-shell pole instrument remains
necessary for spectral tomography.

The smallest falsifier is a vanishing diagonal response, a rank-deficient
calibrated covariance, or an upstream source map that identifies the two WET
coordinates before they reach the detector.
