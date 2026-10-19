# Flux-dependent dressed planes are jointly covariant, not one fixed matter doublet

**Third batch, iteration 8 of 10.**

**Strength:** exact algebraic spectral projectors, a common-carrier obstruction and native binary-tetrahedral covariance with retained lead labels. Not physical spin identification or preparation.

[Previous charged closure](CHARGED-SPINOR-CLOSURE.md) · [Checker](check_dressed_flux_projectors.py) · [Receipt](results/dressed-flux-projectors.v1.json)

## 1. Fresh dressed construction

The original coherent doublet is not closed under unit-charge endpoint charging. This turn constructs its dressed replacement separately for each unit-lead flux block, rather than projecting the interaction back onto the old carrier.

Remove the common scalar charging offset and write

    H_i=K-v E_i, v=beta/4>0,
    r=(v+sqrt(v^2+4))/2, r^2-vr-1=0.

The executable works exactly over the prior multiquadratic complex field enlarged by real r. No numerical eigenvectors are fitted.

For z_i=e_i+Qe_i and g_i=r e_i+Qe_i, define

    G_i=g_i g_i*/(r^2+1),
    Z_i=P-z_i z_i*/2,
    Pi_i=G_i+Z_i.

Exact identities give:

- G_i is the rank-one ground projector with eigenvalue 1-r;
- Z_i is the retained rank-one zero-eigenvalue projector;
- Pi_i is Hermitian, idempotent, rank two and commutes with H_i;
- the complementary eigenvalues are 1+1/r and 2.

Thus Pi_i is the dressed low two-plane. It is not an energy-degenerate doublet at positive v. Both low and complementary records remain available.

## 2. There is no common fixed matter two-plane

Exact elimination finds the intersection of all four im Pi_i is zero. This rules out identifying their overlapping matter coordinates as one shared low carrier.

A stronger operator argument excludes any common nontrivial invariant subspace for the four unchanged Hermitian H_i. Its orthogonal projector would commute with all H_i and hence with

    H_i-H_j=-v(E_i-E_j).

Those diagonal differences force that projector to be diagonal. Every off-diagonal K entry is nonzero, so commutation with K forces all its diagonal entries equal. A scalar projector is either zero or identity.

The obstruction concerns a **fixed matter carrier across all fixed unit-lead blocks**. It does not exclude a carrier that retains and transforms the lead label.

## 3. The actual native symmetry transports dressed sectors

The checker reconstructs all twenty-four native binary-tetrahedral actions from the existing quaternion/face-projector rule. It does not fit transports from the new Pi_i. Passing those actions through the exact native-to-line adapter yields unitary four-coordinate matrices T and their face permutations pi.

For every action and each lead i, exact checks give

    T H_i = H_pi(i) T,
    T Pi_i T* = Pi_pi(i),
    T G_i T* = G_pi(i).

All 576 group compositions are verified, and the native central minus-one acts as minus identity. To preserve the full interaction, the same permutation must act on the lead-flux record. Holding that record fixed while rotating only the matter part is a different operation.

The direct sum over the four orthogonal flux labels has:

    dressed low rank: 8,
    dressed ground rank: 4.

This gives genuine conditional joint covariance despite the failure of a fixed matter doublet. It does not identify that symmetry with physical spin rotations, nor select a rank-two physical sector from the four-dimensional ground.

## 4. Retention and next representation test

Lead labels are not erased. The four-dimensional ground degeneracy originates in four equal-energy but orthogonal flux sectors. A possible spinorial decomposition of that joint representation must be calculated, not inferred from multiplicity alone.

Next decompose the rank-four flux-labelled ground under the native binary-tetrahedral group. Test whether rank-two spinorial sectors exist, and whether the retained source/charge/flux observables select one without dropping lead history or inserting a new interaction.

The native rank-two line-mismatch and rank-four polarization records remain accounted for. No physical charge conjugation, emission or annihilation is derived. The root stays null and shared source/atlas/formal contracts remain unchanged.

## Reproduce

```sh
python research/scattering/seed-composition/check_dressed_flux_projectors.py
python research/scattering/seed-composition/check_dressed_flux_projectors.py --check
python research/scattering/seed-composition/check_charged_spinor_closure.py --check
python research/scattering/seed-composition/check_seed_composition_net.py
python research/scattering/low-energy/check_low_energy_net_v3.py
```

Exact quadratic-extension arithmetic checks all ranks and projectors; native actions and field/face data are reconstructed from freshly recomputed prerequisites. Only the new local receipt is written; `--check` is read-only.
