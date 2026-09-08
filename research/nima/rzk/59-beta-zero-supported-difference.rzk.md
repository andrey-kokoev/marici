# Beta-zero supported-map difference

This packet realizes the two independent annihilators of the endpoint-detected
map difference.  Its bottom class is killed by beta and X35, while the existing
Z packet remains only X35-torsion.

```rzk
#lang rzk-1

#define NimaBetaX35Monomial : U := Sigma (_ : MariciNat), MariciNat
#data NimaBetaDifferenceState
  := nima-beta-difference-bottom
  | nima-beta-difference-beta-homotopy
  | nima-beta-difference-x35-homotopy
#define NimaBetaDifferenceBasis : U
  := Sigma (_ : NimaBetaDifferenceState), NimaBetaX35Monomial
#define NimaBetaDifference : U := NimaZSum NimaBetaDifferenceBasis

#define nima-beta-difference-column
  : NimaBetaDifferenceBasis -> NimaBetaDifference
  := \ (q,(b,x)) -> match q
       (nima-beta-difference-bottom => nima-sum-zero NimaBetaDifferenceBasis
       | nima-beta-difference-beta-homotopy =>
          nima-sum-atom NimaBetaDifferenceBasis
            (nima-beta-difference-bottom,(marici-succ b,x))
       | nima-beta-difference-x35-homotopy =>
          nima-sum-atom NimaBetaDifferenceBasis
            (nima-beta-difference-bottom,(b,marici-succ x)))
#define nima-beta-difference-d : NimaBetaDifference -> NimaBetaDifference
  := nima-sum-bind NimaBetaDifferenceBasis NimaBetaDifferenceBasis
       nima-beta-difference-column

#define nima-beta-difference-class (b x : MariciNat) : NimaBetaDifference
  := nima-sum-atom NimaBetaDifferenceBasis
       (nima-beta-difference-bottom,(b,x))

#define nima-beta-multiple-is-boundary (b x : MariciNat)
  : nima-sum-equal NimaBetaDifferenceBasis
      (nima-beta-difference-d
        (nima-sum-atom NimaBetaDifferenceBasis
          (nima-beta-difference-beta-homotopy,(b,x))))
      (nima-beta-difference-class (marici-succ b) x)
  := \ probe -> refl
#define nima-beta-difference-x35-multiple-is-boundary (b x : MariciNat)
  : nima-sum-equal NimaBetaDifferenceBasis
      (nima-beta-difference-d
        (nima-sum-atom NimaBetaDifferenceBasis
          (nima-beta-difference-x35-homotopy,(b,x))))
      (nima-beta-difference-class b (marici-succ x))
  := \ probe -> refl

#define nima-beta-difference-origin-probe
  : NimaBetaDifferenceBasis -> MariciInt
  := \ (q,(b,x)) -> match q
       (nima-beta-difference-bottom => match b
          (marici-zero => match x
             (marici-zero => marici-int-one
             | marici-succ k ih => marici-int-zero)
          | marici-succ k ih => marici-int-zero)
       | nima-beta-difference-beta-homotopy => marici-int-zero
       | nima-beta-difference-x35-homotopy => marici-int-zero)

#define nima-beta-difference-column-origin-zero
  : (v : NimaBetaDifferenceBasis) ->
    nima-sum-eval NimaBetaDifferenceBasis nima-beta-difference-origin-probe
      (nima-beta-difference-column v) = marici-int-zero
  := \ (q,(b,x)) -> (match q into (\ k -> (b' : MariciNat) ->
       (x' : MariciNat) ->
       nima-sum-eval NimaBetaDifferenceBasis nima-beta-difference-origin-probe
         (nima-beta-difference-column (k,(b',x'))) = marici-int-zero) (
    nima-beta-difference-bottom => \ b' x' -> refl
  | nima-beta-difference-beta-homotopy => \ b' x' -> refl
  | nima-beta-difference-x35-homotopy => \ b' -> match b'
      (marici-zero => \ x' -> refl
      | marici-succ k ih => \ x' -> refl)
  )) b x

#define nima-beta-difference-boundary-origin-zero (p : NimaBetaDifference)
  : nima-sum-eval NimaBetaDifferenceBasis nima-beta-difference-origin-probe
      (nima-beta-difference-d p) = marici-int-zero
  := nima-frame-concat MariciInt
       (nima-sum-eval NimaBetaDifferenceBasis nima-beta-difference-origin-probe
         (nima-beta-difference-d p))
       (nima-sum-eval NimaBetaDifferenceBasis
         (\ v -> nima-sum-eval NimaBetaDifferenceBasis
           nima-beta-difference-origin-probe (nima-beta-difference-column v)) p)
       marici-int-zero
       (nima-sum-eval-bind NimaBetaDifferenceBasis NimaBetaDifferenceBasis
         nima-beta-difference-column nima-beta-difference-origin-probe p)
       (nima-any-eval-zero-atoms NimaBetaDifferenceBasis
         (\ v -> nima-sum-eval NimaBetaDifferenceBasis
           nima-beta-difference-origin-probe (nima-beta-difference-column v))
         nima-beta-difference-column-origin-zero p)

#define nima-beta-difference-origin-is-primitive
  : nima-sum-eval NimaBetaDifferenceBasis nima-beta-difference-origin-probe
      (nima-beta-difference-class marici-zero marici-zero) = marici-int-one
  := refl

#define nima-beta-difference-origin-not-boundary
  (p : NimaBetaDifference)
  (boundary : nima-sum-equal NimaBetaDifferenceBasis
    (nima-beta-difference-d p)
    (nima-beta-difference-class marici-zero marici-zero))
  : marici-int-zero = marici-int-one
  := nima-frame-concat MariciInt marici-int-zero
       (nima-sum-eval NimaBetaDifferenceBasis nima-beta-difference-origin-probe
         (nima-beta-difference-d p)) marici-int-one
       (nima-frame-rev MariciInt
         (nima-sum-eval NimaBetaDifferenceBasis nima-beta-difference-origin-probe
           (nima-beta-difference-d p)) marici-int-zero
         (nima-beta-difference-boundary-origin-zero p))
       (boundary nima-beta-difference-origin-probe)

#data NimaBetaZeroClassKind
  := nima-beta-zero-primary-beta-torsion
  | nima-beta-zero-Z-x35-torsion
  | nima-beta-zero-map-difference-beta-x35-torsion
```
