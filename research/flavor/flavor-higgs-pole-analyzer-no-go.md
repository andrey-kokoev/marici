# Higgs-pole analyzer no-go (WP425)

## Observed candidate

The Standard Model Higgs is the most economical observed electroweak pole. It
is produced by commanded collider beams and its nonlinear interactions are
probed by multi-Higgs channels. This supplies apparatus-to-pole and
pole-to-readout arrows without inventing a new resonance.

Primary experimental sources:

- [ATLAS observation of the Higgs-like resonance](https://arxiv.org/abs/1207.7214)
- [ATLAS single- and double-Higgs self-coupling constraints](https://arxiv.org/abs/2211.01216)

## Source typing

Represent the radial Higgs potential and an external production source by

$$
V_J(\phi)=-\frac{\mu^2}{2}\phi^2+\frac{\lambda}{4}\phi^4-J\phi.
$$

The collider command changes (J), which prepares or excites a Higgs state.
It does not change the law parameter (lambda):

$$
\frac{\partial\lambda}{\partial J}=0.
$$

Around a retained commanded background (phi=s+\eta), stationarity fixes

$$
J=-\mu^2s+\lambda s^3.
$$

The shifted potential has command-dependent curvature and cubic response,

$$
V_J''(s)=-\mu^2+3\lambda s^2,
\qquad
V_J'''(s)=6\lambda s,
$$

but its fourth derivative remains

$$
V_J''''(s)=6\lambda.
$$

Equivalently, the coefficient of (eta^4) is always (lambda/4). State
displacement exposes the fixed nonlinearity; it does not actuate that
nonlinearity.

## Hostile equivalence

For any two commanded backgrounds (s_1\neq s_2), the lower Taylor jets are
different while the quartic coefficient is identical. A detector can therefore
observe a command-dependent nonlinear Higgs response and still have zero
command-to-quartic parameter Jacobian. This is the precise state-versus-law
ambiguity that a resonance scan alone does not remove.

## Verdict

The observed Higgs pole is an executable analyzer of the self-interaction, not
an executable actuator of the quartic law. It cannot supply WP416's independent
second source direction. Reinterpreting beam energy, luminosity, or Higgs
occupation as a change of (lambda) would conflate state preparation with law
variation.

The smallest falsifier is an admitted fixed interaction in which the same
command (u) produces a nonzero coefficient derivative

$$
\frac{\partial\lambda_{\rm eff}}{\partial u}\neq0,
$$

measured independently of the state displacement. WP420's conditional singlet
constructor has this type, but no observed preparable substrate has yet supplied
its command and common-frame readout.

Run `uv run --with sympy python
research/flavor/checkers/wp425_higgs_pole_analyzer_no_go.py` to regenerate the
JSON result.
