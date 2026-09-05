# Soundness of reduced normal-form zero testing

A zero numerator path transports a reduced normal form to the reduced-zero case,
whose denominator is already known to be one. Conversely, explicit numerator
nonzeroness refutes structural equality with canonical raw zero by projection.

```rzk
#lang rzk-1
```

```rzk
#define marici-reduced-components-zero-is-canonical
  ( a : MariciInt)
  ( d : MariciNat)
  ( reduced : MariciRawComponentsAreReduced a d)
  ( numerator-zero : a =_{MariciInt} marici-int-zero)
  : marici-raw-fraction a d =_{MariciRawFraction}
      marici-raw-fraction marici-int-zero marici-zero
  := ind-path MariciInt marici-int-zero
      (\ a-prime numerator-path →
        MariciRawComponentsAreReduced a-prime d
        → marici-raw-fraction a-prime d =_{MariciRawFraction}
            marici-raw-fraction marici-int-zero marici-zero)
      (\ reduced-zero →
        marici-reduced-zero-raw-representative-canonical
          d reduced-zero)
      a (rev MariciInt a marici-int-zero numerator-zero) reduced

#define marici-reduced-normal-form-zero-is-canonical
  ( p : MariciReducedRawFraction)
  ( numerator-zero : marici-raw-fraction-numerator
      (marici-reduced-raw-fraction-forget p)
    =_{MariciInt} marici-int-zero)
  : marici-reduced-raw-fraction-forget p =_{MariciRawFraction}
      marici-raw-fraction marici-int-zero marici-zero
  := (match p into
      (\ p-prime →
        (marici-raw-fraction-numerator
          (marici-reduced-raw-fraction-forget p-prime)
          =_{MariciInt} marici-int-zero)
        → marici-reduced-raw-fraction-forget p-prime
            =_{MariciRawFraction}
          marici-raw-fraction marici-int-zero marici-zero)
      ( marici-reduced-raw-fraction a d reduced ⇒ \ zero-prime →
          marici-reduced-components-zero-is-canonical
            a d reduced zero-prime)) numerator-zero

#define marici-reduced-normal-form-nonzero-refutes-canonical-zero
  ( p : MariciReducedRawFraction)
  ( nonzero : MariciReducedNormalFormNonzero p)
  : (marici-reduced-raw-fraction-forget p =_{MariciRawFraction}
      marici-raw-fraction marici-int-zero marici-zero)
    → MariciEmpty
  := \ path → nonzero
      (ap MariciRawFraction MariciInt
        (marici-reduced-raw-fraction-forget p)
        (marici-raw-fraction marici-int-zero marici-zero)
        marici-raw-fraction-numerator path)
```

## Boundary

The executable zero decision on reduced normal forms is sound and complete for
structural equality with canonical raw zero. This conclusion is independent of
general reduced uniqueness because zero reducedness alone forces denominator
one. Relating this structural test to arbitrary equivalent raw presentations
still requires normalization canonicality.
