# Mediator-clock relation census (WP432)

## Objective

WP431 requires a source-derived relation fixing the mediator-to-clock ratio
(M/v). This packet audits the three smallest current mechanisms that can
produce such a relation without using the flavor fit as input:

1. classical scale invariance with a Higgs portal;
2. gauge Higgsing;
3. dimensional transmutation or UV fixed-point crossover.

The acceptance rule is parameter authority, not algebraic existence. A
candidate passes only if the ratio contains no unfixed continuous datum after
the mechanism's declared source inputs are applied.

## Classical scale invariance

Removing an explicit mediator mass leaves a portal-generated relation

$$
M^2=kappa v^2,
\qquad
\frac{M}{v}=\sqrt{kappa}.
$$

The dimensionful input is gone, but the dimensionless portal coupling remains.
Scale invariance does not select (kappa). Measuring or choosing it would
calibrate the ratio; it would not derive it from scale invariance.

## Gauge Higgsing

For a flavor gauge boson broken by a field with scale (f),

$$
M_F=g_F\sqrt{C_R},f,
\qquad
\frac{M_F}{v}=g_F\sqrt{C_R}\frac{f}{v}.
$$

The representation factor (C_R) may be discrete, but the gauge coupling
(g_F) and breaking-scale ratio (f/v) remain continuous. Identifying (f=v)
by declaration still leaves (g_F), and no observed flavor gauge mediator or
source relation currently makes that identification physical.

## Transmutation and fixed points

Dimensional transmutation gives a scale of the schematic form

$$
\frac{Lambda}{v}
=\frac{mu_0}{v}
\exp\left(-\frac{1}{2b g_0^2}\right).
$$

WP134 proves this is RG-invariant along a chosen trajectory but depends on the
coupling and scale boundary. WP135 proves that a UV fixed point fixes critical
data but leaves the relevant amplitude and crossover scale free. Neither
selects the clock-normalized ratio without a boundary constructor.

## Verdict

All three mechanisms parallelize the mediator and clock algebraically. None
currently supplies parameter authority for the ratio. This distinguishes a
named formula from a source-generated prediction.

The closest progressive route is gauge Higgsing because an independently
observed gauge coupling and breaking order parameter could calibrate the ratio
without the selector-facing bins. But no admitted flavor gauge substrate has
those observations, and importing Standard Model (W/Z) data would change the
mediator class rather than identify WP128's flavor adjoints.

The smallest exact falsifier is one admitted mechanism whose final (M/v)
expression has no free continuous input except quantities already measured in
an independent source channel. Its group representation, vacuum relation, and
matching to the WP128 adjoints must be declared before the predicted threshold
is inspected.

Run `uv run --with sympy python
research/flavor/checkers/wp432_mediator_clock_relation_census.py` to regenerate
the JSON result.
