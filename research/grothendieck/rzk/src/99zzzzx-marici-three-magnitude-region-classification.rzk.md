# Nested classification of the mixed residual

When the negative third term dominates the positive middle term, the remaining
comparison is between the positive leading predecessor and the explicit
negative residual. The existing classifier applies without loss of gap data.

```rzk
#lang rzk-1
```

```rzk
#define marici-classify-mixed-leading-residual
  ( leading residual : MariciNat)
  : MariciMixedMiddleThirdClassification leading residual
  := marici-classify-mixed-middle-third leading residual
```

## Boundary

The two-stage outer proof may first classify middle against third and, only in
the third-dominant branch, invoke this residual classification. Its three
constructors select the checked positive-residual, total-cancellation, and
negative-dominant associativity families. The dependent five-way packaging was
not retained because `first` is an Rzk keyword; no parser defect remains.
