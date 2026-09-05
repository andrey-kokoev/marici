# Addition of normalized rationals is componentwise associative

Nested rational additions are flattened one layer at a time. The raw
associativity path transports through normalization, after which the right
bracketing is reconstructed in reverse.

```rzk
#lang rzk-1
```

```rzk
#define marici-normalized-rational-add-assoc-components
  ( p q r : MariciRawFraction)
  : marici-rational-forget
      (marici-rational-add
        (marici-rational-add
          (marici-rational-from-raw p)
          (marici-rational-from-raw q))
        (marici-rational-from-raw r))
    =_{MariciRawFraction}
    marici-rational-forget
      (marici-rational-add
        (marici-rational-from-raw p)
        (marici-rational-add
          (marici-rational-from-raw q)
          (marici-rational-from-raw r)))
  := concat MariciRawFraction
      (marici-rational-forget
        (marici-rational-add
          (marici-rational-add
            (marici-rational-from-raw p)
            (marici-rational-from-raw q))
          (marici-rational-from-raw r)))
      (marici-rational-forget
        (marici-rational-add
          (marici-rational-from-raw (marici-raw-fraction-add p q))
          (marici-rational-from-raw r)))
      (marici-rational-forget
        (marici-rational-add
          (marici-rational-from-raw p)
          (marici-rational-add
            (marici-rational-from-raw q)
            (marici-rational-from-raw r))))
      (marici-rational-add-component-congruent
        (marici-rational-add
          (marici-rational-from-raw p)
          (marici-rational-from-raw q))
        (marici-rational-from-raw (marici-raw-fraction-add p q))
        (marici-rational-from-raw r) (marici-rational-from-raw r)
        (marici-rational-add-from-raw-components p q) refl)
      (concat MariciRawFraction
        (marici-rational-forget
          (marici-rational-add
            (marici-rational-from-raw (marici-raw-fraction-add p q))
            (marici-rational-from-raw r)))
        (marici-rational-forget
          (marici-rational-from-raw
            (marici-raw-fraction-add
              (marici-raw-fraction-add p q) r)))
        (marici-rational-forget
          (marici-rational-add
            (marici-rational-from-raw p)
            (marici-rational-add
              (marici-rational-from-raw q)
              (marici-rational-from-raw r))))
        (marici-rational-add-from-raw-components
          (marici-raw-fraction-add p q) r)
        (concat MariciRawFraction
          (marici-rational-forget
            (marici-rational-from-raw
              (marici-raw-fraction-add
                (marici-raw-fraction-add p q) r)))
          (marici-rational-forget
            (marici-rational-from-raw
              (marici-raw-fraction-add p
                (marici-raw-fraction-add q r))))
          (marici-rational-forget
            (marici-rational-add
              (marici-rational-from-raw p)
              (marici-rational-add
                (marici-rational-from-raw q)
                (marici-rational-from-raw r))))
          (ap MariciRawFraction MariciRawFraction
            (marici-raw-fraction-add (marici-raw-fraction-add p q) r)
            (marici-raw-fraction-add p (marici-raw-fraction-add q r))
            (\ raw → marici-rational-forget
              (marici-rational-from-raw raw))
            (marici-raw-fraction-add-assoc-path p q r))
          (concat MariciRawFraction
            (marici-rational-forget
              (marici-rational-from-raw
                (marici-raw-fraction-add p
                  (marici-raw-fraction-add q r))))
            (marici-rational-forget
              (marici-rational-add
                (marici-rational-from-raw p)
                (marici-rational-from-raw
                  (marici-raw-fraction-add q r))))
            (marici-rational-forget
              (marici-rational-add
                (marici-rational-from-raw p)
                (marici-rational-add
                  (marici-rational-from-raw q)
                  (marici-rational-from-raw r))))
            (rev MariciRawFraction
              (marici-rational-forget
                (marici-rational-add
                  (marici-rational-from-raw p)
                  (marici-rational-from-raw
                    (marici-raw-fraction-add q r))))
              (marici-rational-forget
                (marici-rational-from-raw
                  (marici-raw-fraction-add p
                    (marici-raw-fraction-add q r))))
              (marici-rational-add-from-raw-components
                p (marici-raw-fraction-add q r)))
            (rev MariciRawFraction
              (marici-rational-forget
                (marici-rational-add
                  (marici-rational-from-raw p)
                  (marici-rational-add
                    (marici-rational-from-raw q)
                    (marici-rational-from-raw r))))
              (marici-rational-forget
                (marici-rational-add
                  (marici-rational-from-raw p)
                  (marici-rational-from-raw
                    (marici-raw-fraction-add q r))))
              (marici-rational-add-component-congruent
                (marici-rational-from-raw p) (marici-rational-from-raw p)
                (marici-rational-add
                  (marici-rational-from-raw q)
                  (marici-rational-from-raw r))
                (marici-rational-from-raw (marici-raw-fraction-add q r))
                refl (marici-rational-add-from-raw-components q r))))))
```

## Boundary

Addition is now associative at canonical components for normalized raw inputs.
Normalization retraction transports arbitrary rationals into this theorem,
after which shifted accumulation can be split into prefix plus finite tail.
