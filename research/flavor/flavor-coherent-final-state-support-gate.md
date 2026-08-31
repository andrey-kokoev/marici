# Coherent final-state support gate: WP1048

## Question

Do WP1044--WP1047 calibrations prove that the Flavor amplitude and reference
amplitude reach one coherent final state?

## Cofinality coordinate

Add a coherent-overlap coordinate \(c\). The calibrated interference row is
then

\[
D=4\nu d c\mathcal L g.
\]

Use coordinates

\[
(B,\mathcal L,g,\nu,d,c).
\]

WP1044--WP1047 supply rows for background, signal, interference, visibility,
and live epoch. These rows have rank five on the six coordinates. A cofinality
or overlap row for \(c\) raises the rank to six.

## Exact collision without cofinality

The partial-overlap packet

\[
(B,\mathcal L,g,\nu,d,c)=(0,4,1,1,1,1/2)
\]

and the full-overlap packet

\[
(B,\mathcal L,g,\nu,d,c)=(0,1,2,1,1,1)
\]

share all rows available before cofinality is proved:

\[
B=0,
\qquad
S=4,
\qquad
D=8,
\qquad
V_{\rm ref}=1,
\qquad
\text{epoch}=1.
\]

If the partial-overlap packet is decoded while assuming \(c=1\), it returns

\[
(\mathcal L,g)=(1,2)
\]

instead of the actual \((4,1)\). Thus calibrated visibility and live epoch do
not authorize coherent support.

## Reconstruction with overlap retained

With an explicit overlap record,

\[
g=\frac{4\nu dc(S-B)}{D},
\qquad
\mathcal L=\frac{D^2}{16\nu^2d^2c^2(S-B)}.
\]

For the partial-overlap packet this recovers \((\mathcal L,g)=(4,1)\).

## Classification

This is a conditional support gate. The instrument branch now reaches the
physical `physical16` process assumption: one shared final-state Hilbert or
event cell must be derived for the Flavor and reference amplitudes, or the
overlap must be independently monitored with null-retaining loss accounting.

## Disposition

Productive but still not a selector. The remaining instrument task is no
longer a scalar calibration row; it is a `physical16` cofinality/source-support
constructor.

Checker: `research/flavor/checkers/wp1048_coherent_final_state_support_gate.py`

Result: `results/wp1048_coherent_final_state_support_gate.json`
