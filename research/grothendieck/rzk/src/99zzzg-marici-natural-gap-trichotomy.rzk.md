# Natural trichotomy with explicit positive gaps

Quotient comparison must retain more than an ordering tag: each strict branch
needs the exact positive additive gap. Structural double induction constructs
that evidence for every pair of naturals.

```rzk
#lang rzk-1
```

```rzk
#data MariciNatGapTrichotomy
  ( left right : MariciNat)
  := marici-nat-gap-less
      ( gap-predecessor : MariciNat)
      ( equation : marici-add (marici-succ gap-predecessor) left
        =_{MariciNat} right)
  | marici-nat-gap-equal
      ( equation : left =_{MariciNat} right)
  | marici-nat-gap-greater
      ( gap-predecessor : MariciNat)
      ( equation : marici-add (marici-succ gap-predecessor) right
        =_{MariciNat} left)

#define marici-nat-gap-trichotomy
  ( left right : MariciNat)
  : MariciNatGapTrichotomy left right
  := (match left into
      (\ left-prime →
        (right-prime : MariciNat) →
        MariciNatGapTrichotomy left-prime right-prime)
      ( marici-zero ⇒ \ right-prime →
          match right-prime into
          (\ right-double-prime →
            MariciNatGapTrichotomy marici-zero right-double-prime)
          ( marici-zero ⇒ marici-nat-gap-equal
              marici-zero marici-zero refl
          | marici-succ k ih ⇒ marici-nat-gap-less
              marici-zero (marici-succ k) k
              (marici-add-zero-right (marici-succ k)))
      | marici-succ l ih ⇒ \ right-prime →
          match right-prime into
          (\ right-double-prime →
            MariciNatGapTrichotomy (marici-succ l) right-double-prime)
          ( marici-zero ⇒ marici-nat-gap-greater
              (marici-succ l) marici-zero l
              (marici-add-zero-right (marici-succ l))
          | marici-succ r right-ih ⇒
              match (ih r) into
              (\ comparison →
                MariciNatGapTrichotomy (marici-succ l) (marici-succ r))
              ( marici-nat-gap-less gap equation ⇒
                  marici-nat-gap-less
                    (marici-succ l) (marici-succ r) gap
                    (concat MariciNat
                      (marici-add (marici-succ gap) (marici-succ l))
                      (marici-succ
                        (marici-add (marici-succ gap) l))
                      (marici-succ r)
                      (marici-add-succ-right (marici-succ gap) l)
                      (ap MariciNat MariciNat
                        (marici-add (marici-succ gap) l) r
                        marici-succ equation))
              | marici-nat-gap-equal equation ⇒
                  marici-nat-gap-equal
                    (marici-succ l) (marici-succ r)
                    (ap MariciNat MariciNat l r marici-succ equation)
              | marici-nat-gap-greater gap equation ⇒
                  marici-nat-gap-greater
                    (marici-succ l) (marici-succ r) gap
                    (concat MariciNat
                      (marici-add (marici-succ gap) (marici-succ r))
                      (marici-succ
                        (marici-add (marici-succ gap) r))
                      (marici-succ l)
                      (marici-add-succ-right (marici-succ gap) r)
                      (ap MariciNat MariciNat
                        (marici-add (marici-succ gap) r) l
                        marici-succ equation))))))
      right
```

## Boundary

Every quotient pair now splits into equality or one of two strict branches with
an exact positive additive gap. Rewriting product reconstructions along these
gaps is the remaining step before applying the bounded-remainder obstruction.
