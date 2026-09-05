# Combined tightened modulus dominates both source moduli

The transitive modulus adds the two source moduli evaluated at the tightened
tolerance index. Each summand is bounded by this sum, so any index beyond the
combined modulus is beyond both source moduli.

```rzk
#lang rzk-1
```

```rzk
#define marici-combined-tightened-modulus
  ( left right : MariciNat → MariciNat)
  ( k : MariciNat)
  : MariciNat
  := marici-add
      (left (marici-double-tolerance-index k))
      (right (marici-double-tolerance-index k))

#define marici-left-at-most-combined-tightened-modulus
  ( left right : MariciNat → MariciNat)
  ( k : MariciNat)
  : MariciNatAtMost
      (left (marici-double-tolerance-index k))
      (marici-combined-tightened-modulus left right k)
  := marici-nat-at-most-witness
      (left (marici-double-tolerance-index k))
      (marici-combined-tightened-modulus left right k)
      (right (marici-double-tolerance-index k))
      (marici-add-comm
        (right (marici-double-tolerance-index k))
        (left (marici-double-tolerance-index k)))

#define marici-right-at-most-combined-tightened-modulus
  ( left right : MariciNat → MariciNat)
  ( k : MariciNat)
  : MariciNatAtMost
      (right (marici-double-tolerance-index k))
      (marici-combined-tightened-modulus left right k)
  := marici-nat-at-most-witness
      (right (marici-double-tolerance-index k))
      (marici-combined-tightened-modulus left right k)
      (left (marici-double-tolerance-index k))
      refl

#define marici-combined-tightened-modulus-left-bound
  ( left right : MariciNat → MariciNat)
  ( k n : MariciNat)
  ( combined-bound : MariciNatAtMost
      (marici-combined-tightened-modulus left right k) n)
  : MariciNatAtMost (left (marici-double-tolerance-index k)) n
  := marici-at-most-transitive-general
      (left (marici-double-tolerance-index k))
      (marici-combined-tightened-modulus left right k) n
      (marici-left-at-most-combined-tightened-modulus left right k)
      combined-bound

#define marici-combined-tightened-modulus-right-bound
  ( left right : MariciNat → MariciNat)
  ( k n : MariciNat)
  ( combined-bound : MariciNatAtMost
      (marici-combined-tightened-modulus left right k) n)
  : MariciNatAtMost (right (marici-double-tolerance-index k)) n
  := marici-at-most-transitive-general
      (right (marici-double-tolerance-index k))
      (marici-combined-tightened-modulus left right k) n
      (marici-right-at-most-combined-tightened-modulus left right k)
      combined-bound
```

## Boundary

A bound beyond the combined modulus now feeds both source equivalence witnesses
at the tightened tolerance index. Their pointwise estimates can be composed by
the rational distance triangle and tolerance-combination inequalities.
