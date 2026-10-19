# Occupied-sector action from the retained carrier metric

## The upstream candidate

Use the exact native return space E=im(N) with its supplied positive metric. Let r=dim_C E. Adopt the full unit sphere S(E), not the discrete stage graph and not a phase-only circle inside a larger carrier.

Following the prior normalized-overlap kinetic readout, take

    L = (F²/2)||D_t z||²,  ||z||=1,
    D_t z=dot(z)-i q_external A0 z.

In a local phase direction, the normalized real overlap is cos(theta). The readout -log(cos(theta))/2 has expansion theta²/4+theta⁴/24+..., so twice its diagonal Hessian gives the unit tangent metric. Use the same metric rule on the complete sphere.

Quantize by the scalar Laplace-Beltrami operator, with no added curvature potential:

    H=-(hbar²/(2F²)) Delta_S.

The common internal phase U(1) conserves momentum k. Declare occupied sectors k=+1; the external charge is q_external*k, with multipliers +1,0,-1. The neutral sector therefore has an internal conserved occupation without assigning it electric charge. Empty space is a separate zero-energy, zero-charge state.

This is a declared kinetic action and quantization on normalized carrier amplitudes, not an assertion that a Hilbert-space metric alone mandates quantizing its state sphere. The charge-sector choice is explicit. No physical mass enters the action.

Contract: `contracts/retained-carrier-kinetic-action.json`.

## Derive the complete occupied-sector ground

The sphere has real dimension d-1=2r-1. In polar coordinates, a degree-l homogeneous harmonic polynomial obeys

    Delta_S Y_l = -l(l+d-2)Y_l.

A polynomial of complex bidegree (p,q) has phase weight p-q and degree l=p+q. Thus k=1 requires p=q+1 and first occurs at l=1. Its lowest harmonics are the r holomorphic coordinate functions. All higher admissible degrees have higher energy.

Consequently

    E_ground = [hbar²/(2F²)](2r-1),
    multiplicity = r.

The occupied ground dimension therefore reproduces the native single line or doublet without inserting a desired degeneracy. The choice of action supplies the energy, not the projector support count.

The checker verifies the actual metric/projector identities and counts charged harmonic kernels using exact polynomial Laplacians. The all-degree lower bound is the increasing expression l(l+d-2), not an extrapolation from sampled levels.

## Results at common hbar=F²=1

| Carrier | Native complex rank | Configuration sphere | Occupied ground | Multiplicity | External charge |
|---|---:|---|---:|---:|---:|
| Proton | 1 | S1 | 1/2 | 1 | +1 |
| Neutron | 1 | S1 | 1/2 | 1 | 0 |
| Electron | 2 | S3 | 3/2 | 2 | -1 |

All occupied energies are positive above the common empty state. Unlike the unoffset contact model, this action does not create a negative occupied sector.

Its ratios are nevertheless wrong:

    E_p/E_e = 1/3,
    (E_n-E_p)/E_e = 0.

Changing the common F or hbar cannot alter these ratios.

The first electron k=1 blocks have energies 3/2,15/2,35/2,63/2,99/2 and multiplicities 2,4,6,8,10. Keeping only its phase circle would instead give 1/2 and erase the transverse sphere dynamics. That would be a different action, not a simplification of this spectrum.

## What this isolates

This candidate supplies an actual positive occupied-sector energy law with canonical momentum, conserved charge and a common vacuum, rather than just a formation constraint or a contact offset. It fails because it uses only the normalized retained metric space: both proton and neutron are rank-one spaces, so the action cannot distinguish them, and its rank-two elementary sphere has the higher first harmonic energy.

The structural implication is broader than this particular spectrum: any isometry-natural action depending only on a normalized rank-one return and its metric loses the source information distinguishing proton from neutron. A successful next input must retain additional source dynamics, a charging form or a collective constraint—not rescale an unnormalized state to obtain a desired inertia.

The actual graph kinetics and collective constraints are available elsewhere, but their choice as occupied-sector dynamics still needs an explicit rule. This experiment does not claim to have selected that rule uniquely.

## Verification

```sh
python research/strominger/checkers/check_retained_carrier_kinetic_action.py
```

Eleven reported checks passed. All common-protocol source and packet hashes were verified before use. The held-out reference was opened after the spectrum and ratios were derived. No shared scientific file was changed.

Receipt: `results/retained-carrier-kinetic-action.json`.
