# Factorization refinement and regional face interface

This module packages the exact data needed for the dissection-refinement nerve,
the upper-interval face, its regional product, and the naturality square.  It
does not assume that arbitrary refinement data come from polygon dissections.

```rzk
#lang rzk-1

#data MariciFactRefinementLaws
  ( A : U)
  ( refines : A → A → U)
  :=
    marici-make-fact-refinement-laws
      ( refines-id : (x : A) → refines x x)
      ( refines-comp : (x y z : A)
          → refines x y → refines y z → refines x z)
      ( refines-prop : (x y : A) → is-prop (refines x y))
      ( refines-antisym : (x y : A)
          → refines x y → refines y x → x =_{A} y)
```

A retained two-simplex records the two adjacent refinements, their declared
composite, and the proof that this composite is the one supplied by the
refinement law.

```rzk
#data MariciFactTriangle
  ( A : U)
  ( refines : A → A → U)
  ( compose : (x y z : A)
      → refines x y → refines y z → refines x z)
  ( x y z : A)
  ( f : refines x y)
  ( g : refines y z)
  :=
    marici-make-fact-triangle
      ( h : refines x z)
      ( composite-witness :
          h =_{refines x z} compose x y z f g)
```

The combinatorial residual face is the upper refinement interval.

```rzk
#data MariciFactFace
  ( A : U)
  ( refines : A → A → U)
  ( coarse : A)
  := marici-make-fact-face
      ( fine : A)
      ( inclusion : refines coarse fine)
```

For a fixed dissection, the regional product is represented by a dependent
family selecting one local refinement in every region.

```rzk
#define MariciRegionalProduct
  ( A : U)
  ( Region : A → U)
  ( RegionalFact : (coarse : A) → Region coarse → U)
  ( coarse : A)
  : U
  := (r : Region coarse) → RegionalFact coarse r
```

The face-product theorem is packaged with both maps and both inverse laws.  A
future polygon module must construct this record from restriction and union of
diagonals; supplying the record does not prove those operations exist.

```rzk
#data MariciFaceProductEquivalence
  ( A : U)
  ( refines : A → A → U)
  ( Region : A → U)
  ( RegionalFact : (coarse : A) → Region coarse → U)
  ( coarse : A)
  :=
    marici-make-face-product-equivalence
      ( restrict-regions :
          MariciFactFace A refines coarse
          → MariciRegionalProduct A Region RegionalFact coarse)
      ( union-regions :
          MariciRegionalProduct A Region RegionalFact coarse
          → MariciFactFace A refines coarse)
      ( restrict-union :
          (x : MariciRegionalProduct A Region RegionalFact coarse)
          → restrict-regions (union-regions x)
            =_{MariciRegionalProduct A Region RegionalFact coarse} x)
      ( union-restrict :
          (x : MariciFactFace A refines coarse)
          → union-regions (restrict-regions x)
            =_{MariciFactFace A refines coarse} x)
```

Naturality is stated for one refinement.  `face-map` is composition of upper
interval inclusions; `regional-map` regroups refinements of child regions under
their parent regions.  The comparison path is the central square.

```rzk
#data MariciFaceProductNaturality
  ( A : U)
  ( refines : A → A → U)
  ( Region : A → U)
  ( RegionalFact : (coarse : A) → Region coarse → U)
  ( coarse finer : A)
  ( step : refines coarse finer)
  ( face-product-coarse : MariciFaceProductEquivalence
      A refines Region RegionalFact coarse)
  ( face-product-finer : MariciFaceProductEquivalence
      A refines Region RegionalFact finer)
  ( face-map : MariciFactFace A refines finer
      → MariciFactFace A refines coarse)
  ( regional-map : MariciRegionalProduct A Region RegionalFact finer
      → MariciRegionalProduct A Region RegionalFact coarse)
  :=
    marici-make-face-product-naturality
      ( restrict-coarse : MariciFactFace A refines coarse
          → MariciRegionalProduct A Region RegionalFact coarse)
      ( restrict-finer : MariciFactFace A refines finer
          → MariciRegionalProduct A Region RegionalFact finer)
      ( square : (x : MariciFactFace A refines finer)
          → restrict-coarse (face-map x)
            =_{MariciRegionalProduct A Region RegionalFact coarse}
              regional-map (restrict-finer x))
```

## Boundary

This checked target is an interface, not yet `Fact_n`.  The next module must
construct finite cyclic polygons, diagonals, noncrossing dissections, and the
four refinement laws.  Only then can the Rezk nerve and Segal proof be claimed.
