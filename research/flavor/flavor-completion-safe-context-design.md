# Completion-safe context design (WP403)

## Bounded question

What finite calibration and withheld schedule identifies the WP402 completion
without using displacement-only data or refitting the reserved outcomes?

## Joint static calibration

At each of $c=0,1,2$, measure both mediator curvature and displacement,

\[
H(c)=M^2+c+Q_2c^2,
\qquad
A_\star(c)=\frac{J_0+J_1c+J_2c^2}{H(c)}.
\]

The resulting six-by-five Jacobian has rank five. An exact five-by-five minor
equals $1/3$. This removes WP402's common-factor kernel and separately
calibrates the curvature and tadpole polynomials produced by the same knob.

The affine WP400 hypothesis is the submodel $Q_2=J_2=0$. It may be retained
only after the joint calibration bounds both corrections; it is not assumed
from displacement alone.

## Width and extra-pole calibration

Two absorptive measurements at $(c,\omega)=(0,2)$ and $(1,2)$ give a rank-two
Jacobian for $(\Gamma_0,\Gamma_1)$. Two residual spectral measurements at
$\omega=0,1$ identify a nonzero extra-pole residue and mass. At zero residue,
the extra mass remains outside the faithful quotient.

This staged design includes the first quadratic curvature and tadpole terms,
affine finite width, and one additional mediator. Further fields or higher
orders define an explicit successor grammar and cannot be introduced after
the withheld measurements.

## Frozen withheld predictions

For the exact benchmark, reserve three records:

- static $c=3$: $(H,A_\star)=(4,7/4)$;
- dynamic $(c,\omega)=(2,2)$: $A=(-5+30i)/37$;
- extra-pole residual at $\omega=2$: $1/5$.

These values are generated before the withheld observations. Any discrepancy
rejects the frozen benchmark or its support assumptions; parameters are not
refitted in this protocol.

## Physical boundary

WP403 is an exact experiment design, not an executed experiment. WP237--WP245
provide a real trace-adjoint/Higgs mediator architecture and CMS-calibrated
line-shape machinery, but no laboratory operation currently varies the portal
curvature and tadpole counterfactually. Collider energy, luminosity, and event
selection are observation contexts, not automatically source-coupling knobs.

## Disposition

The completed parameter packet is locally identifiable on the declared
nonzero-residue domain, and all three withheld predictions are fixed. The live
gate is physical binding: one real mediator, one executable knob, and one
common calibration chain for pole curvature, displacement, and absorptive
line shape.

Run `uv run --with sympy python
research/flavor/checkers/wp403_completion_safe_context_design.py` to
regenerate the result.
