# Explicit classification of the mixed middle and third magnitudes

Natural gap trichotomy is reoriented into the exact predecessor presentations
used by the mixed associativity theorems.

```rzk
#lang rzk-1
```

```rzk
#data MariciMixedMiddleThirdClassification
  ( middle third : MariciNat)
  := marici-mixed-middle-dominates
      ( residual : MariciNat)
      ( equation : middle =_{MariciNat}
        marici-add (marici-succ third) residual)
  | marici-mixed-middle-equals
      ( equation : middle =_{MariciNat} third)
  | marici-mixed-third-dominates
      ( residual : MariciNat)
      ( equation : third =_{MariciNat}
        marici-add (marici-succ middle) residual)

#define marici-classify-mixed-middle-third
  ( middle third : MariciNat)
  : MariciMixedMiddleThirdClassification middle third
  := match (marici-nat-gap-trichotomy middle third) into
      (\ comparison → MariciMixedMiddleThirdClassification middle third)
      ( marici-nat-gap-less residual equation ⇒
          marici-mixed-third-dominates middle third residual
            (concat MariciNat
              third
              (marici-add (marici-succ residual) middle)
              (marici-add (marici-succ middle) residual)
              (rev MariciNat
                (marici-add (marici-succ residual) middle)
                third equation)
              (marici-successor-add-swap residual middle))
      | marici-nat-gap-equal equation ⇒
          marici-mixed-middle-equals middle third equation
      | marici-nat-gap-greater residual equation ⇒
          marici-mixed-middle-dominates middle third residual
            (concat MariciNat
              middle
              (marici-add (marici-succ residual) third)
              (marici-add (marici-succ third) residual)
              (rev MariciNat
                (marici-add (marici-succ residual) third)
                middle equation)
              (marici-successor-add-swap residual third)))
```

## Boundary

Every positive-middle/negative-third predecessor pair now lands in exactly the
parameter shape consumed by the dominant-middle theorem, equal cancellation,
or the nested residual comparison. The next outer associativity proof can
match this classification without reconstructing additive gaps from ordering
tags.
