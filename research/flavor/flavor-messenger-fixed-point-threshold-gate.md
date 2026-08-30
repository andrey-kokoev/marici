# Messenger-assisted fixed-point threshold gate

## Candidate source mechanism

WP465 asks whether the vectorlike messenger sector already required by WP435
can repair WP464's strong two-loop gauge root. Above both messenger thresholds,
the diagonal `SU(3)_F` spectrum contains:

- six Dirac flavor fundamentals from the ordinary up/down quarks with color;
- six more Dirac flavor fundamentals from the up/down vectorlike messenger
  pairs with color;
- three real adjoint flavons from WP447.

This packet first evaluates the gauge-only two-loop subsystem. The messenger
Yukawa couplings are not set to zero as a physical claim: their omitted beta
contributions remain a completion gate. The gauge-only computation is an exact
necessary compatibility test for the proposed mechanism.

## Active-spectrum root

Using the real-scalar two-loop coefficients frozen in WP464, the twelve-Dirac
active theory gives

\[
b_0^{\rm high}={3\over2},\qquad b_1^{\rm high}=-113.
\]

Its formal nonzero root is

\[
g_{*,\rm high}^2={24\pi^2\over113},\qquad
\alpha_{*,\rm high}={6\pi\over113}\simeq0.167.
\]

Unlike WP464's root, this value is perturbatively small in the loop coordinate
`g_F^2/(16*pi^2)=3/226`. Thus the messenger matter genuinely opens a possible
weak-coupling window.

## Exact threshold obstruction

WP435 obtains the low-energy Yukawa portal by eliminating messengers with
nonzero masses `M_U` and `M_D`. Below those thresholds the six messenger Dirac
fundamentals are absent. The coefficients revert to WP464's

\[
b_0^{\rm low}={11\over2},\qquad b_1^{\rm low}=-37.
\]

Evaluating the low-energy two-loop bracket at the high-spectrum root gives

\[
b_0^{\rm low}+b_1^{\rm low}{g_{*,\rm high}^2\over16\pi^2}
={566\over113}>0.
\]

Therefore the messenger-assisted root is not a fixed point of the EFT in which
the messengers have been integrated out. A finite threshold crossing transports
the coupling away from the root, and its value at the flavor-breaking pole
depends on the threshold ratios and an RG trajectory. Those are precisely the
continuous inputs the selector was meant to remove.

Keeping the messengers active at the flavor-gauge pole does not compose with
WP449 either: messenger decay channels are then open or threshold-adjacent, so
the independently frozen quark-only widths cease to apply. This is a domain
failure, not a numerical disagreement.

## Disposition

- Descent: both beta functions are law-level weak-basis invariants.
- Selection: the massless active-spectrum truncation conditionally selects a
  weak coupling, but the massive WP435 theory does not select its value at the
  physical flavor pole.
- Rigidification: none.
- Smallest exact falsifier: the low-spectrum beta bracket at the proposed root
  is `566/113`, not zero.
- Remaining gates: derive the full coupled gauge-Yukawa beta system; freeze
  messenger threshold matching and the ratios `M_U/m_1`, `M_D/m_1`; recompute
  pole widths and residues with every open messenger/flavon channel; then test
  whether the resulting finite-scale value is trajectory-independent.

