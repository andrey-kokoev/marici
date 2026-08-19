# 984 — Reflection on the Rank-Two Character Planes

## Question

Entry 982 found two rank-two character planes, in characters (++) and (--), spanned by:

\[
L_\chi=\text{loaded occurrence projector},
\qquad
N_\chi=\text{normal-symbol projector}.
\]

Entry 983 prohibited comparison with the degree-one chamber defect.  The remaining degree-preserving test is the source-labelled reflection

\[
\tau:(A_2,B_{24})\longleftrightarrow(A_3,B_{34}),
\]

together with its dense-word permutation

\[
\pi=(0\ 2)(1\ 3)(4\ 5).
\]

Does the fixed-frame action (R=\pi^{-1}\tau) preserve either proposed line, or mix the two directions?

## Frozen objects

- Entry 977's loaded cochain and loaded corner matrix;
- Entry 982's occurrence-to-dense permutation and normal-symbol row;
- the source-labelled reflection and word permutation above;
- the character projectors for (++) and (--).

No degree-changing contraction, pairing, codifferential, or Gysin map is introduced.

## Exact result

The normal-symbol row is fixed by (R).  In the ordered basis

\[
(L_\chi,N_\chi),
\]

both rank-two character planes carry the same reflection matrix:

\[
\boxed{
[R]_\chi=
\begin{pmatrix}
-1&0\\[1mm]
\dfrac{2(1+Z^2)}{Z^2-1}&1
\end{pmatrix},
\qquad \chi\in\{++,--\}.
}
\]

Equivalently,

\[
R(N_\chi)=N_\chi,
\]

\[
R(L_\chi)
=-L_\chi+
\frac{2(1+Z^2)}{Z^2-1}N_\chi.
\]

Exact reconstruction in independent coordinate minors gives this action in both planes, and direct substitution verifies

\[
R^2=1
\]

on both basis vectors.

## Consequence

The source reflection does not preserve the loaded occurrence line.  It does canonically split each generic rank-two plane into reflection eigendirections:

\[
\mathcal P_\chi
=
\mathbb Q(Z)N_\chi
\oplus
\mathbb Q(Z)
\left(
L_\chi-
\frac{1+Z^2}{Z^2-1}N_\chi
\right),
\]

with eigenvalues (+1) and (-1), respectively.

Thus the two previously compared lines were not the invariant decomposition.  The normal-symbol line is intrinsic under the reflection, while the complementary invariant line is a source-forced correction of the loaded line.

This does not identify either eigendirection with a physical coefficient object.  It only gives the first source-derived internal separator inside the two repeated character planes.

## Narrow status

\[
\boxed{
\text{reflection fixes the normal-symbol line and canonically corrects the loaded complement.}
}
\]

The next finite test is whether the corrected (-1) eigenline is also preserved by the remaining source-labelled generators of the six-point occurrence symmetry.  Failure would show that reflection alone does not define a global submodule; success would produce a canonical degree-zero splitting without invoking Entry 979's degree-one cell.

## Verification artifact

- `research/benincasa/marici-gm/src/bin/string_six_point_character_plane_reflection.rs`
- `research/benincasa/string-six-point-character-plane-reflection.json`

The checker reconstructs the common dense-word representatives, applies the semilinear label reflection, solves the exact two-coordinate systems, verifies all six coordinates, and verifies involutivity directly.

Epistemic graph event: `ev-000000000601-e71371b9-e963-457a-b51d-a4d4d8f66985`.
