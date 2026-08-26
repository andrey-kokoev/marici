# Messenger-threshold kernel transfer

## Question

Does the source-derived WP478 messenger threshold supply the transverse
operation required by WP546 on the faithful source quotient?

## Extended source domain

The four WP543 coordinates are insufficient for this question because the
threshold coefficient depends on additional source labels. Use

\[
x=(\log a,\log w,\log g_F^2,\log g_P^2,
\log y_Q,\log y_\Phi,\log\eta,\log k_\Phi).
\]

The finite messenger loop derives

\[
a={3k_\Phi y_Q^2y_\Phi^2\over16\pi^2\eta}.
\]

Its exact log-gradient is

\[
r_{\mathrm{th}}=(1,0,0,0,-2,-2,1,-1).
\]

On the old projected tangent \(k=(2,-1,0,0,0,0,0,0)^T\), the contraction is
two. The threshold therefore looks transverse if the messenger coefficients
are silently held fixed.

## Exact kernel transfer

Appending the threshold row raises the source rank from three to four, but the
eight-coordinate kernel still has dimension four. In particular,

\[
k_Q=(2,-1,0,0,1,0,0,0)^T
\]

annihilates every row. It simultaneously changes the target by

\[
d\log(g_Ff/v)=-1.
\]

The analogous tangent with \(d\log y_\Phi=1\) also survives. Thus the threshold
does not destroy the physical ambiguity. It transfers it from the portal
coefficient \(a\) into an unfrozen messenger normalization.

The first nonfaithful arrow is the projection from the extended source packet
to \(a\). Its fiber contains the continuously variable combination

\[
{y_Q^2y_\Phi^2k_\Phi\over\eta}.
\]

## Instrument typing

Messenger widths or pole residues can depend on the Yukawa normalizations.
With independently calibrated production, channel support, and detector
response they may identify the realized point on this fiber. That operation
would be a physical readout, not a source selector.

Using such a width or residue to freeze \(y_Q\) before claiming the threshold
predicts \(g_Ff/v\) would reverse the causal arrow. Spectral data may test a
source-selected portal combination only after the source dynamics has selected
it.

## Disposition

WP478 remains a genuine source-derived interaction rigidifier and supplies a
conditional transverse relation. It is not a numerical selector on the
faithful extended source quotient.

The smallest exact falsifier rescales

\[
d\log a=2,\qquad d\log w=-1,\qquad d\log y_Q=1.
\]

The fixed-electroweak relation and messenger threshold remain unchanged while
the target changes. Reopening requires source dynamics that fixes
\(y_Q^2y_\Phi^2k_\Phi/\eta\). Widths and residues must then be recomputed and
independently calibrated as tests.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp547_threshold_kernel_transfer.py

The generated result is
research/flavor/results/wp547_threshold_kernel_transfer.json.

The reviewed graph admission is
ev-000000004918-ce1fcc1d-4055-4e8a-9df4-1e0b80e3c777.
