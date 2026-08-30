# CMS HHH empty sensitive overlap

Work package: WP564  
Owner: marici.Figueiredo

## Why the new CMS result matters

CMS HIG-24-012 is a physically executed triple-Higgs experiment, not a
forecast. It uses 138 inverse femtobarns of 13 TeV proton-proton collisions,
reconstructs resolved and merged six-bottom topologies, calibrates jet and
flavor-tag responses with data, validates its background construction in
control regions, and performs a binned profile-likelihood fit to a SPANET
discriminant. It reports observed one- and two-parameter constraints on the
trilinear and quartic Higgs modifiers.

This closes an important overstatement in WP560--WP563: physical preparation,
scattering, detector readout, calibration, and an uncertainty model now exist
for the CMS kappa-framework experiment. The unresolved question is whether its
likelihood is defined on the flavor source domain.

Authoritative public records:

- CMS result page: https://cms-results.web.cern.ch/cms-results/public-results/publications/HIG-24-012/
- paper: arXiv:2607.05145;
- HEPData: https://doi.org/10.17182/hepdata.180103.

The frozen HEPData record JSON has SHA-256
`b0000f54668a785a25cff6cfb58565f7b07a80620ff12eadf7c94f4bddeddcba`.
The release contains seven result tables: a signal-strength result, an upper
limit, one-dimensional kappa limits, and four sampled confidence contours. It
declares no additional resource and exposes no Combine model or
source-parameterized bin likelihood.

## The admitted CMS likelihood slice

The paper states that its coupling scans:

1. fix the top-quark Yukawa coupling to the Standard Model value;
2. account only for overall normalization effects in HHH and HH;
3. use the Standard Model signal topology for every coupling value;
4. leave dedicated coupling-dependent shape treatment outside the analysis.

Therefore the published likelihood is typed on the phenomenological slice

\[
\kappa_t=1.
\]

Within that slice, the declared scan varies \(\kappa_3\) and \(\kappa_4\).

## Exact empty-overlap theorem

WP562 admits the leading universal trace-adjoint/Higgs mixing domain. Write
(z=\sin^2\theta\). With no exotic decay and no new production amplitude, the
light-Higgs coupling to the top quark obeys

\[
\kappa_t^2=1-z.
\]

The source quartic response derived in WP560 is

\[
{\partial\kappa_4\over\partial\lambda_s}
={z^2\over\lambda_H},
\qquad \lambda_H>0.
\]

Intersecting the portal relation with the CMS scan condition gives

\[
\kappa_t=1
\quad\Longrightarrow\quad
z=0
\quad\Longrightarrow\quad
{\partial\kappa_4\over\partial\lambda_s}=0.
\]

Hence there is no point at which the currently admitted CMS likelihood slice
and the source-sensitive portal domain overlap. This is stronger than a
missing numerical covariance: the pullback is ill-typed before covariance is
formed.

The smallest exact hostile point is

\[
(z,\kappa_t)=\left({3\over4},{1\over2}\right).
\]

It satisfies the portal relation and has response
(9/(16\lambda_H)>0), but violates the CMS scan condition exactly.

## Contextual partition and classification

On its own admitted kappa-framework domain, CMS has a real physical
instrument and its observed contours nontrivially restrict
((\kappa_3,\kappa_4)). Those contours are readouts, not a source selector:
the beam does not prepare or command a value of either coupling.

On the flavor portal domain, the currently transportable CMS probe family is
still only the independently calibrated inclusive-Higgs mixing readout from
WP562. Its contextual classes fix (z) and retain the full
(\lambda_s)-fiber. The HHH scan cannot refine that partition until its
likelihood admits the mixing and associated topology directions.

Thus the CMS operation is:

- a detector-realized kappa-framework readout;
- neither a flavor selector nor a flavor presentation rigidifier;
- not yet an end-to-end realization of the WP559 four-point derivative.

All entrance and exit quantities are weak-basis invariant, so full
weak-basis descent is not the obstruction. The first nonfaithful arrow is the
restriction of the detector likelihood to (\kappa_t=1) and Standard Model
signal topology.

## Smallest repair

A sufficient successor release would provide a calibrated likelihood or
template family over at least

\[
(\kappa_3,\kappa_4,\kappa_t,\kappa_b,\Gamma_H,\nu),
\]

with coupling-dependent HHH and HH shapes, detector and theory nuisances
(\nu), and a declared map from the frozen portal source parameters into that
domain. A portal-complete mixed-scalar likelihood including heavy-state masses,
widths, and threshold effects would be stronger.

Sampled confidence contours alone cannot substitute for that object: they do
not determine the nuisance-profiled local curvature or its pullback to the
source direction.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp564_cms_hhh_empty_sensitive_overlap.py

The generated result is
research/flavor/results/wp564_cms_hhh_empty_sensitive_overlap.json.
