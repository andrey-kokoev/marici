# Strict X35 occurrence summand

This two-state packet records the ordinary summand carrying the specialized
secondary class. The native 35-normal is not identified with this occurrence
partner.

```rzk
#lang rzk-1

#data NimaX35SummandState
  := nima-x35-lower-Z
  | nima-x35-upper-occurrence
#define NimaX35SummandBasis : U
  := Sigma (_ : NimaX35SummandState), MariciNat
#define NimaX35Summand : U := NimaZSum NimaX35SummandBasis

#define nima-x35-summand-column : NimaX35SummandBasis -> NimaX35Summand
  := \ (q,n) -> match q
       (nima-x35-lower-Z => nima-sum-zero NimaX35SummandBasis
       | nima-x35-upper-occurrence => nima-sum-neg NimaX35SummandBasis
          (nima-sum-atom NimaX35SummandBasis
            (nima-x35-lower-Z,marici-succ n)))
#define nima-x35-summand-d : NimaX35Summand -> NimaX35Summand
  := nima-sum-bind NimaX35SummandBasis NimaX35SummandBasis
       nima-x35-summand-column

#define nima-x35-Z (n : MariciNat) : NimaX35Summand
  := nima-sum-atom NimaX35SummandBasis (nima-x35-lower-Z,n)
#define nima-x35-upper (n : MariciNat) : NimaX35Summand
  := nima-sum-atom NimaX35SummandBasis (nima-x35-upper-occurrence,n)

#define nima-x35-multiple-is-boundary (n : MariciNat)
  : nima-sum-equal NimaX35SummandBasis
      (nima-x35-summand-d (nima-x35-upper n))
      (nima-sum-neg NimaX35SummandBasis (nima-x35-Z (marici-succ n)))
  := \ probe -> refl

#define nima-x35-bottom-probe : NimaX35SummandBasis -> MariciInt
  := \ (q,n) -> match q
       (nima-x35-lower-Z => match n
          (marici-zero => marici-int-one
          | marici-succ k ih => marici-int-zero)
       | nima-x35-upper-occurrence => marici-int-zero)
#define nima-x35-column-bottom-zero : (v : NimaX35SummandBasis) ->
  nima-sum-eval NimaX35SummandBasis nima-x35-bottom-probe
    (nima-x35-summand-column v) = marici-int-zero
  := \ (q,n) -> (match q into (\ k -> (n' : MariciNat) ->
       nima-sum-eval NimaX35SummandBasis nima-x35-bottom-probe
         (nima-x35-summand-column (k,n')) = marici-int-zero) (
    nima-x35-lower-Z => \ n' -> refl
  | nima-x35-upper-occurrence => \ n' -> refl
  )) n

#define nima-x35-boundary-bottom-zero (p : NimaX35Summand)
  : nima-sum-eval NimaX35SummandBasis nima-x35-bottom-probe
      (nima-x35-summand-d p) = marici-int-zero
  := nima-frame-concat MariciInt
       (nima-sum-eval NimaX35SummandBasis nima-x35-bottom-probe
         (nima-x35-summand-d p))
       (nima-sum-eval NimaX35SummandBasis
         (\ v -> nima-sum-eval NimaX35SummandBasis nima-x35-bottom-probe
           (nima-x35-summand-column v)) p)
       marici-int-zero
       (nima-sum-eval-bind NimaX35SummandBasis NimaX35SummandBasis
         nima-x35-summand-column nima-x35-bottom-probe p)
       (nima-any-eval-zero-atoms NimaX35SummandBasis
         (\ v -> nima-sum-eval NimaX35SummandBasis nima-x35-bottom-probe
           (nima-x35-summand-column v))
         nima-x35-column-bottom-zero p)

#define nima-x35-Z0-is-primitive
  : nima-sum-eval NimaX35SummandBasis nima-x35-bottom-probe
      (nima-x35-Z marici-zero) = marici-int-one
  := refl

#define nima-x35-Z0-not-boundary
  (p : NimaX35Summand)
  (boundary : nima-sum-equal NimaX35SummandBasis
    (nima-x35-summand-d p) (nima-x35-Z marici-zero))
  : marici-int-zero = marici-int-one
  := nima-frame-concat MariciInt marici-int-zero
       (nima-sum-eval NimaX35SummandBasis nima-x35-bottom-probe
         (nima-x35-summand-d p)) marici-int-one
       (nima-frame-rev MariciInt
         (nima-sum-eval NimaX35SummandBasis nima-x35-bottom-probe
           (nima-x35-summand-d p)) marici-int-zero
         (nima-x35-boundary-bottom-zero p))
       (boundary nima-x35-bottom-probe)
```
