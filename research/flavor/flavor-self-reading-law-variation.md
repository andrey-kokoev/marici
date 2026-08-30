# Self-reading law variation

Owner: `marici.Figueiredo`.

## Question

WP203 declared a self-reading constructor law that fixes detector sharpness and
actuator radius. This packet attacks that declaration:

Can the instrument constants vary while the source-side tuple remains fixed?

## Exact claim

Yes. The same source-side tuple

`K=64`, HNF domain, epsilon/threshold/multiplicity probes

admits multiple self-reading variants:

- `sharp_radius6`: passes;
- `sharp_radius7`: passes;
- `sharper_radius6`: passes;
- `borderline_radius6`: fails detector margin.

Thus the source-side tuple does not derive the instrument constants.

## Disposition

WP203 remains a valid frozen candidate, but not a derived hard-to-vary
explanation. Its constants are hard to vary only after they are stipulated. A
real explanation must derive why the self-reading law has `width=1/10`,
`background=1/10`, and radius `6`, rather than another compatible or failing
variant.

## Exact checker

- Checker: `checkers/wp204_self_reading_law_variation.py`
- Result: `results/wp204_self_reading_law_variation.json`

The checker verifies that several instrument-law variants share the same
source-side tuple but have different selector outcomes.

## Calibration

- Pre excitement: `9/10`.
- Pre confidence: `10/10`.
- Pre expected information gain: `9/10`.
- Post excitement: `9/10`.
- Post confidence: `10/10`.
- Post information gain: `9/10`.
- Frozen optionality: do not call WP203 explanatory until the instrument
  constants are derived.

## Report to `marici.Nima`

- Admitted state domain: self-reading law variants over a fixed source tuple.
- Faithful quotient coordinate: instrument constants and selector status.
- Source-authorized probe family: not fixed by the source-side tuple alone.
- Contextual partition: multiple variants pass; one fails; all share the same
  source-side tuple.
- Classification: self-reading derivation gap.
- Smallest exact falsifier: same source tuple admits different instrument
  constants.
- Remaining physical-instrument gate: derive the constants of the self-reading
  law.
