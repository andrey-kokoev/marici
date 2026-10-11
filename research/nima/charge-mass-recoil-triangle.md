# Charge–mass–recoil as a typed compatibility triangle

## Question and declared test

Operator stimulus: try the proposed charge–mass–recoil triangle, keeping physical time separate. This is a non-evidential search direction. SCC obligation: **route/coherencer compatibility**, downstream of explicitly supplied interaction and inertia laws.

Bare charge, mass and recoil are not three objects with canonical maps between their scalar values. Use three presentations of the SAME two-body interaction instead:

- C: signed coupling coefficient c=q1*q2, with the complete preparation retained;
- R: the two momentum increments (J,-J);
- V: the two velocity increments (J/m1,-J/m2).

Mass belongs to the common context and defines the R-to-V map. It is not manufactured by an arrow from charge. Context includes positive masses, signed charges, initial momenta, units, and a supplied integrated interaction vector G. The coefficient domains are rational numbers for the exact fixture; the algebraic identities also hold over real numbers with positive masses.

Freeze the candidate laws before testing:

    C -> R: J=c*G;
    R -> V: (delta_p1,delta_p2) -> (delta_p1/m1,delta_p2/m2);
    C -> V: c -> (c*G/m1,-c*G/m2).

G has units momentum/charge^2. It is an external impulse interface, NOT a WG-derived force, Coulomb law, or conversion of an iteration count into physical time. No finite-duration trajectory is assumed. The direct formula is a supplied Newtonian comparison law, not an independent experimental prediction.

The face witness is the exact vanishing of the six-component route residual. Preserve both route descriptions even when their returned values agree.

## Risky consequences and rivals

The candidate requires zero total momentum increment, reversed recoil when one charge changes sign, zero recoil for a neutral partner, and different velocity responses for unequal masses.

Named rivals to reject:

1. A one-body account omitting the partner's impulse.
2. A response using the same inertial mass for both bodies.
3. A nonnegative intensity substituted for signed coupling.
4. A claim that momentum balance alone supplies a closed energy budget.

The test must retain the exact nonzero residual of each rival. It must also test charge-normalization and mass-scale changes rather than infer either scale from a commuting triangle.

## Claim boundary

This is a trial nonrelativistic driven-impulse model. Coupling, inertial response and the momentum interpretation are supplied inputs. The existing WG mode norm is not identified with mass, its phase is not identified with charge, and its positional first moment is not identified with momentum.

The energy test compares the kinetic increment with impulse work; any nonzero work requires an energy source outside the instantaneous two-body momentum record. It is not evidence of spontaneous energy production.

A tetrahedral extension requires a fourth typed presentation and additional face witnesses. A workflow index is not that fourth object. No source-to-physical-time map is supplied here.

## Disposition

The exact checker passes 90 rational parameter fixtures and a linear-map basis witness. The six-component route residual vanishes. The general identity follows directly from the displayed maps; the parameter census is regression coverage, not a universal physical test.

For q1=1, q2=-2, m1=2, m2=3 and G=(1,2,-1), the impulses are (-2,-4,2) and (2,4,-2); the velocity increments are (-1,-2,1) and (2/3,4/3,-2/3). Each nonzero component recovers the mass ratio m1/m2=2/3 independently of the common impulse magnitude. Absolute mass remains free. The coupling reads the charge product, not either charge separately; reversing both signs or reciprocal charge rescaling is invisible.

The four rival residuals are retained in `results/charge-mass-recoil-triangle.json`. In particular, the same kick from rest increases kinetic energy by 10 in the fixture's declared units. Momentum balances, but an unrecorded energy supply is required. The triangle is not an isolated energy-conserving interaction model.

Charge rescaling together with inverse-square rescaling of G preserves the response. Scaling both masses and G equally also preserves the velocity response while scaling momentum transfer and energy. Thus closing the face cannot select physical charge or mass normalization.

`python research/nima/checkers/check_charge_mass_recoil_triangle.py` and the owner-local SCC model check pass. SCC categorical validates the diagram but does not close its face: its literal route words differ, and it has no imported algebraic reduction witnessing their equal maps. No identical-token workaround is used; exact semantic verification stays in the independent checker. The time tetrahedron is explicitly unsupported.

The result is a concrete compatibility triangle for supplied laws, not a derivation of those laws from WG. The native-history-to-excitation obstruction is unchanged. No new Agda proof, physical time calibration, experimental match or higher-cell filler is claimed.
