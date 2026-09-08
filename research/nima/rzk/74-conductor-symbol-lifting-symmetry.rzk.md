# Conductor-symbol lifting and symmetry

```rzk
#lang rzk-1

#data NimaConductorSymbolLattice
  := nima-closed-first-symbol-lattice-rank-134
  | nima-quadratic-obstruction-lattice-rank-74
  | nima-full-lift-lattice-rank-60

#data NimaConductorSymbolCompatibility
  := nima-quadratic-compatible
  | nima-quadratic-incompatible
#data NimaConductorSymbolLiftResult
  := nima-unique-full-coefficient-cycle-lift
  | nima-no-full-coefficient-cycle-lift
#define nima-conductor-symbol-lift-result
  : NimaConductorSymbolCompatibility -> NimaConductorSymbolLiftResult
  := \ compatibility -> match compatibility
       (nima-quadratic-compatible => nima-unique-full-coefficient-cycle-lift
       | nima-quadratic-incompatible => nima-no-full-coefficient-cycle-lift)

#data NimaHigherConductorCorrectionStatus
  := nima-no-degree-three-higher-conductor-corrections
#define nima-higher-conductor-correction-status
  : NimaHigherConductorCorrectionStatus
  := nima-no-degree-three-higher-conductor-corrections

#data NimaEquivariantLiftDirection
  := nima-equivariant-visible-direction
  | nima-equivariant-primary-homotopy-direction
#data NimaEquivariantLiftRanks
  := nima-equivariant-ranks-16-visible-9-primary-homotopy
#define nima-equivariant-lift-ranks : NimaEquivariantLiftRanks
  := nima-equivariant-ranks-16-visible-9-primary-homotopy

#data NimaInvariantPreimageDefect
  := nima-invariant-preimage-index-two-defect
#define nima-invariant-preimage-defect : NimaInvariantPreimageDefect
  := nima-invariant-preimage-index-two-defect

#data NimaConductorMorseSelectionStatus
  := nima-scalar-conormal-symbol-does-not-select-chain-symbol
#define nima-conductor-morse-selection-status : NimaConductorMorseSelectionStatus
  := nima-scalar-conormal-symbol-does-not-select-chain-symbol
```
