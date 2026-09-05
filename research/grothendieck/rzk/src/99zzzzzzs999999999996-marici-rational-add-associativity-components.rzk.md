# Rational addition is componentwise associative

Normalization retraction transports three arbitrary rationals to normalization
of their forgotten raw components. Nested addition congruence reaches the
normalized associativity theorem on both bracketings.

```rzk
#lang rzk-1
```

```rzk
#define marici-rational-add-assoc-components
  ( p q r : MariciRational)
  : marici-rational-forget
      (marici-rational-add (marici-rational-add p q) r)
    =_{MariciRawFraction}
    marici-rational-forget
      (marici-rational-add p (marici-rational-add q r))
  := concat MariciRawFraction
      (marici-rational-forget
        (marici-rational-add (marici-rational-add p q) r))
      (marici-rational-forget
        (marici-rational-add
          (marici-rational-add
            (marici-rational-from-raw (marici-rational-forget p))
            (marici-rational-from-raw (marici-rational-forget q)))
          (marici-rational-from-raw (marici-rational-forget r))))
      (marici-rational-forget
        (marici-rational-add p (marici-rational-add q r)))
      (marici-rational-add-component-congruent
        (marici-rational-add p q)
        (marici-rational-add
          (marici-rational-from-raw (marici-rational-forget p))
          (marici-rational-from-raw (marici-rational-forget q)))
        r (marici-rational-from-raw (marici-rational-forget r))
        (marici-rational-add-component-congruent
          p (marici-rational-from-raw (marici-rational-forget p))
          q (marici-rational-from-raw (marici-rational-forget q))
          (marici-rational-to-normalized-forget-components p)
          (marici-rational-to-normalized-forget-components q))
        (marici-rational-to-normalized-forget-components r))
      (concat MariciRawFraction
        (marici-rational-forget
          (marici-rational-add
            (marici-rational-add
              (marici-rational-from-raw (marici-rational-forget p))
              (marici-rational-from-raw (marici-rational-forget q)))
            (marici-rational-from-raw (marici-rational-forget r))))
        (marici-rational-forget
          (marici-rational-add
            (marici-rational-from-raw (marici-rational-forget p))
            (marici-rational-add
              (marici-rational-from-raw (marici-rational-forget q))
              (marici-rational-from-raw (marici-rational-forget r)))))
        (marici-rational-forget
          (marici-rational-add p (marici-rational-add q r)))
        (marici-normalized-rational-add-assoc-components
          (marici-rational-forget p)
          (marici-rational-forget q)
          (marici-rational-forget r))
        (rev MariciRawFraction
          (marici-rational-forget
            (marici-rational-add p (marici-rational-add q r)))
          (marici-rational-forget
            (marici-rational-add
              (marici-rational-from-raw (marici-rational-forget p))
              (marici-rational-add
                (marici-rational-from-raw (marici-rational-forget q))
                (marici-rational-from-raw (marici-rational-forget r)))))
          (marici-rational-add-component-congruent
            p (marici-rational-from-raw (marici-rational-forget p))
            (marici-rational-add q r)
            (marici-rational-add
              (marici-rational-from-raw (marici-rational-forget q))
              (marici-rational-from-raw (marici-rational-forget r)))
            (marici-rational-to-normalized-forget-components p)
            (marici-rational-add-component-congruent
              q (marici-rational-from-raw (marici-rational-forget q))
              r (marici-rational-from-raw (marici-rational-forget r))
              (marici-rational-to-normalized-forget-components q)
              (marici-rational-to-normalized-forget-components r)))))
```

## Boundary

Rational addition is now associative at canonical components for arbitrary
inputs. Induction can therefore split shifted accumulation into the prefix plus
the independently folded tail.
