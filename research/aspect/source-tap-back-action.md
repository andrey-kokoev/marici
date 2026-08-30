# Source-tap back-action audit

## Question

Can the optical tap used to monitor reset-induced source changes identify the
untapped source statistic without assuming that the tap is noninvasive?

## One-tap alias

With source statistic `S`, tap strength `t`, and affine loading coefficient
`b`, the monitor records `S + bt`. One nonzero tap strength cannot distinguish
the intercept from loading. The checker constructs two distinct `(S,b)` pairs
with the same record.

Thus a source monitor at one fixed coupling does not establish the source value
that would exist without the monitor.

## Two-tap affine repair

Measure every reset condition at two independently calibrated tap strengths.
The untapped intercept is

```text
S = (t2 M1 - t1 M2)/(t2-t1).
```

The exact fixture uses condition-dependent loading and recovers all four
untapped source records. These records can then enter the memory-factorial
subtraction without assuming zero monitor back-action.

## Curvature hostile and third tap

If loading contains `c t^2`, two-point linear extrapolation is biased by
`-c t1 t2`. For taps `1/10` and `1/5` with curvature `1/8`, the false intercept
shift is `-1/400`.

A third equally spaced tap at `3/10` exposes the curvature through a nonzero
second difference and recovers the quadratic intercept exactly:

```text
S = 3 M(1/10) - 3 M(1/5) + M(3/10).
```

This identifies one declared quadratic loading mode, not arbitrary monitor
back-action.

## Claim boundary

Tap strengths must be independently calibrated, and source drift across tap
settings must be controlled or interleaved. Monitor-detector gain, reset–tap
interaction, hysteresis, and higher loading orders remain separate ports.

## Verification

Run:

```text
python research/aspect/checkers/check_source_tap_back_action.py
```

The dependency-free exact checker verifies the one-tap alias, two-tap affine
recovery, quadratic hostile, and three-tap repair.
