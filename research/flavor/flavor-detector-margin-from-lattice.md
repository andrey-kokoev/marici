# Detector margin from lattice

Owner: `marici.Figueiredo`.

## Question

WP198 left detector bounds external. This packet asks whether the finite
two-port mediator lattice itself can derive the WP197 multiplicity margin.

## Exact claim

The source-side lattice supplies multiplicity spacing, but not detector width
or background. The margin rule is:

`width + background < spacing/2`.

For unit multiplicity spacing this is the WP197 rule:

`width + background < 1/2`.

Audited cases:

- source only: spacing exists, width/background absent, no margin proof;
- sharp detector: `1/10 + 1/10 = 1/5`, passes;
- borderline detector: `1/4 + 1/4 = 1/2`, fails strict separation;
- smeared detector: `1/3 + 1/4 = 7/12`, fails.

## Disposition

The finite mediator-lattice constructor does not derive the detector margin by
itself. It still needs an independently admitted detector law bounding width
and background.

This keeps WP198's detector gap open.

## Exact checker

- Checker: `checkers/wp199_detector_margin_from_lattice.py`
- Result: `results/wp199_detector_margin_from_lattice.json`

The checker evaluates source-only and detector-bound cases using exact
rational arithmetic.

## Calibration

- Pre excitement: `8/10`.
- Pre confidence: `10/10`.
- Pre expected information gain: `8/10`.
- Post excitement: `8/10`.
- Post confidence: `10/10`.
- Post information gain: `8/10`.
- Frozen optionality: derive detector width/background from an actual detector
  law, not from multiplicity spacing alone.

## Report to `marici.Nima`

- Admitted state domain: finite mediator-lattice detector-margin candidates.
- Faithful quotient coordinate: spacing/width/background margin inequality.
- Source-authorized probe family: none from source-only lattice.
- Contextual partition: source-only has no margin proof; only sharp detector
  contracts pass.
- Classification: detector-law audit.
- Smallest exact falsifier: source-only spacing does not bound width or
  background.
- Remaining physical-instrument gate: derive detector width and background
  bounds.
