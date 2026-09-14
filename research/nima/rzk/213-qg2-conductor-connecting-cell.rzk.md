# qg2 conductor connecting cell

```rzk
#lang rzk-1
#data NimaQG2WallKummerData
  := nima-wall-kernel-is16p4-times-xi-plus-kappa-squared
  | nima-wall-divisor-multiplicity-two
  | nima-normalized-wall-Kummer-character-trivial
#define nima-qg2-wall-Kummer-data : NimaQG2WallKummerData
  := nima-normalized-wall-Kummer-character-trivial
#data NimaQG2ConductorResidues
  := nima-endpoint-and-conductor-residues-both-1-over64p4kappa-minus1
  | nima-infinity-residue-is-negative-finite-residue-sum
#define nima-qg2-conductor-residues : NimaQG2ConductorResidues
  := nima-infinity-residue-is-negative-finite-residue-sum
#data NimaQG2InverseEulerConnectingCoefficient
  := nima-collision-Euler-class-kappa-minus1
  | nima-localized-self-intersection-inverts-kappa-minus1
  | nima-connecting-coefficient-minus1-over32p4kappa-minus1-squared
#define nima-qg2-inverse-Euler-connecting-coefficient
  : NimaQG2InverseEulerConnectingCoefficient
  := nima-connecting-coefficient-minus1-over32p4kappa-minus1-squared
#data NimaQG2ConductorCellScope
  := nima-local-grade-minus1-conductor-connecting-cell-constructed
  | nima-not-the-fitted-qg1-node-normalization
  | nima-physical-relative-cut-chain-still-required
#define nima-qg2-conductor-cell-scope : NimaQG2ConductorCellScope
  := nima-local-grade-minus1-conductor-connecting-cell-constructed
```
