# Mediator interference is the minimum relative-sign instrument

Work package: WP603  
Owner: marici.Figueiredo

## Source grammar

The surviving non-diagonal and collective-breaking branches require a source
interaction that links two flavor sectors. The smallest threshold model has
one resolved mediator of mass \(M\) and two nonzero real couplings
\(g_\phi,g_\psi\). Tree matching gives a low-energy cross coefficient

\[
c_{\mathrm{eff}}=-{g_\phi g_\psi\over M^2}.
\]

The relative sign is load-bearing: changing it can exchange an aligning and a
misaligning flavor interaction without changing the mediator mass or separate
decay rates.

## Why partial widths are insufficient

In an independently calibrated normalization, separate partial widths measure

\[
\Gamma_\phi=g_\phi^2,
\qquad
\Gamma_\psi=g_\psi^2.
\]

For fixed nonzero magnitudes, all four sign assignments have the same width
record. After quotienting the simultaneous global sign reversal, two
physically distinct constructor classes remain:

\[
\{(++),(--)\},
\qquad
\{(+-),(-+)\}.
\]

The width Jacobian has local rank two away from zero. It nevertheless collapses
these two global classes. This is an exact instance of finite fiber not being
singleton fiber: local rank cannot authorize source identification.

## Minimum completed probe

If the mediator grammar independently supplies two coherent amplitudes into
one resolved final state, their interference measures

\[
I=g_\phi g_\psi.
\]

Widths plus \(I\) recover exactly the two global-sign quotient classes. The
joint response Gram determinant is

\[
4g_\phi^4+16g_\phi^2g_\psi^2+4g_\psi^4>0
\]

for nonzero couplings. More importantly, the finite contextual partition is
faithful on the declared constructor quotient.

This is not an arbitrary reference port. The relative phase is defined by two
source-derived amplitudes terminating in the same physical channel. If the
mediator has only disjoint decay channels, the interference record does not
exist and the sign ambiguity remains.

## Executable falsifiers

The minimal tree architecture predicts the joined relations

\[
M^2c_{\mathrm{eff}}+I=0,
\qquad
I^2=\Gamma_\phi\Gamma_\psi
\]

in the declared normalization. A resolved resonance experiment can therefore
criticize the constructor by measuring its mass, two partial widths and a
sign-sensitive shared-channel line shape, then comparing them with the
low-energy cross interaction transported to `physical16`.

The physical instrument is not yet admitted. A complete packet must derive:

- the common final state and both amplitudes from the mediator source;
- finite widths and mixing;
- a calibrated phase convention and background model;
- detector resolution sufficient to retain the interference sign;
- the portal from \(c_{\mathrm{eff}}\) to a faithful `physical16` CP-odd
  coordinate.

Without those items, \(I\) is a formal pole coordinate rather than an
executable observation.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp603_mediator_interference_sign_instrument.py

The generated result is
research/flavor/results/wp603_mediator_interference_sign_instrument.json.
