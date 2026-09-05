# Outer factorization of the mixed associativity proof

The first middle/third classification discharges the middle-dominant and equal
branches using checked families. Consequently the arbitrary `(+,+,-)` face
reduces to one typed handler for the third-dominant branch.

```rzk
#lang rzk-1
```

```rzk
#define MariciThirdDominantAssocHandler
  : U
  := ( a b c residual : MariciNat)
    → (c =_{MariciNat} marici-add (marici-succ b) residual)
    → MariciIntAddAssociates
        (marici-int-pos a) (marici-int-pos b) (marici-int-neg c)

#define marici-int-add-assoc-positive-positive-negative-from-third-handler
  ( handler : MariciThirdDominantAssocHandler)
  ( a b c : MariciNat)
  : MariciIntAddAssociates
      (marici-int-pos a) (marici-int-pos b) (marici-int-neg c)
  := match (marici-classify-mixed-middle-third b c) into
      (\ comparison → MariciIntAddAssociates
        (marici-int-pos a) (marici-int-pos b) (marici-int-neg c))
      ( marici-mixed-middle-dominates residual equation ⇒
          transport MariciNat
            (\ middle → MariciIntAddAssociates
              (marici-int-pos a) (marici-int-pos middle)
              (marici-int-neg c))
            (marici-add (marici-succ c) residual) b
            (rev MariciNat b
              (marici-add (marici-succ c) residual) equation)
            (marici-int-add-assoc-positive-middle-dominates-negative
              a c residual)
      | marici-mixed-middle-equals equation ⇒
          transport MariciNat
            (\ third → MariciIntAddAssociates
              (marici-int-pos a) (marici-int-pos b)
              (marici-int-neg third))
            b c equation
            (marici-int-add-assoc-positive-positive-negative-self a b)
      | marici-mixed-third-dominates residual equation ⇒
          handler a b c residual equation)
```

## Boundary

The full mixed face now has one remaining typed constructor:
`MariciThirdDominantAssocHandler`. It must classify the leading predecessor
against the residual and transport the three already checked residual-region
families. No middle-dominant or equal branch remains in that obligation.
