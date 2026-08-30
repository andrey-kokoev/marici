# Higgs quartic measurement-versus-actuation audit (WP417)

## Observed measurement channel

ATLAS has performed the first LHC search for triple-Higgs production in the
six-bottom-quark final state and reported the first direct constraints on the
quartic Higgs self-coupling modifier $\kappa_4$. This establishes a physically
typed, detector-calibrated channel whose event distribution is sensitive to
the quartic coupling. ATLAS also reports that no evidence for triple-Higgs
production was observed, so the present result is a constraint rather than a
precision determination.

Primary experimental sources:

- [ATLAS first triple-Higgs search](https://arxiv.org/abs/2411.02040)
- [ATLAS experimental briefing](https://www.atlas.cern/Updates/Briefing/First-Tri-Higgs-Search)

This closes the measurability half of the requested instrument gate.

## Why collider settings are not quartic actuation

Let a collider record have expected count

$$
N(E,L;\kappa_4)=L\left[A(E)+B(E)\kappa_4\right]^2.
$$

Beam energy $E$ and luminosity $L$ are executable commands. They alter the
sampling kernel and expected event count. Quartic sensitivity is expressed by

$$
\frac{\partial N}{\partial\kappa_4}\ne0.
$$

But the Standard Model coefficient is a fixed source parameter across those
settings:

$$
\frac{\partial\kappa_4}{\partial E}=0,
\qquad
\frac{\partial\kappa_4}{\partial L}=0.
$$

Event selection and Monte Carlo reweighting likewise change an analysis or
counterfactual model, not the physical coefficient in the collision source.
Consequently ATLAS supplies an executable probe family but not an executable
quartic actuator.

## Minimal missing constructor

A genuine actuator requires a declared physical source map such as

$$
\kappa_4(x)=\kappa_4^{(0)}+g_x\,x,
\qquad
\frac{\partial\kappa_4}{\partial x}=g_x\ne0,
$$

where $x$ is an independently prepared laboratory setting and $g_x$ is an
observed, calibrated coupling. This expression is a type specification, not an
admitted portal model. With no new coupling, $g_x=0$, and the actuation arrow
vanishes.

The same experiment must retain the WP412 broken-vacuum reference and measure
both the curvature and reference-relative displacement. Current collision
records do neither: Higgs bosons decay promptly, and the electroweak vacuum is
not prepared in two commanded quartic states.

## Verdict

The physical-instrument gate is half closed: the quartic is experimentally
probeable, but it is not an executable laboratory control. Calling beam energy
or simulation reweighting a quartic knob would violate the source/probe typing
established in WP404 and WP415.

Run `uv run --with sympy python
research/flavor/checkers/wp417_higgs_quartic_instrument_audit.py` to regenerate
the JSON result.
