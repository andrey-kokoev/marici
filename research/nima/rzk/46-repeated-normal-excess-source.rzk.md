# Actual repeated-normal excess source

This is the smallest source packet distinguishing the two copies of the shared
normal.  It must not be replaced by multiplication of one target state by an
internal normal parameter.

```rzk
#lang rzk-1

#data NimaRepeatedNormalState
  := nima-repeated-normal-base
  | nima-repeated-normal-branch-3
  | nima-repeated-normal-pair-3

#define NimaRepeatedNormalBasis : U
  := Sigma (_ : NimaRepeatedNormalState), MariciNat
#define NimaRepeatedNormal : U := NimaZSum NimaRepeatedNormalBasis

#define nima-repeated-normal-column : NimaRepeatedNormalBasis -> NimaRepeatedNormal
  := \ (q,n) -> match q
       (nima-repeated-normal-base => nima-sum-zero NimaRepeatedNormalBasis
       | nima-repeated-normal-branch-3 =>
          nima-sum-add NimaRepeatedNormalBasis
            (nima-sum-atom NimaRepeatedNormalBasis
              (nima-repeated-normal-base,marici-succ n))
            (nima-sum-zero NimaRepeatedNormalBasis)
       | nima-repeated-normal-pair-3 =>
          nima-sum-add NimaRepeatedNormalBasis
            (nima-sum-atom NimaRepeatedNormalBasis
              (nima-repeated-normal-base,marici-succ n))
            (nima-sum-zero NimaRepeatedNormalBasis))

#define nima-repeated-normal-d : NimaRepeatedNormal -> NimaRepeatedNormal
  := nima-sum-bind NimaRepeatedNormalBasis NimaRepeatedNormalBasis
       nima-repeated-normal-column

#define nima-repeated-normal-column-square : (v : NimaRepeatedNormalBasis) ->
  nima-sum-equal NimaRepeatedNormalBasis
    (nima-repeated-normal-d (nima-repeated-normal-column v))
    (nima-sum-zero NimaRepeatedNormalBasis)
  := \ (q,n) -> (match q into (\ k -> (n' : MariciNat) ->
       nima-sum-equal NimaRepeatedNormalBasis
         (nima-repeated-normal-d (nima-repeated-normal-column (k,n')))
         (nima-sum-zero NimaRepeatedNormalBasis)) (
    nima-repeated-normal-base => \ n' probe -> refl
  | nima-repeated-normal-branch-3 => \ n' probe -> refl
  | nima-repeated-normal-pair-3 => \ n' probe -> refl
  )) n

#define nima-repeated-normal-square (p : NimaRepeatedNormal)
  : nima-sum-equal NimaRepeatedNormalBasis
      (nima-repeated-normal-d (nima-repeated-normal-d p))
      (nima-sum-zero NimaRepeatedNormalBasis)
  := nima-sum-column-square NimaRepeatedNormalBasis nima-repeated-normal-column
       nima-repeated-normal-column-square p

#define nima-repeated-normal-eta (n : MariciNat) : NimaRepeatedNormal
  := nima-sum-add NimaRepeatedNormalBasis
       (nima-sum-atom NimaRepeatedNormalBasis
         (nima-repeated-normal-branch-3,n))
       (nima-sum-neg NimaRepeatedNormalBasis
         (nima-sum-atom NimaRepeatedNormalBasis
           (nima-repeated-normal-pair-3,n)))

#define nima-repeated-normal-eta-cycle (n : MariciNat)
  : nima-sum-equal NimaRepeatedNormalBasis
      (nima-repeated-normal-d (nima-repeated-normal-eta n))
      (nima-sum-zero NimaRepeatedNormalBasis)
  := nima-sum-add-inverse NimaRepeatedNormalBasis
       (nima-repeated-normal-column (nima-repeated-normal-branch-3,n))

#define nima-repeated-normal-excess-probe : NimaRepeatedNormalBasis -> MariciInt
  := \ (q,n) -> match q
       (nima-repeated-normal-base => marici-int-zero
       | nima-repeated-normal-branch-3 => marici-int-one
       | nima-repeated-normal-pair-3 => marici-int-zero)

#define nima-repeated-normal-column-excess-zero : (v : NimaRepeatedNormalBasis) ->
  nima-sum-eval NimaRepeatedNormalBasis nima-repeated-normal-excess-probe
    (nima-repeated-normal-column v) = marici-int-zero
  := \ (q,n) -> (match q into (\ k -> (n' : MariciNat) ->
       nima-sum-eval NimaRepeatedNormalBasis nima-repeated-normal-excess-probe
         (nima-repeated-normal-column (k,n')) = marici-int-zero) (
    nima-repeated-normal-base => \ n' -> refl
  | nima-repeated-normal-branch-3 => \ n' -> refl
  | nima-repeated-normal-pair-3 => \ n' -> refl
  )) n

#define nima-repeated-normal-boundary-excess-zero (p : NimaRepeatedNormal)
  : nima-sum-eval NimaRepeatedNormalBasis nima-repeated-normal-excess-probe
      (nima-repeated-normal-d p) = marici-int-zero
  := nima-frame-concat MariciInt
       (nima-sum-eval NimaRepeatedNormalBasis nima-repeated-normal-excess-probe
         (nima-repeated-normal-d p))
       (nima-sum-eval NimaRepeatedNormalBasis
         (\ v -> nima-sum-eval NimaRepeatedNormalBasis nima-repeated-normal-excess-probe
           (nima-repeated-normal-column v)) p)
       marici-int-zero
       (nima-sum-eval-bind NimaRepeatedNormalBasis NimaRepeatedNormalBasis
         nima-repeated-normal-column nima-repeated-normal-excess-probe p)
       (nima-any-eval-zero-atoms NimaRepeatedNormalBasis
         (\ v -> nima-sum-eval NimaRepeatedNormalBasis nima-repeated-normal-excess-probe
           (nima-repeated-normal-column v))
         nima-repeated-normal-column-excess-zero p)

#define nima-repeated-normal-eta-primitive-value (n : MariciNat)
  : nima-sum-eval NimaRepeatedNormalBasis nima-repeated-normal-excess-probe
      (nima-repeated-normal-eta n) = marici-int-one
  := refl

#define nima-repeated-normal-eta-not-boundary
  (n : MariciNat) (p : NimaRepeatedNormal)
  (boundary : nima-sum-equal NimaRepeatedNormalBasis
    (nima-repeated-normal-d p) (nima-repeated-normal-eta n))
  : marici-int-zero = marici-int-one
  := nima-frame-concat MariciInt marici-int-zero
       (nima-sum-eval NimaRepeatedNormalBasis nima-repeated-normal-excess-probe
         (nima-repeated-normal-d p)) marici-int-one
       (nima-frame-rev MariciInt
         (nima-sum-eval NimaRepeatedNormalBasis nima-repeated-normal-excess-probe
           (nima-repeated-normal-d p)) marici-int-zero
         (nima-repeated-normal-boundary-excess-zero p))
       (boundary nima-repeated-normal-excess-probe)
```
