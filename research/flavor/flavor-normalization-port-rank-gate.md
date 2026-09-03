# Normalization-port rank gate: WP1284

## Question

Can a count of reported normalization numbers substitute for declared
physical ports and Jacobian rank?

## DPC resolution

- **Problem:** test whether finite normalization data can be admitted without
  a port/rank certificate.
- **Bold conjecture:** every admissible typed UV packet must declare physical
  normalization ports and prove a Jacobian rank certificate matching the
  finite scheme orbit, with independent records joined and one scheme point
  reused for subsequent observables.
- **Named rivals:** WP1128 v1 admission contract; WP1283 v9 admission
  contract; rank-shadow packet; reported-number packet; fitted-gain packet;
  fixture packet.
- **Risky consequences:** the Benincasa analogue proves counting reported
  numbers is not enough; WP1283 still has no `normalization_port_rank` object;
  the handoff request demands declared normalization ports and Jacobian rank;
  v10 adds the port-rank object and rejects number-count shadows.
- **Strongest falsification attempt:** replay WP1128 and WP1283; compare the
  v9 and v10 admission contracts; test a rank-shadow packet with all v9
  fields but no normalization-port rank object.
- **Exact residual:** the rank-shadow packet is rejected and no actual packet
  is admitted. The normalization-port-rank necessity conjecture survives. The
  residual is a source-derived port set and Jacobian rank certificate.
- **Disposition:** normalization-port-rank necessity survives attempted
  falsification; authority-grant composition selected.

## Result

The normalization-port-rank necessity conjecture **survived** the attempted
falsification. It remains unproven, and no actual typed packet has been
admitted.

Checker: `research/flavor/checkers/wp1284_normalization_port_rank_gate.py`

Result: `results/wp1284_normalization_port_rank_gate.json`

Contract: `research/flavor/contracts/flavor-event-production-packet-admission.v10.json`
