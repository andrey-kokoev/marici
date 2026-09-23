# An eight-support nine-point paired cell has an exact full-rank image point

The nine-point minimum-support target now has more than an eight-label top-cell lift. It lies on a **dimension-eight positive source-cell candidate** with retained labels

    (1,2,4,5,6,7,8,9),

column 3 zero, and four disjoint parallel-column pairs

    (1,2), (4,5), (6,7), (8,9).

In the eight-column positive rank-two Grassmannian, four independent paired-minor conditions reduce source dimension from 12 to eight. A subsequent PRIMARY-SOURCE AUDIT identifies this retained-eight positroid cell with the starred EIGHT-POINT four-mass ψ cell and both its kinematic branches; see `the-nine-point-four-pair-carrier-is-a-relabelled-sourced-four-mass-psi-cell.md`. Its assignment to a sourced NINE-POINT generalized-R history remains open.

## Exact nonlinear construction

The fixed-target fibre of the eight retained columns has two invisible kernel directions in each of its two source rows, hence four coefficients `(a,b,c,d)` and a determinant `q=ad-bc`. Every retained source minor is affine in the FIVE lifted variables `(a,b,c,d,q)`. The four paired-minor equations are independent linear equations in these five variables: their coefficient matrix in `(a,b,c,d)` has nonzero determinant. They determine `(a,b,c,d)` as rational AFFINE functions of `q`.

Imposing the omitted realizability equation `q=ad-bc` leaves a rational quadratic polynomial. An exact rational interval

    -19199558/10^12 < q < -19199557/10^12

has opposite polynomial signs at its endpoints, so contains exactly one simple real root of this quadratic. Along the affine solution line, the four selected paired minors vanish identically. Each of the remaining 24 ordered minors is affine in `q`; both values at BOTH rational interval endpoints are strictly positive, with a uniform exact lower bound recorded in `nine-point-paired-cell-exact.json` (approximately `2.41e-5`). Thus all 24 are positive at the actual algebraic root. The source point is exactly realizable, not merely feasible in the linear relaxation.

The actual four-minor constraint Jacobian with respect to the four-dimensional fixed-target source fibre is nonzero at the root: its determinant polynomial is coprime to the root's quadratic polynomial. Consequently the eight-dimensional cell has trivial infinitesimal fibre there and its map to the eight-dimensional target has **full rank eight**. This is a local statement at ONE image point, not an image-cover theorem.

For this same target, the independent Farkas packets exclude all 36 seven-label subsets. This cell is therefore not a redundant zero-padding of a seven-support presentation: it reaches an exactly certified minimum-eight-support target. A separate verifier reconstructs the algebraic equations, the isolating interval, 24 positivity bounds, the transversality check, and all seven-support exclusions, refusing four mutations.

## Frontier

This is a genuine higher-support, determinantal positive-cell candidate, but not yet a physical NNMHV cell. The next necessary checks are:

1. derive or source its on-shell/positroid history label rather than attaching one by matching a scalar;
2. push its NOW-COMPUTED normalized fourfold source cyclic residue through `CZ` with the algebraic branch and orientation retained (see `the-nine-point-four-pair-source-form-has-an-exact-zero-column-normalization.md`);
3. compare that pushed-forward form with a **same-external-data** nine-point generalized-R history, including normalization and pole residues;
4. test its boundary incidences against other admitted cells before any global triangulation claim.

No analytic `n^-2` completion statement follows.

Reproduce:

    uv run --with sympy python research/nima/checkers/check_nine_point_paired_cell_exact.py
    uv run --with sympy python research/nima/checkers/verify_nine_point_paired_cell_exact.py

Artifacts: `research/nima/results/nine-point-paired-cell-exact.json` and `nine-point-paired-cell-verification.json`.
