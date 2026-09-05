# Five-gon single-diagonal residual face

This module constructs the first finite face-product fixture.  For the diagonal
`13` in a labelled five-gon, the upper interval has three elements: the
unrefined diagonal and its two triangulation refinements.  The only nontrivial
region is a quadrilateral, whose dissection type has the same three elements.
The maps below are explicit inverses.

```rzk
#lang rzk-1

#data MariciFact5Face13
  := marici-face13-unrefined
  | marici-face13-add14
  | marici-face13-add35

#data MariciQuadrilateralDissection
  := marici-quad-empty
  | marici-quad-left-diagonal
  | marici-quad-right-diagonal
```

Restriction removes the fixed diagonal `13` and records the remaining
dissection of the quadrilateral region.  Union restores `13`.

```rzk
#define marici-face13-restrict
  ( face : MariciFact5Face13)
  : MariciQuadrilateralDissection
  := match face
      ( marici-face13-unrefined ⇒ marici-quad-empty
      | marici-face13-add14 ⇒ marici-quad-left-diagonal
      | marici-face13-add35 ⇒ marici-quad-right-diagonal)

#define marici-face13-union
  ( regional : MariciQuadrilateralDissection)
  : MariciFact5Face13
  := match regional
      ( marici-quad-empty ⇒ marici-face13-unrefined
      | marici-quad-left-diagonal ⇒ marici-face13-add14
      | marici-quad-right-diagonal ⇒ marici-face13-add35)
```

Both inverse laws compute by constructor reduction.

```rzk
#define marici-face13-restrict-union
  ( regional : MariciQuadrilateralDissection)
  : marici-face13-restrict (marici-face13-union regional)
    =_{MariciQuadrilateralDissection} regional
  := match regional
      ( marici-quad-empty ⇒ refl
      | marici-quad-left-diagonal ⇒ refl
      | marici-quad-right-diagonal ⇒ refl)

#define marici-face13-union-restrict
  ( face : MariciFact5Face13)
  : marici-face13-union (marici-face13-restrict face)
    =_{MariciFact5Face13} face
  := match face
      ( marici-face13-unrefined ⇒ refl
      | marici-face13-add14 ⇒ refl
      | marici-face13-add35 ⇒ refl)
```

The two proper refinements have distinct terminal constructors.  This retains
the branching that a later refinement nerve must represent as two arrows from
the same face object, not as two proofs of one arrow.

```rzk
#data MariciFact5Face13ProperRefinement
  := marici-face13-refine-by14
  | marici-face13-refine-by35

#define marici-face13-refinement-target
  ( refinement : MariciFact5Face13ProperRefinement)
  : MariciFact5Face13
  := match refinement
      ( marici-face13-refine-by14 ⇒ marici-face13-add14
      | marici-face13-refine-by35 ⇒ marici-face13-add35)
```

## Boundary

This proves one finite upper-interval product after suppressing the
contractible triangular-region factor.  It does not yet derive the three face
constructors from a generic diagonal-family representation, prove that the two
proper refinements are the only compatible additions, or construct the Segal
nerve.
