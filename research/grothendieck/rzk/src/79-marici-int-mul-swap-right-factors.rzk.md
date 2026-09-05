# Swapping two right multiplication factors

Associativity and commutativity exchange the last two factors of an integer
triple product. This is the coherence path needed to align the common positive
denominator in raw-fraction transitivity.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-mul-swap-right-factors
  ( x y z : MariciInt)
  : marici-int-mul (marici-int-mul x y) z
    =_{MariciInt} marici-int-mul (marici-int-mul x z) y
  := concat MariciInt
      (marici-int-mul (marici-int-mul x y) z)
      (marici-int-mul x (marici-int-mul y z))
      (marici-int-mul (marici-int-mul x z) y)
      (marici-int-mul-assoc x y z)
      (concat MariciInt
        (marici-int-mul x (marici-int-mul y z))
        (marici-int-mul x (marici-int-mul z y))
        (marici-int-mul (marici-int-mul x z) y)
        (ap MariciInt MariciInt
          (marici-int-mul y z) (marici-int-mul z y)
          (\ q → marici-int-mul x q)
          (marici-int-mul-comm y z))
        (rev MariciInt
          (marici-int-mul (marici-int-mul x z) y)
          (marici-int-mul x (marici-int-mul z y))
          (marici-int-mul-assoc x z y)))
```

## Boundary

This theorem only reorders an already-associated triple product. It does not
cancel any factor. Module 78 supplies cancellation once a transitivity chain
has been aligned to a common positive denominator.
