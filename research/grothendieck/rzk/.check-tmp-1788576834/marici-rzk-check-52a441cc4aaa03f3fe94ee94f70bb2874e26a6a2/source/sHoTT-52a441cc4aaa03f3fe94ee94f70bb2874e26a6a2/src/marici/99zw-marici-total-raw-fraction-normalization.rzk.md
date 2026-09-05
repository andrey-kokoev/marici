# Total normalization of raw fractions

Each raw fraction supplies its own denominator predecessor as the external
bound. Reflexivity places it in the bounded normalization family, yielding a
reduced equivalent representative for every input.

```rzk
#lang rzk-1
```

```rzk
#define marici-normalize-raw-components
  ( a : MariciInt)
  ( d : MariciNat)
  : MariciRawFractionNormalization (marici-raw-fraction a d)
  := marici-normalize-bounded d a d (marici-at-most-reflexive d)

#define marici-normalize-raw-fraction
  ( p : MariciRawFraction)
  : MariciRawFractionNormalization p
  := match p
      ( marici-raw-fraction a d ⇒
          marici-normalize-raw-components a d)

#define marici-normalized-raw-representative
  ( p : MariciRawFraction)
  : MariciRawFraction
  := marici-normalization-forget-representative p
      (marici-normalize-raw-fraction p)
```

## Boundary

Normalization existence is now total and executable: every raw fraction yields
a reduced representative with a checked equivalence proof. This does not yet
prove that two equivalent inputs normalize to equal representatives.
Reduced-representative uniqueness and a rational carrier remain open.
