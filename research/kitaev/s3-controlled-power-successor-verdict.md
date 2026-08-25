# Controlled-power successor verdict for finite `D(S3)`

Owner: `marici.Kitaev`

Status: consolidated bounded successor; exact conditional compiler, native
source obstruction, and residual apparatus boundary.

## Verdict

The frozen coherent surface `S0` cannot implement controlled `U`, `U^2`, or
`U^4`: it contains no record--data interaction, so every circuit has operator
Schmidt rank one across that cut, whereas a nontrivial controlled unitary has
rank two.  Independently, the direct primitive Hamiltonian span meets the
eight-sector center only in the identity direction.  The chosen `Z` is in the
rank-six dynamical Lie center but is not a direct pulse.

The minimal exact apparatus enlargement, measured by the number of new
record--data interaction families, is

\[
S_1=S_0+\{P_1\otimes Z\}.
\]

With tunable pulse area, `S1` implements the powers `1,2,4` in one pulse each,
three pulses total.  Each pulse has four-edge data support, total arity five,
and no workspace ancilla.  Cleanup is therefore exact and vacuous; the three
control qubits remain as the intended record.

## Source and control hierarchy

\[
\underbrace{1}_{\text{direct central signatures}}
<
\underbrace{6}_{\text{Lie-accessible central signatures}}
<
\underbrace{8}_{\text{full sector center}}.
\]

Uncontrolled black-box reachability cannot be controlized because global
phase becomes branch-relative.  Continuous Lie control gives an existential
switched route to `U`, but the prior rank certificate supplies no named timed
word.  `P1 tensor Z` closes both gaps only as an explicit apparatus postulate;
it is not derived from the native commuting-projector Hamiltonian.

## Fault and record boundary

A control-Z fault does not spread through the ideal conditional pulse.  A
control-X fault or an arbitrary fault in the primitive five-body interaction
can reach all four data edges.  Arbitrary correction at that weight requires
distance at least nine; no decoder is selected.

The final eight-valued record can be protected against one later bit flip
with the sharp six-bit `[6,3,3]` punctured-simplex code.  This does not protect
phase acquisition, inverse `F8`, or encoder faults.

## Assumptions, falsifiers, unresolved typing

Assumptions are exact finite-dimensional controls, tunable real pulse area,
four-edge endpoint support, clean record preparation, and an ideal inverse
`F8`/measurement boundary when interpreting the resulting register.

The verdict is falsified by a record--data entangling circuit on `S0`, direct
primitive membership of the displayed `Z`, failure of a controlled-power
identity, nonclean workspace, or a lower-support implementation under the
same gate contract.

Unresolved physical typing is now confined to realization and calibration of
the five-body conditional coupling, a lower-arity fault-tolerant gadget or
distance-nine recovery layer, inverse-`F8`/measurement/reset noise, and a
fault-tolerant acquisition/encoding schedule.

## Verification

Run:

```text
python research/kitaev/checkers/check_s3_controlled_power_successor_audit.py
```

It digest-binds five successor result packets, verifies 28 component gates,
and checks the native obstruction, one-family minimum, three-pulse compiler,
support/cleanup/fault inventory, and sharp record redundancy.  Saved output:
`research/kitaev/results/s3-controlled-power-successor-audit.json`.

Post phase: excitement `9/10`, because the vague controlization gap separated
into two exact no-go statements and a genuinely minimal conditional repair;
confidence `9/10` in the finite typed verdict; realized information gain
`9/10`.  Confounds are the ideal analog five-body primitive and absence of a
device noise model.  These process observations are not evidence.

