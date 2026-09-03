# Instrument-chain necessity gate: WP1269

## Question

Can any replayed formal or partial route derive the coefficient relation while
bypassing the calibrated instrument chain?

## DPC resolution

- **Problem:** test whether the coefficient relation can become source-derived
  without closing the instrument chain.
- **Bold conjecture:** every source-derived coefficient relation must close
  the full shared-provenance instrument chain: complementary records, actuator
  normalization, common-substrate RG lift, global source ratio, mixed covariant
  portal, compiler coefficients, and calibrated physical16 readout.
- **Named rivals:** lift tomography; formal complementary records; bounded or
  formal actuator; common-substrate algebraic lift; global score ratio; mixed
  covariant portal; universal word compiler; CP transmission discriminant.
- **Risky consequences:** WP1227 has formal rank four but executable rank zero;
  WP1228 has formal feedback but no physical records; WP1229 has mathematical
  rank-two completion but no physical actuator metric; WP1230 has a priced lift
  but no selected ratio or physical16 image; WP1231 has a unique score orbit
  but no source-generated ratio; WP1232 has universal compiler capacity but no
  source law; WP1233 has a CP discriminant but T=0 is not excluded.
- **Strongest falsification attempt:** replay WP1227 through WP1233 and search
  for a formal or partial route that derives the coefficient relation while
  bypassing any calibrated instrument-chain link.
- **Exact residual:** no formal bypass is found; the instrument-chain
  necessity conjecture survives. The residual is a source-derived finite
  threshold ratio, complete CP-even packet, positive transmission margin, and
  collider-calibrated mediator instrument.
- **Disposition:** instrument-chain necessity survives attempted
  falsification; positive CP-transmission margin selected.

## Result

The instrument-chain necessity conjecture **survived** the attempted
falsification. It remains unproven, and the coefficient relation is still not
source-derived.

Checker: `research/flavor/checkers/wp1269_instrument_chain_necessity_gate.py`

Result: `results/wp1269_instrument_chain_necessity_gate.json`
