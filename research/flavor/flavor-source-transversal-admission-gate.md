# Source-transversal admission gate: WP1277

## Question

Can quotient or predictive recovery certify a source-transversal packet
without a source lift certificate?

## DPC resolution

- **Problem:** test whether predictive descent already supplies the physical
  recovery authority needed by a typed UV packet.
- **Bold conjecture:** every admissible typed UV packet must carry a
  source-derived transversal certificate proving physical recovery on source
  representatives and predictive quotient descent, not merely
  equivalence-class recovery.
- **Named rivals:** WP1128 v1 admission contract; WP1276 v2 admission
  contract; quotient shadow packet; effect-only packet; partial-interface
  composition; fixture packet.
- **Risky consequences:** Sontag recovery distinguishes physical realization
  from predictive quotient recovery; WP1276 still has no `source_transversal`
  object; WP1275 constructs no source-selected `U`; v3 requires an explicit
  `U` map and source lift certificate.
- **Strongest falsification attempt:** replay WP1128 and WP1276; compare the
  v2 and v3 admission contracts; test a quotient shadow packet with all
  event/update fields but no source transversal.
- **Exact residual:** the quotient shadow packet is rejected and no actual
  packet is admitted. The source-transversal necessity conjecture survives.
  The residual is a source-derived transversal certificate from `U`.
- **Disposition:** source-transversal necessity survives attempted
  falsification; preparation-production factorization selected.

## Result

The source-transversal necessity conjecture **survived** the attempted
falsification. It remains unproven, and no actual typed packet has been
admitted.

Checker: `research/flavor/checkers/wp1277_source_transversal_admission_gate.py`

Result: `results/wp1277_source_transversal_admission_gate.json`

Contract: `research/flavor/contracts/flavor-event-production-packet-admission.v3.json`
