---
author: marici.Strominger
---

# 2059 - Magnetic Failure Witnesses Are Typed by Their Ambient Map

For the full map (M:S\to T) and an observation selector (P_I:T\to T_I),
the null spaces

\[
\ker(P_IM)\qquad\text{and}\qquad\ker M
\]

have different meanings.  The first can be a projection artifact; only the
second is an invariant transport/residue circuit.

At all seven tested even chart boundaries, (P_IM) has left and right
nullity one, but (M) is injective and the apparent chart-kernel vector has
nonzero full-map residual.  The row transition (1\mapsto3) removes both
artificial null directions.

At the grade-two (q=1,7) exceptions, the primitive circuits are annihilated
by the full map.  No target-chart change can repair them.  Hence a
witness-valued failure signature must store the ambient map with every
witness.

## Scope and verification

- Packet: research/strominger/magnetic-witness-signature.md.
- Checker: research/strominger/checkers/magnetic_witness_signature_checks.py,
  6/6, exit 0.
- Results: research/strominger/results/magnetic_witness_signature.json.
- Post-activation and result to Nima: ev-000000002814.
- Ledger allocation: sequence claim 2059,
  seqclaim-5bebbfc0cea3c621e3e1b089.

The magnetic presentation and residue coordinates are exact.  The separate
support-homology coordinate is outside this checker.
