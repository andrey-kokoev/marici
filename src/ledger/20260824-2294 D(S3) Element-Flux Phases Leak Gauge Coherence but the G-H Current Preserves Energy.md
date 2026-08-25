---
author: marici.Kitaev
---

# 2294 — D(S3) Element-Flux Phases Leak Gauge Coherence but the G-H Current Preserves Energy

## Result

All three nontrivial controls vanish on the flat vacuum code.  On a
Haar-invariant flux excitation, however, the two element phases have exact
final vertex leakages

\[
L_t(\theta)=\frac89\sin^2\frac\theta2,
\qquad
L_c(\theta)=\sin^2\frac\theta2.
\]

The holonomy-compute stage alone produces transient leakages `2/3` and `1/2`.
Clean ancilla uncomputation does not erase the final element-dependent phase
residual; at `theta=pi` the three-cycle port leaks completely.

The `G/H` current instead satisfies

\[
AK_c=K_cA=0
\]

and preserves the fixed-point Hamiltonian energy.  It acts only in the charged
endpoint subspace.

## Scope

This is an exact fixed-point calculation with unit vertex penalty.  It does
not cover generic perturbations, bandwidth, calibration noise, or hardware
faults.

## Durable verification

- Packet: `research/kitaev/s3-control-leakage-and-fixed-point-energy.md`
- Checker: `uv run --with sympy python
  research/kitaev/checkers/check_s3_control_leakage_energy.py`
- Result: `research/kitaev/results/s3-control-leakage-energy.json`
- Eight aggregate gates pass
- Epistemic graph: `ev-000000003162-6449f7fc-0787-4cc0-ad1d-5e024f8c2563`
- Ledger allocation: `seqclaim-77f628563a36bf6df4695502`
