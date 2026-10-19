# Gauge-preserving selector controls with a retained failure record

**Fourth batch, iteration 1 of 20.**

**Strength:** explicit conditional rotor/matter control factorization and exact coherent selection instrument. Not physical controllability or deterministic preparation.

[Previous cross-lead gate](CROSS-LEAD-SELECTION.md) · [Checker](check_retained_selector_controls.py) · [Receipt](results/retained-selector-controls.v1.json)

## 1. Fresh control factorization

For native monomial T_g|k>=t_k|pi(k)>, define

    F_pi: |k;n;ell> -> |k;n+ell-pi(ell);pi(ell)>,
    M_g:  |k;n;ell> -> t_k|pi(k);n+e_k-e_pi(k);ell>.

F changes lead momentum with a compensating endpoint translation. M changes matter with the usual assisted endpoint translation. Each fixes every G_i=n_i+ell_i+N_i, including away from their common zero kernel. They commute with one another, and

    U_hat_g=M_g F_pi

is a unitary native group representation. On physical n=-ell-e_k states it agrees with the earlier simultaneous matter/endpoint/lead permutation. Away from that kernel it is a different, individually gauge-preserving lift; commutation with the full Hamiltonian there is not asserted.

The checker verifies all 576 group compositions, all physical states from eighty flux fixtures and four matter labels, and corresponding off-kernel Gauss tests. These are unrestricted integer maps; fixture windows are not rotor cutoffs.

## 2. Explicit primitives, not implied source controls

Every pi is decomposed into at most three label transpositions. A field transposition swaps two lead momenta and applies the compensating endpoint shift controlled by their integer values. An assisted matter transposition exchanges the two matter labels with opposite endpoint shifts, fixing other matter labels. Native input phases complete M_g.

These are exact reversible maps on the declared Hilbert space. They require addressable assisted swaps, native phase control, momentum-controlled endpoint shifts and lead swaps. The fixed source Hamiltonian does not provide that control library merely because its individual hopping operators appear in the formula.

Intermediate stages need not preserve the dressed ground or charging energy. On physical basis states the checker records equal and opposite charging changes from F and M. Their final product is the ground-preserving source symmetry, but cancellation of net energy does not supply a physical work reservoir or a pulse implementation. The local receipt retains a nonzero work witness and a fixture maximum.

## 3. Coherent group controller and retained rejection

The character projector is P_full=sum_g alpha_g U_hat_g, with alpha_g=a_g/6 for quaternion scalar a_g. Its absolute coefficient sum is 5/3. Prepare a group controller with weights |alpha_g|/(5/3), apply sign(alpha_g) U_hat_g coherently, then unprepare the controller.

There are eighteen nonzero branches: two preparation probabilities 1/10 and sixteen probabilities 1/20. The success amplitude on the ground is

    B=(3/5)P_plus.

Keep the orthogonal controller failure rather than discard it. Before controller unpreparation its group components are

    R_g=sqrt(p_g)*(sign(alpha_g)T_g-B).

Exact checks give

    B*B=(9/25)P_plus,
    R*R=P_minus+(16/25)P_plus,
    B*B+R*R=I.

The receipt stores the full failure map, not just a success weight. Failure has rank four on the ground, retaining the entire minus doublet and some plus weight. Success selects plus conditionally, with probability (9/25)<P_plus>. It is not a deterministic state preparation or a mechanism for converting minus input to plus.

Reading the orthogonal group-history label before coherent recombination instead produces unitary branches preserving both sectors. It does not implement the interference-based selector. Coherent control, controller unpreparation and a final success/failure readout are explicit extra obligations.

## 4. Retained next test

Test failure-conditioned retries of this instrument. Quantify the all-failure branch and cumulative success probability while retaining the controller history and minus sector. Compare this with a fixed-lead readout, which disturbs the doublet decomposition. Do not substitute a single square-root failure operator for the actual multi-branch retained channel without checking equivalence.

Root outcome remains null. Shared sources, historical receipts, atlas and formal contracts are unchanged. No physical spin, annihilation or photon output is admitted.

## Reproduce

```sh
python research/scattering/seed-composition/check_retained_selector_controls.py
python research/scattering/seed-composition/check_retained_selector_controls.py --check
python research/scattering/seed-composition/check_seed_composition_net.py
python research/scattering/low-energy/check_low_energy_net_v3.py
```

The prerequisite chain and native maps are freshly recomputed. Exact field arithmetic checks instrument completeness; group/rotor statements remain explicitly scoped mathematical arguments rather than machine-formal or physical admission.
