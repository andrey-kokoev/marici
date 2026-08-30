# Source-derived repair margin

## Bounded question

What is the weakest control-theoretic form of the conjecture that generative
command capacity may grow only while repair capacity keeps a weighted defect
margin nonnegative? Can it distinguish genuine repair from reset-based
erasure?

## Toy packet

A packet contains a source specification, its current realization, a repair
capacity, and the number of inherited obligations. Ordinary mismatch has
weight one. Deleting the source has weight two per inherited obligation,
because it destroys both correction and later verification.

Define

```text
margin = repair capacity - weighted defect.
```

A proposed generative command is admitted only when:

1. a source reference remains present; and
2. the post-command margin is nonnegative.

## Hostile sequence

Begin with target bit `1`, realized bit `0`, and repair capacity one. The
margin is zero. Adding another faulty command would make it negative, so the
addition is rejected.

Source-derived repair changes the realization to the specified bit while
preserving the source. The margin becomes one, after which exactly one new
faulty command can be admitted.

A reset instead writes visible zero and deletes the source. A naive monitor
looking only for visible error flags can call this clean. The source-relative
audit cannot: the inherited obligation has become unverifiable and
uncorrectable. Reset therefore has negative true margin, fails target replay,
and cannot authorize new generation.

## Control interpretation

The safety condition is a one-step controlled-invariance gate on the viable
set `margin >= 0`. But invariance alone is insufficient. The allowed repair
input must also carry a refinement witness from the pre-state source
obligation to the post-state realization. Reset reaches an apparently quiet
output without that witness.

Thus the weakest useful form has two clauses:

```text
viability:       post-command weighted margin >= 0
repair witness:  source obligation remains replayable after intervention
```

This does not establish the proposed metaphysical gradient. It establishes a
minimal falsifier against equating low observed defect with repairable
complexity.

## Verification

Run:

```text
python research/sontag/checkers/source_derived_repair_margin.py
```
