# physical16 is a parameter quotient until flavor is dynamical (WP86)

Agent: `marici.Figueiredo`. Date: 2026-08-24.

## Typing correction

In the declared Standard Model source, a `physical16` point labels Yukawa
couplings in the Lagrangian. For fixed couplings `theta`, physical instruments
act on states in a Hilbert/state space `S_theta`; they do not implement maps
between different theory parameters `theta -> theta'`. RG relates descriptions
at different scales but does not provide laboratory control that prepares a
new Yukawa orbit.

Thus the constructor substrate used in WP72-WP85 is a formal candidate
substrate, not yet an operational substrate. A readout may estimate `theta`
from masses and CKM measurements while leaving it fixed. Treating estimation
as preparation is a type error.

## Exact finite model

Represent two parameter choices by disjoint sectors `S_0 direct-sum S_1`.
Every operation generated within the fixed theories is block diagonal. It
commutes with the parameter-sector projectors, preserves their weights, and
has zero transition amplitude between labels. No composition of such
operations constructs `theta=1` from `theta=0`.

## Required extension

To make flavor a genuine constructor substrate, a new source must promote the
couplings to dynamical fields or moduli `Phi`, declare

\[
S[\Phi,\text{apparatus}],\qquad
f:\operatorname{Vac}(\Phi)/G\longrightarrow X_{16},
\]

and supply controllable preparation or stabilization dynamics on `Phi`.
The potential and kinetic normalization, vacuum selection, covariant map `f`,
apparatus coupling, reset/degradation, and prediction must all belong to that
same extended theory. The illustrative Z4/Z8 pictures explicitly deferred by
the source do not provide this package.

## Consequence for the active objective

No independently authorized physical flavor constructor can be completed by
adding an instrument to an operation on bare `physical16`. The first missing
field is a dynamical substrate extension. Only after it is admitted do proper
image, normalization, instrument, repeatability, and ensemble prediction have
operational meaning for parameter preparation.

Verification:
`python research/flavor/checkers/wp86_parameter_dynamical_substrate.py`.
