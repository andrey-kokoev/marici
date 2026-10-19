# Shrinking-radius spending gives finite model release, at an explicit probe cost

**Fourth batch, iteration 18 of 20.**

**Strength:** exact confidence-spent precision schedule and universal angular-width certificate. Not observed probes, exact parameter knowledge or physical preparation.

[Previous repeated-budget test](REPEATED-CALIBRATION-BUDGET.md) · [Checker](check_calibration_precision_refinement.py) · [Receipt](results/calibration-precision-refinement.v1.json)

## 1. Fresh predetermined refinement

Keep the declared population-bias and deployment-drift bounds. Before data in window t, choose

    epsilon_t=1/(t+9),
    delta_t=(1/1000)/[t(t+1)],
    m_t=min integer with 2/2^m_t<=delta_t,
    N_t=ceil(m_t/(2 epsilon_t²)).

Since exp(1)>2, Hoeffding's tail is strictly below 2/2^m_t. All choices and confidence spending precede the window's observations. The checker evaluates every count against the same bias/drift-aware fidelity inequality, storing complete acceptance/rejection runs.

First-release stopping retains all raw-word obligations, rejected windows and decisions. The planned horizon is twenty windows; no physical data are supplied.

## 2. Universal release by window seventeen

A bias-expanded population interval has width at most 2(epsilon+bias). Its maximum angular width occurs at an endpoint and is

    asin(sqrt(2(epsilon+bias))).

The checker compares that worst-case endpoint visibility exactly with the drift-aware threshold. At window seventeen the comparison passes. Every possible count then releases, including counts near the population endpoints. This certificate covers the continuous interval geometry, not just the tested integer grid.

Under complete valid windows and the ideal specified controls, first release therefore occurs no later than window seventeen. Its window uses 6,760 probes and radius 1/26. Worst-case cumulative probe cost before release is **54,398**. A full twenty-window plan would cost 77,938 probes, but its later windows are unnecessary under this certificate.

## 3. Statistical release risk remains explicit

Summing certified sampling tails through window seventeen gives

    P(bad first release)<=53/65536<1/1000,

while the target Bell undo fidelity is 99/100. This uses the same conditional iid and model-bound assumptions as the preceding gate. It does not count bias/drift violations, phase/control errors or inaccessible outcome copies as sampling failures.

Unlike the fixed-radius policy, this ideal count-decision model has release probability one within the finite cap. Thus its conditional-on-release risk equals the unconditional risk **within that model**. Physical aborts, missing windows or extra acceptance filters can change that conclusion and must retain explicit abort records.

No release event becomes exact pointer knowledge. The guarantee remains a probability statement about fidelity under its assumptions.

## 4. Inputs and records are not discharged

The protocol still requires conditionally iid probe populations, the real nonnegative pointer family, ideal Y readout, exact midpoint phase control, preparation/reset resources and access to all distinguishing outcome copies. All ordered probe words and decisions are required records; count compression in the checker does not authorize deleting them.

These are mathematical apparatus/control inputs, not features derived from the native fixed Hamiltonian or evidence of a physical implementation.

## 5. Next irreducible-model-error gate

Let the probe radius tend to zero and quantify the remaining bias/drift floor. Construct distinct nuisance models with identical observed calibration populations. Test whether more iid Z probes alone can certify a stricter fidelity target, or whether detector, source and deployment bounds must be tightened.

Root outcome remains null. Shared sources, historical receipts, atlas and formal contracts are unchanged. No physical calibration, preparation, spin, annihilation or photon output is admitted.

## Reproduce

```sh
python research/scattering/seed-composition/check_calibration_precision_refinement.py
python research/scattering/seed-composition/check_calibration_precision_refinement.py --check
python research/scattering/seed-composition/check_seed_composition_net.py
python research/scattering/low-energy/check_low_energy_net_v3.py
```

Predecessor spending maps are freshly recomputed. Exact count comparisons and universal width inequalities verify the local receipt; concentration, angular geometry and stopping arguments remain explicitly scoped mathematics, not new formal or physical admission.
