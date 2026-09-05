# Constant Cauchy sequences embed rationals into the completion

Every constant rational sequence is Cauchy with zero modulus because each
pointwise comparison is self-distance. Its quotient class defines the canonical
map from rationals to the conditional real completion.

```rzk
#lang rzk-1
```

```rzk
#define marici-rational-constant-cauchy-sequence
  ( q : MariciRational)
  : MariciRationalCauchySequence
  := marici-rational-cauchy-sequence
      (\ index → q)
      (\ tolerance-index → marici-zero)
      (\ k m n m-bound n-bound →
        marici-rational-distance-self-at-most-tolerance q k)

#assume marici-set-quotient
  : ( A : U) → (A → A → U) → U

#assume marici-set-quotient-class
  : ( A : U)
  → ( relation : A → A → U)
  → A
  → marici-set-quotient A relation

#define marici-rational-to-real uses
  (marici-set-quotient marici-set-quotient-class)
  ( q : MariciRational)
  : MariciReal marici-set-quotient
  := marici-real-from-cauchy-sequence
      marici-set-quotient marici-set-quotient-class
      (marici-rational-constant-cauchy-sequence q)
```

## Boundary

Rationals now map to the assumed set-quotient completion through constant Cauchy
sequences. Injectivity, density, real arithmetic, and completeness are not yet
proved; none follows from the quotient interface alone.
