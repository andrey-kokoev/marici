# Arbitrary two-positive/one-negative associativity

The third-dominant handler matches the leading predecessor against the residual
and dispatches to the three transported region implementations. Feeding this
handler to the outer factorization closes the full `(+,+,-)` constructor face;
simultaneous sign reversal closes `(-,-,+)`.

```rzk
#lang rzk-1
```

```rzk
#define marici-third-dominant-assoc-handler
  : MariciThirdDominantAssocHandler
  := \ a b c residual third-equation →
      match (marici-classify-mixed-leading-residual a residual) into
      (\ comparison → MariciIntAddAssociates
        (marici-int-pos a) (marici-int-pos b) (marici-int-neg c))
      ( marici-mixed-middle-dominates remainder leading-equation ⇒
          marici-third-handler-first-dominant-branch
            a b c residual remainder third-equation leading-equation
      | marici-mixed-middle-equals leading-equation ⇒
          marici-third-handler-equal-residual-branch
            a b c residual third-equation leading-equation
      | marici-mixed-third-dominates remainder residual-equation ⇒
          marici-third-handler-residual-dominant-branch
            a b c residual remainder third-equation residual-equation)

#define marici-int-add-assoc-positive-positive-negative
  ( a b c : MariciNat)
  : MariciIntAddAssociates
      (marici-int-pos a) (marici-int-pos b) (marici-int-neg c)
  := marici-int-add-assoc-positive-positive-negative-from-third-handler
      marici-third-dominant-assoc-handler a b c

#define marici-int-add-assoc-negative-negative-positive
  ( a b c : MariciNat)
  : MariciIntAddAssociates
      (marici-int-neg a) (marici-int-neg b) (marici-int-pos c)
  := marici-int-add-assoc-sign-reversal
      (marici-int-pos a) (marici-int-pos b) (marici-int-neg c)
      (marici-int-add-assoc-positive-positive-negative a b c)
```

## Boundary

Two of the six nonzero mixed-sign constructor faces are now closed for
arbitrary magnitudes. The remaining four are permutations with the exceptional
sign in the first or middle position; they require transport using additive
commutativity and the checked face, not new magnitude classifications.
