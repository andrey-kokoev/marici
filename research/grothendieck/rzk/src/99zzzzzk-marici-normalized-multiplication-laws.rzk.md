# Canonical laws for normalize-after-raw multiplication

Strict raw multiplication commutativity and associativity transport through
total normalization. Thus a finite raw Euler-factor product has canonical
components independent of factor order and parenthesization before any
intermediate normalization is inserted.

```rzk
#lang rzk-1
```

```rzk
#define marici-normalized-raw-mul-comm
  ( p q : MariciRawFraction)
  : marici-normalized-raw-multiplication p q
    =_{MariciRawFraction}
    marici-normalized-raw-multiplication q p
  := ap MariciRawFraction MariciRawFraction
      (marici-raw-fraction-mul p q)
      (marici-raw-fraction-mul q p)
      marici-normalized-raw-representative
      (marici-raw-fraction-mul-comm p q)

#define marici-normalized-raw-mul-assoc
  ( p q r : MariciRawFraction)
  : marici-normalized-raw-representative
      (marici-raw-fraction-mul (marici-raw-fraction-mul p q) r)
      =_{MariciRawFraction}
    marici-normalized-raw-representative
      (marici-raw-fraction-mul p (marici-raw-fraction-mul q r))
  := ap MariciRawFraction MariciRawFraction
      (marici-raw-fraction-mul (marici-raw-fraction-mul p q) r)
      (marici-raw-fraction-mul p (marici-raw-fraction-mul q r))
      marici-normalized-raw-representative
      (marici-raw-fraction-mul-assoc p q r)
```

## Boundary

Normalize-once finite multiplication is componentwise commutative and
associative, and iteration 28 proved presentation descent. This is sufficient
to compare finite raw Euler-factor products after one final normalization.
Associativity of the carrier operation that normalizes after every binary step
is a separate theorem requiring canonicality transports between intermediate
normal forms.
