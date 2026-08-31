# No total-lift cell in the ordinary corner blow-up

## Result

On `E=P^2`, the boundary lines are `U=0`, `V=0`, and `U+V+P=0`. Their simultaneous equations force `U=V=P=0`, which is not a projective point. Thus the boundary has three pair intersections but no triple intersection.

Its dual complex has three vertices, three edges, and no face. The edge-boundary map has rank two, so the primitive triangle cycle generates integral first homology. With no degree-two incidence cell, that cycle is not a boundary.

Therefore the ordinary oriented corner blow-up contains no source-geometric total-lift cell whose differential is `Xi_log+minus_sigma123`. The relative class remains a primitive nonboundary.

## Scope

This is a no-go for the ordinary blow-up SNC incidence complex. It does not exclude an enlarged semistable model, a sourced relative-face cone, or a Cayley-Menger compactification that adds a genuine face over the cycle. Such an enlargement must supply both the face and its chain map; adjoining an abstract cone is merely renaming `tau_p`.

## Next leaf

Determine whether admissible blow-ups or subdivisions of the SNC boundary can kill the dual-cycle class. If they preserve its homotopy type, the remaining route must introduce genuinely new source geometry rather than another resolution of the same pair.

## Verification

- `research/voevodsky/check_cosmology_exceptional_triangle_total_lift.py`
- `research/voevodsky/results/cosmology_exceptional_triangle_total_lift.json`
