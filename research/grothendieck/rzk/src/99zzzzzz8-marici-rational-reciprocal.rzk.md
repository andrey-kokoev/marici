# Reciprocal on the canonical rational carrier

The existing sign-aware raw reciprocal lifts to canonical reduced rationals on
an explicitly typed nonzero domain.

```rzk
#lang rzk-1
```

```rzk
#define MariciRationalIsNonzero
  ( q : MariciRational)
  : U
  := MariciRawFractionNumeratorNonzero
      (marici-rational-forget q)

#define marici-rational-reciprocal
  ( q : MariciRational)
  ( nonzero : MariciRationalIsNonzero q)
  : MariciRational
  := marici-normalization-representative
      (marici-raw-fraction-reciprocal
        (marici-rational-forget q) nonzero)
      (marici-normalized-reciprocal-witness
        (marici-rational-forget q) nonzero)

#define marici-rational-divide
  ( p q : MariciRational)
  ( nonzero : MariciRationalIsNonzero q)
  : MariciRational
  := marici-rational-mul p
      (marici-rational-reciprocal q nonzero)
```

## Boundary

Reciprocal and division are executable on the typed nonzero domain. Their field
laws and transport of nonzeroness across rational equality remain unproved.
