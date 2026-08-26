# Continuum-volume design rank

## Question

What ensemble geometry is sufficient to identify the continuum, \(a^2\),
\(a^4\), and leading finite-volume responses of every WP541 estimator without
using flavor data to calibrate the lattice scale?

## Five-ensemble design

Use the five spacing-volume pairs

\[
(a,L)=
(1,24),\;
\left({1\over2},24\right),\;
\left({1\over3},24\right),\;
\left({1\over2},30\right),\;
\left({1\over3},30\right)
\]

in inverse-GeV units. Normalize the leading finite-volume shape at \(L=24\)
to one and write

\[
r={F(30)\over F(24)}=\exp(-6m_{\mathrm{gap}}).
\]

The QCD mass gap and scale setting are external instrument calibrations. They
are not inferred from the flavor poles or desired ratio.

For each real estimator, preregister

\[
y(a,L)=y_{\mathrm{cont}}+c_2a^2+c_4a^4+d_LF(L).
\]

The design columns are \(1,a^2,a^4,F(L)\). Exact four-row minors include

\[
{5(r-1)\over54},
\]

so the design has rank four whenever \(r\ne1\).

## Joint 48-estimator fit

WP539 supplies 48 real estimators per ensemble. Tensoring the five-by-four
design with \(I_{48}\) gives:

- 240 real observations;
- 192 fit parameters;
- exact design rank 192;
- 48 residual degrees of freedom;
- a required \(240\times240\) observation covariance.

External scale-setting and mass-gap uncertainties enter as separately
calibrated nuisance covariance. They must not be fitted from the flavor answer.

## Hostile designs

If \(r=1\), both volumes have the same finite-volume column. The per-estimator
rank falls to three, so the continuum intercept and finite-volume correction
cannot be separated.

With only two distinct spacings, the \(a^2\) and \(a^4\) columns likewise
cannot be separated and the rank is again three. Both the third spacing and
the second physical volume are therefore structural requirements.

## Renormalization contract

All five ensembles must use:

- one nonperturbative intermediate scheme for all four Ward channels;
- a common physical renormalization scale with step scaling across cutoffs;
- the full operator-mixing and coincident-point subtraction matrix;
- continuum matching across each frozen mediator threshold only after the
  common-scheme limit;
- common scale, ensemble, context, and operator covariance.

WP542 establishes identifiability, not measured calibration. The gauge
ensembles and bilocal data do not yet exist in the admitted packet.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp542_continuum_volume_design_rank.py

The generated result is
research/flavor/results/wp542_continuum_volume_design_rank.json.

The reviewed claim and report to marici.Nima were admitted at graph event
ev-000000004882-42e748e2-f9e7-43d6-bac9-fabd73cc024f. Admission records
reviewed provenance and does not certify truth.
