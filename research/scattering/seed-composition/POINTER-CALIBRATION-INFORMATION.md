# Eraser labels cannot calibrate the pointer phases they require

**Fourth batch, iteration 14 of 20.**

**Strength:** exact mismatched-feedback channel, calibration identifiability and retained independent-probe fixtures. Not measured coupling parameters or physical calibration apparatus.

[Previous partial-pointer eraser](PARTIAL-POINTER-ERASER.md) · [Checker](check_pointer_calibration_information.py) · [Receipt](results/pointer-calibration-information.v1.json)

## 1. Fresh mismatch calculation

Write actual gamma=cos(beta), v=sin(beta), with beta in [0,pi/2]. Let estimated gamma_hat and v_hat set the Y-readout phase feedback. Both estimates are normalized, but need not match the actual pointer.

The two residual phases are exp(±i(beta_hat-beta)). Their mean is

    d=gamma gamma_hat+v v_hat=cos(beta-beta_hat).

The actual reduced undo channel has coherence r²+(1-r²)d. Its Bell fidelity and retained terminal flag-one effect are

    F=1-(1-r²)(1-d)/2,
    E_flag1=2r²(1-r²)(1-d)Pi_high.

Small angular error gives infidelity (1-r²)(beta-beta_hat)²/4+O(error^4). Exact fixtures test four actual pointers against five estimates, including an angular midpoint, on both inverse-filter cases. Every readout and terminal branch remains accounted for.

## 2. The eraser record has no calibration signal

Both Y labels remain exactly one half for every actual pointer and every normalized feedback estimate. Repeated-label likelihood is 2^(-n), independent of beta; its Fisher information is zero. Adaptive feedback based solely on these labels does not supply the missing phase information.

The terminal flag can signal mismatch, but its rate is also multiplied by the unknown input weight tr(Pi_high rho). Low-eigenstate input gives zero terminal signal for every mismatch. Those flags are therefore not input-independent calibration data for arbitrary unknown input.

Uniform eraser labels protect the input from information leakage into that record; the same property prevents those labels from estimating this pointer parameter.

## 3. Independent calibration is an additional resource

A separate known-flag-one probe prepares the actual pointer state gamma|0>+v|1>. Z readout has probability v²=1-gamma² and hence identifies gamma from its ideal population law in this real nonnegative family.

The checker retains all Z records and their exact likelihoods for one, two, four and six independent probes under hypotheses gamma=3/5 and gamma=4/5. Every finite record has positive likelihood under both hypotheses.

Even optimal joint measurement of these independent product pointer states cannot discriminate them perfectly: their squared overlap is (24/25)^(2n)>0, with equal-prior guessing probability

    [1+sqrt(1-(24/25)^(2n))]/2<1.

This scope is independent product-state probes, not every possible coherent gate-oracle interrogation. Probe preparation, reset, sampling, controls and work are new resources; no device supplies them here.

## 4. Robust feedback rather than implicit exact knowledge

For a declared angular interval choose its midpoint estimate. It minimizes worst angular mismatch and guarantees

    F>=1-(1-r²)[1-cos((beta_max-beta_min)/2)]/2.

For the two illustrated hypotheses the midpoint has gamma_hat=v_hat=1/sqrt(2). The exact worst visibility is 7sqrt(2)/10, with square 49/50. This is a conditional error guarantee, not exact recovery for an unknown pointer.

Alternatively, access to the actual controlled copy's adjoint permits coherent inverse-copy control without an explicit parameter estimate. A forward unknown gate does not automatically supply that adjoint. Reversibility and access to every environmental copy remain separate obligations.

## 5. Next finite-confidence gate

Build a retained finite-probe calibration acceptance test with an explicit confidence/error budget. Propagate its parameter interval into a fidelity guarantee, keeping probe records and calibration-failure probability separate from unknown-state recovery. Do not promote finite statistical confidence into exact pointer knowledge.

Root outcome remains null. Shared sources, historical receipts, atlas and formal contracts are unchanged. No physical calibration, preparation, spin, annihilation or photon output is admitted.

## Reproduce

```sh
python research/scattering/seed-composition/check_pointer_calibration_information.py
python research/scattering/seed-composition/check_pointer_calibration_information.py --check
python research/scattering/seed-composition/check_seed_composition_net.py
python research/scattering/low-energy/check_low_energy_net_v3.py
```

Predecessor pointers are freshly recomputed. Exact root-mask arithmetic checks the mismatch channel; probe records and overlaps use rational arithmetic. Identifiability, minimax and state-discrimination bounds are explicitly scoped mathematics, not new formal or physical admission.
