# Local Green–Schwarz split cofiber: WP1069

## Question

What local anomaly vector follows from a symmetric split of WP1068's parent
Green–Schwarz coefficient?

## Conditional split

WP1068 gives the parent coefficient \(-3\). Conditionally distribute it
symmetrically between the two fixed points:

\[
g_0=g_\pi=-\frac32.
\]

For the gauge-gravity channels, local cancellation is then

\[
A_0=b+\frac B2+k+g_0,
\qquad
A_\pi=\frac B2-k+g_\pi.
\]

## Complete conditional vector

In the channel order

\[
SU(4)^3,\quad SU(4)^2U(1),\quad SU(2)^2U(1),\quad
U(1)^3,\quad U(1)\,{\rm grav},\quad
SU(4)\,{\rm grav},\quad SU(2)\,{\rm grav},
\]

the one-quartet vector is

\[
\left(\frac12,\frac14,0,2,2,-\frac14,0\right).
\]

At the reflected endpoint it is

\[
\left(-\frac12,-\frac14,0,-2,-2,\frac14,0\right).
\]

The port-destroying \(C=23\) doublet-pair cell has

\[
(0,0,-1,-16,-4,0,-\frac12).
\]

Neither vector is integral on all seven channels.

## Split hostile

The symmetric split is not derived. For example, the alternate parent split

\[
g_0=-2,
\qquad
g_\pi=-1
\]

changes the one-quartet gauge-gravity levels from

\[
\left(-\frac14,0\right)
\quad\text{to}\quad
\left(\frac14,\frac12\right).
\]

Thus WP1068's global coefficient is insufficient without an endpoint-split
law.

## Boundary

The next source must derive both the Green–Schwarz endpoint split and a
multicomponent shifted Chern–Simons quantization lattice.

## Classification

Conditional local Green–Schwarz split. It gives a complete seven-channel
one-quartet vector and an exact split hostile.

Checker: `research/flavor/checkers/wp1069_local_green_schwarz_split_cofiber.py`

Result: `results/wp1069_local_green_schwarz_split_cofiber.json`
