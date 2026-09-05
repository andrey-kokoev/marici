# Rational distance satisfies the triangle inequality

The raw inequality descends through normalization. Distance flattening supplies
the left endpoint path; addition flattening and component congruence supply the
right endpoint path.

```rzk
#lang rzk-1
```

```rzk
#define marici-raw-distance
  ( p q : MariciRawFraction)
  : MariciRawFraction
  := marici-raw-fraction-absolute
      (marici-raw-fraction-subtract p q)

#define marici-rational-distance-sum-raw-components
  ( p q r : MariciRational)
  : marici-rational-forget
      (marici-rational-from-raw
        (marici-raw-fraction-add
          (marici-raw-distance
            (marici-rational-forget p) (marici-rational-forget q))
          (marici-raw-distance
            (marici-rational-forget q) (marici-rational-forget r))))
    =_{MariciRawFraction}
    marici-rational-forget
      (marici-rational-add
        (marici-rational-distance p q)
        (marici-rational-distance q r))
  := concat MariciRawFraction
      (marici-rational-forget
        (marici-rational-from-raw
          (marici-raw-fraction-add
            (marici-raw-distance
              (marici-rational-forget p) (marici-rational-forget q))
            (marici-raw-distance
              (marici-rational-forget q) (marici-rational-forget r)))))
      (marici-rational-forget
        (marici-rational-add
          (marici-rational-from-raw
            (marici-raw-distance
              (marici-rational-forget p) (marici-rational-forget q)))
          (marici-rational-from-raw
            (marici-raw-distance
              (marici-rational-forget q) (marici-rational-forget r)))))
      (marici-rational-forget
        (marici-rational-add
          (marici-rational-distance p q)
          (marici-rational-distance q r)))
      (rev MariciRawFraction
        (marici-rational-forget
          (marici-rational-add
            (marici-rational-from-raw
              (marici-raw-distance
                (marici-rational-forget p) (marici-rational-forget q)))
            (marici-rational-from-raw
              (marici-raw-distance
                (marici-rational-forget q) (marici-rational-forget r)))))
        (marici-rational-forget
          (marici-rational-from-raw
            (marici-raw-fraction-add
              (marici-raw-distance
                (marici-rational-forget p) (marici-rational-forget q))
              (marici-raw-distance
                (marici-rational-forget q) (marici-rational-forget r)))))
        (marici-rational-add-from-raw-components
          (marici-raw-distance
            (marici-rational-forget p) (marici-rational-forget q))
          (marici-raw-distance
            (marici-rational-forget q) (marici-rational-forget r))))
      (marici-rational-add-component-congruent
        (marici-rational-from-raw
          (marici-raw-distance
            (marici-rational-forget p) (marici-rational-forget q)))
        (marici-rational-distance p q)
        (marici-rational-from-raw
          (marici-raw-distance
            (marici-rational-forget q) (marici-rational-forget r)))
        (marici-rational-distance q r)
        (rev MariciRawFraction
          (marici-rational-forget (marici-rational-distance p q))
          (marici-rational-forget
            (marici-rational-from-raw
              (marici-raw-distance
                (marici-rational-forget p) (marici-rational-forget q))))
          (marici-rational-distance-raw-components p q))
        (rev MariciRawFraction
          (marici-rational-forget (marici-rational-distance q r))
          (marici-rational-forget
            (marici-rational-from-raw
              (marici-raw-distance
                (marici-rational-forget q) (marici-rational-forget r))))
          (marici-rational-distance-raw-components q r)))

#define marici-rational-distance-triangle
  ( p q r : MariciRational)
  : MariciRationalAtMost
      (marici-rational-distance p r)
      (marici-rational-add
        (marici-rational-distance p q)
        (marici-rational-distance q r))
  := marici-rational-at-most-transport-right-components
      (marici-rational-distance p r)
      (marici-rational-from-raw
        (marici-raw-fraction-add
          (marici-raw-distance
            (marici-rational-forget p) (marici-rational-forget q))
          (marici-raw-distance
            (marici-rational-forget q) (marici-rational-forget r))))
      (marici-rational-add
        (marici-rational-distance p q)
        (marici-rational-distance q r))
      (marici-rational-distance-sum-raw-components p q r)
      (marici-rational-at-most-transport-left-components
        (marici-rational-from-raw
          (marici-raw-distance
            (marici-rational-forget p) (marici-rational-forget r)))
        (marici-rational-distance p r)
        (marici-rational-from-raw
          (marici-raw-fraction-add
            (marici-raw-distance
              (marici-rational-forget p) (marici-rational-forget q))
            (marici-raw-distance
              (marici-rational-forget q) (marici-rational-forget r))))
        (rev MariciRawFraction
          (marici-rational-forget (marici-rational-distance p r))
          (marici-rational-forget
            (marici-rational-from-raw
              (marici-raw-distance
                (marici-rational-forget p) (marici-rational-forget r))))
          (marici-rational-distance-raw-components p r))
        (marici-raw-at-most-to-rational-at-most
          (marici-raw-distance
            (marici-rational-forget p) (marici-rational-forget r))
          (marici-raw-fraction-add
            (marici-raw-distance
              (marici-rational-forget p) (marici-rational-forget q))
            (marici-raw-distance
              (marici-rational-forget q) (marici-rational-forget r)))
          (marici-raw-distance-triangle
            (marici-rational-forget p)
            (marici-rational-forget q)
            (marici-rational-forget r))))
```

## Boundary

The canonical rational distance now satisfies the triangle inequality. Cauchy-
sequence equivalence transitivity additionally requires a rational bound that
combines two reciprocal tolerances into one target tolerance.
