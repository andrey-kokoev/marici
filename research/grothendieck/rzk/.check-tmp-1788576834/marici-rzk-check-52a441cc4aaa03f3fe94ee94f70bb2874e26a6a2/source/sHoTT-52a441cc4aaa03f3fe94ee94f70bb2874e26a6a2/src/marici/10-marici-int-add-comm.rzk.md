# Marici canonical-integer addition commutativity

Mixed-sign addition is defined through one canonical positive-plus-negative
normalizer. Negative-plus-positive delegates to that normalizer with exchanged
magnitudes. This makes mixed-sign commutativity definitional rather than a
second comparison theorem.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-add-comm
  ( x y : MariciInt)
  : marici-int-add x y =_{MariciInt} marici-int-add y x
  := match x
      ( marici-int-zero ⇒
          rev MariciInt
            (marici-int-add y marici-int-zero) y
            (marici-int-add-zero-right y)
      | marici-int-pos a ⇒
          match y
            ( marici-int-zero ⇒ refl
            | marici-int-pos b ⇒
                ap MariciNat MariciInt
                  (marici-add a b) (marici-add b a)
                  (\ q → marici-int-pos (marici-succ q))
                  (marici-add-comm a b)
            | marici-int-neg b ⇒ refl)
      | marici-int-neg a ⇒
          match y
            ( marici-int-zero ⇒ refl
            | marici-int-pos b ⇒ refl
            | marici-int-neg b ⇒
                ap MariciNat MariciInt
                  (marici-add a b) (marici-add b a)
                  (\ q → marici-int-neg (marici-succ q))
                  (marici-add-comm a b)))
```

## Boundary

This theorem depends on the canonical mixed-sign normalizer introduced in
module 07. It proves commutativity only. Associativity still requires explicit
compatibility lemmas for comparison, truncated subtraction, and nested
normalization; finite constructor tests cannot replace those lemmas.
