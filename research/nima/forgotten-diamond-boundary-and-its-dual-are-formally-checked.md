# Forgotten-diamond boundary and its dual: checked coordinate theorem

## Delivered

`agda/ForgottenDiamondBoundary.agda` proves the exact coordinate identities for the forgotten diamond over any commutative ring. It uses `--safe --cubical --guardedness`, with no postulates or holes.

The primal complexes have degrees -1 and 0:

- the four-edge/four-vertex incidence complex, in vertex order 2,4,6,12 and edge order 24,26,4-12,6-12;
- the two-endpoint boundary complex with matrix `[[1,1],[-1,-1]]`.

Formalized:

1. both chain-map equations between the complexes;
2. both projection/section identities;
3. both degree components of the deformation-retract homotopy;
4. the cycle `(t,-t,t,-t)`, its closedness, and its image `(t,-t)` in the endpoint boundary;
5. nonvanishing of both witnesses when 1 is nonzero;
6. a further explicit deformation retract of the boundary complex onto one scalar in each degree with zero differential;
7. the transposed dual comparison, with differential minus the transpose and homotopy minus the transpose;
8. evaluation-pairing identities verifying those transpose assertions themselves;
9. the dual observer `(1,0)`, its pairing value 1 on the endpoint cycle, and its failure to be a dual boundary;
10. the one-endpoint hostile: `t -> (t,-t)` has zero kernel, so replacing the two-component boundary by one line removes the cycle.

The second retract gives the coordinate content of the stable result R direct-sum R[1]. The dual has its corresponding degree-one detecting class.

## Concrete integer regression

`agda/ForgottenDiamondBoundaryRegression.agda` instantiates the theorem over the integer commutative ring. It checks the actual `(1,-1,1,-1)` cycle, its endpoint image, both nonzero witnesses, and the nonexact dual observer with evaluation 1.

The general proofs do not infer nontriviality for the zero ring. They explicitly take the hypothesis 1 != 0 where needed.

## Fresh verification

```
agda --ignore-interfaces --transliterate -Werror \
  -i research/nima/agda \
  -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 \
  research/nima/agda/ForgottenDiamondBoundaryRegression.agda
```

Agda 2.8.0.1 completed with exit code zero and no warnings. Dependencies were freshly checked. Log: `results/forgotten-diamond-boundary-agda.log`.

The existing exact seam regression was also rerun successfully:

`uv run --with sympy python research/nima/checkers/check_typed_seam_composition.py`.

## Precise scope

These are formal coordinate identities for the finite chain comparison, not an implementation of a general derived-category or cohomology-quotient library. The linear maps are given by their explicit ring-coordinate formulas. The source interpretation as the stable colimit of the two forgotten path pieces, glued along both endpoint lines, remains the mathematical argument in `all-state-clark-sewing-is-a-balanced-counit-with-derived-seam-data.md`.

The formal dual is the transposed coefficient dual. After complex base change its matrices also give the conjugate-dual comparison because all their coefficients are real integers. No general Hermitian or analytical completion theory is formalized here.

## Relation to the newly supplied relation-depth attachment

`three-prime-balanced-counit-relation-filtration.md` combines several distinct carriers. This formal result verifies only the forgotten-diamond incidence/boundary component. It does not identify:

- the five three-prime incidence seam cycles;
- the two three-prime marginal record ghosts;
- the root-to-terminal conormal corner of dimension 210;
- or the four-event product layer of dimension 24.

Grothendieck's `../grothendieck/the-four-prime-relation-layer-has-a-forced-nonsplit-attachment.md` now supplies the additional source-generated triangle

`P -> I -> I/I^2 -> P[1]`.

Its nonzero extension class is an Ext^1 attachment for the full typed source-module family, not a Tor_2 class or a consequence of the root-corner dimensions alone. The present forgotten cycle is not silently substituted for that attaching map.

The next relation-layer comparison should therefore retain the actual multiplication inclusion P->I and its connecting morphism, and specify the functor under which they are observed. Terminal observation can annihilate relation arrows; exactness does not make that observation faithful or force its image of the extension class to remain nonzero.
