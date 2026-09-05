# Natural additive-gap order is transitive

Two additive gaps compose by addition in outer-then-inner order. Natural
addition associativity aligns the composite gap with the left-bound equation, after
which function congruence and the right-bound equation reach the final target.

```rzk
#lang rzk-1
```

```rzk
#define marici-nat-at-most-transitive
  ( a b c : MariciNat)
  ( left-bound : MariciNatAtMost a b)
  ( right-bound : MariciNatAtMost b c)
  : MariciNatAtMost a c
  := match left-bound into
      (\ left-bound-prime → MariciNatAtMost b c → MariciNatAtMost a c)
      ( marici-nat-at-most-witness left-bound-gap left-bound-equation ⇒
          \ right-bound-prime →
            match right-bound-prime
            ( marici-nat-at-most-witness right-bound-gap right-bound-equation ⇒
                marici-nat-at-most-witness a c
                  (marici-add right-bound-gap left-bound-gap)
                  (concat MariciNat
                    (marici-add
                      (marici-add right-bound-gap left-bound-gap) a)
                    (marici-add right-bound-gap
                      (marici-add left-bound-gap a))
                    c
                    (marici-add-assoc right-bound-gap left-bound-gap a)
                    (concat MariciNat
                      (marici-add right-bound-gap
                        (marici-add left-bound-gap a))
                      (marici-add right-bound-gap b)
                      c
                      (ap MariciNat MariciNat
                        (marici-add left-bound-gap a) b
                        (\ target → marici-add right-bound-gap target)
                        left-bound-equation)
                      right-bound-equation)))
      )
      right-bound
```

## Boundary

Every index beyond an intermediate index is now explicitly beyond the original
cutoff, with a composed additive gap retained in the witness. Pattern matching
that witness supplies the length and endpoint equation required by the ordered
partial-sum distance theorem.
