# Completed mediator grammar audit (WP402)

## Bounded question

Can WP400/WP401's static pole-and-displacement experiment include or exclude
quadratic context corrections, nonlinear tadpoles, finite width, and an extra
mediator before reserving a withheld measurement?

## Completed one-pole response

Use the finite-width response

\[
A(\omega,c)=
\frac{J_0+J_1c+J_2c^2}
{M^2+c+Q_2c^2-\omega^2-i\omega(\Gamma_0+\Gamma_1c)}.
\]

The coefficients $J_2$ and $Q_2$ represent the first nonlinear tadpole and
curvature corrections. The affine width completes the pole at the same order
in the context knob.

At zero frequency,

\[
A(0,c)=\frac{J_0+J_1c+J_2c^2}{M^2+c+Q_2c^2}.
\]

The width coefficients disappear exactly. No number of static displacement
measurements can validate or exclude them.

Four static contexts have Jacobian rank four on the five-parameter static
packet and leave one exact ambiguity direction. Thus WP400's four records are
not completion-safe once both quadratic corrections are admitted.

## Complementary dynamic readout

The absorptive component of the finite-frequency response depends on the
width. At the exact benchmark used by the checker, two source-generated
contexts at nonzero frequency give a rank-two Jacobian in
$(\Gamma_0,\Gamma_1)$. This is the minimal complementary repair of the static
width kernel.

The dynamic readout must be a calibrated line-shape or susceptibility
instrument. Algebraic access to a complex propagator is not itself a physical
measurement.

## Extra mediator boundary

Add an optional pole

\[
\frac{R_2}{M_X^2+c-\omega^2}.
\]

Nonzero residue changes the response and is spectrally testable. At $R_2=0$,
the extra mass $M_X$ is exactly unobservable. Uniform exclusion of extra
mediators is therefore impossible on the closure containing zero residue.
The admitted claim must either require a positive residue margin or quotient
away decoupled poles.

## Existing empirical status

WP237 supplies a real trace-adjoint/Higgs mediator architecture and WP235--245
supply CMS-calibrated finite-width dimuon response models. Those packets do
not supply a counterfactual knob varying the source couplings, and WP245 finds
insufficient 2016 exposure for two-pole identification. WP402 therefore types
the missing dynamic experiment; it does not claim that experiment has run.

## Disposition

The robust protocol needs at least five independent static constraints for the
completed static packet, two absorptive contexts for affine width, and a
nonzero-residue spectral search for extra poles. A withheld static displacement
alone cannot certify the requested completion.

Run `uv run --with sympy python
research/flavor/checkers/wp402_completed_mediator_grammar.py` to regenerate
the result.
