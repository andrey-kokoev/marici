# The Tate reflection lift is natural under the first Cut enlargement

Date: 2026-08-23

The first enlargement test is the eight-point physical (6\times4) Cut.
The established source calculation gives, for every physical cut (D),

\[
\operatorname{Res}_{D}H_8
=q_4\otimes H_6^{\rm mark}.
\]

The eight cuts form one (D_8)-orbit.  After the global sheet transform,
all eight primary residue coefficients are (+1), while every nested,
crossing, contact, and double-residue correction remains zero.

The loaded six-point reflection lift has already been proved unique for its
frozen marked signature.  Therefore its occurrence on each
(H_6^{\rm mark}) Cut factor cannot be replaced by a different lift.
Consequently:

\[
\boxed{
\operatorname{Cut}_D\circ H_{\rm refl}^{(8)}
=
(1_{q_4}\otimes H_{\rm refl}^{(6)})
\circ\operatorname{Cut}_D
}
\]

in the fs/Kato sector for all eight physical cuts.

This is the first nontrivial arity-enlargement test of the six-face
conductor homotopy.  It shows that the comparison is transported by the
Carrier's Cut operation rather than being an isolated six-point repair.
No raw-scheme six-functor statement is claimed.

Evidence:

- `research/nima/checkers/check_tate_reflection_lift_eight_point_cut_naturality.py`
- Entries 435, 542, and 544.
