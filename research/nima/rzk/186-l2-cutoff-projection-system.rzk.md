# L2 cutoff projection system

```rzk
#lang rzk-1
#data NimaL2CutoffProjectionChecks
  := nima-D16-to12-D20to16-D24to20-D28to24
  | nima-shared-labelled-columns-project-identically
  | nima-new-columns-have-no-lower-degree-output
#define nima-L2-cutoff-projection-checks : NimaL2CutoffProjectionChecks
  := nima-new-columns-have-no-lower-degree-output
#data NimaL2FilteredMatrixSystem
  := nima-labelled-exact-matrices-form-strict-degree-projection-system
  | nima-u-over-two-integral-lattice-preserved-by-projection
#define nima-L2-filtered-matrix-system : NimaL2FilteredMatrixSystem
  := nima-labelled-exact-matrices-form-strict-degree-projection-system
#data NimaL2DerivedCompatibilityProgress
  := nima-chain-level-cutoff-maps-now-explicit
  | nima-compatible-Smith-bases-not-required-for-chain-map
  | nima-derived-saturation-lift-along-projections-open
#define nima-L2-derived-compatibility-progress : NimaL2DerivedCompatibilityProgress
  := nima-chain-level-cutoff-maps-now-explicit
```
