# Three-carrier separation after fixed-beta specialization

The ordinary supported-Hom class, first-normal symbol, and X35-torsion class
live in different carriers.  This module exposes that typing directly: no
coercion between the three carriers is provided.

```rzk
#lang rzk-1

#data NimaD03ComparisonCarrier
  := nima-d03-ordinary-supported-carrier
  | nima-d03-first-normal-symbol-carrier
  | nima-d03-x35-torsion-carrier

#define NimaD03ComparisonDatum (carrier : NimaD03ComparisonCarrier) : U
  := match carrier
       (nima-d03-ordinary-supported-carrier => NimaD03SupportedCone
       | nima-d03-first-normal-symbol-carrier => NimaD03FirstNormalSymbol
       | nima-d03-x35-torsion-carrier => NimaX35Summand)

#define nima-d03-comparison-datum
  : (carrier : NimaD03ComparisonCarrier) -> NimaD03ComparisonDatum carrier
  := \ carrier -> match carrier
       (nima-d03-ordinary-supported-carrier => nima-d03-supported-primary
       | nima-d03-first-normal-symbol-carrier => nima-d03-first-normal-Z-symbol
       | nima-d03-x35-torsion-carrier => nima-x35-Z marici-zero)

#data NimaD03ComparisonStatus
  := nima-d03-status-ordinary-exact
  | nima-d03-status-first-symbol-primitive
  | nima-d03-status-x35-torsion-primitive

#define nima-d03-comparison-status
  : NimaD03ComparisonCarrier -> NimaD03ComparisonStatus
  := \ carrier -> match carrier
       (nima-d03-ordinary-supported-carrier => nima-d03-status-ordinary-exact
       | nima-d03-first-normal-symbol-carrier =>
          nima-d03-status-first-symbol-primitive
       | nima-d03-x35-torsion-carrier =>
          nima-d03-status-x35-torsion-primitive)

#define NimaD03ComparisonEvidence (carrier : NimaD03ComparisonCarrier) : U
  := match carrier
       (nima-d03-ordinary-supported-carrier =>
          NimaD03SupportedConeEqual nima-d03-supported-primary
            (nima-d03-supported-cone-d nima-d03-supported-primitive)
       | nima-d03-first-normal-symbol-carrier =>
          nima-d03-first-symbol-value nima-d03-first-normal-Z-symbol
            = marici-int-one
       | nima-d03-x35-torsion-carrier =>
          nima-sum-eval NimaX35SummandBasis nima-x35-bottom-probe
            (nima-x35-Z marici-zero) = marici-int-one)

#define nima-d03-comparison-evidence
  : (carrier : NimaD03ComparisonCarrier) -> NimaD03ComparisonEvidence carrier
  := \ carrier -> match carrier
       (nima-d03-ordinary-supported-carrier =>
          nima-d03-supported-primary-is-exact
       | nima-d03-first-normal-symbol-carrier =>
          nima-d03-first-symbol-is-primitive
       | nima-d03-x35-torsion-carrier => nima-x35-Z0-is-primitive)

#define NimaD03ThreeCarrierPacket : U
  := Sigma (_ : NimaD03ComparisonEvidence
       nima-d03-ordinary-supported-carrier),
     Sigma (_ : NimaD03ComparisonEvidence
       nima-d03-first-normal-symbol-carrier),
       NimaD03ComparisonEvidence nima-d03-x35-torsion-carrier

#define nima-d03-three-carrier-packet : NimaD03ThreeCarrierPacket
  := (nima-d03-supported-primary-is-exact,
      (nima-d03-first-symbol-is-primitive,nima-x35-Z0-is-primitive))

#define nima-d03-x35-torsion-action (n : MariciNat)
  : nima-sum-equal NimaX35SummandBasis
      (nima-x35-summand-d (nima-x35-upper n))
      (nima-sum-neg NimaX35SummandBasis (nima-x35-Z (marici-succ n)))
  := nima-x35-multiple-is-boundary n

#define nima-d03-x35-bottom-remains-nonboundary
  (p : NimaX35Summand)
  (boundary : nima-sum-equal NimaX35SummandBasis
    (nima-x35-summand-d p) (nima-x35-Z marici-zero))
  : marici-int-zero = marici-int-one
  := nima-x35-Z0-not-boundary p boundary
```
