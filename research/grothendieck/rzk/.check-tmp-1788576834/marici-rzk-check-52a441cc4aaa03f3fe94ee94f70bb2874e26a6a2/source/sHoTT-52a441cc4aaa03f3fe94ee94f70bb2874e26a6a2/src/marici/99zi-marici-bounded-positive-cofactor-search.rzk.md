# Bounded search for a positive cofactor

Given a positive factor, target, starting cofactor predecessor, and fuel, the
search tests successive positive cofactors using decidable natural equality.
A hit retains the cofactor and exact multiplication path.

```rzk
#lang rzk-1
```

```rzk
#data MariciPositiveCofactorSearchHit
  ( factor-predecessor value-predecessor : MariciNat)
  := marici-positive-cofactor-search-miss
  | marici-positive-cofactor-search-hit
      ( cofactor-predecessor : MariciNat)
      ( equation : marici-mul
          (marici-succ cofactor-predecessor)
          (marici-succ factor-predecessor)
        =_{MariciNat} marici-succ value-predecessor)

#define marici-search-positive-cofactor
  ( fuel factor value : MariciNat)
  : MariciPositiveCofactorSearchHit factor value
  := match fuel
      ( marici-zero ⇒
          marici-positive-cofactor-search-miss factor value
      | marici-succ remaining recurse ⇒
          match (marici-nat-decide-equality
            (marici-mul (marici-succ remaining) (marici-succ factor))
            (marici-succ value))
            ( marici-nat-equal equation ⇒
                marici-positive-cofactor-search-hit
                  factor value remaining equation
            | marici-nat-unequal refutation ⇒ recurse))
```

A closed computation confirms that factor two finds cofactor two for target
four within its second tested candidate.

```rzk
#define marici-search-two-times-two
  : MariciPositiveCofactorSearchHit marici-one marici-three
  := marici-search-positive-cofactor marici-two marici-one marici-three
```

## Boundary

Bounded cofactor enumeration is executable and successful hits carry exact
evidence. A miss currently records only bounded search failure, not a proof of
nondivisibility. Completeness of the bound and refutation accumulation remain
before this becomes a total divisibility decision.
