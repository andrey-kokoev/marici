# Cycle reversal can be antiunitary without reversing the native charge operator

**Third batch, iteration 4 of 10.**

**Strength:** exact cycle intertwiners, charge-sector obstruction and source-library axis test. Not physical charge conjugation, time reversal or annihilation.

[Previous native adapter](NATIVE-INTRINSIC-SPINOR-ADAPTER.md) · [Checker](check_antiunitary_charge_gate.py) · [Receipt](results/antiunitary-charge-gate.v1.json)

## 1. Fresh question and explicit frame

The previous turn found that the inverse transported five-cycle differs from entrywise conjugation in the native/intrinsic adapter frame. That does not exclude an antiunitary with an additional unitary coefficient map.

Let K denote coefficient conjugation in that frame and

    X=[[0,1],[1,0]], C=X K.

For both global doublets and both chiralities, exact arithmetic verifies

    C^2=I,
    X conjugate(U) X*=U^-1.

Thus an explicit antiunitary implements reversal of the selected cycle. Its existence repairs that representation comparison; it does not identify inverse arrows with physical charge conjugation.

A distinct familiar antiunitary is

    Theta=epsilon K, epsilon=[[0,1],[-1,0]].

It has Theta^2=-I and preserves the tested SU(2) actions rather than inverting them. The checker verifies that distinction across all source-bound cases. Neither operator is labelled as physical time reversal by this calculation.

## 2. Raw native carrier and retained complement

If J is the native eight-by-two coherent encoding, the coefficient matrix of C on its image is

    M=J X J^t,
    x -> M conjugate(x).

Exact identities are

    M conjugate(M)=N,
    M M*=N,
    M* M=conjugate(N).

This antiunitary acts on the native rank-two coherent domain. It is not an invertible map on all eight raw coordinates by itself; the rank-six complement remains separately retained as established by the preceding adapter.

## 3. It preserves qN, and the obstruction is not candidate-specific

The owning spinor construction permits the charge family Q_q=qN. For tested q=-2,-1,0,1,2,

    M conjugate(Q_q) M*=Q_q,

not -Q_q unless q=0.

More generally, on the coherent doublet Q_q is the real scalar qI. Every within-sector antiunitary fixes that scalar. It cannot conjugate qI to -qI for nonzero q: the spectra differ. Thus searching for another within-doublet antiunitary does not resolve the charge-reversal gate for this family.

This is a statement about the explicitly retained charge family, not a derivation that physical electric charge equals qN. It leaves broader sector-changing charge constructions open.

## 4. One cycle is different from the full enlarged library

The fixed C above does not invert every added triangle transport. Across the baseline five-cycle and the five added diagonal-triangle cases, their logical SU(2) axes span three dimensions in each chirality/doublet.

An antiunitary conjugation induces an improper orthogonal map O on Pauli observables. For U=aI+i*n.sigma, inversion requires O*n=n because antiunitarity also flips i. Three independent fixed axes would force O=I, which is not improper. Hence no single antiunitary inverts the entire **tested enlarged library** in one fixed logical frame.

This does not rule out a cycle-specific antiunitary, an antiunitary for a smaller two-generator subset, or sourcewise affine inverse generators. The source inverse-library rule can still be defined separately. It simply is not one universal antiunitary on these logical doublets.

## 5. A doubled charge-flipping construction exists only conditionally

Introduce two explicit logical sectors with assigned charges +q and -q and cycle blocks U and U^-1:

    D=diag(U,U^-1), Q_double=q*diag(I,-I).

Swapping sectors together with X K gives an antiunitary that preserves D as a tagged representation and flips Q_double. Exact four-dimensional matrix checks verify both identities and square +I.

This shows that sector enlargement can evade the within-doublet scalar-charge obstruction. It does not derive the opposite charge assignment, sector swap, physical species labels or a native implementation. The original seed reversal alone did not supply those data.

## 6. Next executable source gate

Compare this conditional doubled construction with the owning external-charge and quotient-charge mechanisms. Determine whether they supply the actual opposite-charge operator and sector-changing map on the checked spinor carrier, or require another adapter. Retain carrier dimensions, charge assumptions and reservoirs rather than assigning +q/-q to geometric seed names.

The root remains null. No photon output, annihilation, physical conjugation or preparation is admitted. Shared atlas, stores and formal contracts are unchanged; the earlier historical producer-hash caveat remains visible in prerequisite evidence.

## Reproduce

```sh
python research/scattering/seed-composition/check_antiunitary_charge_gate.py
python research/scattering/seed-composition/check_antiunitary_charge_gate.py --check
python research/scattering/seed-composition/check_native_intrinsic_spinor_adapter.py --check
python research/scattering/seed-composition/check_seed_composition_net.py
python research/scattering/low-energy/check_low_energy_net_v3.py
```

Exact multiquadratic arithmetic checks the operators and axis ranks. The general charge and axis obstructions use the explicit linear-algebra arguments above, not a new machine-formal admission. Prerequisites are recomputed; only the local receipt is written, and `--check` is read-only.
