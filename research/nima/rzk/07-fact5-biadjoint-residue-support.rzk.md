# Five-point biadjoint residue support at channel 13

The five planar cubic diagrams are the five triangulations of the pentagon.
This module computes which diagram terms survive the residue at channel `13`
and identifies them with the two cubic diagrams of the residual quadrilateral.
It formalizes support and factor labels, not rational coefficients.

```rzk
#lang rzk-1

#data MariciFact5PlanarCubicTerm
  := marici-cubic-term-13-14
  | marici-cubic-term-13-35
  | marici-cubic-term-14-24
  | marici-cubic-term-24-25
  | marici-cubic-term-25-35

#data MariciFact5Residue13Term
  := marici-residue13-absent
  | marici-residue13-left
  | marici-residue13-right

#define marici-biadjoint-residue13
  ( term : MariciFact5PlanarCubicTerm)
  : MariciFact5Residue13Term
  := match term
      ( marici-cubic-term-13-14 ⇒ marici-residue13-left
      | marici-cubic-term-13-35 ⇒ marici-residue13-right
      | marici-cubic-term-14-24 ⇒ marici-residue13-absent
      | marici-cubic-term-24-25 ⇒ marici-residue13-absent
      | marici-cubic-term-25-35 ⇒ marici-residue13-absent)
```

The two nonzero residue terms are indexed by the two terminal refinements of
the face above `13`.  Their lower-point factors are the two quadrilateral cubic
terms.

```rzk
#data MariciQuadrilateralCubicTerm
  := marici-quad-cubic-left
  | marici-quad-cubic-right

#define marici-face13-terminal-cubic-term
  ( terminal : MariciFact5Face13Terminal)
  : MariciFact5PlanarCubicTerm
  := match terminal
      ( marici-face13-terminal-1314 ⇒ marici-cubic-term-13-14
      | marici-face13-terminal-1335 ⇒ marici-cubic-term-13-35)

#define marici-face13-terminal-quad-factor
  ( terminal : MariciFact5Face13Terminal)
  : MariciQuadrilateralCubicTerm
  := match terminal
      ( marici-face13-terminal-1314 ⇒ marici-quad-cubic-left
      | marici-face13-terminal-1335 ⇒ marici-quad-cubic-right)

#define marici-quad-factor-residue-label
  ( term : MariciQuadrilateralCubicTerm)
  : MariciFact5Residue13Term
  := match term
      ( marici-quad-cubic-left ⇒ marici-residue13-left
      | marici-quad-cubic-right ⇒ marici-residue13-right)
```

Residue after global diagram inclusion equals the lower-point factor label.

```rzk
#define marici-biadjoint-residue13-factorization
  ( terminal : MariciFact5Face13Terminal)
  : marici-biadjoint-residue13
      (marici-face13-terminal-cubic-term terminal)
    =_{MariciFact5Residue13Term}
      marici-quad-factor-residue-label
        (marici-face13-terminal-quad-factor terminal)
  := match terminal
      ( marici-face13-terminal-1314 ⇒ refl
      | marici-face13-terminal-1335 ⇒ refl)
```

The remaining three global cubic diagrams have no pole at channel `13`.

```rzk
#define marici-biadjoint-residue13-no-pole-14-24
  : marici-biadjoint-residue13 marici-cubic-term-14-24
    =_{MariciFact5Residue13Term} marici-residue13-absent
  := refl

#define marici-biadjoint-residue13-no-pole-24-25
  : marici-biadjoint-residue13 marici-cubic-term-24-25
    =_{MariciFact5Residue13Term} marici-residue13-absent
  := refl

#define marici-biadjoint-residue13-no-pole-25-35
  : marici-biadjoint-residue13 marici-cubic-term-25-35
    =_{MariciFact5Residue13Term} marici-residue13-absent
  := refl
```

## Interpretation boundary

This proves the support-level factorization statement

```text
terms with a 13 pole  <->  cubic terms of the residual quadrilateral.
```

It does not define propagator variables, addition, rational functions,
canonical forms, or the numerical residue `1/X14 + 1/X35`.  Those require a
separate algebraic interpretation of these term labels.
