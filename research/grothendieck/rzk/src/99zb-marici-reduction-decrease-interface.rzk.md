# A typed decrease interface for fraction reduction

Strict decrease is represented by a positive additive gap. A recursive
reduction step must carry both a nonunit common-factor witness and evidence that
its extracted denominator predecessor is strictly smaller than the source.

```rzk
#lang rzk-1
```

```rzk
#data MariciNatStrictlyLess
  ( smaller larger : MariciNat)
  := marici-nat-strictly-less-witness
      ( gap-predecessor : MariciNat)
      ( equation : marici-add (marici-succ gap-predecessor) smaller
        =_{MariciNat} larger)

#define marici-nat-strictly-less-successor
  ( n : MariciNat)
  : MariciNatStrictlyLess n (marici-succ n)
  := marici-nat-strictly-less-witness n (marici-succ n) marici-zero refl

#data MariciRawComponentsDecreasingReduction
  ( numerator : MariciInt)
  ( denominator-predecessor : MariciNat)
  := marici-raw-components-decreasing-reduction
      ( nonunit-predecessor : MariciNat)
      ( numerator-cofactor : MariciInt)
      ( denominator-cofactor-predecessor : MariciNat)
      ( numerator-equation : marici-int-mul numerator-cofactor
          (marici-int-positive-denominator
            (marici-succ nonunit-predecessor))
        =_{MariciInt} numerator)
      ( denominator-equation : marici-mul
          (marici-succ denominator-cofactor-predecessor)
          (marici-succ (marici-succ nonunit-predecessor))
        =_{MariciNat} marici-succ denominator-predecessor)
      ( decrease : MariciNatStrictlyLess
          denominator-cofactor-predecessor denominator-predecessor)
```

## Boundary

The termination evidence required at each recursive step is now explicit and
uses the denominator predecessor as its measure. The general theorem deriving
this decrease from every nonunit denominator factor equation remains open, as
does a well-founded recursion principle consuming these steps.
