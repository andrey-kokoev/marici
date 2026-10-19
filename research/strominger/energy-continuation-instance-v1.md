# Iteration13: positive energy task instance with retained source and probe update

## Fresh task and source reuse

The45-node net recommended `energy-example-interface-comparison`. The new executable instance reuses the preceding continuation System/check_map interface and the actual energy audit's coefficient field, projectors, drift matrix and shared-leg functions. It calls the existing `read_energy_task`, `gain_step`, `infer_components`, `target_gain` and `finish_after_probe` implementations unchanged.

## Declared task map

A retained source state contains the full coefficient field, original source field, predecessor, command and task-update witness. Its projection is(a,b), read from the one-leg/two-leg energy sectors. The allowed commands are the declared fixed drift and common family gain0<=q<=1; the observation is H=a+b.

    gain_q(a,b) = (q^2 a, q^4 b)
    drift(a,b) = (a,b).

The full gain field is (P_mean+q P_one+q^2 P_two)F. Exact matrix checks establish the projector partition, idempotence, orthogonality, source commutation and absence of mean energy. Writing E1=(A P_one)^T(A P_one) and E2=(A P_two)^T(A P_two), additional checks give

    E1+E2=A^T A,
    U^T E1 U=E1,
    U^T E2 U=E2.

These equalities supply a domain-wide algebraic justification of observation decomposition and drift invariance for real coefficient fields, beyond the tested initial trajectory. Gain composition is also checked symbolically as a polynomial identity. The concrete source trajectory, its quotient, endpoint observations and retained witnesses satisfy the previous executable continuation interface.

Thus(a,b) is sufficient for finite words of THESE gains and drift under the declared energy observer. This is not a quotient for arbitrary future sensors or actuators, and it is not a physical calibration theorem.

## Composition and reconstruction boundaries

Two successive gains2/3 and3/5 produce the same full field and task pair as a single gain2/5. Their retained histories remain different. No equality of the complete history-bearing packages is asserted.

The quotient is not a reconstruction of the source. Negating every left arrow/state leg in the ACTUAL shared-leg preparation produces-F. Its two quadratic statistics agree with F although the full source fields differ. The allowed linear commands preserve this sign distinction and the equal task observations. No artificial scalar-only counterexample substitutes for the source model.

## Probe/update semantics

The checker applies q=1/2 to the actual source field and records H before and H1 after. `infer_components(H,H1,q)` reconstructs the PRE-probe(a,b), not the source field or an undone probe.

It then chooses a target h=H1/2 and calls `finish_after_probe`. The returned final gain is applied to the retained POST-probe field. The resulting source energy equals h exactly and its parent remains the probed state. Computing the targeting gain from the old state and applying it after the probe instead misses h; this hostile is detected.

Amplifying/negative gains, an undeclared command and uninformative identification probes0/1 are rejected. No reset, new actuator or full mode controllability has been added.

## Verification and net disposition

Executed:

    uv run --with sympy python research/strominger/checkers/check_energy_continuation_instance.py

Fourteen checks and five command/probe rejections pass. The actual prerequisite source audits and continuation checks rerun. Receipt: `research/strominger/results/energy-continuation-instance-v1.json`.

This is exact executable/symbolic verification, not a new Agda instantiation of the generic task-map theorem. Source selection and calibration remain supplied assumptions. No owner source implementation was changed.

`energy-example-interface-comparison` is constructed at this drift/gain task scope. The next root task is `wg-reusable-identity-assembly`: audit that the schedule, relation and energy witnesses use compatible meanings of retained identity, observation and declared continuation. The examples have different sources and observers; their common interface must not be misreported as a common physical state space or a universal137 realization. Structural graph readiness alone does not establish the assembly.
