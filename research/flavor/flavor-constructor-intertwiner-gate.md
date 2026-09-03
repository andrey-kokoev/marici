# Constructor-intertwiner gate: WP1280

## Question

Can external universality or dimension equality substitute for a constructor
intertwiner?

## DPC resolution

- **Problem:** test whether imported theorem inventory and dimension equality
  already supply physical constructor transport.
- **Bold conjecture:** every admissible typed UV packet importing external
  universality, Hadamard, SIC, or Weyl results must carry a concrete
  constructor intertwiner with executable encoding/decoding, primitive
  intertwining, fault-model matching, leakage transport, and source transport
  authority.
- **Named rivals:** WP1128 v1 admission contract; WP1279 v5 admission
  contract; external shadow packet; dimension-equality packet;
  marginal-record packet; fixture packet.
- **Risky consequences:** the Kitaev analogue shows dimension equality is
  vacuous without constructor transport; WP1279 still has no
  `constructor_intertwiner` object; the handoff request demands a constructor
  intertwiner for imported universality; v6 adds the intertwiner object and
  rejects external shadows.
- **Strongest falsification attempt:** replay WP1128 and WP1279; compare the
  v5 and v6 admission contracts; test an external shadow packet with all v5
  fields but no constructor intertwiner.
- **Exact residual:** the external shadow packet is rejected and no actual
  packet is admitted. The constructor-intertwiner necessity conjecture
  survives. The residual is a concrete source-derived intertwiner for every
  imported theorem.
- **Disposition:** constructor-intertwiner necessity survives attempted
  falsification; independent-frame anchor selected.

## Result

The constructor-intertwiner necessity conjecture **survived** the attempted
falsification. It remains unproven, and no actual typed packet has been
admitted.

Checker: `research/flavor/checkers/wp1280_constructor_intertwiner_gate.py`

Result: `results/wp1280_constructor_intertwiner_gate.json`

Contract: `research/flavor/contracts/flavor-event-production-packet-admission.v6.json`
