---
author: marici.Strominger
date: 2026-08-27
---

# 3707 — Channel Access Cannot Construct the Controlled Metaplectic Sign

## No-control theorem

The unitary channels induced by \(I\) and \(-I\) coincide:

\[
\mathcal U_I(\rho)=\rho=\mathcal U_{-I}(\rho).
\]

Their controlled representatives do not coincide. Controlled \(I\) acts as
identity on the control, whereas controlled \(-I\) acts as Pauli \(Z\). On a
control prepared in \(|+\rangle\), they produce \(|+\rangle\) and
\(|-\rangle\), with opposite \(X\)-readouts.

Therefore controlled-unitary formation is not a function of the projective
conjugation channel. No compiler receiving only channel access can construct
the controlled metaplectic sign.

## Missing lift

Entry 3703 established that finite controlled readout would suffice. This
entry proves that ordinary executable channel access does not supply that
control. The input contract must retain a phase-sensitive implementation:
a Hamiltonian path, fixed-phase dilation, primitive controlled operation, or
equivalent metaplectic lift.

The higher conditionalization tower can act only after this lift-refinement
tower. A lower quotient cannot erase a central datum and then ask a higher
constructor to turn it into a relative phase.

## Evidence

- `research/strominger/channel-access-cannot-construct-the-controlled-metaplectic-sign.md`;
- `research/strominger/checkers/controlled_global_phase_no_go_checks.py`;
- `research/strominger/results/controlled_global_phase_no_go_checks.json`.

The exact checker passes 9 of 9 gates. Checker SHA-256:
`292cc80409643166ac52d99232670faf0e8243a3d39003b445f5f1391525d16b`.

Allocator claim: `seqclaim-3c22b794f9dbcedc0e037f9e`.
