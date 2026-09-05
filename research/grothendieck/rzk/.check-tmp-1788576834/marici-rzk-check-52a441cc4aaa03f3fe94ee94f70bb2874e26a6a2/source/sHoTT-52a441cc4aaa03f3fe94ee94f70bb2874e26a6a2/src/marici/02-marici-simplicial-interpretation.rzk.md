# Marici simplicial interpretation maps

This file supplies the first comparison-side structure: any map between Segal
types acts pointwise on directed arrows and two-simplex witnesses, and the
target Segal uniqueness theorem forces preservation of canonical composition.
No additive interpretation is asserted.

```rzk
#lang rzk-1
```

```rzk
#def marici-map-arrow
  ( A B : U)
  ( F : A → B)
  ( x y : A)
  ( f : hom A x y)
  : hom B (F x) (F y)
  := \ t → F (f t)

#def marici-map-triangle
  ( A B : U)
  ( F : A → B)
  ( x y z : A)
  ( f : hom A x y)
  ( g : hom A y z)
  ( h : hom A x z)
  ( alpha : hom2 A x y z f g h)
  : hom2 B (F x) (F y) (F z)
      (marici-map-arrow A B F x y f)
      (marici-map-arrow A B F y z g)
      (marici-map-arrow A B F x z h)
  := \ (t , s) → F (alpha (t , s))
```

The direction of the equality below is deliberate: target composition is
identified with the image of source composition by applying target uniqueness
to the mapped source filler.

```rzk
#def marici-map-preserves-composite
  ( A B : U)
  ( is-segal-A : is-segal A)
  ( is-segal-B : is-segal B)
  ( F : A → B)
  ( x y z : A)
  ( f : hom A x y)
  ( g : hom A y z)
  : ( comp-is-segal B is-segal-B (F x) (F y) (F z)
        (marici-map-arrow A B F x y f)
        (marici-map-arrow A B F y z g))
  = ( marici-map-arrow A B F x z
        (comp-is-segal A is-segal-A x y z f g))
  := uniqueness-comp-is-segal
      B is-segal-B (F x) (F y) (F z)
      (marici-map-arrow A B F x y f)
      (marici-map-arrow A B F y z g)
      (marici-map-arrow A B F x z
        (comp-is-segal A is-segal-A x y z f g))
      (marici-map-triangle A B F x y z f g
        (comp-is-segal A is-segal-A x y z f g)
        (witness-comp-is-segal A is-segal-A x y z f g))
```

## Boundary

This theorem constructs the categorical preservation cell needed before any
comparison with the Cubical Agda additive boundary maps. The missing object is
a target Segal/Rezk presentation of the additive model together with a map `F`
whose action on generators is source-derived. Nothing here identifies an Rzk
hom with an abelian-group element.
