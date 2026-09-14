# L2 global Bockstein naturality

```rzk
#lang rzk-1
#data NimaL2RelationProjectionNaturality
  := nima-higher-cutoff-A-relation-projects-to-lower-A-relation
  | nima-no-new-source-column-contributes-in-lower-degree
#define nima-L2-relation-projection-naturality : NimaL2RelationProjectionNaturality
  := nima-higher-cutoff-A-relation-projects-to-lower-A-relation
#data NimaL2BocksteinRepresentativeNaturality
  := nima-projection-of-Bx-equals-B-of-projected-x
  | nima-columnwise-strict-equality
#define nima-L2-Bockstein-representative-naturality
  : NimaL2BocksteinRepresentativeNaturality
  := nima-projection-of-Bx-equals-B-of-projected-x
#data NimaL2GlobalBocksteinConstruction
  := nima-every-finite-relation-occurs-at-a-cutoff
  | nima-every-representative-has-finite-support
  | nima-filtered-colimit-defines-global-Bockstein-operator
#define nima-L2-global-Bockstein-construction : NimaL2GlobalBocksteinConstruction
  := nima-filtered-colimit-defines-global-Bockstein-operator
#data NimaL2GlobalBocksteinScope
  := nima-global-relation-to-representative-map-constructed
  | nima-cokernel-saturation-open
  | nima-road-Cech-realization-open
#define nima-L2-global-Bockstein-scope : NimaL2GlobalBocksteinScope
  := nima-global-relation-to-representative-map-constructed
```
