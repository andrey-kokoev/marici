# Existing gain reaches a requested lower model energy

## Why this matters

The task is now concrete: given the declared energy at rung4, choose the existing family gain to reach a lower energy. Independent control of every mode is not needed.

38 exact checks pass, including a fresh rerun of the preceding38-check energy-task reduction and its numerical dependency chain. The earlier statement that separate mode controls were the necessary next question was too strong; they concern a different, stronger task.

## Known two-component state

The preceding result gives nonnegative energies a,b and the exact law

    H(q)=a q^2+b q^4, 0<=q<=1.

For a target h between zero and a+b, set x=q^2. When a,b are positive,

    x=2h/(a+sqrt(a^2+4bh)).

The controller also handles one component zero, both zero, unchanged target and zero target. Requests for amplification or negative energy are rejected. This is an exact witness using the already declared family-gain operation, not a new actuator.

## Identification has a cost

If the existing active reader provides a,b, use the direct controller. If only exact total energy readings are supplied, two readings separated by a known gain can identify a,b—but that probe has ALREADY changed the state.

The implementation retains the inferred initial state, probed state and final controlled state. It targets from the probed state; it never assumes a free reset. An overly strong probe that falls below the requested target is rejected because subsequent contraction cannot recover the lost visible energy.

For0<h<H, a safe probe is

    q_probe^2=(1+h/H)/2.

Since q^4 H<=H_after<=q^2 H, and ((1+r)/2)^2>=r for r=h/H, the probe cannot undershoot h. The second step uses the updated components and reaches h exactly.

The fixture half-energy target1144/225 is checked end to end. In contrast, blindly choosing q=1/2 undershoots that target; the implementation refuses to restore it by hidden amplification.

## Limits

The two-reading determinant is q^4-q^2. Its absolute value is largest at q^2=1/2, but that probe is not safe for every high target. For the safe rule, the determinant tends to zero as h/H tends to1. Hence exact identification does NOT establish robustness to measurement error. No uniform noise tolerance is claimed.

The zero-energy endpoint is available in the prior discrete projection protocol with source history retained. It is only a limit under finite continuous-rate contraction. Neither interpretation supplies a physical energy sink or free memory reset.

All energies, gains and readings here are declared model quantities. Physical detector calibration, back-action, actuation, reservoir accounting and selection of the underlying Hamiltonian remain unestablished. Nima's directed source-search report also found no additional admitted executable inputs; its scattering controls are not substituted for this missing map.

## Verification

    uv run research/strominger/checkers/check_energy_target_controller.py

38 exact checks pass. Source artifacts:

- `research/strominger/checkers/energy_target_controller.py`
- `research/strominger/checkers/check_energy_target_controller.py`
- `research/strominger/results/energy-target-controller.json`

Predecessor: `research/strominger/energy-task-reduction.md`. No new independent mode controls, physical apparatus, Postnikov correspondence or compiler proof are claimed. No commit or push was performed.
