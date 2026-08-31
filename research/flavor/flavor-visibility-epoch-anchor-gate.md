# Visibility epoch-anchor gate: WP1047

## Question

Does a common-frame visibility transport law remain valid without a live epoch
or external drift anchor?

## Drift coordinate

WP1046 requires the Flavor-arm visibility and reference visibility to share a
frame. Add a drift coordinate \(d\) so that

\[
\nu_f=d\nu_r.
\]

Use coordinates

\[
(B,\mathcal L,g,\nu_r,d).
\]

The measured rows are

\[
B,
\qquad
S=B+\mathcal Lg^2,
\qquad
D=4d\nu_r\mathcal Lg,
\qquad
V_r=\nu_r.
\]

They have rank four on five coordinates. A live epoch or external drift anchor
adds the row

\[
d=1,
\]

raising the rank to five.

## Stale-frame hostile

The stale packet

\[
(B,\mathcal L,g,\nu_r,d)=(0,4,1,1,1/2)
\]

and the live packet

\[
(B,\mathcal L,g,\nu_r,d)=(0,1,2,1,1)
\]

share all unanchored records:

\[
B=0,
\qquad
S=4,
\qquad
D=8,
\qquad
V_r=1.
\]

If the stale packet is decoded while assuming \(d=1\), it returns

\[
(\mathcal L,g)=(1,2)
\]

instead of its actual \((4,1)\). This is a confidently wrong gain, not a noisy
record.

## Anchored reconstruction

When the drift anchor is retained, reconstruction is

\[
g=\frac{4d\nu_r(S-B)}{D},
\qquad
\mathcal L=\frac{D^2}{16d^2\nu_r^2(S-B)}.
\]

For the stale packet this recovers \((\mathcal L,g)=(4,1)\), and a live-epoch
interlock may instead reject the stale record before decoding.

## Classification

This is a conditional epoch gate. WP1046's common-frame transport must be live,
not merely declared once. A co-moving or stale calibration frame can preserve
internal rows while moving the science-frame gain.

## Disposition

Productive. The instrument target now requires a live epoch interlock or an
external drift anchor for the actual `physical16` interferometer. Stochastic
drift, finite-width lines, and physical source realization remain open.

Checker: `research/flavor/checkers/wp1047_visibility_epoch_anchor_gate.py`

Result: `results/wp1047_visibility_epoch_anchor_gate.json`
