# Physical road comparison typing obstruction

```rzk
#lang rzk-1
#data NimaPhysicalChartAssemblyType
  := nima-three-cut-sectors-form-C3-equivariant-direct-sum
  | nima-distinct-cut-sectors-have-no-source-double-pole-overlap
  | nima-global-three-sector-Cech-differential-not-source-supported
#define nima-physical-chart-assembly-type : NimaPhysicalChartAssemblyType
  := nima-three-cut-sectors-form-C3-equivariant-direct-sum

#data NimaPhysicalWallGradeProfile
  := nima-qg1-grade-minus1
  | nima-qg2-grade-minus2
  | nima-qg3-grade-minus1
#define nima-physical-wall-grade-profile : NimaPhysicalWallGradeProfile
  := nima-qg2-grade-minus2

#data NimaPhysicalRoadNormalizationObstruction
  := nima-no-source-epsilon-conductor-map-from-qg2-grade-minus2
  | nima-multiplication-by-x-would-be-fitted-grade-shift
  | nima-v-cannot-yet-be-identified-with-physical-qg2-log-class
#define nima-physical-road-normalization-obstruction
  : NimaPhysicalRoadNormalizationObstruction
  := nima-v-cannot-yet-be-identified-with-physical-qg2-log-class

#data NimaPhysicalRoadComparisonRequiredFactorization
  := nima-first-build-source-normalization-N-epsilon
  | nima-then-map-normalized-wall-class-to-selected-v
  | nima-then-compare-local-road-boundary-with-physical-residual
#define nima-physical-road-comparison-required-factorization
  : NimaPhysicalRoadComparisonRequiredFactorization
  := nima-first-build-source-normalization-N-epsilon
```
