# Coherent storage has a query-dependent horizon

## A present port can lose only some future questions

Model a stored environment qubit with phase coherence multiplied by `3/4` per
time step, while computational-basis populations remain unchanged. After `n`
steps, the `|+>` versus `|->` trace distance is `(3/4)^n`. The corresponding
formal phase-reconstruction gain is `(4/3)^n`.

The port therefore retains exact algebraic rank at every finite delay, yet its
phase-sensitive control margin decays geometrically. Meanwhile `|0>` versus
`|1>` remains perfectly distinguishable. There is no single storage lifetime:
there is a lifetime relative to a downstream probe family and an accepted
reconstruction margin.

At eight steps the phase margin is `6561/65536`, approximately `0.1001`, and
the inverse gain already exceeds nine. Population questions still have margin
one. At complete dephasing the phase distinction vanishes while the population
distinction survives.

## Constructor typing needs a deadline

An incidence edge should specify:

- the strongest downstream constructor it must support;
- the subspace or probe family on which it must act;
- the minimum acceptable singular margin;
- the maximum delay before that action;
- the clock and phase reference defining the delay.

“Coherent port available” without these qualifiers can be true physically and
false operationally. Rank-only certification hides the approach to the horizon.

## Optical instrument

Store a path- or polarization-encoded environment mode in a delay loop. At each
delay, interleave `Z`-basis population probes with `X/Y` phase probes. Estimate
direction-resolved trace-distance or process singular margins rather than one
average memory fidelity. Apply refocusing only as a separately typed actuator,
since it changes the supported future-control family.

## Claim boundary

The checker uses identical Markovian phase contractions and exact probe states.
Non-Markovian revivals, drift, pulse errors, loss, and finite-sample uncertainty
remain open.

## Verification

```text
python research/aspect/checkers/check_query_dependent_coherence_horizon.py
```
