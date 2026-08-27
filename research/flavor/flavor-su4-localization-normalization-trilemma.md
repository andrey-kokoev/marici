# The minimal SU(4) parent cannot remove its boundary modulus without reversing the twist: WP773

## Question

Can WP772 eliminate the common boundary kinetic modulus by promoting the
flavor operands into the bulk?

## Boundary branch

The gauge link belongs to the \(SU(4)\) vector adjoint and has no separate
hypermultiplet cost. With the portal operands localized at the boundary,

\[
\kappa=2+15=17>0.
\]

This branch selects the half twist, but WP772's exchange-even boundary kinetic
coefficient remains legal and changes the physical gauge normalization.

## Bulk branch

The orbifold lift of the portal operand packet has degree-weighted
hypermultiplet count \(32\). Promoting it to the bulk gives

\[
\kappa=2+15-32=-15.
\]

This does not remove the normalization modulus. Orbifold fixed points admit
residual-gauge-invariant kinetic operators independently of whether charged
matter is boundary-localized or bulk. In addition, the full-tower potential
now selects the zero twist rather than the required half twist.

Including the compulsory mediator packet adds another \(48\) hypermultiplet
degrees:

\[
\kappa=2+15-32-48=-63.
\]

The exact positive-index budget is only \(16\) hypermultiplet degrees, while
the portal operands already require \(32\).

## Trilemma

Within the minimal \(SU(4)\) gauge-link parent:

1. boundary localization preserves \(\kappa>0\) but retains the normalization
   modulus;
2. bulk localization retains that endpoint modulus and reverses the spectral
   selector;
3. the complete bulk mediator packet makes the reversal stronger.

The two branches are different source frames. Their favorable properties
cannot be combined by taking the positive spectral sign from one and the
absence of boundary terms from the other.

## Escape condition

A larger or different source group must contribute at least sixteen
additional vector degrees merely to restore a positive index after the portal
operands are bulk. That count is only a necessary gate. Enlargement does not
remove the fixed-point kinetic ring; a separate source principle must fix its
common coefficient. The enlarged group must also derive the exact flavor
embedding, chirality, anomaly completion,
isolated gauge normalization, and `physical16` instrument. Adding generators
until the inequality passes would not constitute a source explanation.

Reproduce with:

    uv run --with sympy python research/flavor/checkers/wp773_su4_localization_normalization_trilemma.py

Generated result:
research/flavor/results/wp773_su4_localization_normalization_trilemma.json
