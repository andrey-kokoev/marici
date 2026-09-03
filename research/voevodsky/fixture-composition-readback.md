# Fixture composition readback

## Question

Are the finite fixture edges morphisms in one category, with the two direct edges declared as composites of the corresponding two-step routes?

## Claim boundary

This audit reads the fixture as originally declared. It does not prohibit a source owner from supplying a categorical enhancement.

## Declared structure

The fixture introduced \([x,y]\) as a labelled oriented edge in a free chain group with boundary

\[
d_1[x,y]=[y]-[x].
\]

Its checker defines edge chains and boundaries. It declares no composition operation, identity morphisms, or associativity law. Four detour triangles were later admitted explicitly as representative-change cells.

Therefore the direct edges \([w,-a]\) and \([-w,a]\) are independent edge generators, not declared composites.

## Two models on one skeleton

The same ten-edge 1-skeleton supports two distinct models:

- the declared chain model, whose four 2-cells have boundary-span rank 4;
- the maximal category-nerve closure, whose 12 available triangles span the full rank-7 cycle space.

Endpoint incidence is identical in both models and cannot decide which composition law is present.

## Horn status

The reciprocal triangle pair is combinatorially available but not canonically filled as an inner horn in the declared model. Canonical filling requires a source declaration of one category, its composition table, and the equalities

\[
(w\to -w);(-w\to -a)=w\to -a
\]

and its reciprocal mate, with conventions oriented appropriately.

## Disposition

The odd class vanishes in the maximal nerve closure but remains in the declared chain complex. Current status is `composition_horn_authority_absent`, not a mathematical failure of the available triangle boundary.

## Subsequent ordinary-domain refinement

`ordinary-mellin-affine-chain-object-v1.json` now explicitly admits every affine simplex whose image remains in the ordinary admissible convex spectral domain. Under that strengthened declaration the fixture has all 12 triangles and \(H_1=0\). The composition-authority obstruction remains relevant only outside this affine domain or when modular/cutoff transport fails to preserve the affine fillers.

## Verification

- `research/voevodsky/fixture-composition-readback-v1.json`
- `research/voevodsky/checkers/check_fixture_composition_readback.py`
- `research/voevodsky/results/fixture_composition_readback.json`
