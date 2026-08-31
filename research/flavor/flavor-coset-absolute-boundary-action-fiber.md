# Coset-to-boundary-action fiber: WP1094

## Question

Does WP1070's required anomaly coset determine the absolute UV boundary
Chern–Simons action?

## Integer-lift ambiguity

The required residue is

\[
s=\left(\frac12,\frac14,0,0,0,\frac34,0\right)\pmod{\mathbb Z^7}.
\]

Both \(s\) and

\[
s+(0,0,0,1,0,0,0)
\]

represent the same coset, but they are different absolute lifts.

For a channel-occupation vector \(t=(0,0,0,1,0,0,0)\),

\[
s\cdot t=0,
\qquad
[s+(0,0,0,1,0,0,0)]\cdot t=1.
\]

Thus integer shifts preserve anomaly cancellation while changing a
channel-resolved boundary evaluation.

## Classification

Negative gate. An anomaly coset modulo integers is not a unique classical
boundary action or normalization. The remaining UV packet must select the
absolute Chern–Simons lift, counterterm convention, endpoint orientation, and
physical16 descent.

Checker: `research/flavor/checkers/wp1094_coset_absolute_boundary_action_fiber.py`

Result: `results/wp1094_coset_absolute_boundary_action_fiber.json`
