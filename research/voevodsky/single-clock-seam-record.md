# A single-clock interface register: fixed spectrum, reversible recording

## What we constructed

The persistent-seam model previously left its record gap, binding strength and mixing strength separate. We now give an explicit common-rule realization with **no separately fitted record coefficients**:

1. occupation phase reflection;
2. seam-consistency parity reflection;
3. record flip.

Apply Nima's involution generator to each, using the same clock. This fixes the register spectrum, occupations and positive belt increment. The original coherent return survives.

This is a candidate identification of a neutral elementary interface resource, not an identification with the physical electron. Admitting these three operations as physical interactions is still model input. We have fixed their relative strengths by a declared uniform construction, not discovered them uniquely in geometry.

## 1. An actual seam can be recorded reversibly

Let P be one of the 21 source-derived mismatch projectors, and S=I-P in the carrier sector. For a two-level record define

    U = P tensor I + (I-P) tensor X.

This is a self-adjoint involution. With a ready record |0>, it records failure as 0 and success as 1 while retaining the carrier. In particular,

    U (|N> tensor |0>) = |N> tensor |1>.

Applying U again uncomputes the record. No carrier component or old history need be discarded; pre-existing history registers can remain spectators. For general inputs different seams do not commute: their addressed record gates must be undone in reverse order. The checker verifies this on two actual overlapping seams, with separate record bits.

This supplies a source-addressed reversible recording operation, reusing the history-retaining discipline of Nima's locking construction. It does not by itself make the record an energetic bond. Indeed its reversibility shows that an appended success bit alone does not have to remain present to sustain N.

## 2. The explicit bond-resource Hamiltonian

Set the common energy unit E*=pi*hbar/tau. For every admitted self-adjoint involution R use

    H_R/E* = (I-R)/2.

With n=|1><1| and the preceding S, choose

    R_occ  = I-2n,
    R_cons = I-2(n-S)^2,
    R_mix  = X.

The consistency expression is a projection because n and S are commuting projections on separate factors. Thus all three operations really are involutions. The record Hamiltonian becomes

    h/E* = n + (n-S)^2 + (I-X)/2.

In the previous dressing notation this fixes

    epsilon=1, J=1, g=1/2,

and retains the common +1/2 mixing constant. The existing seam formation projector has coefficient kappa=1 under the same clock. No individual proton/belt stage cost is adjusted.

The involution generator describes each operation separately. Summing these noncommuting contributions defines the new Hamiltonian; it does not claim that the combined evolution reproduces an old whole-Tick schedule at time tau.

## 3. The inactive and matched records have different spectra

In the occupation basis,

    h_inactive/E* = [[1/2,-1/2],[-1/2,5/2]],
    h_matched/E*  = [[3/2,-1/2],[-1/2,3/2]].

Their ground energies are

    lambda_v/E* = (3-sqrt(5))/2,
    lambda_b/E* = 1.

The positive relative energy per seam is fixed:

    delta/E* = (sqrt(5)-1)/2.

For all 21 declared belt interfaces, the extra contribution relative to inactive registers and equal bare carrier baselines is

    Delta E/E* = 21(sqrt(5)-1)/2.

This is a definite prediction of this candidate interaction, rather than a coefficient chosen to reproduce a mass difference.

## 4. The belt remains coherent

The preceding many-register proof needs kappa>delta, not the stronger sufficient assumption J>epsilon. Here

    0 < (sqrt(5)-1)/2 < 1 = kappa/E*.

Therefore the same positive-operator bound applies to the actual noncommuting seam projectors. The carrier ground state remains exactly N, and the record ground states are unique. Native threefold symmetry is preserved because all seam records have the same operations and clock.

Equal occupation and consistency strengths do not force a classical filled bit. The matched ground record is |+>, with

    <n>_matched = 1/2,
    <n>_inactive = 1/2-1/sqrt(5).

The excess occupation is 1/sqrt(5) per seam. This is persistent quantum dressing, not 21 immutable classical success bits. The reversible recording protocol in section 1 and this equilibrium record state are different constructions; the Hamiltonian does not preserve its classical readout indefinitely.

The energy contains interaction and mixing terms, not just occupation:

| Term, in E* units | Matched | Inactive |
|---|---:|---:|
| Occupation | 1/2 | 1/2-1/sqrt(5) |
| Consistency | 1/2 | 1/2-1/sqrt(5) |
| Mixing | 0 | (1-1/sqrt(5))/2 |

Their sum gives the stated relative energy. The checker verifies these expectations exactly.

## 5. Which elementary gap is the reference?

The isolated occupation involution has gap E*. But the **actual inactive record with all three interactions present** has excitation gap sqrt(5) E*. These must not be conflated.

Relative to that dressed inactive excitation, the predicted belt increment is

    Delta E/Delta_record = (21/2)(1-1/sqrt(5)).

Thus the construction supplies both a candidate neutral elementary excitation and a fixed comparison to it. Neither excitation has yet been identified with the physical charged electron or with the geometric spinor carrier. Setting one of these gaps equal to an electron mass would be a further identification, not a consequence of the shared clock.

The remaining test is now sharper: does the retained physical source support these three interface operations and this neutral record spectrum? A different answer changes the interaction law, not a freely adjustable stage coefficient inside this candidate.

## 6. Sources and verification

This reuses:

- Nima's `uniform-local-core-proof.md` involution generator;
- Nima's `mass-comparison-charged-core-dressing.md` two-level dressing mechanism;
- Nima's `mass-history-retaining-locking-interaction.md` retention discipline;
- the actual projectors in `native_operation_energy_lift_store.json`;
- the noncommuting many-register bound in `persistent-seam-occupation-energy.md`.

Run:

    python research/voevodsky/checkers/check_single_clock_seam_record.py

The checker verifies all 21 seam-record involutions and their action on N, a two-seam history reversal, exact spectral and occupation identities, and the strict stability inequality. Results are in `research/voevodsky/results/single_clock_seam_record.json`. The general many-register conclusion uses the preceding written positive-operator proof, not an enumerated 36*2^21 diagonalization.
