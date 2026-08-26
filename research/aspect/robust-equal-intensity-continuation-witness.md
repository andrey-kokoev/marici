# Robust equal-intensity continuation witness

## Question

Can two optical histories with equal endpoint intensity but different continuation states remain experimentally distinguishable after calibrated loss, finite analyzer extinction, depolarization, dark clicks, and bounded systematic error?

## Source pair

Use the reciprocal selective words from the ideal order audit. Applied to a maximally mixed input, horizontal-then-diagonal and diagonal-then-horizontal both occur with ideal probability one quarter. Their normalized continuations are diagonal and horizontal, respectively.

Route-specific attenuation is calibrated so that both histories have the same heralded survival weight `w`. Equalization is part of the frozen source preparation; it is not inferred from the downstream result.

## Noisy downstream analyzer

The final horizontal analyzer has parallel efficiency `eta_parallel` and leakage `eta_perp`. Before it, a depolarizing channel of strength `p` mixes each continuation toward the maximally mixed state. A binary detector adds a dark-click probability `d` to trials without an optical click.

For the horizontal and diagonal continuations, the difference between conditional click probabilities is

```text
(1 - d) (1 - p) (eta_parallel - eta_perp) / 2.
```

Multiplying by the common survival weight gives the absolute per-source separation. If each measured click probability has bounded systematic error `epsilon`, the worst-case criticism margin is

```text
w (1 - d) (1 - p) (eta_parallel - eta_perp) / 2 - 2 epsilon.
```

A positive margin certifies that the downstream analyzer separates the continuations even though the old endpoint intensity is equal.

## Exact benchmark

The checker freezes:

- common survival weight `1/4`;
- parallel efficiency `9/10`;
- leakage `1/10`;
- depolarization `1/5`;
- dark-click probability `1/100`;
- systematic error bound `1/100` on each absolute click probability.

The conditional click gap is `198/625`. The absolute per-source gap is `99/1250`. After adversarial systematic errors on both records, the criticism margin remains `37/625`, which is positive.

## Hostiles

The checker separately verifies that the witness disappears under any of three complete erasures:

1. zero analyzer contrast;
2. complete depolarization;
3. an always-clicking detector.

These hostiles show which calibrated resources carry the distinction. Equal endpoint intensity alone remains non-explanatory; the downstream contrast, coherence retention, and detector dynamic range jointly supply the separating capability.

## Experimental record contract

The apparatus must publish route-survival calibration, analyzer parallel and leakage efficiencies, depolarization estimate, detector dark-click calibration, and the systematic error bound. The equal-intensity claim and downstream-separation claim use distinct held-out records. Reusing the separating data to tune route equalization would make the criticism margin post-selected.

## Claim boundary

This is a finite exact robustness theorem for a heralded binary detector model. It does not supply a shot-noise sample-size bound, drift model, multiphoton correction, detector dead-time model, or laboratory calibration certificate. Those are the next physical implementation layer.

## Finite-sample extension

The companion shot-noise checker treats each route's absolute click record as
an independent Bernoulli sample mean. After reserving the full worst-case
systematic margin `37/625`, the variance of the difference of two sample means
is bounded by `1/(2N)`, where `N` trials are taken on each route. Chebyshev's
inequality therefore bounds the probability of a sign error by
`1/(2 N margin^2)`.

For a target failure probability `1/100`, the exact smallest integer certified
by this conservative bound is computed by:

```text
python research/aspect/checkers/check_robust_continuation_shot_noise.py
```

This certificate is deliberately distribution-robust but conservative. It
does not replace an exact binomial design, preregistered stopping rule, or
independence audit.

## Verification

Run:

```text
python research/aspect/checkers/check_robust_equal_intensity_continuation_witness.py
```

Both checkers are dependency-free and use exact rational arithmetic.
