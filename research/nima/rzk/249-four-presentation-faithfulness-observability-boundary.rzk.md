# Four-presentation faithfulness and observability boundary

```rzk
#lang rzk-1

#define nima-retraction
  (Source Presentation : U)
  (present : Source -> Presentation)
  : U
  := Sigma (recover : Presentation -> Source),
       ((x : Source) -> recover (present x) = x)

#define nima-presentation-injective
  (Source Presentation : U)
  (present : Source -> Presentation)
  : U
  := (x y : Source) -> (present x = present y) -> (x = y)

#define nima-joint-presentation-shadow
  (Source V2 V3 V4 : U)
  (C12 : Source -> V2)
  (C13 : Source -> V3)
  (q4 : Source -> V4)
  : Source -> Sigma (_ : V2), Sigma (_ : V3), V4
  := \ x -> (C12 x, (C13 x, q4 x))

#define nima-fourier-saturated-presentation
  (V D : U)
  : U
  := Sigma (_ : V), D

#define nima-lift-presentation-edge
  (Vi Vj D : U)
  (Cij : Vi -> Vj)
  : nima-fourier-saturated-presentation Vi D ->
    nima-fourier-saturated-presentation Vj D
  := \ x -> (Cij (first x), second x)

#define nima-lift-quarter-turn
  (V D : U)
  (F : D -> D)
  : nima-fourier-saturated-presentation V D ->
    nima-fourier-saturated-presentation V D
  := \ x -> (first x, F (second x))

#define nima-product-quarter-turn-naturality
  (Vi Vj D : U)
  (Cij : Vi -> Vj)
  (F : D -> D)
  (x : nima-fourier-saturated-presentation Vi D)
  : nima-lift-quarter-turn Vj D F
      (nima-lift-presentation-edge Vi Vj D Cij x)
    = nima-lift-presentation-edge Vi Vj D Cij
      (nima-lift-quarter-turn Vi D F x)
  := refl

#data NimaFourPresentationEstablished
  := nima-C13-retraction-gives-joint-faithfulness
  | nima-complete-four-port-pro-record-is-monic
  | nima-C41-algebraic-on-observer-image
  | nima-three-reciprocal-half-turn-squares
  | nima-product-quarter-turn-naturality-established
  | nima-character-diagonal-finite-fiber-classification
  | nima-source-derived-semilocal-Tate-quarter-turn
  | nima-all-seam-response-has-analytic-C41
  | nima-response-graph-is-maximal-isotropic

#define nima-highest-four-presentation-established
  : NimaFourPresentationEstablished
  := nima-response-graph-is-maximal-isotropic

#data NimaFourPresentationOpenGate
  := nima-uniform-four-port-observability-bound-missing
  | nima-inherited-topology-C41-continuity-missing
  | nima-uniform-tail-coercive-augmentation-missing
  | nima-old-scalar-chart-character-edge-coefficients-missing
  | nima-Evans-trace-response-graph-membership-missing
  | nima-prime-cell-four-matrix-unit-equality-missing

#define nima-current-four-presentation-open-gate
  : NimaFourPresentationOpenGate
  := nima-prime-cell-four-matrix-unit-equality-missing

#data NimaFourPresentationForbiddenPromotion
  := nima-pro-faithfulness-does-not-imply-bounded-recovery
  | nima-algebraic-inverse-does-not-imply-continuous-inverse
  | nima-product-quarter-turn-does-not-imply-nontrivial-coupling
  | nima-scalar-Weil-readout-is-not-conservative
  | nima-complete-four-port-is-not-definitionally-history-cycle-image

#define nima-current-four-presentation-forbidden-promotion
  : NimaFourPresentationForbiddenPromotion
  := nima-pro-faithfulness-does-not-imply-bounded-recovery
```
