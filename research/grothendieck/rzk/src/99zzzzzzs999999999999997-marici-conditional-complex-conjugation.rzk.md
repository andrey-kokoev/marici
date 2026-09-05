# Conditional complex conjugation

Conditional real negation changes the sign of the imaginary coordinate while
leaving the real coordinate fixed. The coordinate formulas hold definitionally
for every complex value.

```rzk
#lang rzk-1
```

```rzk
#define marici-complex-conjugate
  ( z : MariciComplex)
  : MariciComplex
  := match z
      ( marici-complex real-part imaginary-part ⇒
          marici-complex real-part
            (marici-real-negate imaginary-part))

#define marici-complex-conjugate-real-part
  ( z : MariciComplex)
  : marici-complex-real-part (marici-complex-conjugate z)
    =_{MariciReal}
    marici-complex-real-part z
  := match z
      ( marici-complex real-part imaginary-part ⇒ refl)

#define marici-complex-conjugate-imaginary-part
  ( z : MariciComplex)
  : marici-complex-imaginary-part (marici-complex-conjugate z)
    =_{MariciReal}
    marici-real-negate (marici-complex-imaginary-part z)
  := match z
      ( marici-complex real-part imaginary-part ⇒ refl)
```

## Boundary

Complex conjugation is conditional on set-quotient real negation. Its coordinate
formulas are proved, but involutivity requires an involution theorem for
`marici-real-negate`. Addition, multiplication, norm, exponentiation, and
analytic structure remain absent.
