# Declared normal-interface audit

## Result

The declared alternative unit normal `ny=(0,1,0)` cannot expose a distinct class. For every raw labelled row,

\[
D_{n_y}R=D_{n_x}R-D_{n_x-n_y}R.
\]

The `nx` quotient class is zero, and the difference is one of the declared p-tangent derived rows. The identity was checked on all 9,780 raw rows with zero failures. Hence the `ny` quotient class is also zero. The listed vector `nx-ny=(1,-1,0)` is tangent, not another normal.

## Claim boundary

This exhausts the declared alternatives only. The kernel of `dp=(1,1,3)` has rank two, whereas the protocol tested one tangent direction. A second integral unit normal is `(-2,0,1)`; its difference from `nx` is the independent tangent vector `(3,0,-1)`. Neither derivative has been reduced against the relation module.

## Disposition

No declared normal interface yields a nonzero class. The next executable test differentiates along `(3,0,-1)` and `(-2,0,1)` to determine whether zero-class normal independence extends across the full tangent lattice.

## Verification

- `research/voevodsky/check_cosmology_declared_normal_interface_audit.py` — exit 0
- `research/voevodsky/results/cosmology_declared_normal_interface_audit.json`
