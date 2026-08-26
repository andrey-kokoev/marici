# Typed source-instrument pencil

## Question

After incorporating the later scale, twist, renormalization, and threshold
contracts, what is the source-image rank of WP538's unified six-port pencil?

## Source derivative

The only currently admitted moving source coordinate is WP537's \(t\), with

\[
a=t^2,\qquad w={1\over t},\qquad v^2=2.
\]

Differentiate the six normalized pencil coefficients with respect to \(t\)
while every instrument control is fixed. The resulting six-by-one tangent is
nonzero and has rank one.

This is the source-image rank. WP538's rank-six state readout and WP539's
rank-24 complex contextual map describe faithful readout layers; they are not
additional source directions.

## External control registry

The instrument bundle contains 29 tagged coordinates:

- one QCD scale coordinate;
- six twist/context coordinates;
- sixteen entries of the four-by-four renormalization and mixing matrix;
- six pole-threshold matching coordinates.

These are fixed by scale calibration, boundary-control protocols,
renormalization conditions, or threshold calculations. They are not
coefficients selected by the flavon source.

The direct-sum tagged Jacobian has total rank 30: one source direction plus 29
external controls. Projecting it back to the source block leaves rank one.
Calling 30 the source rank would smear instrument authority into source
authority.

## Exact scale confounder

Uniform source-pole scaling and inverse instrument-unit scaling have opposite
pencil-coefficient tangents. If the QCD scale is not independently calibrated,
their six-by-two Jacobian has rank one and kernel

\[
(1,1).
\]

Dimensionless pole coefficients therefore cannot distinguish a source-scale
change from an inverse unit change. External scale calibration is necessary
for identifying \(t\); it does not select \(t\).

## Rank ledger

The typed ranks are:

- fixed-control source image: 1;
- six-state pole readout: 6;
- four-channel contextual analysis: 24 complex;
- external calibration bundle: 29;
- tagged source-plus-control bundle: 30.

Only the first number carries source-image authority.

## Disposition

The instrument can separate the one-dimensional moving source family once all
controls are calibrated. It cannot create additional source directions or
remove WP543's selector kernel.

Physical realization still requires external scale and threshold
calibrations, implemented twists, nonperturbative four-channel
mixing/contact subtraction, and WP542's measured covariance. Numerical
selection remains a separate source-dynamics problem.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp544_typed_source_instrument_pencil.py

The generated result is
research/flavor/results/wp544_typed_source_instrument_pencil.json.

The reviewed claim and reply to marici.Nima were admitted at graph event
ev-000000004890-f55f2645-5ab5-4b2a-80d3-374f99744c1a. Admission records
reviewed provenance and does not certify truth.
