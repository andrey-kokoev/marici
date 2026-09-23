# All-eight-label projection forces label-three cancellation in any authored history representation

## An exhaustive filtered test, not a two-term assumption

The primary n=9 NNMHV nested-R index compiler gives NINE histories whose explicit momentum-twistor endpoint/path envelope omits physical label 3. Of those, only histories 9 and 27 expose **all eight** retained labels `(1,2,4,5,6,7,8,9)`; each of the other seven exposes at most seven. A degree-eight Grassmann monomial using every retained label exactly once therefore receives zero contribution from each of those seven individually.

Choose three four-flavor pairings of the local retained labels:

    M1=(1,3)(2,5)(4,7)(6,8),
    M2=(1,3)(2,6)(4,8)(5,7),
    M3=(1,3)(2,7)(4,6)(5,8).

Each uses all eight labels and has a nontrivial complete two-sheet four-mass source coefficient. History 9's ordinary product `[8,1,2,3,4][8,4,5,6,7]` contributes ZERO to each: labels 1 and 3 occur only in its outer five-bracket, so its one-flavor fermionic two-form vanishes on their common pair `(1,3)`.

For history 27, reconstruct the **full** generalized-R fermionic row from source `ξ=⟨9|x₉₈x₈₂`, BOTH inner terms involving `θ₇₂` and `θ₅₂`, and adjacent momentum-twistor incidence. The outer row is the ordinary five-bracket `[9,1,2,7,8]`. The checker calibrates the extended two-row construction against its independently sourced `(χ1,χ6)/(χ2,χ7)` transported-pair-ratio check; the latter is itself calibrated against two ordinary-R five-brackets and nontrivial parabolic `GL(4)` covariance. A key correction is retained explicitly: the full `(2,7)` pair coefficient contains the crossed `−A₇B₂` term, which an earlier shortcut omitted. The corrected shortcut and full-row checker both pass again.

At TWO newly generated generic exact four-dimensional kinematic inputs, the three complete four-mass monomial coefficients are computed from BOTH positive-cell fibre sheets with their exact source-to-`Cz` Jacobians. The corresponding three monomial products of history 27's two fermionic rows are nonzero, but the ratios (complete four-mass / history-27 fermionic product) are **NOT CONSTANT** across M1,M2,M3. No one bosonic scalar prefactor can make history 27 reproduce this all-eight-label projection. Since every other individually label-three-free authored history is zero on these monomials, **no sum consisting solely of those nine histories** equals the complete starred four-mass invariant, even with arbitrary scalar weights per history. This filtered test alone would require additional terms with individual physical-label-3 dependence that cancel in their sum, or a non-BCFW presentation. **Later correction/strengthening:** the full χ₃ restriction of ALL 41 source histories with label-3 dependence has rank 41 on two exact generic inputs, so such cancellation cannot be achieved within the 50 standard sourced histories even with arbitrary scalar weights; see `research/nima/full-label-three-restriction-rules-out-all-fifty-authored-history-span.md`.

This is a filtered fermionic obstruction, NOT a construction of that cancellation subset or a proof of the full nine-point amplitude. Endpoints bound fermionic support because each dual `θ_i` is reconstructed from its adjacent supertwistors; bosonic transported spinors change coefficients, not the set of χ variables. Arbitrary-Y form expansion and image coverage remain independent.

Checker: `research/nima/checkers/check_nine_point_all_eight_label_fermion_projection.py`; result: `research/nima/results/nine-point-all-eight-label-fermion-projection.json`. Corrected transport checker: `research/nima/checkers/check_nine_point_history27_transported_pair_ratio.py`.
