# Closed rational-order tests

The canonical zero and one presentations exercise cross multiplication,
integer subtraction, and sign-based nonnegativity through the full normalized
rational definitions.

```rzk
#lang rzk-1
```

```rzk
#define marici-rational-zero-at-most-zero
  : MariciRationalAtMost
      marici-rational-zero marici-rational-zero
  := marici-trivial

#define marici-rational-zero-at-most-one
  : MariciRationalAtMost
      marici-rational-zero marici-rational-one
  := marici-trivial

#define marici-rational-one-at-most-one
  : MariciRationalAtMost
      marici-rational-one marici-rational-one
  := marici-trivial
```

## Boundary

These are closed normalization tests, not general order laws. They establish
that the executable order recognizes `0 <= 0`, `0 <= 1`, and `1 <= 1`; general
reflexivity and transitivity remain open.
