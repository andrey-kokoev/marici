# L2 global chain-map gate

```rzk
#lang rzk-1
#define nima-L2-global-chain-map-witness
  (Source Target : U)
  (dSource : Source -> Source)
  (dTarget : Target -> Target)
  (L2operator : Source -> Target)
  : U
  := (x : Source) -> dTarget (L2operator x) = L2operator (dSource x)
#define nima-L2-global-chain-map-commutes
  (Source Target : U)
  (dSource : Source -> Source)
  (dTarget : Target -> Target)
  (L2operator : Source -> Target)
  (witness : nima-L2-global-chain-map-witness
    Source Target dSource dTarget L2operator)
  (x : Source)
  : dTarget (L2operator x) = L2operator (dSource x)
  := witness x
#data NimaL2GlobalOperatorStatus
  := nima-termwise-operator-locally-finite
  | nima-strict-filtered-projections-proved
  | nima-differential-commutation-not-yet-checked
#define nima-L2-global-operator-status : NimaL2GlobalOperatorStatus
  := nima-differential-commutation-not-yet-checked
#data NimaL2GlobalChainMapNextInput
  := nima-model-global-source-and-target-differentials
  | nima-prove-dTarget-L2-equals-L2-dSource-on-generators
#define nima-L2-global-chain-map-next-input : NimaL2GlobalChainMapNextInput
  := nima-prove-dTarget-L2-equals-L2-dSource-on-generators
```
