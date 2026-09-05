# Conditional complex conjugation is involutive

Applying complex conjugation twice fixes the real coordinate and negates the
imaginary coordinate twice. Conditional real-negation involutivity lifts through
the complex constructor.

```rzk
#lang rzk-1
```

```rzk
#define marici-complex-conjugate-involutive
  ( z : MariciComplex)
  : marici-complex-conjugate (marici-complex-conjugate z)
    =_{MariciComplex}
    z
  := match z
      ( marici-complex real-part imaginary-part ⇒
          ap MariciReal MariciComplex
            (marici-real-negate
              (marici-real-negate imaginary-part))
            imaginary-part
            (\ coordinate → marici-complex real-part coordinate)
            (marici-real-negate-involutive imaginary-part))
```

## Boundary

Complex conjugation is involutive, conditional on the seven explicit
set-quotient assumptions supporting real negation. This is an algebraic
structure theorem only; complex addition, multiplication, exponentiation, and
analytic continuation remain unconstructed.
