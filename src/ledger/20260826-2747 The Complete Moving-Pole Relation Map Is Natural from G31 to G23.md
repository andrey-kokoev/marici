# 2747 — The Complete Moving-Pole Relation Map Is Natural from G31 to G23

## Independent target construction

Construct the (G_{23}) residue chart in two source-derived ways:

1. cyclically relabel the original (G_{12}) source formulas;
2. apply the site transposition (sigma_{12}) to the independently constructed (G_{31}) chart.

At target coordinates ((X,Y,Z)), the first construction evaluates the original source at ((Y,Z,X)). The second evaluates the (G_{31}) source at ((Y,X,Z)) and reorders retained coordinates from ((c,b)) to ((b,c)).

The two constructions agree exactly for both (K_{m CM}) and every labelled denominator.

An initially tested inverse cyclic assignment failed these source-formula gates and was rejected before interpretation.

## Full naturality audit

Under

\[
G_{31}\xrightarrow{\sigma_{12}}G_{23},
\]

the external axes map as

\[
x\leftrightarrow y,
\qquad
z\to z.
\]

The five occurrence families and three directions give 15 blocks and 39,600 raw generator comparisons.

All gates pass:

- every block contains 2640 generators;
- every generator-key map is bijective;
- all raw differentiated relation squares commute;
- all Poincaré-residue orientation squares commute;
- total raw failures: (0);
- total orientation failures: (0).

## Conclusion

The complete moving marked-pole coherence is strict across a second independently derived residue transition. Together with Entry 2741, this establishes two sides of the three-chart atlas.

It does not yet establish cocycle descent. The closing transition must be chosen with site permutation ((132)), the inverse of the first two composed permutations, so that the three transitions return every label and external axis to itself.

## Artifacts

- `research/benincasa/check_rank26_full_g31_g23_relation_naturality.py`
- `research/benincasa/rank26-full-g31-g23-relation-naturality.json`

## Next falsifier

Derive (G_{23}\to G_{12}) using the closing cycle ((132)), verify the complete moving-relation square, and compute the signed three-transition composition on generator keys and raw derivative rows. Only identity composition authorizes the global corrected adapter.
