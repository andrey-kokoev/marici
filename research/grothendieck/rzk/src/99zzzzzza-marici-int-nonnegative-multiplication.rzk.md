# Nonnegative integers are closed under multiplication

Canonical sign elimination proves multiplicative closure; every negative branch
is discharged by the supplied nonnegativity witness.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-nonnegative-mul
  ( x y : MariciInt)
  ( x-nonnegative : MariciIntIsNonnegative x)
  ( y-nonnegative : MariciIntIsNonnegative y)
  : MariciIntIsNonnegative (marici-int-mul x y)
  := (match x into
      (\ x-prime → MariciIntIsNonnegative x-prime
        → MariciIntIsNonnegative y
        → MariciIntIsNonnegative (marici-int-mul x-prime y))
      ( marici-int-zero ⇒ \ hx hy → marici-trivial
      | marici-int-pos a ⇒ \ hx →
          (match y into
            (\ y-prime → MariciIntIsNonnegative y-prime
              → MariciIntIsNonnegative
                  (marici-int-mul (marici-int-pos a) y-prime))
            ( marici-int-zero ⇒ \ hy → marici-trivial
            | marici-int-pos b ⇒ \ hy → marici-trivial
            | marici-int-neg b ⇒ \ hy →
                marici-empty-elim
                  (MariciIntIsNonnegative
                    (marici-int-mul (marici-int-pos a) (marici-int-neg b)))
                  hy))
      | marici-int-neg a ⇒ \ hx hy →
          marici-empty-elim
            (MariciIntIsNonnegative (marici-int-mul (marici-int-neg a) y))
            hx)) x-nonnegative y-nonnegative
```

## Boundary

This proves multiplicative closure of integer nonnegativity. Additive closure
and order transport through positive multiplication remain separate theorems.
