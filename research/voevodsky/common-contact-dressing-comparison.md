# A shared contact-dressing law orders the belt above the proton

## Result

Using the same normalized local shared-edge contact, the actual proton response is strictly larger than the actual belt response below their spectra. Under an identical stable reference coupling, this makes the proton branch shift down farther, leaving the belt branch higher.

This is a source-specific ordering result without separate proton/belt offsets, record gaps or fitted stage costs. It is conditional on the common coupling law and selected source interfaces; it is not yet a physical neutron mass prediction.

## Prior work reused

- Nima's `interface-required-record.md` already studies the source-marked proton AB/BA interface. We reuse that address, not invent a replacement proton geometry.
- The collective carrier spectrum and the odd/even belt response calculations supply the current Hamiltonians and mode decomposition.
- The previous coherent-port vacuum test supplies the Schur stability condition and distinguishes an excitation block from the empty vacuum.
- Prior emission and charge-sector audits retain the requirement for a charge-compatible reference field or reservoir.

The new calculation compares the two actual source responses under one common rule.

## 1. Match the locality and normalization

The proton contact is the symmetric combination of its AB and BA triangle modes, which share an actual edge. The belt contact is the symmetric combination of triangle modes 0 and 3 in **one** paired sector.

Both contacts are normalized in their original physical metrics. In particular, the belt contact is not the three-sector coherent average used in the preceding even-sector calculation. Comparing that average with a single local proton contact would change the probe protocol.

The proton's contact weights at energies 0, 1/2, 1 and 3/2 are

    1/6, 0, 1/2, 1/3.

For the belt, let

    lambda=(0,4485/3292,5391/3292),
    r=(1193/4485,2099/8970,1/2).

The local contact has weights r/3 at lambda and 2r/3 at lambda+3/4. This follows from resolving a single sector into its three rotation characters. The checker verifies the resulting weights against the actual 36-dimensional operator using exact moments and an annihilating polynomial.

The lowest face-odd soft mode is absent from this symmetric contact. A carrier's smallest excitation alone therefore does not determine its response to a specified external field.

## 2. An exact response ordering

For positive t define the below-spectrum response

    R_s(t)=<w_s,(H_s+tI)^(-1)w_s>
          = sum_j r_sj/(lambda_sj+t).

The computed rational functions satisfy

    R_proton(t)>R_belt(t) for every t>0.

This is not a scan over selected parameters. After multiplying by the positive denominators, their difference has nonnegative rational polynomial coefficients, with strictly positive coefficients present. The complete certificate is retained in the result JSON.

## 3. A common stable reference law

Supply the same bare carrier offset mu, reference energy epsilon, and nonzero exchange strength g to both carriers:

    H_s,dressed = [[epsilon, g<w_s|],
                   [g|w_s>, H_s+mu I]].

Take epsilon>mu>0 and require

    epsilon>g^2 R_proton(mu).

The proton inequality also ensures belt stability because its response is smaller. Both excitation blocks then lie above an empty zero-excitation reference of energy zero.

The lowest pole E_s solves

    epsilon-E_s-g^2 R_s(mu-E_s)=0,
    0<E_s<mu.

Each left side decreases strictly in E. At the proton root, the belt's left side is positive, so its root lies higher:

    E_belt>E_proton.

For epsilon>mu these branches tend to their original coherent carriers as g tends to zero. The ordering therefore does not rely on relabelling a low reference excitation as a nucleon.

## 4. An illustrative, unfitted check

With shared epsilon=1, mu=1/2 and g=1/2:

| Carrier-connected excitation | Energy in common units |
|---|---:|
| Proton | 0.403236457334 |
| Belt | 0.445750886936 |
| Belt minus proton | 0.042514429602 |

The checker encloses both roots with exact rational brackets. These parameter values are a stability/example test, not a calibration to the neutron mass.

At finite coupling the state is dressed: it contains reference amplitude and internal carrier excitations. It is **not exactly the bare rank-one return N**. The report includes the reference occupation and the coherent fraction of the carrier component, evaluated numerically from the certified pole brackets. The source carrier operators themselves are retained unchanged.

## 5. What this establishes and what it does not

The mechanism now has a different form from independent seam energy: **unequal collective response produces unequal dressing under equal input parameters**. The sign of the splitting follows from the actual source response ordering, rather than a separately chosen belt energy offset.

However, the common reference law remains supplied. In particular:

- A charged proton excitation requires a charge-compatible reference or reservoir. One neutral oscillator cannot simply be used to create both a charged proton and a proposed neutral belt.
- The physical origin of epsilon, g, mu and the common energy unit has not been derived.
- A different physically selected contact may have different weights; this theorem concerns the explicitly marked local interfaces tested here.
- No relation to the electron mass, atomic-mass unit or relativistic mass pole has been established.

Thus this is a concrete common-law candidate with a robust ordering, not a completed neutron mass derivation. The next identification is the charge-compatible reference interaction, not a particle-specific adjustment of the computed response.

## Verification

    python research/voevodsky/checkers/check_common_contact_dressing.py

Results: `research/voevodsky/results/common_contact_dressing.json`.

Exact checks cover the source contacts, spectral weights, all-positive response-difference certificate, common-vacuum stability and pole brackets. No measured mass is used.
