# Nested-cut naturality for the five-gon face above diagonal 13

This module checks the first nontrivial naturality square and its two-step
coherence.  The two terminal objects are the triangulations containing `13`.
They can be mapped directly to the full five-gon or first to the residual
quadrilateral and then reassembled.

```rzk
#lang rzk-1

#data MariciFact5Face13Terminal
  := marici-face13-terminal-1314
  | marici-face13-terminal-1335
```

The geometric inclusions run from the smaller terminal faces into the face
above `13`, and from there into the full five-gon dissection type.

```rzk
#define marici-face13-terminal-to-face
  ( terminal : MariciFact5Face13Terminal)
  : MariciFact5Face13
  := match terminal
      ( marici-face13-terminal-1314 ⇒ marici-face13-add14
      | marici-face13-terminal-1335 ⇒ marici-face13-add35)

#define marici-face13-terminal-direct-global
  ( terminal : MariciFact5Face13Terminal)
  : MariciFact5Dissection
  := match terminal
      ( marici-face13-terminal-1314 ⇒ marici-fact5-tri-13-14
      | marici-face13-terminal-1335 ⇒ marici-fact5-tri-13-35)

#define marici-face13-terminal-nested-global
  ( terminal : MariciFact5Face13Terminal)
  : MariciFact5Dissection
  := marici-face13-encode-dissection
      (marici-face13-terminal-to-face terminal)
```

The direct inclusion equals the composite inclusion for both nested cuts.

```rzk
#define marici-face13-nested-face-coherence
  ( terminal : MariciFact5Face13Terminal)
  : marici-face13-terminal-nested-global terminal
    =_{MariciFact5Dissection}
      marici-face13-terminal-direct-global terminal
  := match terminal
      ( marici-face13-terminal-1314 ⇒ refl
      | marici-face13-terminal-1335 ⇒ refl)
```

On regional products, the terminal cut selects one of the two quadrilateral
diagonals.  Reassembly through the quadrilateral factor must agree with the
direct global triangulation.

```rzk
#define marici-face13-terminal-regional
  ( terminal : MariciFact5Face13Terminal)
  : MariciQuadrilateralDissection
  := match terminal
      ( marici-face13-terminal-1314 ⇒ marici-quad-left-diagonal
      | marici-face13-terminal-1335 ⇒ marici-quad-right-diagonal)

#define marici-face13-regional-nested-global
  ( terminal : MariciFact5Face13Terminal)
  : MariciFact5Dissection
  := marici-face13-encode-dissection
      (marici-face13-union
        (marici-face13-terminal-regional terminal))

#define marici-face13-nested-product-naturality
  ( terminal : MariciFact5Face13Terminal)
  : marici-face13-regional-nested-global terminal
    =_{MariciFact5Dissection}
      marici-face13-terminal-direct-global terminal
  := match terminal
      ( marici-face13-terminal-1314 ⇒ refl
      | marici-face13-terminal-1335 ⇒ refl)
```

The one-step face-product square also commutes for every point of the face:
restrict to the quadrilateral, reassemble, then include globally.

```rzk
#define marici-face13-face-product-square
  ( face : MariciFact5Face13)
  : marici-face13-encode-dissection
      (marici-face13-union (marici-face13-restrict face))
    =_{MariciFact5Dissection}
      marici-face13-encode-dissection face
  := match face
      ( marici-face13-unrefined ⇒ refl
      | marici-face13-add14 ⇒ refl
      | marici-face13-add35 ⇒ refl)
```

## Boundary

This proves object-level naturality for both nested cuts through the face
`F_13`.  It does not yet compare paths between naturality proofs inside an
actual Segal type, and cyclic transport to the other four diagonal faces has
not been formalized.
