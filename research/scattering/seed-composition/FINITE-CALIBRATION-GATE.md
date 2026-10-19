# Finite calibration can certify a fidelity gate, not exact pointer knowledge

**Fourth batch, iteration 15 of 20.**

**Strength:** certified fixed-sample confidence, exact release inequalities and retained selection-risk fixtures. Not observed calibration data or a formal physical acceptance contract.

[Previous calibration-information gate](POINTER-CALIBRATION-INFORMATION.md) · [Checker](check_finite_calibration_gate.py) · [Receipt](results/finite-calibration-gate.v1.json)

## 1. Fresh declared sampling model

Supply 512 independent known-flag-one Z-pointer probes with constant population p=v²=sin²(beta). Let k be the number of ones. The declared recorder must retain the ordered probe word; k is an analysis statistic, not permission to erase that record.

No physical probe word is supplied here. The checker accounts for all 2^512 possible words through exact binomial multiplicities, not by claiming they were measured or enumerating them individually.

The assumptions are iid probes, one pointer parameter throughout calibration and deployment, ideal population readout and independent preparation/reset. These are added model/resource inputs.

## 2. Certified confidence without floating exponentials

Use radius epsilon=1/10 and interval

    p in [max(0,k/512-epsilon), min(1,k/512+epsilon)].

Hoeffding gives noncoverage probability at most 2 exp(-256/25). The checker lower-bounds exp(256/25) by its first thirteen positive Taylor terms, obtaining a rational upper bound below 1/1000. Thus unconditional coverage is at least 999/1000 for every fixed p under the declared iid model.

Exact binomial fixtures at seven populations, including endpoints, compute noncoverage, acceptance and accepted noncoverage probabilities. All count outcomes, including abstentions, are recorded.

## 3. Exact interval-to-fidelity release

Map the population endpoints to beta_low=asin(sqrt(p_low)) and beta_high=asin(sqrt(p_high)). Choose the **angular** midpoint for feedback. Endpoint visibility is

    d_end=sqrt((1-p_low)(1-p_high))+sqrt(p_low*p_high).

Worst midpoint visibility is sqrt((1+d_end)/2). Release the 99% Bell undo-fidelity guarantee only if

    d_end>=1151/1250,

which is equivalent to midpoint visibility at least 49/50. Indeed for either inverse-filter ratio,

    F>=1-(1-r²)(1-d_min)/2>=(1+d_min)/2>=99/100.

The checker evaluates every possible count using a rational squared-radical comparison, without numerical inverse trigonometry. Rejected counts retain their records and do not release this guarantee. Exact midpoint phase synthesis is still an ideal control input, not a demonstrated pulse.

## 4. Coverage is not a postselection confidence claim

The valid statement is

    P(accept AND fidelity below target) <= certified noncoverage bound.

It is not automatically the same bound for P(bad fidelity | accept). A generic conditional bound divides by acceptance probability; exact fixture noncoverage ratios are stored. Noncoverage itself is only an upper bound on fidelity failure, since a parameter outside the interval may still give adequate fidelity.

Repeatedly sampling until a count is accepted does not inherit the same fixed-sample confidence budget. It needs an explicit repeated-test or anytime allocation. Finite confidence does not become exact pointer knowledge.

## 5. Next deployment-assumption gate

Test angular drift and population-readout bias. Extend the interval/release rule using declared bounds and construct a passing-calibration/failing-deployment witness. Keep sampling confidence distinct from model drift, readout errors and phase-control precision.

Root outcome remains null. Shared sources, historical receipts, atlas and formal contracts are unchanged. This local gate does not admit physical calibration, preparation, spin, annihilation or photon output.

## Reproduce

```sh
python research/scattering/seed-composition/check_finite_calibration_gate.py
python research/scattering/seed-composition/check_finite_calibration_gate.py --check
python research/scattering/seed-composition/check_seed_composition_net.py
python research/scattering/low-energy/check_low_energy_net_v3.py
```

Predecessor calibration maps are freshly recomputed. Confidence certification, count inequalities and fixture tails use exact rational arithmetic. Hoeffding and angular propagation are explicitly scoped mathematical arguments, not new machine-formal or physical admission.
