# Vacuum-stress source-rank gate

Work package: WP582  
Owner: marici.Figueiredo

## Lorentz-invariant vacuum channel

WP581 shows that a normalized vacuum ratio is relational and one-dimensional.
The underlying stress tensor makes the rank obstruction sharper. In four
spacetime dimensions, a Lorentz-invariant vacuum has

\[
T^{\mathrm{vac}}_{\mu\nu}=-\rho g_{\mu\nu}.
\]

Its trace is \(T=-4\rho\), and its trace-reversed source is

\[
S_{\mu\nu}
=
T_{\mu\nu}-{1\over2}Tg_{\mu\nu}
=
\rho g_{\mu\nu}.
\]

Both objects span the same one-dimensional metric line. Changing the
normalization reference \(M\) used in
\(\eta=\rho/M^4\) leaves the physical stress tensor unchanged:

\[
{\partial T^{\mathrm{vac}}_{\mu\nu}\over\partial M}=0.
\]

Thus \((\rho,M)\) is not a two-source physical family. It is one physical
source coordinate plus one relational readout reference.

## Smallest independent completion

A second local stress channel must leave the metric line. The smallest exact
example in a fixed Minkowski frame is a nonzero traceless tensor \(U\) with

\[
g^{\mu\nu}U_{\mu\nu}=0.
\]

For

\[
g=\operatorname{diag}(-1,1,1,1),
\qquad
U=\operatorname{diag}(3,1,1,1),
\]

the trace is zero and \(U\) is not proportional to \(g\). The two-source
family

\[
T_{\mu\nu}=-\rho g_{\mu\nu}+\tau U_{\mu\nu}
\]

has rank two with respect to \((\rho,\tau)\).

This completion is not another vacuum normalization. The displayed \(U\)
selects a timelike rest frame. A physical realization therefore requires an
admitted matter, anisotropic stress, boundary, or relational-frame source.
Adding that source changes the admitted state domain and groupoid.

## Flavor consequence

Even a genuine pair \((\rho,\tau)\) does not automatically generate two
flavor directions. Let \(C\) be the source-derived response from these stress
channels to invariant portal coordinates \((r,q)\). The flavor entrance has
rank two only if

\[
\det C\ne0.
\]

Lorentz decomposition supplies possible independent source types; it does not
derive their flavor couplings, choose their numerical values, or provide a
detector instrument. If both stress channels couple through the same scalar
combination, \(C\) remains rank one.

The smallest exact falsifier to a two-vacuum-source claim is the pair of
labels \((\rho,M)\): the \(M\) derivative of the physical stress vanishes.
The smallest conditional repair is a nonzero traceless channel, accompanied
by its physical frame and a noncollinear invariant flavor coupling.

## Classification

The Lorentz-invariant vacuum is a one-channel potential source, not a flavor
selector. The traceless completion is a conditional second-source
architecture, neither selector nor rigidifier. No physical16 refinement
occurs until a source-derived coupling and calibrated flavor instrument are
provided.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp582_vacuum_stress_source_rank.py

The generated result is
research/flavor/results/wp582_vacuum_stress_source_rank.json.
