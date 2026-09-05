# Directed refinement-order isomorphism for the five-gon face

The object equivalence for the face above diagonal `13` is strengthened here
to an isomorphism of its complete directed refinement graph with the complete
directed refinement graph of the residual quadrilateral.

```rzk
#lang rzk-1

#data MariciFact5Face13Arrow
  := marici-face13-id-unrefined
  | marici-face13-id-add14
  | marici-face13-id-add35
  | marici-face13-arrow-add14
  | marici-face13-arrow-add35

#define marici-face13-arrow-source
  ( arrow : MariciFact5Face13Arrow)
  : MariciFact5Face13
  := match arrow
      ( marici-face13-id-unrefined ⇒ marici-face13-unrefined
      | marici-face13-id-add14 ⇒ marici-face13-add14
      | marici-face13-id-add35 ⇒ marici-face13-add35
      | marici-face13-arrow-add14 ⇒ marici-face13-unrefined
      | marici-face13-arrow-add35 ⇒ marici-face13-unrefined)

#define marici-face13-arrow-target
  ( arrow : MariciFact5Face13Arrow)
  : MariciFact5Face13
  := match arrow
      ( marici-face13-id-unrefined ⇒ marici-face13-unrefined
      | marici-face13-id-add14 ⇒ marici-face13-add14
      | marici-face13-id-add35 ⇒ marici-face13-add35
      | marici-face13-arrow-add14 ⇒ marici-face13-add14
      | marici-face13-arrow-add35 ⇒ marici-face13-add35)

#data MariciQuadrilateralArrow
  := marici-quad-id-empty
  | marici-quad-id-left
  | marici-quad-id-right
  | marici-quad-arrow-left
  | marici-quad-arrow-right

#define marici-quad-arrow-source
  ( arrow : MariciQuadrilateralArrow)
  : MariciQuadrilateralDissection
  := match arrow
      ( marici-quad-id-empty ⇒ marici-quad-empty
      | marici-quad-id-left ⇒ marici-quad-left-diagonal
      | marici-quad-id-right ⇒ marici-quad-right-diagonal
      | marici-quad-arrow-left ⇒ marici-quad-empty
      | marici-quad-arrow-right ⇒ marici-quad-empty)

#define marici-quad-arrow-target
  ( arrow : MariciQuadrilateralArrow)
  : MariciQuadrilateralDissection
  := match arrow
      ( marici-quad-id-empty ⇒ marici-quad-empty
      | marici-quad-id-left ⇒ marici-quad-left-diagonal
      | marici-quad-id-right ⇒ marici-quad-right-diagonal
      | marici-quad-arrow-left ⇒ marici-quad-left-diagonal
      | marici-quad-arrow-right ⇒ marici-quad-right-diagonal)
```

Restriction and union act on all five arrows, including identities.

```rzk
#define marici-face13-restrict-arrow
  ( arrow : MariciFact5Face13Arrow)
  : MariciQuadrilateralArrow
  := match arrow
      ( marici-face13-id-unrefined ⇒ marici-quad-id-empty
      | marici-face13-id-add14 ⇒ marici-quad-id-left
      | marici-face13-id-add35 ⇒ marici-quad-id-right
      | marici-face13-arrow-add14 ⇒ marici-quad-arrow-left
      | marici-face13-arrow-add35 ⇒ marici-quad-arrow-right)

#define marici-face13-union-arrow
  ( arrow : MariciQuadrilateralArrow)
  : MariciFact5Face13Arrow
  := match arrow
      ( marici-quad-id-empty ⇒ marici-face13-id-unrefined
      | marici-quad-id-left ⇒ marici-face13-id-add14
      | marici-quad-id-right ⇒ marici-face13-id-add35
      | marici-quad-arrow-left ⇒ marici-face13-arrow-add14
      | marici-quad-arrow-right ⇒ marici-face13-arrow-add35)
```

The mapped source and target are definitionally the restrictions of the
original source and target.

```rzk
#define marici-face13-restrict-arrow-source
  ( arrow : MariciFact5Face13Arrow)
  : marici-quad-arrow-source (marici-face13-restrict-arrow arrow)
    =_{MariciQuadrilateralDissection}
      marici-face13-restrict (marici-face13-arrow-source arrow)
  := match arrow
      ( marici-face13-id-unrefined ⇒ refl
      | marici-face13-id-add14 ⇒ refl
      | marici-face13-id-add35 ⇒ refl
      | marici-face13-arrow-add14 ⇒ refl
      | marici-face13-arrow-add35 ⇒ refl)

#define marici-face13-restrict-arrow-target
  ( arrow : MariciFact5Face13Arrow)
  : marici-quad-arrow-target (marici-face13-restrict-arrow arrow)
    =_{MariciQuadrilateralDissection}
      marici-face13-restrict (marici-face13-arrow-target arrow)
  := match arrow
      ( marici-face13-id-unrefined ⇒ refl
      | marici-face13-id-add14 ⇒ refl
      | marici-face13-id-add35 ⇒ refl
      | marici-face13-arrow-add14 ⇒ refl
      | marici-face13-arrow-add35 ⇒ refl)
```

The arrow maps are inverse on every directed refinement.

```rzk
#define marici-face13-arrow-union-restrict
  ( arrow : MariciFact5Face13Arrow)
  : marici-face13-union-arrow (marici-face13-restrict-arrow arrow)
    =_{MariciFact5Face13Arrow} arrow
  := match arrow
      ( marici-face13-id-unrefined ⇒ refl
      | marici-face13-id-add14 ⇒ refl
      | marici-face13-id-add35 ⇒ refl
      | marici-face13-arrow-add14 ⇒ refl
      | marici-face13-arrow-add35 ⇒ refl)

#define marici-face13-arrow-restrict-union
  ( arrow : MariciQuadrilateralArrow)
  : marici-face13-restrict-arrow (marici-face13-union-arrow arrow)
    =_{MariciQuadrilateralArrow} arrow
  := match arrow
      ( marici-quad-id-empty ⇒ refl
      | marici-quad-id-left ⇒ refl
      | marici-quad-id-right ⇒ refl
      | marici-quad-arrow-left ⇒ refl
      | marici-quad-arrow-right ⇒ refl)
```

## Boundary

This proves preservation and reflection of every refinement arrow in the
single-diagonal five-gon face.  Composition is still trivial in this height-one
interval; the next module must construct the full five-gon refinement category,
where empty-to-single-to-triangulation chains supply nonidentity 2-simplices.
