# Doubled reciprocal-tolerance index

The index `succ (k + k)` represents denominator `2(k+1)`. This is the tighter
reciprocal tolerance whose two equal copies combine to the tolerance indexed by
`k`.

```rzk
#lang rzk-1
```

```rzk
#define marici-double-tolerance-index
  ( k : MariciNat)
  : MariciNat
  := marici-succ (marici-add k k)

#define marici-double-tolerance-denominator
  ( k : MariciNat)
  : marici-succ (marici-double-tolerance-index k)
    =_{MariciNat}
    marici-add (marici-succ k) (marici-succ k)
  := rev MariciNat
      (marici-add (marici-succ k) (marici-succ k))
      (marici-succ (marici-double-tolerance-index k))
      (marici-add-succ-right (marici-succ k) k)
```

## Boundary

The required tighter modulus index and its exact denominator identity are now
available. The reciprocal-tolerance combination bound still requires lifting
this identity through raw fraction addition and rational normalization.
