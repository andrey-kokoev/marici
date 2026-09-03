# Parshin-flag comparison on the exceptional triangle

## Question

Do sourced iterated residues of `{u,v}` recover the exceptional triangle cycle on the actual compactification?

## Claim boundary

Yes. The correct compactification is `P2` with three boundary lines `X Y Z=0`, with `u=X/Z` and `v=Y/Z`. The tame units, up to constants, are `v^-1`, `u`, and `v/u`. Their ordered secondary valuations at the three pair intersections are opposite in each pair and induce coefficient one on the oriented dual edges

`X->Y`, `Y->Z`, and `Z->X`.

Thus the sourced flag vector is the primitive triangle `(1,1,1)`, equivalent to the earlier `(1,-1,1)` convention after reversing the second edge orientation.

This corrects the previous use of the four-divisor `P1 x P1` compactification: there is no boundary-type mismatch on the actual three-line model. The correction does not fill the horn. The K2 symbol and its residues form a sourced total degree-two cocycle; no total degree-one precycle with that differential has been constructed.

## Disposition

The flag-comparison leaf is complete. The next leaf computes total-complex degree and exactness of `(Xi_log,-sigma123)` to distinguish a nonzero relative regulator class from a boundary.

## Verification

- `research/voevodsky/check_cosmology_Parshin_flag_exceptional_triangle_comparison.py`
- `research/voevodsky/results/cosmology_Parshin_flag_exceptional_triangle_comparison.json`
