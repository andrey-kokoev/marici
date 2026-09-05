# Integer addition associativity on the zero faces

Each face of the ternary associativity cube containing zero reduces by the
checked left and right unit paths. These faces remove all zero branches from a
future constructor census of global integer addition associativity.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-add-assoc-right-zero
  ( x y : MariciInt)
  : marici-int-add (marici-int-add x y) marici-int-zero
    =_{MariciInt}
    marici-int-add x (marici-int-add y marici-int-zero)
  := concat MariciInt
      (marici-int-add (marici-int-add x y) marici-int-zero)
      (marici-int-add x y)
      (marici-int-add x (marici-int-add y marici-int-zero))
      (marici-int-add-zero-right (marici-int-add x y))
      (ap MariciInt MariciInt
        y (marici-int-add y marici-int-zero)
        (\ value → marici-int-add x value)
        (rev MariciInt
          (marici-int-add y marici-int-zero) y
          (marici-int-add-zero-right y)))

#define marici-int-add-assoc-middle-zero
  ( x z : MariciInt)
  : marici-int-add (marici-int-add x marici-int-zero) z
    =_{MariciInt}
    marici-int-add x (marici-int-add marici-int-zero z)
  := concat MariciInt
      (marici-int-add (marici-int-add x marici-int-zero) z)
      (marici-int-add x z)
      (marici-int-add x (marici-int-add marici-int-zero z))
      (ap MariciInt MariciInt
        (marici-int-add x marici-int-zero) x
        (\ value → marici-int-add value z)
        (marici-int-add-zero-right x))
      (ap MariciInt MariciInt
        z (marici-int-add marici-int-zero z)
        (\ value → marici-int-add x value)
        (rev MariciInt
          (marici-int-add marici-int-zero z) z
          (marici-int-add-zero-left z)))

#define marici-int-add-assoc-left-zero
  ( y z : MariciInt)
  : marici-int-add (marici-int-add marici-int-zero y) z
    =_{MariciInt}
    marici-int-add marici-int-zero (marici-int-add y z)
  := concat MariciInt
      (marici-int-add (marici-int-add marici-int-zero y) z)
      (marici-int-add y z)
      (marici-int-add marici-int-zero (marici-int-add y z))
      (ap MariciInt MariciInt
        (marici-int-add marici-int-zero y) y
        (\ value → marici-int-add value z)
        (marici-int-add-zero-left y))
      (rev MariciInt
        (marici-int-add marici-int-zero (marici-int-add y z))
        (marici-int-add y z)
        (marici-int-add-zero-left (marici-int-add y z)))
```

## Boundary

All ternary addition branches containing zero are checked. The remaining
associativity census contains only positive and negative constructors; its
same-sign faces are already covered by the embedded-natural and
negated-embedded-natural theorems, leaving genuinely mixed-sign nonzero faces.
