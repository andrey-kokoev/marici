# 988 — The Global Character Splitting Survives Generic Source Walls

## Localization gate

Entry 987 established a global occurrence-equivariant splitting of the repeated (++) and (--) planes.  Test whether it survives generic specialization to the six labelled source walls

\[
(ZA_2)^2=1,
\qquad
(ZA_2B_{24})^2=1,
\qquad
(A_3/Z)^2=1,
\qquad
(A_3B_{34}/Z)^2=1,
\]

where the two composite walls each occur twice in the source occurrence basis.

For each character use the global eigendirections

\[
\mathcal L_{\chi,+}=\mathbb Q(Z)N_\chi,
\]

\[
\mathcal L_{\chi,-}=\mathbb Q(Z)
\left(L_\chi-\frac{1+Z^2}{Z^2-1}N_\chi\right).
\]

## Exact specialization

Substitute both signed roots of every wall:

\[
Z=\pm A_2^{-1},
\quad
Z=\pm(A_2B_{24})^{-1},
\quad
Z=\pm A_3,
\quad
Z=\pm A_3B_{34}.
\]

At all eight generic signed specializations, in both (++) and (--), at least one exact projective minor of the two specialized six-word vectors is nonzero.  Hence

\[
\boxed{
\operatorname{rank}
\left(
\mathcal L_{\chi,+}|_{f_i=0}
\oplus
\mathcal L_{\chi,-}|_{f_i=0}
\right)=2
}
\]

for every labelled occurrence (i), away from the already declared wall intersections and normalization divisors.

## Narrow result

\[
\boxed{
\text{the global character splitting survives the generic first source-wall specialization.}
}
\]

Thus the two lines are not merely generic-interior symmetry eigenspaces.  They remain separated in the first supported boundary fibers.  No additional boundary extension is forced at this grade.

This does not prove compatibility with iterated residues at wall intersections, nor with the degree-one exceptional chamber cell of Entry 979.

## Next falsifier

Compute the ordered double specializations at the nonempty pairwise wall intersections and compare the two residue orders.  The first possible failure is a supported Beck--Chevalley commutator that mixes the (+) and (-) lines even though every single-wall restriction preserves them.

## Verification artifacts

- `research/benincasa/marici-gm/src/bin/string_six_point_character_plane_reflection.rs`
- `research/benincasa/string-six-point-character-plane-reflection.json`

The extended checker substitutes every signed source-wall root into both exact eigendirections and computes their projective rank without sampling.

Epistemic graph event: `ev-000000000605-c5a270e1-8dfe-4a19-b99c-69658fb853f7`.
