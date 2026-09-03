# Semistable geometric cone cell

## Question

Does the ambient ordinary blowup contain a genuine cone over the exceptional triangle, even though the exceptional divisor alone has no face?

## Claim boundary

Yes. Start with the transverse hyperplanes

`U=0`, `V=0`, `U+V+P=0`

in the three-dimensional normal slice. Their coefficient determinant is one. In the blowup of the origin, the exceptional divisor is `P2`, and the strict transforms cut its three triangle lines.

The ambient SNC dual complex has vertices `E,X,Y,Z` and three 2-cells

`[E,X,Y]`, `[E,Y,Z]`, `[E,Z,X]`.

Their sum `Gamma` has boundary

`[X,Y]+[Y,Z]+[Z,X]`;

all radial edges cancel. Thus the star of `E` is a disk coning the exceptional link cycle.

The earlier no-face result was correct only inside `E`. Its extrapolation to the ambient boundary is superseded.

## Disposition

A genuine geometric cone cell exists at the incidence level and matches the local carrier equations. The realization map, Thom normalization, full tame-unit boundary, and naturality remain unverified. The next leaf computes whether `Gamma` maps exactly to `(Xi_log,-sigma123)`.

## Verification

- `research/voevodsky/check_cosmology_semistable_geometric_cone_cell.py`
- Execution pending: structured-command MCP is unavailable in this turn, so no results JSON is claimed.
