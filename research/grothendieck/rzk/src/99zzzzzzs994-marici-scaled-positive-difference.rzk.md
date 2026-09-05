# Positive-oriented differences distribute through scaling

Right multiplication distributes over a difference written as `x + (-y)`, and
multiplication commutes with negation in the subtracted term.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-positive-difference-scale-right
  ( x y d : MariciInt)
  : marici-int-mul
      (marici-int-add x (marici-int-negate y)) d
    =_{MariciInt}
    marici-int-add
      (marici-int-mul x d)
      (marici-int-negate (marici-int-mul y d))
  := concat MariciInt
      (marici-int-mul
        (marici-int-add x (marici-int-negate y)) d)
      (marici-int-add
        (marici-int-mul x d)
        (marici-int-mul (marici-int-negate y) d))
      (marici-int-add
        (marici-int-mul x d)
        (marici-int-negate (marici-int-mul y d)))
      (marici-int-mul-add-right-distrib x (marici-int-negate y) d)
      (ap MariciInt MariciInt
        (marici-int-mul (marici-int-negate y) d)
        (marici-int-negate (marici-int-mul y d))
        (\ subtracted → marici-int-add
          (marici-int-mul x d) subtracted)
        (marici-int-mul-negate-left y d))
```

## Boundary

Scaled positive-oriented differences now expand into scaled endpoints. The
three-denominator triangle identity additionally requires reassociating and
commuting the positive scale factors.
