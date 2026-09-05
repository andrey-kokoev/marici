# Conditional real-axis embedding into the complex carrier

Every conditional completed real determines a complex value with zero imaginary
part. Projection of an equality between such values recovers equality of the
real inputs, so the embedding is injective without requiring complex arithmetic.

```rzk
#lang rzk-1
```

```rzk
#define marici-real-to-complex
  ( real : MariciReal)
  : MariciComplex
  := marici-complex real marici-real-zero

#define marici-real-to-complex-real-part
  ( real : MariciReal)
  : marici-complex-real-part (marici-real-to-complex real)
    =_{MariciReal}
    real
  := refl

#define marici-real-to-complex-imaginary-part
  ( real : MariciReal)
  : marici-complex-imaginary-part (marici-real-to-complex real)
    =_{MariciReal}
    marici-real-zero
  := refl

#define marici-real-to-complex-injective
  ( left-real right-real : MariciReal)
  ( path : marici-real-to-complex left-real
    =_{MariciComplex}
    marici-real-to-complex right-real)
  : left-real =_{MariciReal} right-real
  := ap MariciComplex MariciReal
      (marici-real-to-complex left-real)
      (marici-real-to-complex right-real)
      marici-complex-real-part
      path

#define marici-zeta-two-complex-is-real-axis-embedding
  : marici-zeta-two-complex
    =_{MariciComplex}
    marici-real-to-complex marici-zeta-two-real
  := refl
```

## Boundary

The real-axis embedding is now defined and proved injective for the conditional
carriers. It supplies no complex addition, multiplication, exponentiation, norm,
or analytic structure; those require descended operations on `MariciReal` and
separate coherence proofs.
