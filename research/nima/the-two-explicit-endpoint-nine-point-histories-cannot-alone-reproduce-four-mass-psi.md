# The two explicit-endpoint nine-point histories cannot alone reproduce four-mass ψ

## A fixed-coefficient two-history falsifier

The source's n=9 nested-R compiler exposes only two histories whose **explicit** endpoint/path envelope equals the retained four-mass labels `(1,2,4,5,6,7,8,9)` without physical `3`: ordinary-product history 9 and transported-spinor history 27. Every single history is a product of two flavor-blind fermionic δ⁴ factors and therefore has a rank-one tensor in the two-pair flavor test.

Let `F=(F_XXXX,F_YYYY,F_XXYY)` be the COMPLETE two-sheet four-mass fermion tensor for retained local pairs `X=(1,5)` and `Y=(2,6)`, computed by reconstructing both source matrices and their independent eight-by-eight `J_z`. Let `K` be the exact tensor for ordinary history 9, the product of all FIVE cyclic denominators of `[8,1,2,3,4]` and `[8,4,5,6,7]` and their proper X/Y fermion numerators. The residual necessary condition for `F=±K+(one history 27)` is

    (F_XXXX∓K_XXXX)(F_YYYY∓K_YYYY) − (F_XXYY∓K_XXYY)² = 0.

To avoid hidden singular specializations, the checker constructs **new generic rational four-dimensional external `z`** directly in the exact nullspace of a positive four-pair source point, gauges its first four rows to the identity, demands every history-9 denominator be nonzero, solves the OTHER four-pair fibre sheet using an independent quadratic, and verifies `F_XXXX` against the complete sourced-ψ companion trace. At TWO independently generated data sets, the above residual determinant is NONZERO for **both** relative signs. Even allowing an unspecified scalar λ multiplying history 9, the unique λ needed merely to make the remainder rank one is different at the two data sets: it cannot be a kinematic-independent coefficient as in the authored sum.

Hence the complete starred four-mass invariant is **not** the standalone history 27 and is **not** a fixed-sign/fixed-coefficient sum of ONLY candidates 9 and 27. This does not rule out cancellation among additional authored terms whose individual endpoint envelopes contain physical label 3, a kinematic change of basis with explicitly accounted coefficients, or a different on-shell presentation. The full n=9 history assignment and amplitude equality remain open.

Checker: `research/nima/checkers/check_nine_point_two_candidate_fermion_residual.py`; result: `research/nima/results/nine-point-two-candidate-fermion-residual.json`.
