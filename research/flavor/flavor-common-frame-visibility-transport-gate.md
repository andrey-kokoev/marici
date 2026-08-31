# Common-frame visibility transport gate: WP1046

## Question

Does a reference-only visibility measurement calibrate the Flavor interference
arm without common-frame transport?

## Two visibility coordinates

WP1045 adds a reference visibility row. That row measures the Flavor
interference visibility only if both visibilities live in one calibrated frame.
Use coordinates

\[
(B,\mathcal L,g,\nu_f,\nu_r),
\]

where \(\nu_f\) is the Flavor arm visibility and \(\nu_r\) is the reference
visibility. The rows

\[
B,
\qquad
S=B+\mathcal Lg^2,
\qquad
D=4\nu_f\mathcal Lg,
\qquad
V_r=\nu_r
\]

have rank four on five coordinates. Add the common-frame transport constraint

\[
\nu_f-\nu_r=0.
\]

The augmented row set has rank five.

## Exact collision without common-frame transport

The packets

\[
(B,\mathcal L,g,\nu_f,\nu_r)=(0,4,1,1/2,1)
\]

and

\[
(B,\mathcal L,g,\nu_f,\nu_r)=(0,1,2,1,1)
\]

share all measured rows:

\[
B=0,
\qquad
S=4,
\qquad
D=8,
\qquad
V_r=1.
\]

The first packet violates \(\nu_f=\nu_r\); the second satisfies it. Therefore
a reference row is not enough. The source or apparatus must also authorize the
transport identifying the reference visibility with the Flavor-arm visibility.

## Reconstruction after the transport is granted

When \(\nu_f=\nu_r\), the WP1045 reconstruction uses the reference record:

\[
g=\frac{4\nu_r(S-B)}{D},
\qquad
\mathcal L=\frac{D^2}{16\nu_r^2(S-B)}.
\]

For the surviving packet this gives

\[
(\mathcal L,g)=(1,2).
\]

## Classification

This is a conditional transport gate. It does not add a new detector number;
it declares the equality needed for the reference number to apply to the
Flavor path. A separate reference arm with no common-frame law leaves the gain
fiber open.

## Disposition

Productive. WP1045's reference-independence caveat is now a typed obligation:
derive common-frame visibility transport for the actual `physical16` process,
including drift and finite-width response. This still does not prove the
existence of an independent reference channel or source value of \(g\).

Checker: `research/flavor/checkers/wp1046_common_frame_visibility_transport_gate.py`

Result: `results/wp1046_common_frame_visibility_transport_gate.json`
