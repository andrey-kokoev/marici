# Lifting magnitude divisibility to signed integer divisibility

A natural factorization of a nonzero canonical magnitude determines the signed
integer cofactor by preserving the source sign. Successor injectivity converts
the positive-product magnitude equation to equality of predecessor payloads.

```rzk
#lang rzk-1
```

```rzk
#define marici-positive-product-predecessor-from-magnitude
  ( a q f : MariciNat)
  ( e : marici-mul (marici-succ q) (marici-succ f)
    =_{MariciNat} marici-succ a)
  : marici-positive-product-predecessor q f =_{MariciNat} a
  := marici-succ-injective
      (marici-positive-product-predecessor q f) a
      (concat MariciNat
        (marici-succ (marici-positive-product-predecessor q f))
        (marici-mul (marici-succ q) (marici-succ f))
        (marici-succ a)
        (marici-succ-positive-product q f) e)

#define marici-magnitude-factorization-lifts-to-int
  ( z : MariciInt)
  ( q f : MariciNat)
  ( e : marici-mul (marici-succ q) (marici-succ f)
    =_{MariciNat} marici-int-magnitude z)
  : MariciIntRightPositiveDivides f z
  := (match z into
        (\ z-prime →
          (marici-mul (marici-succ q) (marici-succ f)
            =_{MariciNat} marici-int-magnitude z-prime)
          → MariciIntRightPositiveDivides f z-prime)
      ( marici-int-zero ⇒ \ eq →
          marici-int-zero-right-positive-divides f
      | marici-int-pos a ⇒ \ eq →
          marici-int-right-positive-divides-witness
            f (marici-int-pos a) (marici-int-pos q)
            (ap MariciNat MariciInt
              (marici-positive-product-predecessor q f) a
              marici-int-pos
              (marici-positive-product-predecessor-from-magnitude a q f eq))
      | marici-int-neg a ⇒ \ eq →
          marici-int-right-positive-divides-witness
            f (marici-int-neg a) (marici-int-neg q)
            (ap MariciNat MariciInt
              (marici-positive-product-predecessor q f) a
              marici-int-neg
              (marici-positive-product-predecessor-from-magnitude a q f eq)))) e
```

## Boundary

Every supplied positive natural factorization of an integer magnitude now
lifts to the required signed right-divisibility witness. Constructing such a
factorization decision by bounded natural search remains open.
