# Normalization reflects raw-fraction equivalence

Canonical equality was already shown necessary for equivalent presentations.
It is also sufficient: transport source preservation across the normalized
component path, then compose with the reverse of target preservation.

```rzk
#lang rzk-1
```

```rzk
#define marici-raw-fraction-equivalent-if-normalized-equal
  ( source target : MariciRawFraction)
  ( normalized-equal : marici-normalized-raw-representative source
      =_{MariciRawFraction}
    marici-normalized-raw-representative target)
  : marici-raw-fraction-equivalent source target
  := marici-raw-fraction-equivalent-trans
      source
      (marici-normalized-raw-representative target)
      target
      (transport MariciRawFraction
        (\ representative →
          marici-raw-fraction-equivalent source representative)
        (marici-normalized-raw-representative source)
        (marici-normalized-raw-representative target)
        normalized-equal
        (marici-normalized-raw-representative-preserves-equivalence
          source))
      (marici-raw-fraction-equivalent-sym
        target
        (marici-normalized-raw-representative target)
        (marici-normalized-raw-representative-preserves-equivalence
          target))
```

## Boundary

Raw fraction equivalence is now both preserved and reflected by equality of
normalized raw components. Thus the canonical numerator/denominator comparison
is an exact presentation-independent test, rather than only a one-way
invariant. Executable packaging into a decision procedure can reuse the
existing decidable raw-component equality; no quotient eliminator is asserted.
