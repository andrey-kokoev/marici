---
author: marici.Kitaev
sequence_claim: seqclaim-33212f11b9b370dea5194cb4
---

# 2524 — Lockstep Controller Redundancy Is a Repetition-Code Complex

## Exact complex

For (n) controller replicas,

\[
0\longrightarrow\mathbf F_2
\xrightarrow{E_n}\mathbf F_2^n
\xrightarrow{H_n}\mathbf F_2^{n-1}
\longrightarrow0,
\]

with (E_n(b)=b\mathbf1_n) and
((H_nx)_j=x_j+x_{j+1}), is exact:

\[
H_nE_n=0,qquad
\ker H_n=\operatorname{im}E_n=\operatorname{span}\{\mathbf1_n\}.
\]

It is the binary repetition code ([n,1,n]). Hence (n\ge s+1) detects
every error of weight at most (s), while (n\ge2t+1) corrects every error
of weight at most (t). Two-copy detection and three-copy correction are the
first cases.

## Common mode and fanout

The common-mode vector (mathbf1_n) has zero syndrome because it is the
logical (X) codeword, not a detectable defect. Under

\[
F:\mathbf F_2\to\mathbf F_2^4,qquad F(b)=b\mathbf1_4,
\]

that logical flip becomes simultaneous inversion of all four actuator
commands.

## Carrier and lens boundary

The complex, syndrome quotient, distance, and fanout incidence belong to
shared Carrier geometry. Mapping command inversion to encoded Pauli/CPTP
faults, recovery, exRec semantics, and (T)-equivalent cost requires the
quantum coefficient lens.

## Durable verification

- Packet: `research/kitaev/lockstep-controller-repetition-complex.md`.
- Checker:
  `uv run python research/kitaev/checkers/check_lockstep_controller_repetition_complex.py`.
- Result: `research/kitaev/results/lockstep-controller-repetition-complex.json`.
- Result SHA256:
  `A24ED5841DB757557C3DEAEC585140E1580D6D50785E0B403DBF26C66A9788D2`.
- Graph admission: `ev-000000003505-f2bad01e-6b4f-4688-ae2c-f6d3443f7a6b`.
- Ledger allocation: `seqclaim-33212f11b9b370dea5194cb4`.
