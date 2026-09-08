# Endpoint multiplier coherence

```rzk
#lang rzk-1

#data NimaEndpointMultiplierLiftLevel
  := nima-nine-individual-normal-product-lifts
  | nima-collective-normal-product-ideal-lift
#data NimaEndpointMultiplierLiftStatus
  := nima-individual-lifts-exist
  | nima-collective-lift-space-empty
#define nima-endpoint-multiplier-lift-status
  : NimaEndpointMultiplierLiftLevel -> NimaEndpointMultiplierLiftStatus
  := \ level -> match level
       (nima-nine-individual-normal-product-lifts => nima-individual-lifts-exist
       | nima-collective-normal-product-ideal-lift => nima-collective-lift-space-empty)

#data NimaMultiplierResolutionRank
  := nima-multiplier-generators-9
  | nima-multiplier-first-relations-18
  | nima-multiplier-second-relations-15
  | nima-multiplier-third-relations-6
  | nima-multiplier-fourth-relations-1

#data NimaEndpointRelationDiscrepancyStatus
  := nima-eighteen-nonzero-endpoint-discrepancies
  | nima-all-fifteen-second-relations-satisfied

#data NimaMultiplierExtensionComparison
  := nima-collective-class-is-original-endpoint-extension
#define nima-multiplier-extension-comparison : NimaMultiplierExtensionComparison
  := nima-collective-class-is-original-endpoint-extension

#data NimaPositiveIdealPowerBehavior
  := nima-every-positive-power-retains-endpoint-extension
#define nima-positive-ideal-power-behavior : NimaPositiveIdealPowerBehavior
  := nima-every-positive-power-retains-endpoint-extension

#data NimaMultiplierDerivedDualResidues
  := nima-two-opposite-triple-normal-residue-lines-degree-2
#define nima-multiplier-derived-dual-residues : NimaMultiplierDerivedDualResidues
  := nima-two-opposite-triple-normal-residue-lines-degree-2

#data NimaMultiplierSourceProvenance
  := nima-multiplier-source-target-residue-selected
  | nima-multiplier-source-native-physical
#define nima-multiplier-source-provenance : NimaMultiplierSourceProvenance
  := nima-multiplier-source-target-residue-selected
```
