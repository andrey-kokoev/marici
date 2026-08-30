# Six-port bilocal instrument

Work package: WP535  
Owner: marici.Figueiredo

## Question

What is the smallest source-shaped neutral-\(B_s\) lattice interface that can
consume WP534's six signed complex poles without repeating WP524's scalar
projection loss?

## Raw Ward-complete estimator

For each pole \(i=1,\ldots,6\), define four renormalized integrated-correlator
estimators using the Euclidean continuation of its exact complex kernel:

\[
H_{i,V},\qquad H_{i,RR},\qquad H_{i,LL},\qquad H_{i,RL}.
\]

They correspond to the vector left-left channel and the three scalar
bilocals required by the WP525 longitudinal-plus-Goldstone completion. The raw
packet therefore contains 24 complex estimators, or 48 real components.

The pole-resolved Ward-complete amplitude is

\[
A_i=
H_{i,V}
-\frac{
m_b^2H_{i,RR}
+m_s^2H_{i,LL}
-2m_bm_sH_{i,RL}}
{\mu_i^2}.
\]

Because each row acts on its own four estimator coordinates and contains a
unit vector coefficient, the source-generated map from 24 complex estimators
to the six \(A_i\) has exact rank six.

## Experimental collapse

The new-physics mixing amplitude is

\[
M_{12}^{\mathrm{new}}=\sum_{i=1}^6 r_iA_i.
\]

This scalar map has rank one on the six pole amplitudes and hence a
five-dimensional kernel. A hostile two-pole displacement is

\[
\delta A=(r_2,-r_1,0,0,0,0).
\]

It is nonzero but satisfies

\[
\sum_i r_i\delta A_i=0.
\]

Thus a measured \(\Delta M_s\) value cannot identify the pole decomposition.
The six-port lattice vector separates the hostile pair before experimental
compression.

## Covariance and calibration contract

An executable calculation must report the 48 real estimator components with
one \(48\times48\) covariance matrix. The covariance must include:

- nonperturbative operator mixing and coincident-point subtraction;
- correlations across all pole kernels on common gauge ensembles;
- finite-volume, continuum and heavy-quark systematics;
- threshold matching and current-normalization uncertainty;
- every admitted null mode.

The checker uses unit raw covariance only to prove that the six-port response
Gram matrix can be nonsingular. It is not a substitute for calibrated lattice
covariance.

## Physical realization and authority

The proposed instrument is six complex-kernel integrated \(B_s\) correlators,
each evaluated in four renormalized operator channels on the same ensembles.
This is an executable extension of the established bilocal integrated-
correlator architecture cited in WP523. It is not yet a realized instrument:
the bounded WP523 census found no neutral-\(B_s\) calculation publishing these
estimators and covariance.

WP535 therefore supplies an instrument specification and exact rank theorem,
not data. It neither selects the source coefficients nor identifies a UV
constructor from \(\Delta M_s\).

The smallest exact falsifier is the hostile nonzero \(\delta A\), which the
scalar readout annihilates while the six-port vector detects it.

The remaining gate is execution on common \(B_s\) lattice ensembles with the
declared renormalization, subtraction, continuum, finite-volume, heavy-quark,
threshold and covariance controls.

## Reproduction

Run uv run --offline --with sympy python
research/flavor/checkers/wp535_six_port_bilocal_instrument.py.

The generated result is
research/flavor/results/wp535_six_port_bilocal_instrument.json.
