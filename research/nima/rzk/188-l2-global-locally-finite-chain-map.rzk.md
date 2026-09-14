# L2 global locally finite labelled operator

```rzk
#lang rzk-1
#data NimaL2GlobalMapConstruction
  := nima-apply-labelled-column-formula-termwise
  | nima-finite-source-polynomial-has-finite-image
#define nima-L2-global-map-construction : NimaL2GlobalMapConstruction
  := nima-apply-labelled-column-formula-termwise
#data NimaL2GlobalMapDegreeBound
  := nima-source-support-m-through-D-maps-to-mplus2-through-Dplus7
#define nima-L2-global-map-degree-bound : NimaL2GlobalMapDegreeBound
  := nima-source-support-m-through-D-maps-to-mplus2-through-Dplus7
#data NimaL2GlobalMapTruncation
  := nima-every-finite-matrix-is-restriction-of-one-global-map
  | nima-cutoff-projections-commute-strictly
#define nima-L2-global-map-truncation : NimaL2GlobalMapTruncation
  := nima-every-finite-matrix-is-restriction-of-one-global-map
#data NimaL2GlobalMapScope
  := nima-global-coefficient-labelled-operator-constructed
  | nima-chain-map-compatibility-still-required
  | nima-road-Cech-geometric-identification-open
  | nima-integral-saturation-tower-open
#define nima-L2-global-map-scope : NimaL2GlobalMapScope
  := nima-global-coefficient-labelled-operator-constructed
```
