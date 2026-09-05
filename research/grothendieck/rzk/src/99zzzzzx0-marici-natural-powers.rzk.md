# Natural powers

```rzk
#lang rzk-1
```

```rzk
#define marici-nat-power
  ( base exponent : MariciNat)
  : MariciNat
  := match exponent
      ( marici-zero ⇒ marici-one
      | marici-succ k ih ⇒ marici-mul base ih)
```

## Boundary

This is natural exponentiation by primitive recursion. Positivity for positive
bases is proved in the following module.
