# First-release calibration needs confidence spending and can still abstain

**Fourth batch, iteration 17 of 20.**

**Strength:** finite stopping-policy confidence certificate, exact count partitions and a naive-retry counterexample. Not measured calibration windows or guaranteed physical release.

[Previous deployment bounds](CALIBRATION-DEPLOYMENT-BOUNDS.md) · [Checker](check_repeated_calibration_budget.py) · [Receipt](results/repeated-calibration-budget.v1.json)

## 1. Fresh finite schedule

Allow at most twenty calibration windows, stopping at the first bias/drift-aware release. Otherwise retain a censored no-release record. Before window data, choose

    N_t=512+128(t-1), epsilon=1/10,
    delta_t=(1/1000)/[t(t+1)].

Each window's concentration tail is rationally certified by positive Taylor terms and is below its allocated delta_t. Every count is checked against the preceding exact deployment gate; accepted and rejected counts are stored as complete interval runs.

Ordered raw probe words, counts and decisions are required records, including rejected windows. No physical observation is supplied. Maximum probe cost is 34,560, with preparation/reset/control resources still inputs.

## 2. Stopping does not defeat the declared budget

A bad first release, under the declared bias/drift/phase assumptions, is contained in the union of window noncoverage events. Hence

    P(bad release)<=sum delta_t
      =(1/1000)(20/21)<1/1000.

The certified tail sum is smaller still. Between-window independence is unnecessary for this union bound; each window needs conditional iid concentration for its observed population, with its schedule fixed before its data. Bias/drift/control-bound violations are not covered by this statistical budget.

This remains an unconditional bound. Conditioning on eventual release does not automatically retain the same confidence level.

## 3. Why indefinite fixed-window reuse fails

Repeat the original robust 512-probe window independently at constant p=q=1/100, with no bias/drift violation. Every accepted interval misses p, but its acceptance probability a is strictly positive. The receipt stores a exactly and all first-release/censoring probability formulas.

At first release, interval noncoverage is certain. For the finite horizon H=ceil(1/a),

    P(noncovering release)=1-(1-a)^H>1/2.

The bound follows from aH>=1 and exp(1)>2. This illustrates invalid confidence reuse, not a claim that noncoverage always equals actual fidelity failure. The proper budgeted policy avoids this accumulated risk; waiting arbitrarily long under the old fixed-window guarantee does not.

## 4. Safe spending is not guaranteed release

The budgeted policy also abstains on every covered window at p=1/100. Its fixed radius cannot resolve that endpoint-near population enough for the robust angular target. Larger N reduces the probability of noncoverage but does not shrink the interval used by this policy.

No-release is a retained valid outcome, not a reason to discard records or declare successful physical preparation. This conservative protocol is safe under its assumptions but not a universally terminating calibration procedure.

## 5. Next precision-resource gate

Construct a confidence-spent schedule with a shrinking population radius. Test release for covered endpoint-near populations within a finite probe budget, retaining the bias/drift margins, raw records and all abstentions. Separate finite statistical termination guarantees from physical control implementation.

Root outcome remains null. Shared sources, historical receipts, atlas and formal contracts are unchanged. No physical calibration, preparation, spin, annihilation or photon output is admitted.

## Reproduce

```sh
python research/scattering/seed-composition/check_repeated_calibration_budget.py
python research/scattering/seed-composition/check_repeated_calibration_budget.py --check
python research/scattering/seed-composition/check_seed_composition_net.py
python research/scattering/low-energy/check_low_energy_net_v3.py
```

Predecessor deployment tests are freshly recomputed. Exact spending, count partitions and binomial/geometric identities verify the receipt. Conditional concentration and union-bound arguments are explicitly scoped mathematics, not new formal or physical admission.
