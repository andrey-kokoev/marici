# Gain nuisance-state observability gate: WP1283

## Question

Can a fitted scalar gain or stale calibration substitute for gain
nuisance-state observability?

## DPC resolution

- **Problem:** test whether the packet can treat detector/source gain as a
  fitted scalar rather than an observed nuisance state.
- **Bold conjecture:** every admissible typed UV packet must carry
  detector/source gain as a nuisance state with calibration excitation, epoch
  and setting lineage, a drift model or robust-set certificate, and a join
  from estimator to corrected record.
- **Named rivals:** WP1128 v1 admission contract; WP1282 v8 admission
  contract; fitted-gain shadow packet; stale-calibration packet; probe-domain
  packet; fixture packet.
- **Risky consequences:** the Sontag analogue shows observation of physical
  state and gain is structurally non-injective without excitation; calibration
  at another time is not automatically a state estimate; WP1282 still has no
  `gain_nuisance_observability` object; v9 adds the gain object and rejects
  scalar/stale shadows.
- **Strongest falsification attempt:** replay WP1128 and WP1282; compare the
  v8 and v9 admission contracts; test a fitted-gain shadow packet with all v8
  fields but no nuisance-state observability object.
- **Exact residual:** the fitted-gain shadow packet is rejected and no actual
  packet is admitted. The gain-observability necessity conjecture survives.
  The residual is a source-derived gain observation channel with lineage and
  drift or robust certificate.
- **Disposition:** gain nuisance-state observability survives attempted
  falsification; normalization-port rank selected.

## Result

The gain-observability necessity conjecture **survived** the attempted
falsification. It remains unproven, and no actual typed packet has been
admitted.

Checker: `research/flavor/checkers/wp1283_gain_nuisance_observability_gate.py`

Result: `results/wp1283_gain_nuisance_observability_gate.json`

Contract: `research/flavor/contracts/flavor-event-production-packet-admission.v9.json`
