# 2751 — The Moving-Pole Coherence Closes on the Three-Chart Atlas

## Closing transition

Derive the closing residue transition

\[
G_{23}\xrightarrow{(132)}G_{12}.
\]

The cycle ((132)) is the inverse of the first two composed site permutations. It maps retained coordinates

\[
(b,c)\longrightarrow(a,b)
\]

without exchanging their order, so its Poincaré-residue sign is (+1).

The independently transformed (G_{23}) formulas agree exactly with the original (G_{12}) formulas for (K_{m CM}) and all five labelled denominators.

## Full relation-map audit

All five occurrence families and all three external directions are tested:

- 15 occurrence-direction blocks;
- 2640 generators per block;
- 39,600 raw generator comparisons;
- key-map failures: (0);
- differentiated relation-map failures: (0);
- orientation failures: (0).

## Three-transition composition

Compose

\[
G_{12}\to G_{31}\to G_{23}\to G_{12}.
\]

The composition is identity on:

- all three external derivative axes;
- all five occurrence positions;
- every numerator exponent pair;
- the source and target kinematic point.

The residue-orientation product is

\[
(-1)(-1)(+1)=+1.
\]

Thus the signed composition is also identity.

## Conclusion

The derivative of the complete labelled marked-pole relation map defines a strict coherence cell on the three-chart residue atlas. It is source-derived, occurrence-resolved, orientation-compatible, and cocyclic.

This closes the naturality gate opened by Entry 2708. It does not by itself alter the quotient connection: the finite adapter must now be totalized with this relation-map derivative, after which the differentiated Euler identity must be rerun.

## Artifacts

- `research/benincasa/check_rank26_full_g23_g12_relation_naturality.py`
- `research/benincasa/rank26-full-g23-g12-relation-naturality.json`

## Next falsifier

Construct the corrected finite adapter as the totalization of quotient transport with the moving marked-pole relation-map coherence. Rerun the nine differentiated Euler tests. Zero defect would establish a source-natural second-jet adapter; a residual would identify a genuinely missing relation family or higher coherence.
