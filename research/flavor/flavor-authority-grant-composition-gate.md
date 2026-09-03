# Authority-grant composition gate: WP1285

## Question

Can partial authority grants compose into full packet authority without a
typed composition certificate?

## DPC resolution

- **Problem:** test whether partial grants with matching labels can be
  combined directly into packet authority.
- **Bold conjecture:** every admissible typed UV packet must compose
  authority only through admitted grants with matching endpoints, kind,
  variance, evidence domains, transformations, coherence witnesses, and a
  triple associativity certificate.
- **Named rivals:** WP1128 v1 admission contract; WP1284 v10 admission
  contract; grant shadow packet; reported-number packet; fixture packet.
- **Risky consequences:** the Strominger analogue proves local validity does
  not guarantee a factorization-independent or kind-preserving composite;
  WP1284 still has no `authority_grant_composition` object; the handoff
  request demands typed authority-grant composition with coherence witnesses;
  v11 adds the grant object and rejects partial-grant shadows.
- **Strongest falsification attempt:** replay WP1128 and WP1284; compare the
  v10 and v11 admission contracts; test a grant shadow packet with all v10
  fields but no authority-composition object.
- **Exact residual:** the grant shadow packet is rejected and no actual
  packet is admitted. The authority-composition necessity conjecture
  survives. The residual is a source-derived typed grant atlas and coherence
  certificate.
- **Disposition:** authority-grant composition necessity survives attempted
  falsification; sequential-record lineage selected.

## Result

The authority-composition necessity conjecture **survived** the attempted
falsification. It remains unproven, and no actual typed packet has been
admitted.

Checker: `research/flavor/checkers/wp1285_authority_grant_composition_gate.py`

Result: `results/wp1285_authority_grant_composition_gate.json`

Contract: `research/flavor/contracts/flavor-event-production-packet-admission.v11.json`
