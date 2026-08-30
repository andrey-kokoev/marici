# Prime-two 43/44 optical sign-flip prediction

## Prediction

The completed prime-two architecture predicts a threshold at exactly the
forty-fourth gamma channel:

- the 43-channel bank has a negative even mode;
- the 44-channel bank has a positive even ground mode;
- the 44-channel odd sector remains positive.

This is not a smooth improvement claim. It is an adjacent-truncation sign
change fixed by the half-integer gamma tower.

## Why the prediction follows

Nima's directed level-43 determinant has a sign change below zero, so the
43-channel operator has an even negative eigenvalue. At level 44, the odd
weighted-Schur certificate excludes the whole odd negative spectrum. The
same bound excludes poles of the even Riccati chart. Its response is Loewner
monotone and has inertia `(43 negative, 1 positive)` both at the negative
limit and at zero, excluding every even nonpositive root. Hence the
44-channel operator is strictly positive.

The omitted gamma tail is positive term by term, so later levels cannot undo
the repair.

## Optical falsifier

Drive simultaneous 43-channel and 44-channel complementary-Lorentzian banks
from one coherent source. Use one preregistered even near-null waveform and an
odd parity control. Interleave source-off frames independently in both banks.

The outcome must be:

`43-even < 0 < 44-even`, with `44-odd > 0`.

A common positive gain cannot change this sign pattern. Independent gain
tuning, unsubtracted offsets, or post-hoc input-mode selection invalidate the
run.

This is the first direct optical prediction of the completed archimedean
architecture. Failure rejects the proposed physical realization or one of
its source-derived sewing laws. Passing it tests the prime-two completion; it
does not by itself establish the Riemann hypothesis.

## Verification

```text
python research/aspect/checkers/check_prime_two_43_44_optical_sign_flip.py
```
