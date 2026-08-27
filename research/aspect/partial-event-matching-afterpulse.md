# Partial optical event matching with a copied afterpulse

## Equal counts can conceal two opposite faults

Freeze source pilots `alpha`, `beta`, and `gamma`. The detector records
`alpha`, `gamma`, and a second `gamma`: the beta event was missed and a gamma
afterpulse was added. Source and detector counts are both three.

A forced order-preserving complete join assigns the first gamma detection to
beta and silently fabricates a beta response. Count conservation and complete
matching therefore do not certify event completeness.

## What source pilots repair

Comparing pilot multiplicities exposes one missing beta and one excess gamma.
The correct data structure is a partial matching with explicit unmatched
source and detector records.

But the pilot does not solve everything. If an afterpulse inherits the parent
gamma tag, the two gamma candidates remain

```text
time 2:    amplitude 4
time 21/10: amplitude 1.
```

Pilot incidence identifies their source family but does not say which record
is the primary response and which is a detector-memory copy.

## Causal separator

Apply a detector-memory reset or recovery intervention that suppresses the
afterpulse while preserving the source pulse. In the frozen model, only the
time-two gamma record remains.

This attribution is causal only if an independent source tap verifies that the
reset did not alter pulse generation, routing, or amplitude. Otherwise the
disappearing gamma record could be a source change rather than detector-memory
suppression.

## Instrument contract

Event tables should permit at least four states:

- uniquely matched;
- multiply matched;
- unmatched source trigger;
- unmatched detector record.

Forcing every row into a pair converts missingness and afterpulsing into false
physical measurements. A copied event key is lineage evidence, not proof of a
new source event.

## Claim boundary

The checker freezes one missed beta event, one gamma-tagged afterpulse, perfect
pilot decoding, and a reset affecting only detector memory. Pilot corruption,
reset-induced source shifts, multiple afterpulse generations, and stochastic
association remain open.

## Verification

```text
python research/aspect/checkers/check_partial_event_matching_afterpulse.py
```
