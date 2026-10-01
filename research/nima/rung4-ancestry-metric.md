# A candidate rung4 spatial and clock readout

## Explicit construction

This experiment supplies readout choices rather than treating the designation
"rung4" as a numerical metric law. Use the existing fixed-carrier realization
G4=10I4+J4 from `carrier-gram-restriction-tower.md`. That realization has an
explicit probe construction; its physical role is still a hypothesis.

Assign the four seed addresses the four coefficient basis vectors. A promoted
relationship retains both parents; its coordinate vector is the sum of their
ancestral endpoint-occurrence vectors. These coefficients count occurrences,
including repeated ancestral addresses, rather than distinct seed records.
Full packets and their ancestry remain separate from this coarse readout.

At promotion k, every vector has total coefficient weight2^k. Subtracting its
common component gives three spatial contrast coordinates. Differences within
a cycle have zero sum, so

    distance_squared(x,y) = (x-y)^T G4 (x-y) = 10 sum_i (x_i-y_i)^2.

A seed edge has squared length20. All spatial lengths below are in that fixed
reference-edge unit. The Euclidean diameter is computed over every distinct
readout position, not from hop distances. Every directed packet's candidate
length is also checked after the eight retained-total transitions to rung4.

## Normalization control

An alternative readout divides each vector by its total weight while retaining
that weight as a separate field. The child position is then the midpoint of
the two parent positions. This second convention preserves the encoded weight
information but yields a different spatial scale. Its convex hull is nested,
so its diameter cannot grow. Both readouts use the same fixed Gram and retained
packets; neither normalization is selected by the current cycle law.

| Promotion | Records | Distinct positions | Additive diameter | Averaged diameter | Common-mode elapsed candidate | Witness-tick elapsed candidate |
|---:|---:|---:|---:|---:|---:|---:|
|0|4|4|1.000000|1.000000|0|0|
|1|4|4|1.414214|0.707107|1|8|
|2|5|5|1.732051|0.433013|3|16|
|3|8|8|2.828427|0.353553|7|24|
|4|18|17|4.358899|0.272431|15|32|
|5|64|56|8.485281|0.265165|31|40|
|6|396|290|15.842980|0.247547|63|48|
|7|4552|2288|31.384710|0.245193|127|56|

Squared lengths are stored as exact rational numbers; diameters shown here are
decimal square roots. Clock candidates are exact integer readouts.

## Time candidates and degeneracy

The Gram splits into a common direction (eigenvalue14) and three contrast
directions (eigenvalue10). Its common amplitude, measured relative to the seed,
is the coefficient sum2^k. One candidate elapsed clock is therefore2^k-1.
A different operational clock counts eight descent witnesses per promotion,
relative to the initial rung4 calibration: elapsed ticks8k. These are explicit
candidate conventions, not derived proper time. G4 is positive definite; this
experiment does not infer a Lorentzian signature by relabelling one component.

Distinct histories begin sharing a spatial coordinate at promotion4. At
promotion7 there are2288 distinct positions for4552 records, and696 graph edges
have zero spatial readout length. Thus this is a pseudometric on packet records,
or a metric on their spatial images, not a faithful spatial embedding of all
records. Retaining the original records preserves the distinctions lost by
this projection.

## Outcome

The additive ancestry readout grows in spatial extent while the normalized
control contracts. This localizes a missing physical choice: how retained
multiplicity calibrates position relative to the fixed Gram reference. The
temporal choice is likewise explicit, with two different candidate clocks.
The calculation supplies conditional spatial and temporal readouts, not a
unique scale factor, physical elapsed seconds, or a cosmological solution.

## Reproduction

```
python research/nima/checkers/check_rung4_ancestry_metric.py
```

All assertions passed, including orthogonality of common/contrast components,
seed-edge calibration, all directed-packet rung4 reconstruction, and nested
convex-hull diameter for the averaging control.

- Checker: `checkers/check_rung4_ancestry_metric.py`
- Results: `results/rung4-ancestry-metric.json`
