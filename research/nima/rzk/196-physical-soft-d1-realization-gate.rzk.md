# Physical soft D1 realization gate

```rzk
#lang rzk-1
#data NimaPhysicalPrincipalLiteralVanishing
  := nima-D2-D3-Z12-Z13-Z23-maps-zero-by-support
  | nima-physical-D1-corner-maps-zero
#define nima-physical-principal-literal-vanishing
  : NimaPhysicalPrincipalLiteralVanishing
  := nima-physical-D1-corner-maps-zero
#data NimaPhysicalSoftD1MapKind
  := nima-not-ordinary-fibre-boundary
  | nima-requires-soft-nearby-cycle-specialization
#define nima-physical-soft-D1-map-kind : NimaPhysicalSoftD1MapKind
  := nima-requires-soft-nearby-cycle-specialization
#data NimaPhysicalSoftD1SourceStatus
  := nima-primary-source-supplies-no-analytic-continuation
  | nima-synthetic-coefficient-cell-does-not-fill-this-gap
#define nima-physical-soft-D1-source-status : NimaPhysicalSoftD1SourceStatus
  := nima-primary-source-supplies-no-analytic-continuation
#data NimaPhysicalSoftD1ExecutableNextInput
  := nima-construct-nearby-cycle-specialization-morphism
  | nima-check-its-boundary-equals-Cech-image-of-Bx
#define nima-physical-soft-D1-executable-next-input : NimaPhysicalSoftD1ExecutableNextInput
  := nima-construct-nearby-cycle-specialization-morphism
```
