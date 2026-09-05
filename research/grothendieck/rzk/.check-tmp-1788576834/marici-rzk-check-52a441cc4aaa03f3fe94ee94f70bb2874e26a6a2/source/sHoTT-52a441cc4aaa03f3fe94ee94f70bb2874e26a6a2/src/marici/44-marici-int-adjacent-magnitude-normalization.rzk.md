# Adjacent opposite-sign magnitude normalization

The comparison normalizer is checked on an unbounded adjacent-magnitude family.
Cancelling equal prefixes leaves exactly positive or negative one according to
which magnitude is larger.

```rzk
#lang rzk-1
```

```rzk
#define marici-compare-successor-self
  ( n : MariciNat)
  : marici-compare (marici-succ n) n
    =_{MariciOrdering} marici-greater
  := match n
      ( marici-zero ⇒ refl
      | marici-succ k ih ⇒ ih)

#define marici-compare-self-successor
  ( n : MariciNat)
  : marici-compare n (marici-succ n)
    =_{MariciOrdering} marici-less
  := match n
      ( marici-zero ⇒ refl
      | marici-succ k ih ⇒ ih)
```

```rzk
#define marici-int-add-adjacent-positive-negative
  ( n : MariciNat)
  : marici-int-add
      (marici-int-embed-nat (marici-succ (marici-succ n)))
      (marici-int-negate
        (marici-int-embed-nat (marici-succ n)))
    =_{MariciInt} marici-int-one
  := match n
      ( marici-zero ⇒ refl
      | marici-succ k ih ⇒ ih)

#define marici-int-add-adjacent-negative-positive
  ( n : MariciNat)
  : marici-int-add
      (marici-int-negate
        (marici-int-embed-nat (marici-succ (marici-succ n))))
      (marici-int-embed-nat (marici-succ n))
    =_{MariciInt} marici-int-minus-one
  := match n
      ( marici-zero ⇒ refl
      | marici-succ k ih ⇒ ih)
```

## Boundary

These are unbounded adjacent-magnitude normalization theorems. They establish a
first unequal opposite-sign comparison family, but do not yet prove
multiplication distributes across that normalized difference or cover larger
magnitude gaps.
