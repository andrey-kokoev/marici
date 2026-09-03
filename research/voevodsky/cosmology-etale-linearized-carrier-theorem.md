# Étale-linearized carrier theorem

## Theorem

Let `C` be a regular codimension-three center with common line `L` and ordered conormals. Suppose an algebraic neighborhood `U` admits an étale map

`psi:U -> Tot(N_C/X)`

that is the identity on `C`, preserves orientation, and pulls the three walls back from the ordered linear coordinates.

Étale flatness and pullback of the center ideal identify `DNC(U,C)` with the corresponding base change of the normal-model DNC. Blowup and exceptional incidence strata commute with this base change.

Pulling back the normal-model ratios, symbol, tame tuple, star, and chosen nullhomotopy gives an algebraic integral total `HomotopyLift` on the DNC neighborhood, with

`d Phi(Gamma)=(Xi,-sigma123)`

and zero radial and codimension-two residuals. The construction is functorial for Cartesian maps preserving the certificate.

This is a neighborhood theorem. It neither extends over unrelated carrier points nor gives a rank-26 `ElementLift`.

The local polynomial `A3` chart is an instance. No intended global carrier neighborhood map is materialized.

## Disposition

Étale linearization is a complete algebraic effectivity certificate near the center. The next leaf determines whether the p-normal target requires any extension beyond that neighborhood.

## Verification

- `research/voevodsky/check_cosmology_etale_linearized_carrier_theorem.py`
- Execution pending: structured-command MCP is unavailable in this turn, so no results JSON is claimed.
