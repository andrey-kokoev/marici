# Coprimality excludes divisibility by the whole nonunit value

If a structurally nonunit value divides the other coordinate, it is itself a
nonunit common divisor: the supplied witness handles the first coordinate and
reflexivity handles the value. Coprimality therefore refutes that divisibility.

```rzk
#lang rzk-1
```

```rzk
#define marici-coprime-excludes-whole-nonunit-divisor
  ( x factor-predecessor : MariciNat)
  ( coprime : MariciNatAreCoprime x
      (marici-succ (marici-succ factor-predecessor)))
  : MariciNatDivides
      (marici-succ (marici-succ factor-predecessor)) x
    → MariciEmpty
  := \ divides-x →
      coprime
        (marici-nat-nonunit-common-divisor
          x (marici-succ (marici-succ factor-predecessor))
          factor-predecessor divides-x
          (marici-nat-divides-reflexive
            (marici-succ (marici-succ factor-predecessor))))

#define marici-coprime-at-least-three-excludes-whole-divisor
  ( residual x : MariciNat)
  ( coprime : MariciNatAreCoprime x
      (marici-succ (marici-succ (marici-succ residual))))
  : MariciNatDivides
      (marici-succ (marici-succ (marici-succ residual))) x
    → MariciEmpty
  := marici-coprime-excludes-whole-nonunit-divisor
      x (marici-succ residual) coprime
```

## Boundary

For every nonunit divisor, coprimality now supplies the exact refutation of the
branch in which that whole divisor divides the other coordinate. In the
irreducible Euclid proof, executable divisibility testing of the first product
factor can therefore retain only its negative branch. The final prime-divisor
step still requires the additive division induction on the nondivisible first
factor.
