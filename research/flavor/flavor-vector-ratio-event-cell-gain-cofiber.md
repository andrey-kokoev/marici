# Vector-ratio event-cell gain cofiber: WP1064

## Question

Can WP1052's `physical16` atom cell carry WP1062's source-derived vector
threshold ratio?

## Vector-ratio cell

WP1062 gives the first vector-KK threshold ratio and shape

\[
\frac{p^2}{M^2}=4,
\qquad
\mathcal L=\frac15.
\]

Insert this into WP1052's common-source atom cell

\[
\alpha=\beta=\sigma=\nu=d=1,
\qquad
c=\eta=\frac12,
\qquad
B=0,
\qquad
g=1.
\]

The retained rows become

\[
S=B+\alpha\mathcal Lg^2=\frac15,
\]

\[
D=4\nu dc\sigma\mathcal Lg=\frac25,
\]

\[
M=\eta c\beta=\frac14,
\qquad
N=\eta\beta=\frac12.
\]

The typed WP1051 reconstruction returns exactly

\[
\eta=\frac{N}{\beta}=\frac12,
\qquad
c=\frac{M}{\eta}=\frac12,
\]

\[
g=\frac{4\nu dc(S-B)}{D}=1,
\qquad
\mathcal L=\frac{D^2}{16\nu^2d^2c^2(S-B)}=\frac15.
\]

## Exact hostiles

Keeping WP1042's ratio-one shape instead gives

\[
\mathcal L=\frac12,
\qquad
S=\frac12,
\qquad
D=1.
\]

The vector and unit-ratio rows therefore differ by

\[
\Delta S=\frac3{10},
\qquad
\Delta D=\frac35.
\]

A pure-rate laundering pair

\[
(g,\mathcal L)=\left(\frac12,\frac45\right)
\]

has the same \(S-B=1/5\) but coherent difference

\[
D=\frac45,
\]

not \(2/5\). The retained coherent row separates it.

## Boundary

This is a conditional event-cell branch, not a physical source derivation.
The remaining gates are actual `physical16` production/decay channels for the
vector and/or soft ports, source-derived atom weights and labels, and a
source-derived gain \(g\).

## Classification

Conditional vector-ratio event-cell constructor. It shows that the gain chain
can carry the source-derived ratio-\(4\) threshold shape, so the missing
soft-scale channel is no longer the only coherent readout route.

Checker: `research/flavor/checkers/wp1064_vector_ratio_event_cell_gain_cofiber.py`

Result: `results/wp1064_vector_ratio_event_cell_gain_cofiber.json`
