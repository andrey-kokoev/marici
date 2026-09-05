# Normalized translated addition cancels

Rational addition and subtraction are flattened to one raw expression. The raw
translated-addition equivalence then identifies its normalized representative
with that of the untranslated second summand.

```rzk
#lang rzk-1
```

```rzk
#define marici-normalized-translated-addition-cancellation-components
  ( p q : MariciRawFraction)
  : marici-rational-forget
      (marici-rational-subtract
        (marici-rational-add
          (marici-rational-from-raw p)
          (marici-rational-from-raw q))
        (marici-rational-from-raw p))
    =_{MariciRawFraction}
    marici-rational-forget (marici-rational-from-raw q)
  := concat MariciRawFraction
      (marici-rational-forget
        (marici-rational-subtract
          (marici-rational-add
            (marici-rational-from-raw p)
            (marici-rational-from-raw q))
          (marici-rational-from-raw p)))
      (marici-rational-forget
        (marici-rational-subtract
          (marici-rational-from-raw
            (marici-raw-fraction-add p q))
          (marici-rational-from-raw p)))
      (marici-rational-forget (marici-rational-from-raw q))
      (marici-rational-subtract-component-congruent
        (marici-rational-add
          (marici-rational-from-raw p)
          (marici-rational-from-raw q))
        (marici-rational-from-raw (marici-raw-fraction-add p q))
        (marici-rational-from-raw p)
        (marici-rational-from-raw p)
        (marici-rational-add-from-raw-components p q) refl)
      (concat MariciRawFraction
        (marici-rational-forget
          (marici-rational-subtract
            (marici-rational-from-raw
              (marici-raw-fraction-add p q))
            (marici-rational-from-raw p)))
        (marici-rational-forget
          (marici-rational-from-raw
            (marici-raw-fraction-subtract
              (marici-raw-fraction-add p q) p)))
        (marici-rational-forget (marici-rational-from-raw q))
        (marici-rational-subtract-from-raw-components
          (marici-raw-fraction-add p q) p)
        (concat MariciRawFraction
          (marici-rational-forget
            (marici-rational-from-raw
              (marici-raw-fraction-subtract
                (marici-raw-fraction-add p q) p)))
          (marici-normalized-raw-representative
            (marici-raw-fraction-subtract
              (marici-raw-fraction-add p q) p))
          (marici-rational-forget (marici-rational-from-raw q))
          (marici-rational-from-raw-forget-normalized
            (marici-raw-fraction-subtract
              (marici-raw-fraction-add p q) p))
          (concat MariciRawFraction
            (marici-normalized-raw-representative
              (marici-raw-fraction-subtract
                (marici-raw-fraction-add p q) p))
            (marici-normalized-raw-representative q)
            (marici-rational-forget (marici-rational-from-raw q))
            (marici-normalized-raw-representatives-respect-equivalence
              (marici-raw-fraction-subtract
                (marici-raw-fraction-add p q) p)
              q (marici-raw-translated-addition-cancellation p q))
            (rev MariciRawFraction
              (marici-rational-forget (marici-rational-from-raw q))
              (marici-normalized-raw-representative q)
              (marici-rational-from-raw-forget-normalized q)))))
```

## Boundary

Translated addition now cancels after rational normalization at canonical
components. Component congruence can transport arbitrary rational prefix and
tail presentations into this lemma, completing shifted-tail extraction.
