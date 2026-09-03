# Sequential-record fidelity gate: WP1279

## Question

Can marginal records and unconstrained continuation substitute for
branch-conditioned sequential fidelity?

## DPC resolution

- **Problem:** test whether a packet can satisfy all previous interfaces while
  retaining only marginal records and unconstrained later continuation.
- **Bold conjecture:** every admissible typed UV packet must preserve joint
  record words under branch-conditioned continuation, bind each later record
  to the earlier instrument branch, and forbid cross-branch substitution.
- **Named rivals:** WP1128 v1 admission contract; WP1278 v4 admission
  contract; marginal-record shadow packet; effect-only packet; fused shadow
  packet; fixture packet.
- **Risky consequences:** the Sontag hostile separates effect-equivalent
  instruments by one-step continuation and joint records; WP1278 still has
  no `sequential_record_fidelity` object; the handoff request demands a
  sequential-record continuation law and joint record words; v5 adds
  sequential fidelity and rejects marginal/cross-branch shadows.
- **Strongest falsification attempt:** replay WP1128 and WP1278; compare the
  v4 and v5 admission contracts; test a marginal-record shadow packet with
  all v4 fields but no sequential fidelity object.
- **Exact residual:** the marginal-record shadow packet is rejected and no
  actual packet is admitted. The sequential-fidelity necessity conjecture
  survives. The residual is a source-derived branch-conditioned continuation
  certificate.
- **Disposition:** sequential-record fidelity necessity survives attempted
  falsification; constructor-intertwiner certificate selected.

## Result

The sequential-fidelity necessity conjecture **survived** the attempted
falsification. It remains unproven, and no actual typed packet has been
admitted.

Checker: `research/flavor/checkers/wp1279_sequential_record_fidelity_gate.py`

Result: `results/wp1279_sequential_record_fidelity_gate.json`

Contract: `research/flavor/contracts/flavor-event-production-packet-admission.v5.json`
