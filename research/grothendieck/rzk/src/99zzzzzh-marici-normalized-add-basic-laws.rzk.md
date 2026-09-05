# Basic laws for normalized raw addition

Strict raw commutativity and zero laws transport through the total normalization
function, yielding equality of canonical components without any distributivity
premise.

```rzk
#lang rzk-1
```

```rzk
#define marici-normalized-raw-add
  ( p q : MariciRawFraction)
  : MariciRawFraction
  := marici-normalized-raw-representative
      (marici-raw-fraction-add p q)

#define marici-normalized-raw-add-comm
  ( p q : MariciRawFraction)
  : marici-normalized-raw-add p q
    =_{MariciRawFraction}
    marici-normalized-raw-add q p
  := ap MariciRawFraction MariciRawFraction
      (marici-raw-fraction-add p q)
      (marici-raw-fraction-add q p)
      marici-normalized-raw-representative
      (marici-raw-fraction-add-comm p q)

#define marici-normalized-raw-add-zero-right
  ( p : MariciRawFraction)
  : marici-normalized-raw-add p (marici-raw-zero-at marici-zero)
    =_{MariciRawFraction}
    marici-normalized-raw-representative p
  := ap MariciRawFraction MariciRawFraction
      (marici-raw-fraction-add p (marici-raw-zero-at marici-zero)) p
      marici-normalized-raw-representative
      (marici-raw-fraction-add-zero-right p)

#define marici-normalized-raw-add-zero-left
  ( p : MariciRawFraction)
  : marici-normalized-raw-add (marici-raw-zero-at marici-zero) p
    =_{MariciRawFraction}
    marici-normalized-raw-representative p
  := ap MariciRawFraction MariciRawFraction
      (marici-raw-fraction-add (marici-raw-zero-at marici-zero) p) p
      marici-normalized-raw-representative
      (marici-raw-fraction-add-zero-left p)
```

## Boundary

Normalize-after-raw addition is componentwise commutative and unital, and the
previous module supplies additive inverses. General presentation congruence and
associativity remain downstream of global integer distributivity.
