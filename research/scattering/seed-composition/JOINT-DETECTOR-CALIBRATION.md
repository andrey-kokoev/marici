# Joint detector calibration resolves diagonal bias, but coherence remains a model gate

**Fourth batch, iteration 20 of 20.**

**Strength:** exact three-stream confidence, inverse intervals and contrast-conditioned fidelity certificate; explicit coherent-detector counterexample. Not physical reference preparation or detector validation.

[Previous error floor](CALIBRATION-MODEL-ERROR-FLOOR.md) · [Checker](check_joint_detector_calibration.py) · [Receipt](results/joint-detector-calibration.v1.json)

## 1. Fresh additional calibration observables

Supply separate known-pointer-zero and known-pointer-one preparations. For a diagonal detector E1=diag(a,1-b), their Z populations are a and 1-b. A copy-pointer stream has

    q=a+(1-a-b)p.

Use known-one misses to estimate b, retaining its original ordered outcomes. The same detector parameters and exact preparation model must apply across all streams. These are added resources, not native source features.

Each stream has radius 1/2000 and 26,000,000 probes. A dyadic Hoeffding certificate bounds each noncoverage probability by 1/4096, giving simultaneous noncoverage ≤3/4096<1/1000. Total cost is **78,000,000 probes**. No physical observations are supplied; fixtures use explicitly simulated counts.

## 2. Exact interval inversion and conditioning

For confidence boxes in q,a,b with certified positive slope, the pointer enclosure is

    p_low =clip((q_low-a_high)/(1-a_high-b_low)),
    p_high=clip((q_high-a_low)/(1-a_low-b_high)).

The checker verifies 96 enclosures and 768 corner tests. If the slope is uncertified/nonpositive, abstain and retain records. The release condition requires slope lower bound at least 19/20.

Along the interval-extreme path, the inverse derivative is bounded by

    [delta q+(1-p)|delta a|+p delta b]/slope_lower.

Thus its population width is at most 4epsilon/slope_lower≤1/475. This is a conditioning certificate, not permission to assume detector contrast before calibration.

The two preceding q=1/100 nuisance models now have different reference-probe populations and disjoint pointer intervals. The added observables genuinely break that diagonal-model ambiguity.

## 3. Residual drift still applies

Keep the declared rho with cos(rho)=2499/2501. The maximum angular width for a population interval of width 1/475 passes the exact drift-aware **99.9%** fidelity threshold. The checker certifies this comparison in Q(sqrt(111)).

On simultaneous coverage and contrast release, angular-midpoint control therefore meets the target. Unconditional bad-release probability is ≤3/4096 under the declared model and controls. That is not automatically the same confidence conditional on contrast acceptance, nor a reusable repeated-test budget.

The earlier drift-only 99.99% obstruction remains. More detector probes do not supply future deployment information.

## 4. Zero/one references do not validate detector diagonality

A positive complete coherent POVM can have

    E1=[[1/200,1/200],[1/200,199/200]].

Known-zero and known-one probes still report a=b=1/200. For the real plus pointer, true p=1/2 but observed q=101/200 due to the off-diagonal term. All three population intervals cover their actual populations, yet the diagonal-model pointer interval excludes 1/2 and its contrast check passes.

This is an out-of-model counterexample, not a claimed fidelity violation from this particular small perturbation. It shows that reference-population confidence does not establish diagonality. The new detector assumption remains explicit and unadmitted.

## 5. Nonredundant continuation after batch completion

Test detector tomography using supplied superposition references and controlled pointer phase flips. Determine whether phase-cycled populations cancel the off-diagonal term without assuming it absent, retaining confidence, contrast, phase-control and deployment obligations.

The fourth batch is complete; the scientific root is not. Root outcome remains null. Shared sources, historical receipts, atlas and formal contracts are unchanged. No physical calibration, preparation, spin, annihilation or photon output is admitted.

## Reproduce

```sh
python research/scattering/seed-composition/check_joint_detector_calibration.py
python research/scattering/seed-composition/check_joint_detector_calibration.py --check
python research/scattering/seed-composition/check_seed_composition_net.py
python research/scattering/low-energy/check_low_energy_net_v3.py
```

Predecessor nuisance models are freshly recomputed. Exact rational intervals, confidence certificates and radical comparisons verify the receipt. Monotonicity and width propagation are scoped mathematical arguments, not new formal or physical admission.
