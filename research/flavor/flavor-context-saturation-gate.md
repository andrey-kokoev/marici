# Context-saturation gate: WP1282

## Question

Can probe-domain equivalence substitute for context-saturated packet testing?

## DPC resolution

- **Problem:** test whether a packet can be admitted after matching only the
  injected probe domain.
- **Bold conjecture:** every admissible typed UV packet must be tested under
  the admitted context monoid, including feedback, coherent control, and
  internal route slots, before endpoint or probe equivalence can be treated as
  compositional.
- **Named rivals:** WP1128 v1 admission contract; WP1281 v7 admission
  contract; probe-domain shadow packet; common-mode packet; fixture packet.
- **Risky consequences:** the Aspect analogue separates devices identical on
  an injected probe by feedback and internal route slots; WP1281 still has no
  `context_saturation` object; the handoff request demands context-saturation
  tests; v8 adds the saturation object and rejects probe-domain shadows.
- **Strongest falsification attempt:** replay WP1128 and WP1281; compare the
  v7 and v8 admission contracts; test a probe-domain shadow packet with all
  v7 fields but no context saturation.
- **Exact residual:** the probe-domain shadow packet is rejected and no actual
  packet is admitted. The context-saturation necessity conjecture survives.
  The residual is a source-derived admitted context monoid and saturation
  certificate.
- **Disposition:** context-saturation necessity survives attempted
  falsification; gain nuisance-state observability selected.

## Result

The context-saturation necessity conjecture **survived** the attempted
falsification. It remains unproven, and no actual typed packet has been
admitted.

Checker: `research/flavor/checkers/wp1282_context_saturation_gate.py`

Result: `results/wp1282_context_saturation_gate.json`

Contract: `research/flavor/contracts/flavor-event-production-packet-admission.v8.json`
