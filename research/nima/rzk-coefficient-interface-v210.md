# v210: correction — the pullback detector line is not the three-target packet

The v209 matrix calculation is valid: the internal dual of the Entry-436 pullback `H1` is one primitive integral line, and its endpoint and road row representatives both evaluate `z=(1,0,1,0,0)` to `+1`.

It does **not** follow that the separately typed `s`, `W`, and `v` target detectors all descend to those rows, nor that the physical packet coordinates are `(1,1,1)`. Their unit signatures occur in different targets:

- `s` is the generic-Q primary class;
- `W` is a paired-endpoint supported class;
- `v` is the road relation class;
- the Entry-436 `+1` values certify primitive normalizations of restrictions, not equality of these three classes or their coefficient coordinates.

Therefore the prior rank-one scaling conclusion was too strong and is withdrawn. A rank-one physical homology source can map its chosen generator to the fixed vector `a*s+b*W+c*v`; the coefficients must be computed from explicit target-to-pullback cochains. They cannot be replaced by the three structural unit normalizations.

The remaining executable gate is now exact: construct the primary, reciprocal, and relation target cochains on the rank-five `C1`, verify that each annihilates all four `d2` columns, and evaluate them on `z`. Module 232 records this corrected typing boundary.
