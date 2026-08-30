# ABBA vacuum-phase twirl

## Question

What finite phase schedule makes the vacuum-port first-moment null robust to
drift during acquisition?

## Shortest exact schedule

Represent the two ancillary phase choices by signs `+1` and `-1`. For samples
at times zero through three, the schedule

```text
+ - - +
```

has signed moments

\[
\sum s_t=0,
\qquad
\sum t s_t=0,
\qquad
\sum t^2s_t=4.
\]

It therefore cancels constant coherent leakage and linear within-block drift
exactly. Exhaustive enumeration proves that four shots are minimal; the only
solutions are `+--+` and its global sign reversal `-++-`.

Simple alternation `+-+-` is balanced but has linear moment `-2`. It cancels a
stationary displacement while converting linear drift into a false residual.

## Curvature witness

ABBA does not hide the next obstruction. If the ancillary coherent amplitude
contains a quadratic coefficient `1/100` per normalized block-time squared,
its signed ABBA average is exactly `1/100`. With the `3/5`–`4/5` coupler, the
residual visibility bound is

\[
2\frac35\frac45\frac1{100}=\frac6{625}.
\]

That residual is recorded rather than declared cancelled.

## Apparatus protocol

Randomize whole ABBA blocks and their sign-reversed partners across the sealed
route schedule. Keep the four shots inside one calibration epoch. Record the
actual phase monitor for every herald. Use the measured quadratic residual as
an uncertainty contribution to the sewing visibility rather than correcting
it from the science data.

## Deutschian content

The null is supplied by an executable finite transformation with known
counterfactual behavior under drift. “Random phase” is replaced by a concrete
constructor whose cancellation order and first surviving obstruction are both
measured.

## Disposition

The vacuum first-moment gate now has a minimal drift-resistant acquisition
word. Constant and linear contamination are annihilated; quadratic curvature
remains an explicit falsifier.

## Verification

Run:

```text
python research/aspect/checkers/check_abba_vacuum_phase_twirl.py
```
