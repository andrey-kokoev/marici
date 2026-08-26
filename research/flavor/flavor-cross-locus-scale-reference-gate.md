# Cross-locus scale-reference gate

## Question

Does Aspect's comb-referenced six-port theorem directly repair WP544's
flavor/QCD detector-unit kernel?

## Distinct physical loci

Aspect proves an exact rank theorem when the six pole channels and reference
share one instrument-unit coordinate. A transfer to flavor must not assume
that identification.

Use three log coordinates:

\[
(\tau,u_F,u_C),
\]

where \(\tau\) is the physical flavor scale, \(u_F\) is the flavor/QCD detector
unit, and \(u_C\) is the comb unit. The six flavor rows are

\[
(c_i,-c_i,0),
\qquad c_i\in\{1,2,3,5,7,11\},
\]

while the independent comb row is

\[
(0,0,1).
\]

This seven-row Jacobian has rank two and exact kernel

\[
(1,1,0)^T.
\]

Thus calibrating the comb locus does not by itself calibrate the flavor locus.
The original physical-scale ambiguity survives.

## Missing interface constructor

The required new row is

\[
(0,1,-1),
\]

representing a physical interface \(P_{\mathrm{scale}}\) from a
comb-referenced frequency standard to the flavor/QCD detector energy unit.

After this row is admitted, the combined Jacobian has rank three and zero
kernel. The interface must provide:

- a named physical transfer chain;
- traceable coefficients in common units;
- uncertainty and drift covariance;
- support and bandwidth assumptions;
- readback proving that the calibrated unit is the one entering all six
  flavor ports.

Possible architectures include clock-referenced field metrology followed by
charged-beam momentum calibration, or an experimentally calibrated hadron
mass followed by lattice-spacing scale setting. Neither is admitted merely by
writing the interface row; its transfer coefficients and covariance must be
derived from the apparatus.

## Authority boundary

The Aspect architecture transfers as an abstract reference-port theorem. It
does not yet constitute an experimentally calibrated flavor instrument.

Even a completed \(P_{\mathrm{scale}}\) repairs identification only. It leaves
the rank-one source image unchanged and supplies no source gradient
\(\ell\). Numerical selection still requires

\[
2\ell_a-\ell_w\ne0
\]

from independently declared flavor dynamics.

## Smallest falsifier

Shift the physical flavor scale and flavor detector unit together while
holding the comb unit fixed:

\[
(\delta\tau,\delta u_F,\delta u_C)=(1,1,0).
\]

All six flavor rows and the comb row are unchanged. This exact hostile
direction disproves direct cross-locus calibration without
\(P_{\mathrm{scale}}\).

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp548_cross_locus_scale_reference_gate.py

The generated result is
research/flavor/results/wp548_cross_locus_scale_reference_gate.json.

The reviewed graph admission is
ev-000000004955-1e1725ec-8fc5-4c64-b782-639b00019233.
