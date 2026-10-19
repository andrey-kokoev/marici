# More probes cannot remove observationally hidden detector and deployment uncertainty

**Fourth batch, iteration 19 of 20.**

**Strength:** valid detector POVMs, identical observation laws and exact stricter-target obstructions. Not a no-go for added observables or coherent apparatus control.

[Previous precision refinement](CALIBRATION-PRECISION-REFINEMENT.md) · [Checker](check_calibration_model_error_floor.py) · [Receipt](results/calibration-model-error-floor.v1.json)

## 1. Fresh nuisance models with the same records

A binary detector with false-positive a and false-negative b gives

    q=a+(1-a-b)p.

Its diagonal effects are positive and sum to identity. Consider:

- Model A: a=1/100, b=0, true calibration p=0; deployment angle zero.
- Model B: a=0, b=1/100, true calibration p=1/99; deployment angle asin(sqrt(1/99))+rho.

Both have observed q=1/100. Both even satisfy a global population-bias bound: |q-p|≤max(a,b)≤1/100. Their deployment changes obey the declared drift bound.

Every ordered iid Z-probe word has the same likelihood in both models; the checker enumerates finite examples. The formula establishes equality for any sample count. Y eraser labels likewise remain uniformly parameter independent. The observation scope is these Z records and Y labels, not additional detector tomography, known-input phase probes or gate-adjoint access.

## 2. A stricter target is not identifiable

The deployment angle gap is

    Delta=asin(sqrt(1/99))+rho,
    cos(Delta)=(2499sqrt(98)-100)/(2501sqrt(99)).

Exact positive-radical comparisons give cos(Delta)<119071/120050, so the best common worst-angle visibility is strictly below 489/490. On the source-bound witnessed minus filter, 1-r²>49/50; consequently worst-model Bell infidelity is strictly greater than 1/1000.

Thus more of the allowed records alone cannot uniformly certify 99.9% fidelity for this calibration-based phase-feedback protocol. This is model ambiguity even at zero sampling error, not a finite-confidence tail.

Because the observation laws coincide, randomized policies do not restore identifiability. With always-release feedback, at least one model has target-success probability at most one half. If both models require bad-release probability ≤delta, their common release probability must be ≤2delta. At delta=1/1000, high-probability release is incompatible with this stricter uniform target.

These statements do not exclude extra coherent controls or new calibration measurements. They concern a common policy inferred from the stated indistinguishable records.

## 3. Drift alone leaves another floor

Even with ideal detector and exact calibration p=q=1/2, deployment may be at pi/4-rho or pi/4+rho. The optimal common worst visibility is cos(rho)=2499/2501.

For the same source witness, Bell infidelity is strictly greater than

    49/125050>1/10000.

Therefore 99.99% fidelity needs tighter drift bounds, deployment information or additional compensating control. Detector calibration alone cannot remove this floor.

The preceding 99% release certificate is not invalidated: it targets a weaker fidelity under these very bounds. Shrinking the sampling radius removes sampling uncertainty, not bias/drift ambiguity.

## 4. Additional observables can break the detector ambiguity

Separately supplied known-pointer-zero and known-pointer-one probes have detector populations a and 1-b. Combining them with the pointer-copy population q identifies

    p=(q-a)/(1-a-b)

when the slope is positive. Those preparation/readout capabilities are new resources, not contained in the original unknown-pointer Z records. They still do not measure future deployment drift.

Next construct a retained joint detector/pointer interval with confidence spending and slope conditioning, then propagate the residual drift. Keep supplied reference preparations and detector controls distinct from native source admission.

Root outcome remains null. Shared sources, historical receipts, atlas and formal contracts are unchanged. No physical calibration, preparation, spin, annihilation or photon output is admitted.

## Reproduce

```sh
python research/scattering/seed-composition/check_calibration_model_error_floor.py
python research/scattering/seed-composition/check_calibration_model_error_floor.py --check
python research/scattering/seed-composition/check_seed_composition_net.py
python research/scattering/low-energy/check_low_energy_net_v3.py
```

Predecessor refinement tests are freshly recomputed. Exact POVM, likelihood and radical inequalities verify the receipt. Minimax, identifiability and randomized-policy bounds remain explicitly scoped mathematical arguments, not new formal or physical admission.
