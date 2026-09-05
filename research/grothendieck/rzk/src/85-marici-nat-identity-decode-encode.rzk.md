# Conditional transfer from identity-code uniqueness

Code uniqueness yields equality of decoded encodings. If the path-side
composite equations are supplied for two paths, this equality transfers to the
paths themselves. This isolates the sole remaining identity-elimination edge.

```rzk
#lang rzk-1
```

```rzk
#define marici-nat-path-equal-from-composites
  ( n m : MariciNat)
  ( e f : n =_{MariciNat} m)
  ( de : marici-nat-identity-decode n m
      (marici-nat-identity-encode n m e)
      =_{(n =_{MariciNat} m)} e)
  ( df : marici-nat-identity-decode n m
      (marici-nat-identity-encode n m f)
      =_{(n =_{MariciNat} m)} f)
  : e =_{(n =_{MariciNat} m)} f
  := concat (n =_{MariciNat} m)
      e
      (marici-nat-identity-decode n m
        (marici-nat-identity-encode n m e))
      f
      (rev (n =_{MariciNat} m)
        (marici-nat-identity-decode n m
          (marici-nat-identity-encode n m e)) e de)
      (concat (n =_{MariciNat} m)
        (marici-nat-identity-decode n m
          (marici-nat-identity-encode n m e))
        (marici-nat-identity-decode n m
          (marici-nat-identity-encode n m f))
        f
        (ap (MariciNatIdentityCode n m) (n =_{MariciNat} m)
          (marici-nat-identity-encode n m e)
          (marici-nat-identity-encode n m f)
          (marici-nat-identity-decode n m)
          (marici-nat-identity-code-unique n m
            (marici-nat-identity-encode n m e)
            (marici-nat-identity-encode n m f)))
        df)
```

## Boundary

Code uniqueness has been transferred conditionally to path uniqueness. The
only missing premise is the arbitrary-path decode--encode composite; module 83
provides its reflexive case.
