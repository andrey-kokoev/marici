# Derived normalization, duality, and dilation

```rzk
#lang rzk-1
#data NimaDerivedNormalizationComparison
  := nima-total-conductor-kernel-quasi-isomorphism
  | nima-explicit-integral-kernel-contraction
  | nima-intermediate-normalization-diagrams-not-equivalent
#data NimaNormalizationRowFiltration
  := nima-filtered-comparison-not-quasi-isomorphism
  | nima-lambda-torsion-I-occ-degree-minus-1
  | nima-lambda-torsion-B2-all-nonnegative-degrees
#define nima-normalization-row-filtration : NimaNormalizationRowFiltration
  := nima-filtered-comparison-not-quasi-isomorphism
#data NimaTwoGradeConductorTrace
  := nima-normalized-matrix-1-1-0-1-times-minus-beta
  | nima-occurrence-normal-line-retained
#define nima-two-grade-conductor-trace : NimaTwoGradeConductorTrace
  := nima-occurrence-normal-line-retained
#data NimaFullConductorResidue
  := nima-two-independent-six-support-trace-lifts
  | nima-rank-two-unimodular-supported-Hom
  | nima-dualizing-residue-distinguishes-relation-difference
#define nima-full-conductor-residue : NimaFullConductorResidue
  := nima-two-independent-six-support-trace-lifts
#data NimaSeparatedDilationStatus
  := nima-two-traces-supported-on-dilation-intersection
  | nima-generic-incidence-zero-on-invertible-locus
  | nima-equal-parameter-specialization-nonflat
#define nima-separated-dilation-status : NimaSeparatedDilationStatus
  := nima-two-traces-supported-on-dilation-intersection
#data NimaDerivedNormalizationPhysicalStatus
  := nima-coefficient-derived-diagram-not-physical-correspondence
#define nima-derived-normalization-physical-status
  : NimaDerivedNormalizationPhysicalStatus
  := nima-coefficient-derived-diagram-not-physical-correspondence
```
