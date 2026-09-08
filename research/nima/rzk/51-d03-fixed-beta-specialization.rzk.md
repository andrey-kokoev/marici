# D03 fixed-beta specialization packet

The fixed-beta graph creates a primitive for the former filling cycle while
retaining a separately typed first-normal comparison cycle.

```rzk
#lang rzk-1

#data NimaD03SpecializedState
  := nima-d03-specialized-Omega
  | nima-d03-specialized-S
  | nima-d03-specialized-Hmu
#define NimaD03SpecializedPacket : U := NimaZSum NimaD03SpecializedState

#define nima-d03-specialized-column
  : NimaD03SpecializedState -> NimaD03SpecializedPacket
  := \ q -> match q
       (nima-d03-specialized-Omega => nima-sum-zero NimaD03SpecializedState
       | nima-d03-specialized-S => nima-sum-atom NimaD03SpecializedState
          nima-d03-specialized-Omega
       | nima-d03-specialized-Hmu => nima-sum-atom NimaD03SpecializedState
          nima-d03-specialized-Omega)
#define nima-d03-specialized-d : NimaD03SpecializedPacket -> NimaD03SpecializedPacket
  := nima-sum-bind NimaD03SpecializedState NimaD03SpecializedState
       nima-d03-specialized-column

#define nima-d03-specialized-Omega-chain : NimaD03SpecializedPacket
  := nima-sum-atom NimaD03SpecializedState nima-d03-specialized-Omega
#define nima-d03-specialized-S-chain : NimaD03SpecializedPacket
  := nima-sum-atom NimaD03SpecializedState nima-d03-specialized-S
#define nima-d03-specialized-Hmu-chain : NimaD03SpecializedPacket
  := nima-sum-atom NimaD03SpecializedState nima-d03-specialized-Hmu
#define nima-d03-specialized-Z-chain : NimaD03SpecializedPacket
  := nima-sum-add NimaD03SpecializedState
       nima-d03-specialized-Hmu-chain
       (nima-sum-neg NimaD03SpecializedState nima-d03-specialized-S-chain)

#define nima-d03-specialized-primary-is-boundary
  : nima-sum-equal NimaD03SpecializedState
      (nima-d03-specialized-d nima-d03-specialized-S-chain)
      nima-d03-specialized-Omega-chain
  := \ probe -> refl
#define nima-d03-specialized-Z-cycle
  : nima-sum-equal NimaD03SpecializedState
      (nima-d03-specialized-d nima-d03-specialized-Z-chain)
      (nima-sum-zero NimaD03SpecializedState)
  := nima-sum-add-inverse NimaD03SpecializedState
       nima-d03-specialized-Omega-chain

#define nima-d03-specialized-Z-probe : NimaD03SpecializedState -> MariciInt
  := \ q -> match q
       (nima-d03-specialized-Omega => marici-int-zero
       | nima-d03-specialized-S => marici-int-zero
       | nima-d03-specialized-Hmu => marici-int-one)
#define nima-d03-specialized-column-Z-zero (q : NimaD03SpecializedState)
  : nima-sum-eval NimaD03SpecializedState nima-d03-specialized-Z-probe
      (nima-d03-specialized-column q) = marici-int-zero
  := match q
       (nima-d03-specialized-Omega => refl
       | nima-d03-specialized-S => refl
       | nima-d03-specialized-Hmu => refl)

#define nima-d03-specialized-boundary-Z-zero (p : NimaD03SpecializedPacket)
  : nima-sum-eval NimaD03SpecializedState nima-d03-specialized-Z-probe
      (nima-d03-specialized-d p) = marici-int-zero
  := nima-frame-concat MariciInt
       (nima-sum-eval NimaD03SpecializedState nima-d03-specialized-Z-probe
         (nima-d03-specialized-d p))
       (nima-sum-eval NimaD03SpecializedState
         (\ q -> nima-sum-eval NimaD03SpecializedState
           nima-d03-specialized-Z-probe (nima-d03-specialized-column q)) p)
       marici-int-zero
       (nima-sum-eval-bind NimaD03SpecializedState NimaD03SpecializedState
         nima-d03-specialized-column nima-d03-specialized-Z-probe p)
       (nima-any-eval-zero-atoms NimaD03SpecializedState
         (\ q -> nima-sum-eval NimaD03SpecializedState
           nima-d03-specialized-Z-probe (nima-d03-specialized-column q))
         nima-d03-specialized-column-Z-zero p)

#define nima-d03-specialized-Z-value
  : nima-sum-eval NimaD03SpecializedState nima-d03-specialized-Z-probe
      nima-d03-specialized-Z-chain = marici-int-one
  := refl

#define nima-d03-specialized-Z-not-boundary
  (p : NimaD03SpecializedPacket)
  (boundary : nima-sum-equal NimaD03SpecializedState
    (nima-d03-specialized-d p) nima-d03-specialized-Z-chain)
  : marici-int-zero = marici-int-one
  := nima-frame-concat MariciInt marici-int-zero
       (nima-sum-eval NimaD03SpecializedState nima-d03-specialized-Z-probe
         (nima-d03-specialized-d p)) marici-int-one
       (nima-frame-rev MariciInt
         (nima-sum-eval NimaD03SpecializedState nima-d03-specialized-Z-probe
           (nima-d03-specialized-d p)) marici-int-zero
         (nima-d03-specialized-boundary-Z-zero p))
       (boundary nima-d03-specialized-Z-probe)

#data NimaD03FirstNormalSymbol
  := nima-d03-first-normal-Z-symbol
#define nima-d03-first-symbol-value
  : NimaD03FirstNormalSymbol -> MariciInt
  := \ symbol -> marici-int-one
#define nima-d03-first-symbol-is-primitive
  : nima-d03-first-symbol-value nima-d03-first-normal-Z-symbol = marici-int-one
  := refl
```
