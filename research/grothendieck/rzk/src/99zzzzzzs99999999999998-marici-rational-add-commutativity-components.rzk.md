# Rational addition is componentwise commutative

Normalization retraction replaces arbitrary rational inputs by their forgotten
raw presentations. Flattening exposes raw addition commutativity, after which
the opposite rational presentation is reconstructed.

```rzk
#lang rzk-1
```

```rzk
#define marici-rational-add-comm-components
  ( p q : MariciRational)
  : marici-rational-forget (marici-rational-add p q)
    =_{MariciRawFraction}
    marici-rational-forget (marici-rational-add q p)
  := concat MariciRawFraction
      (marici-rational-forget (marici-rational-add p q))
      (marici-rational-forget
        (marici-rational-add
          (marici-rational-from-raw (marici-rational-forget p))
          (marici-rational-from-raw (marici-rational-forget q))))
      (marici-rational-forget (marici-rational-add q p))
      (marici-rational-add-component-congruent
        p (marici-rational-from-raw (marici-rational-forget p))
        q (marici-rational-from-raw (marici-rational-forget q))
        (marici-rational-to-normalized-forget-components p)
        (marici-rational-to-normalized-forget-components q))
      (concat MariciRawFraction
        (marici-rational-forget
          (marici-rational-add
            (marici-rational-from-raw (marici-rational-forget p))
            (marici-rational-from-raw (marici-rational-forget q))))
        (marici-rational-forget
          (marici-rational-from-raw
            (marici-raw-fraction-add
              (marici-rational-forget p)
              (marici-rational-forget q))))
        (marici-rational-forget (marici-rational-add q p))
        (marici-rational-add-from-raw-components
          (marici-rational-forget p) (marici-rational-forget q))
        (concat MariciRawFraction
          (marici-rational-forget
            (marici-rational-from-raw
              (marici-raw-fraction-add
                (marici-rational-forget p)
                (marici-rational-forget q))))
          (marici-rational-forget
            (marici-rational-from-raw
              (marici-raw-fraction-add
                (marici-rational-forget q)
                (marici-rational-forget p))))
          (marici-rational-forget (marici-rational-add q p))
          (ap MariciRawFraction MariciRawFraction
            (marici-raw-fraction-add
              (marici-rational-forget p) (marici-rational-forget q))
            (marici-raw-fraction-add
              (marici-rational-forget q) (marici-rational-forget p))
            (\ raw → marici-rational-forget
              (marici-rational-from-raw raw))
            (marici-raw-fraction-add-comm
              (marici-rational-forget p) (marici-rational-forget q)))
          (concat MariciRawFraction
            (marici-rational-forget
              (marici-rational-from-raw
                (marici-raw-fraction-add
                  (marici-rational-forget q)
                  (marici-rational-forget p))))
            (marici-rational-forget
              (marici-rational-add
                (marici-rational-from-raw (marici-rational-forget q))
                (marici-rational-from-raw (marici-rational-forget p))))
            (marici-rational-forget (marici-rational-add q p))
            (rev MariciRawFraction
              (marici-rational-forget
                (marici-rational-add
                  (marici-rational-from-raw (marici-rational-forget q))
                  (marici-rational-from-raw (marici-rational-forget p))))
              (marici-rational-forget
                (marici-rational-from-raw
                  (marici-raw-fraction-add
                    (marici-rational-forget q)
                    (marici-rational-forget p))))
              (marici-rational-add-from-raw-components
                (marici-rational-forget q) (marici-rational-forget p)))
            (rev MariciRawFraction
              (marici-rational-forget (marici-rational-add q p))
              (marici-rational-forget
                (marici-rational-add
                  (marici-rational-from-raw (marici-rational-forget q))
                  (marici-rational-from-raw (marici-rational-forget p))))
              (marici-rational-add-component-congruent
                q (marici-rational-from-raw (marici-rational-forget q))
                p (marici-rational-from-raw (marici-rational-forget p))
                (marici-rational-to-normalized-forget-components q)
                (marici-rational-to-normalized-forget-components p))))))
```

## Boundary

Rational addition is now commutative at canonical components. Together with
negation involution, this yields invariance of rational distance under
simultaneous negation and enables pointwise negation of Cauchy sequences.
