# Second-direction full-image membership

## Result

The 390 targets that failed their `nx`-optimized local certificate spans were reduced against the complete A12 algebraic source image over `F_32003`.

- source rows: 43,564 (`T`, `S_K`, and `Q`);
- source-image rank: 8,793;
- targets: 6 IBP and 384 q;
- nonzero quotient residuals: 0.

Thus the local failures were basis insufficiencies, not modular nonmembership witnesses. Every target lies in the full special image over this field.

## Claim boundary

Vanishing after reduction modulo one prime does not prove rational membership. It only rules out a nonmember witness at `32003`. Exact characteristic-zero source words are still required before asserting full normal-torsor independence. No geometric or exceptional comparison is supplied.

## Disposition

Proceed to exact reconstruction for the 390 targets using full-image pivots. If exact reconstruction succeeds, the second tangent and derived normal classes vanish over the rationals; if it fails while modular ranks persist, retain the exact obstruction rather than inferring from modular data.

## Verification

- `research/voevodsky/check_cosmology_second_direction_full_image_membership.py` — exit 0
- `research/voevodsky/results/cosmology_second_direction_full_image_membership.json`
