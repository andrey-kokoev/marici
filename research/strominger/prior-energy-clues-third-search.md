# Third energy search: collective modes, elementary dressing and primitive charge

## What changes the current plan

The earlier research explicitly distinguishes source-native collective modes from independent seam records. Our latest 21-register coupling is a valid composition of a prior model, but it is not the strongest source-only route. Its success cannot establish that 21 extra physical resources are present.

This was a document search, not a fresh execution of the cited checkers.

## 1. The neutral carrier already has an exactly closed collective sector

`research/voevodsky/collective-carrier-spectrum.md` supplies an exact 36-to-6 invariant reduction of the belt after native phase selection and alignment. All 21 seams act inside six collective amplitudes, leaving one ground mode and five excitations. There is no leakage to the other thirty coordinates.

The collective energies in the note's E*=pi*hbar/tau units are

    0,
    0.172938631059...,
    4485/3292,
    1.433959780713...,
    5391/3292,
    2.393101588228....

The softest state is antisymmetric under interchange of the paired faces. The proton's lowest native excitation is 1/2 in those same units. The complete 36-dimensional spectra are also accounted for.

The note explicitly follows the failed independent-seam mass trial and recommends connecting these actual collective modes to the common vacuum, rather than reinstalling seam-count energy. This is directly relevant to our recent 21-register add-on.

Reusable checker: `research/voevodsky/checkers/check_collective_carrier_spectrum.py`.

## 2. The full elementary field contact is already known

`research/voevodsky/interacting-elementary-reference.md` derives the contact from all six shared face edges. After normalization it is the entire rank-two N_e, not a selected spin component.

Its native coherent states are annihilated by all positive projector defects. Changing their defect weights cannot change the coherent rest offset. A neutral field acting through N_e dresses both spin components equally. Under the old shared oscillator rule the elementary offset 1 becomes 3/4. That dressed denominator was already tested and still failed the mass comparison.

Therefore another adjustment to the dark spinor defect penalty will not supply the missing proton/electron hierarchy. A new term must act on the retained sector or change its physical charging action. When transporting the contact into the endpoint-rotor model, its gauge dressing and conserved lead-flux structure must be checked; it is not automatically the same unassisted matrix on the enlarged physical space.

Reusable checker: `research/voevodsky/checkers/check_interacting_elementary_reference.py`.

## 3. A unit-charged collective rotor is possible, but its action is different

`research/nima/mass-primitive-quotient-charge.md` repairs the earlier charge-1836 objection using the faithful quotient circle:

    T^N / image(B) = U(1), Phi=sum theta_s,
    Q=k-n_e,
    C_eff^-1=sum_s C_s^-1.

The primitive collective state and elementary state then have opposite unit charges. Equal inertias give the collective/elementary energy ratio N; unequal source-type inertias give 1944 with the same charge law. Thus a large collective charging cost and unit external charge are compatible, but the capacitance form still needs a source.

This is not the symmetric many-occupation trial we just excluded: it is a different constrained phase-space quotient and canonical inertia. Our equal-M bound does not apply automatically to it. Conversely, merely reusing equal inertias and the old normalized mediator would return to the excluded common-baseline mass branch.

`mass-path-operations-connect-comparison-ports.md` identifies the exact remaining dynamical issue. The actual 1836-slot path/readout graph is weakly connected, but has ten directed strongly connected components. Endpoint readouts have no supplied inverses. Kirchhoff current conservation Bj=0 is not the proposed charge-locking constraint B^T n=0. Turning that source incidence into reversible collective charging is a real unconstructed operation, not another count.

## 4. Relative neutral-record coefficients already have a shared-clock constructor

`research/voevodsky/single-clock-seam-record.md` applies the same involution generator to occupation reflection, seam-consistency reflection and record flip. It fixes epsilon=J=1, g=1/2, with all constants retained.

Its belt increment is 21(sqrt(5)-1)/2; the actual inactive record gap is sqrt(5), not the isolated occupation gap 1. This is a more uniform record construction than treating three coefficients as independently adjustable. It still cannot repair the charged-sector ratio when only belt controls are active.

## 5. Other searched shortcuts have concrete counterexamples

- `research/nima/mass-carrier-gram-spectrum-audit.md`: the 1836-slot tagged Gram Hamiltonian has rank 54, not 1836. Its maximum/minimum nonzero eigenvalue ratio is 64. The trace ratio 212976/121 is not a particle gap.
- `research/nima/scalar-action-weight-derivation.md`: fixed kinetic normalization, symmetry and factorization do not select a remaining contact coupling; two actions pass with different amplitudes.
- `research/nima/tower-energy-descent-trial.md`: dimensional restriction only gives a linear energy law under a specified distribution and metric. The old Higgs-number checker supplies no Hamiltonian or justified whole-budget calibration.
- `research/nima/triangle-source-contrast-clock.md`: actual source contrast repeats after three compositions, while retained word counts grow. No common physical frequency follows from that recurrence.

## Recommended next test

There are two non-equivalent directions, not one generic parameter sweep:

1. **Use already realized dynamics:** transport the exact belt collective sector and full electron contact into the same gauge-invariant endpoint/neutral interaction, preserving kinetic normalization, native complements, lead flux and common vacuum. Determine whether that composite interaction actually changes the proton/electron ratio; do not merely add belt records again.
2. **Pursue a new hierarchy mechanism upstream:** construct the history-retaining interaction which makes the primitive quotient charge-locking action physical, and derive its charging metric. The typed directed source graph and its inverse/readout obstruction provide concrete tests. Large ratios from assigned equal inertias alone are not new evidence.

The searched files do not supply a completed source-selected charging form fixing both mass comparisons. They do supply these sharper operations, exact source spectra and previously tested failures.
