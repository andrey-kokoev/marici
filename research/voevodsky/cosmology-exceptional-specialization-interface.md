# Exceptional-specialization interface

## Result

The source and target are now separately typed:

- source: 43,564 labelled generators with a two-term algebraic presentation boundary;
- target: the three oriented exceptional edges with rank-two incidence boundary and primitive cycle `(1,1,1)`.

Three interface fields remain absent: support correspondence, generator specialization, and chain residual.

## Falsification

Mapping `g1`, `g2`, and `g3` to the three displayed exceptional edges by order is not source-derived. It leaves `K`, `g23`, and `g31` unmapped and supplies neither images for all generators nor a boundary-commutation residual.

## Disposition

Retain the independently typed algebraic source and exceptional target. Do not populate exceptional specialization.

The first missing typed object is a blowup-derived correspondence from the six K/q pole loci or their geometric cycles to the three strict-transform lines on `E=P2`. Its acceptance test is recorded once. No waiting-only bridge leaf is opened; the next executable task reassesses the supported-comparison interface using the fields now populated.

## Verification

- `research/voevodsky/check_cosmology_exceptional_specialization_interface.py` — exit 0
- `research/voevodsky/results/cosmology_exceptional_specialization_interface.json`
