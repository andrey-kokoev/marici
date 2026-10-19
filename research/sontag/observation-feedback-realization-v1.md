# Observation and feedback realization: exact energy task v1

## Scoped construction

The existing energy gain/probe controller admits an executable closed-loop event trace whose decisions use only the declared available observations. This is a mathematical-model realization, not physical measurement, actuation, timing, or reservoir accounting. It does not resolve arbitrary WG feedback or the physical-binding node.

Sources: `research/strominger/checkers/energy_task_reduction.py`, `research/strominger/checkers/energy_target_controller.py`, and `research/strominger/energy-target-controller.md`. No source-owner implementation was changed.

## Information and event sequence

The retained underlying state is nonnegative `(a,b)` with provenance; exact total observation is H=a+b. The controller initially knows H and requested target h, not the components. Its information state is the compatible family `{(a,b)≥0:a+b=H}`. A model reading alone has no additional transition; physical detector back-action is unspecified.

The implemented trace is:

1. Record exact H and target h, validating `0≤h≤H`.
2. If h=H, choose q=1; if h=0, choose q=0. These decisions need no component inference, including H=h=0.
3. For `0<h<H`, choose `qprobe²=(1+h/H)/2` using only H,h.
4. Execute `gain_step`; state becomes `(qprobe²a,qprobe⁴b)`. Record q and parent/result provenance. The probe is NOT a passive reading.
5. Record the second exact total Hafter.
6. Use `infer_components(H,Hafter,qprobe)` to reconstruct the pre-probe components; apply the recorded gain to reconstruct the CURRENT state.
7. Choose `target_gain(current,h)` and execute it on the actual probed state, not the initial state.
8. Record final exact total and check Hfinal=h.

All observations and controls occur in their declared construction order. No physical clock is supplied. External disturbances and noisy results are not part of this deterministic exact instance; adding either requires a successor observation/transition model, not silently replaying this trace.

## Why the policy is lawful

For Q=qprobe² and r=h/H, Q=(1+r)/2. Nonnegative components give `Q²H≤Hafter≤QH`. Since `Q²−r=(1−r)²/4≥0`, Hafter cannot fall below h. The existing exact targeting law therefore applies from the updated state. Component-zero cases and boundary targets are handled by the source controller.

The two-reading determinant is qprobe⁴−qprobe², nonzero for the interior-target branch. Thus the exact observation transcript identifies the components without granting access to hidden initial state. Equal initial totals produce identical first controls, but unequal after-readings can lawfully produce different feedback controls. The checker explicitly tests this distinction on `(8,0)` and `(0,8)` with target 4.

## Control and observation claims

- **Reachability:** every exact target h in `[0,H]` is reachable by at most two admitted gains in this model. Targets above H or negative are rejected; this is not unrestricted state controllability.
- **Identification:** two exact readings with a recorded nontrivial gain identify `(a,b)` for this vocabulary. This is active, task-relative identification, not passive observability of a physical plant.
- **Policy transport:** equal available transcripts and target yield equal decisions; source replay retains the actual state-changing probe.
- **Resources:** model energy is nonincreasing; provenance/source history remains retained. No free reset, amplification, sink, or memory erasure is introduced.
- **Robustness:** the identification determinant tends to zero as h/H tends to one. No uniform measurement-noise margin is established.
- **Continuous interpretation:** q=0 is an admitted discrete model endpoint; it is not asserted reachable in finite physical time under continuous-rate contraction.

## Verification and disposition

`uv run --with sympy python research/sontag/checkers/observation_feedback_realization_v1.py`

54 exact checks passed across 20 traces, covering both single-component cases, zero state, interior and endpoint targets, updated-state targeting, public-information decisions, adaptive feedback, invalid targets and rejection of recovery after a blind undershooting probe.

Result: `research/sontag/results/observation-feedback-realization-v1.json`.

This supplies a bounded witness for the energy branch of `observation-feedback-realization`. It does not justify the full mathematical-control assembly: the WG continuation-equivalence/transport and presentation-naturality gates remain open. The Nima-owned work contract and source pins are unchanged pending owner review.
