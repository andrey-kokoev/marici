# The flux-labelled ground splits into two spinorial doublets, but selection needs cross-lead coherence

**Third batch, iteration 9 of 10.**

**Strength:** exact finite-group character decomposition and compressed-observable tests. Not physical spin identification or an implemented sector selector.

[Previous dressed projectors](DRESSED-FLUX-PROJECTORS.md) · [Checker](check_flux_ground_doublets.py) · [Receipt](results/flux-ground-doublets.v1.json)

## 1. Fresh ground representation

Each unit-lead block has one dressed ground vector g_i=r e_i+Qe_i. Keeping the four orthogonal lead labels gives a rank-four ground in sixteen matter/lead coordinates. All g_i have norm squared r^2+1, so the ground-coordinate metric is one common scalar times identity.

The native joint action permutes lead labels and transforms matter. Exact intertwiners show that its four-by-four ground-label matrix is numerically the same T as the prior line representation. This equality is not permission to act on matter while holding the lead fixed.

## 2. Exact spinorial decomposition

On ground-label coordinates define

    P_plus=(I+Q_label)/2,
    P_minus=(I-Q_label)/2.

They are orthogonal rank-two projectors commuting with all twenty-four native actions. The checker computes each restricted character and its complete group inner products:

    <chi_plus,chi_plus>=1,
    <chi_minus,chi_minus>=1,
    <chi_plus,chi_minus>=0.

Thus the summands are inequivalent irreducible doublets, each appearing once. The full representation commutant has dimension two and equals span{I,Q_label}. The plus character is exactly the native fundamental spinor character 2a for quaternion (a,b,c,d). The central minus-one acts as -I on both summands.

Here “spinorial” means the checked binary-tetrahedral representation and central action. It does not establish continuous physical rotation covariance, spin statistics or physical particle identity.

This corrects the stronger possible inference that no rank-two sector survives dressing: conditional joint sectors do exist. What remains is their preparation/selection, not their mathematical existence.

## 3. Existing simple observables do not select a summand

Assigned charge and ground energy act as qI4 and E_ground I4, so neither distinguishes the two doublets. Every fixed lead projector E_i fails to commute with P_plus: commutator rank two and plus-to-minus branch rank one, with squared Hilbert–Schmidt norm 1/4.

A fixed-label readout therefore changes the coherent doublet decomposition. A matrix commuting with all lead readers must be diagonal; native transitivity then makes it scalar if it also commutes with all symmetries. There is no nontrivial selector in that simultaneous commuting class.

The symmetry projectors are available mathematically, for example through finite-group representation data. Their off-diagonal ground-label entries require coherence across distinct lead-flux records. That operation is not supplied by a diagonal flux reader or a charge label.

## 4. Native matter return is not Q_label

The native line observable Q_matter acts as identity on the lead register. Its ground compression is

    cI4, c=2r/(r^2+1)=2/sqrt(v^2+4).

The corresponding native coherent projector compresses to (1+c)I4/2. Neither selects a ground doublet.

Moreover matter Q does not preserve the dressed ground: its leakage has rank four, with normalized squared norm v^2/(v^2+4) on every ground direction. At v=3/20 this is 9/1609. The checker verifies both compression and leakage exactly over the quadratic extension.

Thus the numerical conference matrix used on ground-label coordinates must not be mistaken for the same matter-only operator. Their carriers and operational meanings differ even though each involves Q.

## 5. Next source-dynamics gate

Inspect the owning endpoint/lead dynamics for an admitted coherent transfer between lead-flux sectors that preserves Gauss constraints and the dressed ground. If none is present in the tested operation class, state the missing interaction rather than claiming that group covariance implements a selector.

The existing free endpoint Hamiltonian conserves lead labels; its symmetry action is not automatically a dynamical flux-transfer coupling. A constructive enlargement must retain field history and nonselected doublet records, and specify any required controls and energy exchange.

The root remains null. Shared sources, atlas and formal outcomes are unchanged. No physical preparation, charge conjugation, annihilation or photon output is admitted.

## Reproduce

```sh
python research/scattering/seed-composition/check_flux_ground_doublets.py
python research/scattering/seed-composition/check_flux_ground_doublets.py --check
python research/scattering/seed-composition/check_seed_composition_net.py
python research/scattering/low-energy/check_low_energy_net_v3.py
```

Exact character arithmetic proves the decomposition using the stated finite-group character theorem. The checker reconstructs all prerequisite maps and tests the observable identities directly; no new machine-formal or physical admission is claimed. Only its local receipt is written; `--check` is read-only.
