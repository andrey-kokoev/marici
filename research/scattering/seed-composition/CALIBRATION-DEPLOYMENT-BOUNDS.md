# Sampling confidence does not cover readout bias or deployment drift

**Fourth batch, iteration 16 of 20.**

**Strength:** exact bias/drift-aware release inequalities and passing-calibration counterexamples. Not measured deployment bounds or a physical acceptance admission.

[Previous finite calibration](FINITE-CALIBRATION-GATE.md) · [Checker](check_calibration_deployment_bounds.py) · [Receipt](results/calibration-deployment-bounds.v1.json)

## 1. Fresh declared model bounds

Distinguish true calibration population p from observed iid population q. Declare

    |q-p|<=1/100,
    |beta_deploy-beta_calibration|<=rho,
    cos(rho)=2499/2501, sin(rho)=100/2501.

These bounds are inputs, not measured facts. Sampling concentration applies to q. Widening the old interval by the bias bound gives

    p in [max(0,k/n-epsilon-bias), min(1,k/n+epsilon+bias)].

Exact binomial fixtures verify that this widening retains the previous certified sampling noncoverage budget. It does not absorb violations of the bias bound, time variation within the probe window, control phase errors or an unavailable drift bound.

## 2. Deployment-aware release

Use the angular midpoint of the expanded calibration interval. If its half-width is h, the conservative deployment error is at most h+rho. Release the ratio-independent 99% Bell fidelity guarantee only if

    cos(h+rho)>=49/50.

Equivalently, require cos(h)>=cos(acos(49/50)-rho). That threshold is rational plus a rational multiple of sqrt(11). The checker transforms it to an endpoint-visibility inequality and compares square roots exactly using signs in Q(sqrt(11)).

Every accepted count also passes the old gate, but fewer counts are accepted. Count 256 still passes. Rejected counts and all widened intervals remain recorded. The guarantee requires both sampling coverage and the declared deployment/readout/control assumptions.

## 3. Small-bias counterexample to the old gate

For n=512 take k=26. The old observed-population interval has lower endpoint zero and upper endpoint

    q=26/512+1/10.

Let true p=q+1/100, with no additional deployment drift. The observed q is **inside** the old interval, and the old gate accepts. Its angular estimate is half the angle corresponding to q. The new gate rejects this count.

Exact doubled-angle comparisons show actual visibility below 48/49. The source-bound witnessed minus inverse filter has 1-r²>49/50. Hence actual Bell infidelity is strictly greater than 1/100. This failure occurs on the old sampling-coverage event: its cause is biased population readout, not a concentration-tail event.

The example respects the new population-bias bound and illustrates why expanding the interval is necessary. It is a declared model fixture, not measured apparatus noise.

## 4. Deployment-only drift counterexample

Count 256 with calibration population 1/2 passes the old gate and estimates angle pi/4. Change the deployed population to one, whose angle is pi/2. Visibility becomes 1/sqrt(2).

For the same witnessed minus filter, exact algebra gives fidelity below 351/400, far below 99/100. This large drift is outside the new rho bound, so it does not refute the strengthened conditional guarantee. It shows why arbitrarily confident calibration does not protect against unbounded deployment change.

## 5. Confidence and model risks remain separate

Unconditional probability of release with bad fidelity is bounded by the sampling tail only while the bias, drift and control assumptions hold. Conditioning on release still needs the previous selection-risk accounting. No amount of raw iid sampling establishes those additional bounds by itself.

Next construct a finite repeated-calibration confidence-spending schedule. Stopping at the first release must not reuse a single-window failure budget; rejected windows, probe records and deployment assumptions remain part of the protocol.

Root outcome remains null. Shared sources, historical receipts, atlas and formal contracts are unchanged. No physical calibration, preparation, spin, annihilation or photon output is admitted.

## Reproduce

```sh
python research/scattering/seed-composition/check_calibration_deployment_bounds.py
python research/scattering/seed-composition/check_calibration_deployment_bounds.py --check
python research/scattering/seed-composition/check_seed_composition_net.py
python research/scattering/low-energy/check_low_energy_net_v3.py
```

Predecessor confidence tests are freshly recomputed. Exact interval comparisons, biased binomial fixtures and source-ratio counterexample bounds verify the local receipt. Drift propagation is explicitly scoped mathematics, not new formal or physical admission.
