# Ambient-cone carrier functor

## Question

Does the local semistable cone realization extend functorially over the full characteristic-zero carrier?

## Claim boundary

It is functorial for ordered transverse triples. Given a smooth center with rank-three normal bundle and three labeled conormals of unit determinant, blowup, exceptional projectivization, the star chain, tame symbols, and ordered residues commute with transverse base change preserving labels and orientation.

Global extension requires more than the verified rank-26 square transport. One must prove that:

- the principal center is globally smooth;
- the three conormals orient or trivialize its normal determinant line;
- transition maps preserve the ordered star chain;
- changes of local equations create no horizontal or mixed logarithmic residues;
- the local normal slice is the actual carrier comparison rather than only a presentation chart.

The available packets establish these conditions only on the local slice `U,V,U+V+P`. Rank-26 absorption does not certify geometric descent.

## Disposition

The integral `HomotopyLift` is valid étale-locally and natural in the ordered-transverse-triple category. Global carrier extension remains unverified. The next leaf audits normal-bundle monodromy and transition actions.

## Verification

- `research/voevodsky/check_cosmology_ambient_cone_carrier_functor.py`
- Execution pending: structured-command MCP is unavailable in this turn, so no results JSON is claimed.
