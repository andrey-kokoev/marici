# Common-prefix invariance of mixed-sign normalization

Adding the same natural prefix to both predecessor magnitudes does not change
comparison or the normalized mixed-sign integer sum. This captures the
recursive cancellation performed by the normalizer in one unbounded theorem.

```rzk
#lang rzk-1
```

```rzk
#define marici-compare-common-prefix
  ( k a b : MariciNat)
  : marici-compare (marici-add k a) (marici-add k b)
    =_{MariciOrdering} marici-compare a b
  := match k
      ( marici-zero ⇒ refl
      | marici-succ j ih ⇒ ih)

#define marici-int-add-pos-neg-common-prefix
  ( k a b : MariciNat)
  : marici-int-add-pos-neg
      (marici-add k a) (marici-add k b)
    =_{MariciInt} marici-int-add-pos-neg a b
  := match k
      ( marici-zero ⇒ refl
      | marici-succ j ih ⇒ ih)

#define marici-int-add-neg-pos-common-prefix
  ( k a b : MariciNat)
  : marici-int-add-neg-pos
      (marici-add k a) (marici-add k b)
    =_{MariciInt} marici-int-add-neg-pos a b
  := match k
      ( marici-zero ⇒ refl
      | marici-succ j ih ⇒ ih)
```

The constructor-level versions state the same invariance for normalized
integers with positive magnitudes.

```rzk
#define marici-int-add-opposite-common-prefix
  ( k a b : MariciNat)
  : marici-int-add
      (marici-int-pos (marici-add k a))
      (marici-int-neg (marici-add k b))
    =_{MariciInt}
    marici-int-add (marici-int-pos a) (marici-int-neg b)
  := marici-int-add-pos-neg-common-prefix k a b

#define marici-int-add-reversed-opposite-common-prefix
  ( k a b : MariciNat)
  : marici-int-add
      (marici-int-neg (marici-add k a))
      (marici-int-pos (marici-add k b))
    =_{MariciInt}
    marici-int-add (marici-int-neg a) (marici-int-pos b)
  := marici-int-add-neg-pos-common-prefix k a b
```

## Boundary

Common recursive prefixes can now be removed uniformly before analyzing an
opposite-sign sum. The residual branch still needs explicit subtraction laws
when one predecessor magnitude reaches zero; distribution through that
residual remains open.
