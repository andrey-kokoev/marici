# Joint-graph operator amplitude bridge

```rzk
#lang rzk-1

#define nima-operator-amplitude
  (Filling Scalars : U)
  (operator-pairing : Filling -> Filling -> Scalars)
  : Filling -> Filling -> Scalars
  := operator-pairing

#define nima-feature-amplitude
  (Filling Feature Scalars : U)
  (feature : Filling -> Feature)
  (signed-pairing : Feature -> Feature -> Scalars)
  : Filling -> Filling -> Scalars
  := \ x y -> signed-pairing (feature x) (feature y)

#define nima-operator-feature-realization
  (Filling Feature Scalars : U)
  (operator-pairing : Filling -> Filling -> Scalars)
  (feature : Filling -> Feature)
  (signed-pairing : Feature -> Feature -> Scalars)
  : U
  := (x y : Filling) ->
       operator-pairing x y = signed-pairing (feature x) (feature y)

#define nima-selected-state-amplitude
  (Filling Scalars : U)
  (operator-pairing : Filling -> Filling -> Scalars)
  (selected-state : Filling)
  : Filling -> Scalars
  := \ x -> operator-pairing selected-state x

#define nima-diagonal-amplitude
  (Filling Scalars : U)
  (operator-pairing : Filling -> Filling -> Scalars)
  : Filling -> Scalars
  := \ x -> operator-pairing x x

#define nima-readout-amplitude
  (Filling Physical Scalars : U)
  (physical-observation : Filling -> Physical)
  (readout : Physical -> Scalars)
  : Filling -> Scalars
  := \ x -> readout (physical-observation x)

#define nima-chart-transported-pairing
  (Source Chart Scalars : U)
  (recover : Chart -> Source)
  (source-pairing : Source -> Source -> Scalars)
  : Chart -> Chart -> Scalars
  := \ x y -> source-pairing (recover x) (recover y)

#define nima-chart-comparison-preserves-pairing
  (Source ChartI ChartJ Scalars : U)
  (recoverI : ChartI -> Source)
  (recoverJ : ChartJ -> Source)
  (compare : ChartI -> ChartJ)
  (source-pairing : Source -> Source -> Scalars)
  : U
  := (x y : ChartI) ->
       nima-chart-transported-pairing Source ChartJ Scalars recoverJ
         source-pairing (compare x) (compare y)
       = nima-chart-transported-pairing Source ChartI Scalars recoverI
         source-pairing x y

#define nima-amplitude-gluing-law
  (Filling Scalars : U)
  (amplitude : Filling -> Scalars)
  (glue : Filling -> Filling -> Filling)
  (multiply : Scalars -> Scalars -> Scalars)
  : U
  := (x y : Filling) ->
       amplitude (glue x y) = multiply (amplitude x) (amplitude y)

#define nima-amplitude-unit-law
  (Filling Scalars : U)
  (amplitude : Filling -> Scalars)
  (unit-filling : Filling)
  (one : Scalars)
  : U
  := amplitude unit-filling = one

#define nima-joint-graph-amplitude-interface
  (Filling Feature Scalars : U)
  (operator-pairing : Filling -> Filling -> Scalars)
  (feature : Filling -> Feature)
  (signed-pairing : Feature -> Feature -> Scalars)
  : U
  := Sigma (_ : nima-operator-feature-realization Filling Feature Scalars
       operator-pairing feature signed-pairing),
       Filling -> Scalars

#define nima-joint-graph-amplitude-point
  (Filling Feature Scalars : U)
  (operator-pairing : Filling -> Filling -> Scalars)
  (feature : Filling -> Feature)
  (signed-pairing : Feature -> Feature -> Scalars)
  (realization : nima-operator-feature-realization Filling Feature Scalars
    operator-pairing feature signed-pairing)
  (amplitude : Filling -> Scalars)
  : nima-joint-graph-amplitude-interface Filling Feature Scalars
      operator-pairing feature signed-pairing
  := (realization, amplitude)

#data NimaJointGraphAmplitudeEstablished
  := nima-source-reached-physical-carrier-available
  | nima-bounded-self-adjoint-observer-operator-available
  | nima-minimal-signed-feature-available
  | nima-bilinear-operator-amplitude-available
  | nima-four-chart-pairing-transport-available

#define nima-current-joint-graph-amplitude-status
  : NimaJointGraphAmplitudeEstablished
  := nima-four-chart-pairing-transport-available

#data NimaScalarAmplitudeChoice
  := nima-selected-state-matrix-coefficient
  | nima-diagonal-quadratic-evaluation
  | nima-terminal-supported-readout
  | nima-no-canonical-choice-yet

#define nima-current-scalar-amplitude-choice : NimaScalarAmplitudeChoice
  := nima-no-canonical-choice-yet

#data NimaAmplitudeCompletionGate
  := nima-select-scalarization
  | nima-declare-unit-filling
  | nima-declare-gluing-operation
  | nima-prove-unit-normalization
  | nima-prove-gluing-factorization
  | nima-prove-symmetry-covariance
  | nima-inhabit-certified-amplitude-package

#define nima-first-amplitude-completion-gate : NimaAmplitudeCompletionGate
  := nima-select-scalarization

#data NimaAmplitudeForbiddenPromotion
  := nima-bilinear-form-does-not-select-one-input-amplitude
  | nima-feature-factorization-does-not-imply-gluing-factorization
  | nima-chart-invariance-does-not-imply-unit-normalization
  | nima-terminal-readout-does-not-become-reversible

#define nima-current-amplitude-forbidden-promotion
  : NimaAmplitudeForbiddenPromotion
  := nima-bilinear-form-does-not-select-one-input-amplitude
```
