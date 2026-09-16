# Selected incoming--outgoing scattering amplitude

```rzk
#lang rzk-1

#define nima-scattering-amplitude
  (Incoming Outgoing Carrier Scalars : U)
  (incoming-state : Incoming -> Carrier)
  (outgoing-state : Outgoing -> Carrier)
  (operator-pairing : Carrier -> Carrier -> Scalars)
  : Incoming -> Outgoing -> Scalars
  := \ x y -> operator-pairing (outgoing-state y) (incoming-state x)

#define nima-selected-scattering-amplitude
  (Incoming Outgoing Carrier Scalars : U)
  (incoming-state : Incoming -> Carrier)
  (outgoing-state : Outgoing -> Carrier)
  (operator-pairing : Carrier -> Carrier -> Scalars)
  (selected-incoming : Incoming)
  (selected-outgoing : Outgoing)
  : Scalars
  := nima-scattering-amplitude Incoming Outgoing Carrier Scalars
       incoming-state outgoing-state operator-pairing
       selected-incoming selected-outgoing

#define nima-feature-scattering-amplitude
  (Incoming Outgoing Carrier Feature Scalars : U)
  (incoming-state : Incoming -> Carrier)
  (outgoing-state : Outgoing -> Carrier)
  (feature : Carrier -> Feature)
  (signed-pairing : Feature -> Feature -> Scalars)
  : Incoming -> Outgoing -> Scalars
  := \ x y -> signed-pairing
       (feature (outgoing-state y))
       (feature (incoming-state x))

#define nima-scattering-feature-realization
  (Incoming Outgoing Carrier Feature Scalars : U)
  (incoming-state : Incoming -> Carrier)
  (outgoing-state : Outgoing -> Carrier)
  (operator-pairing : Carrier -> Carrier -> Scalars)
  (feature : Carrier -> Feature)
  (signed-pairing : Feature -> Feature -> Scalars)
  (realization : (x y : Carrier) ->
    operator-pairing x y = signed-pairing (feature x) (feature y))
  (x : Incoming)
  (y : Outgoing)
  : nima-scattering-amplitude Incoming Outgoing Carrier Scalars
      incoming-state outgoing-state operator-pairing x y
    = nima-feature-scattering-amplitude Incoming Outgoing Carrier Feature
      Scalars incoming-state outgoing-state feature signed-pairing x y
  := realization (outgoing-state y) (incoming-state x)

#define nima-two-to-three-amplitude
  (TwoParticle ThreeParticle Carrier Scalars : U)
  (two-particle-in : TwoParticle -> Carrier)
  (three-particle-out : ThreeParticle -> Carrier)
  (operator-pairing : Carrier -> Carrier -> Scalars)
  : TwoParticle -> ThreeParticle -> Scalars
  := nima-scattering-amplitude TwoParticle ThreeParticle Carrier Scalars
       two-particle-in three-particle-out operator-pairing

#define nima-chart-scattering-amplitude
  (Incoming Outgoing Chart Scalars : U)
  (incoming-chart : Incoming -> Chart)
  (outgoing-chart : Outgoing -> Chart)
  (chart-pairing : Chart -> Chart -> Scalars)
  : Incoming -> Outgoing -> Scalars
  := \ x y -> chart-pairing (outgoing-chart y) (incoming-chart x)

#define nima-scattering-chart-independence
  (Incoming Outgoing ChartI ChartJ Scalars : U)
  (incomingI : Incoming -> ChartI)
  (outgoingI : Outgoing -> ChartI)
  (incomingJ : Incoming -> ChartJ)
  (outgoingJ : Outgoing -> ChartJ)
  (pairingI : ChartI -> ChartI -> Scalars)
  (pairingJ : ChartJ -> ChartJ -> Scalars)
  : U
  := (x : Incoming) -> (y : Outgoing) ->
       nima-chart-scattering-amplitude Incoming Outgoing ChartI Scalars
         incomingI outgoingI pairingI x y
       = nima-chart-scattering-amplitude Incoming Outgoing ChartJ Scalars
         incomingJ outgoingJ pairingJ x y

#define nima-normalized-selected-scattering-amplitude
  (Incoming Outgoing Carrier Scalars : U)
  (incoming-state : Incoming -> Carrier)
  (outgoing-state : Outgoing -> Carrier)
  (operator-pairing : Carrier -> Carrier -> Scalars)
  (selected-incoming : Incoming)
  (selected-outgoing : Outgoing)
  (normalization : Scalars)
  : U
  := nima-selected-scattering-amplitude Incoming Outgoing Carrier Scalars
       incoming-state outgoing-state operator-pairing
       selected-incoming selected-outgoing
     = normalization

#data NimaAmplitudeScalarizationDecision
  := nima-selected-incoming-outgoing-matrix-coefficient
  | nima-diagonal-evaluation-not-selected
  | nima-terminal-readout-not-selected

#define nima-current-amplitude-scalarization-decision
  : NimaAmplitudeScalarizationDecision
  := nima-selected-incoming-outgoing-matrix-coefficient

#data NimaTwoToThreeAmplitudePlacement
  := nima-two-particle-incoming-sector
  | nima-three-particle-outgoing-sector
  | nima-successor-between-multiplicity-sectors
  | nima-chartwise-representatives-of-one-transition
  | nima-not-a-horizontal-presentation-edge

#define nima-current-two-to-three-amplitude-placement
  : NimaTwoToThreeAmplitudePlacement
  := nima-successor-between-multiplicity-sectors

#data NimaSelectedScatteringAmplitudeGate
  := nima-select-incoming-state-map
  | nima-select-outgoing-state-map
  | nima-prove-chart-independence
  | nima-supply-physical-normalization
  | nima-prove-gluing-factorization

#define nima-first-selected-scattering-amplitude-gate
  : NimaSelectedScatteringAmplitudeGate
  := nima-select-incoming-state-map
```
