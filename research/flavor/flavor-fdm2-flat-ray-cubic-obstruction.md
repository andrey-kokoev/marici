# Flat-ray cubic obstruction in the portal-complete source (WP104)

Agent: `marici.Figueiredo`. Date: 2026-08-25.

WP103's non-strict copositivity boundary is not generically a stable source.
Take the exact saturated coefficients

\[
\lambda_H=1/8,\qquad \lambda_x=-1,\qquad \lambda_y=0.
\]

Along `u=t^2`, `x=+/- t/2`, `y=0`, the complete quartic vanishes:

\[
\lambda_Hu^2+2x^4+\lambda_xux^2=0.
\]

The independently allowed CP-even dimension-three portal

\[
\mu_x(H^\dagger H)x=\mu_xux
\]

then contributes `+/- mu_x t^3/2`. For every nonzero real `mu_x`, one of the
two sign rays tends to minus infinity. Terms of degree at most two cannot
repair that runaway.

Thus quartic copositivity with equality is insufficient once the full
renormalizable source is admitted. On this flat ray, boundedness forces the
cubic projection to vanish exactly; more generally every quartic zero ray
requires all odd leading lower-degree projections to vanish and the first
nonzero even projection to be nonnegative.

The smallest exact falsifier is
`(lambda_H,lambda_x,lambda_y,mu_x)=(1/8,-1,0,1)` with `x=-t/2`, whose leading
potential is `-t^3/2`. This obstruction is a weak-basis scalar and occurs
before thermal selection.

Classification: strict portal stability remains a nonempty conditional source
domain, not a numerical selector or rigidifier. The non-strict boundary is
admissible only after exact flat-ray constraints. Remaining gate: require a
strict RG-stable margin or enumerate every zero ray and its lower-degree
projections at the declared renormalization scale.

Verification: `uv run --with sympy python
research/flavor/checkers/wp104_fdm2_flat_ray_cubic.py`.
