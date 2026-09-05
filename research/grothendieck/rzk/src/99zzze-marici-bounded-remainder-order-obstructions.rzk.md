# Order obstructions for bounded remainders

A successor cannot lie at most at its predecessor. Conversely, every product
by a structurally positive multiplier lies at least at its multiplicand. These
two facts supply the contradiction when a bounded nonzero remainder is forced
to contain a full divisor.

```rzk
#lang rzk-1
```

```rzk
#define marici-successor-not-at-most-predecessor
  ( d : MariciNat)
  : MariciNatAtMost (marici-succ d) d → MariciEmpty
  := ind-MariciNat
      (\ d-prime →
        MariciNatAtMost (marici-succ d-prime) d-prime → MariciEmpty)
      (\ bounded →
        match bounded
        ( marici-nat-at-most-witness gap equation ⇒
          marici-succ-not-zero
            (marici-add gap marici-zero)
            (concat MariciNat
              (marici-succ (marici-add gap marici-zero))
              (marici-add gap (marici-succ marici-zero))
              marici-zero
              (rev MariciNat
                (marici-add gap (marici-succ marici-zero))
                (marici-succ (marici-add gap marici-zero))
                (marici-add-succ-right gap marici-zero))
              equation)))
      (\ k ih bounded →
        match bounded
        ( marici-nat-at-most-witness gap equation ⇒
          ih (marici-nat-at-most-witness
            (marici-succ k) k gap
            (marici-succ-injective
              (marici-add gap (marici-succ k)) k
              (concat MariciNat
                (marici-succ (marici-add gap (marici-succ k)))
                (marici-add gap (marici-succ (marici-succ k)))
                (marici-succ k)
                (rev MariciNat
                  (marici-add gap (marici-succ (marici-succ k)))
                  (marici-succ (marici-add gap (marici-succ k)))
                  (marici-add-succ-right gap (marici-succ k)))
                equation)))))
      d

#define marici-positive-multiple-at-least-factor
  ( multiplier-predecessor factor : MariciNat)
  : MariciNatAtMost factor
      (marici-mul (marici-succ multiplier-predecessor) factor)
  := marici-nat-at-most-witness factor
      (marici-mul (marici-succ multiplier-predecessor) factor)
      (marici-mul multiplier-predecessor factor)
      (concat MariciNat
        (marici-add (marici-mul multiplier-predecessor factor) factor)
        (marici-add factor (marici-mul multiplier-predecessor factor))
        (marici-mul (marici-succ multiplier-predecessor) factor)
        (marici-add-comm
          (marici-mul multiplier-predecessor factor) factor)
        refl)

#define marici-at-most-transitive-general
  ( a b c : MariciNat)
  ( a-at-most-b : MariciNatAtMost a b)
  ( b-at-most-c : MariciNatAtMost b c)
  : MariciNatAtMost a c
  := match a-at-most-b
      ( marici-nat-at-most-witness first-gap first-equation ⇒
        match b-at-most-c
        ( marici-nat-at-most-witness second-gap second-equation ⇒
          marici-nat-at-most-witness a c
            (marici-add second-gap first-gap)
            (concat MariciNat
              (marici-add (marici-add second-gap first-gap) a)
              (marici-add second-gap (marici-add first-gap a))
              c
              (marici-add-assoc second-gap first-gap a)
              (concat MariciNat
                (marici-add second-gap (marici-add first-gap a))
                (marici-add second-gap b)
                c
                (ap MariciNat MariciNat
                  (marici-add first-gap a) b
                  (\ value → marici-add second-gap value)
                  first-equation)
                second-equation))))

#define marici-at-most-reindex-upper-general
  ( lower upper upper-prime : MariciNat)
  ( path : upper =_{MariciNat} upper-prime)
  ( bounded : MariciNatAtMost lower upper)
  : MariciNatAtMost lower upper-prime
  := match bounded
      ( marici-nat-at-most-witness gap equation ⇒
        marici-nat-at-most-witness lower upper-prime gap
          (concat MariciNat
            (marici-add gap lower) upper upper-prime equation path))

#define marici-full-positive-divisor-not-bounded-remainder
  ( d multiplier-predecessor remainder : MariciNat)
  ( product-equation : marici-mul
      (marici-succ multiplier-predecessor) (marici-succ d)
    =_{MariciNat} remainder)
  ( remainder-bounded : MariciNatAtMost remainder d)
  : MariciEmpty
  := marici-successor-not-at-most-predecessor d
      (marici-at-most-transitive-general
        (marici-succ d) remainder d
        (marici-at-most-reindex-upper-general
          (marici-succ d)
          (marici-mul (marici-succ multiplier-predecessor)
            (marici-succ d))
          remainder product-equation
          (marici-positive-multiple-at-least-factor
            multiplier-predecessor (marici-succ d)))
        remainder-bounded)
```

## Boundary

A bounded remainder cannot equal a positive multiple of the full divisor. The
remaining division-uniqueness proof must compare the quotient in a division
state with the quotient in a divisibility witness and reduce unequal quotient
branches to this obstruction.
