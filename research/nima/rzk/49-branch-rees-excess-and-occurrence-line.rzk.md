# Branch Rees excess and supported occurrence line

This module records two tests required by the branch-supported comparison:
the complementary-minor return scales the excess by the full branch Rees
product, while a principal occurrence line remains nonzero after its
multiplication map specializes to zero.

```rzk
#lang rzk-1

#define NimaBranchRees3 : U
  := Sigma (_ : MariciNat), Sigma (_ : MariciNat), MariciNat
#data NimaBranchExcessState
  := nima-branch-excess-copy
  | nima-pair-excess-copy
#define NimaBranchExcessBasis : U
  := Sigma (_ : NimaBranchExcessState), NimaBranchRees3
#define NimaBranchExcessPacket : U := NimaZSum NimaBranchExcessBasis

#define nima-rees3-zero : NimaBranchRees3
  := (marici-zero,(marici-zero,marici-zero))
#define nima-rees3-t3 (m : NimaBranchRees3) : NimaBranchRees3
  := let (a,(b,c)) := m in (a,(marici-succ b,c))
#define nima-rees3-t1t5 (m : NimaBranchRees3) : NimaBranchRees3
  := let (a,(b,c)) := m in (marici-succ a,(b,marici-succ c))
#define nima-rees3-tau (m : NimaBranchRees3) : NimaBranchRees3
  := let (a,(b,c)) := m in
     (marici-succ a,(marici-succ b,marici-succ c))

#define nima-branch-selector-column : NimaBranchExcessBasis -> NimaBranchExcessPacket
  := \ (q,m) -> match q
       (nima-branch-excess-copy => nima-sum-atom NimaBranchExcessBasis
          (nima-branch-excess-copy,nima-rees3-t3 m)
       | nima-pair-excess-copy => nima-sum-atom NimaBranchExcessBasis
          (nima-pair-excess-copy,m))
#define nima-branch-return-column : NimaBranchExcessBasis -> NimaBranchExcessPacket
  := \ (q,m) -> match q
       (nima-branch-excess-copy => nima-sum-atom NimaBranchExcessBasis
          (nima-branch-excess-copy,nima-rees3-t1t5 m)
       | nima-pair-excess-copy => nima-sum-atom NimaBranchExcessBasis
          (nima-pair-excess-copy,nima-rees3-tau m))

#define nima-branch-selector : NimaBranchExcessPacket -> NimaBranchExcessPacket
  := nima-sum-bind NimaBranchExcessBasis NimaBranchExcessBasis
       nima-branch-selector-column
#define nima-branch-return : NimaBranchExcessPacket -> NimaBranchExcessPacket
  := nima-sum-bind NimaBranchExcessBasis NimaBranchExcessBasis
       nima-branch-return-column

#define nima-excess-eta-u : NimaBranchExcessPacket
  := nima-sum-add NimaBranchExcessBasis
       (nima-sum-atom NimaBranchExcessBasis
         (nima-branch-excess-copy,nima-rees3-zero))
       (nima-sum-neg NimaBranchExcessBasis
         (nima-sum-atom NimaBranchExcessBasis
           (nima-pair-excess-copy,nima-rees3-zero)))
#define nima-excess-eta-x : NimaBranchExcessPacket
  := nima-sum-add NimaBranchExcessBasis
       (nima-sum-atom NimaBranchExcessBasis
         (nima-branch-excess-copy,nima-rees3-t3 nima-rees3-zero))
       (nima-sum-neg NimaBranchExcessBasis
         (nima-sum-atom NimaBranchExcessBasis
           (nima-pair-excess-copy,nima-rees3-zero)))
#define nima-excess-tau-eta-u : NimaBranchExcessPacket
  := nima-sum-add NimaBranchExcessBasis
       (nima-sum-atom NimaBranchExcessBasis
         (nima-branch-excess-copy,nima-rees3-tau nima-rees3-zero))
       (nima-sum-neg NimaBranchExcessBasis
         (nima-sum-atom NimaBranchExcessBasis
           (nima-pair-excess-copy,nima-rees3-tau nima-rees3-zero)))

#define nima-selector-preserves-excess
  : nima-sum-equal NimaBranchExcessBasis
      (nima-branch-selector nima-excess-eta-u) nima-excess-eta-x
  := \ probe -> refl
#define nima-return-scales-excess
  : nima-sum-equal NimaBranchExcessBasis
      (nima-branch-return nima-excess-eta-x) nima-excess-tau-eta-u
  := \ probe -> refl

#data NimaPrincipalOccurrenceLine := nima-principal-occurrence-frame
#data NimaPrincipalOccurrenceDual := nima-principal-occurrence-dual-frame

#define nima-occurrence-line-pair
  : NimaPrincipalOccurrenceDual -> NimaPrincipalOccurrenceLine -> MariciInt
  := \ dual line -> marici-int-one
#define nima-occurrence-line-pair-is-primitive
  : nima-occurrence-line-pair nima-principal-occurrence-dual-frame
      nima-principal-occurrence-frame = marici-int-one
  := refl

#define nima-selected-branch-multiplication
  : NimaPrincipalOccurrenceLine -> MariciInt
  := \ line -> marici-int-zero
#define nima-selected-branch-multiplication-vanishes
  : nima-selected-branch-multiplication nima-principal-occurrence-frame
      = marici-int-zero
  := refl
```
