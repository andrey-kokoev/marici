# 1813 — The Transverse Double Residue Carries the Normal Orientation Line

## Question

What occurrence character is carried by Entry 1811's ordered double residue?

## Wall swap

Interchange the two labelled wall occurrences:

\[
(h_1,(a,b))\longleftrightarrow(h_2,(c,d)).
\]

The quadratic form

\[
h^TL^{-T}L^{-1}h
\]

is invariant under this simultaneous row and coordinate swap. However,

\[
D=\det L\longmapsto-D.
\]

Therefore the ordered Poincaré residues obey

\[
\boxed{
\operatorname{Res}_{B}\operatorname{Res}_{A}
=-operatorname{Res}_{A}\operatorname{Res}_{B}.
}
\]

## Result

The rational quadratic quotient is tensored with the normal orientation line

\[
\boxed{
\det N^*_{A,B}.
}
\]

Under the wall-exchange group \(S_2\), this line carries the sign character.
This must be distinguished from the scalar source denominator product
\(g_Ag_B\), which is symmetric.

Thus two statements coexist without contradiction:

- the scalar occurrence product has trivial exchange character;
- the ordered derived residue has alternating exchange character.

The distinction applies to all 22 local active types and their 110 labelled
cyclic occurrences. It is intrinsic Gysin orientation data, not a new carrier
generator.

## Architectural consequence

Forgetting occurrence order before applying the residue functor erases a
physical coefficient line. The supported comparison must therefore be typed
as an oriented determinant-line map, rather than as a map from an unordered
scalar pair.

## Next falsifier

Construct the iterated threshold/wall comparison with the determinant-line
twist included. Test whether its nodal nearby-cycle line is generated
functorially and whether cyclic transport preserves the chosen ordered
orientation.

## Evidence

- research/benincasa/checkers/five_site_g5_transverse_pair_residue_orientation.py
- research/benincasa/results/five-site-g5-transverse-pair-residue-orientation.json
- Entry 1811
- allocator claim: seqclaim-2dce038f5cd63eb8afc83844