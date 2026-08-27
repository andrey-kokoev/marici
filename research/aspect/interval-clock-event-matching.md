# Event matching with interval-valued clock authority

## Distinct timestamps can still be ambiguous

Freeze source-trigger times `(0,1)` and low-gain detector times `(2/5,3/5)`.
With admitted clock-and-jitter tolerance `3/5`, every detector record is
compatible with every source event. The bipartite association graph has two
perfect matchings.

The detector amplitudes `{1/2,1}` therefore support both conditional records

```text
reset -> 1/2, control -> 1
reset -> 1,   control -> 1/2.
```

Every timestamp is unique. Uniqueness of rows is not uniqueness of crossing.

## Two different repairs

Tightening the independently calibrated timing tolerance to `1/2` leaves only
the order-preserving matching in this frozen geometry. This is a quantitative
clock repair, and its authority depends on the worst-case offset and jitter
bound holding at the science epoch.

Alternatively, attach pilot symbols `alpha` and `beta` at the source trigger
and carry them through both gain branches. The pilots select one matching even
under the broader timing tolerance. This is an incidence repair rather than a
more precise clock.

Identifiers generated only after detection do not help. Labels such as
`row-17` and `row-18` distinguish detector records from each other but provide
no relation to the source events.

## Optical implementations

Useful source-carried keys include pulse-sequence numbers in a synchronized
modulator, sparse wavelength or polarization pilot codes, or a separate timing
comb referenced before the optical split. The code must not alter the science
state in an uncontrolled way; pilot leakage and modulation back-action require
their own ablation.

When events may be missing or duplicated, perfect matching must be replaced by
a partial association problem with explicit unmatched states. Forcing a
complete join silently fabricates records.

## Claim boundary

The checker covers two events, exact interval tolerance, no missing records,
and perfect pilots. Probabilistic jitter, drifting offset, pilot corruption,
pileup, and unequal event counts remain open.

## Verification

```text
python research/aspect/checkers/check_interval_clock_event_matching.py
```
