# Relative mediator sequence separates norms, arcs and boundary readout

Work package: WP605  
Owner: marici.Figueiredo

## Directed factorization

WP603 is refined into four typed components:

1. sector norm channels \(\Gamma_\phi,\Gamma_\psi\);
2. the coherent relative arc \(I\);
3. the boundary channel into `physical16`;
4. source composition and calibration laws.

The admitted source domain consists of nonzero real coupling pairs
\((g_\phi,g_\psi)\), quotiented by simultaneous global sign, and restricted
to records reachable from one common mediator.

## Relative exact sequence

At the discrete sign level, the structure is

\[
C_2^{\mathrm{global}}
\longrightarrow
C_2\times C_2
\longrightarrow
C_2^{\mathrm{relative}}.
\]

The sector norms

\[
\Gamma_\phi=g_\phi^2,
\qquad
\Gamma_\psi=g_\psi^2
\]

collapse all four sign assignments. The relative arc

\[
I=g_\phi g_\psi
\]

refines that fiber to exactly the two global-sign orbits. Thus norms plus the
arc are jointly faithful on the source quotient, while the norms alone are
not.

## Reachable composition

Separately valid coordinates do not automatically form a physical composite
record. A tuple is reachable from the declared one-mediator source only if

\[
I^2=\Gamma_\phi\Gamma_\psi.
\]

For example, the formal tuple \((4,9,5)\) violates this relation by \(-11\).
It cannot be used to infer a source state. Tree matching adds

\[
M^2c_{\mathrm{eff}}+I=0.
\]

These equations are source composition laws, not fitted reconstruction
identities.

## Boundary channel

Let the weak-basis-invariant portal be independently calibrated as

\[
J_{16}=-{\kappa I\over M^2}.
\]

For known \(M\) and nonzero calibrated \(\kappa\), the boundary channel
preserves the relative sign. If \(\kappa=0\), is unknown, or exists only in a
texture chart, the distinction does not reach `physical16`. Measured-ten
coordinates cannot replace this boundary because their projection is not
faithful on the physical flavor quotient.

## Completion continuity

Model finite-width propagation, background subtraction and detector response
by a calibrated visibility \(\nu\):

\[
I_{\mathrm{det}}=\nu I.
\]

Every \(\nu>0\) preserves the exact sign partition; \(\nu=0\) restores the
relative kernel. With uncertainty radius \(\delta\), robust separation requires

\[
\delta<\nu\lvert I\rvert.
\]

This distinguishes algebraic joint faithfulness, reachable-domain
composition and experimentally robust completion. None implies the next.

## Relation to the oriented-triangle source

WP604 supplies a coefficient-independent source chirality on its phase
quotient. A microscopic completion could realize its cyclic orientation
carrier through a common mediator. WP605 states exactly what that completion
must expose:

- two calibrated sector norm channels;
- one coherent cross-sector interference channel;
- a nonzero portal into `physical16`;
- the source matching identities on the actually reachable record domain;
- nonzero visibility with uncertainty below the sign-separation margin.

Until a concrete mediator and detector channel instantiate these arrows,
WP605 is an exact instrument specification, not an existing experiment.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp605_relative_mediator_exact_sequence.py

The generated result is
research/flavor/results/wp605_relative_mediator_exact_sequence.json.
