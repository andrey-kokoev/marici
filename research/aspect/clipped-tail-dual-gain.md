# Clipped optical tails and dual-gain repair

## Saturation can erase every recorded moment

Compare two burst laws with the same event probability `1/4`: one produces
amplitudes `+2` or `-2`, the other `+4` or `-4`. Both are otherwise zero.

Hard clipping at `+1` and `-1` maps both laws to the identical recorded
distribution

```text
-1 with probability 1/8
 0 with probability 3/4
+1 with probability 1/8.
```

Their clipped variance and fourth moment are both `1/4`, even though their true
variances are `1` and `4` and their true fourth moments are `4` and `64`.
No higher moment computed after clipping can recover the erased amplitude.

## An overflow bit is necessary but incomplete

A one-bit overflow flag records probability `1/4` for both laws. It repairs
burst counting and proves that clipping occurred, but it does not measure how
far beyond range the waveform travelled.

This separates burst rate from burst severity. Calling every overflow a value
of one preserves the first and destroys the second.

## Two minimal repairs for two questions

A second threshold at amplitude `3` directly separates the declared severity
event: probability zero for the moderate law and `1/4` for the severe law. It
still does not reconstruct arbitrary amplitudes above that threshold.

A pre-calibrated auxiliary channel with gain `1/4` remains unsaturated on both
frozen supports. Its peak records are `1/2` and `1`, recovering their amplitude
difference. The high-gain channel retains small-signal sensitivity; the
low-gain channel retains headroom.

The dual-gain channels must share a calibrated source tap, clock, and event
association. Otherwise different records may describe different optical
pulses. Tap back-action and gain uncertainty must be audited independently.

## Broader implication

Tail instrumentation needs at least three distinct records:

- the clipped science value;
- an overflow or quality flag;
- an uncensored severity port when amplitude beyond range matters.

An overflow flag is metadata about validity, not a substitute for the missing
physical amplitude.

## Claim boundary

The checker uses memoryless clipping, perfect event association, and an exact
quarter-gain auxiliary channel. Recovery dead time, pileup, uncertain gain,
and source-tap back-action remain outside the claim.

## Verification

```text
python research/aspect/checkers/check_clipped_tail_dual_gain.py
```
