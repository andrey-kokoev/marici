# Nonnegative integers are closed under addition

Canonical sign elimination proves additive closure; negative constructor
branches contradict the supplied nonnegativity witnesses.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-nonnegative-add
  ( x y : MariciInt)
  ( x-nonnegative : MariciIntIsNonnegative x)
  ( y-nonnegative : MariciIntIsNonnegative y)
  : MariciIntIsNonnegative (marici-int-add x y)
  := (match x into
      (\ x-prime → MariciIntIsNonnegative x-prime
        → MariciIntIsNonnegative y
        → MariciIntIsNonnegative (marici-int-add x-prime y))
      ( marici-int-zero ⇒ \ hx hy → hy
      | marici-int-pos a ⇒ \ hx →
          (match y into
            (\ y-prime → MariciIntIsNonnegative y-prime
              → MariciIntIsNonnegative
                  (marici-int-add (marici-int-pos a) y-prime))
            ( marici-int-zero ⇒ \ hy → marici-trivial
            | marici-int-pos b ⇒ \ hy → marici-trivial
            | marici-int-neg b ⇒ \ hy →
                marici-empty-elim
                  (MariciIntIsNonnegative
                    (marici-int-add (marici-int-pos a) (marici-int-neg b)))
                  hy))
      | marici-int-neg a ⇒ \ hx hy →
          marici-empty-elim
            (MariciIntIsNonnegative (marici-int-add (marici-int-neg a) y))
            hx)) x-nonnegative y-nonnegative
```

## Boundary

This proves additive closure of integer nonnegativity. Integer-order
transitivity still requires rewriting the sum of two differences to the outer
difference by the checked ring laws.
