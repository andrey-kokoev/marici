# Functoriality of the Marici simplicial interpretation

This file connects ordinary map identity/composition from the arithmetic map
layer to pointwise action on directed simplices. The equalities compute because
both routes apply the same maps to the same simplex coordinates.

```rzk
#lang rzk-1
```

```rzk
#define marici-map-arrow-id
  ( A : U)
  ( x y : A)
  ( f : hom A x y)
  : marici-map-arrow A A (marici-id-map A) x y f
    =_{hom A x y} f
  := refl

#define marici-map-arrow-compose
  ( A B C : U)
  ( F : A → B)
  ( G : B → C)
  ( x y : A)
  ( f : hom A x y)
  : marici-map-arrow A C (marici-compose-map A B C F G) x y f
    =_{hom C (G (F x)) (G (F y))}
      marici-map-arrow B C G (F x) (F y)
        (marici-map-arrow A B F x y f)
  := refl
```

The same identity and composition laws hold for retained two-simplex fillers,
not only their diagonal arrows.

```rzk
#define marici-map-triangle-id
  ( A : U)
  ( x y z : A)
  ( f : hom A x y)
  ( g : hom A y z)
  ( h : hom A x z)
  ( alpha : hom2 A x y z f g h)
  : marici-map-triangle A A (marici-id-map A)
      x y z f g h alpha
    =_{hom2 A x y z f g h} alpha
  := refl

#define marici-map-triangle-compose
  ( A B C : U)
  ( F : A → B)
  ( G : B → C)
  ( x y z : A)
  ( f : hom A x y)
  ( g : hom A y z)
  ( h : hom A x z)
  ( alpha : hom2 A x y z f g h)
  : marici-map-triangle A C (marici-compose-map A B C F G)
      x y z f g h alpha
    =_{hom2 C (G (F x)) (G (F y)) (G (F z))
        (marici-map-arrow B C G (F x) (F y)
          (marici-map-arrow A B F x y f))
        (marici-map-arrow B C G (F y) (F z)
          (marici-map-arrow A B F y z g))
        (marici-map-arrow B C G (F x) (F z)
          (marici-map-arrow A B F x z h))}
      marici-map-triangle B C G
        (F x) (F y) (F z)
        (marici-map-arrow A B F x y f)
        (marici-map-arrow A B F y z g)
        (marici-map-arrow A B F x z h)
        (marici-map-triangle A B F x y z f g h alpha)
  := refl
```

## Boundary

The pointwise simplicial action is now functorial under the same map identity
and composition used by the arithmetic interpretation layer. This does not
supply a simplicial realization of `MariciNat` or `MariciInt`; that requires
sethood/discreteness or another explicit Segal target construction.
