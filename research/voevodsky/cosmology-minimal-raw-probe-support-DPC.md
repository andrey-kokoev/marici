# Minimal raw-probe support: DPC boundary

## Question

What is the least support of a raw coefficient functional that annihilates every A14 grade-eight relation row and evaluates nonzero on the chosen target?

## Exact bounds

Support one is impossible: the target's unique raw column occurs in the relation packet.

Support two is impossible: among all other columns, none has the same relation-row support with coefficients proportional to the target column. The exhaustive two-column test produced no candidate.

Therefore every raw coefficient probe has support at least three.

A finite-support probe does exist at A14. The target is outside the exact relation span, so finite-dimensional linear duality separates it from that span. This existence statement is finite and nonconstructive; it neither identifies minimum support nor supplies an ambient-compatible formula.

## DPC disposition

The conjectures “support one suffices” and “support two suffices” are falsified by exact witnesses. The minimum is not established; it lies in the range three or larger. The surviving alternatives are:

- a three-coordinate cancellation probe;
- a larger sparse coordinate probe;
- a structured extraction functional whose coordinate support grows with ambient index.

The next discriminating test is an exhaustive three-column dependence search constrained to include the target column. Failure raises the exact lower bound to four; success must be followed by ambient-shift testing before it bears on all-even persistence.

## Evidence

- `research/voevodsky/results/cosmology_single_coordinate_raw_probe_DPC.json`
- `research/voevodsky/results/cosmology_two_coordinate_raw_probe_DPC.json`
