# Mirrored phase schedule for the determinant instrument

## Question

Can differential analyzer phase drift manufacture a false X-state NPT record,
and what acquisition schedule prevents it?

## The unsafe assembly

A common phase-frame rotation preserves the coherence norm exactly. The danger
appears when `Re(z)` and `Im(z)` are assembled from different times and hence
different rotated frames. Those two numbers need not be components of any one
coherence vector.

The exact hostile starts from a true determinant-boundary record with
`z=(3+4i)/100` and `b=c=1/20`. Take two phase frames with cosine `3/5` and
opposite sine `4/5`. Combining the real component from the negative-angle
block with the imaginary component from the positive-angle block produces
false NPT residual `36/15625`.

## Mirrored complete-block schedule

Acquire all four correlation settings needed for both quadratures in one
short block at phase `+epsilon`, then repeat the complete block at the mirrored
phase `-epsilon`. Reconstruct one coherence vector per block before averaging
the two vectors.

The odd phase component cancels exactly. The averaged vector is the true
coherence multiplied by `cos(epsilon)`. Its norm can only decrease, so a
strictly positive measured determinant remains a safe NPT certificate. The
checker includes such a surviving positive record.

For a PPT certificate, attenuation must be reversed conservatively. If an
independent phase monitor gives `|cos(epsilon)| >= gamma`, then the true
coherence norm is at most the measured norm divided by `gamma`. The resulting
upper determinant bound is safe. At the frozen boundary and `gamma=3/5`, that
corrected upper bound returns exactly zero rather than manufacturing a sign.

## Claim boundary

The model assumes one common phase angle during each complete four-setting
block. It does not cover within-block drift, unequal setting gains, loss
imbalance, or finite-count uncertainty. The schedule is therefore a reason to
make each block fast and to record a phase-visibility lower bound, not a claim
that arbitrary drift has been removed.

## Verification

Run:

```text
python research/aspect/checkers/check_differential_phase_balanced_determinant.py
```

The dependency-free checker uses exact rational rotations and contains the
deliberate cross-time false-positive hostile.
