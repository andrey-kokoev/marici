# Neutron rest energy, iteration 1: test what the bound action determines

## Fresh calculation

Read the current occupied-closure receipt and verify its bound source hashes. On the exact 11-complex-dimensional closure, examine all eighteen port/frame generators P=(I-E)/2 using the inherited metric.

For the unit coherent neutron and empty bank, every initial pulse expectation is

    h=2099/53820.

But its exact generator-eigenstate residual is

    ||P psi-h psi||² = h(1-h)
                     =108562379/2896592400 > 0.

Thus this preparation is not a stationary ray of any addressed pulse generator. The previously calculated h is an interaction-pulse expectation, not an established rest eigenvalue.

## The shared stationary sector

Stack the eighteen projector constraints and solve their exact kernel. It has complex dimension one and is fixed by the actual native rotation. Every existing pulse energy vanishes there. The prepared coherent neutron has squared projection

    7301453/9333285

onto this common fixed line.

For each rank-one projector, its nonzero image fails to be an eigenline of another projector. Consequently there is no additional common positive-energy stationary ray for this pulse family.

This is a diagnostic of the already bound action, not a new general zero-mode discovery and not a claim that neutron rest mass is zero. A rest Hamiltonian need not coincide with every interaction pulse; such a Hamiltonian has not been selected here.

## Occupation energy cannot be inserted into the 11D closure unchanged

The existing closure is exact for pulses and rotation. Test the record-bank occupation projector on its basis in the faithful 13-dimensional preparation envelope. Adding those images increases the span from **11 to 13 complex dimensions**.

Therefore even that simple candidate charging observable is not an endomorphism of the smaller closure. Compressing an added charging dynamics into its eleven coordinates without retaining the extra directions would change the dynamics. No charging Hamiltonian was added by this test.

## The existing 21/4 result is a separate model

Freshly read `research/voevodsky/checkers/check_seam_occupation_energy.py` and its current receipt. Verify the bound native energy-lift digest. That model uses 21 additional neutral registers with coupling

    epsilon*n_e + J*(n_e-S_e)^2 - g*X_e,
    S_e=c-P_e.

Its 21/4 increment is at supplied epsilon=1/4, J=1/2, kappa=1, g=0, with vacuum subtraction and a supplied conserved carrier sector. These neutral registers are not the sixteen dynamical source-bank coordinates of the new canonical binding. The old checker was inspected, not freshly rerun in this iteration.

The prior recovered clock note also explicitly supplies angular advance, not physical seconds. No physical normalization was inferred from an endpoint cycle.

## Verification

```sh
python research/strominger/checkers/check_neutron_rest_energy_preflight.py
```

Six checks passed. All generator residuals, common-kernel basis, nonzero eigenline exclusion witnesses, the record-occupation enlargement and provenance:

`research/strominger/results/neutron-rest-energy-preflight.json`.

## Next executable step

Transport the actual 21 native seam controls into the retained neutron/bank representation. Determine their invariant closure before considering any reuse of the prior neutral-register Hamiltonian. This separates a legitimate sourced operator transport from merely copying its 21/4 energy onto the new binding.
