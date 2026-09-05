# Positive natural scaling preserves comparison

Multiplication by a successor factor preserves the three-way natural
comparison. The proof uses simultaneous structural reduction and common-prefix
invariance; no order structure is assumed.

```rzk
#lang rzk-1
```

```rzk
#define marici-compare-positive-scale
  ( p a b : MariciNat)
  : marici-compare
      (marici-mul (marici-succ p) a)
      (marici-mul (marici-succ p) b)
    =_{MariciOrdering} marici-compare a b
  := (match a into
        (\ a-prime → (b-prime : MariciNat) →
          marici-compare
            (marici-mul (marici-succ p) a-prime)
            (marici-mul (marici-succ p) b-prime)
          =_{MariciOrdering} marici-compare a-prime b-prime)
      ( marici-zero ⇒ \ q → match q
          ( marici-zero ⇒
              marici-compare-self
                (marici-mul (marici-succ p) marici-zero)
          | marici-succ j jh ⇒
              ap MariciNat MariciOrdering
                (marici-mul (marici-succ p) marici-zero)
                marici-zero
                (\ z → marici-compare z
                  (marici-mul (marici-succ p) (marici-succ j)))
                (marici-mul-zero-right (marici-succ p)))
      | marici-succ i ih ⇒ \ q → match q
          ( marici-zero ⇒
              ap MariciNat MariciOrdering
                (marici-mul (marici-succ p) marici-zero)
                marici-zero
                (\ z → marici-compare
                  (marici-mul (marici-succ p) (marici-succ i)) z)
                (marici-mul-zero-right (marici-succ p))
          | marici-succ j jh ⇒ concat MariciOrdering
              (marici-compare
                (marici-mul (marici-succ p) (marici-succ i))
                (marici-mul (marici-succ p) (marici-succ j)))
              (marici-compare
                (marici-add p
                  (marici-mul (marici-succ p) i))
                (marici-add p
                  (marici-mul (marici-succ p) j)))
              (marici-compare i j)
              (concat MariciOrdering
                (marici-compare
                  (marici-mul (marici-succ p) (marici-succ i))
                  (marici-mul (marici-succ p) (marici-succ j)))
                (marici-compare
                  (marici-succ
                    (marici-add p
                      (marici-mul (marici-succ p) i)))
                  (marici-succ
                    (marici-add p
                      (marici-mul (marici-succ p) j))))
                (marici-compare
                  (marici-add p
                    (marici-mul (marici-succ p) i))
                  (marici-add p
                    (marici-mul (marici-succ p) j)))
                (concat MariciOrdering
                  (marici-compare
                    (marici-mul (marici-succ p) (marici-succ i))
                    (marici-mul (marici-succ p) (marici-succ j)))
                  (marici-compare
                    (marici-succ
                      (marici-add p
                        (marici-mul (marici-succ p) i)))
                    (marici-mul (marici-succ p) (marici-succ j)))
                  (marici-compare
                    (marici-succ
                      (marici-add p
                        (marici-mul (marici-succ p) i)))
                    (marici-succ
                      (marici-add p
                        (marici-mul (marici-succ p) j))))
                  (ap MariciNat MariciOrdering
                    (marici-mul (marici-succ p) (marici-succ i))
                    (marici-add (marici-succ p)
                      (marici-mul (marici-succ p) i))
                    (\ z → marici-compare z
                      (marici-mul (marici-succ p) (marici-succ j)))
                    (marici-mul-succ-right (marici-succ p) i))
                  (ap MariciNat MariciOrdering
                    (marici-mul (marici-succ p) (marici-succ j))
                    (marici-add (marici-succ p)
                      (marici-mul (marici-succ p) j))
                    (\ z → marici-compare
                      (marici-succ
                        (marici-add p
                          (marici-mul (marici-succ p) i))) z)
                    (marici-mul-succ-right (marici-succ p) j)))
                refl)
              (concat MariciOrdering
                (marici-compare
                  (marici-add p
                    (marici-mul (marici-succ p) i))
                  (marici-add p
                    (marici-mul (marici-succ p) j)))
                (marici-compare
                  (marici-mul (marici-succ p) i)
                  (marici-mul (marici-succ p) j))
                (marici-compare i j)
                (marici-compare-common-prefix p
                  (marici-mul (marici-succ p) i)
                  (marici-mul (marici-succ p) j))
                (ih j))))) b
```

## Boundary

Positive scaling preserves comparison but this theorem does not state
multiplicative cancellation of equality. It supplies the missing sign branch
for scaling normalized mixed integer sums.
