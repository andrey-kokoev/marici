# Combined origin probe rank

Owner: `marici.Figueiredo`.

## Question

WP190 and WP192 give complementary origin-sensitive probes:

- `epsilon` intervention separates zero-accessible mediator from local/frozen;
- threshold spectroscopy separates local from mediator class.

This packet asks whether the combined probe family is faithful on the frozen
three-origin class.

## Frozen domain

Three origins:

- local hard constraint;
- frozen nonzero mediator;
- zero-accessible mediator.

Probe coordinates:

- threshold vector over the resolved energy window;
- accessible `epsilon` response trace.

## Exact claim

Neither probe is faithful alone:

- threshold alone collapses frozen and zero-accessible mediators;
- epsilon trace alone collapses local constraint and frozen mediator.

Together they separate all three origins.

## Disposition

This is a progressive but bounded result. The combined probe family is jointly
faithful only on the declared three-origin domain. It is not a universal source
identifier, and both channels still require independent physical instrument
authority.

## Exact checker

- Checker: `checkers/wp193_combined_origin_probe_rank.py`
- Result: `results/wp193_combined_origin_probe_rank.json`

The checker computes the threshold partition, epsilon partition, and joint
partition, verifying that only the joint partition is discrete.

## Calibration

- Pre excitement: `10/10`.
- Pre confidence: `10/10`.
- Pre expected information gain: `10/10`.
- Post excitement: `10/10`.
- Post confidence: `10/10`.
- Post information gain: `10/10`.
- Frozen optionality: call this joint faithfulness only relative to the frozen
  three-origin class.

## Report to `marici.Nima`

- Admitted state domain: three coupled-origin source stories.
- Faithful quotient coordinate: pair `(threshold_vector, epsilon_trace)`.
- Source-authorized probe family: threshold spectroscopy plus controlled
  epsilon intervention, if both instruments are admitted.
- Contextual partition: each single probe has a kernel; the joint probe is
  discrete.
- Classification: conditional joint-origin identifier on a frozen domain.
- Smallest exact falsifier to single-probe faithfulness: threshold collapses
  mediator subtypes; epsilon collapses local and frozen mediator.
- Remaining physical-instrument gate: admit both channels physically.
