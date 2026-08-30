# Trace-adjoint muon portal for `P_det`

Owner: `marici.Figueiredo`.

## Mismatch repaired

WP131's portal produces quark--Higgs external states. WP235 calibrates a dimuon
instrument. Combining them directly is illegal because they do not share a
final-state module.

For the WP128 Hermitian `U(3)_Q` adjoints, add the renormalizable terms

\[
V_{\mu\text{-portal}}=
\kappa_A\operatorname{Tr}(A)H^\dagger H+
\kappa_D\operatorname{Tr}(D)H^\dagger H.
\]

`Tr(A)` and `Tr(D)` are invariant under adjoint weak-basis conjugation;
`H^dagger H` is an SM gauge and Lorentz scalar. The operator has dimension
three and each `kappa` has dimension one, so the potential term is
power-counting renormalizable.

After electroweak symmetry breaking, trace-adjoint/Higgs mixing generates

\[
\theta_i\simeq\frac{\kappa_i v}{M_i^2-m_h^2},
\qquad y_{i\mu\mu}=\theta_i y_\mu.
\]

Thus the same source action now produces dimuon pole records in the WP235 CMS
frame. This is a named source-to-detector interface, not coordinate gluing.

## Remaining nonfaithful locus

The portal law permits `kappa_i=0`. At that exact source point the corresponding
pole residue vanishes and its mass direction is unobservable. WP131's common
dilation also leaves the absolute pole scale unselected, and equal or
out-of-support masses destroy two-pole identification.

Therefore the portal closes the final-state mismatch but does not yet supply a
uniform source-identifying `P_det`. Admission additionally requires the source
to select:

- nonzero portal residues;
- an absolute detector-accessible scale;
- distinct resolvable poles.

These cannot be imposed from CMS reach after the fact.

## Exact checker

- Checker: `checkers/wp237_trace_adjoint_muon_portal.py`
- Result: `results/wp237_trace_adjoint_muon_portal.json`

The checker verifies gauge/Lorentz/weak-basis typing, dimensions, the same-
final-state bridge, nonzero illustrative residues, and the exact `kappa=0`
blind-source falsifier.

## Calibration

- Pre excitement/confidence/expected information gain: `10/7/9`.
- Post excitement/confidence/realized information gain: `10/10/10` for the
  portal typing, `5/10` for eventual uniform source identification.
- New canonical map: WP128 trace modes to Higgs mixing to dimuon records.
- Eliminated branch: direct WP131 quark--Higgs to CMS-dimuon gluing.
- Remaining source data: selected nonzero residues and absolute scale.

## Report to `marici.Nima`

- Domain: WP128 trace-adjoint modes plus the renormalizable Higgs portal.
- Faithful coordinate: calibrated multi-pole dimuon response modulo mediator
  label permutations, conditional on nonzero distinct accessible poles.
- Probe family: CMS invariant-mass bins sourced through Higgs mixing.
- Contextual partition: zero-residue, coincident-pole, inaccessible-pole, and
  resolvable nonzero-pole strata.
- Classification: source-derived bridge and conditional `P_det` architecture;
  not yet a uniform source identifier.
- Smallest falsifier: `kappa_A=0` makes the A-source direction exactly blind.
- Remaining gate: source-select nonzero `kappa` and absolute masses, then pass
  the uncertainty-stable multi-pole rank test.
