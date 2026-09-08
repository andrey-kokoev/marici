# Three-pair supported PC section

```rzk
#lang rzk-1

#data NimaPairOrbitStage
  := nima-pair-orbit-none
  | nima-pair-orbit-D03
  | nima-pair-orbit-D03-D25
  | nima-pair-orbit-all-three

#define nima-pair-orbit-remaining-rees-count : NimaPairOrbitStage -> MariciNat
  := \ stage -> match stage
       (nima-pair-orbit-none => marici-succ (marici-succ (marici-succ
          (marici-succ (marici-succ (marici-succ marici-zero)))))
       | nima-pair-orbit-D03 => marici-succ (marici-succ
          (marici-succ (marici-succ marici-zero)))
       | nima-pair-orbit-D03-D25 => marici-succ (marici-succ marici-zero)
       | nima-pair-orbit-all-three => marici-zero)

#define NimaFullySupportedPCBoundary : U := NimaZSum NimaD03EndpointConnectorState
#define NimaFullySupportedPCTarget : U
  := Sigma (_ : NimaD03QTopVector), NimaFullySupportedPCBoundary

#define nima-fully-supported-q-section
  : NimaD03QTopVector -> NimaFullySupportedPCTarget
  := \ q -> (q,nima-sum-zero NimaD03EndpointConnectorState)
#define nima-fully-supported-q-projection
  : NimaFullySupportedPCTarget -> NimaD03QTopVector
  := \ (q,boundary) -> q

#define nima-fully-supported-q-section-is-strict (q : NimaD03QTopVector)
  : nima-sum-equal NimaD03QTopState
      (nima-fully-supported-q-projection (nima-fully-supported-q-section q)) q
  := \ probe -> refl

#define nima-fully-supported-four-term-lift : NimaFullySupportedPCTarget
  := nima-fully-supported-q-section nima-d03-q-four-term-vector
#define nima-fully-supported-four-term-projects
  : nima-sum-equal NimaD03QTopState
      (nima-fully-supported-q-projection nima-fully-supported-four-term-lift)
      nima-d03-q-four-term-vector
  := \ probe -> refl
```
