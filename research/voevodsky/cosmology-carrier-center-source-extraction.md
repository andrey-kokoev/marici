# Carrier-center source extraction

## Question

Does the authoritative dependency chain define the global principal center needed for descent?

## Claim boundary

No global carrier object is materialized in that chain. The exceptional checker hardcodes the `P2` triangle; the semistable checker uses a local `A3` transverse triple; the DNC and rank-26 checkers compose row-module results and counts.

The chain proves a local ideal identity, determinant-one regularity, the exceptional labeled triangle, and relation-module absorption. It does not define a global scheme or stack `X`, ideal sheaf `I_C`, wall sections, transition cocycle, regular-embedding certificate, or map from the rank-26 presentation to the ambient blowup complex.

Therefore global descent is neither proved nor refuted. The local integral `HomotopyLift` and the conditional regularity theorem remain valid.

A sufficient future carrier packet must define `X,C`, prove rank three for `I_C/I_C^2`, label and orient the three conormals, and construct the relation-to-geometric-DNC comparison.

## Disposition

The missing object is a typed global carrier constructor. The next leaf constructs the horn universally for ordered transverse triples, allowing any future carrier map to pull it back.

## Verification

- `research/voevodsky/check_cosmology_carrier_center_source_extraction.py`
- Execution pending: structured-command MCP is unavailable in this turn, so no results JSON is claimed.
