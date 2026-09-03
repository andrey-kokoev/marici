# Geometric-pair provenance gate

## Question

What distinguishes the ambient-star pair from an isomorphic freely adjoined cone?

## Claim boundary

Define `GeoPair_ord` using regular codimension-three centers with ordered common-line conormals, their blowups, actual labeled incidence strata, and transverse orientation-preserving morphisms.

There are two functors:

- `C_rel`, sending geometry to the derived arrow from the exceptional-triangle boundary complex into the ambient-star incidence complex;
- `K_Ger`, sending geometry to the relative logarithmic/Gersten comparison pair.

Wall ratios, logarithmic differentials, and tame symbols define a natural-transformation candidate `Phi:C_rel -> K_Ger` carrying `Gamma` to `tau`.

Admission requires independent source geometry, a regular center, actual strata, an incidence fundamental chain, source-derived wall ratios, complete tame boundary, and base-change naturality. An algebraic pair is sourced only with an explicit geometric witness and comparison maps; abstract isomorphism to an object in the essential image does not create provenance.

The local blowup of `A3` with walls `U,V,U+V+P` passes these gates. A formal disk can copy its chain matrix but fails the geometric and naturality gates.

## Disposition

The local ambient star is a sourced relative `HomotopyLift`; an unsourced cone remains excluded. The next leaf verifies the regulator naturality square rather than assuming it from matching local formulas.

## Verification

- `research/voevodsky/check_cosmology_geometric_pair_provenance_gate.py`
- Execution pending: structured-command MCP is unavailable in this turn, so no results JSON is claimed.
