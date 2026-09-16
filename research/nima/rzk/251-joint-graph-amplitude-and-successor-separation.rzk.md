# Joint-graph amplitude and successor separation

```rzk
#lang rzk-1

#define nima-correlated-response-graph
  (Source Regular Endpoint : U)
  (regular : Source -> Regular)
  (endpoint : Source -> Endpoint)
  : U
  := Sigma (source : Source),
       Sigma (_ : Regular), Endpoint

#define nima-correlated-response-point
  (Source Regular Endpoint : U)
  (regular : Source -> Regular)
  (endpoint : Source -> Endpoint)
  (x : Source)
  : nima-correlated-response-graph Source Regular Endpoint regular endpoint
  := (x, (regular x, endpoint x))

#define nima-correlated-response-source
  (Source Regular Endpoint : U)
  (regular : Source -> Regular)
  (endpoint : Source -> Endpoint)
  : nima-correlated-response-graph Source Regular Endpoint regular endpoint -> Source
  := \ x -> first x

#define nima-correlated-response-recovery
  (Source Regular Endpoint : U)
  (regular : Source -> Regular)
  (endpoint : Source -> Endpoint)
  (x : Source)
  : nima-correlated-response-source Source Regular Endpoint regular endpoint
      (nima-correlated-response-point Source Regular Endpoint regular endpoint x)
    = x
  := refl

#define nima-four-chart-system
  (Source V1 V2 V3 V4 : U)
  (S1 : Source -> V1)
  (S2 : Source -> V2)
  (S3 : Source -> V3)
  (S4 : Source -> V4)
  : U
  := Sigma (R1 : V1 -> Source),
       Sigma (R2 : V2 -> Source),
       Sigma (R3 : V3 -> Source),
       Sigma (R4 : V4 -> Source),
       Sigma (_ : (x : Source) -> R1 (S1 x) = x),
       Sigma (_ : (x : Source) -> R2 (S2 x) = x),
       Sigma (_ : (x : Source) -> R3 (S3 x) = x),
       ((x : Source) -> R4 (S4 x) = x)

#define nima-chart-comparison
  (Source Vi Vj : U)
  (Sj : Source -> Vj)
  (Ri : Vi -> Source)
  : Vi -> Vj
  := \ x -> Sj (Ri x)

#define nima-successor-chart-naturality
  (Source SourceNext Vi ViNext Vj VjNext : U)
  (Si : Source -> Vi)
  (Sj : Source -> Vj)
  (SiNext : SourceNext -> ViNext)
  (SjNext : SourceNext -> VjNext)
  (Ri : Vi -> Source)
  (RiNext : ViNext -> SourceNext)
  (successor : Source -> SourceNext)
  : U
  := (x : Vi) ->
       SjNext (successor (Ri x)) =
       nima-chart-comparison SourceNext ViNext VjNext SjNext RiNext
         (SiNext (successor (Ri x)))

#define nima-signed-feature-realization
  (Carrier Feature : U)
  (feature : Carrier -> Feature)
  (signature : Feature -> Feature)
  (readout : Carrier -> Carrier -> U)
  : U
  := (x y : Carrier) -> readout x y

#data NimaAnalyticalSystemEstablished
  := nima-regular-and-endpoint-channels-source-correlated
  | nima-source-retaining-joint-graph-recoverable
  | nima-complete-Hermitian-readout-on-joint-graph
  | nima-canonical-absolute-value-feature
  | nima-four-chart-strict-comparison-system
  | nima-order-four-chart-rotation
  | nima-cofinal-positive-pro-completion

#define nima-current-analytical-system-status
  : NimaAnalyticalSystemEstablished
  := nima-cofinal-positive-pro-completion

#data NimaAmplitudeCarrierChoice
  := nima-inherited-correlated-joint-graph-feature
  | nima-minimal-compressed-observer-feature
  | nima-terminal-scalar-readout

#define nima-current-physical-amplitude-carrier
  : NimaAmplitudeCarrierChoice
  := nima-minimal-compressed-observer-feature

#data NimaChartSuccessorSeparation
  := nima-chart-edge-changes-presentation-at-fixed-stage
  | nima-successor-edge-changes-stage-at-fixed-presentation
  | nima-successor-is-connection-natural
  | nima-successor-commutes-with-chart-rotation
  | nima-chart-rotation-is-not-Fourier-port-rotation

#define nima-current-chart-successor-separation
  : NimaChartSuccessorSeparation
  := nima-successor-commutes-with-chart-rotation

#data NimaAnalyticalForbiddenPromotion
  := nima-endpoint-channel-does-not-factor-through-regular-bulk
  | nima-joint-graph-does-not-canonically-split
  | nima-signed-compression-does-not-imply-absolute-Gram-compression
  | nima-pro-Hilbert-completion-does-not-imply-one-Hilbert-limit
  | nima-graph-trace-bound-does-not-imply-Green-energy-bound
  | nima-odd-return-does-not-determine-diagonal-loading
  | nima-terminal-scalar-readout-is-not-a-reversible-chart

#define nima-current-analytical-forbidden-promotion
  : NimaAnalyticalForbiddenPromotion
  := nima-endpoint-channel-does-not-factor-through-regular-bulk
```
