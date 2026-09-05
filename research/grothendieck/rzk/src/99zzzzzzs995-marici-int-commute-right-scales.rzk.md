# Reordering two right scale factors

Associativity and commutativity allow two successive right multiplication
factors to exchange positions while keeping the scaled integer fixed.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-commute-right-scales
  ( x d e : MariciInt)
  : marici-int-mul (marici-int-mul x d) e
    =_{MariciInt}
    marici-int-mul (marici-int-mul x e) d
  := concat MariciInt
      (marici-int-mul (marici-int-mul x d) e)
      (marici-int-mul x (marici-int-mul d e))
      (marici-int-mul (marici-int-mul x e) d)
      (marici-int-mul-assoc x d e)
      (concat MariciInt
        (marici-int-mul x (marici-int-mul d e))
        (marici-int-mul x (marici-int-mul e d))
        (marici-int-mul (marici-int-mul x e) d)
        (ap MariciInt MariciInt
          (marici-int-mul d e) (marici-int-mul e d)
          (\ scale → marici-int-mul x scale)
          (marici-int-mul-comm d e))
        (rev MariciInt
          (marici-int-mul (marici-int-mul x e) d)
          (marici-int-mul x (marici-int-mul e d))
          (marici-int-mul-assoc x e d)))
```

## Boundary

Successive right scales can now be reordered. The three-denominator numerator
identity still requires applying this path to each expanded endpoint and then
using positive-difference cancellation.
