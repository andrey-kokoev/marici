# Nondegenerate two-Segal fixture for the five-gon refinement nerve

The five-gon refinement poset has ten nondegenerate length-two chains.  Each
starts at the empty dissection, passes through one diagonal, and ends at one of
the two triangulations containing that diagonal.  This module proves that a
nondegenerate two-simplex is equivalent to its composable two-arrow spine.

```rzk
#lang rzk-1

#data MariciFact5TwoSpine
  := marici-spine-13-1314
  | marici-spine-13-1335
  | marici-spine-14-1314
  | marici-spine-14-1424
  | marici-spine-24-1424
  | marici-spine-24-2425
  | marici-spine-25-2425
  | marici-spine-25-2535
  | marici-spine-35-1335
  | marici-spine-35-2535

#data MariciFact5NondegenerateTriangle
  := marici-triangle-13-1314
  | marici-triangle-13-1335
  | marici-triangle-14-1314
  | marici-triangle-14-1424
  | marici-triangle-24-1424
  | marici-triangle-24-2425
  | marici-triangle-25-2425
  | marici-triangle-25-2535
  | marici-triangle-35-1335
  | marici-triangle-35-2535
```

The middle and terminal vertices make the incidence content explicit.

```rzk
#define marici-fact5-spine-middle
  ( spine : MariciFact5TwoSpine)
  : MariciFact5Dissection
  := match spine
      ( marici-spine-13-1314 ⇒ marici-fact5-only13
      | marici-spine-13-1335 ⇒ marici-fact5-only13
      | marici-spine-14-1314 ⇒ marici-fact5-only14
      | marici-spine-14-1424 ⇒ marici-fact5-only14
      | marici-spine-24-1424 ⇒ marici-fact5-only24
      | marici-spine-24-2425 ⇒ marici-fact5-only24
      | marici-spine-25-2425 ⇒ marici-fact5-only25
      | marici-spine-25-2535 ⇒ marici-fact5-only25
      | marici-spine-35-1335 ⇒ marici-fact5-only35
      | marici-spine-35-2535 ⇒ marici-fact5-only35)

#define marici-fact5-spine-terminal
  ( spine : MariciFact5TwoSpine)
  : MariciFact5Dissection
  := match spine
      ( marici-spine-13-1314 ⇒ marici-fact5-tri-13-14
      | marici-spine-13-1335 ⇒ marici-fact5-tri-13-35
      | marici-spine-14-1314 ⇒ marici-fact5-tri-13-14
      | marici-spine-14-1424 ⇒ marici-fact5-tri-14-24
      | marici-spine-24-1424 ⇒ marici-fact5-tri-14-24
      | marici-spine-24-2425 ⇒ marici-fact5-tri-24-25
      | marici-spine-25-2425 ⇒ marici-fact5-tri-24-25
      | marici-spine-25-2535 ⇒ marici-fact5-tri-25-35
      | marici-spine-35-1335 ⇒ marici-fact5-tri-13-35
      | marici-spine-35-2535 ⇒ marici-fact5-tri-25-35)
```

The Segal map forgets the filled triangle and retains its adjacent-arrow
spine.  The filler reconstructs the unique triangle.

```rzk
#define marici-fact5-triangle-spine
  ( triangle : MariciFact5NondegenerateTriangle)
  : MariciFact5TwoSpine
  := match triangle
      ( marici-triangle-13-1314 ⇒ marici-spine-13-1314
      | marici-triangle-13-1335 ⇒ marici-spine-13-1335
      | marici-triangle-14-1314 ⇒ marici-spine-14-1314
      | marici-triangle-14-1424 ⇒ marici-spine-14-1424
      | marici-triangle-24-1424 ⇒ marici-spine-24-1424
      | marici-triangle-24-2425 ⇒ marici-spine-24-2425
      | marici-triangle-25-2425 ⇒ marici-spine-25-2425
      | marici-triangle-25-2535 ⇒ marici-spine-25-2535
      | marici-triangle-35-1335 ⇒ marici-spine-35-1335
      | marici-triangle-35-2535 ⇒ marici-spine-35-2535)

#define marici-fact5-spine-fill
  ( spine : MariciFact5TwoSpine)
  : MariciFact5NondegenerateTriangle
  := match spine
      ( marici-spine-13-1314 ⇒ marici-triangle-13-1314
      | marici-spine-13-1335 ⇒ marici-triangle-13-1335
      | marici-spine-14-1314 ⇒ marici-triangle-14-1314
      | marici-spine-14-1424 ⇒ marici-triangle-14-1424
      | marici-spine-24-1424 ⇒ marici-triangle-24-1424
      | marici-spine-24-2425 ⇒ marici-triangle-24-2425
      | marici-spine-25-2425 ⇒ marici-triangle-25-2425
      | marici-spine-25-2535 ⇒ marici-triangle-25-2535
      | marici-spine-35-1335 ⇒ marici-triangle-35-1335
      | marici-spine-35-2535 ⇒ marici-triangle-35-2535)
```

Both Segal inverse laws compute constructorwise.

```rzk
#define marici-fact5-spine-fill-section
  ( spine : MariciFact5TwoSpine)
  : marici-fact5-triangle-spine (marici-fact5-spine-fill spine)
    =_{MariciFact5TwoSpine} spine
  := match spine
      ( marici-spine-13-1314 ⇒ refl
      | marici-spine-13-1335 ⇒ refl
      | marici-spine-14-1314 ⇒ refl
      | marici-spine-14-1424 ⇒ refl
      | marici-spine-24-1424 ⇒ refl
      | marici-spine-24-2425 ⇒ refl
      | marici-spine-25-2425 ⇒ refl
      | marici-spine-25-2535 ⇒ refl
      | marici-spine-35-1335 ⇒ refl
      | marici-spine-35-2535 ⇒ refl)

#define marici-fact5-spine-fill-retraction
  ( triangle : MariciFact5NondegenerateTriangle)
  : marici-fact5-spine-fill (marici-fact5-triangle-spine triangle)
    =_{MariciFact5NondegenerateTriangle} triangle
  := match triangle
      ( marici-triangle-13-1314 ⇒ refl
      | marici-triangle-13-1335 ⇒ refl
      | marici-triangle-14-1314 ⇒ refl
      | marici-triangle-14-1424 ⇒ refl
      | marici-triangle-24-1424 ⇒ refl
      | marici-triangle-24-2425 ⇒ refl
      | marici-triangle-25-2425 ⇒ refl
      | marici-triangle-25-2535 ⇒ refl
      | marici-triangle-35-1335 ⇒ refl
      | marici-triangle-35-2535 ⇒ refl)
```

## Boundary

This is the complete nondegenerate two-simplex Segal check for the five-gon.
Degenerate simplices carrying identity arrows and the realization as a genuine
simplicial type remain to be constructed.  Since the five-gon refinement poset
has height two, it has no nondegenerate simplices above dimension two.
