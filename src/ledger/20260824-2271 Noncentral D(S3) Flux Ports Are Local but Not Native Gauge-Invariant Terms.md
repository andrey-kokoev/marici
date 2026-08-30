---
author: marici.Kitaev
---

# 2271 — Noncentral D(S3) Flux Ports Are Local but Not Native Gauge-Invariant Terms

## Result

On one frozen oriented square, the based plaquette-flux effects

\[
B^g|g_0,g_1,g_2,g_3\rangle
=\delta_{g,g_0g_1g_2^{-1}g_3^{-1}}|g_0,g_1,g_2,g_3\rangle
\]

are four-edge Hermitian projectors.  Hence their exponentials are exact local
diagonal pulses whenever a based, element-resolved holonomy coupling is
admitted.

They are not terms of the native commuting-projector Hamiltonian.  With

\[
A=\frac1{6}\sum_{x\in S_3}U_x,
\]

exact enumeration gives

\[
\|[A,B^t]\|_F^2=48,
\qquad
\|[A,B^c]\|_F^2=36
\]

for the frozen transposition and three-cycle representatives.  Every
conjugacy-class sum commutes with `A`, but class averaging loses the element
resolution required by the 36-dimensional endpoint-algebra theorem.

Thus the two minimal flux ports are local and Hermitian, but their physical
availability is a genuine apparatus enlargement.  They can leave the larger
vertex-invariant excitation space, while acting exactly trivially on the flat
vacuum code because `B^t B^e=B^c B^e=0`.  A useful control protocol must first
type the endpoint excitation on which these ports act.

## Scope

This is a finite, source-typed result on one square plaquette and its base
vertex.  It does not establish a ribbon compilation, a perturbative gadget,
fault-tolerant execution, a leakage bound in time, or hardware access to the
four-edge diagonal coupling.  It does not promote endpoint-algebra span into
physical control.

## Durable verification

- Packet: `research/kitaev/s3-local-hamiltonian-source-model.md`
- Checker: `python research/kitaev/checkers/check_s3_local_source_model.py`
- Result: `research/kitaev/results/s3-local-source-model.json`
- Exact coverage: 1,296 basis states, 46,656 conjugation cases, eight
  aggregate gates
- Regression: `uv run --with sympy python
  research/kitaev/checkers/check_s3_minimal_flux_resolved_generators.py`
  still returns the conditional endpoint closure dimension 36
- Epistemic graph: `ev-000000003140-0cfdb6e2-1b23-4511-8caa-991fbbd9bacf`
- Graph correction separating excitation-space noncommutation from flat-code
  leakage: `ev-000000003143-cc7453be-5cec-49d8-884f-de80fe514b89`
- Ledger allocation: sequence claim `seqclaim-9b3318c9915392b1adfe9044`
