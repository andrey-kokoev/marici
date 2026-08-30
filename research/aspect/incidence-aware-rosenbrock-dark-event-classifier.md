# Incidence-aware Rosenbrock dark-event classifier

## Joined packet

Combine Buzzard's exact passive realization with the denominator-three
incidence port.  The state-space fixture is

`x_next=A x+B u`,

with

`A=3/5`, `B=-12/25`,

and selected/complementary outputs

`y_selected=(4/5)x+(9/25)u`,

`y_complement=(4/5)u`.

At

`lambda=5/3`, `x=-9/20`, `u=1`,

the Rosenbrock state equation and selected output both vanish, while the
complementary output equals `4/5`.  This is a selected-port transmission zero,
not a zero of the complete output packet.

Attach the fractional-endpoint incidence output from the normalized
denominator-three source:

`y_incidence=2epsilon/(1+2epsilon) u`.

At `epsilon=1/5`, it equals `2/7`.  The canonical integer source has the same
selected and complementary fixture but zero fractional-incidence output.

## Four-way classification

For every scalar dark event, inspect the complete packet and retained history.

### Packet zero

The selected output and every complementary, incidence, and history port
vanish.  Only this is a zero of the faithful packet.

### Transmission zero

The Rosenbrock kernel equations hold for the selected output, but at least one
complementary output is bright.

### Incidence alias

Canonical and hostile scalar outputs agree while an endpoint-incidence port
differs.  The scalar closure has forgotten source type.

### Normalization erasure

The scalar transition is flat while the retained affine or logarithmic
history is nonzero.  Constructor response has been cancelled rather than
absent.

The exact joined fixture is simultaneously a transmission zero and an
incidence alias.  It is not a packet zero.  These labels are compatible rather
than mutually exclusive because they answer different typed questions.

## Relation to the two-prime theta hostile

At the off-seam zero of `H_2+H_3`, the selected scalar vanishes while both
local prime amplitudes and their dagger power remain nonzero.  It receives the
same transmission-zero classification.  If the denominator-three incidence
probe is also bright, the record additionally certifies source-incidence
aliasing.

## Apparatus record

One acquisition must retain:

- parameter, state, and input witness;
- selected scalar amplitude;
- every complementary local amplitude;
- dagger power;
- endpoint-incidence amplitudes;
- affine forcing and counterphase history;
- source labels and calibration matrix.

The classifier operates on this record.  It never infers packet zero from a
single dark detector.

Strominger's path observable is an orthogonal fifth label: a valid endpoint
gate may still be path-disconnected inside the symmetry-fixed locus.  Full
path tomography should therefore accompany state/output classification when
the constructor itself is claimed executable.

## Verification

```text
uv run --with sympy --with mpmath python research/aspect/checkers/check_incidence_aware_rosenbrock_classifier.py
```
