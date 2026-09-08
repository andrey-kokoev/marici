# Beta endpoint-Q transgression

This module records the forced endpoint/Q compatibility and the distinction
between ordinary and strict-endpoint short-boundary homology.

```rzk
#lang rzk-1

#data NimaBetaTopCycleDirection
  := nima-beta-top-negative-endpoint
  | nima-beta-top-positive-endpoint
#data NimaBetaQProjectionOrder
  := nima-beta-q-order-two
  | nima-beta-q-projection-zero
#data NimaBetaEndpointLeadingCoordinate
  := nima-beta-leading-negative-endpoint
  | nima-beta-leading-positive-endpoint

#define nima-beta-top-endpoint-signature
  : NimaBetaTopCycleDirection -> NimaBetaEndpointLeadingCoordinate
  := \ direction -> match direction
       (nima-beta-top-negative-endpoint => nima-beta-leading-negative-endpoint
       | nima-beta-top-positive-endpoint => nima-beta-leading-positive-endpoint)
#define nima-beta-top-q-order
  : NimaBetaTopCycleDirection -> NimaBetaQProjectionOrder
  := \ direction -> match direction
       (nima-beta-top-negative-endpoint => nima-beta-q-order-two
       | nima-beta-top-positive-endpoint => nima-beta-q-projection-zero)

#data NimaBeta2AttachmentState
  := nima-beta2-attachment-chi
  | nima-beta2-attachment-primitive-W
#define NimaBeta2AttachmentBasis : U
  := Sigma (_ : NimaBeta2AttachmentState), MariciNat
#define NimaBeta2Attachment : U := NimaZSum NimaBeta2AttachmentBasis

#define nima-beta2-attachment-column
  : NimaBeta2AttachmentBasis -> NimaBeta2Attachment
  := \ (q,n) -> match q
       (nima-beta2-attachment-chi => nima-sum-zero NimaBeta2AttachmentBasis
       | nima-beta2-attachment-primitive-W =>
          nima-sum-atom NimaBeta2AttachmentBasis
            (nima-beta2-attachment-chi,marici-succ (marici-succ n)))
#define nima-beta2-attachment-d : NimaBeta2Attachment -> NimaBeta2Attachment
  := nima-sum-bind NimaBeta2AttachmentBasis NimaBeta2AttachmentBasis
       nima-beta2-attachment-column
#define nima-beta2-chi (n : MariciNat) : NimaBeta2Attachment
  := nima-sum-atom NimaBeta2AttachmentBasis (nima-beta2-attachment-chi,n)
#define nima-beta2-W (n : MariciNat) : NimaBeta2Attachment
  := nima-sum-atom NimaBeta2AttachmentBasis
       (nima-beta2-attachment-primitive-W,n)

#define nima-beta-square-kills-chi (n : MariciNat)
  : nima-sum-equal NimaBeta2AttachmentBasis
      (nima-beta2-attachment-d (nima-beta2-W n))
      (nima-beta2-chi (marici-succ (marici-succ n)))
  := \ probe -> refl

#define nima-beta-chi-probe : NimaBeta2AttachmentBasis -> MariciInt
  := \ (q,n) -> match q
       (nima-beta2-attachment-chi => match n
          (marici-zero => marici-int-zero
          | marici-succ k ih => match k
             (marici-zero => marici-int-one
             | marici-succ j ij => marici-int-zero))
       | nima-beta2-attachment-primitive-W => marici-int-zero)
#define nima-beta-chi-is-primitive
  : nima-sum-eval NimaBeta2AttachmentBasis nima-beta-chi-probe
      (nima-beta2-chi (marici-succ marici-zero)) = marici-int-one
  := refl

#define nima-beta2-column-probe-zero : (v : NimaBeta2AttachmentBasis) ->
  nima-sum-eval NimaBeta2AttachmentBasis nima-beta-chi-probe
    (nima-beta2-attachment-column v) = marici-int-zero
  := \ (q,n) -> (match q into (\ k -> (n' : MariciNat) ->
       nima-sum-eval NimaBeta2AttachmentBasis nima-beta-chi-probe
         (nima-beta2-attachment-column (k,n')) = marici-int-zero) (
    nima-beta2-attachment-chi => \ n' -> refl
  | nima-beta2-attachment-primitive-W => \ n' -> refl
  )) n

#define nima-beta-chi-lower-obstruction-not-boundary
  (p : NimaBeta2Attachment)
  (boundary : nima-sum-equal NimaBeta2AttachmentBasis
    (nima-beta2-attachment-d p)
    (nima-beta2-chi (marici-succ marici-zero)))
  : marici-int-zero = marici-int-one
  := nima-frame-concat MariciInt marici-int-zero
       (nima-sum-eval NimaBeta2AttachmentBasis nima-beta-chi-probe
         (nima-beta2-attachment-d p)) marici-int-one
       (nima-frame-rev MariciInt
         (nima-sum-eval NimaBeta2AttachmentBasis nima-beta-chi-probe
           (nima-beta2-attachment-d p)) marici-int-zero
         (nima-frame-concat MariciInt
          (nima-sum-eval NimaBeta2AttachmentBasis nima-beta-chi-probe
            (nima-beta2-attachment-d p))
          (nima-sum-eval NimaBeta2AttachmentBasis
            (\ v -> nima-sum-eval NimaBeta2AttachmentBasis nima-beta-chi-probe
              (nima-beta2-attachment-column v)) p)
          marici-int-zero
          (nima-sum-eval-bind NimaBeta2AttachmentBasis NimaBeta2AttachmentBasis
            nima-beta2-attachment-column nima-beta-chi-probe p)
          (nima-any-eval-zero-atoms NimaBeta2AttachmentBasis
            (\ v -> nima-sum-eval NimaBeta2AttachmentBasis nima-beta-chi-probe
              (nima-beta2-attachment-column v))
            nima-beta2-column-probe-zero p)))
       (boundary nima-beta-chi-probe)

#data NimaEndpointFramingMode
  := nima-endpoint-framing-ordinary
  | nima-endpoint-framing-strict
#data NimaChiAnnihilatorStatus
  := nima-chi-annihilator-beta-square
  | nima-chi-annihilator-faithful
#define nima-chi-annihilator-status
  : NimaEndpointFramingMode -> NimaChiAnnihilatorStatus
  := \ framing -> match framing
       (nima-endpoint-framing-ordinary => nima-chi-annihilator-beta-square
       | nima-endpoint-framing-strict => nima-chi-annihilator-faithful)
```
