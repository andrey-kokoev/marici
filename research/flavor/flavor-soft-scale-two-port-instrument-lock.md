# Soft-scale two-port instrument lock: WP1063

## Question

Can WP770's two-port instrument be locked to WP1060's common pole clock?

## Conditional identification

WP770 uses two calibrated momentum ports \(p=1,2\) in units of its instrument
mass standard \(m=1\). Conditionally identify that standard with WP1060's
common pole mass \(M\). The two-port ratios become

\[
\frac{p_{\rm soft}^2}{M^2}=1,
\qquad
\frac{p_{\rm vector}^2}{M^2}=4.
\]

The corresponding normalized one-pole responses are

\[
\frac12,
\qquad
\frac15.
\]

The response determinant for rows \((1,1/(1+r))\) is

\[
\frac15-\frac12=-\frac3{10},
\]

so the pair is an independent two-port readout. The first row restores the
WP1042 conditional \(1/2\) shape; the second row is the WP1062 same-radius
vector-KK cross-check.

## Vector-only hostile

Replacing the soft reference by the first vector KK port gives the pair

\[
\left(\frac{p^2}{M^2}\right)=(4,16),
\qquad
\left(\frac{R(p^2)}{R(0)}\right)=\left(\frac15,\frac1{17}\right).
\]

These rows are independent:

\[
\frac1{17}-\frac15=-\frac{12}{85},
\]

but neither is WP1042's ratio-one row. Vector-port independence alone is
therefore not the missing soft-scale channel.

## Boundary

The soft port is still a WP770 instrument reference, not a derived
`physical16` production or decay channel. The next source must realize both
ports in actual `physical16` channels and derive the source-to-detector gain
law in the same frame. WP1061's absolute radius cofiber also remains open.

## Classification

Conditional soft-scale two-port instrument. It reduces the momentum blocker
from an abstract ratio-one gap to a concrete `physical16` channel-realization
gate.

Checker: `research/flavor/checkers/wp1063_soft_scale_two_port_instrument_lock.py`

Result: `results/wp1063_soft_scale_two_port_instrument_lock.json`
