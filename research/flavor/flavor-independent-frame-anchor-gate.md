# Independent-frame anchor gate: WP1281

## Question

Can internal self-calibration substitute for an independent frame anchor
against common-mode drift?

## DPC resolution

- **Problem:** test whether packet-frame self-calibration already exposes
  common-mode drift.
- **Bold conjecture:** every admissible typed UV packet must carry an
  independently sourced frame anchor in a separate fault domain, with a
  disagreement alarm and explicit drift syndrome making common-mode drift
  visible.
- **Named rivals:** WP1128 v1 admission contract; WP1280 v6 admission
  contract; common-mode shadow packet; self-calibration packet; external
  theorem shadow; fixture packet.
- **Risky consequences:** the Kitaev analogue separates the anchor from a
  one-bit disagreement alarm and shows common displacement is silent; the
  Aspect analogue shows internal identity calibration can hide a ninety-degree
  common rotation; WP1280 still has no `independent_frame_anchor` object; v7
  adds the anchor object and rejects common-mode shadows.
- **Strongest falsification attempt:** replay WP1128 and WP1280; compare the
  v6 and v7 admission contracts; test a common-mode shadow packet with all
  v6 fields but no independent anchor.
- **Exact residual:** the common-mode shadow packet is rejected and no actual
  packet is admitted. The independent-frame-anchor necessity conjecture
  survives. The residual is an externally sourced anchor with a separate
  fault domain and drift syndrome.
- **Disposition:** independent-frame-anchor necessity survives attempted
  falsification; context saturation selected.

## Result

The independent-frame-anchor necessity conjecture **survived** the attempted
falsification. It remains unproven, and no actual typed packet has been
admitted.

Checker: `research/flavor/checkers/wp1281_independent_frame_anchor_gate.py`

Result: `results/wp1281_independent_frame_anchor_gate.json`

Contract: `research/flavor/contracts/flavor-event-production-packet-admission.v7.json`
