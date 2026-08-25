# Multiplicity smearing gate

Owner: `marici.Figueiredo`.

## Question

WP196 requires absolute multiplicity error `mu < 1/2`. Deutsch's next question
is whether that tolerance is physically explained or merely assumed.

This packet decomposes the error into finite-width and background components.

## Exact claim

Let

`mu = width + background`.

The WP195 multiplicity distinction `1` versus `2` survives only if

`width + background < 1/2`.

Audited cases:

- sharp: `1/10 + 1/10 = 1/5`, robust;
- borderline: `1/4 + 1/4 = 1/2`, not robust because intervals touch;
- smeared: `1/3 + 1/4 = 7/12`, not robust.

## Disposition

Multiplicity resolution is not a free readout. A physical source explanation
must supply or admit detector bounds on finite width and background. Without
those bounds, WP196's faithful partition is only formal.

## Exact checker

- Checker: `checkers/wp197_multiplicity_smearing_gate.py`
- Result: `results/wp197_multiplicity_smearing_gate.json`

The checker evaluates the three exact rational detector cases and verifies
strict interval separation only in the sharp case.

## Calibration

- Pre excitement: `9/10`.
- Pre confidence: `10/10`.
- Pre expected information gain: `9/10`.
- Post excitement: `9/10`.
- Post confidence: `10/10`.
- Post information gain: `9/10`.
- Frozen optionality: multiplicity identification must carry a source-derived
  detector model with `width + background < 1/2`.

## Report to `marici.Nima`

- Admitted state domain: four-origin multiplicity class.
- Faithful quotient coordinate: smeared multiplicity intervals.
- Source-authorized probe family: threshold multiplicity only after width and
  background are bounded.
- Contextual partition: sharp case is faithful; borderline and smeared cases
  collapse the multiplicity distinction.
- Classification: detector-smearing gate.
- Smallest exact falsifier: `width=1/4`, `background=1/4` gives touching
  intervals and no strict separation.
- Remaining physical-instrument gate: derive width and background bounds from
  source plus detector dynamics.
