# Natural order lifts to positive-denominator integer order

An additive natural gap also separates the corresponding positive
denominators. Successor-right addition and embedding preservation identify the
larger denominator with the smaller denominator plus the embedded nonnegative
gap.

```rzk
#lang rzk-1
```

```rzk
#define marici-positive-denominator-gap-path
  ( smaller larger gap : MariciNat)
  ( equation : marici-add gap smaller =_{MariciNat} larger)
  : marici-int-positive-denominator larger
    =_{MariciInt}
    marici-int-add
      (marici-int-positive-denominator smaller)
      (marici-int-embed-nat gap)
  := concat MariciInt
      (marici-int-positive-denominator larger)
      (marici-int-embed-nat (marici-add gap (marici-succ smaller)))
      (marici-int-add
        (marici-int-positive-denominator smaller)
        (marici-int-embed-nat gap))
      (ap MariciNat MariciInt
        (marici-succ larger)
        (marici-add gap (marici-succ smaller))
        marici-int-embed-nat
        (rev MariciNat
          (marici-add gap (marici-succ smaller))
          (marici-succ larger)
          (concat MariciNat
            (marici-add gap (marici-succ smaller))
            (marici-succ (marici-add gap smaller))
            (marici-succ larger)
            (marici-add-succ-right gap smaller)
            (ap MariciNat MariciNat
              (marici-add gap smaller) larger marici-succ equation))))
      (concat MariciInt
        (marici-int-embed-nat (marici-add gap (marici-succ smaller)))
        (marici-int-add
          (marici-int-embed-nat gap)
          (marici-int-positive-denominator smaller))
        (marici-int-add
          (marici-int-positive-denominator smaller)
          (marici-int-embed-nat gap))
        (marici-int-embed-add gap (marici-succ smaller))
        (marici-int-add-comm
          (marici-int-embed-nat gap)
          (marici-int-positive-denominator smaller)))

#define marici-positive-denominator-at-most-from-natural-at-most
  ( smaller larger : MariciNat)
  ( witness : MariciNatAtMost smaller larger)
  : MariciIntAtMost
      (marici-int-positive-denominator smaller)
      (marici-int-positive-denominator larger)
  := match witness
      ( marici-nat-at-most-witness gap equation ⇒
          marici-int-at-most-transport-right
            (marici-int-positive-denominator smaller)
            (marici-int-add
              (marici-int-positive-denominator smaller)
              (marici-int-embed-nat gap))
            (marici-int-positive-denominator larger)
            (rev MariciInt
              (marici-int-positive-denominator larger)
              (marici-int-add
                (marici-int-positive-denominator smaller)
                (marici-int-embed-nat gap))
              (marici-positive-denominator-gap-path
                smaller larger gap equation))
            (marici-int-at-most-add-nonnegative
              (marici-int-positive-denominator smaller)
              (marici-int-embed-nat gap)
              marici-trivial))
```

## Boundary

Natural cutoff order now lifts to integer denominator order. Cross multiplying
unit numerators reverses this inequality into antitonicity of reciprocal
rational tolerances.
