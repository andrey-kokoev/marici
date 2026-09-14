# L2 integral denominator lattice

```rzk
#lang rzk-1
#data NimaL2ExactRationalColumnAudit
  := nima-6960-labelled-columns-through-D28
  | nima-denominators-only-one-or-two
  | nima-all-half-integrality-confined-to-u-sector
#define nima-L2-exact-rational-column-audit : NimaL2ExactRationalColumnAudit
  := nima-all-half-integrality-confined-to-u-sector
#data NimaL2IntegralLatticeCandidate
  := nima-use-u-over-two-as-square-zero-integral-generator
  | nima-u0-sector-retains-original-integral-lattice
  | nima-all-tested-labelled-columns-become-integral
#define nima-L2-integral-lattice-candidate : NimaL2IntegralLatticeCandidate
  := nima-use-u-over-two-as-square-zero-integral-generator
#data NimaL2IntegralPresentationGate
  := nima-denominator-lattice-now-explicit
  | nima-Bockstein-relation-Smith-matrix-still-required
  | nima-finite-audit-not-all-degree-denominator-theorem
#define nima-L2-integral-presentation-gate : NimaL2IntegralPresentationGate
  := nima-Bockstein-relation-Smith-matrix-still-required
```
