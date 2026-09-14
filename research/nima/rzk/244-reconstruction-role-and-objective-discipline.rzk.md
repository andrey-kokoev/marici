# Reconstruction-role and objective discipline

```rzk
#lang rzk-1

#data NimaReconstructionObjective
  := nima-quotient-objective
  | nima-source-objective
  | nima-product-objective

#data NimaConstructorRole
  := nima-coherent-descent-role
  | nima-essential-bulk-observer-role
  | nima-finite-defect-repair-role
  | nima-relational-moduli-observer-role
  | nima-ringed-support-correspondence-role

#define nima-role-indexed-constructor (Role : NimaConstructorRole) (Carrier : U) : U
  := Sigma (_ : Carrier), Role = Role

#define nima-objective-indexed-certificate
  (Objective : NimaReconstructionObjective)
  (Evidence : U)
  : U
  := Sigma (_ : Evidence), Objective = Objective

#define nima-descent-constructor (Carrier : U) : U
  := nima-role-indexed-constructor nima-coherent-descent-role Carrier

#define nima-essential-constructor (Carrier : U) : U
  := nima-role-indexed-constructor nima-essential-bulk-observer-role Carrier

#define nima-finite-repair-constructor (Carrier : U) : U
  := nima-role-indexed-constructor nima-finite-defect-repair-role Carrier

#define nima-moduli-constructor (Carrier : U) : U
  := nima-role-indexed-constructor nima-relational-moduli-observer-role Carrier

#define nima-ringed-support-constructor (Carrier : U) : U
  := nima-role-indexed-constructor nima-ringed-support-correspondence-role Carrier

#define nima-source-reconstruction-input
  (Descent Essential Repair : U)
  : U
  := Sigma (_ : nima-descent-constructor Descent),
       Sigma (_ : nima-essential-constructor Essential),
       nima-finite-repair-constructor Repair

#define nima-product-reconstruction-input
  (SourceEvidence Moduli : U)
  : U
  := Sigma
       (_ : nima-objective-indexed-certificate nima-source-objective SourceEvidence),
       nima-moduli-constructor Moduli

#define nima-certified-source-assembly
  (Descent Essential Repair StabilityEvidence : U)
  (inputs : nima-source-reconstruction-input Descent Essential Repair)
  (stability : StabilityEvidence)
  : nima-objective-indexed-certificate nima-source-objective
      (Sigma (_ : nima-source-reconstruction-input Descent Essential Repair), StabilityEvidence)
  := ((inputs, stability), refl)

#define nima-certified-product-assembly
  (SourceEvidence Moduli ProductMetricEvidence ProductStabilityEvidence : U)
  (inputs : nima-product-reconstruction-input SourceEvidence Moduli)
  (metric : ProductMetricEvidence)
  (stability : ProductStabilityEvidence)
  : nima-objective-indexed-certificate nima-product-objective
      (Sigma (_ : nima-product-reconstruction-input SourceEvidence Moduli),
       Sigma (_ : ProductMetricEvidence), ProductStabilityEvidence)
  := ((inputs, (metric, stability)), refl)

#data NimaTypingGateOrder
  := nima-gate-source-and-target
  | nima-gate-arity-and-variance
  | nima-gate-support-and-labels
  | nima-gate-required-cells
  | nima-gate-numeric-equality

#define nima-first-geometric-connector-gate : NimaTypingGateOrder
  := nima-gate-source-and-target

#data NimaForbiddenPromotion
  := nima-descent-is-not-essential-observation
  | nima-quotient-is-not-source-reconstruction
  | nima-finite-repair-is-not-essential-observation
  | nima-moduli-readout-is-not-bulk-coercivity
  | nima-scalar-equality-is-not-constructor-equality
  | nima-cellular-comparison-is-not-ringed-support-correspondence
  | nima-coefficient-witness-is-not-geometric-realization

#define nima-current-connector-forbidden-promotion : NimaForbiddenPromotion
  := nima-coefficient-witness-is-not-geometric-realization

#data NimaConnectorObjectiveStatus
  := nima-coefficient-objective-inhabited
  | nima-quotient-objective-not-yet-exported-from-six-functors
  | nima-source-objective-blocked-by-ringed-support-map
  | nima-product-objective-premature

#define nima-current-connector-objective-status : NimaConnectorObjectiveStatus
  := nima-source-objective-blocked-by-ringed-support-map
```
