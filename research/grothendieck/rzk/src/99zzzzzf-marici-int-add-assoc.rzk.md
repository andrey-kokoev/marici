# Global integer addition associativity

A three-way constructor match assembles the checked zero, same-sign, and six
mixed-sign faces. No comparison or subtraction obligation remains hidden in
the assembly.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-add-assoc
  ( x y z : MariciInt)
  : MariciIntAddAssociates x y z
  := match x into
      (\ x-prime → (y-prime z-prime : MariciInt)
        → MariciIntAddAssociates x-prime y-prime z-prime)
      ( marici-int-zero ⇒ \ y-prime z-prime →
          marici-int-add-assoc-left-zero y-prime z-prime
      | marici-int-pos a ⇒ \ y-prime z-prime → match y-prime into
          (\ y-double-prime → MariciIntAddAssociates
            (marici-int-pos a) y-double-prime z-prime)
          ( marici-int-zero ⇒
              marici-int-add-assoc-middle-zero (marici-int-pos a) z-prime
          | marici-int-pos b ⇒ match z-prime
              ( marici-int-zero ⇒
                  marici-int-add-assoc-right-zero
                    (marici-int-pos a) (marici-int-pos b)
              | marici-int-pos c ⇒
                  marici-int-add-assoc-embedded-nat
                    (marici-succ a) (marici-succ b) (marici-succ c)
              | marici-int-neg c ⇒
                  marici-int-add-assoc-positive-positive-negative a b c)
          | marici-int-neg b ⇒ match z-prime
              ( marici-int-zero ⇒
                  marici-int-add-assoc-right-zero
                    (marici-int-pos a) (marici-int-neg b)
              | marici-int-pos c ⇒
                  marici-int-add-assoc-positive-negative-positive a b c
              | marici-int-neg c ⇒
                  marici-int-add-assoc-positive-negative-negative a b c))
      | marici-int-neg a ⇒ \ y-prime z-prime → match y-prime into
          (\ y-double-prime → MariciIntAddAssociates
            (marici-int-neg a) y-double-prime z-prime)
          ( marici-int-zero ⇒
              marici-int-add-assoc-middle-zero (marici-int-neg a) z-prime
          | marici-int-pos b ⇒ match z-prime
              ( marici-int-zero ⇒
                  marici-int-add-assoc-right-zero
                    (marici-int-neg a) (marici-int-pos b)
              | marici-int-pos c ⇒
                  marici-int-add-assoc-negative-positive-positive a b c
              | marici-int-neg c ⇒
                  marici-int-add-assoc-negative-positive-negative a b c)
          | marici-int-neg b ⇒ match z-prime
              ( marici-int-zero ⇒
                  marici-int-add-assoc-right-zero
                    (marici-int-neg a) (marici-int-neg b)
              | marici-int-pos c ⇒
                  marici-int-add-assoc-negative-negative-positive a b c
              | marici-int-neg c ⇒
                  marici-int-add-assoc-negated-embedded-nat
                    (marici-succ a) (marici-succ b) (marici-succ c))))
      y z
```

## Boundary

Canonical integer addition is globally associative. This closes the principal
additive-normalization blocker. Raw-fraction addition congruence and
associativity may now be derived using integer associativity together with the
remaining distributivity paths; those rational laws are not asserted here.
