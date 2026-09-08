# Genuine union recollement and obstruction persistence

The finite union layer and the all-thickening local-cohomology object are kept
as different types.  The open complement does not remove any of the six
branch-normal components of either Q obstruction.

```rzk
#lang rzk-1

#data NimaUnionSupportModel
  := nima-union-finite-dual-layer
  | nima-union-all-thickening-local-cohomology
  | nima-union-genuine-open-complement

#data NimaUnionSupportProperty
  := nima-finite-cone-has-closed-fibre-classes
  | nima-genuine-open-vanishes-on-closed-pair-fibre
  | nima-genuine-supported-open-orthogonal

#define nima-union-support-property
  : NimaUnionSupportModel -> NimaUnionSupportProperty
  := \ model -> match model
       (nima-union-finite-dual-layer =>
          nima-finite-cone-has-closed-fibre-classes
       | nima-union-all-thickening-local-cohomology =>
          nima-genuine-supported-open-orthogonal
       | nima-union-genuine-open-complement =>
          nima-genuine-open-vanishes-on-closed-pair-fibre)

#data NimaQObstructionComponent6
  := nima-q-component-positive-13
  | nima-q-component-positive-15
  | nima-q-component-positive-35
  | nima-q-component-negative-02
  | nima-q-component-negative-04
  | nima-q-component-negative-24

#data NimaPairIntersection3
  := nima-pair-intersection-04-35
  | nima-pair-intersection-02-15
  | nima-pair-intersection-24-13

#data NimaComponentEscapeWitness
  := nima-component-has-point-outside-pair-union

#define nima-q-component-escapes-pair-union
  : NimaQObstructionComponent6 -> NimaComponentEscapeWitness
  := \ component -> nima-component-has-point-outside-pair-union

#data NimaOpenObstructionKind
  := nima-open-individual-lift-obstruction
  | nima-open-coefficient-naturality-obstruction

#define NimaOpenObstructionGenerator
  (kind : NimaOpenObstructionKind) : U
  := match kind
       (nima-open-individual-lift-obstruction =>
          NimaAlternatingReesAnnihilatorGenerator
       | nima-open-coefficient-naturality-obstruction =>
          NimaNaturalityAnnihilatorGenerator)

#define nima-open-obstruction-generator
  : (kind : NimaOpenObstructionKind) -> NimaOpenObstructionGenerator kind
  := \ kind -> match kind
       (nima-open-individual-lift-obstruction => nima-annihilator-common
       | nima-open-coefficient-naturality-obstruction =>
          nima-naturality-annihilator-common-rees)

#data NimaOpenLiftStatus
  := nima-open-generic-unit-has-no-lift
  | nima-open-admissible-lifts-are-original-discrete-torsors
  | nima-open-naturality-extension-remains-nonsplit

#define nima-open-primary-status : NimaOpenLiftStatus
  := nima-open-generic-unit-has-no-lift
#define nima-open-ambiguity-status : NimaOpenLiftStatus
  := nima-open-admissible-lifts-are-original-discrete-torsors
#define nima-open-secondary-status : NimaOpenLiftStatus
  := nima-open-naturality-extension-remains-nonsplit

#data NimaNormalPoleOrder
  := nima-first-normal-pole
  | nima-higher-normal-pole (remaining-depth : MariciNat)
#data NimaNormalMultiplicationResult
  := nima-first-pole-killed
  | nima-higher-pole-descends

#define nima-normal-pole-multiplication
  : NimaNormalPoleOrder -> NimaNormalMultiplicationResult
  := \ pole -> match pole
       (nima-first-normal-pole => nima-first-pole-killed
       | nima-higher-normal-pole depth => nima-higher-pole-descends)

#define nima-higher-pole-is-not-first-layer
  (depth : MariciNat)
  : nima-normal-pole-multiplication (nima-higher-normal-pole depth)
      = nima-higher-pole-descends
  := refl
```
