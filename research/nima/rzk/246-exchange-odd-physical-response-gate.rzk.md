# Exchange-odd physical response and filtered-lowering gate

```rzk
#lang rzk-1

#define nima-mixed-occurrence-covector (Scalars : U) : U
  := Sigma (_ : Scalars), Scalars

#define nima-canonical-even-mixed-covector (Scalars : U) (one : Scalars)
  : nima-mixed-occurrence-covector Scalars
  := (one, one)

#define nima-shape-odd-mixed-covector
  (Scalars : U) (one : Scalars) (negate : Scalars -> Scalars)
  : nima-mixed-occurrence-covector Scalars
  := (one, negate one)

#define nima-valg-projection
  (Scalars : U)
  (add multiply : Scalars -> Scalars -> Scalars)
  (negate : Scalars -> Scalars)
  (v : Scalars)
  : nima-mixed-occurrence-covector Scalars -> Scalars
  := \ weights -> add
       (multiply (first weights) (negate v))
       (multiply (second weights) v)

#define nima-even-physical-valg-cancellation
  (Scalars : U)
  (add multiply : Scalars -> Scalars -> Scalars)
  (negate : Scalars -> Scalars)
  (zero one v : Scalars)
  (canonical-cancellation : add
     (multiply one (negate v)) (multiply one v) = zero)
  : nima-valg-projection Scalars add multiply negate v
      (nima-canonical-even-mixed-covector Scalars one) = zero
  := canonical-cancellation

#define nima-global-GM-IBP-reduction-certificate
  (FullShapeJet SimpleMixed : U)
  (Horizontal : FullShapeJet -> U)
  (RelativeExact : SimpleMixed -> U)
  (Integral : SimpleMixed -> U)
  : U
  := Sigma (reduce : FullShapeJet -> SimpleMixed),
       Sigma (_ : (jet : FullShapeJet) -> Horizontal jet),
       Sigma (_ : (jet : FullShapeJet) -> RelativeExact (reduce jet)),
       ((jet : FullShapeJet) -> Integral (reduce jet))

#data NimaPhysicalResponseEmpty

#define nima-nonzero-odd-projection-after-global-reduction
  (FullShapeJet SimpleMixed Scalars : U)
  (reduce : FullShapeJet -> SimpleMixed)
  (shapeJet : FullShapeJet)
  (project : SimpleMixed -> Scalars)
  (zero : Scalars)
  : U
  := (project (reduce shapeJet) = zero) -> NimaPhysicalResponseEmpty

#data NimaC4FilteredCospanStatus
  := nima-log-image-rank-three
  | nima-cut-image-rank-three
  | nima-common-e6-line-rank-one
  | nima-integral-top-leg-has-index-two
  | nima-filtered-cospan-is-algebraic-not-yet-ringed

#define nima-current-C4-cospan-scope : NimaC4FilteredCospanStatus
  := nima-filtered-cospan-is-algebraic-not-yet-ringed

#data NimaPhysicalMixedDetectorStatus
  := nima-canonical-even-residue-kills-valg
  | nima-top-Leray-boundary-odd-but-physical-pairing-even
  | nima-fixed-coordinate-shape-response-is-odd
  | nima-wall-horizontal-lift-kills-doubled-pole-response
  | nima-direct-C15b-doubled-wall-claim-withdrawn
  | nima-full-contact-weighted-shape-jet-remains
  | nima-global-GM-IBP-simple-residue-reduction-is-missing
  | nima-physical-valg-detector-remains-conditional

#define nima-current-physical-mixed-detector-status
  : NimaPhysicalMixedDetectorStatus
  := nima-global-GM-IBP-simple-residue-reduction-is-missing

#data NimaGlobalShapeReductionAcceptanceGate
  := nima-use-full-contact-weighted-six-term-shape-jet
  | nima-use-wall-horizontal-Gauss-Manin-lift
  | nima-reduce-by-IBP-to-simple-mixed-residues
  | nima-preserve-relative-source-cycle
  | nima-preserve-integral-Betti-lattice
  | nima-project-nontrivially-to-g101-minus-g110

#define nima-first-global-shape-reduction-gate
  : NimaGlobalShapeReductionAcceptanceGate
  := nima-use-full-contact-weighted-six-term-shape-jet

#data NimaEndpointComparisonCorrection
  := nima-formal-identity-is-unique-unimodular-candidate
  | nima-sourced-coordinate-induces-label-swap
  | nima-old-weight-three-gap-is-withdrawn
  | nima-endpoint-ratio-is-not-constant
  | nima-genuine-Gauss-Manin-transport-is-required

#define nima-current-endpoint-comparison-correction
  : NimaEndpointComparisonCorrection
  := nima-genuine-Gauss-Manin-transport-is-required
```
