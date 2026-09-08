# Orbit source assembly gate

The three-pair tensor and closed-support descent are different coefficient
objects and therefore have differently typed lifting results.

```rzk
#lang rzk-1

#data NimaOrbitAssembly
  := nima-orbit-common-intersection
  | nima-orbit-closed-support-union

#data NimaOrbitDualDegree
  := nima-orbit-dual-degree-2
  | nima-orbit-dual-degree-3
  | nima-orbit-dual-degree-4
  | nima-orbit-dual-degree-6

#define NimaOrbitDualClass (assembly : NimaOrbitAssembly) : U
  := match assembly
       (nima-orbit-common-intersection => NimaD03QTopVector
       | nima-orbit-closed-support-union =>
          Sigma (_ : NimaOrbitDualDegree), NimaD03QTopVector)

#define nima-orbit-intersection-degree : NimaOrbitDualDegree
  := nima-orbit-dual-degree-6

#data NimaUnionDualStratum
  := nima-union-pair-residue-0 | nima-union-pair-residue-1
  | nima-union-pair-residue-2
  | nima-union-double-overlap-01 | nima-union-double-overlap-02
  | nima-union-double-overlap-12
  | nima-union-triple-overlap

#define nima-union-dual-stratum-degree
  : NimaUnionDualStratum -> NimaOrbitDualDegree
  := \ stratum -> match stratum
       (nima-union-pair-residue-0 => nima-orbit-dual-degree-2
       | nima-union-pair-residue-1 => nima-orbit-dual-degree-2
       | nima-union-pair-residue-2 => nima-orbit-dual-degree-2
       | nima-union-double-overlap-01 => nima-orbit-dual-degree-3
       | nima-union-double-overlap-02 => nima-orbit-dual-degree-3
       | nima-union-double-overlap-12 => nima-orbit-dual-degree-3
       | nima-union-triple-overlap => nima-orbit-dual-degree-4)

#data NimaOrbitSectionStatus
  := nima-orbit-intersection-has-strict-section
  | nima-orbit-union-has-no-derived-section

#define nima-orbit-section-status : NimaOrbitAssembly -> NimaOrbitSectionStatus
  := \ assembly -> match assembly
       (nima-orbit-common-intersection =>
          nima-orbit-intersection-has-strict-section
       | nima-orbit-closed-support-union =>
          nima-orbit-union-has-no-derived-section)

#define nima-orbit-intersection-section-witness
  (q : NimaD03QTopVector)
  : nima-sum-equal NimaD03QTopState
      (nima-fully-supported-q-projection (nima-fully-supported-q-section q)) q
  := nima-fully-supported-q-section-is-strict q

#data NimaOrbitGenericOpenBehavior
  := nima-intersection-contractible-on-six-parameter-open
  | nima-union-retains-local-pair-operation

#define nima-orbit-generic-open-behavior
  : NimaOrbitAssembly -> NimaOrbitGenericOpenBehavior
  := \ assembly -> match assembly
       (nima-orbit-common-intersection =>
          nima-intersection-contractible-on-six-parameter-open
       | nima-orbit-closed-support-union =>
          nima-union-retains-local-pair-operation)

#data NimaLocalizedUnionObstruction
  := nima-localized-union-missing-t13-t15-divisibility
#define nima-localized-union-obstruction-value
  : NimaLocalizedUnionObstruction -> MariciInt
  := \ obstruction -> marici-int-one
#define nima-localized-union-obstruction-is-primitive
  : nima-localized-union-obstruction-value
      nima-localized-union-missing-t13-t15-divisibility = marici-int-one
  := refl
```
