# Both multiplication orientations preserve natural subtraction

Multiplication commutativity transports the right-argument subtraction theorem
to the left-argument orientation.

```rzk
#lang rzk-1
```

```rzk
#define marici-mul-sub-left-distrib
  ( a b n : MariciNat)
  : marici-sub (marici-mul a n) (marici-mul b n)
    =_{MariciNat} marici-mul (marici-sub a b) n
  := concat MariciNat
      (marici-sub (marici-mul a n) (marici-mul b n))
      (marici-sub (marici-mul n a) (marici-mul n b))
      (marici-mul (marici-sub a b) n)
      (concat MariciNat
        (marici-sub (marici-mul a n) (marici-mul b n))
        (marici-sub (marici-mul n a) (marici-mul b n))
        (marici-sub (marici-mul n a) (marici-mul n b))
        (ap MariciNat MariciNat
          (marici-mul a n) (marici-mul n a)
          (\ z → marici-sub z (marici-mul b n))
          (marici-mul-comm a n))
        (ap MariciNat MariciNat
          (marici-mul b n) (marici-mul n b)
          (\ z → marici-sub (marici-mul n a) z)
          (marici-mul-comm b n)))
      (concat MariciNat
        (marici-sub (marici-mul n a) (marici-mul n b))
        (marici-mul n (marici-sub a b))
        (marici-mul (marici-sub a b) n)
        (marici-mul-sub-right-distrib n a b)
        (marici-mul-comm n (marici-sub a b)))
```

## Boundary

Truncated subtraction is preserved by multiplication in both orientations.
This still does not prove that a positive factor reflects comparison or can be
cancelled from an equality.
