# A nondivisible residue is coprime to an irreducible value

For a value with no proper nonunit factor, every nonunit divisor of that value
is the whole value. Hence any nonunit common divisor of a residue and the value
would reindex to whole-value divisibility of the residue. A refutation of that
divisibility therefore proves coprimality.

```rzk
#lang rzk-1
```

```rzk
#define marici-irreducible-nondivisor-is-coprime
  ( irreducible-residual residue : MariciNat)
  ( irreducible : MariciNatNoProperNonunitFactor irreducible-residual)
  ( whole-not-divides-residue : MariciNatDivides
      (marici-succ (marici-succ (marici-succ irreducible-residual)))
      residue
    → MariciEmpty)
  : MariciNatAreCoprime residue
      (marici-succ (marici-succ (marici-succ irreducible-residual)))
  := \ common →
      match common
      ( marici-nat-nonunit-common-divisor
          factor-predecessor divides-residue divides-irreducible ⇒
        whole-not-divides-residue
          (marici-nat-divides-reindex-divisor
            (marici-succ (marici-succ factor-predecessor))
            (marici-succ
              (marici-succ (marici-succ irreducible-residual)))
            residue
            (marici-irreducible-nonunit-divisor-rigid
              irreducible-residual factor-predecessor
              irreducible divides-irreducible)
            divides-residue))
```

## Boundary

A residue not divisible by an irreducible value is now constructively coprime
to it. For the computed remainder of `x` modulo that value, the remaining step
is to show whole-value divisibility of the remainder would combine with the
explicit quotient multiple to give whole-value divisibility of `x`, which the
original coprimality hypothesis refutes.
