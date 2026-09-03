# Geometric nonuniqueness of the minimal extension

## Question

Is the geometric witness unique because the algebraic relative extension is initial?

## Claim boundary

No. For a fixed ordered regular triple `(X,C,L,phi,walls)`, the blowup and unsplit ambient star are canonical up to unique isomorphism. Across carrier data, witnesses are identified only by zigzags of orientation-preserving geometric isomorphisms and witnessed toroidal subdivisions whose carrier, wall, DNC, and regulator squares commute.

Equal chain pairs, boundary vectors, normal ranks, or regulators do not suffice without those geometric maps.

Residual witness data include the formal neighborhood of `C`, higher wall jets beyond `I/I^2`, the DNC-to-carrier comparison, and global transition or monodromy data. Distinct witnesses may therefore have the same ordered normal-cone realization while remaining inequivalent as carrier geometry.

The rank-one algebraic extension is initial only after forgetting geometry. Its fiber of witnesses need not be contractible or connected.

## Disposition

The local normal model is canonical for fixed first-order data but does not select a unique global carrier witness. The next leaf determines exactly which parts of the `HomotopyLift` depend only on the normal cone and which require higher formal-neighborhood data.

## Verification

- `research/voevodsky/check_cosmology_geometric_nonuniqueness_of_minimal_extension.py`
- Execution pending: structured-command MCP is unavailable in this turn, so no results JSON is claimed.
