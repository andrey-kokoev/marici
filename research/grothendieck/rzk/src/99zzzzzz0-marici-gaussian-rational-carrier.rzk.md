# Gaussian rational carrier

Pairs of canonical rationals provide the first complex-valued executable
carrier. Operations are defined componentwise, with multiplication using the
standard real and imaginary decomposition.

```rzk
#lang rzk-1
```

```rzk
#data MariciGaussianRational
  := marici-gaussian-rational
      ( real : MariciRational)
      ( imaginary : MariciRational)

#define marici-gaussian-rational-zero
  : MariciGaussianRational
  := marici-gaussian-rational
      marici-rational-zero marici-rational-zero

#define marici-gaussian-rational-one
  : MariciGaussianRational
  := marici-gaussian-rational
      marici-rational-one marici-rational-zero

#define marici-gaussian-rational-add
  ( z w : MariciGaussianRational)
  : MariciGaussianRational
  := match z
      ( marici-gaussian-rational a b ⇒
          match w
            ( marici-gaussian-rational c d ⇒
                marici-gaussian-rational
                  (marici-rational-add a c)
                  (marici-rational-add b d)))

#define marici-gaussian-rational-negate
  ( z : MariciGaussianRational)
  : MariciGaussianRational
  := match z
      ( marici-gaussian-rational a b ⇒
          marici-gaussian-rational
            (marici-rational-negate a)
            (marici-rational-negate b))

#define marici-gaussian-rational-mul
  ( z w : MariciGaussianRational)
  : MariciGaussianRational
  := match z
      ( marici-gaussian-rational a b ⇒
          match w
            ( marici-gaussian-rational c d ⇒
                marici-gaussian-rational
                  (marici-rational-add
                    (marici-rational-mul a c)
                    (marici-rational-negate
                      (marici-rational-mul b d)))
                  (marici-rational-add
                    (marici-rational-mul a d)
                    (marici-rational-mul b c))))

#define marici-gaussian-rational-embed
  ( q : MariciRational)
  : MariciGaussianRational
  := marici-gaussian-rational q marici-rational-zero
```

## Boundary

This is Gaussian rational arithmetic, not a complete complex-number object.
It enables complex-valued finite algebraic tests but supplies no metric,
completion, transcendental functions, infinite sums, or analytic continuation.
