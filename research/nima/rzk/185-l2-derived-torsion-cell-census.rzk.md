# L2 derived torsion-cell census

```rzk
#lang rzk-1
#data NimaL2TorsionCellCounts
  := nima-D12-D16-D20-D24-D28-cells-17-34-53-76-103
#define nima-L2-torsion-cell-counts : NimaL2TorsionCellCounts
  := nima-D12-D16-D20-D24-D28-cells-17-34-53-76-103
#data NimaL2PrimaryLengths
  := nima-two-primary-lengths-18-38-61-82-117
  | nima-three-primary-lengths-9-13-17-25-25
#define nima-L2-primary-lengths : NimaL2PrimaryLengths
  := nima-two-primary-lengths-18-38-61-82-117
#data NimaL2DerivedSaturationConstruction
  := nima-one-cell-per-nonunit-invariant-factor
  | nima-cell-differential-is-multiplication-by-factor
  | nima-only-2-and3-primary-cells-required
#define nima-L2-derived-saturation-construction : NimaL2DerivedSaturationConstruction
  := nima-cell-differential-is-multiplication-by-factor
#data NimaL2DerivedTowerGate
  := nima-finite-cell-censuses-explicit
  | nima-cutoff-compatibility-maps-open
  | nima-global-derived-tower-open
#define nima-L2-derived-tower-gate : NimaL2DerivedTowerGate
  := nima-cutoff-compatibility-maps-open
```
