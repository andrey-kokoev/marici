# Natural at-most antisymmetry

Antisymmetry is proved by structural recursion. At zero, the reverse bound
forces the other index to be zero. At two successors, both bounds descend and
the induction hypothesis identifies their predecessors.

```rzk
#lang rzk-1
```

```rzk
#define marici-at-most-antisymmetric
  : MariciNatAtMostAntisymmetry
  := \ d → match d into
      (\ d-prime → (e : MariciNat)
        → MariciNatAtMost d-prime e
        → MariciNatAtMost e d-prime
        → d-prime =_{MariciNat} e)
      ( marici-zero ⇒ \ e bound-forward bound-reverse →
          rev MariciNat e marici-zero
            (marici-at-most-zero-equal-zero e bound-reverse)
      | marici-succ n induction ⇒ \ e → match e
          ( marici-zero ⇒ \ bound-forward bound-reverse →
              marici-at-most-zero-equal-zero
                (marici-succ n) bound-forward
          | marici-succ m previous ⇒
              \ bound-forward bound-reverse →
                ap MariciNat MariciNat
                  n m marici-succ
                  (induction m
                    (marici-at-most-successors-descend
                      n m bound-forward)
                    (marici-at-most-successors-descend
                      m n bound-reverse))))

#define marici-positive-denominator-divisibility-antisymmetric
  : MariciPositiveDenominatorDivisibilityAntisymmetry
  := marici-positive-denominator-divisibility-antisymmetry-from-at-most
      marici-at-most-antisymmetric

#define marici-reduced-representative-uniqueness-from-euclid
  ( euclid : MariciReducedCrossProductDenominatorDivisibility)
  : MariciReducedRepresentativeUniqueness
  := marici-reduced-representative-uniqueness-from-euclid-and-order
      euclid marici-at-most-antisymmetric
```

## Boundary

Natural-order and positive-divisibility antisymmetry are discharged. General
reduced-representative uniqueness now has one remaining premise only:
`MariciReducedCrossProductDenominatorDivisibility`, the constructive Euclid
bridge from reducedness and cross-product equality.
