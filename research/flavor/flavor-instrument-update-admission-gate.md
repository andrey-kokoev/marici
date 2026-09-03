# Instrument-update admission gate: WP1276

## Question

Can an event-production packet be admitted from effects and readout images
without a record-conditioned instrument update?

## DPC resolution

- **Problem:** test whether the typed UV packet can remain an effect-only
  shadow.
- **Bold conjecture:** every admissible typed UV event-production packet must
  include a record-conditioned post-record update map, sequential continuation
  law, and joint-record lineage in addition to effects, kernels, gains, and
  images.
- **Named rivals:** WP1128 v1 admission contract; effect-only packet;
  kernel-only packet; phase-gauge packet; fixture packet; partial-interface
  composition.
- **Risky consequences:** Sontag's hostile gives identical present effects
  with different post-record states and different joint future records;
  WP1128 v1 has no instrument-update object; WP1274 admits no typed packet;
  WP1275 constructs no source-selected `U`; the v2 contract adds
  source-selected `U` and instrument update as required objects.
- **Strongest falsification attempt:** replay WP1128, WP1274, and WP1275;
  compare the v1 and v2 admission contracts; test an effect-only packet
  carrying the v1 event algebra.
- **Exact residual:** the effect-only packet is rejected and no actual packet
  is admitted. The instrument-update necessity conjecture survives. The
  residual is a source-derived update map from `U` with sequential-record
  continuation and lineage.
- **Disposition:** instrument-update necessity survives attempted
  falsification; source-transversal certificate selected.

## Result

The instrument-update necessity conjecture **survived** the attempted
falsification. It remains unproven, and no actual typed packet has been
admitted.

Checker: `research/flavor/checkers/wp1276_instrument_update_admission_gate.py`

Result: `results/wp1276_instrument_update_admission_gate.json`

Contract: `research/flavor/contracts/flavor-event-production-packet-admission.v2.json`
