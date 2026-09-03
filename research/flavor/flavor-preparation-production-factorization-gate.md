# Preparation-production factorization gate: WP1278

## Question

Can one fused record-labelled update substitute for independent preparation
and production factors?

## DPC resolution

- **Problem:** test whether a single record-labelled update already supplies
  the factorized packet interface.
- **Bold conjecture:** every admissible typed UV packet must carry one joint
  hidden-state update factored into independent preparation and production
  maps with separate messenger and response lineage.
- **Named rivals:** WP1128 v1 admission contract; WP1277 v3 admission
  contract; fused shadow packet; effect-only packet; quotient shadow packet;
  fixture packet.
- **Risky consequences:** the Sontag hostile makes record-conditioned updates
  sequential and joint-record typed; WP1277 still has no
  `preparation_production_factorization` object; the strengthened handoff
  request explicitly demands factorized preparation and production maps with
  separate lineage; v4 adds the factorization object and rejects fused
  updates.
- **Strongest falsification attempt:** replay WP1128 and WP1277; compare the
  v3 and v4 admission contracts; test a fused shadow packet with all v3
  fields but no factorization object.
- **Exact residual:** the fused shadow packet is rejected and no actual
  packet is admitted. The factorization necessity conjecture survives. The
  residual is a source-derived joint update with independent preparation and
  production factors.
- **Disposition:** preparation-production factorization necessity survives
  attempted falsification; sequential-record fidelity selected.

## Result

The factorization necessity conjecture **survived** the attempted
falsification. It remains unproven, and no actual typed packet has been
admitted.

Checker: `research/flavor/checkers/wp1278_preparation_production_factorization_gate.py`

Result: `results/wp1278_preparation_production_factorization_gate.json`

Contract: `research/flavor/contracts/flavor-event-production-packet-admission.v4.json`
