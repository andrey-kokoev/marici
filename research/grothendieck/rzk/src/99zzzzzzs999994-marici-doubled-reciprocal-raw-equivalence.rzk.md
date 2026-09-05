# Two tightened reciprocal numerators equal one target reciprocal

Cross multiplication reduces the comparison to the doubled-denominator
identity: two copies of `k+1` equal the denominator represented by the tightened
index `2k+1`.

```rzk
#lang rzk-1
```

```rzk
#define marici-doubled-reciprocal-raw-equivalent
  ( k : MariciNat)
  : marici-raw-fraction-equivalent
      (marici-raw-fraction
        (marici-int-add marici-int-one marici-int-one)
        (marici-double-tolerance-index k))
      (marici-raw-reciprocal-tolerance k)
  := concat MariciInt
      (marici-int-mul
        (marici-int-add marici-int-one marici-int-one)
        (marici-int-positive-denominator k))
      (marici-int-add
        (marici-int-positive-denominator k)
        (marici-int-positive-denominator k))
      (marici-int-mul marici-int-one
        (marici-int-positive-denominator
          (marici-double-tolerance-index k)))
      (concat MariciInt
        (marici-int-mul
          (marici-int-add marici-int-one marici-int-one)
          (marici-int-positive-denominator k))
        (marici-int-add
          (marici-int-mul marici-int-one
            (marici-int-positive-denominator k))
          (marici-int-mul marici-int-one
            (marici-int-positive-denominator k)))
        (marici-int-add
          (marici-int-positive-denominator k)
          (marici-int-positive-denominator k))
        (marici-int-mul-add-right-distrib
          marici-int-one marici-int-one
          (marici-int-positive-denominator k))
        (marici-int-add-congruent
          (marici-int-mul marici-int-one
            (marici-int-positive-denominator k))
          (marici-int-positive-denominator k)
          (marici-int-mul marici-int-one
            (marici-int-positive-denominator k))
          (marici-int-positive-denominator k)
          (marici-int-mul-one-left
            (marici-int-positive-denominator k))
          (marici-int-mul-one-left
            (marici-int-positive-denominator k))))
      (concat MariciInt
        (marici-int-add
          (marici-int-positive-denominator k)
          (marici-int-positive-denominator k))
        (marici-int-positive-denominator
          (marici-double-tolerance-index k))
        (marici-int-mul marici-int-one
          (marici-int-positive-denominator
            (marici-double-tolerance-index k)))
        (concat MariciInt
          (marici-int-add
            (marici-int-embed-nat (marici-succ k))
            (marici-int-embed-nat (marici-succ k)))
          (marici-int-embed-nat
            (marici-add (marici-succ k) (marici-succ k)))
          (marici-int-embed-nat
            (marici-succ (marici-double-tolerance-index k)))
          (rev MariciInt
            (marici-int-embed-nat
              (marici-add (marici-succ k) (marici-succ k)))
            (marici-int-add
              (marici-int-embed-nat (marici-succ k))
              (marici-int-embed-nat (marici-succ k)))
            (marici-int-embed-add (marici-succ k) (marici-succ k)))
          (ap MariciNat MariciInt
            (marici-add (marici-succ k) (marici-succ k))
            (marici-succ (marici-double-tolerance-index k))
            marici-int-embed-nat
            (rev MariciNat
              (marici-succ (marici-double-tolerance-index k))
              (marici-add (marici-succ k) (marici-succ k))
              (marici-double-tolerance-denominator k))))
        (rev MariciInt
          (marici-int-mul marici-int-one
            (marici-int-positive-denominator
              (marici-double-tolerance-index k)))
          (marici-int-positive-denominator
            (marici-double-tolerance-index k))
          (marici-int-mul-one-left
            (marici-int-positive-denominator
              (marici-double-tolerance-index k)))))
```

## Boundary

The contracted numerator-two tightened fraction is now equivalent to the target
reciprocal fraction. Composing this with same-denominator raw addition yields
the full two-tolerance combination equivalence.
