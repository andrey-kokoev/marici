# `physical16` shared-cell event space: WP1051

## Question

Can a typed `physical16` shared-cell event space distinguish an actual same-cell
overlap from a leaked or mis-celled monitor overlap?

## Typed event-cell rows

Add detector-cell support \(\alpha\) and monitor-cell support \(\beta\) to the
WP1050 coordinates. The minimal typed event space is

\[
S=B+\alpha\mathcal Lg^2,
\]

\[
D=4\nu dc\sigma\mathcal Lg,
\]

\[
M=\eta c\beta,
\qquad
N=\eta\beta.
\]

Use coordinates

\[
(B,\mathcal L,g,\nu,d,c,\eta,\sigma,\alpha,\beta).
\]

The WP1044--WP1050 rows have rank eight on ten coordinates. Adding typed
detector-cell and monitor-cell supports raises the rank to ten.

## Mis-celled hostile

The same-cell packet

\[
(B,\mathcal L,g,\nu,d,c,\eta,\sigma,\alpha,\beta)
=(0,4,1,1,1,1/2,1/2,1,1,1)
\]

and a monitor-leak packet

\[
(B,\mathcal L,g,\nu,d,c,\eta,\sigma,\alpha,\beta)
=(0,4,1,1,1,1/2,1/2,1,1,1/2)
\]

share the detector rows \(B=0\), \(S=4\), and \(D=8\), but their monitor rows
differ:

\[
(M,N)_{\rm same}=(1/4,1/2),
\qquad
(M,N)_{\rm leak}=(1/8,1/4).
\]

If the leak packet is decoded while assuming \(\beta=1\), the ratio \(M/N\)
returns \(1/2\), hiding the fact that the typed monitor cell reconstructs
\(c=1/4\) and would decode \((\mathcal L,g)=(16,1/2)\).

## Typed reconstruction

With typed monitor support,

\[
\eta=\frac{N}{\beta},
\qquad
c=\frac{M}{\eta},
\]

and then

\[
g=\frac{4\nu dc(S-B)}{D},
\qquad
\mathcal L=\frac{D^2}{16\nu^2d^2c^2(S-B)}.
\]

For the same-cell packet this recovers \((\eta,c,\mathcal L,g)=(1/2,1/2,4,1)\).

## Classification

This is a conditional event-cell gate. A same-cell certificate is insufficient
unless detector-cell and monitor-cell supports are typed and null-complete.
The actual `physical16` event cell must separate detector support, monitor
support, Flavor/reference/cross amplitudes, and null outcomes.

## Disposition

Productive. WP1050's typed event-cell requirement now has a minimal exact
mis-celled hostile and a cell-support reconstruction. The next required object
is a physical derivation of the detector and monitor supports from one source.

Checker: `research/flavor/checkers/wp1051_physical16_shared_cell_event_space.py`

Result: `results/wp1051_physical16_shared_cell_event_space.json`
