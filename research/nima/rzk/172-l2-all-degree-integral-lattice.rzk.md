# L2 all-degree integral lattice

```rzk
#lang rzk-1
#data NimaL2SquareZeroPowerLaw
  := nima-l1-and-l2-powers-have-integral-u0-and-at-most-half-u1
  | nima-only-exponents-zero-one-two-occur
  | nima-u2-zero-removes-higher-denominators
#define nima-L2-square-zero-power-law : NimaL2SquareZeroPowerLaw
  := nima-u2-zero-removes-higher-denominators
#data NimaL2DerivativeIntegrality
  := nima-three-halves-times-db-k-is-integral
  | nima-three-halves-times-da-k-is-integral
  | nima-all-other-column-coefficients-integral
#define nima-L2-derivative-integrality : NimaL2DerivativeIntegrality
  := nima-three-halves-times-da-k-is-integral
#data NimaL2AllDegreeIntegralLattice
  := nima-u0-original-and-u1-generated-by-u-over-two
  | nima-every-labelled-p-q-column-integral-in-all-degrees
#define nima-L2-all-degree-integral-lattice : NimaL2AllDegreeIntegralLattice
  := nima-every-labelled-p-q-column-integral-in-all-degrees
#data NimaL2AllDegreeSmithGate
  := nima-integral-column-lattice-proved
  | nima-relation-kernel-Smith-presentation-remains
#define nima-L2-all-degree-Smith-gate : NimaL2AllDegreeSmithGate
  := nima-relation-kernel-Smith-presentation-remains
```
