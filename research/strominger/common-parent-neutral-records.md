# Neutral seam records coupled to the common endpoint parent

## Construction

Attach the existing neutral seam-occupation law to the signed endpoint parent. Do not assign a scalar energy to the belt sector. Retain the 21 actual seam projectors, one two-state register per seam, and the complete interaction

    h_e = epsilon n_e + J(n_e-S_e)^2 - g X_e,
    S_e = c_belt(I-P_e).

The source local groups are unchanged: proton has twelve single-triangle groups, belt has three six-triangle groups, and elementary spinor has four single-face-line groups. Only the belt grouping admits the 21 existing within-group triangle seams. This model supplies the record/control policy; it is not inferred solely from geometric incidence.

The same 21-register pool is present in every sector and in the vacuum. Outside the belt, all controls S_e vanish and the records occupy their inactive ground. Subtract this one common inactive ground energy, including for nonzero g. Registers are neutral and the belt has external charge zero, so these controls commute with the endpoint Gauss generators.

## Exact native operator attachment

The checker reconstructs the 36-to-18 belt mode embedding and decoder from the stored intrinsic coefficients and metric. For every native seam it verifies

    P_e(native) V = V P_e(selected).

On the weighted selected-mode space, the actual projector for seam i,j is

    gamma = m_i m_j/(m_i+m_j),
    P_ii=gamma/m_i, P_ij=-gamma/m_i,
    P_ji=-gamma/m_j, P_jj=gamma/m_j.

It verifies metric orthogonality, idempotence, rank one and preservation of the native return. The retained kinetic operator decomposes exactly as

    K_belt = A_alignment + sum_e P_e,

where A_alignment is a positive weighted graph Laplacian reconstructed from the remaining native edges. No desired ground projector is inserted into K.

## Joint ground theorem

The existing local record certificate gives inactive/matched ground energies e_v,e_b. Put delta=e_b-e_v. For each seam,

    h_e-e_v I >= delta(I-P_e).

This holds as an operator inequality even though different seam projectors do not commute. Summing and using the native K decomposition gives

    H_joint - 21 e_v I
      >= 21 delta + A_alignment + (1-delta)sum_e P_e
                   + H_endpoint_field.

With the inherited epsilon=1/4 and J=1/2, all tested g satisfy 0<delta<=1/4<1. The constant belt amplitude, zero endpoint/lead flux and product of matched record ground states attain the bound. Thus its exact joint ground energy is **21 delta**, and its matter return survives.

This proof covers the complete record space, rather than diagonalizing a truncated 18 times 2^21 matrix. The charged sectors retain their prior ground energies because their record controls vanish and the same inactive energy is subtracted.

## Results

At g=0, delta=1/4:

| Carrier | Common-vacuum ground energy |
|---|---:|
| Electron | 0.4721914439934211… |
| Proton | 0.5491721529617364… |
| Neutron belt | **21/4 = 5.25** |

The inherited mixing trials are also exact:

| g | Belt energy |
|---|---|
| 0 | 21/4 |
| 1/8 | 21(sqrt(10)-sqrt(2))/8 |
| 3/8 | 21(3sqrt(2)-sqrt(10))/8 |

At zero mixing,

    E_p/E_e = 1.1630285977172172…,
    (E_b-E_p)/E_e = 9.955343127953329….

The belt now has positive stored energy from explicit operators. The numerical mass comparison still fails. Varying these neutral record parameters cannot repair the unchanged proton/electron ratio: this interaction has no nontrivial control in either charged sector.

## Verification

```sh
python research/strominger/checkers/check_common_parent_neutral_records.py
```

Seven reported checks passed, plus the exact native projector, metric, embedding and local spectral assertions. Parent hashes and the weighted source's native-energy-store hash are checked. Shared stores are read only.

Receipt: `research/strominger/results/common-parent-neutral-records.json`.

This composes two prior admitted model ingredients under one vacuum reference. It retains their supplied local grouping, charging metric and register law; it does not replace them with arrow-count energies or fitted species offsets.
