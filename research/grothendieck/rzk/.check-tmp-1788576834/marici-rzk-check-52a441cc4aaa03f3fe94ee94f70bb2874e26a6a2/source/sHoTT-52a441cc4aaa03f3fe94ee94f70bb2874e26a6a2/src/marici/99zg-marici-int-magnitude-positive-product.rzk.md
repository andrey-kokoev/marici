# Canonical-integer magnitude and positive products

The unsigned magnitude of a canonical integer is zero at zero and the successor
of the stored predecessor in either signed branch. Multiplication by a positive
integer acts on this magnitude by natural multiplication.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-magnitude
  ( z : MariciInt)
  : MariciNat
  := match z
      ( marici-int-zero ⇒ marici-zero
      | marici-int-pos a ⇒ marici-succ a
      | marici-int-neg a ⇒ marici-succ a)

#define marici-int-magnitude-positive-right-product
  ( z : MariciInt)
  ( f : MariciNat)
  : marici-int-magnitude
      (marici-int-mul z (marici-int-positive-denominator f))
    =_{MariciNat}
      marici-mul (marici-int-magnitude z) (marici-succ f)
  := match z
      ( marici-int-zero ⇒ refl
      | marici-int-pos a ⇒
          marici-succ-positive-product a f
      | marici-int-neg a ⇒
          marici-succ-positive-product a f)

#define marici-int-zero-right-positive-divides
  ( f : MariciNat)
  : MariciIntRightPositiveDivides f marici-int-zero
  := marici-int-right-positive-divides-witness
      f marici-int-zero marici-int-zero refl
```

## Boundary

Positive integer divisibility can now be reduced to natural divisibility of the
absolute magnitude, with zero handled uniformly for every positive factor. A
checked conversion from a nonzero magnitude cofactor equation back to a signed
integer cofactor and a total natural divisibility algorithm remain open.
