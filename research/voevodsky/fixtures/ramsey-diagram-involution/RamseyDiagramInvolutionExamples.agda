{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyDiagramInvolutionExamples where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Empty.Base using (⊥)
open import RamseySingleFrameFaces using (c0; m0; c1; m1)
import RamseyRequestedPortExamples as C
import RamseyFourFacetVertexCells as F
open import RamseyExternalPEExamples
import RamseyExternalSeedPolicyExamples as Policy
data Code : Type where
  s01 s02 s03 s10 s12 s13 s20 s21 s23 s30 s31 s32 : Code
input : Code → P.S.InputIndex
input s01 = C.q0 , (m0 , F.vp-0-1)
input s02 = C.q0 , (c1 , F.vp-0-2)
input s03 = C.q0 , (m1 , F.vp-0-3)
input s10 = C.q7 , (c0 , F.vp-1-0)
input s12 = C.q7 , (c1 , F.vp-1-2)
input s13 = C.q7 , (m1 , F.vp-1-3)
input s20 = C.q0 , (c0 , F.vp-2-0)
input s21 = C.q0 , (m0 , F.vp-2-1)
input s23 = C.q0 , (m1 , F.vp-2-3)
input s30 = C.q7 , (c0 , F.vp-3-0)
input s31 = C.q7 , (m0 , F.vp-3-1)
input s32 = C.q7 , (c1 , F.vp-3-2)
swap : Code → Code
swap s01 = s10
swap s02 = s13
swap s03 = s12
swap s10 = s01
swap s12 = s03
swap s13 = s02
swap s20 = s31
swap s21 = s30
swap s23 = s32
swap s30 = s21
swap s31 = s20
swap s32 = s23
swap-square : (s : Code) → swap (swap s) ≡ s
swap-square s01 = refl
swap-square s02 = refl
swap-square s03 = refl
swap-square s10 = refl
swap-square s12 = refl
swap-square s13 = refl
swap-square s20 = refl
swap-square s21 = refl
swap-square s23 = refl
swap-square s30 = refl
swap-square s31 = refl
swap-square s32 = refl
pair-preserved : (s : Code) → Policy.PairChart (fst (input (swap s)))
pair-preserved s01 = tt
pair-preserved s02 = tt
pair-preserved s03 = tt
pair-preserved s10 = tt
pair-preserved s12 = tt
pair-preserved s13 = tt
pair-preserved s20 = tt
pair-preserved s21 = tt
pair-preserved s23 = tt
pair-preserved s30 = tt
pair-preserved s31 = tt
pair-preserved s32 = tt
base-not-invariant : ((s : Code) → Policy.BaseChart (fst (input s)) → Policy.BaseChart (fst (input (swap s)))) → ⊥
base-not-invariant alleged = alleged s01 tt
ComplementChart : C.Chart → Type
ComplementChart C.q0 = ⊥
ComplementChart C.q1 = ⊥
ComplementChart C.q2 = ⊥
ComplementChart C.q3 = ⊥
ComplementChart C.q4 = ⊥
ComplementChart C.q5 = ⊥
ComplementChart C.q6 = ⊥
ComplementChart C.q7 = Unit
ComplementChart C.q8 = ⊥
ComplementChart C.q9 = ⊥
ComplementChart C.q10 = ⊥
ComplementChart C.q11 = ⊥
ComplementChart C.q12 = ⊥
ComplementChart C.q13 = ⊥
ComplementChart C.q14 = ⊥
ComplementChart C.q15 = ⊥
ComplementChart C.q16 = ⊥
ComplementChart C.q17 = ⊥
ComplementChart C.q18 = ⊥
ComplementChart C.q19 = ⊥
ComplementChart C.q20 = ⊥
ComplementChart C.q21 = ⊥
ComplementChart C.q22 = ⊥
ComplementChart C.q23 = ⊥
base-to-complement : (s : Code) → Policy.BaseChart (fst (input s)) → ComplementChart (fst (input (swap s)))
base-to-complement s01 allowed = tt
base-to-complement s02 allowed = tt
base-to-complement s03 allowed = tt
base-to-complement s10 ()
base-to-complement s12 ()
base-to-complement s13 ()
base-to-complement s20 allowed = tt
base-to-complement s21 allowed = tt
base-to-complement s23 allowed = tt
base-to-complement s30 ()
base-to-complement s31 ()
base-to-complement s32 ()
complement-to-base : (s : Code) → ComplementChart (fst (input s)) → Policy.BaseChart (fst (input (swap s)))
complement-to-base s01 ()
complement-to-base s02 ()
complement-to-base s03 ()
complement-to-base s10 allowed = tt
complement-to-base s12 allowed = tt
complement-to-base s13 allowed = tt
complement-to-base s20 ()
complement-to-base s21 ()
complement-to-base s23 ()
complement-to-base s30 allowed = tt
complement-to-base s31 allowed = tt
complement-to-base s32 allowed = tt
occ-0-1-2-0 : P.T.Occurrence tree-0-1-2
occ-0-1-2-0 = (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.source-leg , tt)))
origin-0-1-2-0 : P.T.origin tree-0-1-2 occ-0-1-2-0 ≡ input s20
origin-0-1-2-0 = refl
transport-0-1-2-0 : P.T.origin tree-1-0-3 (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-0-1-2-0 = refl
occ-0-1-2-1 : P.T.Occurrence tree-0-1-2
occ-0-1-2-1 = (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.target-leg , tt)))
origin-0-1-2-1 : P.T.origin tree-0-1-2 occ-0-1-2-1 ≡ input s10
origin-0-1-2-1 = refl
transport-0-1-2-1 : P.T.origin tree-1-0-3 (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.target-leg , tt))) ≡ input (swap s10)
transport-0-1-2-1 = refl
occ-0-1-2-2 : P.T.Occurrence tree-0-1-2
occ-0-1-2-2 = (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.source-leg , tt)))
origin-0-1-2-2 : P.T.origin tree-0-1-2 occ-0-1-2-2 ≡ input s20
origin-0-1-2-2 = refl
transport-0-1-2-2 : P.T.origin tree-1-0-3 (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-0-1-2-2 = refl
occ-0-1-2-3 : P.T.Occurrence tree-0-1-2
occ-0-1-2-3 = (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.target-leg , tt)))
origin-0-1-2-3 : P.T.origin tree-0-1-2 occ-0-1-2-3 ≡ input s30
origin-0-1-2-3 = refl
transport-0-1-2-3 : P.T.origin tree-1-0-3 (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.target-leg , tt))) ≡ input (swap s30)
transport-0-1-2-3 = refl
occ-0-1-2-4 : P.T.Occurrence tree-0-1-2
occ-0-1-2-4 = (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-0-1-2-4 : P.T.origin tree-0-1-2 occ-0-1-2-4 ≡ input s01
origin-0-1-2-4 = refl
transport-0-1-2-4 : P.T.origin tree-1-0-3 (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s01)
transport-0-1-2-4 = refl
occ-0-1-2-5 : P.T.Occurrence tree-0-1-2
occ-0-1-2-5 = (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-0-1-2-5 : P.T.origin tree-0-1-2 occ-0-1-2-5 ≡ input s31
origin-0-1-2-5 = refl
transport-0-1-2-5 : P.T.origin tree-1-0-3 (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-0-1-2-5 = refl
occ-0-1-2-6 : P.T.Occurrence tree-0-1-2
occ-0-1-2-6 = (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-0-1-2-6 : P.T.origin tree-0-1-2 occ-0-1-2-6 ≡ input s21
origin-0-1-2-6 = refl
transport-0-1-2-6 : P.T.origin tree-1-0-3 (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s21)
transport-0-1-2-6 = refl
occ-0-1-2-7 : P.T.Occurrence tree-0-1-2
occ-0-1-2-7 = (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-0-1-2-7 : P.T.origin tree-0-1-2 occ-0-1-2-7 ≡ input s31
origin-0-1-2-7 = refl
transport-0-1-2-7 : P.T.origin tree-1-0-3 (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-0-1-2-7 = refl
occ-0-1-2-8 : P.T.Occurrence tree-0-1-2
occ-0-1-2-8 = (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.source-leg , tt)))
origin-0-1-2-8 : P.T.origin tree-0-1-2 occ-0-1-2-8 ≡ input s02
origin-0-1-2-8 = refl
transport-0-1-2-8 : P.T.origin tree-1-0-3 (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-0-1-2-8 = refl
occ-0-1-2-9 : P.T.Occurrence tree-0-1-2
occ-0-1-2-9 = (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.target-leg , tt)))
origin-0-1-2-9 : P.T.origin tree-0-1-2 occ-0-1-2-9 ≡ input s12
origin-0-1-2-9 = refl
transport-0-1-2-9 : P.T.origin tree-1-0-3 (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.target-leg , tt))) ≡ input (swap s12)
transport-0-1-2-9 = refl
occ-0-1-2-10 : P.T.Occurrence tree-0-1-2
occ-0-1-2-10 = (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.source-leg , tt)))
origin-0-1-2-10 : P.T.origin tree-0-1-2 occ-0-1-2-10 ≡ input s02
origin-0-1-2-10 = refl
transport-0-1-2-10 : P.T.origin tree-1-0-3 (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-0-1-2-10 = refl
occ-0-1-2-11 : P.T.Occurrence tree-0-1-2
occ-0-1-2-11 = (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.target-leg , tt)))
origin-0-1-2-11 : P.T.origin tree-0-1-2 occ-0-1-2-11 ≡ input s32
origin-0-1-2-11 = refl
transport-0-1-2-11 : P.T.origin tree-1-0-3 (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.target-leg , tt))) ≡ input (swap s32)
transport-0-1-2-11 = refl
occ-0-1-2-12 : P.T.Occurrence tree-0-1-2
occ-0-1-2-12 = (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-0-1-2-12 : P.T.origin tree-0-1-2 occ-0-1-2-12 ≡ input s03
origin-0-1-2-12 = refl
transport-0-1-2-12 : P.T.origin tree-1-0-3 (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s03)
transport-0-1-2-12 = refl
occ-0-1-2-13 : P.T.Occurrence tree-0-1-2
occ-0-1-2-13 = (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-0-1-2-13 : P.T.origin tree-0-1-2 occ-0-1-2-13 ≡ input s13
origin-0-1-2-13 = refl
transport-0-1-2-13 : P.T.origin tree-1-0-3 (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-0-1-2-13 = refl
occ-0-1-2-14 : P.T.Occurrence tree-0-1-2
occ-0-1-2-14 = (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-0-1-2-14 : P.T.origin tree-0-1-2 occ-0-1-2-14 ≡ input s23
origin-0-1-2-14 = refl
transport-0-1-2-14 : P.T.origin tree-1-0-3 (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s23)
transport-0-1-2-14 = refl
occ-0-1-2-15 : P.T.Occurrence tree-0-1-2
occ-0-1-2-15 = (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-0-1-2-15 : P.T.origin tree-0-1-2 occ-0-1-2-15 ≡ input s13
origin-0-1-2-15 = refl
transport-0-1-2-15 : P.T.origin tree-1-0-3 (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-0-1-2-15 = refl
occ-0-1-2-16 : P.T.Occurrence tree-0-1-2
occ-0-1-2-16 = (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-0-1-2-16 : P.T.origin tree-0-1-2 occ-0-1-2-16 ≡ input s10
origin-0-1-2-16 = refl
transport-0-1-2-16 : P.T.origin tree-1-0-3 (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s10)
transport-0-1-2-16 = refl
occ-0-1-2-17 : P.T.Occurrence tree-0-1-2
occ-0-1-2-17 = (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-0-1-2-17 : P.T.origin tree-0-1-2 occ-0-1-2-17 ≡ input s20
origin-0-1-2-17 = refl
transport-0-1-2-17 : P.T.origin tree-1-0-3 (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-0-1-2-17 = refl
occ-0-1-2-18 : P.T.Occurrence tree-0-1-2
occ-0-1-2-18 = (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-0-1-2-18 : P.T.origin tree-0-1-2 occ-0-1-2-18 ≡ input s30
origin-0-1-2-18 = refl
transport-0-1-2-18 : P.T.origin tree-1-0-3 (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s30)
transport-0-1-2-18 = refl
occ-0-1-2-19 : P.T.Occurrence tree-0-1-2
occ-0-1-2-19 = (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-0-1-2-19 : P.T.origin tree-0-1-2 occ-0-1-2-19 ≡ input s20
origin-0-1-2-19 = refl
transport-0-1-2-19 : P.T.origin tree-1-0-3 (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-0-1-2-19 = refl
occ-0-1-2-20 : P.T.Occurrence tree-0-1-2
occ-0-1-2-20 = (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.source-leg , tt)))
origin-0-1-2-20 : P.T.origin tree-0-1-2 occ-0-1-2-20 ≡ input s31
origin-0-1-2-20 = refl
transport-0-1-2-20 : P.T.origin tree-1-0-3 (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-0-1-2-20 = refl
occ-0-1-2-21 : P.T.Occurrence tree-0-1-2
occ-0-1-2-21 = (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.target-leg , tt)))
origin-0-1-2-21 : P.T.origin tree-0-1-2 occ-0-1-2-21 ≡ input s01
origin-0-1-2-21 = refl
transport-0-1-2-21 : P.T.origin tree-1-0-3 (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.target-leg , tt))) ≡ input (swap s01)
transport-0-1-2-21 = refl
occ-0-1-2-22 : P.T.Occurrence tree-0-1-2
occ-0-1-2-22 = (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.source-leg , tt)))
origin-0-1-2-22 : P.T.origin tree-0-1-2 occ-0-1-2-22 ≡ input s31
origin-0-1-2-22 = refl
transport-0-1-2-22 : P.T.origin tree-1-0-3 (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-0-1-2-22 = refl
occ-0-1-2-23 : P.T.Occurrence tree-0-1-2
occ-0-1-2-23 = (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.target-leg , tt)))
origin-0-1-2-23 : P.T.origin tree-0-1-2 occ-0-1-2-23 ≡ input s21
origin-0-1-2-23 = refl
transport-0-1-2-23 : P.T.origin tree-1-0-3 (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.target-leg , tt))) ≡ input (swap s21)
transport-0-1-2-23 = refl
occ-0-1-2-24 : P.T.Occurrence tree-0-1-2
occ-0-1-2-24 = (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-0-1-2-24 : P.T.origin tree-0-1-2 occ-0-1-2-24 ≡ input s12
origin-0-1-2-24 = refl
transport-0-1-2-24 : P.T.origin tree-1-0-3 (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s12)
transport-0-1-2-24 = refl
occ-0-1-2-25 : P.T.Occurrence tree-0-1-2
occ-0-1-2-25 = (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-0-1-2-25 : P.T.origin tree-0-1-2 occ-0-1-2-25 ≡ input s02
origin-0-1-2-25 = refl
transport-0-1-2-25 : P.T.origin tree-1-0-3 (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-0-1-2-25 = refl
occ-0-1-2-26 : P.T.Occurrence tree-0-1-2
occ-0-1-2-26 = (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-0-1-2-26 : P.T.origin tree-0-1-2 occ-0-1-2-26 ≡ input s32
origin-0-1-2-26 = refl
transport-0-1-2-26 : P.T.origin tree-1-0-3 (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s32)
transport-0-1-2-26 = refl
occ-0-1-2-27 : P.T.Occurrence tree-0-1-2
occ-0-1-2-27 = (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-0-1-2-27 : P.T.origin tree-0-1-2 occ-0-1-2-27 ≡ input s02
origin-0-1-2-27 = refl
transport-0-1-2-27 : P.T.origin tree-1-0-3 (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-0-1-2-27 = refl
occ-0-1-2-28 : P.T.Occurrence tree-0-1-2
occ-0-1-2-28 = (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.source-leg , tt)))
origin-0-1-2-28 : P.T.origin tree-0-1-2 occ-0-1-2-28 ≡ input s13
origin-0-1-2-28 = refl
transport-0-1-2-28 : P.T.origin tree-1-0-3 (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-0-1-2-28 = refl
occ-0-1-2-29 : P.T.Occurrence tree-0-1-2
occ-0-1-2-29 = (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.target-leg , tt)))
origin-0-1-2-29 : P.T.origin tree-0-1-2 occ-0-1-2-29 ≡ input s03
origin-0-1-2-29 = refl
transport-0-1-2-29 : P.T.origin tree-1-0-3 (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.target-leg , tt))) ≡ input (swap s03)
transport-0-1-2-29 = refl
occ-0-1-2-30 : P.T.Occurrence tree-0-1-2
occ-0-1-2-30 = (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.source-leg , tt)))
origin-0-1-2-30 : P.T.origin tree-0-1-2 occ-0-1-2-30 ≡ input s13
origin-0-1-2-30 = refl
transport-0-1-2-30 : P.T.origin tree-1-0-3 (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-0-1-2-30 = refl
occ-0-1-2-31 : P.T.Occurrence tree-0-1-2
occ-0-1-2-31 = (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.target-leg , tt)))
origin-0-1-2-31 : P.T.origin tree-0-1-2 occ-0-1-2-31 ≡ input s23
origin-0-1-2-31 = refl
transport-0-1-2-31 : P.T.origin tree-1-0-3 (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.target-leg , tt))) ≡ input (swap s23)
transport-0-1-2-31 = refl
occ-0-1-2-32 : P.T.Occurrence tree-0-1-2
occ-0-1-2-32 = (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-0-1-2-32 : P.T.origin tree-0-1-2 occ-0-1-2-32 ≡ input s20
origin-0-1-2-32 = refl
transport-0-1-2-32 : P.T.origin tree-1-0-3 (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-0-1-2-32 = refl
occ-0-1-2-33 : P.T.Occurrence tree-0-1-2
occ-0-1-2-33 = (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-0-1-2-33 : P.T.origin tree-0-1-2 occ-0-1-2-33 ≡ input s20
origin-0-1-2-33 = refl
transport-0-1-2-33 : P.T.origin tree-1-0-3 (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-0-1-2-33 = refl
occ-0-1-2-34 : P.T.Occurrence tree-0-1-2
occ-0-1-2-34 = (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-0-1)) , (P.S.source-leg , tt)))
origin-0-1-2-34 : P.T.origin tree-0-1-2 occ-0-1-2-34 ≡ input s01
origin-0-1-2-34 = refl
transport-0-1-2-34 : P.T.origin tree-1-0-3 (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-1-0)) , (P.S.source-leg , tt))) ≡ input (swap s01)
transport-0-1-2-34 = refl
occ-0-1-2-35 : P.T.Occurrence tree-0-1-2
occ-0-1-2-35 = (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-0-1)) , (P.S.target-leg , tt)))
origin-0-1-2-35 : P.T.origin tree-0-1-2 occ-0-1-2-35 ≡ input s01
origin-0-1-2-35 = refl
transport-0-1-2-35 : P.T.origin tree-1-0-3 (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-1-0)) , (P.S.target-leg , tt))) ≡ input (swap s01)
transport-0-1-2-35 = refl
occ-0-1-2-36 : P.T.Occurrence tree-0-1-2
occ-0-1-2-36 = (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.source-leg , tt)))
origin-0-1-2-36 : P.T.origin tree-0-1-2 occ-0-1-2-36 ≡ input s01
origin-0-1-2-36 = refl
transport-0-1-2-36 : P.T.origin tree-1-0-3 (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.source-leg , tt))) ≡ input (swap s01)
transport-0-1-2-36 = refl
occ-0-1-2-37 : P.T.Occurrence tree-0-1-2
occ-0-1-2-37 = (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.target-leg , tt)))
origin-0-1-2-37 : P.T.origin tree-0-1-2 occ-0-1-2-37 ≡ input s21
origin-0-1-2-37 = refl
transport-0-1-2-37 : P.T.origin tree-1-0-3 (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.target-leg , tt))) ≡ input (swap s21)
transport-0-1-2-37 = refl
occ-0-1-2-38 : P.T.Occurrence tree-0-1-2
occ-0-1-2-38 = (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.source-leg , tt)))
origin-0-1-2-38 : P.T.origin tree-0-1-2 occ-0-1-2-38 ≡ input s21
origin-0-1-2-38 = refl
transport-0-1-2-38 : P.T.origin tree-1-0-3 (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.source-leg , tt))) ≡ input (swap s21)
transport-0-1-2-38 = refl
occ-0-1-2-39 : P.T.Occurrence tree-0-1-2
occ-0-1-2-39 = (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.target-leg , tt)))
origin-0-1-2-39 : P.T.origin tree-0-1-2 occ-0-1-2-39 ≡ input s01
origin-0-1-2-39 = refl
transport-0-1-2-39 : P.T.origin tree-1-0-3 (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.target-leg , tt))) ≡ input (swap s01)
transport-0-1-2-39 = refl
occ-0-1-2-40 : P.T.Occurrence tree-0-1-2
occ-0-1-2-40 = (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-2-1)) , (P.S.source-leg , tt)))
origin-0-1-2-40 : P.T.origin tree-0-1-2 occ-0-1-2-40 ≡ input s21
origin-0-1-2-40 = refl
transport-0-1-2-40 : P.T.origin tree-1-0-3 (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-3-0)) , (P.S.source-leg , tt))) ≡ input (swap s21)
transport-0-1-2-40 = refl
occ-0-1-2-41 : P.T.Occurrence tree-0-1-2
occ-0-1-2-41 = (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-2-1)) , (P.S.target-leg , tt)))
origin-0-1-2-41 : P.T.origin tree-0-1-2 occ-0-1-2-41 ≡ input s21
origin-0-1-2-41 = refl
transport-0-1-2-41 : P.T.origin tree-1-0-3 (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-3-0)) , (P.S.target-leg , tt))) ≡ input (swap s21)
transport-0-1-2-41 = refl
occ-0-1-2-42 : P.T.Occurrence tree-0-1-2
occ-0-1-2-42 = (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-0-1-2-42 : P.T.origin tree-0-1-2 occ-0-1-2-42 ≡ input s02
origin-0-1-2-42 = refl
transport-0-1-2-42 : P.T.origin tree-1-0-3 (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-0-1-2-42 = refl
occ-0-1-2-43 : P.T.Occurrence tree-0-1-2
occ-0-1-2-43 = (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-0-1-2-43 : P.T.origin tree-0-1-2 occ-0-1-2-43 ≡ input s02
origin-0-1-2-43 = refl
transport-0-1-2-43 : P.T.origin tree-1-0-3 (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-0-1-2-43 = refl
occ-0-1-2-44 : P.T.Occurrence tree-0-1-2
occ-0-1-2-44 = (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-0-3)) , (P.S.source-leg , tt)))
origin-0-1-2-44 : P.T.origin tree-0-1-2 occ-0-1-2-44 ≡ input s03
origin-0-1-2-44 = refl
transport-0-1-2-44 : P.T.origin tree-1-0-3 (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-1-2)) , (P.S.source-leg , tt))) ≡ input (swap s03)
transport-0-1-2-44 = refl
occ-0-1-2-45 : P.T.Occurrence tree-0-1-2
occ-0-1-2-45 = (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-0-3)) , (P.S.target-leg , tt)))
origin-0-1-2-45 : P.T.origin tree-0-1-2 occ-0-1-2-45 ≡ input s03
origin-0-1-2-45 = refl
transport-0-1-2-45 : P.T.origin tree-1-0-3 (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-1-2)) , (P.S.target-leg , tt))) ≡ input (swap s03)
transport-0-1-2-45 = refl
occ-0-1-2-46 : P.T.Occurrence tree-0-1-2
occ-0-1-2-46 = (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.source-leg , tt)))
origin-0-1-2-46 : P.T.origin tree-0-1-2 occ-0-1-2-46 ≡ input s03
origin-0-1-2-46 = refl
transport-0-1-2-46 : P.T.origin tree-1-0-3 (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.source-leg , tt))) ≡ input (swap s03)
transport-0-1-2-46 = refl
occ-0-1-2-47 : P.T.Occurrence tree-0-1-2
occ-0-1-2-47 = (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.target-leg , tt)))
origin-0-1-2-47 : P.T.origin tree-0-1-2 occ-0-1-2-47 ≡ input s23
origin-0-1-2-47 = refl
transport-0-1-2-47 : P.T.origin tree-1-0-3 (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.target-leg , tt))) ≡ input (swap s23)
transport-0-1-2-47 = refl
occ-0-1-2-48 : P.T.Occurrence tree-0-1-2
occ-0-1-2-48 = (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.source-leg , tt)))
origin-0-1-2-48 : P.T.origin tree-0-1-2 occ-0-1-2-48 ≡ input s23
origin-0-1-2-48 = refl
transport-0-1-2-48 : P.T.origin tree-1-0-3 (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.source-leg , tt))) ≡ input (swap s23)
transport-0-1-2-48 = refl
occ-0-1-2-49 : P.T.Occurrence tree-0-1-2
occ-0-1-2-49 = (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.target-leg , tt)))
origin-0-1-2-49 : P.T.origin tree-0-1-2 occ-0-1-2-49 ≡ input s03
origin-0-1-2-49 = refl
transport-0-1-2-49 : P.T.origin tree-1-0-3 (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.target-leg , tt))) ≡ input (swap s03)
transport-0-1-2-49 = refl
occ-0-1-2-50 : P.T.Occurrence tree-0-1-2
occ-0-1-2-50 = (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-2-3)) , (P.S.source-leg , tt)))
origin-0-1-2-50 : P.T.origin tree-0-1-2 occ-0-1-2-50 ≡ input s23
origin-0-1-2-50 = refl
transport-0-1-2-50 : P.T.origin tree-1-0-3 (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-3-2)) , (P.S.source-leg , tt))) ≡ input (swap s23)
transport-0-1-2-50 = refl
occ-0-1-2-51 : P.T.Occurrence tree-0-1-2
occ-0-1-2-51 = (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-2-3)) , (P.S.target-leg , tt)))
origin-0-1-2-51 : P.T.origin tree-0-1-2 occ-0-1-2-51 ≡ input s23
origin-0-1-2-51 = refl
transport-0-1-2-51 : P.T.origin tree-1-0-3 (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-3-2)) , (P.S.target-leg , tt))) ≡ input (swap s23)
transport-0-1-2-51 = refl
occ-0-1-2-52 : P.T.Occurrence tree-0-1-2
occ-0-1-2-52 = (P.S.full-source , (P.S.first-port , tt))
origin-0-1-2-52 : P.T.origin tree-0-1-2 occ-0-1-2-52 ≡ input s03
origin-0-1-2-52 = refl
transport-0-1-2-52 : P.T.origin tree-1-0-3 (P.S.full-source , (P.S.first-port , tt)) ≡ input (swap s03)
transport-0-1-2-52 = refl
occ-0-1-2-53 : P.T.Occurrence tree-0-1-2
occ-0-1-2-53 = (P.S.full-source , (P.S.middle-port , tt))
origin-0-1-2-53 : P.T.origin tree-0-1-2 occ-0-1-2-53 ≡ input s13
origin-0-1-2-53 = refl
transport-0-1-2-53 : P.T.origin tree-1-0-3 (P.S.full-source , (P.S.middle-port , tt)) ≡ input (swap s13)
transport-0-1-2-53 = refl
occ-0-1-2-54 : P.T.Occurrence tree-0-1-2
occ-0-1-2-54 = (P.S.full-source , (P.S.final-port , tt))
origin-0-1-2-54 : P.T.origin tree-0-1-2 occ-0-1-2-54 ≡ input s23
origin-0-1-2-54 = refl
transport-0-1-2-54 : P.T.origin tree-1-0-3 (P.S.full-source , (P.S.final-port , tt)) ≡ input (swap s23)
transport-0-1-2-54 = refl
selected-source-0-1-2-AB : P.S.ab-index {a = C.q0} {b = C.q7} {c = C.q0} F.triple-0-1-2 ≡ (m1 , (F.vp-0-3 , F.vp-1-3))
selected-source-0-1-2-AB = refl
selected-target-0-1-2-AB : P.S.ab-index {a = C.q7} {b = C.q0} {c = C.q7} F.triple-1-0-3 ≡ (c1 , (F.vp-1-2 , F.vp-0-2))
selected-target-0-1-2-AB = refl
selected-source-0-1-2-BC : P.S.bc-index {a = C.q0} {b = C.q7} {c = C.q0} F.triple-0-1-2 ≡ (m1 , (F.vp-1-3 , F.vp-2-3))
selected-source-0-1-2-BC = refl
selected-target-0-1-2-BC : P.S.bc-index {a = C.q7} {b = C.q0} {c = C.q7} F.triple-1-0-3 ≡ (c1 , (F.vp-0-2 , F.vp-3-2))
selected-target-0-1-2-BC = refl
selected-source-0-1-2-AC : P.S.ac-index {a = C.q0} {b = C.q7} {c = C.q0} F.triple-0-1-2 ≡ (m1 , (F.vp-0-3 , F.vp-2-3))
selected-source-0-1-2-AC = refl
selected-target-0-1-2-AC : P.S.ac-index {a = C.q7} {b = C.q0} {c = C.q7} F.triple-1-0-3 ≡ (c1 , (F.vp-1-2 , F.vp-3-2))
selected-target-0-1-2-AC = refl
occ-0-1-3-0 : P.T.Occurrence tree-0-1-3
occ-0-1-3-0 = (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.source-leg , tt)))
origin-0-1-3-0 : P.T.origin tree-0-1-3 occ-0-1-3-0 ≡ input s20
origin-0-1-3-0 = refl
transport-0-1-3-0 : P.T.origin tree-1-0-2 (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-0-1-3-0 = refl
occ-0-1-3-1 : P.T.Occurrence tree-0-1-3
occ-0-1-3-1 = (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.target-leg , tt)))
origin-0-1-3-1 : P.T.origin tree-0-1-3 occ-0-1-3-1 ≡ input s10
origin-0-1-3-1 = refl
transport-0-1-3-1 : P.T.origin tree-1-0-2 (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.target-leg , tt))) ≡ input (swap s10)
transport-0-1-3-1 = refl
occ-0-1-3-2 : P.T.Occurrence tree-0-1-3
occ-0-1-3-2 = (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.source-leg , tt)))
origin-0-1-3-2 : P.T.origin tree-0-1-3 occ-0-1-3-2 ≡ input s20
origin-0-1-3-2 = refl
transport-0-1-3-2 : P.T.origin tree-1-0-2 (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-0-1-3-2 = refl
occ-0-1-3-3 : P.T.Occurrence tree-0-1-3
occ-0-1-3-3 = (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.target-leg , tt)))
origin-0-1-3-3 : P.T.origin tree-0-1-3 occ-0-1-3-3 ≡ input s30
origin-0-1-3-3 = refl
transport-0-1-3-3 : P.T.origin tree-1-0-2 (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.target-leg , tt))) ≡ input (swap s30)
transport-0-1-3-3 = refl
occ-0-1-3-4 : P.T.Occurrence tree-0-1-3
occ-0-1-3-4 = (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-0-1-3-4 : P.T.origin tree-0-1-3 occ-0-1-3-4 ≡ input s01
origin-0-1-3-4 = refl
transport-0-1-3-4 : P.T.origin tree-1-0-2 (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s01)
transport-0-1-3-4 = refl
occ-0-1-3-5 : P.T.Occurrence tree-0-1-3
occ-0-1-3-5 = (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-0-1-3-5 : P.T.origin tree-0-1-3 occ-0-1-3-5 ≡ input s31
origin-0-1-3-5 = refl
transport-0-1-3-5 : P.T.origin tree-1-0-2 (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-0-1-3-5 = refl
occ-0-1-3-6 : P.T.Occurrence tree-0-1-3
occ-0-1-3-6 = (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-0-1-3-6 : P.T.origin tree-0-1-3 occ-0-1-3-6 ≡ input s21
origin-0-1-3-6 = refl
transport-0-1-3-6 : P.T.origin tree-1-0-2 (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s21)
transport-0-1-3-6 = refl
occ-0-1-3-7 : P.T.Occurrence tree-0-1-3
occ-0-1-3-7 = (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-0-1-3-7 : P.T.origin tree-0-1-3 occ-0-1-3-7 ≡ input s31
origin-0-1-3-7 = refl
transport-0-1-3-7 : P.T.origin tree-1-0-2 (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-0-1-3-7 = refl
occ-0-1-3-8 : P.T.Occurrence tree-0-1-3
occ-0-1-3-8 = (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.source-leg , tt)))
origin-0-1-3-8 : P.T.origin tree-0-1-3 occ-0-1-3-8 ≡ input s02
origin-0-1-3-8 = refl
transport-0-1-3-8 : P.T.origin tree-1-0-2 (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-0-1-3-8 = refl
occ-0-1-3-9 : P.T.Occurrence tree-0-1-3
occ-0-1-3-9 = (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.target-leg , tt)))
origin-0-1-3-9 : P.T.origin tree-0-1-3 occ-0-1-3-9 ≡ input s12
origin-0-1-3-9 = refl
transport-0-1-3-9 : P.T.origin tree-1-0-2 (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.target-leg , tt))) ≡ input (swap s12)
transport-0-1-3-9 = refl
occ-0-1-3-10 : P.T.Occurrence tree-0-1-3
occ-0-1-3-10 = (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.source-leg , tt)))
origin-0-1-3-10 : P.T.origin tree-0-1-3 occ-0-1-3-10 ≡ input s02
origin-0-1-3-10 = refl
transport-0-1-3-10 : P.T.origin tree-1-0-2 (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-0-1-3-10 = refl
occ-0-1-3-11 : P.T.Occurrence tree-0-1-3
occ-0-1-3-11 = (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.target-leg , tt)))
origin-0-1-3-11 : P.T.origin tree-0-1-3 occ-0-1-3-11 ≡ input s32
origin-0-1-3-11 = refl
transport-0-1-3-11 : P.T.origin tree-1-0-2 (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.target-leg , tt))) ≡ input (swap s32)
transport-0-1-3-11 = refl
occ-0-1-3-12 : P.T.Occurrence tree-0-1-3
occ-0-1-3-12 = (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-0-1-3-12 : P.T.origin tree-0-1-3 occ-0-1-3-12 ≡ input s03
origin-0-1-3-12 = refl
transport-0-1-3-12 : P.T.origin tree-1-0-2 (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s03)
transport-0-1-3-12 = refl
occ-0-1-3-13 : P.T.Occurrence tree-0-1-3
occ-0-1-3-13 = (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-0-1-3-13 : P.T.origin tree-0-1-3 occ-0-1-3-13 ≡ input s13
origin-0-1-3-13 = refl
transport-0-1-3-13 : P.T.origin tree-1-0-2 (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-0-1-3-13 = refl
occ-0-1-3-14 : P.T.Occurrence tree-0-1-3
occ-0-1-3-14 = (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-0-1-3-14 : P.T.origin tree-0-1-3 occ-0-1-3-14 ≡ input s23
origin-0-1-3-14 = refl
transport-0-1-3-14 : P.T.origin tree-1-0-2 (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s23)
transport-0-1-3-14 = refl
occ-0-1-3-15 : P.T.Occurrence tree-0-1-3
occ-0-1-3-15 = (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-0-1-3-15 : P.T.origin tree-0-1-3 occ-0-1-3-15 ≡ input s13
origin-0-1-3-15 = refl
transport-0-1-3-15 : P.T.origin tree-1-0-2 (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-0-1-3-15 = refl
occ-0-1-3-16 : P.T.Occurrence tree-0-1-3
occ-0-1-3-16 = (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-1-0)) , (P.S.source-leg , tt)))
origin-0-1-3-16 : P.T.origin tree-0-1-3 occ-0-1-3-16 ≡ input s10
origin-0-1-3-16 = refl
transport-0-1-3-16 : P.T.origin tree-1-0-2 (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-0-1)) , (P.S.source-leg , tt))) ≡ input (swap s10)
transport-0-1-3-16 = refl
occ-0-1-3-17 : P.T.Occurrence tree-0-1-3
occ-0-1-3-17 = (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-1-0)) , (P.S.target-leg , tt)))
origin-0-1-3-17 : P.T.origin tree-0-1-3 occ-0-1-3-17 ≡ input s10
origin-0-1-3-17 = refl
transport-0-1-3-17 : P.T.origin tree-1-0-2 (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-0-1)) , (P.S.target-leg , tt))) ≡ input (swap s10)
transport-0-1-3-17 = refl
occ-0-1-3-18 : P.T.Occurrence tree-0-1-3
occ-0-1-3-18 = (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.source-leg , tt)))
origin-0-1-3-18 : P.T.origin tree-0-1-3 occ-0-1-3-18 ≡ input s10
origin-0-1-3-18 = refl
transport-0-1-3-18 : P.T.origin tree-1-0-2 (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.source-leg , tt))) ≡ input (swap s10)
transport-0-1-3-18 = refl
occ-0-1-3-19 : P.T.Occurrence tree-0-1-3
occ-0-1-3-19 = (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.target-leg , tt)))
origin-0-1-3-19 : P.T.origin tree-0-1-3 occ-0-1-3-19 ≡ input s30
origin-0-1-3-19 = refl
transport-0-1-3-19 : P.T.origin tree-1-0-2 (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.target-leg , tt))) ≡ input (swap s30)
transport-0-1-3-19 = refl
occ-0-1-3-20 : P.T.Occurrence tree-0-1-3
occ-0-1-3-20 = (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.source-leg , tt)))
origin-0-1-3-20 : P.T.origin tree-0-1-3 occ-0-1-3-20 ≡ input s30
origin-0-1-3-20 = refl
transport-0-1-3-20 : P.T.origin tree-1-0-2 (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.source-leg , tt))) ≡ input (swap s30)
transport-0-1-3-20 = refl
occ-0-1-3-21 : P.T.Occurrence tree-0-1-3
occ-0-1-3-21 = (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.target-leg , tt)))
origin-0-1-3-21 : P.T.origin tree-0-1-3 occ-0-1-3-21 ≡ input s10
origin-0-1-3-21 = refl
transport-0-1-3-21 : P.T.origin tree-1-0-2 (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.target-leg , tt))) ≡ input (swap s10)
transport-0-1-3-21 = refl
occ-0-1-3-22 : P.T.Occurrence tree-0-1-3
occ-0-1-3-22 = (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-3-0)) , (P.S.source-leg , tt)))
origin-0-1-3-22 : P.T.origin tree-0-1-3 occ-0-1-3-22 ≡ input s30
origin-0-1-3-22 = refl
transport-0-1-3-22 : P.T.origin tree-1-0-2 (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-2-1)) , (P.S.source-leg , tt))) ≡ input (swap s30)
transport-0-1-3-22 = refl
occ-0-1-3-23 : P.T.Occurrence tree-0-1-3
occ-0-1-3-23 = (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-3-0)) , (P.S.target-leg , tt)))
origin-0-1-3-23 : P.T.origin tree-0-1-3 occ-0-1-3-23 ≡ input s30
origin-0-1-3-23 = refl
transport-0-1-3-23 : P.T.origin tree-1-0-2 (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-2-1)) , (P.S.target-leg , tt))) ≡ input (swap s30)
transport-0-1-3-23 = refl
occ-0-1-3-24 : P.T.Occurrence tree-0-1-3
occ-0-1-3-24 = (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-0-1-3-24 : P.T.origin tree-0-1-3 occ-0-1-3-24 ≡ input s31
origin-0-1-3-24 = refl
transport-0-1-3-24 : P.T.origin tree-1-0-2 (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-0-1-3-24 = refl
occ-0-1-3-25 : P.T.Occurrence tree-0-1-3
occ-0-1-3-25 = (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-0-1-3-25 : P.T.origin tree-0-1-3 occ-0-1-3-25 ≡ input s31
origin-0-1-3-25 = refl
transport-0-1-3-25 : P.T.origin tree-1-0-2 (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-0-1-3-25 = refl
occ-0-1-3-26 : P.T.Occurrence tree-0-1-3
occ-0-1-3-26 = (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-1-2)) , (P.S.source-leg , tt)))
origin-0-1-3-26 : P.T.origin tree-0-1-3 occ-0-1-3-26 ≡ input s12
origin-0-1-3-26 = refl
transport-0-1-3-26 : P.T.origin tree-1-0-2 (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-0-3)) , (P.S.source-leg , tt))) ≡ input (swap s12)
transport-0-1-3-26 = refl
occ-0-1-3-27 : P.T.Occurrence tree-0-1-3
occ-0-1-3-27 = (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-1-2)) , (P.S.target-leg , tt)))
origin-0-1-3-27 : P.T.origin tree-0-1-3 occ-0-1-3-27 ≡ input s12
origin-0-1-3-27 = refl
transport-0-1-3-27 : P.T.origin tree-1-0-2 (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-0-3)) , (P.S.target-leg , tt))) ≡ input (swap s12)
transport-0-1-3-27 = refl
occ-0-1-3-28 : P.T.Occurrence tree-0-1-3
occ-0-1-3-28 = (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.source-leg , tt)))
origin-0-1-3-28 : P.T.origin tree-0-1-3 occ-0-1-3-28 ≡ input s12
origin-0-1-3-28 = refl
transport-0-1-3-28 : P.T.origin tree-1-0-2 (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.source-leg , tt))) ≡ input (swap s12)
transport-0-1-3-28 = refl
occ-0-1-3-29 : P.T.Occurrence tree-0-1-3
occ-0-1-3-29 = (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.target-leg , tt)))
origin-0-1-3-29 : P.T.origin tree-0-1-3 occ-0-1-3-29 ≡ input s32
origin-0-1-3-29 = refl
transport-0-1-3-29 : P.T.origin tree-1-0-2 (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.target-leg , tt))) ≡ input (swap s32)
transport-0-1-3-29 = refl
occ-0-1-3-30 : P.T.Occurrence tree-0-1-3
occ-0-1-3-30 = (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.source-leg , tt)))
origin-0-1-3-30 : P.T.origin tree-0-1-3 occ-0-1-3-30 ≡ input s32
origin-0-1-3-30 = refl
transport-0-1-3-30 : P.T.origin tree-1-0-2 (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.source-leg , tt))) ≡ input (swap s32)
transport-0-1-3-30 = refl
occ-0-1-3-31 : P.T.Occurrence tree-0-1-3
occ-0-1-3-31 = (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.target-leg , tt)))
origin-0-1-3-31 : P.T.origin tree-0-1-3 occ-0-1-3-31 ≡ input s12
origin-0-1-3-31 = refl
transport-0-1-3-31 : P.T.origin tree-1-0-2 (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.target-leg , tt))) ≡ input (swap s12)
transport-0-1-3-31 = refl
occ-0-1-3-32 : P.T.Occurrence tree-0-1-3
occ-0-1-3-32 = (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-3-2)) , (P.S.source-leg , tt)))
origin-0-1-3-32 : P.T.origin tree-0-1-3 occ-0-1-3-32 ≡ input s32
origin-0-1-3-32 = refl
transport-0-1-3-32 : P.T.origin tree-1-0-2 (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-2-3)) , (P.S.source-leg , tt))) ≡ input (swap s32)
transport-0-1-3-32 = refl
occ-0-1-3-33 : P.T.Occurrence tree-0-1-3
occ-0-1-3-33 = (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-3-2)) , (P.S.target-leg , tt)))
origin-0-1-3-33 : P.T.origin tree-0-1-3 occ-0-1-3-33 ≡ input s32
origin-0-1-3-33 = refl
transport-0-1-3-33 : P.T.origin tree-1-0-2 (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-2-3)) , (P.S.target-leg , tt))) ≡ input (swap s32)
transport-0-1-3-33 = refl
occ-0-1-3-34 : P.T.Occurrence tree-0-1-3
occ-0-1-3-34 = (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-0-1-3-34 : P.T.origin tree-0-1-3 occ-0-1-3-34 ≡ input s13
origin-0-1-3-34 = refl
transport-0-1-3-34 : P.T.origin tree-1-0-2 (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-0-1-3-34 = refl
occ-0-1-3-35 : P.T.Occurrence tree-0-1-3
occ-0-1-3-35 = (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-0-1-3-35 : P.T.origin tree-0-1-3 occ-0-1-3-35 ≡ input s13
origin-0-1-3-35 = refl
transport-0-1-3-35 : P.T.origin tree-1-0-2 (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-0-1-3-35 = refl
occ-0-1-3-36 : P.T.Occurrence tree-0-1-3
occ-0-1-3-36 = (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.source-leg , tt)))
origin-0-1-3-36 : P.T.origin tree-0-1-3 occ-0-1-3-36 ≡ input s20
origin-0-1-3-36 = refl
transport-0-1-3-36 : P.T.origin tree-1-0-2 (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-0-1-3-36 = refl
occ-0-1-3-37 : P.T.Occurrence tree-0-1-3
occ-0-1-3-37 = (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.target-leg , tt)))
origin-0-1-3-37 : P.T.origin tree-0-1-3 occ-0-1-3-37 ≡ input s10
origin-0-1-3-37 = refl
transport-0-1-3-37 : P.T.origin tree-1-0-2 (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.target-leg , tt))) ≡ input (swap s10)
transport-0-1-3-37 = refl
occ-0-1-3-38 : P.T.Occurrence tree-0-1-3
occ-0-1-3-38 = (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.source-leg , tt)))
origin-0-1-3-38 : P.T.origin tree-0-1-3 occ-0-1-3-38 ≡ input s20
origin-0-1-3-38 = refl
transport-0-1-3-38 : P.T.origin tree-1-0-2 (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-0-1-3-38 = refl
occ-0-1-3-39 : P.T.Occurrence tree-0-1-3
occ-0-1-3-39 = (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.target-leg , tt)))
origin-0-1-3-39 : P.T.origin tree-0-1-3 occ-0-1-3-39 ≡ input s30
origin-0-1-3-39 = refl
transport-0-1-3-39 : P.T.origin tree-1-0-2 (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.target-leg , tt))) ≡ input (swap s30)
transport-0-1-3-39 = refl
occ-0-1-3-40 : P.T.Occurrence tree-0-1-3
occ-0-1-3-40 = (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-0-1-3-40 : P.T.origin tree-0-1-3 occ-0-1-3-40 ≡ input s01
origin-0-1-3-40 = refl
transport-0-1-3-40 : P.T.origin tree-1-0-2 (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s01)
transport-0-1-3-40 = refl
occ-0-1-3-41 : P.T.Occurrence tree-0-1-3
occ-0-1-3-41 = (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-0-1-3-41 : P.T.origin tree-0-1-3 occ-0-1-3-41 ≡ input s31
origin-0-1-3-41 = refl
transport-0-1-3-41 : P.T.origin tree-1-0-2 (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-0-1-3-41 = refl
occ-0-1-3-42 : P.T.Occurrence tree-0-1-3
occ-0-1-3-42 = (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-0-1-3-42 : P.T.origin tree-0-1-3 occ-0-1-3-42 ≡ input s21
origin-0-1-3-42 = refl
transport-0-1-3-42 : P.T.origin tree-1-0-2 (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s21)
transport-0-1-3-42 = refl
occ-0-1-3-43 : P.T.Occurrence tree-0-1-3
occ-0-1-3-43 = (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-0-1-3-43 : P.T.origin tree-0-1-3 occ-0-1-3-43 ≡ input s31
origin-0-1-3-43 = refl
transport-0-1-3-43 : P.T.origin tree-1-0-2 (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-0-1-3-43 = refl
occ-0-1-3-44 : P.T.Occurrence tree-0-1-3
occ-0-1-3-44 = (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.source-leg , tt)))
origin-0-1-3-44 : P.T.origin tree-0-1-3 occ-0-1-3-44 ≡ input s02
origin-0-1-3-44 = refl
transport-0-1-3-44 : P.T.origin tree-1-0-2 (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-0-1-3-44 = refl
occ-0-1-3-45 : P.T.Occurrence tree-0-1-3
occ-0-1-3-45 = (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.target-leg , tt)))
origin-0-1-3-45 : P.T.origin tree-0-1-3 occ-0-1-3-45 ≡ input s12
origin-0-1-3-45 = refl
transport-0-1-3-45 : P.T.origin tree-1-0-2 (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.target-leg , tt))) ≡ input (swap s12)
transport-0-1-3-45 = refl
occ-0-1-3-46 : P.T.Occurrence tree-0-1-3
occ-0-1-3-46 = (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.source-leg , tt)))
origin-0-1-3-46 : P.T.origin tree-0-1-3 occ-0-1-3-46 ≡ input s02
origin-0-1-3-46 = refl
transport-0-1-3-46 : P.T.origin tree-1-0-2 (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-0-1-3-46 = refl
occ-0-1-3-47 : P.T.Occurrence tree-0-1-3
occ-0-1-3-47 = (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.target-leg , tt)))
origin-0-1-3-47 : P.T.origin tree-0-1-3 occ-0-1-3-47 ≡ input s32
origin-0-1-3-47 = refl
transport-0-1-3-47 : P.T.origin tree-1-0-2 (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.target-leg , tt))) ≡ input (swap s32)
transport-0-1-3-47 = refl
occ-0-1-3-48 : P.T.Occurrence tree-0-1-3
occ-0-1-3-48 = (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-0-1-3-48 : P.T.origin tree-0-1-3 occ-0-1-3-48 ≡ input s03
origin-0-1-3-48 = refl
transport-0-1-3-48 : P.T.origin tree-1-0-2 (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s03)
transport-0-1-3-48 = refl
occ-0-1-3-49 : P.T.Occurrence tree-0-1-3
occ-0-1-3-49 = (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-0-1-3-49 : P.T.origin tree-0-1-3 occ-0-1-3-49 ≡ input s13
origin-0-1-3-49 = refl
transport-0-1-3-49 : P.T.origin tree-1-0-2 (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-0-1-3-49 = refl
occ-0-1-3-50 : P.T.Occurrence tree-0-1-3
occ-0-1-3-50 = (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-0-1-3-50 : P.T.origin tree-0-1-3 occ-0-1-3-50 ≡ input s23
origin-0-1-3-50 = refl
transport-0-1-3-50 : P.T.origin tree-1-0-2 (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s23)
transport-0-1-3-50 = refl
occ-0-1-3-51 : P.T.Occurrence tree-0-1-3
occ-0-1-3-51 = (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-0-1-3-51 : P.T.origin tree-0-1-3 occ-0-1-3-51 ≡ input s13
origin-0-1-3-51 = refl
transport-0-1-3-51 : P.T.origin tree-1-0-2 (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-0-1-3-51 = refl
occ-0-1-3-52 : P.T.Occurrence tree-0-1-3
occ-0-1-3-52 = (P.S.full-source , (P.S.first-port , tt))
origin-0-1-3-52 : P.T.origin tree-0-1-3 occ-0-1-3-52 ≡ input s02
origin-0-1-3-52 = refl
transport-0-1-3-52 : P.T.origin tree-1-0-2 (P.S.full-source , (P.S.first-port , tt)) ≡ input (swap s02)
transport-0-1-3-52 = refl
occ-0-1-3-53 : P.T.Occurrence tree-0-1-3
occ-0-1-3-53 = (P.S.full-source , (P.S.middle-port , tt))
origin-0-1-3-53 : P.T.origin tree-0-1-3 occ-0-1-3-53 ≡ input s12
origin-0-1-3-53 = refl
transport-0-1-3-53 : P.T.origin tree-1-0-2 (P.S.full-source , (P.S.middle-port , tt)) ≡ input (swap s12)
transport-0-1-3-53 = refl
occ-0-1-3-54 : P.T.Occurrence tree-0-1-3
occ-0-1-3-54 = (P.S.full-source , (P.S.final-port , tt))
origin-0-1-3-54 : P.T.origin tree-0-1-3 occ-0-1-3-54 ≡ input s32
origin-0-1-3-54 = refl
transport-0-1-3-54 : P.T.origin tree-1-0-2 (P.S.full-source , (P.S.final-port , tt)) ≡ input (swap s32)
transport-0-1-3-54 = refl
selected-source-0-1-3-AB : P.S.ab-index {a = C.q0} {b = C.q7} {c = C.q7} F.triple-0-1-3 ≡ (c1 , (F.vp-0-2 , F.vp-1-2))
selected-source-0-1-3-AB = refl
selected-target-0-1-3-AB : P.S.ab-index {a = C.q7} {b = C.q0} {c = C.q0} F.triple-1-0-2 ≡ (m1 , (F.vp-1-3 , F.vp-0-3))
selected-target-0-1-3-AB = refl
selected-source-0-1-3-BC : P.S.bc-index {a = C.q0} {b = C.q7} {c = C.q7} F.triple-0-1-3 ≡ (c1 , (F.vp-1-2 , F.vp-3-2))
selected-source-0-1-3-BC = refl
selected-target-0-1-3-BC : P.S.bc-index {a = C.q7} {b = C.q0} {c = C.q0} F.triple-1-0-2 ≡ (m1 , (F.vp-0-3 , F.vp-2-3))
selected-target-0-1-3-BC = refl
selected-source-0-1-3-AC : P.S.ac-index {a = C.q0} {b = C.q7} {c = C.q7} F.triple-0-1-3 ≡ (c1 , (F.vp-0-2 , F.vp-3-2))
selected-source-0-1-3-AC = refl
selected-target-0-1-3-AC : P.S.ac-index {a = C.q7} {b = C.q0} {c = C.q0} F.triple-1-0-2 ≡ (m1 , (F.vp-1-3 , F.vp-2-3))
selected-target-0-1-3-AC = refl
occ-0-2-1-0 : P.T.Occurrence tree-0-2-1
occ-0-2-1-0 = (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-0-2-1-0 : P.T.origin tree-0-2-1 occ-0-2-1-0 ≡ input s20
origin-0-2-1-0 = refl
transport-0-2-1-0 : P.T.origin tree-1-3-0 (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-0-2-1-0 = refl
occ-0-2-1-1 : P.T.Occurrence tree-0-2-1
occ-0-2-1-1 = (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-0-2-1-1 : P.T.origin tree-0-2-1 occ-0-2-1-1 ≡ input s20
origin-0-2-1-1 = refl
transport-0-2-1-1 : P.T.origin tree-1-3-0 (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-0-2-1-1 = refl
occ-0-2-1-2 : P.T.Occurrence tree-0-2-1
occ-0-2-1-2 = (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-0-1)) , (P.S.source-leg , tt)))
origin-0-2-1-2 : P.T.origin tree-0-2-1 occ-0-2-1-2 ≡ input s01
origin-0-2-1-2 = refl
transport-0-2-1-2 : P.T.origin tree-1-3-0 (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-1-0)) , (P.S.source-leg , tt))) ≡ input (swap s01)
transport-0-2-1-2 = refl
occ-0-2-1-3 : P.T.Occurrence tree-0-2-1
occ-0-2-1-3 = (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-0-1)) , (P.S.target-leg , tt)))
origin-0-2-1-3 : P.T.origin tree-0-2-1 occ-0-2-1-3 ≡ input s01
origin-0-2-1-3 = refl
transport-0-2-1-3 : P.T.origin tree-1-3-0 (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-1-0)) , (P.S.target-leg , tt))) ≡ input (swap s01)
transport-0-2-1-3 = refl
occ-0-2-1-4 : P.T.Occurrence tree-0-2-1
occ-0-2-1-4 = (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.source-leg , tt)))
origin-0-2-1-4 : P.T.origin tree-0-2-1 occ-0-2-1-4 ≡ input s01
origin-0-2-1-4 = refl
transport-0-2-1-4 : P.T.origin tree-1-3-0 (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.source-leg , tt))) ≡ input (swap s01)
transport-0-2-1-4 = refl
occ-0-2-1-5 : P.T.Occurrence tree-0-2-1
occ-0-2-1-5 = (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.target-leg , tt)))
origin-0-2-1-5 : P.T.origin tree-0-2-1 occ-0-2-1-5 ≡ input s21
origin-0-2-1-5 = refl
transport-0-2-1-5 : P.T.origin tree-1-3-0 (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.target-leg , tt))) ≡ input (swap s21)
transport-0-2-1-5 = refl
occ-0-2-1-6 : P.T.Occurrence tree-0-2-1
occ-0-2-1-6 = (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.source-leg , tt)))
origin-0-2-1-6 : P.T.origin tree-0-2-1 occ-0-2-1-6 ≡ input s21
origin-0-2-1-6 = refl
transport-0-2-1-6 : P.T.origin tree-1-3-0 (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.source-leg , tt))) ≡ input (swap s21)
transport-0-2-1-6 = refl
occ-0-2-1-7 : P.T.Occurrence tree-0-2-1
occ-0-2-1-7 = (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.target-leg , tt)))
origin-0-2-1-7 : P.T.origin tree-0-2-1 occ-0-2-1-7 ≡ input s01
origin-0-2-1-7 = refl
transport-0-2-1-7 : P.T.origin tree-1-3-0 (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.target-leg , tt))) ≡ input (swap s01)
transport-0-2-1-7 = refl
occ-0-2-1-8 : P.T.Occurrence tree-0-2-1
occ-0-2-1-8 = (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-2-1)) , (P.S.source-leg , tt)))
origin-0-2-1-8 : P.T.origin tree-0-2-1 occ-0-2-1-8 ≡ input s21
origin-0-2-1-8 = refl
transport-0-2-1-8 : P.T.origin tree-1-3-0 (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-3-0)) , (P.S.source-leg , tt))) ≡ input (swap s21)
transport-0-2-1-8 = refl
occ-0-2-1-9 : P.T.Occurrence tree-0-2-1
occ-0-2-1-9 = (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-2-1)) , (P.S.target-leg , tt)))
origin-0-2-1-9 : P.T.origin tree-0-2-1 occ-0-2-1-9 ≡ input s21
origin-0-2-1-9 = refl
transport-0-2-1-9 : P.T.origin tree-1-3-0 (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-3-0)) , (P.S.target-leg , tt))) ≡ input (swap s21)
transport-0-2-1-9 = refl
occ-0-2-1-10 : P.T.Occurrence tree-0-2-1
occ-0-2-1-10 = (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-0-2-1-10 : P.T.origin tree-0-2-1 occ-0-2-1-10 ≡ input s02
origin-0-2-1-10 = refl
transport-0-2-1-10 : P.T.origin tree-1-3-0 (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-0-2-1-10 = refl
occ-0-2-1-11 : P.T.Occurrence tree-0-2-1
occ-0-2-1-11 = (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-0-2-1-11 : P.T.origin tree-0-2-1 occ-0-2-1-11 ≡ input s02
origin-0-2-1-11 = refl
transport-0-2-1-11 : P.T.origin tree-1-3-0 (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-0-2-1-11 = refl
occ-0-2-1-12 : P.T.Occurrence tree-0-2-1
occ-0-2-1-12 = (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-0-3)) , (P.S.source-leg , tt)))
origin-0-2-1-12 : P.T.origin tree-0-2-1 occ-0-2-1-12 ≡ input s03
origin-0-2-1-12 = refl
transport-0-2-1-12 : P.T.origin tree-1-3-0 (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-1-2)) , (P.S.source-leg , tt))) ≡ input (swap s03)
transport-0-2-1-12 = refl
occ-0-2-1-13 : P.T.Occurrence tree-0-2-1
occ-0-2-1-13 = (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-0-3)) , (P.S.target-leg , tt)))
origin-0-2-1-13 : P.T.origin tree-0-2-1 occ-0-2-1-13 ≡ input s03
origin-0-2-1-13 = refl
transport-0-2-1-13 : P.T.origin tree-1-3-0 (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-1-2)) , (P.S.target-leg , tt))) ≡ input (swap s03)
transport-0-2-1-13 = refl
occ-0-2-1-14 : P.T.Occurrence tree-0-2-1
occ-0-2-1-14 = (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.source-leg , tt)))
origin-0-2-1-14 : P.T.origin tree-0-2-1 occ-0-2-1-14 ≡ input s03
origin-0-2-1-14 = refl
transport-0-2-1-14 : P.T.origin tree-1-3-0 (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.source-leg , tt))) ≡ input (swap s03)
transport-0-2-1-14 = refl
occ-0-2-1-15 : P.T.Occurrence tree-0-2-1
occ-0-2-1-15 = (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.target-leg , tt)))
origin-0-2-1-15 : P.T.origin tree-0-2-1 occ-0-2-1-15 ≡ input s23
origin-0-2-1-15 = refl
transport-0-2-1-15 : P.T.origin tree-1-3-0 (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.target-leg , tt))) ≡ input (swap s23)
transport-0-2-1-15 = refl
occ-0-2-1-16 : P.T.Occurrence tree-0-2-1
occ-0-2-1-16 = (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.source-leg , tt)))
origin-0-2-1-16 : P.T.origin tree-0-2-1 occ-0-2-1-16 ≡ input s23
origin-0-2-1-16 = refl
transport-0-2-1-16 : P.T.origin tree-1-3-0 (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.source-leg , tt))) ≡ input (swap s23)
transport-0-2-1-16 = refl
occ-0-2-1-17 : P.T.Occurrence tree-0-2-1
occ-0-2-1-17 = (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.target-leg , tt)))
origin-0-2-1-17 : P.T.origin tree-0-2-1 occ-0-2-1-17 ≡ input s03
origin-0-2-1-17 = refl
transport-0-2-1-17 : P.T.origin tree-1-3-0 (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.target-leg , tt))) ≡ input (swap s03)
transport-0-2-1-17 = refl
occ-0-2-1-18 : P.T.Occurrence tree-0-2-1
occ-0-2-1-18 = (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-2-3)) , (P.S.source-leg , tt)))
origin-0-2-1-18 : P.T.origin tree-0-2-1 occ-0-2-1-18 ≡ input s23
origin-0-2-1-18 = refl
transport-0-2-1-18 : P.T.origin tree-1-3-0 (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-3-2)) , (P.S.source-leg , tt))) ≡ input (swap s23)
transport-0-2-1-18 = refl
occ-0-2-1-19 : P.T.Occurrence tree-0-2-1
occ-0-2-1-19 = (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-2-3)) , (P.S.target-leg , tt)))
origin-0-2-1-19 : P.T.origin tree-0-2-1 occ-0-2-1-19 ≡ input s23
origin-0-2-1-19 = refl
transport-0-2-1-19 : P.T.origin tree-1-3-0 (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-3-2)) , (P.S.target-leg , tt))) ≡ input (swap s23)
transport-0-2-1-19 = refl
occ-0-2-1-20 : P.T.Occurrence tree-0-2-1
occ-0-2-1-20 = (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.source-leg , tt)))
origin-0-2-1-20 : P.T.origin tree-0-2-1 occ-0-2-1-20 ≡ input s20
origin-0-2-1-20 = refl
transport-0-2-1-20 : P.T.origin tree-1-3-0 (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-0-2-1-20 = refl
occ-0-2-1-21 : P.T.Occurrence tree-0-2-1
occ-0-2-1-21 = (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.target-leg , tt)))
origin-0-2-1-21 : P.T.origin tree-0-2-1 occ-0-2-1-21 ≡ input s10
origin-0-2-1-21 = refl
transport-0-2-1-21 : P.T.origin tree-1-3-0 (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.target-leg , tt))) ≡ input (swap s10)
transport-0-2-1-21 = refl
occ-0-2-1-22 : P.T.Occurrence tree-0-2-1
occ-0-2-1-22 = (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.source-leg , tt)))
origin-0-2-1-22 : P.T.origin tree-0-2-1 occ-0-2-1-22 ≡ input s20
origin-0-2-1-22 = refl
transport-0-2-1-22 : P.T.origin tree-1-3-0 (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-0-2-1-22 = refl
occ-0-2-1-23 : P.T.Occurrence tree-0-2-1
occ-0-2-1-23 = (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.target-leg , tt)))
origin-0-2-1-23 : P.T.origin tree-0-2-1 occ-0-2-1-23 ≡ input s30
origin-0-2-1-23 = refl
transport-0-2-1-23 : P.T.origin tree-1-3-0 (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.target-leg , tt))) ≡ input (swap s30)
transport-0-2-1-23 = refl
occ-0-2-1-24 : P.T.Occurrence tree-0-2-1
occ-0-2-1-24 = (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-0-2-1-24 : P.T.origin tree-0-2-1 occ-0-2-1-24 ≡ input s01
origin-0-2-1-24 = refl
transport-0-2-1-24 : P.T.origin tree-1-3-0 (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s01)
transport-0-2-1-24 = refl
occ-0-2-1-25 : P.T.Occurrence tree-0-2-1
occ-0-2-1-25 = (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-0-2-1-25 : P.T.origin tree-0-2-1 occ-0-2-1-25 ≡ input s31
origin-0-2-1-25 = refl
transport-0-2-1-25 : P.T.origin tree-1-3-0 (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-0-2-1-25 = refl
occ-0-2-1-26 : P.T.Occurrence tree-0-2-1
occ-0-2-1-26 = (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-0-2-1-26 : P.T.origin tree-0-2-1 occ-0-2-1-26 ≡ input s21
origin-0-2-1-26 = refl
transport-0-2-1-26 : P.T.origin tree-1-3-0 (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s21)
transport-0-2-1-26 = refl
occ-0-2-1-27 : P.T.Occurrence tree-0-2-1
occ-0-2-1-27 = (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-0-2-1-27 : P.T.origin tree-0-2-1 occ-0-2-1-27 ≡ input s31
origin-0-2-1-27 = refl
transport-0-2-1-27 : P.T.origin tree-1-3-0 (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-0-2-1-27 = refl
occ-0-2-1-28 : P.T.Occurrence tree-0-2-1
occ-0-2-1-28 = (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.source-leg , tt)))
origin-0-2-1-28 : P.T.origin tree-0-2-1 occ-0-2-1-28 ≡ input s02
origin-0-2-1-28 = refl
transport-0-2-1-28 : P.T.origin tree-1-3-0 (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-0-2-1-28 = refl
occ-0-2-1-29 : P.T.Occurrence tree-0-2-1
occ-0-2-1-29 = (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.target-leg , tt)))
origin-0-2-1-29 : P.T.origin tree-0-2-1 occ-0-2-1-29 ≡ input s12
origin-0-2-1-29 = refl
transport-0-2-1-29 : P.T.origin tree-1-3-0 (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.target-leg , tt))) ≡ input (swap s12)
transport-0-2-1-29 = refl
occ-0-2-1-30 : P.T.Occurrence tree-0-2-1
occ-0-2-1-30 = (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.source-leg , tt)))
origin-0-2-1-30 : P.T.origin tree-0-2-1 occ-0-2-1-30 ≡ input s02
origin-0-2-1-30 = refl
transport-0-2-1-30 : P.T.origin tree-1-3-0 (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-0-2-1-30 = refl
occ-0-2-1-31 : P.T.Occurrence tree-0-2-1
occ-0-2-1-31 = (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.target-leg , tt)))
origin-0-2-1-31 : P.T.origin tree-0-2-1 occ-0-2-1-31 ≡ input s32
origin-0-2-1-31 = refl
transport-0-2-1-31 : P.T.origin tree-1-3-0 (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.target-leg , tt))) ≡ input (swap s32)
transport-0-2-1-31 = refl
occ-0-2-1-32 : P.T.Occurrence tree-0-2-1
occ-0-2-1-32 = (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-0-2-1-32 : P.T.origin tree-0-2-1 occ-0-2-1-32 ≡ input s03
origin-0-2-1-32 = refl
transport-0-2-1-32 : P.T.origin tree-1-3-0 (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s03)
transport-0-2-1-32 = refl
occ-0-2-1-33 : P.T.Occurrence tree-0-2-1
occ-0-2-1-33 = (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-0-2-1-33 : P.T.origin tree-0-2-1 occ-0-2-1-33 ≡ input s13
origin-0-2-1-33 = refl
transport-0-2-1-33 : P.T.origin tree-1-3-0 (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-0-2-1-33 = refl
occ-0-2-1-34 : P.T.Occurrence tree-0-2-1
occ-0-2-1-34 = (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-0-2-1-34 : P.T.origin tree-0-2-1 occ-0-2-1-34 ≡ input s23
origin-0-2-1-34 = refl
transport-0-2-1-34 : P.T.origin tree-1-3-0 (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s23)
transport-0-2-1-34 = refl
occ-0-2-1-35 : P.T.Occurrence tree-0-2-1
occ-0-2-1-35 = (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-0-2-1-35 : P.T.origin tree-0-2-1 occ-0-2-1-35 ≡ input s13
origin-0-2-1-35 = refl
transport-0-2-1-35 : P.T.origin tree-1-3-0 (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-0-2-1-35 = refl
occ-0-2-1-36 : P.T.Occurrence tree-0-2-1
occ-0-2-1-36 = (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.source-leg , tt)))
origin-0-2-1-36 : P.T.origin tree-0-2-1 occ-0-2-1-36 ≡ input s20
origin-0-2-1-36 = refl
transport-0-2-1-36 : P.T.origin tree-1-3-0 (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-0-2-1-36 = refl
occ-0-2-1-37 : P.T.Occurrence tree-0-2-1
occ-0-2-1-37 = (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.target-leg , tt)))
origin-0-2-1-37 : P.T.origin tree-0-2-1 occ-0-2-1-37 ≡ input s10
origin-0-2-1-37 = refl
transport-0-2-1-37 : P.T.origin tree-1-3-0 (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.target-leg , tt))) ≡ input (swap s10)
transport-0-2-1-37 = refl
occ-0-2-1-38 : P.T.Occurrence tree-0-2-1
occ-0-2-1-38 = (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.source-leg , tt)))
origin-0-2-1-38 : P.T.origin tree-0-2-1 occ-0-2-1-38 ≡ input s20
origin-0-2-1-38 = refl
transport-0-2-1-38 : P.T.origin tree-1-3-0 (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-0-2-1-38 = refl
occ-0-2-1-39 : P.T.Occurrence tree-0-2-1
occ-0-2-1-39 = (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.target-leg , tt)))
origin-0-2-1-39 : P.T.origin tree-0-2-1 occ-0-2-1-39 ≡ input s30
origin-0-2-1-39 = refl
transport-0-2-1-39 : P.T.origin tree-1-3-0 (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.target-leg , tt))) ≡ input (swap s30)
transport-0-2-1-39 = refl
occ-0-2-1-40 : P.T.Occurrence tree-0-2-1
occ-0-2-1-40 = (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-0-2-1-40 : P.T.origin tree-0-2-1 occ-0-2-1-40 ≡ input s01
origin-0-2-1-40 = refl
transport-0-2-1-40 : P.T.origin tree-1-3-0 (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s01)
transport-0-2-1-40 = refl
occ-0-2-1-41 : P.T.Occurrence tree-0-2-1
occ-0-2-1-41 = (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-0-2-1-41 : P.T.origin tree-0-2-1 occ-0-2-1-41 ≡ input s31
origin-0-2-1-41 = refl
transport-0-2-1-41 : P.T.origin tree-1-3-0 (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-0-2-1-41 = refl
occ-0-2-1-42 : P.T.Occurrence tree-0-2-1
occ-0-2-1-42 = (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-0-2-1-42 : P.T.origin tree-0-2-1 occ-0-2-1-42 ≡ input s21
origin-0-2-1-42 = refl
transport-0-2-1-42 : P.T.origin tree-1-3-0 (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s21)
transport-0-2-1-42 = refl
occ-0-2-1-43 : P.T.Occurrence tree-0-2-1
occ-0-2-1-43 = (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-0-2-1-43 : P.T.origin tree-0-2-1 occ-0-2-1-43 ≡ input s31
origin-0-2-1-43 = refl
transport-0-2-1-43 : P.T.origin tree-1-3-0 (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-0-2-1-43 = refl
occ-0-2-1-44 : P.T.Occurrence tree-0-2-1
occ-0-2-1-44 = (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.source-leg , tt)))
origin-0-2-1-44 : P.T.origin tree-0-2-1 occ-0-2-1-44 ≡ input s02
origin-0-2-1-44 = refl
transport-0-2-1-44 : P.T.origin tree-1-3-0 (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-0-2-1-44 = refl
occ-0-2-1-45 : P.T.Occurrence tree-0-2-1
occ-0-2-1-45 = (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.target-leg , tt)))
origin-0-2-1-45 : P.T.origin tree-0-2-1 occ-0-2-1-45 ≡ input s12
origin-0-2-1-45 = refl
transport-0-2-1-45 : P.T.origin tree-1-3-0 (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.target-leg , tt))) ≡ input (swap s12)
transport-0-2-1-45 = refl
occ-0-2-1-46 : P.T.Occurrence tree-0-2-1
occ-0-2-1-46 = (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.source-leg , tt)))
origin-0-2-1-46 : P.T.origin tree-0-2-1 occ-0-2-1-46 ≡ input s02
origin-0-2-1-46 = refl
transport-0-2-1-46 : P.T.origin tree-1-3-0 (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-0-2-1-46 = refl
occ-0-2-1-47 : P.T.Occurrence tree-0-2-1
occ-0-2-1-47 = (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.target-leg , tt)))
origin-0-2-1-47 : P.T.origin tree-0-2-1 occ-0-2-1-47 ≡ input s32
origin-0-2-1-47 = refl
transport-0-2-1-47 : P.T.origin tree-1-3-0 (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.target-leg , tt))) ≡ input (swap s32)
transport-0-2-1-47 = refl
occ-0-2-1-48 : P.T.Occurrence tree-0-2-1
occ-0-2-1-48 = (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-0-2-1-48 : P.T.origin tree-0-2-1 occ-0-2-1-48 ≡ input s03
origin-0-2-1-48 = refl
transport-0-2-1-48 : P.T.origin tree-1-3-0 (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s03)
transport-0-2-1-48 = refl
occ-0-2-1-49 : P.T.Occurrence tree-0-2-1
occ-0-2-1-49 = (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-0-2-1-49 : P.T.origin tree-0-2-1 occ-0-2-1-49 ≡ input s13
origin-0-2-1-49 = refl
transport-0-2-1-49 : P.T.origin tree-1-3-0 (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-0-2-1-49 = refl
occ-0-2-1-50 : P.T.Occurrence tree-0-2-1
occ-0-2-1-50 = (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-0-2-1-50 : P.T.origin tree-0-2-1 occ-0-2-1-50 ≡ input s23
origin-0-2-1-50 = refl
transport-0-2-1-50 : P.T.origin tree-1-3-0 (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s23)
transport-0-2-1-50 = refl
occ-0-2-1-51 : P.T.Occurrence tree-0-2-1
occ-0-2-1-51 = (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-0-2-1-51 : P.T.origin tree-0-2-1 occ-0-2-1-51 ≡ input s13
origin-0-2-1-51 = refl
transport-0-2-1-51 : P.T.origin tree-1-3-0 (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-0-2-1-51 = refl
occ-0-2-1-52 : P.T.Occurrence tree-0-2-1
occ-0-2-1-52 = (P.S.full-source , (P.S.first-port , tt))
origin-0-2-1-52 : P.T.origin tree-0-2-1 occ-0-2-1-52 ≡ input s03
origin-0-2-1-52 = refl
transport-0-2-1-52 : P.T.origin tree-1-3-0 (P.S.full-source , (P.S.first-port , tt)) ≡ input (swap s03)
transport-0-2-1-52 = refl
occ-0-2-1-53 : P.T.Occurrence tree-0-2-1
occ-0-2-1-53 = (P.S.full-source , (P.S.middle-port , tt))
origin-0-2-1-53 : P.T.origin tree-0-2-1 occ-0-2-1-53 ≡ input s23
origin-0-2-1-53 = refl
transport-0-2-1-53 : P.T.origin tree-1-3-0 (P.S.full-source , (P.S.middle-port , tt)) ≡ input (swap s23)
transport-0-2-1-53 = refl
occ-0-2-1-54 : P.T.Occurrence tree-0-2-1
occ-0-2-1-54 = (P.S.full-source , (P.S.final-port , tt))
origin-0-2-1-54 : P.T.origin tree-0-2-1 occ-0-2-1-54 ≡ input s13
origin-0-2-1-54 = refl
transport-0-2-1-54 : P.T.origin tree-1-3-0 (P.S.full-source , (P.S.final-port , tt)) ≡ input (swap s13)
transport-0-2-1-54 = refl
selected-source-0-2-1-AB : P.S.ab-index {a = C.q0} {b = C.q0} {c = C.q7} F.triple-0-2-1 ≡ (m1 , (F.vp-0-3 , F.vp-2-3))
selected-source-0-2-1-AB = refl
selected-target-0-2-1-AB : P.S.ab-index {a = C.q7} {b = C.q7} {c = C.q0} F.triple-1-3-0 ≡ (c1 , (F.vp-1-2 , F.vp-3-2))
selected-target-0-2-1-AB = refl
selected-source-0-2-1-BC : P.S.bc-index {a = C.q0} {b = C.q0} {c = C.q7} F.triple-0-2-1 ≡ (m1 , (F.vp-2-3 , F.vp-1-3))
selected-source-0-2-1-BC = refl
selected-target-0-2-1-BC : P.S.bc-index {a = C.q7} {b = C.q7} {c = C.q0} F.triple-1-3-0 ≡ (c1 , (F.vp-3-2 , F.vp-0-2))
selected-target-0-2-1-BC = refl
selected-source-0-2-1-AC : P.S.ac-index {a = C.q0} {b = C.q0} {c = C.q7} F.triple-0-2-1 ≡ (m1 , (F.vp-0-3 , F.vp-1-3))
selected-source-0-2-1-AC = refl
selected-target-0-2-1-AC : P.S.ac-index {a = C.q7} {b = C.q7} {c = C.q0} F.triple-1-3-0 ≡ (c1 , (F.vp-1-2 , F.vp-0-2))
selected-target-0-2-1-AC = refl
occ-0-2-3-0 : P.T.Occurrence tree-0-2-3
occ-0-2-3-0 = (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-0-2-3-0 : P.T.origin tree-0-2-3 occ-0-2-3-0 ≡ input s20
origin-0-2-3-0 = refl
transport-0-2-3-0 : P.T.origin tree-1-3-2 (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-0-2-3-0 = refl
occ-0-2-3-1 : P.T.Occurrence tree-0-2-3
occ-0-2-3-1 = (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-0-2-3-1 : P.T.origin tree-0-2-3 occ-0-2-3-1 ≡ input s20
origin-0-2-3-1 = refl
transport-0-2-3-1 : P.T.origin tree-1-3-2 (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-0-2-3-1 = refl
occ-0-2-3-2 : P.T.Occurrence tree-0-2-3
occ-0-2-3-2 = (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-0-1)) , (P.S.source-leg , tt)))
origin-0-2-3-2 : P.T.origin tree-0-2-3 occ-0-2-3-2 ≡ input s01
origin-0-2-3-2 = refl
transport-0-2-3-2 : P.T.origin tree-1-3-2 (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-1-0)) , (P.S.source-leg , tt))) ≡ input (swap s01)
transport-0-2-3-2 = refl
occ-0-2-3-3 : P.T.Occurrence tree-0-2-3
occ-0-2-3-3 = (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-0-1)) , (P.S.target-leg , tt)))
origin-0-2-3-3 : P.T.origin tree-0-2-3 occ-0-2-3-3 ≡ input s01
origin-0-2-3-3 = refl
transport-0-2-3-3 : P.T.origin tree-1-3-2 (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-1-0)) , (P.S.target-leg , tt))) ≡ input (swap s01)
transport-0-2-3-3 = refl
occ-0-2-3-4 : P.T.Occurrence tree-0-2-3
occ-0-2-3-4 = (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.source-leg , tt)))
origin-0-2-3-4 : P.T.origin tree-0-2-3 occ-0-2-3-4 ≡ input s01
origin-0-2-3-4 = refl
transport-0-2-3-4 : P.T.origin tree-1-3-2 (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.source-leg , tt))) ≡ input (swap s01)
transport-0-2-3-4 = refl
occ-0-2-3-5 : P.T.Occurrence tree-0-2-3
occ-0-2-3-5 = (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.target-leg , tt)))
origin-0-2-3-5 : P.T.origin tree-0-2-3 occ-0-2-3-5 ≡ input s21
origin-0-2-3-5 = refl
transport-0-2-3-5 : P.T.origin tree-1-3-2 (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.target-leg , tt))) ≡ input (swap s21)
transport-0-2-3-5 = refl
occ-0-2-3-6 : P.T.Occurrence tree-0-2-3
occ-0-2-3-6 = (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.source-leg , tt)))
origin-0-2-3-6 : P.T.origin tree-0-2-3 occ-0-2-3-6 ≡ input s21
origin-0-2-3-6 = refl
transport-0-2-3-6 : P.T.origin tree-1-3-2 (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.source-leg , tt))) ≡ input (swap s21)
transport-0-2-3-6 = refl
occ-0-2-3-7 : P.T.Occurrence tree-0-2-3
occ-0-2-3-7 = (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.target-leg , tt)))
origin-0-2-3-7 : P.T.origin tree-0-2-3 occ-0-2-3-7 ≡ input s01
origin-0-2-3-7 = refl
transport-0-2-3-7 : P.T.origin tree-1-3-2 (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.target-leg , tt))) ≡ input (swap s01)
transport-0-2-3-7 = refl
occ-0-2-3-8 : P.T.Occurrence tree-0-2-3
occ-0-2-3-8 = (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-2-1)) , (P.S.source-leg , tt)))
origin-0-2-3-8 : P.T.origin tree-0-2-3 occ-0-2-3-8 ≡ input s21
origin-0-2-3-8 = refl
transport-0-2-3-8 : P.T.origin tree-1-3-2 (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-3-0)) , (P.S.source-leg , tt))) ≡ input (swap s21)
transport-0-2-3-8 = refl
occ-0-2-3-9 : P.T.Occurrence tree-0-2-3
occ-0-2-3-9 = (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-2-1)) , (P.S.target-leg , tt)))
origin-0-2-3-9 : P.T.origin tree-0-2-3 occ-0-2-3-9 ≡ input s21
origin-0-2-3-9 = refl
transport-0-2-3-9 : P.T.origin tree-1-3-2 (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-3-0)) , (P.S.target-leg , tt))) ≡ input (swap s21)
transport-0-2-3-9 = refl
occ-0-2-3-10 : P.T.Occurrence tree-0-2-3
occ-0-2-3-10 = (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-0-2-3-10 : P.T.origin tree-0-2-3 occ-0-2-3-10 ≡ input s02
origin-0-2-3-10 = refl
transport-0-2-3-10 : P.T.origin tree-1-3-2 (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-0-2-3-10 = refl
occ-0-2-3-11 : P.T.Occurrence tree-0-2-3
occ-0-2-3-11 = (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-0-2-3-11 : P.T.origin tree-0-2-3 occ-0-2-3-11 ≡ input s02
origin-0-2-3-11 = refl
transport-0-2-3-11 : P.T.origin tree-1-3-2 (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-0-2-3-11 = refl
occ-0-2-3-12 : P.T.Occurrence tree-0-2-3
occ-0-2-3-12 = (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-0-3)) , (P.S.source-leg , tt)))
origin-0-2-3-12 : P.T.origin tree-0-2-3 occ-0-2-3-12 ≡ input s03
origin-0-2-3-12 = refl
transport-0-2-3-12 : P.T.origin tree-1-3-2 (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-1-2)) , (P.S.source-leg , tt))) ≡ input (swap s03)
transport-0-2-3-12 = refl
occ-0-2-3-13 : P.T.Occurrence tree-0-2-3
occ-0-2-3-13 = (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-0-3)) , (P.S.target-leg , tt)))
origin-0-2-3-13 : P.T.origin tree-0-2-3 occ-0-2-3-13 ≡ input s03
origin-0-2-3-13 = refl
transport-0-2-3-13 : P.T.origin tree-1-3-2 (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-1-2)) , (P.S.target-leg , tt))) ≡ input (swap s03)
transport-0-2-3-13 = refl
occ-0-2-3-14 : P.T.Occurrence tree-0-2-3
occ-0-2-3-14 = (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.source-leg , tt)))
origin-0-2-3-14 : P.T.origin tree-0-2-3 occ-0-2-3-14 ≡ input s03
origin-0-2-3-14 = refl
transport-0-2-3-14 : P.T.origin tree-1-3-2 (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.source-leg , tt))) ≡ input (swap s03)
transport-0-2-3-14 = refl
occ-0-2-3-15 : P.T.Occurrence tree-0-2-3
occ-0-2-3-15 = (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.target-leg , tt)))
origin-0-2-3-15 : P.T.origin tree-0-2-3 occ-0-2-3-15 ≡ input s23
origin-0-2-3-15 = refl
transport-0-2-3-15 : P.T.origin tree-1-3-2 (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.target-leg , tt))) ≡ input (swap s23)
transport-0-2-3-15 = refl
occ-0-2-3-16 : P.T.Occurrence tree-0-2-3
occ-0-2-3-16 = (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.source-leg , tt)))
origin-0-2-3-16 : P.T.origin tree-0-2-3 occ-0-2-3-16 ≡ input s23
origin-0-2-3-16 = refl
transport-0-2-3-16 : P.T.origin tree-1-3-2 (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.source-leg , tt))) ≡ input (swap s23)
transport-0-2-3-16 = refl
occ-0-2-3-17 : P.T.Occurrence tree-0-2-3
occ-0-2-3-17 = (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.target-leg , tt)))
origin-0-2-3-17 : P.T.origin tree-0-2-3 occ-0-2-3-17 ≡ input s03
origin-0-2-3-17 = refl
transport-0-2-3-17 : P.T.origin tree-1-3-2 (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.target-leg , tt))) ≡ input (swap s03)
transport-0-2-3-17 = refl
occ-0-2-3-18 : P.T.Occurrence tree-0-2-3
occ-0-2-3-18 = (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-2-3)) , (P.S.source-leg , tt)))
origin-0-2-3-18 : P.T.origin tree-0-2-3 occ-0-2-3-18 ≡ input s23
origin-0-2-3-18 = refl
transport-0-2-3-18 : P.T.origin tree-1-3-2 (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-3-2)) , (P.S.source-leg , tt))) ≡ input (swap s23)
transport-0-2-3-18 = refl
occ-0-2-3-19 : P.T.Occurrence tree-0-2-3
occ-0-2-3-19 = (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-2-3)) , (P.S.target-leg , tt)))
origin-0-2-3-19 : P.T.origin tree-0-2-3 occ-0-2-3-19 ≡ input s23
origin-0-2-3-19 = refl
transport-0-2-3-19 : P.T.origin tree-1-3-2 (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-3-2)) , (P.S.target-leg , tt))) ≡ input (swap s23)
transport-0-2-3-19 = refl
occ-0-2-3-20 : P.T.Occurrence tree-0-2-3
occ-0-2-3-20 = (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.source-leg , tt)))
origin-0-2-3-20 : P.T.origin tree-0-2-3 occ-0-2-3-20 ≡ input s20
origin-0-2-3-20 = refl
transport-0-2-3-20 : P.T.origin tree-1-3-2 (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-0-2-3-20 = refl
occ-0-2-3-21 : P.T.Occurrence tree-0-2-3
occ-0-2-3-21 = (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.target-leg , tt)))
origin-0-2-3-21 : P.T.origin tree-0-2-3 occ-0-2-3-21 ≡ input s10
origin-0-2-3-21 = refl
transport-0-2-3-21 : P.T.origin tree-1-3-2 (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.target-leg , tt))) ≡ input (swap s10)
transport-0-2-3-21 = refl
occ-0-2-3-22 : P.T.Occurrence tree-0-2-3
occ-0-2-3-22 = (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.source-leg , tt)))
origin-0-2-3-22 : P.T.origin tree-0-2-3 occ-0-2-3-22 ≡ input s20
origin-0-2-3-22 = refl
transport-0-2-3-22 : P.T.origin tree-1-3-2 (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-0-2-3-22 = refl
occ-0-2-3-23 : P.T.Occurrence tree-0-2-3
occ-0-2-3-23 = (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.target-leg , tt)))
origin-0-2-3-23 : P.T.origin tree-0-2-3 occ-0-2-3-23 ≡ input s30
origin-0-2-3-23 = refl
transport-0-2-3-23 : P.T.origin tree-1-3-2 (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.target-leg , tt))) ≡ input (swap s30)
transport-0-2-3-23 = refl
occ-0-2-3-24 : P.T.Occurrence tree-0-2-3
occ-0-2-3-24 = (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-0-2-3-24 : P.T.origin tree-0-2-3 occ-0-2-3-24 ≡ input s01
origin-0-2-3-24 = refl
transport-0-2-3-24 : P.T.origin tree-1-3-2 (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s01)
transport-0-2-3-24 = refl
occ-0-2-3-25 : P.T.Occurrence tree-0-2-3
occ-0-2-3-25 = (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-0-2-3-25 : P.T.origin tree-0-2-3 occ-0-2-3-25 ≡ input s31
origin-0-2-3-25 = refl
transport-0-2-3-25 : P.T.origin tree-1-3-2 (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-0-2-3-25 = refl
occ-0-2-3-26 : P.T.Occurrence tree-0-2-3
occ-0-2-3-26 = (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-0-2-3-26 : P.T.origin tree-0-2-3 occ-0-2-3-26 ≡ input s21
origin-0-2-3-26 = refl
transport-0-2-3-26 : P.T.origin tree-1-3-2 (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s21)
transport-0-2-3-26 = refl
occ-0-2-3-27 : P.T.Occurrence tree-0-2-3
occ-0-2-3-27 = (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-0-2-3-27 : P.T.origin tree-0-2-3 occ-0-2-3-27 ≡ input s31
origin-0-2-3-27 = refl
transport-0-2-3-27 : P.T.origin tree-1-3-2 (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-0-2-3-27 = refl
occ-0-2-3-28 : P.T.Occurrence tree-0-2-3
occ-0-2-3-28 = (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.source-leg , tt)))
origin-0-2-3-28 : P.T.origin tree-0-2-3 occ-0-2-3-28 ≡ input s02
origin-0-2-3-28 = refl
transport-0-2-3-28 : P.T.origin tree-1-3-2 (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-0-2-3-28 = refl
occ-0-2-3-29 : P.T.Occurrence tree-0-2-3
occ-0-2-3-29 = (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.target-leg , tt)))
origin-0-2-3-29 : P.T.origin tree-0-2-3 occ-0-2-3-29 ≡ input s12
origin-0-2-3-29 = refl
transport-0-2-3-29 : P.T.origin tree-1-3-2 (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.target-leg , tt))) ≡ input (swap s12)
transport-0-2-3-29 = refl
occ-0-2-3-30 : P.T.Occurrence tree-0-2-3
occ-0-2-3-30 = (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.source-leg , tt)))
origin-0-2-3-30 : P.T.origin tree-0-2-3 occ-0-2-3-30 ≡ input s02
origin-0-2-3-30 = refl
transport-0-2-3-30 : P.T.origin tree-1-3-2 (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-0-2-3-30 = refl
occ-0-2-3-31 : P.T.Occurrence tree-0-2-3
occ-0-2-3-31 = (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.target-leg , tt)))
origin-0-2-3-31 : P.T.origin tree-0-2-3 occ-0-2-3-31 ≡ input s32
origin-0-2-3-31 = refl
transport-0-2-3-31 : P.T.origin tree-1-3-2 (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.target-leg , tt))) ≡ input (swap s32)
transport-0-2-3-31 = refl
occ-0-2-3-32 : P.T.Occurrence tree-0-2-3
occ-0-2-3-32 = (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-0-2-3-32 : P.T.origin tree-0-2-3 occ-0-2-3-32 ≡ input s03
origin-0-2-3-32 = refl
transport-0-2-3-32 : P.T.origin tree-1-3-2 (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s03)
transport-0-2-3-32 = refl
occ-0-2-3-33 : P.T.Occurrence tree-0-2-3
occ-0-2-3-33 = (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-0-2-3-33 : P.T.origin tree-0-2-3 occ-0-2-3-33 ≡ input s13
origin-0-2-3-33 = refl
transport-0-2-3-33 : P.T.origin tree-1-3-2 (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-0-2-3-33 = refl
occ-0-2-3-34 : P.T.Occurrence tree-0-2-3
occ-0-2-3-34 = (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-0-2-3-34 : P.T.origin tree-0-2-3 occ-0-2-3-34 ≡ input s23
origin-0-2-3-34 = refl
transport-0-2-3-34 : P.T.origin tree-1-3-2 (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s23)
transport-0-2-3-34 = refl
occ-0-2-3-35 : P.T.Occurrence tree-0-2-3
occ-0-2-3-35 = (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-0-2-3-35 : P.T.origin tree-0-2-3 occ-0-2-3-35 ≡ input s13
origin-0-2-3-35 = refl
transport-0-2-3-35 : P.T.origin tree-1-3-2 (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-0-2-3-35 = refl
occ-0-2-3-36 : P.T.Occurrence tree-0-2-3
occ-0-2-3-36 = (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.source-leg , tt)))
origin-0-2-3-36 : P.T.origin tree-0-2-3 occ-0-2-3-36 ≡ input s20
origin-0-2-3-36 = refl
transport-0-2-3-36 : P.T.origin tree-1-3-2 (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-0-2-3-36 = refl
occ-0-2-3-37 : P.T.Occurrence tree-0-2-3
occ-0-2-3-37 = (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.target-leg , tt)))
origin-0-2-3-37 : P.T.origin tree-0-2-3 occ-0-2-3-37 ≡ input s10
origin-0-2-3-37 = refl
transport-0-2-3-37 : P.T.origin tree-1-3-2 (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.target-leg , tt))) ≡ input (swap s10)
transport-0-2-3-37 = refl
occ-0-2-3-38 : P.T.Occurrence tree-0-2-3
occ-0-2-3-38 = (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.source-leg , tt)))
origin-0-2-3-38 : P.T.origin tree-0-2-3 occ-0-2-3-38 ≡ input s20
origin-0-2-3-38 = refl
transport-0-2-3-38 : P.T.origin tree-1-3-2 (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-0-2-3-38 = refl
occ-0-2-3-39 : P.T.Occurrence tree-0-2-3
occ-0-2-3-39 = (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.target-leg , tt)))
origin-0-2-3-39 : P.T.origin tree-0-2-3 occ-0-2-3-39 ≡ input s30
origin-0-2-3-39 = refl
transport-0-2-3-39 : P.T.origin tree-1-3-2 (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.target-leg , tt))) ≡ input (swap s30)
transport-0-2-3-39 = refl
occ-0-2-3-40 : P.T.Occurrence tree-0-2-3
occ-0-2-3-40 = (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-0-2-3-40 : P.T.origin tree-0-2-3 occ-0-2-3-40 ≡ input s01
origin-0-2-3-40 = refl
transport-0-2-3-40 : P.T.origin tree-1-3-2 (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s01)
transport-0-2-3-40 = refl
occ-0-2-3-41 : P.T.Occurrence tree-0-2-3
occ-0-2-3-41 = (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-0-2-3-41 : P.T.origin tree-0-2-3 occ-0-2-3-41 ≡ input s31
origin-0-2-3-41 = refl
transport-0-2-3-41 : P.T.origin tree-1-3-2 (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-0-2-3-41 = refl
occ-0-2-3-42 : P.T.Occurrence tree-0-2-3
occ-0-2-3-42 = (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-0-2-3-42 : P.T.origin tree-0-2-3 occ-0-2-3-42 ≡ input s21
origin-0-2-3-42 = refl
transport-0-2-3-42 : P.T.origin tree-1-3-2 (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s21)
transport-0-2-3-42 = refl
occ-0-2-3-43 : P.T.Occurrence tree-0-2-3
occ-0-2-3-43 = (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-0-2-3-43 : P.T.origin tree-0-2-3 occ-0-2-3-43 ≡ input s31
origin-0-2-3-43 = refl
transport-0-2-3-43 : P.T.origin tree-1-3-2 (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-0-2-3-43 = refl
occ-0-2-3-44 : P.T.Occurrence tree-0-2-3
occ-0-2-3-44 = (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.source-leg , tt)))
origin-0-2-3-44 : P.T.origin tree-0-2-3 occ-0-2-3-44 ≡ input s02
origin-0-2-3-44 = refl
transport-0-2-3-44 : P.T.origin tree-1-3-2 (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-0-2-3-44 = refl
occ-0-2-3-45 : P.T.Occurrence tree-0-2-3
occ-0-2-3-45 = (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.target-leg , tt)))
origin-0-2-3-45 : P.T.origin tree-0-2-3 occ-0-2-3-45 ≡ input s12
origin-0-2-3-45 = refl
transport-0-2-3-45 : P.T.origin tree-1-3-2 (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.target-leg , tt))) ≡ input (swap s12)
transport-0-2-3-45 = refl
occ-0-2-3-46 : P.T.Occurrence tree-0-2-3
occ-0-2-3-46 = (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.source-leg , tt)))
origin-0-2-3-46 : P.T.origin tree-0-2-3 occ-0-2-3-46 ≡ input s02
origin-0-2-3-46 = refl
transport-0-2-3-46 : P.T.origin tree-1-3-2 (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-0-2-3-46 = refl
occ-0-2-3-47 : P.T.Occurrence tree-0-2-3
occ-0-2-3-47 = (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.target-leg , tt)))
origin-0-2-3-47 : P.T.origin tree-0-2-3 occ-0-2-3-47 ≡ input s32
origin-0-2-3-47 = refl
transport-0-2-3-47 : P.T.origin tree-1-3-2 (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.target-leg , tt))) ≡ input (swap s32)
transport-0-2-3-47 = refl
occ-0-2-3-48 : P.T.Occurrence tree-0-2-3
occ-0-2-3-48 = (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-0-2-3-48 : P.T.origin tree-0-2-3 occ-0-2-3-48 ≡ input s03
origin-0-2-3-48 = refl
transport-0-2-3-48 : P.T.origin tree-1-3-2 (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s03)
transport-0-2-3-48 = refl
occ-0-2-3-49 : P.T.Occurrence tree-0-2-3
occ-0-2-3-49 = (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-0-2-3-49 : P.T.origin tree-0-2-3 occ-0-2-3-49 ≡ input s13
origin-0-2-3-49 = refl
transport-0-2-3-49 : P.T.origin tree-1-3-2 (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-0-2-3-49 = refl
occ-0-2-3-50 : P.T.Occurrence tree-0-2-3
occ-0-2-3-50 = (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-0-2-3-50 : P.T.origin tree-0-2-3 occ-0-2-3-50 ≡ input s23
origin-0-2-3-50 = refl
transport-0-2-3-50 : P.T.origin tree-1-3-2 (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s23)
transport-0-2-3-50 = refl
occ-0-2-3-51 : P.T.Occurrence tree-0-2-3
occ-0-2-3-51 = (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-0-2-3-51 : P.T.origin tree-0-2-3 occ-0-2-3-51 ≡ input s13
origin-0-2-3-51 = refl
transport-0-2-3-51 : P.T.origin tree-1-3-2 (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-0-2-3-51 = refl
occ-0-2-3-52 : P.T.Occurrence tree-0-2-3
occ-0-2-3-52 = (P.S.full-source , (P.S.first-port , tt))
origin-0-2-3-52 : P.T.origin tree-0-2-3 occ-0-2-3-52 ≡ input s01
origin-0-2-3-52 = refl
transport-0-2-3-52 : P.T.origin tree-1-3-2 (P.S.full-source , (P.S.first-port , tt)) ≡ input (swap s01)
transport-0-2-3-52 = refl
occ-0-2-3-53 : P.T.Occurrence tree-0-2-3
occ-0-2-3-53 = (P.S.full-source , (P.S.middle-port , tt))
origin-0-2-3-53 : P.T.origin tree-0-2-3 occ-0-2-3-53 ≡ input s21
origin-0-2-3-53 = refl
transport-0-2-3-53 : P.T.origin tree-1-3-2 (P.S.full-source , (P.S.middle-port , tt)) ≡ input (swap s21)
transport-0-2-3-53 = refl
occ-0-2-3-54 : P.T.Occurrence tree-0-2-3
occ-0-2-3-54 = (P.S.full-source , (P.S.final-port , tt))
origin-0-2-3-54 : P.T.origin tree-0-2-3 occ-0-2-3-54 ≡ input s31
origin-0-2-3-54 = refl
transport-0-2-3-54 : P.T.origin tree-1-3-2 (P.S.full-source , (P.S.final-port , tt)) ≡ input (swap s31)
transport-0-2-3-54 = refl
selected-source-0-2-3-AB : P.S.ab-index {a = C.q0} {b = C.q0} {c = C.q7} F.triple-0-2-3 ≡ (m0 , (F.vp-0-1 , F.vp-2-1))
selected-source-0-2-3-AB = refl
selected-target-0-2-3-AB : P.S.ab-index {a = C.q7} {b = C.q7} {c = C.q0} F.triple-1-3-2 ≡ (c0 , (F.vp-1-0 , F.vp-3-0))
selected-target-0-2-3-AB = refl
selected-source-0-2-3-BC : P.S.bc-index {a = C.q0} {b = C.q0} {c = C.q7} F.triple-0-2-3 ≡ (m0 , (F.vp-2-1 , F.vp-3-1))
selected-source-0-2-3-BC = refl
selected-target-0-2-3-BC : P.S.bc-index {a = C.q7} {b = C.q7} {c = C.q0} F.triple-1-3-2 ≡ (c0 , (F.vp-3-0 , F.vp-2-0))
selected-target-0-2-3-BC = refl
selected-source-0-2-3-AC : P.S.ac-index {a = C.q0} {b = C.q0} {c = C.q7} F.triple-0-2-3 ≡ (m0 , (F.vp-0-1 , F.vp-3-1))
selected-source-0-2-3-AC = refl
selected-target-0-2-3-AC : P.S.ac-index {a = C.q7} {b = C.q7} {c = C.q0} F.triple-1-3-2 ≡ (c0 , (F.vp-1-0 , F.vp-2-0))
selected-target-0-2-3-AC = refl
occ-0-3-1-0 : P.T.Occurrence tree-0-3-1
occ-0-3-1-0 = (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.source-leg , tt)))
origin-0-3-1-0 : P.T.origin tree-0-3-1 occ-0-3-1-0 ≡ input s20
origin-0-3-1-0 = refl
transport-0-3-1-0 : P.T.origin tree-1-2-0 (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-0-3-1-0 = refl
occ-0-3-1-1 : P.T.Occurrence tree-0-3-1
occ-0-3-1-1 = (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.target-leg , tt)))
origin-0-3-1-1 : P.T.origin tree-0-3-1 occ-0-3-1-1 ≡ input s10
origin-0-3-1-1 = refl
transport-0-3-1-1 : P.T.origin tree-1-2-0 (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.target-leg , tt))) ≡ input (swap s10)
transport-0-3-1-1 = refl
occ-0-3-1-2 : P.T.Occurrence tree-0-3-1
occ-0-3-1-2 = (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.source-leg , tt)))
origin-0-3-1-2 : P.T.origin tree-0-3-1 occ-0-3-1-2 ≡ input s20
origin-0-3-1-2 = refl
transport-0-3-1-2 : P.T.origin tree-1-2-0 (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-0-3-1-2 = refl
occ-0-3-1-3 : P.T.Occurrence tree-0-3-1
occ-0-3-1-3 = (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.target-leg , tt)))
origin-0-3-1-3 : P.T.origin tree-0-3-1 occ-0-3-1-3 ≡ input s30
origin-0-3-1-3 = refl
transport-0-3-1-3 : P.T.origin tree-1-2-0 (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.target-leg , tt))) ≡ input (swap s30)
transport-0-3-1-3 = refl
occ-0-3-1-4 : P.T.Occurrence tree-0-3-1
occ-0-3-1-4 = (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-0-3-1-4 : P.T.origin tree-0-3-1 occ-0-3-1-4 ≡ input s01
origin-0-3-1-4 = refl
transport-0-3-1-4 : P.T.origin tree-1-2-0 (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s01)
transport-0-3-1-4 = refl
occ-0-3-1-5 : P.T.Occurrence tree-0-3-1
occ-0-3-1-5 = (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-0-3-1-5 : P.T.origin tree-0-3-1 occ-0-3-1-5 ≡ input s31
origin-0-3-1-5 = refl
transport-0-3-1-5 : P.T.origin tree-1-2-0 (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-0-3-1-5 = refl
occ-0-3-1-6 : P.T.Occurrence tree-0-3-1
occ-0-3-1-6 = (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-0-3-1-6 : P.T.origin tree-0-3-1 occ-0-3-1-6 ≡ input s21
origin-0-3-1-6 = refl
transport-0-3-1-6 : P.T.origin tree-1-2-0 (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s21)
transport-0-3-1-6 = refl
occ-0-3-1-7 : P.T.Occurrence tree-0-3-1
occ-0-3-1-7 = (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-0-3-1-7 : P.T.origin tree-0-3-1 occ-0-3-1-7 ≡ input s31
origin-0-3-1-7 = refl
transport-0-3-1-7 : P.T.origin tree-1-2-0 (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-0-3-1-7 = refl
occ-0-3-1-8 : P.T.Occurrence tree-0-3-1
occ-0-3-1-8 = (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.source-leg , tt)))
origin-0-3-1-8 : P.T.origin tree-0-3-1 occ-0-3-1-8 ≡ input s02
origin-0-3-1-8 = refl
transport-0-3-1-8 : P.T.origin tree-1-2-0 (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-0-3-1-8 = refl
occ-0-3-1-9 : P.T.Occurrence tree-0-3-1
occ-0-3-1-9 = (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.target-leg , tt)))
origin-0-3-1-9 : P.T.origin tree-0-3-1 occ-0-3-1-9 ≡ input s12
origin-0-3-1-9 = refl
transport-0-3-1-9 : P.T.origin tree-1-2-0 (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.target-leg , tt))) ≡ input (swap s12)
transport-0-3-1-9 = refl
occ-0-3-1-10 : P.T.Occurrence tree-0-3-1
occ-0-3-1-10 = (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.source-leg , tt)))
origin-0-3-1-10 : P.T.origin tree-0-3-1 occ-0-3-1-10 ≡ input s02
origin-0-3-1-10 = refl
transport-0-3-1-10 : P.T.origin tree-1-2-0 (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-0-3-1-10 = refl
occ-0-3-1-11 : P.T.Occurrence tree-0-3-1
occ-0-3-1-11 = (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.target-leg , tt)))
origin-0-3-1-11 : P.T.origin tree-0-3-1 occ-0-3-1-11 ≡ input s32
origin-0-3-1-11 = refl
transport-0-3-1-11 : P.T.origin tree-1-2-0 (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.target-leg , tt))) ≡ input (swap s32)
transport-0-3-1-11 = refl
occ-0-3-1-12 : P.T.Occurrence tree-0-3-1
occ-0-3-1-12 = (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-0-3-1-12 : P.T.origin tree-0-3-1 occ-0-3-1-12 ≡ input s03
origin-0-3-1-12 = refl
transport-0-3-1-12 : P.T.origin tree-1-2-0 (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s03)
transport-0-3-1-12 = refl
occ-0-3-1-13 : P.T.Occurrence tree-0-3-1
occ-0-3-1-13 = (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-0-3-1-13 : P.T.origin tree-0-3-1 occ-0-3-1-13 ≡ input s13
origin-0-3-1-13 = refl
transport-0-3-1-13 : P.T.origin tree-1-2-0 (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-0-3-1-13 = refl
occ-0-3-1-14 : P.T.Occurrence tree-0-3-1
occ-0-3-1-14 = (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-0-3-1-14 : P.T.origin tree-0-3-1 occ-0-3-1-14 ≡ input s23
origin-0-3-1-14 = refl
transport-0-3-1-14 : P.T.origin tree-1-2-0 (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s23)
transport-0-3-1-14 = refl
occ-0-3-1-15 : P.T.Occurrence tree-0-3-1
occ-0-3-1-15 = (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-0-3-1-15 : P.T.origin tree-0-3-1 occ-0-3-1-15 ≡ input s13
origin-0-3-1-15 = refl
transport-0-3-1-15 : P.T.origin tree-1-2-0 (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-0-3-1-15 = refl
occ-0-3-1-16 : P.T.Occurrence tree-0-3-1
occ-0-3-1-16 = (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-1-0)) , (P.S.source-leg , tt)))
origin-0-3-1-16 : P.T.origin tree-0-3-1 occ-0-3-1-16 ≡ input s10
origin-0-3-1-16 = refl
transport-0-3-1-16 : P.T.origin tree-1-2-0 (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-0-1)) , (P.S.source-leg , tt))) ≡ input (swap s10)
transport-0-3-1-16 = refl
occ-0-3-1-17 : P.T.Occurrence tree-0-3-1
occ-0-3-1-17 = (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-1-0)) , (P.S.target-leg , tt)))
origin-0-3-1-17 : P.T.origin tree-0-3-1 occ-0-3-1-17 ≡ input s10
origin-0-3-1-17 = refl
transport-0-3-1-17 : P.T.origin tree-1-2-0 (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-0-1)) , (P.S.target-leg , tt))) ≡ input (swap s10)
transport-0-3-1-17 = refl
occ-0-3-1-18 : P.T.Occurrence tree-0-3-1
occ-0-3-1-18 = (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.source-leg , tt)))
origin-0-3-1-18 : P.T.origin tree-0-3-1 occ-0-3-1-18 ≡ input s10
origin-0-3-1-18 = refl
transport-0-3-1-18 : P.T.origin tree-1-2-0 (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.source-leg , tt))) ≡ input (swap s10)
transport-0-3-1-18 = refl
occ-0-3-1-19 : P.T.Occurrence tree-0-3-1
occ-0-3-1-19 = (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.target-leg , tt)))
origin-0-3-1-19 : P.T.origin tree-0-3-1 occ-0-3-1-19 ≡ input s30
origin-0-3-1-19 = refl
transport-0-3-1-19 : P.T.origin tree-1-2-0 (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.target-leg , tt))) ≡ input (swap s30)
transport-0-3-1-19 = refl
occ-0-3-1-20 : P.T.Occurrence tree-0-3-1
occ-0-3-1-20 = (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.source-leg , tt)))
origin-0-3-1-20 : P.T.origin tree-0-3-1 occ-0-3-1-20 ≡ input s30
origin-0-3-1-20 = refl
transport-0-3-1-20 : P.T.origin tree-1-2-0 (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.source-leg , tt))) ≡ input (swap s30)
transport-0-3-1-20 = refl
occ-0-3-1-21 : P.T.Occurrence tree-0-3-1
occ-0-3-1-21 = (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.target-leg , tt)))
origin-0-3-1-21 : P.T.origin tree-0-3-1 occ-0-3-1-21 ≡ input s10
origin-0-3-1-21 = refl
transport-0-3-1-21 : P.T.origin tree-1-2-0 (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.target-leg , tt))) ≡ input (swap s10)
transport-0-3-1-21 = refl
occ-0-3-1-22 : P.T.Occurrence tree-0-3-1
occ-0-3-1-22 = (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-3-0)) , (P.S.source-leg , tt)))
origin-0-3-1-22 : P.T.origin tree-0-3-1 occ-0-3-1-22 ≡ input s30
origin-0-3-1-22 = refl
transport-0-3-1-22 : P.T.origin tree-1-2-0 (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-2-1)) , (P.S.source-leg , tt))) ≡ input (swap s30)
transport-0-3-1-22 = refl
occ-0-3-1-23 : P.T.Occurrence tree-0-3-1
occ-0-3-1-23 = (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-3-0)) , (P.S.target-leg , tt)))
origin-0-3-1-23 : P.T.origin tree-0-3-1 occ-0-3-1-23 ≡ input s30
origin-0-3-1-23 = refl
transport-0-3-1-23 : P.T.origin tree-1-2-0 (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-2-1)) , (P.S.target-leg , tt))) ≡ input (swap s30)
transport-0-3-1-23 = refl
occ-0-3-1-24 : P.T.Occurrence tree-0-3-1
occ-0-3-1-24 = (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-0-3-1-24 : P.T.origin tree-0-3-1 occ-0-3-1-24 ≡ input s31
origin-0-3-1-24 = refl
transport-0-3-1-24 : P.T.origin tree-1-2-0 (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-0-3-1-24 = refl
occ-0-3-1-25 : P.T.Occurrence tree-0-3-1
occ-0-3-1-25 = (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-0-3-1-25 : P.T.origin tree-0-3-1 occ-0-3-1-25 ≡ input s31
origin-0-3-1-25 = refl
transport-0-3-1-25 : P.T.origin tree-1-2-0 (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-0-3-1-25 = refl
occ-0-3-1-26 : P.T.Occurrence tree-0-3-1
occ-0-3-1-26 = (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-1-2)) , (P.S.source-leg , tt)))
origin-0-3-1-26 : P.T.origin tree-0-3-1 occ-0-3-1-26 ≡ input s12
origin-0-3-1-26 = refl
transport-0-3-1-26 : P.T.origin tree-1-2-0 (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-0-3)) , (P.S.source-leg , tt))) ≡ input (swap s12)
transport-0-3-1-26 = refl
occ-0-3-1-27 : P.T.Occurrence tree-0-3-1
occ-0-3-1-27 = (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-1-2)) , (P.S.target-leg , tt)))
origin-0-3-1-27 : P.T.origin tree-0-3-1 occ-0-3-1-27 ≡ input s12
origin-0-3-1-27 = refl
transport-0-3-1-27 : P.T.origin tree-1-2-0 (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-0-3)) , (P.S.target-leg , tt))) ≡ input (swap s12)
transport-0-3-1-27 = refl
occ-0-3-1-28 : P.T.Occurrence tree-0-3-1
occ-0-3-1-28 = (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.source-leg , tt)))
origin-0-3-1-28 : P.T.origin tree-0-3-1 occ-0-3-1-28 ≡ input s12
origin-0-3-1-28 = refl
transport-0-3-1-28 : P.T.origin tree-1-2-0 (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.source-leg , tt))) ≡ input (swap s12)
transport-0-3-1-28 = refl
occ-0-3-1-29 : P.T.Occurrence tree-0-3-1
occ-0-3-1-29 = (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.target-leg , tt)))
origin-0-3-1-29 : P.T.origin tree-0-3-1 occ-0-3-1-29 ≡ input s32
origin-0-3-1-29 = refl
transport-0-3-1-29 : P.T.origin tree-1-2-0 (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.target-leg , tt))) ≡ input (swap s32)
transport-0-3-1-29 = refl
occ-0-3-1-30 : P.T.Occurrence tree-0-3-1
occ-0-3-1-30 = (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.source-leg , tt)))
origin-0-3-1-30 : P.T.origin tree-0-3-1 occ-0-3-1-30 ≡ input s32
origin-0-3-1-30 = refl
transport-0-3-1-30 : P.T.origin tree-1-2-0 (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.source-leg , tt))) ≡ input (swap s32)
transport-0-3-1-30 = refl
occ-0-3-1-31 : P.T.Occurrence tree-0-3-1
occ-0-3-1-31 = (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.target-leg , tt)))
origin-0-3-1-31 : P.T.origin tree-0-3-1 occ-0-3-1-31 ≡ input s12
origin-0-3-1-31 = refl
transport-0-3-1-31 : P.T.origin tree-1-2-0 (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.target-leg , tt))) ≡ input (swap s12)
transport-0-3-1-31 = refl
occ-0-3-1-32 : P.T.Occurrence tree-0-3-1
occ-0-3-1-32 = (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-3-2)) , (P.S.source-leg , tt)))
origin-0-3-1-32 : P.T.origin tree-0-3-1 occ-0-3-1-32 ≡ input s32
origin-0-3-1-32 = refl
transport-0-3-1-32 : P.T.origin tree-1-2-0 (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-2-3)) , (P.S.source-leg , tt))) ≡ input (swap s32)
transport-0-3-1-32 = refl
occ-0-3-1-33 : P.T.Occurrence tree-0-3-1
occ-0-3-1-33 = (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-3-2)) , (P.S.target-leg , tt)))
origin-0-3-1-33 : P.T.origin tree-0-3-1 occ-0-3-1-33 ≡ input s32
origin-0-3-1-33 = refl
transport-0-3-1-33 : P.T.origin tree-1-2-0 (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-2-3)) , (P.S.target-leg , tt))) ≡ input (swap s32)
transport-0-3-1-33 = refl
occ-0-3-1-34 : P.T.Occurrence tree-0-3-1
occ-0-3-1-34 = (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-0-3-1-34 : P.T.origin tree-0-3-1 occ-0-3-1-34 ≡ input s13
origin-0-3-1-34 = refl
transport-0-3-1-34 : P.T.origin tree-1-2-0 (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-0-3-1-34 = refl
occ-0-3-1-35 : P.T.Occurrence tree-0-3-1
occ-0-3-1-35 = (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-0-3-1-35 : P.T.origin tree-0-3-1 occ-0-3-1-35 ≡ input s13
origin-0-3-1-35 = refl
transport-0-3-1-35 : P.T.origin tree-1-2-0 (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-0-3-1-35 = refl
occ-0-3-1-36 : P.T.Occurrence tree-0-3-1
occ-0-3-1-36 = (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.source-leg , tt)))
origin-0-3-1-36 : P.T.origin tree-0-3-1 occ-0-3-1-36 ≡ input s20
origin-0-3-1-36 = refl
transport-0-3-1-36 : P.T.origin tree-1-2-0 (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-0-3-1-36 = refl
occ-0-3-1-37 : P.T.Occurrence tree-0-3-1
occ-0-3-1-37 = (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.target-leg , tt)))
origin-0-3-1-37 : P.T.origin tree-0-3-1 occ-0-3-1-37 ≡ input s10
origin-0-3-1-37 = refl
transport-0-3-1-37 : P.T.origin tree-1-2-0 (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.target-leg , tt))) ≡ input (swap s10)
transport-0-3-1-37 = refl
occ-0-3-1-38 : P.T.Occurrence tree-0-3-1
occ-0-3-1-38 = (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.source-leg , tt)))
origin-0-3-1-38 : P.T.origin tree-0-3-1 occ-0-3-1-38 ≡ input s20
origin-0-3-1-38 = refl
transport-0-3-1-38 : P.T.origin tree-1-2-0 (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-0-3-1-38 = refl
occ-0-3-1-39 : P.T.Occurrence tree-0-3-1
occ-0-3-1-39 = (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.target-leg , tt)))
origin-0-3-1-39 : P.T.origin tree-0-3-1 occ-0-3-1-39 ≡ input s30
origin-0-3-1-39 = refl
transport-0-3-1-39 : P.T.origin tree-1-2-0 (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.target-leg , tt))) ≡ input (swap s30)
transport-0-3-1-39 = refl
occ-0-3-1-40 : P.T.Occurrence tree-0-3-1
occ-0-3-1-40 = (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-0-3-1-40 : P.T.origin tree-0-3-1 occ-0-3-1-40 ≡ input s01
origin-0-3-1-40 = refl
transport-0-3-1-40 : P.T.origin tree-1-2-0 (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s01)
transport-0-3-1-40 = refl
occ-0-3-1-41 : P.T.Occurrence tree-0-3-1
occ-0-3-1-41 = (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-0-3-1-41 : P.T.origin tree-0-3-1 occ-0-3-1-41 ≡ input s31
origin-0-3-1-41 = refl
transport-0-3-1-41 : P.T.origin tree-1-2-0 (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-0-3-1-41 = refl
occ-0-3-1-42 : P.T.Occurrence tree-0-3-1
occ-0-3-1-42 = (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-0-3-1-42 : P.T.origin tree-0-3-1 occ-0-3-1-42 ≡ input s21
origin-0-3-1-42 = refl
transport-0-3-1-42 : P.T.origin tree-1-2-0 (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s21)
transport-0-3-1-42 = refl
occ-0-3-1-43 : P.T.Occurrence tree-0-3-1
occ-0-3-1-43 = (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-0-3-1-43 : P.T.origin tree-0-3-1 occ-0-3-1-43 ≡ input s31
origin-0-3-1-43 = refl
transport-0-3-1-43 : P.T.origin tree-1-2-0 (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-0-3-1-43 = refl
occ-0-3-1-44 : P.T.Occurrence tree-0-3-1
occ-0-3-1-44 = (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.source-leg , tt)))
origin-0-3-1-44 : P.T.origin tree-0-3-1 occ-0-3-1-44 ≡ input s02
origin-0-3-1-44 = refl
transport-0-3-1-44 : P.T.origin tree-1-2-0 (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-0-3-1-44 = refl
occ-0-3-1-45 : P.T.Occurrence tree-0-3-1
occ-0-3-1-45 = (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.target-leg , tt)))
origin-0-3-1-45 : P.T.origin tree-0-3-1 occ-0-3-1-45 ≡ input s12
origin-0-3-1-45 = refl
transport-0-3-1-45 : P.T.origin tree-1-2-0 (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.target-leg , tt))) ≡ input (swap s12)
transport-0-3-1-45 = refl
occ-0-3-1-46 : P.T.Occurrence tree-0-3-1
occ-0-3-1-46 = (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.source-leg , tt)))
origin-0-3-1-46 : P.T.origin tree-0-3-1 occ-0-3-1-46 ≡ input s02
origin-0-3-1-46 = refl
transport-0-3-1-46 : P.T.origin tree-1-2-0 (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-0-3-1-46 = refl
occ-0-3-1-47 : P.T.Occurrence tree-0-3-1
occ-0-3-1-47 = (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.target-leg , tt)))
origin-0-3-1-47 : P.T.origin tree-0-3-1 occ-0-3-1-47 ≡ input s32
origin-0-3-1-47 = refl
transport-0-3-1-47 : P.T.origin tree-1-2-0 (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.target-leg , tt))) ≡ input (swap s32)
transport-0-3-1-47 = refl
occ-0-3-1-48 : P.T.Occurrence tree-0-3-1
occ-0-3-1-48 = (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-0-3-1-48 : P.T.origin tree-0-3-1 occ-0-3-1-48 ≡ input s03
origin-0-3-1-48 = refl
transport-0-3-1-48 : P.T.origin tree-1-2-0 (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s03)
transport-0-3-1-48 = refl
occ-0-3-1-49 : P.T.Occurrence tree-0-3-1
occ-0-3-1-49 = (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-0-3-1-49 : P.T.origin tree-0-3-1 occ-0-3-1-49 ≡ input s13
origin-0-3-1-49 = refl
transport-0-3-1-49 : P.T.origin tree-1-2-0 (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-0-3-1-49 = refl
occ-0-3-1-50 : P.T.Occurrence tree-0-3-1
occ-0-3-1-50 = (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-0-3-1-50 : P.T.origin tree-0-3-1 occ-0-3-1-50 ≡ input s23
origin-0-3-1-50 = refl
transport-0-3-1-50 : P.T.origin tree-1-2-0 (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s23)
transport-0-3-1-50 = refl
occ-0-3-1-51 : P.T.Occurrence tree-0-3-1
occ-0-3-1-51 = (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-0-3-1-51 : P.T.origin tree-0-3-1 occ-0-3-1-51 ≡ input s13
origin-0-3-1-51 = refl
transport-0-3-1-51 : P.T.origin tree-1-2-0 (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-0-3-1-51 = refl
occ-0-3-1-52 : P.T.Occurrence tree-0-3-1
occ-0-3-1-52 = (P.S.full-source , (P.S.first-port , tt))
origin-0-3-1-52 : P.T.origin tree-0-3-1 occ-0-3-1-52 ≡ input s02
origin-0-3-1-52 = refl
transport-0-3-1-52 : P.T.origin tree-1-2-0 (P.S.full-source , (P.S.first-port , tt)) ≡ input (swap s02)
transport-0-3-1-52 = refl
occ-0-3-1-53 : P.T.Occurrence tree-0-3-1
occ-0-3-1-53 = (P.S.full-source , (P.S.middle-port , tt))
origin-0-3-1-53 : P.T.origin tree-0-3-1 occ-0-3-1-53 ≡ input s32
origin-0-3-1-53 = refl
transport-0-3-1-53 : P.T.origin tree-1-2-0 (P.S.full-source , (P.S.middle-port , tt)) ≡ input (swap s32)
transport-0-3-1-53 = refl
occ-0-3-1-54 : P.T.Occurrence tree-0-3-1
occ-0-3-1-54 = (P.S.full-source , (P.S.final-port , tt))
origin-0-3-1-54 : P.T.origin tree-0-3-1 occ-0-3-1-54 ≡ input s12
origin-0-3-1-54 = refl
transport-0-3-1-54 : P.T.origin tree-1-2-0 (P.S.full-source , (P.S.final-port , tt)) ≡ input (swap s12)
transport-0-3-1-54 = refl
selected-source-0-3-1-AB : P.S.ab-index {a = C.q0} {b = C.q7} {c = C.q7} F.triple-0-3-1 ≡ (c1 , (F.vp-0-2 , F.vp-3-2))
selected-source-0-3-1-AB = refl
selected-target-0-3-1-AB : P.S.ab-index {a = C.q7} {b = C.q0} {c = C.q0} F.triple-1-2-0 ≡ (m1 , (F.vp-1-3 , F.vp-2-3))
selected-target-0-3-1-AB = refl
selected-source-0-3-1-BC : P.S.bc-index {a = C.q0} {b = C.q7} {c = C.q7} F.triple-0-3-1 ≡ (c1 , (F.vp-3-2 , F.vp-1-2))
selected-source-0-3-1-BC = refl
selected-target-0-3-1-BC : P.S.bc-index {a = C.q7} {b = C.q0} {c = C.q0} F.triple-1-2-0 ≡ (m1 , (F.vp-2-3 , F.vp-0-3))
selected-target-0-3-1-BC = refl
selected-source-0-3-1-AC : P.S.ac-index {a = C.q0} {b = C.q7} {c = C.q7} F.triple-0-3-1 ≡ (c1 , (F.vp-0-2 , F.vp-1-2))
selected-source-0-3-1-AC = refl
selected-target-0-3-1-AC : P.S.ac-index {a = C.q7} {b = C.q0} {c = C.q0} F.triple-1-2-0 ≡ (m1 , (F.vp-1-3 , F.vp-0-3))
selected-target-0-3-1-AC = refl
occ-0-3-2-0 : P.T.Occurrence tree-0-3-2
occ-0-3-2-0 = (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.source-leg , tt)))
origin-0-3-2-0 : P.T.origin tree-0-3-2 occ-0-3-2-0 ≡ input s20
origin-0-3-2-0 = refl
transport-0-3-2-0 : P.T.origin tree-1-2-3 (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-0-3-2-0 = refl
occ-0-3-2-1 : P.T.Occurrence tree-0-3-2
occ-0-3-2-1 = (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.target-leg , tt)))
origin-0-3-2-1 : P.T.origin tree-0-3-2 occ-0-3-2-1 ≡ input s10
origin-0-3-2-1 = refl
transport-0-3-2-1 : P.T.origin tree-1-2-3 (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.target-leg , tt))) ≡ input (swap s10)
transport-0-3-2-1 = refl
occ-0-3-2-2 : P.T.Occurrence tree-0-3-2
occ-0-3-2-2 = (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.source-leg , tt)))
origin-0-3-2-2 : P.T.origin tree-0-3-2 occ-0-3-2-2 ≡ input s20
origin-0-3-2-2 = refl
transport-0-3-2-2 : P.T.origin tree-1-2-3 (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-0-3-2-2 = refl
occ-0-3-2-3 : P.T.Occurrence tree-0-3-2
occ-0-3-2-3 = (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.target-leg , tt)))
origin-0-3-2-3 : P.T.origin tree-0-3-2 occ-0-3-2-3 ≡ input s30
origin-0-3-2-3 = refl
transport-0-3-2-3 : P.T.origin tree-1-2-3 (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.target-leg , tt))) ≡ input (swap s30)
transport-0-3-2-3 = refl
occ-0-3-2-4 : P.T.Occurrence tree-0-3-2
occ-0-3-2-4 = (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-0-3-2-4 : P.T.origin tree-0-3-2 occ-0-3-2-4 ≡ input s01
origin-0-3-2-4 = refl
transport-0-3-2-4 : P.T.origin tree-1-2-3 (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s01)
transport-0-3-2-4 = refl
occ-0-3-2-5 : P.T.Occurrence tree-0-3-2
occ-0-3-2-5 = (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-0-3-2-5 : P.T.origin tree-0-3-2 occ-0-3-2-5 ≡ input s31
origin-0-3-2-5 = refl
transport-0-3-2-5 : P.T.origin tree-1-2-3 (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-0-3-2-5 = refl
occ-0-3-2-6 : P.T.Occurrence tree-0-3-2
occ-0-3-2-6 = (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-0-3-2-6 : P.T.origin tree-0-3-2 occ-0-3-2-6 ≡ input s21
origin-0-3-2-6 = refl
transport-0-3-2-6 : P.T.origin tree-1-2-3 (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s21)
transport-0-3-2-6 = refl
occ-0-3-2-7 : P.T.Occurrence tree-0-3-2
occ-0-3-2-7 = (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-0-3-2-7 : P.T.origin tree-0-3-2 occ-0-3-2-7 ≡ input s31
origin-0-3-2-7 = refl
transport-0-3-2-7 : P.T.origin tree-1-2-3 (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-0-3-2-7 = refl
occ-0-3-2-8 : P.T.Occurrence tree-0-3-2
occ-0-3-2-8 = (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.source-leg , tt)))
origin-0-3-2-8 : P.T.origin tree-0-3-2 occ-0-3-2-8 ≡ input s02
origin-0-3-2-8 = refl
transport-0-3-2-8 : P.T.origin tree-1-2-3 (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-0-3-2-8 = refl
occ-0-3-2-9 : P.T.Occurrence tree-0-3-2
occ-0-3-2-9 = (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.target-leg , tt)))
origin-0-3-2-9 : P.T.origin tree-0-3-2 occ-0-3-2-9 ≡ input s12
origin-0-3-2-9 = refl
transport-0-3-2-9 : P.T.origin tree-1-2-3 (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.target-leg , tt))) ≡ input (swap s12)
transport-0-3-2-9 = refl
occ-0-3-2-10 : P.T.Occurrence tree-0-3-2
occ-0-3-2-10 = (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.source-leg , tt)))
origin-0-3-2-10 : P.T.origin tree-0-3-2 occ-0-3-2-10 ≡ input s02
origin-0-3-2-10 = refl
transport-0-3-2-10 : P.T.origin tree-1-2-3 (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-0-3-2-10 = refl
occ-0-3-2-11 : P.T.Occurrence tree-0-3-2
occ-0-3-2-11 = (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.target-leg , tt)))
origin-0-3-2-11 : P.T.origin tree-0-3-2 occ-0-3-2-11 ≡ input s32
origin-0-3-2-11 = refl
transport-0-3-2-11 : P.T.origin tree-1-2-3 (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.target-leg , tt))) ≡ input (swap s32)
transport-0-3-2-11 = refl
occ-0-3-2-12 : P.T.Occurrence tree-0-3-2
occ-0-3-2-12 = (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-0-3-2-12 : P.T.origin tree-0-3-2 occ-0-3-2-12 ≡ input s03
origin-0-3-2-12 = refl
transport-0-3-2-12 : P.T.origin tree-1-2-3 (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s03)
transport-0-3-2-12 = refl
occ-0-3-2-13 : P.T.Occurrence tree-0-3-2
occ-0-3-2-13 = (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-0-3-2-13 : P.T.origin tree-0-3-2 occ-0-3-2-13 ≡ input s13
origin-0-3-2-13 = refl
transport-0-3-2-13 : P.T.origin tree-1-2-3 (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-0-3-2-13 = refl
occ-0-3-2-14 : P.T.Occurrence tree-0-3-2
occ-0-3-2-14 = (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-0-3-2-14 : P.T.origin tree-0-3-2 occ-0-3-2-14 ≡ input s23
origin-0-3-2-14 = refl
transport-0-3-2-14 : P.T.origin tree-1-2-3 (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s23)
transport-0-3-2-14 = refl
occ-0-3-2-15 : P.T.Occurrence tree-0-3-2
occ-0-3-2-15 = (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-0-3-2-15 : P.T.origin tree-0-3-2 occ-0-3-2-15 ≡ input s13
origin-0-3-2-15 = refl
transport-0-3-2-15 : P.T.origin tree-1-2-3 (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-0-3-2-15 = refl
occ-0-3-2-16 : P.T.Occurrence tree-0-3-2
occ-0-3-2-16 = (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-0-3-2-16 : P.T.origin tree-0-3-2 occ-0-3-2-16 ≡ input s10
origin-0-3-2-16 = refl
transport-0-3-2-16 : P.T.origin tree-1-2-3 (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s10)
transport-0-3-2-16 = refl
occ-0-3-2-17 : P.T.Occurrence tree-0-3-2
occ-0-3-2-17 = (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-0-3-2-17 : P.T.origin tree-0-3-2 occ-0-3-2-17 ≡ input s20
origin-0-3-2-17 = refl
transport-0-3-2-17 : P.T.origin tree-1-2-3 (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-0-3-2-17 = refl
occ-0-3-2-18 : P.T.Occurrence tree-0-3-2
occ-0-3-2-18 = (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-0-3-2-18 : P.T.origin tree-0-3-2 occ-0-3-2-18 ≡ input s30
origin-0-3-2-18 = refl
transport-0-3-2-18 : P.T.origin tree-1-2-3 (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s30)
transport-0-3-2-18 = refl
occ-0-3-2-19 : P.T.Occurrence tree-0-3-2
occ-0-3-2-19 = (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-0-3-2-19 : P.T.origin tree-0-3-2 occ-0-3-2-19 ≡ input s20
origin-0-3-2-19 = refl
transport-0-3-2-19 : P.T.origin tree-1-2-3 (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-0-3-2-19 = refl
occ-0-3-2-20 : P.T.Occurrence tree-0-3-2
occ-0-3-2-20 = (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.source-leg , tt)))
origin-0-3-2-20 : P.T.origin tree-0-3-2 occ-0-3-2-20 ≡ input s31
origin-0-3-2-20 = refl
transport-0-3-2-20 : P.T.origin tree-1-2-3 (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-0-3-2-20 = refl
occ-0-3-2-21 : P.T.Occurrence tree-0-3-2
occ-0-3-2-21 = (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.target-leg , tt)))
origin-0-3-2-21 : P.T.origin tree-0-3-2 occ-0-3-2-21 ≡ input s01
origin-0-3-2-21 = refl
transport-0-3-2-21 : P.T.origin tree-1-2-3 (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.target-leg , tt))) ≡ input (swap s01)
transport-0-3-2-21 = refl
occ-0-3-2-22 : P.T.Occurrence tree-0-3-2
occ-0-3-2-22 = (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.source-leg , tt)))
origin-0-3-2-22 : P.T.origin tree-0-3-2 occ-0-3-2-22 ≡ input s31
origin-0-3-2-22 = refl
transport-0-3-2-22 : P.T.origin tree-1-2-3 (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-0-3-2-22 = refl
occ-0-3-2-23 : P.T.Occurrence tree-0-3-2
occ-0-3-2-23 = (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.target-leg , tt)))
origin-0-3-2-23 : P.T.origin tree-0-3-2 occ-0-3-2-23 ≡ input s21
origin-0-3-2-23 = refl
transport-0-3-2-23 : P.T.origin tree-1-2-3 (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.target-leg , tt))) ≡ input (swap s21)
transport-0-3-2-23 = refl
occ-0-3-2-24 : P.T.Occurrence tree-0-3-2
occ-0-3-2-24 = (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-0-3-2-24 : P.T.origin tree-0-3-2 occ-0-3-2-24 ≡ input s12
origin-0-3-2-24 = refl
transport-0-3-2-24 : P.T.origin tree-1-2-3 (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s12)
transport-0-3-2-24 = refl
occ-0-3-2-25 : P.T.Occurrence tree-0-3-2
occ-0-3-2-25 = (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-0-3-2-25 : P.T.origin tree-0-3-2 occ-0-3-2-25 ≡ input s02
origin-0-3-2-25 = refl
transport-0-3-2-25 : P.T.origin tree-1-2-3 (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-0-3-2-25 = refl
occ-0-3-2-26 : P.T.Occurrence tree-0-3-2
occ-0-3-2-26 = (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-0-3-2-26 : P.T.origin tree-0-3-2 occ-0-3-2-26 ≡ input s32
origin-0-3-2-26 = refl
transport-0-3-2-26 : P.T.origin tree-1-2-3 (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s32)
transport-0-3-2-26 = refl
occ-0-3-2-27 : P.T.Occurrence tree-0-3-2
occ-0-3-2-27 = (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-0-3-2-27 : P.T.origin tree-0-3-2 occ-0-3-2-27 ≡ input s02
origin-0-3-2-27 = refl
transport-0-3-2-27 : P.T.origin tree-1-2-3 (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-0-3-2-27 = refl
occ-0-3-2-28 : P.T.Occurrence tree-0-3-2
occ-0-3-2-28 = (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.source-leg , tt)))
origin-0-3-2-28 : P.T.origin tree-0-3-2 occ-0-3-2-28 ≡ input s13
origin-0-3-2-28 = refl
transport-0-3-2-28 : P.T.origin tree-1-2-3 (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-0-3-2-28 = refl
occ-0-3-2-29 : P.T.Occurrence tree-0-3-2
occ-0-3-2-29 = (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.target-leg , tt)))
origin-0-3-2-29 : P.T.origin tree-0-3-2 occ-0-3-2-29 ≡ input s03
origin-0-3-2-29 = refl
transport-0-3-2-29 : P.T.origin tree-1-2-3 (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.target-leg , tt))) ≡ input (swap s03)
transport-0-3-2-29 = refl
occ-0-3-2-30 : P.T.Occurrence tree-0-3-2
occ-0-3-2-30 = (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.source-leg , tt)))
origin-0-3-2-30 : P.T.origin tree-0-3-2 occ-0-3-2-30 ≡ input s13
origin-0-3-2-30 = refl
transport-0-3-2-30 : P.T.origin tree-1-2-3 (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-0-3-2-30 = refl
occ-0-3-2-31 : P.T.Occurrence tree-0-3-2
occ-0-3-2-31 = (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.target-leg , tt)))
origin-0-3-2-31 : P.T.origin tree-0-3-2 occ-0-3-2-31 ≡ input s23
origin-0-3-2-31 = refl
transport-0-3-2-31 : P.T.origin tree-1-2-3 (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.target-leg , tt))) ≡ input (swap s23)
transport-0-3-2-31 = refl
occ-0-3-2-32 : P.T.Occurrence tree-0-3-2
occ-0-3-2-32 = (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-0-3-2-32 : P.T.origin tree-0-3-2 occ-0-3-2-32 ≡ input s20
origin-0-3-2-32 = refl
transport-0-3-2-32 : P.T.origin tree-1-2-3 (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-0-3-2-32 = refl
occ-0-3-2-33 : P.T.Occurrence tree-0-3-2
occ-0-3-2-33 = (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-0-3-2-33 : P.T.origin tree-0-3-2 occ-0-3-2-33 ≡ input s20
origin-0-3-2-33 = refl
transport-0-3-2-33 : P.T.origin tree-1-2-3 (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-0-3-2-33 = refl
occ-0-3-2-34 : P.T.Occurrence tree-0-3-2
occ-0-3-2-34 = (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-0-1)) , (P.S.source-leg , tt)))
origin-0-3-2-34 : P.T.origin tree-0-3-2 occ-0-3-2-34 ≡ input s01
origin-0-3-2-34 = refl
transport-0-3-2-34 : P.T.origin tree-1-2-3 (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-1-0)) , (P.S.source-leg , tt))) ≡ input (swap s01)
transport-0-3-2-34 = refl
occ-0-3-2-35 : P.T.Occurrence tree-0-3-2
occ-0-3-2-35 = (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-0-1)) , (P.S.target-leg , tt)))
origin-0-3-2-35 : P.T.origin tree-0-3-2 occ-0-3-2-35 ≡ input s01
origin-0-3-2-35 = refl
transport-0-3-2-35 : P.T.origin tree-1-2-3 (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-1-0)) , (P.S.target-leg , tt))) ≡ input (swap s01)
transport-0-3-2-35 = refl
occ-0-3-2-36 : P.T.Occurrence tree-0-3-2
occ-0-3-2-36 = (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.source-leg , tt)))
origin-0-3-2-36 : P.T.origin tree-0-3-2 occ-0-3-2-36 ≡ input s01
origin-0-3-2-36 = refl
transport-0-3-2-36 : P.T.origin tree-1-2-3 (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.source-leg , tt))) ≡ input (swap s01)
transport-0-3-2-36 = refl
occ-0-3-2-37 : P.T.Occurrence tree-0-3-2
occ-0-3-2-37 = (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.target-leg , tt)))
origin-0-3-2-37 : P.T.origin tree-0-3-2 occ-0-3-2-37 ≡ input s21
origin-0-3-2-37 = refl
transport-0-3-2-37 : P.T.origin tree-1-2-3 (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.target-leg , tt))) ≡ input (swap s21)
transport-0-3-2-37 = refl
occ-0-3-2-38 : P.T.Occurrence tree-0-3-2
occ-0-3-2-38 = (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.source-leg , tt)))
origin-0-3-2-38 : P.T.origin tree-0-3-2 occ-0-3-2-38 ≡ input s21
origin-0-3-2-38 = refl
transport-0-3-2-38 : P.T.origin tree-1-2-3 (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.source-leg , tt))) ≡ input (swap s21)
transport-0-3-2-38 = refl
occ-0-3-2-39 : P.T.Occurrence tree-0-3-2
occ-0-3-2-39 = (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.target-leg , tt)))
origin-0-3-2-39 : P.T.origin tree-0-3-2 occ-0-3-2-39 ≡ input s01
origin-0-3-2-39 = refl
transport-0-3-2-39 : P.T.origin tree-1-2-3 (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.target-leg , tt))) ≡ input (swap s01)
transport-0-3-2-39 = refl
occ-0-3-2-40 : P.T.Occurrence tree-0-3-2
occ-0-3-2-40 = (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-2-1)) , (P.S.source-leg , tt)))
origin-0-3-2-40 : P.T.origin tree-0-3-2 occ-0-3-2-40 ≡ input s21
origin-0-3-2-40 = refl
transport-0-3-2-40 : P.T.origin tree-1-2-3 (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-3-0)) , (P.S.source-leg , tt))) ≡ input (swap s21)
transport-0-3-2-40 = refl
occ-0-3-2-41 : P.T.Occurrence tree-0-3-2
occ-0-3-2-41 = (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-2-1)) , (P.S.target-leg , tt)))
origin-0-3-2-41 : P.T.origin tree-0-3-2 occ-0-3-2-41 ≡ input s21
origin-0-3-2-41 = refl
transport-0-3-2-41 : P.T.origin tree-1-2-3 (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-3-0)) , (P.S.target-leg , tt))) ≡ input (swap s21)
transport-0-3-2-41 = refl
occ-0-3-2-42 : P.T.Occurrence tree-0-3-2
occ-0-3-2-42 = (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-0-3-2-42 : P.T.origin tree-0-3-2 occ-0-3-2-42 ≡ input s02
origin-0-3-2-42 = refl
transport-0-3-2-42 : P.T.origin tree-1-2-3 (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-0-3-2-42 = refl
occ-0-3-2-43 : P.T.Occurrence tree-0-3-2
occ-0-3-2-43 = (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-0-3-2-43 : P.T.origin tree-0-3-2 occ-0-3-2-43 ≡ input s02
origin-0-3-2-43 = refl
transport-0-3-2-43 : P.T.origin tree-1-2-3 (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-0-3-2-43 = refl
occ-0-3-2-44 : P.T.Occurrence tree-0-3-2
occ-0-3-2-44 = (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-0-3)) , (P.S.source-leg , tt)))
origin-0-3-2-44 : P.T.origin tree-0-3-2 occ-0-3-2-44 ≡ input s03
origin-0-3-2-44 = refl
transport-0-3-2-44 : P.T.origin tree-1-2-3 (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-1-2)) , (P.S.source-leg , tt))) ≡ input (swap s03)
transport-0-3-2-44 = refl
occ-0-3-2-45 : P.T.Occurrence tree-0-3-2
occ-0-3-2-45 = (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-0-3)) , (P.S.target-leg , tt)))
origin-0-3-2-45 : P.T.origin tree-0-3-2 occ-0-3-2-45 ≡ input s03
origin-0-3-2-45 = refl
transport-0-3-2-45 : P.T.origin tree-1-2-3 (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-1-2)) , (P.S.target-leg , tt))) ≡ input (swap s03)
transport-0-3-2-45 = refl
occ-0-3-2-46 : P.T.Occurrence tree-0-3-2
occ-0-3-2-46 = (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.source-leg , tt)))
origin-0-3-2-46 : P.T.origin tree-0-3-2 occ-0-3-2-46 ≡ input s03
origin-0-3-2-46 = refl
transport-0-3-2-46 : P.T.origin tree-1-2-3 (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.source-leg , tt))) ≡ input (swap s03)
transport-0-3-2-46 = refl
occ-0-3-2-47 : P.T.Occurrence tree-0-3-2
occ-0-3-2-47 = (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.target-leg , tt)))
origin-0-3-2-47 : P.T.origin tree-0-3-2 occ-0-3-2-47 ≡ input s23
origin-0-3-2-47 = refl
transport-0-3-2-47 : P.T.origin tree-1-2-3 (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.target-leg , tt))) ≡ input (swap s23)
transport-0-3-2-47 = refl
occ-0-3-2-48 : P.T.Occurrence tree-0-3-2
occ-0-3-2-48 = (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.source-leg , tt)))
origin-0-3-2-48 : P.T.origin tree-0-3-2 occ-0-3-2-48 ≡ input s23
origin-0-3-2-48 = refl
transport-0-3-2-48 : P.T.origin tree-1-2-3 (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.source-leg , tt))) ≡ input (swap s23)
transport-0-3-2-48 = refl
occ-0-3-2-49 : P.T.Occurrence tree-0-3-2
occ-0-3-2-49 = (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.target-leg , tt)))
origin-0-3-2-49 : P.T.origin tree-0-3-2 occ-0-3-2-49 ≡ input s03
origin-0-3-2-49 = refl
transport-0-3-2-49 : P.T.origin tree-1-2-3 (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.target-leg , tt))) ≡ input (swap s03)
transport-0-3-2-49 = refl
occ-0-3-2-50 : P.T.Occurrence tree-0-3-2
occ-0-3-2-50 = (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-2-3)) , (P.S.source-leg , tt)))
origin-0-3-2-50 : P.T.origin tree-0-3-2 occ-0-3-2-50 ≡ input s23
origin-0-3-2-50 = refl
transport-0-3-2-50 : P.T.origin tree-1-2-3 (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-3-2)) , (P.S.source-leg , tt))) ≡ input (swap s23)
transport-0-3-2-50 = refl
occ-0-3-2-51 : P.T.Occurrence tree-0-3-2
occ-0-3-2-51 = (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-2-3)) , (P.S.target-leg , tt)))
origin-0-3-2-51 : P.T.origin tree-0-3-2 occ-0-3-2-51 ≡ input s23
origin-0-3-2-51 = refl
transport-0-3-2-51 : P.T.origin tree-1-2-3 (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-3-2)) , (P.S.target-leg , tt))) ≡ input (swap s23)
transport-0-3-2-51 = refl
occ-0-3-2-52 : P.T.Occurrence tree-0-3-2
occ-0-3-2-52 = (P.S.full-source , (P.S.first-port , tt))
origin-0-3-2-52 : P.T.origin tree-0-3-2 occ-0-3-2-52 ≡ input s01
origin-0-3-2-52 = refl
transport-0-3-2-52 : P.T.origin tree-1-2-3 (P.S.full-source , (P.S.first-port , tt)) ≡ input (swap s01)
transport-0-3-2-52 = refl
occ-0-3-2-53 : P.T.Occurrence tree-0-3-2
occ-0-3-2-53 = (P.S.full-source , (P.S.middle-port , tt))
origin-0-3-2-53 : P.T.origin tree-0-3-2 occ-0-3-2-53 ≡ input s31
origin-0-3-2-53 = refl
transport-0-3-2-53 : P.T.origin tree-1-2-3 (P.S.full-source , (P.S.middle-port , tt)) ≡ input (swap s31)
transport-0-3-2-53 = refl
occ-0-3-2-54 : P.T.Occurrence tree-0-3-2
occ-0-3-2-54 = (P.S.full-source , (P.S.final-port , tt))
origin-0-3-2-54 : P.T.origin tree-0-3-2 occ-0-3-2-54 ≡ input s21
origin-0-3-2-54 = refl
transport-0-3-2-54 : P.T.origin tree-1-2-3 (P.S.full-source , (P.S.final-port , tt)) ≡ input (swap s21)
transport-0-3-2-54 = refl
selected-source-0-3-2-AB : P.S.ab-index {a = C.q0} {b = C.q7} {c = C.q0} F.triple-0-3-2 ≡ (m0 , (F.vp-0-1 , F.vp-3-1))
selected-source-0-3-2-AB = refl
selected-target-0-3-2-AB : P.S.ab-index {a = C.q7} {b = C.q0} {c = C.q7} F.triple-1-2-3 ≡ (c0 , (F.vp-1-0 , F.vp-2-0))
selected-target-0-3-2-AB = refl
selected-source-0-3-2-BC : P.S.bc-index {a = C.q0} {b = C.q7} {c = C.q0} F.triple-0-3-2 ≡ (m0 , (F.vp-3-1 , F.vp-2-1))
selected-source-0-3-2-BC = refl
selected-target-0-3-2-BC : P.S.bc-index {a = C.q7} {b = C.q0} {c = C.q7} F.triple-1-2-3 ≡ (c0 , (F.vp-2-0 , F.vp-3-0))
selected-target-0-3-2-BC = refl
selected-source-0-3-2-AC : P.S.ac-index {a = C.q0} {b = C.q7} {c = C.q0} F.triple-0-3-2 ≡ (m0 , (F.vp-0-1 , F.vp-2-1))
selected-source-0-3-2-AC = refl
selected-target-0-3-2-AC : P.S.ac-index {a = C.q7} {b = C.q0} {c = C.q7} F.triple-1-2-3 ≡ (c0 , (F.vp-1-0 , F.vp-3-0))
selected-target-0-3-2-AC = refl
occ-1-0-2-0 : P.T.Occurrence tree-1-0-2
occ-1-0-2-0 = (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-1-0-2-0 : P.T.origin tree-1-0-2 occ-1-0-2-0 ≡ input s10
origin-1-0-2-0 = refl
transport-1-0-2-0 : P.T.origin tree-0-1-3 (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s10)
transport-1-0-2-0 = refl
occ-1-0-2-1 : P.T.Occurrence tree-1-0-2
occ-1-0-2-1 = (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-1-0-2-1 : P.T.origin tree-1-0-2 occ-1-0-2-1 ≡ input s20
origin-1-0-2-1 = refl
transport-1-0-2-1 : P.T.origin tree-0-1-3 (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-1-0-2-1 = refl
occ-1-0-2-2 : P.T.Occurrence tree-1-0-2
occ-1-0-2-2 = (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-1-0-2-2 : P.T.origin tree-1-0-2 occ-1-0-2-2 ≡ input s30
origin-1-0-2-2 = refl
transport-1-0-2-2 : P.T.origin tree-0-1-3 (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s30)
transport-1-0-2-2 = refl
occ-1-0-2-3 : P.T.Occurrence tree-1-0-2
occ-1-0-2-3 = (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-1-0-2-3 : P.T.origin tree-1-0-2 occ-1-0-2-3 ≡ input s20
origin-1-0-2-3 = refl
transport-1-0-2-3 : P.T.origin tree-0-1-3 (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-1-0-2-3 = refl
occ-1-0-2-4 : P.T.Occurrence tree-1-0-2
occ-1-0-2-4 = (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.source-leg , tt)))
origin-1-0-2-4 : P.T.origin tree-1-0-2 occ-1-0-2-4 ≡ input s31
origin-1-0-2-4 = refl
transport-1-0-2-4 : P.T.origin tree-0-1-3 (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-1-0-2-4 = refl
occ-1-0-2-5 : P.T.Occurrence tree-1-0-2
occ-1-0-2-5 = (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.target-leg , tt)))
origin-1-0-2-5 : P.T.origin tree-1-0-2 occ-1-0-2-5 ≡ input s01
origin-1-0-2-5 = refl
transport-1-0-2-5 : P.T.origin tree-0-1-3 (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.target-leg , tt))) ≡ input (swap s01)
transport-1-0-2-5 = refl
occ-1-0-2-6 : P.T.Occurrence tree-1-0-2
occ-1-0-2-6 = (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.source-leg , tt)))
origin-1-0-2-6 : P.T.origin tree-1-0-2 occ-1-0-2-6 ≡ input s31
origin-1-0-2-6 = refl
transport-1-0-2-6 : P.T.origin tree-0-1-3 (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-1-0-2-6 = refl
occ-1-0-2-7 : P.T.Occurrence tree-1-0-2
occ-1-0-2-7 = (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.target-leg , tt)))
origin-1-0-2-7 : P.T.origin tree-1-0-2 occ-1-0-2-7 ≡ input s21
origin-1-0-2-7 = refl
transport-1-0-2-7 : P.T.origin tree-0-1-3 (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.target-leg , tt))) ≡ input (swap s21)
transport-1-0-2-7 = refl
occ-1-0-2-8 : P.T.Occurrence tree-1-0-2
occ-1-0-2-8 = (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-1-0-2-8 : P.T.origin tree-1-0-2 occ-1-0-2-8 ≡ input s12
origin-1-0-2-8 = refl
transport-1-0-2-8 : P.T.origin tree-0-1-3 (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s12)
transport-1-0-2-8 = refl
occ-1-0-2-9 : P.T.Occurrence tree-1-0-2
occ-1-0-2-9 = (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-1-0-2-9 : P.T.origin tree-1-0-2 occ-1-0-2-9 ≡ input s02
origin-1-0-2-9 = refl
transport-1-0-2-9 : P.T.origin tree-0-1-3 (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-1-0-2-9 = refl
occ-1-0-2-10 : P.T.Occurrence tree-1-0-2
occ-1-0-2-10 = (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-1-0-2-10 : P.T.origin tree-1-0-2 occ-1-0-2-10 ≡ input s32
origin-1-0-2-10 = refl
transport-1-0-2-10 : P.T.origin tree-0-1-3 (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s32)
transport-1-0-2-10 = refl
occ-1-0-2-11 : P.T.Occurrence tree-1-0-2
occ-1-0-2-11 = (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-1-0-2-11 : P.T.origin tree-1-0-2 occ-1-0-2-11 ≡ input s02
origin-1-0-2-11 = refl
transport-1-0-2-11 : P.T.origin tree-0-1-3 (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-1-0-2-11 = refl
occ-1-0-2-12 : P.T.Occurrence tree-1-0-2
occ-1-0-2-12 = (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.source-leg , tt)))
origin-1-0-2-12 : P.T.origin tree-1-0-2 occ-1-0-2-12 ≡ input s13
origin-1-0-2-12 = refl
transport-1-0-2-12 : P.T.origin tree-0-1-3 (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-1-0-2-12 = refl
occ-1-0-2-13 : P.T.Occurrence tree-1-0-2
occ-1-0-2-13 = (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.target-leg , tt)))
origin-1-0-2-13 : P.T.origin tree-1-0-2 occ-1-0-2-13 ≡ input s03
origin-1-0-2-13 = refl
transport-1-0-2-13 : P.T.origin tree-0-1-3 (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.target-leg , tt))) ≡ input (swap s03)
transport-1-0-2-13 = refl
occ-1-0-2-14 : P.T.Occurrence tree-1-0-2
occ-1-0-2-14 = (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.source-leg , tt)))
origin-1-0-2-14 : P.T.origin tree-1-0-2 occ-1-0-2-14 ≡ input s13
origin-1-0-2-14 = refl
transport-1-0-2-14 : P.T.origin tree-0-1-3 (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-1-0-2-14 = refl
occ-1-0-2-15 : P.T.Occurrence tree-1-0-2
occ-1-0-2-15 = (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.target-leg , tt)))
origin-1-0-2-15 : P.T.origin tree-1-0-2 occ-1-0-2-15 ≡ input s23
origin-1-0-2-15 = refl
transport-1-0-2-15 : P.T.origin tree-0-1-3 (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.target-leg , tt))) ≡ input (swap s23)
transport-1-0-2-15 = refl
occ-1-0-2-16 : P.T.Occurrence tree-1-0-2
occ-1-0-2-16 = (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-1-0-2-16 : P.T.origin tree-1-0-2 occ-1-0-2-16 ≡ input s20
origin-1-0-2-16 = refl
transport-1-0-2-16 : P.T.origin tree-0-1-3 (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-1-0-2-16 = refl
occ-1-0-2-17 : P.T.Occurrence tree-1-0-2
occ-1-0-2-17 = (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-1-0-2-17 : P.T.origin tree-1-0-2 occ-1-0-2-17 ≡ input s20
origin-1-0-2-17 = refl
transport-1-0-2-17 : P.T.origin tree-0-1-3 (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-1-0-2-17 = refl
occ-1-0-2-18 : P.T.Occurrence tree-1-0-2
occ-1-0-2-18 = (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-0-1)) , (P.S.source-leg , tt)))
origin-1-0-2-18 : P.T.origin tree-1-0-2 occ-1-0-2-18 ≡ input s01
origin-1-0-2-18 = refl
transport-1-0-2-18 : P.T.origin tree-0-1-3 (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-1-0)) , (P.S.source-leg , tt))) ≡ input (swap s01)
transport-1-0-2-18 = refl
occ-1-0-2-19 : P.T.Occurrence tree-1-0-2
occ-1-0-2-19 = (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-0-1)) , (P.S.target-leg , tt)))
origin-1-0-2-19 : P.T.origin tree-1-0-2 occ-1-0-2-19 ≡ input s01
origin-1-0-2-19 = refl
transport-1-0-2-19 : P.T.origin tree-0-1-3 (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-1-0)) , (P.S.target-leg , tt))) ≡ input (swap s01)
transport-1-0-2-19 = refl
occ-1-0-2-20 : P.T.Occurrence tree-1-0-2
occ-1-0-2-20 = (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.source-leg , tt)))
origin-1-0-2-20 : P.T.origin tree-1-0-2 occ-1-0-2-20 ≡ input s01
origin-1-0-2-20 = refl
transport-1-0-2-20 : P.T.origin tree-0-1-3 (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.source-leg , tt))) ≡ input (swap s01)
transport-1-0-2-20 = refl
occ-1-0-2-21 : P.T.Occurrence tree-1-0-2
occ-1-0-2-21 = (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.target-leg , tt)))
origin-1-0-2-21 : P.T.origin tree-1-0-2 occ-1-0-2-21 ≡ input s21
origin-1-0-2-21 = refl
transport-1-0-2-21 : P.T.origin tree-0-1-3 (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.target-leg , tt))) ≡ input (swap s21)
transport-1-0-2-21 = refl
occ-1-0-2-22 : P.T.Occurrence tree-1-0-2
occ-1-0-2-22 = (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.source-leg , tt)))
origin-1-0-2-22 : P.T.origin tree-1-0-2 occ-1-0-2-22 ≡ input s21
origin-1-0-2-22 = refl
transport-1-0-2-22 : P.T.origin tree-0-1-3 (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.source-leg , tt))) ≡ input (swap s21)
transport-1-0-2-22 = refl
occ-1-0-2-23 : P.T.Occurrence tree-1-0-2
occ-1-0-2-23 = (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.target-leg , tt)))
origin-1-0-2-23 : P.T.origin tree-1-0-2 occ-1-0-2-23 ≡ input s01
origin-1-0-2-23 = refl
transport-1-0-2-23 : P.T.origin tree-0-1-3 (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.target-leg , tt))) ≡ input (swap s01)
transport-1-0-2-23 = refl
occ-1-0-2-24 : P.T.Occurrence tree-1-0-2
occ-1-0-2-24 = (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-2-1)) , (P.S.source-leg , tt)))
origin-1-0-2-24 : P.T.origin tree-1-0-2 occ-1-0-2-24 ≡ input s21
origin-1-0-2-24 = refl
transport-1-0-2-24 : P.T.origin tree-0-1-3 (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-3-0)) , (P.S.source-leg , tt))) ≡ input (swap s21)
transport-1-0-2-24 = refl
occ-1-0-2-25 : P.T.Occurrence tree-1-0-2
occ-1-0-2-25 = (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-2-1)) , (P.S.target-leg , tt)))
origin-1-0-2-25 : P.T.origin tree-1-0-2 occ-1-0-2-25 ≡ input s21
origin-1-0-2-25 = refl
transport-1-0-2-25 : P.T.origin tree-0-1-3 (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-3-0)) , (P.S.target-leg , tt))) ≡ input (swap s21)
transport-1-0-2-25 = refl
occ-1-0-2-26 : P.T.Occurrence tree-1-0-2
occ-1-0-2-26 = (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-1-0-2-26 : P.T.origin tree-1-0-2 occ-1-0-2-26 ≡ input s02
origin-1-0-2-26 = refl
transport-1-0-2-26 : P.T.origin tree-0-1-3 (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-1-0-2-26 = refl
occ-1-0-2-27 : P.T.Occurrence tree-1-0-2
occ-1-0-2-27 = (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-1-0-2-27 : P.T.origin tree-1-0-2 occ-1-0-2-27 ≡ input s02
origin-1-0-2-27 = refl
transport-1-0-2-27 : P.T.origin tree-0-1-3 (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-1-0-2-27 = refl
occ-1-0-2-28 : P.T.Occurrence tree-1-0-2
occ-1-0-2-28 = (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-0-3)) , (P.S.source-leg , tt)))
origin-1-0-2-28 : P.T.origin tree-1-0-2 occ-1-0-2-28 ≡ input s03
origin-1-0-2-28 = refl
transport-1-0-2-28 : P.T.origin tree-0-1-3 (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-1-2)) , (P.S.source-leg , tt))) ≡ input (swap s03)
transport-1-0-2-28 = refl
occ-1-0-2-29 : P.T.Occurrence tree-1-0-2
occ-1-0-2-29 = (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-0-3)) , (P.S.target-leg , tt)))
origin-1-0-2-29 : P.T.origin tree-1-0-2 occ-1-0-2-29 ≡ input s03
origin-1-0-2-29 = refl
transport-1-0-2-29 : P.T.origin tree-0-1-3 (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-1-2)) , (P.S.target-leg , tt))) ≡ input (swap s03)
transport-1-0-2-29 = refl
occ-1-0-2-30 : P.T.Occurrence tree-1-0-2
occ-1-0-2-30 = (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.source-leg , tt)))
origin-1-0-2-30 : P.T.origin tree-1-0-2 occ-1-0-2-30 ≡ input s03
origin-1-0-2-30 = refl
transport-1-0-2-30 : P.T.origin tree-0-1-3 (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.source-leg , tt))) ≡ input (swap s03)
transport-1-0-2-30 = refl
occ-1-0-2-31 : P.T.Occurrence tree-1-0-2
occ-1-0-2-31 = (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.target-leg , tt)))
origin-1-0-2-31 : P.T.origin tree-1-0-2 occ-1-0-2-31 ≡ input s23
origin-1-0-2-31 = refl
transport-1-0-2-31 : P.T.origin tree-0-1-3 (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.target-leg , tt))) ≡ input (swap s23)
transport-1-0-2-31 = refl
occ-1-0-2-32 : P.T.Occurrence tree-1-0-2
occ-1-0-2-32 = (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.source-leg , tt)))
origin-1-0-2-32 : P.T.origin tree-1-0-2 occ-1-0-2-32 ≡ input s23
origin-1-0-2-32 = refl
transport-1-0-2-32 : P.T.origin tree-0-1-3 (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.source-leg , tt))) ≡ input (swap s23)
transport-1-0-2-32 = refl
occ-1-0-2-33 : P.T.Occurrence tree-1-0-2
occ-1-0-2-33 = (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.target-leg , tt)))
origin-1-0-2-33 : P.T.origin tree-1-0-2 occ-1-0-2-33 ≡ input s03
origin-1-0-2-33 = refl
transport-1-0-2-33 : P.T.origin tree-0-1-3 (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.target-leg , tt))) ≡ input (swap s03)
transport-1-0-2-33 = refl
occ-1-0-2-34 : P.T.Occurrence tree-1-0-2
occ-1-0-2-34 = (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-2-3)) , (P.S.source-leg , tt)))
origin-1-0-2-34 : P.T.origin tree-1-0-2 occ-1-0-2-34 ≡ input s23
origin-1-0-2-34 = refl
transport-1-0-2-34 : P.T.origin tree-0-1-3 (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-3-2)) , (P.S.source-leg , tt))) ≡ input (swap s23)
transport-1-0-2-34 = refl
occ-1-0-2-35 : P.T.Occurrence tree-1-0-2
occ-1-0-2-35 = (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-2-3)) , (P.S.target-leg , tt)))
origin-1-0-2-35 : P.T.origin tree-1-0-2 occ-1-0-2-35 ≡ input s23
origin-1-0-2-35 = refl
transport-1-0-2-35 : P.T.origin tree-0-1-3 (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-3-2)) , (P.S.target-leg , tt))) ≡ input (swap s23)
transport-1-0-2-35 = refl
occ-1-0-2-36 : P.T.Occurrence tree-1-0-2
occ-1-0-2-36 = (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-1-0-2-36 : P.T.origin tree-1-0-2 occ-1-0-2-36 ≡ input s10
origin-1-0-2-36 = refl
transport-1-0-2-36 : P.T.origin tree-0-1-3 (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s10)
transport-1-0-2-36 = refl
occ-1-0-2-37 : P.T.Occurrence tree-1-0-2
occ-1-0-2-37 = (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-1-0-2-37 : P.T.origin tree-1-0-2 occ-1-0-2-37 ≡ input s20
origin-1-0-2-37 = refl
transport-1-0-2-37 : P.T.origin tree-0-1-3 (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-1-0-2-37 = refl
occ-1-0-2-38 : P.T.Occurrence tree-1-0-2
occ-1-0-2-38 = (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-1-0-2-38 : P.T.origin tree-1-0-2 occ-1-0-2-38 ≡ input s30
origin-1-0-2-38 = refl
transport-1-0-2-38 : P.T.origin tree-0-1-3 (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s30)
transport-1-0-2-38 = refl
occ-1-0-2-39 : P.T.Occurrence tree-1-0-2
occ-1-0-2-39 = (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-1-0-2-39 : P.T.origin tree-1-0-2 occ-1-0-2-39 ≡ input s20
origin-1-0-2-39 = refl
transport-1-0-2-39 : P.T.origin tree-0-1-3 (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-1-0-2-39 = refl
occ-1-0-2-40 : P.T.Occurrence tree-1-0-2
occ-1-0-2-40 = (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.source-leg , tt)))
origin-1-0-2-40 : P.T.origin tree-1-0-2 occ-1-0-2-40 ≡ input s31
origin-1-0-2-40 = refl
transport-1-0-2-40 : P.T.origin tree-0-1-3 (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-1-0-2-40 = refl
occ-1-0-2-41 : P.T.Occurrence tree-1-0-2
occ-1-0-2-41 = (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.target-leg , tt)))
origin-1-0-2-41 : P.T.origin tree-1-0-2 occ-1-0-2-41 ≡ input s01
origin-1-0-2-41 = refl
transport-1-0-2-41 : P.T.origin tree-0-1-3 (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.target-leg , tt))) ≡ input (swap s01)
transport-1-0-2-41 = refl
occ-1-0-2-42 : P.T.Occurrence tree-1-0-2
occ-1-0-2-42 = (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.source-leg , tt)))
origin-1-0-2-42 : P.T.origin tree-1-0-2 occ-1-0-2-42 ≡ input s31
origin-1-0-2-42 = refl
transport-1-0-2-42 : P.T.origin tree-0-1-3 (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-1-0-2-42 = refl
occ-1-0-2-43 : P.T.Occurrence tree-1-0-2
occ-1-0-2-43 = (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.target-leg , tt)))
origin-1-0-2-43 : P.T.origin tree-1-0-2 occ-1-0-2-43 ≡ input s21
origin-1-0-2-43 = refl
transport-1-0-2-43 : P.T.origin tree-0-1-3 (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.target-leg , tt))) ≡ input (swap s21)
transport-1-0-2-43 = refl
occ-1-0-2-44 : P.T.Occurrence tree-1-0-2
occ-1-0-2-44 = (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-1-0-2-44 : P.T.origin tree-1-0-2 occ-1-0-2-44 ≡ input s12
origin-1-0-2-44 = refl
transport-1-0-2-44 : P.T.origin tree-0-1-3 (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s12)
transport-1-0-2-44 = refl
occ-1-0-2-45 : P.T.Occurrence tree-1-0-2
occ-1-0-2-45 = (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-1-0-2-45 : P.T.origin tree-1-0-2 occ-1-0-2-45 ≡ input s02
origin-1-0-2-45 = refl
transport-1-0-2-45 : P.T.origin tree-0-1-3 (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-1-0-2-45 = refl
occ-1-0-2-46 : P.T.Occurrence tree-1-0-2
occ-1-0-2-46 = (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-1-0-2-46 : P.T.origin tree-1-0-2 occ-1-0-2-46 ≡ input s32
origin-1-0-2-46 = refl
transport-1-0-2-46 : P.T.origin tree-0-1-3 (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s32)
transport-1-0-2-46 = refl
occ-1-0-2-47 : P.T.Occurrence tree-1-0-2
occ-1-0-2-47 = (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-1-0-2-47 : P.T.origin tree-1-0-2 occ-1-0-2-47 ≡ input s02
origin-1-0-2-47 = refl
transport-1-0-2-47 : P.T.origin tree-0-1-3 (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-1-0-2-47 = refl
occ-1-0-2-48 : P.T.Occurrence tree-1-0-2
occ-1-0-2-48 = (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.source-leg , tt)))
origin-1-0-2-48 : P.T.origin tree-1-0-2 occ-1-0-2-48 ≡ input s13
origin-1-0-2-48 = refl
transport-1-0-2-48 : P.T.origin tree-0-1-3 (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-1-0-2-48 = refl
occ-1-0-2-49 : P.T.Occurrence tree-1-0-2
occ-1-0-2-49 = (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.target-leg , tt)))
origin-1-0-2-49 : P.T.origin tree-1-0-2 occ-1-0-2-49 ≡ input s03
origin-1-0-2-49 = refl
transport-1-0-2-49 : P.T.origin tree-0-1-3 (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.target-leg , tt))) ≡ input (swap s03)
transport-1-0-2-49 = refl
occ-1-0-2-50 : P.T.Occurrence tree-1-0-2
occ-1-0-2-50 = (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.source-leg , tt)))
origin-1-0-2-50 : P.T.origin tree-1-0-2 occ-1-0-2-50 ≡ input s13
origin-1-0-2-50 = refl
transport-1-0-2-50 : P.T.origin tree-0-1-3 (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-1-0-2-50 = refl
occ-1-0-2-51 : P.T.Occurrence tree-1-0-2
occ-1-0-2-51 = (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.target-leg , tt)))
origin-1-0-2-51 : P.T.origin tree-1-0-2 occ-1-0-2-51 ≡ input s23
origin-1-0-2-51 = refl
transport-1-0-2-51 : P.T.origin tree-0-1-3 (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.target-leg , tt))) ≡ input (swap s23)
transport-1-0-2-51 = refl
occ-1-0-2-52 : P.T.Occurrence tree-1-0-2
occ-1-0-2-52 = (P.S.full-source , (P.S.first-port , tt))
origin-1-0-2-52 : P.T.origin tree-1-0-2 occ-1-0-2-52 ≡ input s13
origin-1-0-2-52 = refl
transport-1-0-2-52 : P.T.origin tree-0-1-3 (P.S.full-source , (P.S.first-port , tt)) ≡ input (swap s13)
transport-1-0-2-52 = refl
occ-1-0-2-53 : P.T.Occurrence tree-1-0-2
occ-1-0-2-53 = (P.S.full-source , (P.S.middle-port , tt))
origin-1-0-2-53 : P.T.origin tree-1-0-2 occ-1-0-2-53 ≡ input s03
origin-1-0-2-53 = refl
transport-1-0-2-53 : P.T.origin tree-0-1-3 (P.S.full-source , (P.S.middle-port , tt)) ≡ input (swap s03)
transport-1-0-2-53 = refl
occ-1-0-2-54 : P.T.Occurrence tree-1-0-2
occ-1-0-2-54 = (P.S.full-source , (P.S.final-port , tt))
origin-1-0-2-54 : P.T.origin tree-1-0-2 occ-1-0-2-54 ≡ input s23
origin-1-0-2-54 = refl
transport-1-0-2-54 : P.T.origin tree-0-1-3 (P.S.full-source , (P.S.final-port , tt)) ≡ input (swap s23)
transport-1-0-2-54 = refl
selected-source-1-0-2-AB : P.S.ab-index {a = C.q7} {b = C.q0} {c = C.q0} F.triple-1-0-2 ≡ (m1 , (F.vp-1-3 , F.vp-0-3))
selected-source-1-0-2-AB = refl
selected-target-1-0-2-AB : P.S.ab-index {a = C.q0} {b = C.q7} {c = C.q7} F.triple-0-1-3 ≡ (c1 , (F.vp-0-2 , F.vp-1-2))
selected-target-1-0-2-AB = refl
selected-source-1-0-2-BC : P.S.bc-index {a = C.q7} {b = C.q0} {c = C.q0} F.triple-1-0-2 ≡ (m1 , (F.vp-0-3 , F.vp-2-3))
selected-source-1-0-2-BC = refl
selected-target-1-0-2-BC : P.S.bc-index {a = C.q0} {b = C.q7} {c = C.q7} F.triple-0-1-3 ≡ (c1 , (F.vp-1-2 , F.vp-3-2))
selected-target-1-0-2-BC = refl
selected-source-1-0-2-AC : P.S.ac-index {a = C.q7} {b = C.q0} {c = C.q0} F.triple-1-0-2 ≡ (m1 , (F.vp-1-3 , F.vp-2-3))
selected-source-1-0-2-AC = refl
selected-target-1-0-2-AC : P.S.ac-index {a = C.q0} {b = C.q7} {c = C.q7} F.triple-0-1-3 ≡ (c1 , (F.vp-0-2 , F.vp-3-2))
selected-target-1-0-2-AC = refl
occ-1-0-3-0 : P.T.Occurrence tree-1-0-3
occ-1-0-3-0 = (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-1-0-3-0 : P.T.origin tree-1-0-3 occ-1-0-3-0 ≡ input s10
origin-1-0-3-0 = refl
transport-1-0-3-0 : P.T.origin tree-0-1-2 (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s10)
transport-1-0-3-0 = refl
occ-1-0-3-1 : P.T.Occurrence tree-1-0-3
occ-1-0-3-1 = (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-1-0-3-1 : P.T.origin tree-1-0-3 occ-1-0-3-1 ≡ input s20
origin-1-0-3-1 = refl
transport-1-0-3-1 : P.T.origin tree-0-1-2 (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-1-0-3-1 = refl
occ-1-0-3-2 : P.T.Occurrence tree-1-0-3
occ-1-0-3-2 = (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-1-0-3-2 : P.T.origin tree-1-0-3 occ-1-0-3-2 ≡ input s30
origin-1-0-3-2 = refl
transport-1-0-3-2 : P.T.origin tree-0-1-2 (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s30)
transport-1-0-3-2 = refl
occ-1-0-3-3 : P.T.Occurrence tree-1-0-3
occ-1-0-3-3 = (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-1-0-3-3 : P.T.origin tree-1-0-3 occ-1-0-3-3 ≡ input s20
origin-1-0-3-3 = refl
transport-1-0-3-3 : P.T.origin tree-0-1-2 (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-1-0-3-3 = refl
occ-1-0-3-4 : P.T.Occurrence tree-1-0-3
occ-1-0-3-4 = (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.source-leg , tt)))
origin-1-0-3-4 : P.T.origin tree-1-0-3 occ-1-0-3-4 ≡ input s31
origin-1-0-3-4 = refl
transport-1-0-3-4 : P.T.origin tree-0-1-2 (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-1-0-3-4 = refl
occ-1-0-3-5 : P.T.Occurrence tree-1-0-3
occ-1-0-3-5 = (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.target-leg , tt)))
origin-1-0-3-5 : P.T.origin tree-1-0-3 occ-1-0-3-5 ≡ input s01
origin-1-0-3-5 = refl
transport-1-0-3-5 : P.T.origin tree-0-1-2 (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.target-leg , tt))) ≡ input (swap s01)
transport-1-0-3-5 = refl
occ-1-0-3-6 : P.T.Occurrence tree-1-0-3
occ-1-0-3-6 = (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.source-leg , tt)))
origin-1-0-3-6 : P.T.origin tree-1-0-3 occ-1-0-3-6 ≡ input s31
origin-1-0-3-6 = refl
transport-1-0-3-6 : P.T.origin tree-0-1-2 (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-1-0-3-6 = refl
occ-1-0-3-7 : P.T.Occurrence tree-1-0-3
occ-1-0-3-7 = (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.target-leg , tt)))
origin-1-0-3-7 : P.T.origin tree-1-0-3 occ-1-0-3-7 ≡ input s21
origin-1-0-3-7 = refl
transport-1-0-3-7 : P.T.origin tree-0-1-2 (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.target-leg , tt))) ≡ input (swap s21)
transport-1-0-3-7 = refl
occ-1-0-3-8 : P.T.Occurrence tree-1-0-3
occ-1-0-3-8 = (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-1-0-3-8 : P.T.origin tree-1-0-3 occ-1-0-3-8 ≡ input s12
origin-1-0-3-8 = refl
transport-1-0-3-8 : P.T.origin tree-0-1-2 (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s12)
transport-1-0-3-8 = refl
occ-1-0-3-9 : P.T.Occurrence tree-1-0-3
occ-1-0-3-9 = (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-1-0-3-9 : P.T.origin tree-1-0-3 occ-1-0-3-9 ≡ input s02
origin-1-0-3-9 = refl
transport-1-0-3-9 : P.T.origin tree-0-1-2 (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-1-0-3-9 = refl
occ-1-0-3-10 : P.T.Occurrence tree-1-0-3
occ-1-0-3-10 = (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-1-0-3-10 : P.T.origin tree-1-0-3 occ-1-0-3-10 ≡ input s32
origin-1-0-3-10 = refl
transport-1-0-3-10 : P.T.origin tree-0-1-2 (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s32)
transport-1-0-3-10 = refl
occ-1-0-3-11 : P.T.Occurrence tree-1-0-3
occ-1-0-3-11 = (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-1-0-3-11 : P.T.origin tree-1-0-3 occ-1-0-3-11 ≡ input s02
origin-1-0-3-11 = refl
transport-1-0-3-11 : P.T.origin tree-0-1-2 (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-1-0-3-11 = refl
occ-1-0-3-12 : P.T.Occurrence tree-1-0-3
occ-1-0-3-12 = (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.source-leg , tt)))
origin-1-0-3-12 : P.T.origin tree-1-0-3 occ-1-0-3-12 ≡ input s13
origin-1-0-3-12 = refl
transport-1-0-3-12 : P.T.origin tree-0-1-2 (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-1-0-3-12 = refl
occ-1-0-3-13 : P.T.Occurrence tree-1-0-3
occ-1-0-3-13 = (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.target-leg , tt)))
origin-1-0-3-13 : P.T.origin tree-1-0-3 occ-1-0-3-13 ≡ input s03
origin-1-0-3-13 = refl
transport-1-0-3-13 : P.T.origin tree-0-1-2 (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.target-leg , tt))) ≡ input (swap s03)
transport-1-0-3-13 = refl
occ-1-0-3-14 : P.T.Occurrence tree-1-0-3
occ-1-0-3-14 = (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.source-leg , tt)))
origin-1-0-3-14 : P.T.origin tree-1-0-3 occ-1-0-3-14 ≡ input s13
origin-1-0-3-14 = refl
transport-1-0-3-14 : P.T.origin tree-0-1-2 (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-1-0-3-14 = refl
occ-1-0-3-15 : P.T.Occurrence tree-1-0-3
occ-1-0-3-15 = (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.target-leg , tt)))
origin-1-0-3-15 : P.T.origin tree-1-0-3 occ-1-0-3-15 ≡ input s23
origin-1-0-3-15 = refl
transport-1-0-3-15 : P.T.origin tree-0-1-2 (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.target-leg , tt))) ≡ input (swap s23)
transport-1-0-3-15 = refl
occ-1-0-3-16 : P.T.Occurrence tree-1-0-3
occ-1-0-3-16 = (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.source-leg , tt)))
origin-1-0-3-16 : P.T.origin tree-1-0-3 occ-1-0-3-16 ≡ input s20
origin-1-0-3-16 = refl
transport-1-0-3-16 : P.T.origin tree-0-1-2 (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-1-0-3-16 = refl
occ-1-0-3-17 : P.T.Occurrence tree-1-0-3
occ-1-0-3-17 = (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.target-leg , tt)))
origin-1-0-3-17 : P.T.origin tree-1-0-3 occ-1-0-3-17 ≡ input s10
origin-1-0-3-17 = refl
transport-1-0-3-17 : P.T.origin tree-0-1-2 (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.target-leg , tt))) ≡ input (swap s10)
transport-1-0-3-17 = refl
occ-1-0-3-18 : P.T.Occurrence tree-1-0-3
occ-1-0-3-18 = (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.source-leg , tt)))
origin-1-0-3-18 : P.T.origin tree-1-0-3 occ-1-0-3-18 ≡ input s20
origin-1-0-3-18 = refl
transport-1-0-3-18 : P.T.origin tree-0-1-2 (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-1-0-3-18 = refl
occ-1-0-3-19 : P.T.Occurrence tree-1-0-3
occ-1-0-3-19 = (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.target-leg , tt)))
origin-1-0-3-19 : P.T.origin tree-1-0-3 occ-1-0-3-19 ≡ input s30
origin-1-0-3-19 = refl
transport-1-0-3-19 : P.T.origin tree-0-1-2 (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.target-leg , tt))) ≡ input (swap s30)
transport-1-0-3-19 = refl
occ-1-0-3-20 : P.T.Occurrence tree-1-0-3
occ-1-0-3-20 = (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-1-0-3-20 : P.T.origin tree-1-0-3 occ-1-0-3-20 ≡ input s01
origin-1-0-3-20 = refl
transport-1-0-3-20 : P.T.origin tree-0-1-2 (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s01)
transport-1-0-3-20 = refl
occ-1-0-3-21 : P.T.Occurrence tree-1-0-3
occ-1-0-3-21 = (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-1-0-3-21 : P.T.origin tree-1-0-3 occ-1-0-3-21 ≡ input s31
origin-1-0-3-21 = refl
transport-1-0-3-21 : P.T.origin tree-0-1-2 (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-1-0-3-21 = refl
occ-1-0-3-22 : P.T.Occurrence tree-1-0-3
occ-1-0-3-22 = (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-1-0-3-22 : P.T.origin tree-1-0-3 occ-1-0-3-22 ≡ input s21
origin-1-0-3-22 = refl
transport-1-0-3-22 : P.T.origin tree-0-1-2 (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s21)
transport-1-0-3-22 = refl
occ-1-0-3-23 : P.T.Occurrence tree-1-0-3
occ-1-0-3-23 = (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-1-0-3-23 : P.T.origin tree-1-0-3 occ-1-0-3-23 ≡ input s31
origin-1-0-3-23 = refl
transport-1-0-3-23 : P.T.origin tree-0-1-2 (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-1-0-3-23 = refl
occ-1-0-3-24 : P.T.Occurrence tree-1-0-3
occ-1-0-3-24 = (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.source-leg , tt)))
origin-1-0-3-24 : P.T.origin tree-1-0-3 occ-1-0-3-24 ≡ input s02
origin-1-0-3-24 = refl
transport-1-0-3-24 : P.T.origin tree-0-1-2 (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-1-0-3-24 = refl
occ-1-0-3-25 : P.T.Occurrence tree-1-0-3
occ-1-0-3-25 = (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.target-leg , tt)))
origin-1-0-3-25 : P.T.origin tree-1-0-3 occ-1-0-3-25 ≡ input s12
origin-1-0-3-25 = refl
transport-1-0-3-25 : P.T.origin tree-0-1-2 (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.target-leg , tt))) ≡ input (swap s12)
transport-1-0-3-25 = refl
occ-1-0-3-26 : P.T.Occurrence tree-1-0-3
occ-1-0-3-26 = (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.source-leg , tt)))
origin-1-0-3-26 : P.T.origin tree-1-0-3 occ-1-0-3-26 ≡ input s02
origin-1-0-3-26 = refl
transport-1-0-3-26 : P.T.origin tree-0-1-2 (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-1-0-3-26 = refl
occ-1-0-3-27 : P.T.Occurrence tree-1-0-3
occ-1-0-3-27 = (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.target-leg , tt)))
origin-1-0-3-27 : P.T.origin tree-1-0-3 occ-1-0-3-27 ≡ input s32
origin-1-0-3-27 = refl
transport-1-0-3-27 : P.T.origin tree-0-1-2 (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.target-leg , tt))) ≡ input (swap s32)
transport-1-0-3-27 = refl
occ-1-0-3-28 : P.T.Occurrence tree-1-0-3
occ-1-0-3-28 = (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-1-0-3-28 : P.T.origin tree-1-0-3 occ-1-0-3-28 ≡ input s03
origin-1-0-3-28 = refl
transport-1-0-3-28 : P.T.origin tree-0-1-2 (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s03)
transport-1-0-3-28 = refl
occ-1-0-3-29 : P.T.Occurrence tree-1-0-3
occ-1-0-3-29 = (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-1-0-3-29 : P.T.origin tree-1-0-3 occ-1-0-3-29 ≡ input s13
origin-1-0-3-29 = refl
transport-1-0-3-29 : P.T.origin tree-0-1-2 (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-1-0-3-29 = refl
occ-1-0-3-30 : P.T.Occurrence tree-1-0-3
occ-1-0-3-30 = (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-1-0-3-30 : P.T.origin tree-1-0-3 occ-1-0-3-30 ≡ input s23
origin-1-0-3-30 = refl
transport-1-0-3-30 : P.T.origin tree-0-1-2 (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s23)
transport-1-0-3-30 = refl
occ-1-0-3-31 : P.T.Occurrence tree-1-0-3
occ-1-0-3-31 = (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-1-0-3-31 : P.T.origin tree-1-0-3 occ-1-0-3-31 ≡ input s13
origin-1-0-3-31 = refl
transport-1-0-3-31 : P.T.origin tree-0-1-2 (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-1-0-3-31 = refl
occ-1-0-3-32 : P.T.Occurrence tree-1-0-3
occ-1-0-3-32 = (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-1-0)) , (P.S.source-leg , tt)))
origin-1-0-3-32 : P.T.origin tree-1-0-3 occ-1-0-3-32 ≡ input s10
origin-1-0-3-32 = refl
transport-1-0-3-32 : P.T.origin tree-0-1-2 (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-0-1)) , (P.S.source-leg , tt))) ≡ input (swap s10)
transport-1-0-3-32 = refl
occ-1-0-3-33 : P.T.Occurrence tree-1-0-3
occ-1-0-3-33 = (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-1-0)) , (P.S.target-leg , tt)))
origin-1-0-3-33 : P.T.origin tree-1-0-3 occ-1-0-3-33 ≡ input s10
origin-1-0-3-33 = refl
transport-1-0-3-33 : P.T.origin tree-0-1-2 (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-0-1)) , (P.S.target-leg , tt))) ≡ input (swap s10)
transport-1-0-3-33 = refl
occ-1-0-3-34 : P.T.Occurrence tree-1-0-3
occ-1-0-3-34 = (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.source-leg , tt)))
origin-1-0-3-34 : P.T.origin tree-1-0-3 occ-1-0-3-34 ≡ input s10
origin-1-0-3-34 = refl
transport-1-0-3-34 : P.T.origin tree-0-1-2 (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.source-leg , tt))) ≡ input (swap s10)
transport-1-0-3-34 = refl
occ-1-0-3-35 : P.T.Occurrence tree-1-0-3
occ-1-0-3-35 = (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.target-leg , tt)))
origin-1-0-3-35 : P.T.origin tree-1-0-3 occ-1-0-3-35 ≡ input s30
origin-1-0-3-35 = refl
transport-1-0-3-35 : P.T.origin tree-0-1-2 (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.target-leg , tt))) ≡ input (swap s30)
transport-1-0-3-35 = refl
occ-1-0-3-36 : P.T.Occurrence tree-1-0-3
occ-1-0-3-36 = (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.source-leg , tt)))
origin-1-0-3-36 : P.T.origin tree-1-0-3 occ-1-0-3-36 ≡ input s30
origin-1-0-3-36 = refl
transport-1-0-3-36 : P.T.origin tree-0-1-2 (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.source-leg , tt))) ≡ input (swap s30)
transport-1-0-3-36 = refl
occ-1-0-3-37 : P.T.Occurrence tree-1-0-3
occ-1-0-3-37 = (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.target-leg , tt)))
origin-1-0-3-37 : P.T.origin tree-1-0-3 occ-1-0-3-37 ≡ input s10
origin-1-0-3-37 = refl
transport-1-0-3-37 : P.T.origin tree-0-1-2 (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.target-leg , tt))) ≡ input (swap s10)
transport-1-0-3-37 = refl
occ-1-0-3-38 : P.T.Occurrence tree-1-0-3
occ-1-0-3-38 = (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-3-0)) , (P.S.source-leg , tt)))
origin-1-0-3-38 : P.T.origin tree-1-0-3 occ-1-0-3-38 ≡ input s30
origin-1-0-3-38 = refl
transport-1-0-3-38 : P.T.origin tree-0-1-2 (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-2-1)) , (P.S.source-leg , tt))) ≡ input (swap s30)
transport-1-0-3-38 = refl
occ-1-0-3-39 : P.T.Occurrence tree-1-0-3
occ-1-0-3-39 = (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-3-0)) , (P.S.target-leg , tt)))
origin-1-0-3-39 : P.T.origin tree-1-0-3 occ-1-0-3-39 ≡ input s30
origin-1-0-3-39 = refl
transport-1-0-3-39 : P.T.origin tree-0-1-2 (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-2-1)) , (P.S.target-leg , tt))) ≡ input (swap s30)
transport-1-0-3-39 = refl
occ-1-0-3-40 : P.T.Occurrence tree-1-0-3
occ-1-0-3-40 = (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-1-0-3-40 : P.T.origin tree-1-0-3 occ-1-0-3-40 ≡ input s31
origin-1-0-3-40 = refl
transport-1-0-3-40 : P.T.origin tree-0-1-2 (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-1-0-3-40 = refl
occ-1-0-3-41 : P.T.Occurrence tree-1-0-3
occ-1-0-3-41 = (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-1-0-3-41 : P.T.origin tree-1-0-3 occ-1-0-3-41 ≡ input s31
origin-1-0-3-41 = refl
transport-1-0-3-41 : P.T.origin tree-0-1-2 (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-1-0-3-41 = refl
occ-1-0-3-42 : P.T.Occurrence tree-1-0-3
occ-1-0-3-42 = (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-1-2)) , (P.S.source-leg , tt)))
origin-1-0-3-42 : P.T.origin tree-1-0-3 occ-1-0-3-42 ≡ input s12
origin-1-0-3-42 = refl
transport-1-0-3-42 : P.T.origin tree-0-1-2 (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-0-3)) , (P.S.source-leg , tt))) ≡ input (swap s12)
transport-1-0-3-42 = refl
occ-1-0-3-43 : P.T.Occurrence tree-1-0-3
occ-1-0-3-43 = (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-1-2)) , (P.S.target-leg , tt)))
origin-1-0-3-43 : P.T.origin tree-1-0-3 occ-1-0-3-43 ≡ input s12
origin-1-0-3-43 = refl
transport-1-0-3-43 : P.T.origin tree-0-1-2 (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-0-3)) , (P.S.target-leg , tt))) ≡ input (swap s12)
transport-1-0-3-43 = refl
occ-1-0-3-44 : P.T.Occurrence tree-1-0-3
occ-1-0-3-44 = (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.source-leg , tt)))
origin-1-0-3-44 : P.T.origin tree-1-0-3 occ-1-0-3-44 ≡ input s12
origin-1-0-3-44 = refl
transport-1-0-3-44 : P.T.origin tree-0-1-2 (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.source-leg , tt))) ≡ input (swap s12)
transport-1-0-3-44 = refl
occ-1-0-3-45 : P.T.Occurrence tree-1-0-3
occ-1-0-3-45 = (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.target-leg , tt)))
origin-1-0-3-45 : P.T.origin tree-1-0-3 occ-1-0-3-45 ≡ input s32
origin-1-0-3-45 = refl
transport-1-0-3-45 : P.T.origin tree-0-1-2 (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.target-leg , tt))) ≡ input (swap s32)
transport-1-0-3-45 = refl
occ-1-0-3-46 : P.T.Occurrence tree-1-0-3
occ-1-0-3-46 = (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.source-leg , tt)))
origin-1-0-3-46 : P.T.origin tree-1-0-3 occ-1-0-3-46 ≡ input s32
origin-1-0-3-46 = refl
transport-1-0-3-46 : P.T.origin tree-0-1-2 (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.source-leg , tt))) ≡ input (swap s32)
transport-1-0-3-46 = refl
occ-1-0-3-47 : P.T.Occurrence tree-1-0-3
occ-1-0-3-47 = (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.target-leg , tt)))
origin-1-0-3-47 : P.T.origin tree-1-0-3 occ-1-0-3-47 ≡ input s12
origin-1-0-3-47 = refl
transport-1-0-3-47 : P.T.origin tree-0-1-2 (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.target-leg , tt))) ≡ input (swap s12)
transport-1-0-3-47 = refl
occ-1-0-3-48 : P.T.Occurrence tree-1-0-3
occ-1-0-3-48 = (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-3-2)) , (P.S.source-leg , tt)))
origin-1-0-3-48 : P.T.origin tree-1-0-3 occ-1-0-3-48 ≡ input s32
origin-1-0-3-48 = refl
transport-1-0-3-48 : P.T.origin tree-0-1-2 (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-2-3)) , (P.S.source-leg , tt))) ≡ input (swap s32)
transport-1-0-3-48 = refl
occ-1-0-3-49 : P.T.Occurrence tree-1-0-3
occ-1-0-3-49 = (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-3-2)) , (P.S.target-leg , tt)))
origin-1-0-3-49 : P.T.origin tree-1-0-3 occ-1-0-3-49 ≡ input s32
origin-1-0-3-49 = refl
transport-1-0-3-49 : P.T.origin tree-0-1-2 (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-2-3)) , (P.S.target-leg , tt))) ≡ input (swap s32)
transport-1-0-3-49 = refl
occ-1-0-3-50 : P.T.Occurrence tree-1-0-3
occ-1-0-3-50 = (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-1-0-3-50 : P.T.origin tree-1-0-3 occ-1-0-3-50 ≡ input s13
origin-1-0-3-50 = refl
transport-1-0-3-50 : P.T.origin tree-0-1-2 (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-1-0-3-50 = refl
occ-1-0-3-51 : P.T.Occurrence tree-1-0-3
occ-1-0-3-51 = (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-1-0-3-51 : P.T.origin tree-1-0-3 occ-1-0-3-51 ≡ input s13
origin-1-0-3-51 = refl
transport-1-0-3-51 : P.T.origin tree-0-1-2 (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-1-0-3-51 = refl
occ-1-0-3-52 : P.T.Occurrence tree-1-0-3
occ-1-0-3-52 = (P.S.full-source , (P.S.first-port , tt))
origin-1-0-3-52 : P.T.origin tree-1-0-3 occ-1-0-3-52 ≡ input s12
origin-1-0-3-52 = refl
transport-1-0-3-52 : P.T.origin tree-0-1-2 (P.S.full-source , (P.S.first-port , tt)) ≡ input (swap s12)
transport-1-0-3-52 = refl
occ-1-0-3-53 : P.T.Occurrence tree-1-0-3
occ-1-0-3-53 = (P.S.full-source , (P.S.middle-port , tt))
origin-1-0-3-53 : P.T.origin tree-1-0-3 occ-1-0-3-53 ≡ input s02
origin-1-0-3-53 = refl
transport-1-0-3-53 : P.T.origin tree-0-1-2 (P.S.full-source , (P.S.middle-port , tt)) ≡ input (swap s02)
transport-1-0-3-53 = refl
occ-1-0-3-54 : P.T.Occurrence tree-1-0-3
occ-1-0-3-54 = (P.S.full-source , (P.S.final-port , tt))
origin-1-0-3-54 : P.T.origin tree-1-0-3 occ-1-0-3-54 ≡ input s32
origin-1-0-3-54 = refl
transport-1-0-3-54 : P.T.origin tree-0-1-2 (P.S.full-source , (P.S.final-port , tt)) ≡ input (swap s32)
transport-1-0-3-54 = refl
selected-source-1-0-3-AB : P.S.ab-index {a = C.q7} {b = C.q0} {c = C.q7} F.triple-1-0-3 ≡ (c1 , (F.vp-1-2 , F.vp-0-2))
selected-source-1-0-3-AB = refl
selected-target-1-0-3-AB : P.S.ab-index {a = C.q0} {b = C.q7} {c = C.q0} F.triple-0-1-2 ≡ (m1 , (F.vp-0-3 , F.vp-1-3))
selected-target-1-0-3-AB = refl
selected-source-1-0-3-BC : P.S.bc-index {a = C.q7} {b = C.q0} {c = C.q7} F.triple-1-0-3 ≡ (c1 , (F.vp-0-2 , F.vp-3-2))
selected-source-1-0-3-BC = refl
selected-target-1-0-3-BC : P.S.bc-index {a = C.q0} {b = C.q7} {c = C.q0} F.triple-0-1-2 ≡ (m1 , (F.vp-1-3 , F.vp-2-3))
selected-target-1-0-3-BC = refl
selected-source-1-0-3-AC : P.S.ac-index {a = C.q7} {b = C.q0} {c = C.q7} F.triple-1-0-3 ≡ (c1 , (F.vp-1-2 , F.vp-3-2))
selected-source-1-0-3-AC = refl
selected-target-1-0-3-AC : P.S.ac-index {a = C.q0} {b = C.q7} {c = C.q0} F.triple-0-1-2 ≡ (m1 , (F.vp-0-3 , F.vp-2-3))
selected-target-1-0-3-AC = refl
occ-1-2-0-0 : P.T.Occurrence tree-1-2-0
occ-1-2-0-0 = (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-1-2-0-0 : P.T.origin tree-1-2-0 occ-1-2-0-0 ≡ input s10
origin-1-2-0-0 = refl
transport-1-2-0-0 : P.T.origin tree-0-3-1 (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s10)
transport-1-2-0-0 = refl
occ-1-2-0-1 : P.T.Occurrence tree-1-2-0
occ-1-2-0-1 = (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-1-2-0-1 : P.T.origin tree-1-2-0 occ-1-2-0-1 ≡ input s20
origin-1-2-0-1 = refl
transport-1-2-0-1 : P.T.origin tree-0-3-1 (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-1-2-0-1 = refl
occ-1-2-0-2 : P.T.Occurrence tree-1-2-0
occ-1-2-0-2 = (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-1-2-0-2 : P.T.origin tree-1-2-0 occ-1-2-0-2 ≡ input s30
origin-1-2-0-2 = refl
transport-1-2-0-2 : P.T.origin tree-0-3-1 (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s30)
transport-1-2-0-2 = refl
occ-1-2-0-3 : P.T.Occurrence tree-1-2-0
occ-1-2-0-3 = (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-1-2-0-3 : P.T.origin tree-1-2-0 occ-1-2-0-3 ≡ input s20
origin-1-2-0-3 = refl
transport-1-2-0-3 : P.T.origin tree-0-3-1 (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-1-2-0-3 = refl
occ-1-2-0-4 : P.T.Occurrence tree-1-2-0
occ-1-2-0-4 = (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.source-leg , tt)))
origin-1-2-0-4 : P.T.origin tree-1-2-0 occ-1-2-0-4 ≡ input s31
origin-1-2-0-4 = refl
transport-1-2-0-4 : P.T.origin tree-0-3-1 (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-1-2-0-4 = refl
occ-1-2-0-5 : P.T.Occurrence tree-1-2-0
occ-1-2-0-5 = (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.target-leg , tt)))
origin-1-2-0-5 : P.T.origin tree-1-2-0 occ-1-2-0-5 ≡ input s01
origin-1-2-0-5 = refl
transport-1-2-0-5 : P.T.origin tree-0-3-1 (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.target-leg , tt))) ≡ input (swap s01)
transport-1-2-0-5 = refl
occ-1-2-0-6 : P.T.Occurrence tree-1-2-0
occ-1-2-0-6 = (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.source-leg , tt)))
origin-1-2-0-6 : P.T.origin tree-1-2-0 occ-1-2-0-6 ≡ input s31
origin-1-2-0-6 = refl
transport-1-2-0-6 : P.T.origin tree-0-3-1 (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-1-2-0-6 = refl
occ-1-2-0-7 : P.T.Occurrence tree-1-2-0
occ-1-2-0-7 = (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.target-leg , tt)))
origin-1-2-0-7 : P.T.origin tree-1-2-0 occ-1-2-0-7 ≡ input s21
origin-1-2-0-7 = refl
transport-1-2-0-7 : P.T.origin tree-0-3-1 (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.target-leg , tt))) ≡ input (swap s21)
transport-1-2-0-7 = refl
occ-1-2-0-8 : P.T.Occurrence tree-1-2-0
occ-1-2-0-8 = (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-1-2-0-8 : P.T.origin tree-1-2-0 occ-1-2-0-8 ≡ input s12
origin-1-2-0-8 = refl
transport-1-2-0-8 : P.T.origin tree-0-3-1 (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s12)
transport-1-2-0-8 = refl
occ-1-2-0-9 : P.T.Occurrence tree-1-2-0
occ-1-2-0-9 = (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-1-2-0-9 : P.T.origin tree-1-2-0 occ-1-2-0-9 ≡ input s02
origin-1-2-0-9 = refl
transport-1-2-0-9 : P.T.origin tree-0-3-1 (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-1-2-0-9 = refl
occ-1-2-0-10 : P.T.Occurrence tree-1-2-0
occ-1-2-0-10 = (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-1-2-0-10 : P.T.origin tree-1-2-0 occ-1-2-0-10 ≡ input s32
origin-1-2-0-10 = refl
transport-1-2-0-10 : P.T.origin tree-0-3-1 (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s32)
transport-1-2-0-10 = refl
occ-1-2-0-11 : P.T.Occurrence tree-1-2-0
occ-1-2-0-11 = (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-1-2-0-11 : P.T.origin tree-1-2-0 occ-1-2-0-11 ≡ input s02
origin-1-2-0-11 = refl
transport-1-2-0-11 : P.T.origin tree-0-3-1 (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-1-2-0-11 = refl
occ-1-2-0-12 : P.T.Occurrence tree-1-2-0
occ-1-2-0-12 = (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.source-leg , tt)))
origin-1-2-0-12 : P.T.origin tree-1-2-0 occ-1-2-0-12 ≡ input s13
origin-1-2-0-12 = refl
transport-1-2-0-12 : P.T.origin tree-0-3-1 (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-1-2-0-12 = refl
occ-1-2-0-13 : P.T.Occurrence tree-1-2-0
occ-1-2-0-13 = (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.target-leg , tt)))
origin-1-2-0-13 : P.T.origin tree-1-2-0 occ-1-2-0-13 ≡ input s03
origin-1-2-0-13 = refl
transport-1-2-0-13 : P.T.origin tree-0-3-1 (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.target-leg , tt))) ≡ input (swap s03)
transport-1-2-0-13 = refl
occ-1-2-0-14 : P.T.Occurrence tree-1-2-0
occ-1-2-0-14 = (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.source-leg , tt)))
origin-1-2-0-14 : P.T.origin tree-1-2-0 occ-1-2-0-14 ≡ input s13
origin-1-2-0-14 = refl
transport-1-2-0-14 : P.T.origin tree-0-3-1 (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-1-2-0-14 = refl
occ-1-2-0-15 : P.T.Occurrence tree-1-2-0
occ-1-2-0-15 = (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.target-leg , tt)))
origin-1-2-0-15 : P.T.origin tree-1-2-0 occ-1-2-0-15 ≡ input s23
origin-1-2-0-15 = refl
transport-1-2-0-15 : P.T.origin tree-0-3-1 (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.target-leg , tt))) ≡ input (swap s23)
transport-1-2-0-15 = refl
occ-1-2-0-16 : P.T.Occurrence tree-1-2-0
occ-1-2-0-16 = (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-1-2-0-16 : P.T.origin tree-1-2-0 occ-1-2-0-16 ≡ input s20
origin-1-2-0-16 = refl
transport-1-2-0-16 : P.T.origin tree-0-3-1 (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-1-2-0-16 = refl
occ-1-2-0-17 : P.T.Occurrence tree-1-2-0
occ-1-2-0-17 = (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-1-2-0-17 : P.T.origin tree-1-2-0 occ-1-2-0-17 ≡ input s20
origin-1-2-0-17 = refl
transport-1-2-0-17 : P.T.origin tree-0-3-1 (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-1-2-0-17 = refl
occ-1-2-0-18 : P.T.Occurrence tree-1-2-0
occ-1-2-0-18 = (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-0-1)) , (P.S.source-leg , tt)))
origin-1-2-0-18 : P.T.origin tree-1-2-0 occ-1-2-0-18 ≡ input s01
origin-1-2-0-18 = refl
transport-1-2-0-18 : P.T.origin tree-0-3-1 (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-1-0)) , (P.S.source-leg , tt))) ≡ input (swap s01)
transport-1-2-0-18 = refl
occ-1-2-0-19 : P.T.Occurrence tree-1-2-0
occ-1-2-0-19 = (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-0-1)) , (P.S.target-leg , tt)))
origin-1-2-0-19 : P.T.origin tree-1-2-0 occ-1-2-0-19 ≡ input s01
origin-1-2-0-19 = refl
transport-1-2-0-19 : P.T.origin tree-0-3-1 (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-1-0)) , (P.S.target-leg , tt))) ≡ input (swap s01)
transport-1-2-0-19 = refl
occ-1-2-0-20 : P.T.Occurrence tree-1-2-0
occ-1-2-0-20 = (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.source-leg , tt)))
origin-1-2-0-20 : P.T.origin tree-1-2-0 occ-1-2-0-20 ≡ input s01
origin-1-2-0-20 = refl
transport-1-2-0-20 : P.T.origin tree-0-3-1 (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.source-leg , tt))) ≡ input (swap s01)
transport-1-2-0-20 = refl
occ-1-2-0-21 : P.T.Occurrence tree-1-2-0
occ-1-2-0-21 = (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.target-leg , tt)))
origin-1-2-0-21 : P.T.origin tree-1-2-0 occ-1-2-0-21 ≡ input s21
origin-1-2-0-21 = refl
transport-1-2-0-21 : P.T.origin tree-0-3-1 (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.target-leg , tt))) ≡ input (swap s21)
transport-1-2-0-21 = refl
occ-1-2-0-22 : P.T.Occurrence tree-1-2-0
occ-1-2-0-22 = (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.source-leg , tt)))
origin-1-2-0-22 : P.T.origin tree-1-2-0 occ-1-2-0-22 ≡ input s21
origin-1-2-0-22 = refl
transport-1-2-0-22 : P.T.origin tree-0-3-1 (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.source-leg , tt))) ≡ input (swap s21)
transport-1-2-0-22 = refl
occ-1-2-0-23 : P.T.Occurrence tree-1-2-0
occ-1-2-0-23 = (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.target-leg , tt)))
origin-1-2-0-23 : P.T.origin tree-1-2-0 occ-1-2-0-23 ≡ input s01
origin-1-2-0-23 = refl
transport-1-2-0-23 : P.T.origin tree-0-3-1 (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.target-leg , tt))) ≡ input (swap s01)
transport-1-2-0-23 = refl
occ-1-2-0-24 : P.T.Occurrence tree-1-2-0
occ-1-2-0-24 = (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-2-1)) , (P.S.source-leg , tt)))
origin-1-2-0-24 : P.T.origin tree-1-2-0 occ-1-2-0-24 ≡ input s21
origin-1-2-0-24 = refl
transport-1-2-0-24 : P.T.origin tree-0-3-1 (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-3-0)) , (P.S.source-leg , tt))) ≡ input (swap s21)
transport-1-2-0-24 = refl
occ-1-2-0-25 : P.T.Occurrence tree-1-2-0
occ-1-2-0-25 = (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-2-1)) , (P.S.target-leg , tt)))
origin-1-2-0-25 : P.T.origin tree-1-2-0 occ-1-2-0-25 ≡ input s21
origin-1-2-0-25 = refl
transport-1-2-0-25 : P.T.origin tree-0-3-1 (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-3-0)) , (P.S.target-leg , tt))) ≡ input (swap s21)
transport-1-2-0-25 = refl
occ-1-2-0-26 : P.T.Occurrence tree-1-2-0
occ-1-2-0-26 = (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-1-2-0-26 : P.T.origin tree-1-2-0 occ-1-2-0-26 ≡ input s02
origin-1-2-0-26 = refl
transport-1-2-0-26 : P.T.origin tree-0-3-1 (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-1-2-0-26 = refl
occ-1-2-0-27 : P.T.Occurrence tree-1-2-0
occ-1-2-0-27 = (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-1-2-0-27 : P.T.origin tree-1-2-0 occ-1-2-0-27 ≡ input s02
origin-1-2-0-27 = refl
transport-1-2-0-27 : P.T.origin tree-0-3-1 (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-1-2-0-27 = refl
occ-1-2-0-28 : P.T.Occurrence tree-1-2-0
occ-1-2-0-28 = (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-0-3)) , (P.S.source-leg , tt)))
origin-1-2-0-28 : P.T.origin tree-1-2-0 occ-1-2-0-28 ≡ input s03
origin-1-2-0-28 = refl
transport-1-2-0-28 : P.T.origin tree-0-3-1 (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-1-2)) , (P.S.source-leg , tt))) ≡ input (swap s03)
transport-1-2-0-28 = refl
occ-1-2-0-29 : P.T.Occurrence tree-1-2-0
occ-1-2-0-29 = (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-0-3)) , (P.S.target-leg , tt)))
origin-1-2-0-29 : P.T.origin tree-1-2-0 occ-1-2-0-29 ≡ input s03
origin-1-2-0-29 = refl
transport-1-2-0-29 : P.T.origin tree-0-3-1 (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-1-2)) , (P.S.target-leg , tt))) ≡ input (swap s03)
transport-1-2-0-29 = refl
occ-1-2-0-30 : P.T.Occurrence tree-1-2-0
occ-1-2-0-30 = (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.source-leg , tt)))
origin-1-2-0-30 : P.T.origin tree-1-2-0 occ-1-2-0-30 ≡ input s03
origin-1-2-0-30 = refl
transport-1-2-0-30 : P.T.origin tree-0-3-1 (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.source-leg , tt))) ≡ input (swap s03)
transport-1-2-0-30 = refl
occ-1-2-0-31 : P.T.Occurrence tree-1-2-0
occ-1-2-0-31 = (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.target-leg , tt)))
origin-1-2-0-31 : P.T.origin tree-1-2-0 occ-1-2-0-31 ≡ input s23
origin-1-2-0-31 = refl
transport-1-2-0-31 : P.T.origin tree-0-3-1 (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.target-leg , tt))) ≡ input (swap s23)
transport-1-2-0-31 = refl
occ-1-2-0-32 : P.T.Occurrence tree-1-2-0
occ-1-2-0-32 = (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.source-leg , tt)))
origin-1-2-0-32 : P.T.origin tree-1-2-0 occ-1-2-0-32 ≡ input s23
origin-1-2-0-32 = refl
transport-1-2-0-32 : P.T.origin tree-0-3-1 (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.source-leg , tt))) ≡ input (swap s23)
transport-1-2-0-32 = refl
occ-1-2-0-33 : P.T.Occurrence tree-1-2-0
occ-1-2-0-33 = (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.target-leg , tt)))
origin-1-2-0-33 : P.T.origin tree-1-2-0 occ-1-2-0-33 ≡ input s03
origin-1-2-0-33 = refl
transport-1-2-0-33 : P.T.origin tree-0-3-1 (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.target-leg , tt))) ≡ input (swap s03)
transport-1-2-0-33 = refl
occ-1-2-0-34 : P.T.Occurrence tree-1-2-0
occ-1-2-0-34 = (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-2-3)) , (P.S.source-leg , tt)))
origin-1-2-0-34 : P.T.origin tree-1-2-0 occ-1-2-0-34 ≡ input s23
origin-1-2-0-34 = refl
transport-1-2-0-34 : P.T.origin tree-0-3-1 (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-3-2)) , (P.S.source-leg , tt))) ≡ input (swap s23)
transport-1-2-0-34 = refl
occ-1-2-0-35 : P.T.Occurrence tree-1-2-0
occ-1-2-0-35 = (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-2-3)) , (P.S.target-leg , tt)))
origin-1-2-0-35 : P.T.origin tree-1-2-0 occ-1-2-0-35 ≡ input s23
origin-1-2-0-35 = refl
transport-1-2-0-35 : P.T.origin tree-0-3-1 (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-3-2)) , (P.S.target-leg , tt))) ≡ input (swap s23)
transport-1-2-0-35 = refl
occ-1-2-0-36 : P.T.Occurrence tree-1-2-0
occ-1-2-0-36 = (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-1-2-0-36 : P.T.origin tree-1-2-0 occ-1-2-0-36 ≡ input s10
origin-1-2-0-36 = refl
transport-1-2-0-36 : P.T.origin tree-0-3-1 (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s10)
transport-1-2-0-36 = refl
occ-1-2-0-37 : P.T.Occurrence tree-1-2-0
occ-1-2-0-37 = (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-1-2-0-37 : P.T.origin tree-1-2-0 occ-1-2-0-37 ≡ input s20
origin-1-2-0-37 = refl
transport-1-2-0-37 : P.T.origin tree-0-3-1 (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-1-2-0-37 = refl
occ-1-2-0-38 : P.T.Occurrence tree-1-2-0
occ-1-2-0-38 = (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-1-2-0-38 : P.T.origin tree-1-2-0 occ-1-2-0-38 ≡ input s30
origin-1-2-0-38 = refl
transport-1-2-0-38 : P.T.origin tree-0-3-1 (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s30)
transport-1-2-0-38 = refl
occ-1-2-0-39 : P.T.Occurrence tree-1-2-0
occ-1-2-0-39 = (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-1-2-0-39 : P.T.origin tree-1-2-0 occ-1-2-0-39 ≡ input s20
origin-1-2-0-39 = refl
transport-1-2-0-39 : P.T.origin tree-0-3-1 (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-1-2-0-39 = refl
occ-1-2-0-40 : P.T.Occurrence tree-1-2-0
occ-1-2-0-40 = (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.source-leg , tt)))
origin-1-2-0-40 : P.T.origin tree-1-2-0 occ-1-2-0-40 ≡ input s31
origin-1-2-0-40 = refl
transport-1-2-0-40 : P.T.origin tree-0-3-1 (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-1-2-0-40 = refl
occ-1-2-0-41 : P.T.Occurrence tree-1-2-0
occ-1-2-0-41 = (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.target-leg , tt)))
origin-1-2-0-41 : P.T.origin tree-1-2-0 occ-1-2-0-41 ≡ input s01
origin-1-2-0-41 = refl
transport-1-2-0-41 : P.T.origin tree-0-3-1 (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.target-leg , tt))) ≡ input (swap s01)
transport-1-2-0-41 = refl
occ-1-2-0-42 : P.T.Occurrence tree-1-2-0
occ-1-2-0-42 = (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.source-leg , tt)))
origin-1-2-0-42 : P.T.origin tree-1-2-0 occ-1-2-0-42 ≡ input s31
origin-1-2-0-42 = refl
transport-1-2-0-42 : P.T.origin tree-0-3-1 (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-1-2-0-42 = refl
occ-1-2-0-43 : P.T.Occurrence tree-1-2-0
occ-1-2-0-43 = (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.target-leg , tt)))
origin-1-2-0-43 : P.T.origin tree-1-2-0 occ-1-2-0-43 ≡ input s21
origin-1-2-0-43 = refl
transport-1-2-0-43 : P.T.origin tree-0-3-1 (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.target-leg , tt))) ≡ input (swap s21)
transport-1-2-0-43 = refl
occ-1-2-0-44 : P.T.Occurrence tree-1-2-0
occ-1-2-0-44 = (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-1-2-0-44 : P.T.origin tree-1-2-0 occ-1-2-0-44 ≡ input s12
origin-1-2-0-44 = refl
transport-1-2-0-44 : P.T.origin tree-0-3-1 (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s12)
transport-1-2-0-44 = refl
occ-1-2-0-45 : P.T.Occurrence tree-1-2-0
occ-1-2-0-45 = (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-1-2-0-45 : P.T.origin tree-1-2-0 occ-1-2-0-45 ≡ input s02
origin-1-2-0-45 = refl
transport-1-2-0-45 : P.T.origin tree-0-3-1 (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-1-2-0-45 = refl
occ-1-2-0-46 : P.T.Occurrence tree-1-2-0
occ-1-2-0-46 = (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-1-2-0-46 : P.T.origin tree-1-2-0 occ-1-2-0-46 ≡ input s32
origin-1-2-0-46 = refl
transport-1-2-0-46 : P.T.origin tree-0-3-1 (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s32)
transport-1-2-0-46 = refl
occ-1-2-0-47 : P.T.Occurrence tree-1-2-0
occ-1-2-0-47 = (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-1-2-0-47 : P.T.origin tree-1-2-0 occ-1-2-0-47 ≡ input s02
origin-1-2-0-47 = refl
transport-1-2-0-47 : P.T.origin tree-0-3-1 (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-1-2-0-47 = refl
occ-1-2-0-48 : P.T.Occurrence tree-1-2-0
occ-1-2-0-48 = (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.source-leg , tt)))
origin-1-2-0-48 : P.T.origin tree-1-2-0 occ-1-2-0-48 ≡ input s13
origin-1-2-0-48 = refl
transport-1-2-0-48 : P.T.origin tree-0-3-1 (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-1-2-0-48 = refl
occ-1-2-0-49 : P.T.Occurrence tree-1-2-0
occ-1-2-0-49 = (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.target-leg , tt)))
origin-1-2-0-49 : P.T.origin tree-1-2-0 occ-1-2-0-49 ≡ input s03
origin-1-2-0-49 = refl
transport-1-2-0-49 : P.T.origin tree-0-3-1 (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.target-leg , tt))) ≡ input (swap s03)
transport-1-2-0-49 = refl
occ-1-2-0-50 : P.T.Occurrence tree-1-2-0
occ-1-2-0-50 = (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.source-leg , tt)))
origin-1-2-0-50 : P.T.origin tree-1-2-0 occ-1-2-0-50 ≡ input s13
origin-1-2-0-50 = refl
transport-1-2-0-50 : P.T.origin tree-0-3-1 (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-1-2-0-50 = refl
occ-1-2-0-51 : P.T.Occurrence tree-1-2-0
occ-1-2-0-51 = (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.target-leg , tt)))
origin-1-2-0-51 : P.T.origin tree-1-2-0 occ-1-2-0-51 ≡ input s23
origin-1-2-0-51 = refl
transport-1-2-0-51 : P.T.origin tree-0-3-1 (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.target-leg , tt))) ≡ input (swap s23)
transport-1-2-0-51 = refl
occ-1-2-0-52 : P.T.Occurrence tree-1-2-0
occ-1-2-0-52 = (P.S.full-source , (P.S.first-port , tt))
origin-1-2-0-52 : P.T.origin tree-1-2-0 occ-1-2-0-52 ≡ input s13
origin-1-2-0-52 = refl
transport-1-2-0-52 : P.T.origin tree-0-3-1 (P.S.full-source , (P.S.first-port , tt)) ≡ input (swap s13)
transport-1-2-0-52 = refl
occ-1-2-0-53 : P.T.Occurrence tree-1-2-0
occ-1-2-0-53 = (P.S.full-source , (P.S.middle-port , tt))
origin-1-2-0-53 : P.T.origin tree-1-2-0 occ-1-2-0-53 ≡ input s23
origin-1-2-0-53 = refl
transport-1-2-0-53 : P.T.origin tree-0-3-1 (P.S.full-source , (P.S.middle-port , tt)) ≡ input (swap s23)
transport-1-2-0-53 = refl
occ-1-2-0-54 : P.T.Occurrence tree-1-2-0
occ-1-2-0-54 = (P.S.full-source , (P.S.final-port , tt))
origin-1-2-0-54 : P.T.origin tree-1-2-0 occ-1-2-0-54 ≡ input s03
origin-1-2-0-54 = refl
transport-1-2-0-54 : P.T.origin tree-0-3-1 (P.S.full-source , (P.S.final-port , tt)) ≡ input (swap s03)
transport-1-2-0-54 = refl
selected-source-1-2-0-AB : P.S.ab-index {a = C.q7} {b = C.q0} {c = C.q0} F.triple-1-2-0 ≡ (m1 , (F.vp-1-3 , F.vp-2-3))
selected-source-1-2-0-AB = refl
selected-target-1-2-0-AB : P.S.ab-index {a = C.q0} {b = C.q7} {c = C.q7} F.triple-0-3-1 ≡ (c1 , (F.vp-0-2 , F.vp-3-2))
selected-target-1-2-0-AB = refl
selected-source-1-2-0-BC : P.S.bc-index {a = C.q7} {b = C.q0} {c = C.q0} F.triple-1-2-0 ≡ (m1 , (F.vp-2-3 , F.vp-0-3))
selected-source-1-2-0-BC = refl
selected-target-1-2-0-BC : P.S.bc-index {a = C.q0} {b = C.q7} {c = C.q7} F.triple-0-3-1 ≡ (c1 , (F.vp-3-2 , F.vp-1-2))
selected-target-1-2-0-BC = refl
selected-source-1-2-0-AC : P.S.ac-index {a = C.q7} {b = C.q0} {c = C.q0} F.triple-1-2-0 ≡ (m1 , (F.vp-1-3 , F.vp-0-3))
selected-source-1-2-0-AC = refl
selected-target-1-2-0-AC : P.S.ac-index {a = C.q0} {b = C.q7} {c = C.q7} F.triple-0-3-1 ≡ (c1 , (F.vp-0-2 , F.vp-1-2))
selected-target-1-2-0-AC = refl
occ-1-2-3-0 : P.T.Occurrence tree-1-2-3
occ-1-2-3-0 = (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-1-2-3-0 : P.T.origin tree-1-2-3 occ-1-2-3-0 ≡ input s10
origin-1-2-3-0 = refl
transport-1-2-3-0 : P.T.origin tree-0-3-2 (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s10)
transport-1-2-3-0 = refl
occ-1-2-3-1 : P.T.Occurrence tree-1-2-3
occ-1-2-3-1 = (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-1-2-3-1 : P.T.origin tree-1-2-3 occ-1-2-3-1 ≡ input s20
origin-1-2-3-1 = refl
transport-1-2-3-1 : P.T.origin tree-0-3-2 (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-1-2-3-1 = refl
occ-1-2-3-2 : P.T.Occurrence tree-1-2-3
occ-1-2-3-2 = (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-1-2-3-2 : P.T.origin tree-1-2-3 occ-1-2-3-2 ≡ input s30
origin-1-2-3-2 = refl
transport-1-2-3-2 : P.T.origin tree-0-3-2 (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s30)
transport-1-2-3-2 = refl
occ-1-2-3-3 : P.T.Occurrence tree-1-2-3
occ-1-2-3-3 = (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-1-2-3-3 : P.T.origin tree-1-2-3 occ-1-2-3-3 ≡ input s20
origin-1-2-3-3 = refl
transport-1-2-3-3 : P.T.origin tree-0-3-2 (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-1-2-3-3 = refl
occ-1-2-3-4 : P.T.Occurrence tree-1-2-3
occ-1-2-3-4 = (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.source-leg , tt)))
origin-1-2-3-4 : P.T.origin tree-1-2-3 occ-1-2-3-4 ≡ input s31
origin-1-2-3-4 = refl
transport-1-2-3-4 : P.T.origin tree-0-3-2 (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-1-2-3-4 = refl
occ-1-2-3-5 : P.T.Occurrence tree-1-2-3
occ-1-2-3-5 = (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.target-leg , tt)))
origin-1-2-3-5 : P.T.origin tree-1-2-3 occ-1-2-3-5 ≡ input s01
origin-1-2-3-5 = refl
transport-1-2-3-5 : P.T.origin tree-0-3-2 (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.target-leg , tt))) ≡ input (swap s01)
transport-1-2-3-5 = refl
occ-1-2-3-6 : P.T.Occurrence tree-1-2-3
occ-1-2-3-6 = (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.source-leg , tt)))
origin-1-2-3-6 : P.T.origin tree-1-2-3 occ-1-2-3-6 ≡ input s31
origin-1-2-3-6 = refl
transport-1-2-3-6 : P.T.origin tree-0-3-2 (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-1-2-3-6 = refl
occ-1-2-3-7 : P.T.Occurrence tree-1-2-3
occ-1-2-3-7 = (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.target-leg , tt)))
origin-1-2-3-7 : P.T.origin tree-1-2-3 occ-1-2-3-7 ≡ input s21
origin-1-2-3-7 = refl
transport-1-2-3-7 : P.T.origin tree-0-3-2 (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.target-leg , tt))) ≡ input (swap s21)
transport-1-2-3-7 = refl
occ-1-2-3-8 : P.T.Occurrence tree-1-2-3
occ-1-2-3-8 = (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-1-2-3-8 : P.T.origin tree-1-2-3 occ-1-2-3-8 ≡ input s12
origin-1-2-3-8 = refl
transport-1-2-3-8 : P.T.origin tree-0-3-2 (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s12)
transport-1-2-3-8 = refl
occ-1-2-3-9 : P.T.Occurrence tree-1-2-3
occ-1-2-3-9 = (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-1-2-3-9 : P.T.origin tree-1-2-3 occ-1-2-3-9 ≡ input s02
origin-1-2-3-9 = refl
transport-1-2-3-9 : P.T.origin tree-0-3-2 (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-1-2-3-9 = refl
occ-1-2-3-10 : P.T.Occurrence tree-1-2-3
occ-1-2-3-10 = (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-1-2-3-10 : P.T.origin tree-1-2-3 occ-1-2-3-10 ≡ input s32
origin-1-2-3-10 = refl
transport-1-2-3-10 : P.T.origin tree-0-3-2 (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s32)
transport-1-2-3-10 = refl
occ-1-2-3-11 : P.T.Occurrence tree-1-2-3
occ-1-2-3-11 = (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-1-2-3-11 : P.T.origin tree-1-2-3 occ-1-2-3-11 ≡ input s02
origin-1-2-3-11 = refl
transport-1-2-3-11 : P.T.origin tree-0-3-2 (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-1-2-3-11 = refl
occ-1-2-3-12 : P.T.Occurrence tree-1-2-3
occ-1-2-3-12 = (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.source-leg , tt)))
origin-1-2-3-12 : P.T.origin tree-1-2-3 occ-1-2-3-12 ≡ input s13
origin-1-2-3-12 = refl
transport-1-2-3-12 : P.T.origin tree-0-3-2 (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-1-2-3-12 = refl
occ-1-2-3-13 : P.T.Occurrence tree-1-2-3
occ-1-2-3-13 = (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.target-leg , tt)))
origin-1-2-3-13 : P.T.origin tree-1-2-3 occ-1-2-3-13 ≡ input s03
origin-1-2-3-13 = refl
transport-1-2-3-13 : P.T.origin tree-0-3-2 (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.target-leg , tt))) ≡ input (swap s03)
transport-1-2-3-13 = refl
occ-1-2-3-14 : P.T.Occurrence tree-1-2-3
occ-1-2-3-14 = (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.source-leg , tt)))
origin-1-2-3-14 : P.T.origin tree-1-2-3 occ-1-2-3-14 ≡ input s13
origin-1-2-3-14 = refl
transport-1-2-3-14 : P.T.origin tree-0-3-2 (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-1-2-3-14 = refl
occ-1-2-3-15 : P.T.Occurrence tree-1-2-3
occ-1-2-3-15 = (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.target-leg , tt)))
origin-1-2-3-15 : P.T.origin tree-1-2-3 occ-1-2-3-15 ≡ input s23
origin-1-2-3-15 = refl
transport-1-2-3-15 : P.T.origin tree-0-3-2 (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.target-leg , tt))) ≡ input (swap s23)
transport-1-2-3-15 = refl
occ-1-2-3-16 : P.T.Occurrence tree-1-2-3
occ-1-2-3-16 = (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.source-leg , tt)))
origin-1-2-3-16 : P.T.origin tree-1-2-3 occ-1-2-3-16 ≡ input s20
origin-1-2-3-16 = refl
transport-1-2-3-16 : P.T.origin tree-0-3-2 (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-1-2-3-16 = refl
occ-1-2-3-17 : P.T.Occurrence tree-1-2-3
occ-1-2-3-17 = (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.target-leg , tt)))
origin-1-2-3-17 : P.T.origin tree-1-2-3 occ-1-2-3-17 ≡ input s10
origin-1-2-3-17 = refl
transport-1-2-3-17 : P.T.origin tree-0-3-2 (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.target-leg , tt))) ≡ input (swap s10)
transport-1-2-3-17 = refl
occ-1-2-3-18 : P.T.Occurrence tree-1-2-3
occ-1-2-3-18 = (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.source-leg , tt)))
origin-1-2-3-18 : P.T.origin tree-1-2-3 occ-1-2-3-18 ≡ input s20
origin-1-2-3-18 = refl
transport-1-2-3-18 : P.T.origin tree-0-3-2 (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-1-2-3-18 = refl
occ-1-2-3-19 : P.T.Occurrence tree-1-2-3
occ-1-2-3-19 = (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.target-leg , tt)))
origin-1-2-3-19 : P.T.origin tree-1-2-3 occ-1-2-3-19 ≡ input s30
origin-1-2-3-19 = refl
transport-1-2-3-19 : P.T.origin tree-0-3-2 (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.target-leg , tt))) ≡ input (swap s30)
transport-1-2-3-19 = refl
occ-1-2-3-20 : P.T.Occurrence tree-1-2-3
occ-1-2-3-20 = (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-1-2-3-20 : P.T.origin tree-1-2-3 occ-1-2-3-20 ≡ input s01
origin-1-2-3-20 = refl
transport-1-2-3-20 : P.T.origin tree-0-3-2 (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s01)
transport-1-2-3-20 = refl
occ-1-2-3-21 : P.T.Occurrence tree-1-2-3
occ-1-2-3-21 = (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-1-2-3-21 : P.T.origin tree-1-2-3 occ-1-2-3-21 ≡ input s31
origin-1-2-3-21 = refl
transport-1-2-3-21 : P.T.origin tree-0-3-2 (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-1-2-3-21 = refl
occ-1-2-3-22 : P.T.Occurrence tree-1-2-3
occ-1-2-3-22 = (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-1-2-3-22 : P.T.origin tree-1-2-3 occ-1-2-3-22 ≡ input s21
origin-1-2-3-22 = refl
transport-1-2-3-22 : P.T.origin tree-0-3-2 (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s21)
transport-1-2-3-22 = refl
occ-1-2-3-23 : P.T.Occurrence tree-1-2-3
occ-1-2-3-23 = (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-1-2-3-23 : P.T.origin tree-1-2-3 occ-1-2-3-23 ≡ input s31
origin-1-2-3-23 = refl
transport-1-2-3-23 : P.T.origin tree-0-3-2 (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-1-2-3-23 = refl
occ-1-2-3-24 : P.T.Occurrence tree-1-2-3
occ-1-2-3-24 = (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.source-leg , tt)))
origin-1-2-3-24 : P.T.origin tree-1-2-3 occ-1-2-3-24 ≡ input s02
origin-1-2-3-24 = refl
transport-1-2-3-24 : P.T.origin tree-0-3-2 (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-1-2-3-24 = refl
occ-1-2-3-25 : P.T.Occurrence tree-1-2-3
occ-1-2-3-25 = (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.target-leg , tt)))
origin-1-2-3-25 : P.T.origin tree-1-2-3 occ-1-2-3-25 ≡ input s12
origin-1-2-3-25 = refl
transport-1-2-3-25 : P.T.origin tree-0-3-2 (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.target-leg , tt))) ≡ input (swap s12)
transport-1-2-3-25 = refl
occ-1-2-3-26 : P.T.Occurrence tree-1-2-3
occ-1-2-3-26 = (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.source-leg , tt)))
origin-1-2-3-26 : P.T.origin tree-1-2-3 occ-1-2-3-26 ≡ input s02
origin-1-2-3-26 = refl
transport-1-2-3-26 : P.T.origin tree-0-3-2 (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-1-2-3-26 = refl
occ-1-2-3-27 : P.T.Occurrence tree-1-2-3
occ-1-2-3-27 = (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.target-leg , tt)))
origin-1-2-3-27 : P.T.origin tree-1-2-3 occ-1-2-3-27 ≡ input s32
origin-1-2-3-27 = refl
transport-1-2-3-27 : P.T.origin tree-0-3-2 (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.target-leg , tt))) ≡ input (swap s32)
transport-1-2-3-27 = refl
occ-1-2-3-28 : P.T.Occurrence tree-1-2-3
occ-1-2-3-28 = (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-1-2-3-28 : P.T.origin tree-1-2-3 occ-1-2-3-28 ≡ input s03
origin-1-2-3-28 = refl
transport-1-2-3-28 : P.T.origin tree-0-3-2 (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s03)
transport-1-2-3-28 = refl
occ-1-2-3-29 : P.T.Occurrence tree-1-2-3
occ-1-2-3-29 = (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-1-2-3-29 : P.T.origin tree-1-2-3 occ-1-2-3-29 ≡ input s13
origin-1-2-3-29 = refl
transport-1-2-3-29 : P.T.origin tree-0-3-2 (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-1-2-3-29 = refl
occ-1-2-3-30 : P.T.Occurrence tree-1-2-3
occ-1-2-3-30 = (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-1-2-3-30 : P.T.origin tree-1-2-3 occ-1-2-3-30 ≡ input s23
origin-1-2-3-30 = refl
transport-1-2-3-30 : P.T.origin tree-0-3-2 (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s23)
transport-1-2-3-30 = refl
occ-1-2-3-31 : P.T.Occurrence tree-1-2-3
occ-1-2-3-31 = (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-1-2-3-31 : P.T.origin tree-1-2-3 occ-1-2-3-31 ≡ input s13
origin-1-2-3-31 = refl
transport-1-2-3-31 : P.T.origin tree-0-3-2 (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-1-2-3-31 = refl
occ-1-2-3-32 : P.T.Occurrence tree-1-2-3
occ-1-2-3-32 = (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-1-0)) , (P.S.source-leg , tt)))
origin-1-2-3-32 : P.T.origin tree-1-2-3 occ-1-2-3-32 ≡ input s10
origin-1-2-3-32 = refl
transport-1-2-3-32 : P.T.origin tree-0-3-2 (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-0-1)) , (P.S.source-leg , tt))) ≡ input (swap s10)
transport-1-2-3-32 = refl
occ-1-2-3-33 : P.T.Occurrence tree-1-2-3
occ-1-2-3-33 = (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-1-0)) , (P.S.target-leg , tt)))
origin-1-2-3-33 : P.T.origin tree-1-2-3 occ-1-2-3-33 ≡ input s10
origin-1-2-3-33 = refl
transport-1-2-3-33 : P.T.origin tree-0-3-2 (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-0-1)) , (P.S.target-leg , tt))) ≡ input (swap s10)
transport-1-2-3-33 = refl
occ-1-2-3-34 : P.T.Occurrence tree-1-2-3
occ-1-2-3-34 = (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.source-leg , tt)))
origin-1-2-3-34 : P.T.origin tree-1-2-3 occ-1-2-3-34 ≡ input s10
origin-1-2-3-34 = refl
transport-1-2-3-34 : P.T.origin tree-0-3-2 (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.source-leg , tt))) ≡ input (swap s10)
transport-1-2-3-34 = refl
occ-1-2-3-35 : P.T.Occurrence tree-1-2-3
occ-1-2-3-35 = (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.target-leg , tt)))
origin-1-2-3-35 : P.T.origin tree-1-2-3 occ-1-2-3-35 ≡ input s30
origin-1-2-3-35 = refl
transport-1-2-3-35 : P.T.origin tree-0-3-2 (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.target-leg , tt))) ≡ input (swap s30)
transport-1-2-3-35 = refl
occ-1-2-3-36 : P.T.Occurrence tree-1-2-3
occ-1-2-3-36 = (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.source-leg , tt)))
origin-1-2-3-36 : P.T.origin tree-1-2-3 occ-1-2-3-36 ≡ input s30
origin-1-2-3-36 = refl
transport-1-2-3-36 : P.T.origin tree-0-3-2 (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.source-leg , tt))) ≡ input (swap s30)
transport-1-2-3-36 = refl
occ-1-2-3-37 : P.T.Occurrence tree-1-2-3
occ-1-2-3-37 = (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.target-leg , tt)))
origin-1-2-3-37 : P.T.origin tree-1-2-3 occ-1-2-3-37 ≡ input s10
origin-1-2-3-37 = refl
transport-1-2-3-37 : P.T.origin tree-0-3-2 (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.target-leg , tt))) ≡ input (swap s10)
transport-1-2-3-37 = refl
occ-1-2-3-38 : P.T.Occurrence tree-1-2-3
occ-1-2-3-38 = (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-3-0)) , (P.S.source-leg , tt)))
origin-1-2-3-38 : P.T.origin tree-1-2-3 occ-1-2-3-38 ≡ input s30
origin-1-2-3-38 = refl
transport-1-2-3-38 : P.T.origin tree-0-3-2 (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-2-1)) , (P.S.source-leg , tt))) ≡ input (swap s30)
transport-1-2-3-38 = refl
occ-1-2-3-39 : P.T.Occurrence tree-1-2-3
occ-1-2-3-39 = (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-3-0)) , (P.S.target-leg , tt)))
origin-1-2-3-39 : P.T.origin tree-1-2-3 occ-1-2-3-39 ≡ input s30
origin-1-2-3-39 = refl
transport-1-2-3-39 : P.T.origin tree-0-3-2 (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-2-1)) , (P.S.target-leg , tt))) ≡ input (swap s30)
transport-1-2-3-39 = refl
occ-1-2-3-40 : P.T.Occurrence tree-1-2-3
occ-1-2-3-40 = (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-1-2-3-40 : P.T.origin tree-1-2-3 occ-1-2-3-40 ≡ input s31
origin-1-2-3-40 = refl
transport-1-2-3-40 : P.T.origin tree-0-3-2 (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-1-2-3-40 = refl
occ-1-2-3-41 : P.T.Occurrence tree-1-2-3
occ-1-2-3-41 = (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-1-2-3-41 : P.T.origin tree-1-2-3 occ-1-2-3-41 ≡ input s31
origin-1-2-3-41 = refl
transport-1-2-3-41 : P.T.origin tree-0-3-2 (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-1-2-3-41 = refl
occ-1-2-3-42 : P.T.Occurrence tree-1-2-3
occ-1-2-3-42 = (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-1-2)) , (P.S.source-leg , tt)))
origin-1-2-3-42 : P.T.origin tree-1-2-3 occ-1-2-3-42 ≡ input s12
origin-1-2-3-42 = refl
transport-1-2-3-42 : P.T.origin tree-0-3-2 (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-0-3)) , (P.S.source-leg , tt))) ≡ input (swap s12)
transport-1-2-3-42 = refl
occ-1-2-3-43 : P.T.Occurrence tree-1-2-3
occ-1-2-3-43 = (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-1-2)) , (P.S.target-leg , tt)))
origin-1-2-3-43 : P.T.origin tree-1-2-3 occ-1-2-3-43 ≡ input s12
origin-1-2-3-43 = refl
transport-1-2-3-43 : P.T.origin tree-0-3-2 (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-0-3)) , (P.S.target-leg , tt))) ≡ input (swap s12)
transport-1-2-3-43 = refl
occ-1-2-3-44 : P.T.Occurrence tree-1-2-3
occ-1-2-3-44 = (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.source-leg , tt)))
origin-1-2-3-44 : P.T.origin tree-1-2-3 occ-1-2-3-44 ≡ input s12
origin-1-2-3-44 = refl
transport-1-2-3-44 : P.T.origin tree-0-3-2 (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.source-leg , tt))) ≡ input (swap s12)
transport-1-2-3-44 = refl
occ-1-2-3-45 : P.T.Occurrence tree-1-2-3
occ-1-2-3-45 = (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.target-leg , tt)))
origin-1-2-3-45 : P.T.origin tree-1-2-3 occ-1-2-3-45 ≡ input s32
origin-1-2-3-45 = refl
transport-1-2-3-45 : P.T.origin tree-0-3-2 (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.target-leg , tt))) ≡ input (swap s32)
transport-1-2-3-45 = refl
occ-1-2-3-46 : P.T.Occurrence tree-1-2-3
occ-1-2-3-46 = (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.source-leg , tt)))
origin-1-2-3-46 : P.T.origin tree-1-2-3 occ-1-2-3-46 ≡ input s32
origin-1-2-3-46 = refl
transport-1-2-3-46 : P.T.origin tree-0-3-2 (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.source-leg , tt))) ≡ input (swap s32)
transport-1-2-3-46 = refl
occ-1-2-3-47 : P.T.Occurrence tree-1-2-3
occ-1-2-3-47 = (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.target-leg , tt)))
origin-1-2-3-47 : P.T.origin tree-1-2-3 occ-1-2-3-47 ≡ input s12
origin-1-2-3-47 = refl
transport-1-2-3-47 : P.T.origin tree-0-3-2 (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.target-leg , tt))) ≡ input (swap s12)
transport-1-2-3-47 = refl
occ-1-2-3-48 : P.T.Occurrence tree-1-2-3
occ-1-2-3-48 = (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-3-2)) , (P.S.source-leg , tt)))
origin-1-2-3-48 : P.T.origin tree-1-2-3 occ-1-2-3-48 ≡ input s32
origin-1-2-3-48 = refl
transport-1-2-3-48 : P.T.origin tree-0-3-2 (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-2-3)) , (P.S.source-leg , tt))) ≡ input (swap s32)
transport-1-2-3-48 = refl
occ-1-2-3-49 : P.T.Occurrence tree-1-2-3
occ-1-2-3-49 = (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-3-2)) , (P.S.target-leg , tt)))
origin-1-2-3-49 : P.T.origin tree-1-2-3 occ-1-2-3-49 ≡ input s32
origin-1-2-3-49 = refl
transport-1-2-3-49 : P.T.origin tree-0-3-2 (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-2-3)) , (P.S.target-leg , tt))) ≡ input (swap s32)
transport-1-2-3-49 = refl
occ-1-2-3-50 : P.T.Occurrence tree-1-2-3
occ-1-2-3-50 = (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-1-2-3-50 : P.T.origin tree-1-2-3 occ-1-2-3-50 ≡ input s13
origin-1-2-3-50 = refl
transport-1-2-3-50 : P.T.origin tree-0-3-2 (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-1-2-3-50 = refl
occ-1-2-3-51 : P.T.Occurrence tree-1-2-3
occ-1-2-3-51 = (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-1-2-3-51 : P.T.origin tree-1-2-3 occ-1-2-3-51 ≡ input s13
origin-1-2-3-51 = refl
transport-1-2-3-51 : P.T.origin tree-0-3-2 (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-1-2-3-51 = refl
occ-1-2-3-52 : P.T.Occurrence tree-1-2-3
occ-1-2-3-52 = (P.S.full-source , (P.S.first-port , tt))
origin-1-2-3-52 : P.T.origin tree-1-2-3 occ-1-2-3-52 ≡ input s10
origin-1-2-3-52 = refl
transport-1-2-3-52 : P.T.origin tree-0-3-2 (P.S.full-source , (P.S.first-port , tt)) ≡ input (swap s10)
transport-1-2-3-52 = refl
occ-1-2-3-53 : P.T.Occurrence tree-1-2-3
occ-1-2-3-53 = (P.S.full-source , (P.S.middle-port , tt))
origin-1-2-3-53 : P.T.origin tree-1-2-3 occ-1-2-3-53 ≡ input s20
origin-1-2-3-53 = refl
transport-1-2-3-53 : P.T.origin tree-0-3-2 (P.S.full-source , (P.S.middle-port , tt)) ≡ input (swap s20)
transport-1-2-3-53 = refl
occ-1-2-3-54 : P.T.Occurrence tree-1-2-3
occ-1-2-3-54 = (P.S.full-source , (P.S.final-port , tt))
origin-1-2-3-54 : P.T.origin tree-1-2-3 occ-1-2-3-54 ≡ input s30
origin-1-2-3-54 = refl
transport-1-2-3-54 : P.T.origin tree-0-3-2 (P.S.full-source , (P.S.final-port , tt)) ≡ input (swap s30)
transport-1-2-3-54 = refl
selected-source-1-2-3-AB : P.S.ab-index {a = C.q7} {b = C.q0} {c = C.q7} F.triple-1-2-3 ≡ (c0 , (F.vp-1-0 , F.vp-2-0))
selected-source-1-2-3-AB = refl
selected-target-1-2-3-AB : P.S.ab-index {a = C.q0} {b = C.q7} {c = C.q0} F.triple-0-3-2 ≡ (m0 , (F.vp-0-1 , F.vp-3-1))
selected-target-1-2-3-AB = refl
selected-source-1-2-3-BC : P.S.bc-index {a = C.q7} {b = C.q0} {c = C.q7} F.triple-1-2-3 ≡ (c0 , (F.vp-2-0 , F.vp-3-0))
selected-source-1-2-3-BC = refl
selected-target-1-2-3-BC : P.S.bc-index {a = C.q0} {b = C.q7} {c = C.q0} F.triple-0-3-2 ≡ (m0 , (F.vp-3-1 , F.vp-2-1))
selected-target-1-2-3-BC = refl
selected-source-1-2-3-AC : P.S.ac-index {a = C.q7} {b = C.q0} {c = C.q7} F.triple-1-2-3 ≡ (c0 , (F.vp-1-0 , F.vp-3-0))
selected-source-1-2-3-AC = refl
selected-target-1-2-3-AC : P.S.ac-index {a = C.q0} {b = C.q7} {c = C.q0} F.triple-0-3-2 ≡ (m0 , (F.vp-0-1 , F.vp-2-1))
selected-target-1-2-3-AC = refl
occ-1-3-0-0 : P.T.Occurrence tree-1-3-0
occ-1-3-0-0 = (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-1-0)) , (P.S.source-leg , tt)))
origin-1-3-0-0 : P.T.origin tree-1-3-0 occ-1-3-0-0 ≡ input s10
origin-1-3-0-0 = refl
transport-1-3-0-0 : P.T.origin tree-0-2-1 (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-0-1)) , (P.S.source-leg , tt))) ≡ input (swap s10)
transport-1-3-0-0 = refl
occ-1-3-0-1 : P.T.Occurrence tree-1-3-0
occ-1-3-0-1 = (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-1-0)) , (P.S.target-leg , tt)))
origin-1-3-0-1 : P.T.origin tree-1-3-0 occ-1-3-0-1 ≡ input s10
origin-1-3-0-1 = refl
transport-1-3-0-1 : P.T.origin tree-0-2-1 (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-0-1)) , (P.S.target-leg , tt))) ≡ input (swap s10)
transport-1-3-0-1 = refl
occ-1-3-0-2 : P.T.Occurrence tree-1-3-0
occ-1-3-0-2 = (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.source-leg , tt)))
origin-1-3-0-2 : P.T.origin tree-1-3-0 occ-1-3-0-2 ≡ input s10
origin-1-3-0-2 = refl
transport-1-3-0-2 : P.T.origin tree-0-2-1 (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.source-leg , tt))) ≡ input (swap s10)
transport-1-3-0-2 = refl
occ-1-3-0-3 : P.T.Occurrence tree-1-3-0
occ-1-3-0-3 = (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.target-leg , tt)))
origin-1-3-0-3 : P.T.origin tree-1-3-0 occ-1-3-0-3 ≡ input s30
origin-1-3-0-3 = refl
transport-1-3-0-3 : P.T.origin tree-0-2-1 (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.target-leg , tt))) ≡ input (swap s30)
transport-1-3-0-3 = refl
occ-1-3-0-4 : P.T.Occurrence tree-1-3-0
occ-1-3-0-4 = (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.source-leg , tt)))
origin-1-3-0-4 : P.T.origin tree-1-3-0 occ-1-3-0-4 ≡ input s30
origin-1-3-0-4 = refl
transport-1-3-0-4 : P.T.origin tree-0-2-1 (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.source-leg , tt))) ≡ input (swap s30)
transport-1-3-0-4 = refl
occ-1-3-0-5 : P.T.Occurrence tree-1-3-0
occ-1-3-0-5 = (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.target-leg , tt)))
origin-1-3-0-5 : P.T.origin tree-1-3-0 occ-1-3-0-5 ≡ input s10
origin-1-3-0-5 = refl
transport-1-3-0-5 : P.T.origin tree-0-2-1 (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.target-leg , tt))) ≡ input (swap s10)
transport-1-3-0-5 = refl
occ-1-3-0-6 : P.T.Occurrence tree-1-3-0
occ-1-3-0-6 = (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-3-0)) , (P.S.source-leg , tt)))
origin-1-3-0-6 : P.T.origin tree-1-3-0 occ-1-3-0-6 ≡ input s30
origin-1-3-0-6 = refl
transport-1-3-0-6 : P.T.origin tree-0-2-1 (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-2-1)) , (P.S.source-leg , tt))) ≡ input (swap s30)
transport-1-3-0-6 = refl
occ-1-3-0-7 : P.T.Occurrence tree-1-3-0
occ-1-3-0-7 = (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-3-0)) , (P.S.target-leg , tt)))
origin-1-3-0-7 : P.T.origin tree-1-3-0 occ-1-3-0-7 ≡ input s30
origin-1-3-0-7 = refl
transport-1-3-0-7 : P.T.origin tree-0-2-1 (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-2-1)) , (P.S.target-leg , tt))) ≡ input (swap s30)
transport-1-3-0-7 = refl
occ-1-3-0-8 : P.T.Occurrence tree-1-3-0
occ-1-3-0-8 = (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-1-3-0-8 : P.T.origin tree-1-3-0 occ-1-3-0-8 ≡ input s31
origin-1-3-0-8 = refl
transport-1-3-0-8 : P.T.origin tree-0-2-1 (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-1-3-0-8 = refl
occ-1-3-0-9 : P.T.Occurrence tree-1-3-0
occ-1-3-0-9 = (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-1-3-0-9 : P.T.origin tree-1-3-0 occ-1-3-0-9 ≡ input s31
origin-1-3-0-9 = refl
transport-1-3-0-9 : P.T.origin tree-0-2-1 (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-1-3-0-9 = refl
occ-1-3-0-10 : P.T.Occurrence tree-1-3-0
occ-1-3-0-10 = (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-1-2)) , (P.S.source-leg , tt)))
origin-1-3-0-10 : P.T.origin tree-1-3-0 occ-1-3-0-10 ≡ input s12
origin-1-3-0-10 = refl
transport-1-3-0-10 : P.T.origin tree-0-2-1 (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-0-3)) , (P.S.source-leg , tt))) ≡ input (swap s12)
transport-1-3-0-10 = refl
occ-1-3-0-11 : P.T.Occurrence tree-1-3-0
occ-1-3-0-11 = (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-1-2)) , (P.S.target-leg , tt)))
origin-1-3-0-11 : P.T.origin tree-1-3-0 occ-1-3-0-11 ≡ input s12
origin-1-3-0-11 = refl
transport-1-3-0-11 : P.T.origin tree-0-2-1 (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-0-3)) , (P.S.target-leg , tt))) ≡ input (swap s12)
transport-1-3-0-11 = refl
occ-1-3-0-12 : P.T.Occurrence tree-1-3-0
occ-1-3-0-12 = (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.source-leg , tt)))
origin-1-3-0-12 : P.T.origin tree-1-3-0 occ-1-3-0-12 ≡ input s12
origin-1-3-0-12 = refl
transport-1-3-0-12 : P.T.origin tree-0-2-1 (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.source-leg , tt))) ≡ input (swap s12)
transport-1-3-0-12 = refl
occ-1-3-0-13 : P.T.Occurrence tree-1-3-0
occ-1-3-0-13 = (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.target-leg , tt)))
origin-1-3-0-13 : P.T.origin tree-1-3-0 occ-1-3-0-13 ≡ input s32
origin-1-3-0-13 = refl
transport-1-3-0-13 : P.T.origin tree-0-2-1 (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.target-leg , tt))) ≡ input (swap s32)
transport-1-3-0-13 = refl
occ-1-3-0-14 : P.T.Occurrence tree-1-3-0
occ-1-3-0-14 = (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.source-leg , tt)))
origin-1-3-0-14 : P.T.origin tree-1-3-0 occ-1-3-0-14 ≡ input s32
origin-1-3-0-14 = refl
transport-1-3-0-14 : P.T.origin tree-0-2-1 (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.source-leg , tt))) ≡ input (swap s32)
transport-1-3-0-14 = refl
occ-1-3-0-15 : P.T.Occurrence tree-1-3-0
occ-1-3-0-15 = (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.target-leg , tt)))
origin-1-3-0-15 : P.T.origin tree-1-3-0 occ-1-3-0-15 ≡ input s12
origin-1-3-0-15 = refl
transport-1-3-0-15 : P.T.origin tree-0-2-1 (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.target-leg , tt))) ≡ input (swap s12)
transport-1-3-0-15 = refl
occ-1-3-0-16 : P.T.Occurrence tree-1-3-0
occ-1-3-0-16 = (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-3-2)) , (P.S.source-leg , tt)))
origin-1-3-0-16 : P.T.origin tree-1-3-0 occ-1-3-0-16 ≡ input s32
origin-1-3-0-16 = refl
transport-1-3-0-16 : P.T.origin tree-0-2-1 (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-2-3)) , (P.S.source-leg , tt))) ≡ input (swap s32)
transport-1-3-0-16 = refl
occ-1-3-0-17 : P.T.Occurrence tree-1-3-0
occ-1-3-0-17 = (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-3-2)) , (P.S.target-leg , tt)))
origin-1-3-0-17 : P.T.origin tree-1-3-0 occ-1-3-0-17 ≡ input s32
origin-1-3-0-17 = refl
transport-1-3-0-17 : P.T.origin tree-0-2-1 (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-2-3)) , (P.S.target-leg , tt))) ≡ input (swap s32)
transport-1-3-0-17 = refl
occ-1-3-0-18 : P.T.Occurrence tree-1-3-0
occ-1-3-0-18 = (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-1-3-0-18 : P.T.origin tree-1-3-0 occ-1-3-0-18 ≡ input s13
origin-1-3-0-18 = refl
transport-1-3-0-18 : P.T.origin tree-0-2-1 (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-1-3-0-18 = refl
occ-1-3-0-19 : P.T.Occurrence tree-1-3-0
occ-1-3-0-19 = (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-1-3-0-19 : P.T.origin tree-1-3-0 occ-1-3-0-19 ≡ input s13
origin-1-3-0-19 = refl
transport-1-3-0-19 : P.T.origin tree-0-2-1 (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-1-3-0-19 = refl
occ-1-3-0-20 : P.T.Occurrence tree-1-3-0
occ-1-3-0-20 = (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-1-3-0-20 : P.T.origin tree-1-3-0 occ-1-3-0-20 ≡ input s10
origin-1-3-0-20 = refl
transport-1-3-0-20 : P.T.origin tree-0-2-1 (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s10)
transport-1-3-0-20 = refl
occ-1-3-0-21 : P.T.Occurrence tree-1-3-0
occ-1-3-0-21 = (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-1-3-0-21 : P.T.origin tree-1-3-0 occ-1-3-0-21 ≡ input s20
origin-1-3-0-21 = refl
transport-1-3-0-21 : P.T.origin tree-0-2-1 (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-1-3-0-21 = refl
occ-1-3-0-22 : P.T.Occurrence tree-1-3-0
occ-1-3-0-22 = (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-1-3-0-22 : P.T.origin tree-1-3-0 occ-1-3-0-22 ≡ input s30
origin-1-3-0-22 = refl
transport-1-3-0-22 : P.T.origin tree-0-2-1 (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s30)
transport-1-3-0-22 = refl
occ-1-3-0-23 : P.T.Occurrence tree-1-3-0
occ-1-3-0-23 = (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-1-3-0-23 : P.T.origin tree-1-3-0 occ-1-3-0-23 ≡ input s20
origin-1-3-0-23 = refl
transport-1-3-0-23 : P.T.origin tree-0-2-1 (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-1-3-0-23 = refl
occ-1-3-0-24 : P.T.Occurrence tree-1-3-0
occ-1-3-0-24 = (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.source-leg , tt)))
origin-1-3-0-24 : P.T.origin tree-1-3-0 occ-1-3-0-24 ≡ input s31
origin-1-3-0-24 = refl
transport-1-3-0-24 : P.T.origin tree-0-2-1 (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-1-3-0-24 = refl
occ-1-3-0-25 : P.T.Occurrence tree-1-3-0
occ-1-3-0-25 = (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.target-leg , tt)))
origin-1-3-0-25 : P.T.origin tree-1-3-0 occ-1-3-0-25 ≡ input s01
origin-1-3-0-25 = refl
transport-1-3-0-25 : P.T.origin tree-0-2-1 (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.target-leg , tt))) ≡ input (swap s01)
transport-1-3-0-25 = refl
occ-1-3-0-26 : P.T.Occurrence tree-1-3-0
occ-1-3-0-26 = (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.source-leg , tt)))
origin-1-3-0-26 : P.T.origin tree-1-3-0 occ-1-3-0-26 ≡ input s31
origin-1-3-0-26 = refl
transport-1-3-0-26 : P.T.origin tree-0-2-1 (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-1-3-0-26 = refl
occ-1-3-0-27 : P.T.Occurrence tree-1-3-0
occ-1-3-0-27 = (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.target-leg , tt)))
origin-1-3-0-27 : P.T.origin tree-1-3-0 occ-1-3-0-27 ≡ input s21
origin-1-3-0-27 = refl
transport-1-3-0-27 : P.T.origin tree-0-2-1 (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.target-leg , tt))) ≡ input (swap s21)
transport-1-3-0-27 = refl
occ-1-3-0-28 : P.T.Occurrence tree-1-3-0
occ-1-3-0-28 = (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-1-3-0-28 : P.T.origin tree-1-3-0 occ-1-3-0-28 ≡ input s12
origin-1-3-0-28 = refl
transport-1-3-0-28 : P.T.origin tree-0-2-1 (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s12)
transport-1-3-0-28 = refl
occ-1-3-0-29 : P.T.Occurrence tree-1-3-0
occ-1-3-0-29 = (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-1-3-0-29 : P.T.origin tree-1-3-0 occ-1-3-0-29 ≡ input s02
origin-1-3-0-29 = refl
transport-1-3-0-29 : P.T.origin tree-0-2-1 (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-1-3-0-29 = refl
occ-1-3-0-30 : P.T.Occurrence tree-1-3-0
occ-1-3-0-30 = (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-1-3-0-30 : P.T.origin tree-1-3-0 occ-1-3-0-30 ≡ input s32
origin-1-3-0-30 = refl
transport-1-3-0-30 : P.T.origin tree-0-2-1 (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s32)
transport-1-3-0-30 = refl
occ-1-3-0-31 : P.T.Occurrence tree-1-3-0
occ-1-3-0-31 = (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-1-3-0-31 : P.T.origin tree-1-3-0 occ-1-3-0-31 ≡ input s02
origin-1-3-0-31 = refl
transport-1-3-0-31 : P.T.origin tree-0-2-1 (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-1-3-0-31 = refl
occ-1-3-0-32 : P.T.Occurrence tree-1-3-0
occ-1-3-0-32 = (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.source-leg , tt)))
origin-1-3-0-32 : P.T.origin tree-1-3-0 occ-1-3-0-32 ≡ input s13
origin-1-3-0-32 = refl
transport-1-3-0-32 : P.T.origin tree-0-2-1 (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-1-3-0-32 = refl
occ-1-3-0-33 : P.T.Occurrence tree-1-3-0
occ-1-3-0-33 = (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.target-leg , tt)))
origin-1-3-0-33 : P.T.origin tree-1-3-0 occ-1-3-0-33 ≡ input s03
origin-1-3-0-33 = refl
transport-1-3-0-33 : P.T.origin tree-0-2-1 (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.target-leg , tt))) ≡ input (swap s03)
transport-1-3-0-33 = refl
occ-1-3-0-34 : P.T.Occurrence tree-1-3-0
occ-1-3-0-34 = (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.source-leg , tt)))
origin-1-3-0-34 : P.T.origin tree-1-3-0 occ-1-3-0-34 ≡ input s13
origin-1-3-0-34 = refl
transport-1-3-0-34 : P.T.origin tree-0-2-1 (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-1-3-0-34 = refl
occ-1-3-0-35 : P.T.Occurrence tree-1-3-0
occ-1-3-0-35 = (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.target-leg , tt)))
origin-1-3-0-35 : P.T.origin tree-1-3-0 occ-1-3-0-35 ≡ input s23
origin-1-3-0-35 = refl
transport-1-3-0-35 : P.T.origin tree-0-2-1 (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.target-leg , tt))) ≡ input (swap s23)
transport-1-3-0-35 = refl
occ-1-3-0-36 : P.T.Occurrence tree-1-3-0
occ-1-3-0-36 = (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-1-3-0-36 : P.T.origin tree-1-3-0 occ-1-3-0-36 ≡ input s10
origin-1-3-0-36 = refl
transport-1-3-0-36 : P.T.origin tree-0-2-1 (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s10)
transport-1-3-0-36 = refl
occ-1-3-0-37 : P.T.Occurrence tree-1-3-0
occ-1-3-0-37 = (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-1-3-0-37 : P.T.origin tree-1-3-0 occ-1-3-0-37 ≡ input s20
origin-1-3-0-37 = refl
transport-1-3-0-37 : P.T.origin tree-0-2-1 (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-1-3-0-37 = refl
occ-1-3-0-38 : P.T.Occurrence tree-1-3-0
occ-1-3-0-38 = (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-1-3-0-38 : P.T.origin tree-1-3-0 occ-1-3-0-38 ≡ input s30
origin-1-3-0-38 = refl
transport-1-3-0-38 : P.T.origin tree-0-2-1 (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s30)
transport-1-3-0-38 = refl
occ-1-3-0-39 : P.T.Occurrence tree-1-3-0
occ-1-3-0-39 = (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-1-3-0-39 : P.T.origin tree-1-3-0 occ-1-3-0-39 ≡ input s20
origin-1-3-0-39 = refl
transport-1-3-0-39 : P.T.origin tree-0-2-1 (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-1-3-0-39 = refl
occ-1-3-0-40 : P.T.Occurrence tree-1-3-0
occ-1-3-0-40 = (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.source-leg , tt)))
origin-1-3-0-40 : P.T.origin tree-1-3-0 occ-1-3-0-40 ≡ input s31
origin-1-3-0-40 = refl
transport-1-3-0-40 : P.T.origin tree-0-2-1 (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-1-3-0-40 = refl
occ-1-3-0-41 : P.T.Occurrence tree-1-3-0
occ-1-3-0-41 = (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.target-leg , tt)))
origin-1-3-0-41 : P.T.origin tree-1-3-0 occ-1-3-0-41 ≡ input s01
origin-1-3-0-41 = refl
transport-1-3-0-41 : P.T.origin tree-0-2-1 (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.target-leg , tt))) ≡ input (swap s01)
transport-1-3-0-41 = refl
occ-1-3-0-42 : P.T.Occurrence tree-1-3-0
occ-1-3-0-42 = (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.source-leg , tt)))
origin-1-3-0-42 : P.T.origin tree-1-3-0 occ-1-3-0-42 ≡ input s31
origin-1-3-0-42 = refl
transport-1-3-0-42 : P.T.origin tree-0-2-1 (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-1-3-0-42 = refl
occ-1-3-0-43 : P.T.Occurrence tree-1-3-0
occ-1-3-0-43 = (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.target-leg , tt)))
origin-1-3-0-43 : P.T.origin tree-1-3-0 occ-1-3-0-43 ≡ input s21
origin-1-3-0-43 = refl
transport-1-3-0-43 : P.T.origin tree-0-2-1 (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.target-leg , tt))) ≡ input (swap s21)
transport-1-3-0-43 = refl
occ-1-3-0-44 : P.T.Occurrence tree-1-3-0
occ-1-3-0-44 = (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-1-3-0-44 : P.T.origin tree-1-3-0 occ-1-3-0-44 ≡ input s12
origin-1-3-0-44 = refl
transport-1-3-0-44 : P.T.origin tree-0-2-1 (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s12)
transport-1-3-0-44 = refl
occ-1-3-0-45 : P.T.Occurrence tree-1-3-0
occ-1-3-0-45 = (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-1-3-0-45 : P.T.origin tree-1-3-0 occ-1-3-0-45 ≡ input s02
origin-1-3-0-45 = refl
transport-1-3-0-45 : P.T.origin tree-0-2-1 (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-1-3-0-45 = refl
occ-1-3-0-46 : P.T.Occurrence tree-1-3-0
occ-1-3-0-46 = (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-1-3-0-46 : P.T.origin tree-1-3-0 occ-1-3-0-46 ≡ input s32
origin-1-3-0-46 = refl
transport-1-3-0-46 : P.T.origin tree-0-2-1 (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s32)
transport-1-3-0-46 = refl
occ-1-3-0-47 : P.T.Occurrence tree-1-3-0
occ-1-3-0-47 = (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-1-3-0-47 : P.T.origin tree-1-3-0 occ-1-3-0-47 ≡ input s02
origin-1-3-0-47 = refl
transport-1-3-0-47 : P.T.origin tree-0-2-1 (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-1-3-0-47 = refl
occ-1-3-0-48 : P.T.Occurrence tree-1-3-0
occ-1-3-0-48 = (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.source-leg , tt)))
origin-1-3-0-48 : P.T.origin tree-1-3-0 occ-1-3-0-48 ≡ input s13
origin-1-3-0-48 = refl
transport-1-3-0-48 : P.T.origin tree-0-2-1 (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-1-3-0-48 = refl
occ-1-3-0-49 : P.T.Occurrence tree-1-3-0
occ-1-3-0-49 = (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.target-leg , tt)))
origin-1-3-0-49 : P.T.origin tree-1-3-0 occ-1-3-0-49 ≡ input s03
origin-1-3-0-49 = refl
transport-1-3-0-49 : P.T.origin tree-0-2-1 (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.target-leg , tt))) ≡ input (swap s03)
transport-1-3-0-49 = refl
occ-1-3-0-50 : P.T.Occurrence tree-1-3-0
occ-1-3-0-50 = (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.source-leg , tt)))
origin-1-3-0-50 : P.T.origin tree-1-3-0 occ-1-3-0-50 ≡ input s13
origin-1-3-0-50 = refl
transport-1-3-0-50 : P.T.origin tree-0-2-1 (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-1-3-0-50 = refl
occ-1-3-0-51 : P.T.Occurrence tree-1-3-0
occ-1-3-0-51 = (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.target-leg , tt)))
origin-1-3-0-51 : P.T.origin tree-1-3-0 occ-1-3-0-51 ≡ input s23
origin-1-3-0-51 = refl
transport-1-3-0-51 : P.T.origin tree-0-2-1 (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.target-leg , tt))) ≡ input (swap s23)
transport-1-3-0-51 = refl
occ-1-3-0-52 : P.T.Occurrence tree-1-3-0
occ-1-3-0-52 = (P.S.full-source , (P.S.first-port , tt))
origin-1-3-0-52 : P.T.origin tree-1-3-0 occ-1-3-0-52 ≡ input s12
origin-1-3-0-52 = refl
transport-1-3-0-52 : P.T.origin tree-0-2-1 (P.S.full-source , (P.S.first-port , tt)) ≡ input (swap s12)
transport-1-3-0-52 = refl
occ-1-3-0-53 : P.T.Occurrence tree-1-3-0
occ-1-3-0-53 = (P.S.full-source , (P.S.middle-port , tt))
origin-1-3-0-53 : P.T.origin tree-1-3-0 occ-1-3-0-53 ≡ input s32
origin-1-3-0-53 = refl
transport-1-3-0-53 : P.T.origin tree-0-2-1 (P.S.full-source , (P.S.middle-port , tt)) ≡ input (swap s32)
transport-1-3-0-53 = refl
occ-1-3-0-54 : P.T.Occurrence tree-1-3-0
occ-1-3-0-54 = (P.S.full-source , (P.S.final-port , tt))
origin-1-3-0-54 : P.T.origin tree-1-3-0 occ-1-3-0-54 ≡ input s02
origin-1-3-0-54 = refl
transport-1-3-0-54 : P.T.origin tree-0-2-1 (P.S.full-source , (P.S.final-port , tt)) ≡ input (swap s02)
transport-1-3-0-54 = refl
selected-source-1-3-0-AB : P.S.ab-index {a = C.q7} {b = C.q7} {c = C.q0} F.triple-1-3-0 ≡ (c1 , (F.vp-1-2 , F.vp-3-2))
selected-source-1-3-0-AB = refl
selected-target-1-3-0-AB : P.S.ab-index {a = C.q0} {b = C.q0} {c = C.q7} F.triple-0-2-1 ≡ (m1 , (F.vp-0-3 , F.vp-2-3))
selected-target-1-3-0-AB = refl
selected-source-1-3-0-BC : P.S.bc-index {a = C.q7} {b = C.q7} {c = C.q0} F.triple-1-3-0 ≡ (c1 , (F.vp-3-2 , F.vp-0-2))
selected-source-1-3-0-BC = refl
selected-target-1-3-0-BC : P.S.bc-index {a = C.q0} {b = C.q0} {c = C.q7} F.triple-0-2-1 ≡ (m1 , (F.vp-2-3 , F.vp-1-3))
selected-target-1-3-0-BC = refl
selected-source-1-3-0-AC : P.S.ac-index {a = C.q7} {b = C.q7} {c = C.q0} F.triple-1-3-0 ≡ (c1 , (F.vp-1-2 , F.vp-0-2))
selected-source-1-3-0-AC = refl
selected-target-1-3-0-AC : P.S.ac-index {a = C.q0} {b = C.q0} {c = C.q7} F.triple-0-2-1 ≡ (m1 , (F.vp-0-3 , F.vp-1-3))
selected-target-1-3-0-AC = refl
occ-1-3-2-0 : P.T.Occurrence tree-1-3-2
occ-1-3-2-0 = (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-1-0)) , (P.S.source-leg , tt)))
origin-1-3-2-0 : P.T.origin tree-1-3-2 occ-1-3-2-0 ≡ input s10
origin-1-3-2-0 = refl
transport-1-3-2-0 : P.T.origin tree-0-2-3 (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-0-1)) , (P.S.source-leg , tt))) ≡ input (swap s10)
transport-1-3-2-0 = refl
occ-1-3-2-1 : P.T.Occurrence tree-1-3-2
occ-1-3-2-1 = (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-1-0)) , (P.S.target-leg , tt)))
origin-1-3-2-1 : P.T.origin tree-1-3-2 occ-1-3-2-1 ≡ input s10
origin-1-3-2-1 = refl
transport-1-3-2-1 : P.T.origin tree-0-2-3 (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-0-1)) , (P.S.target-leg , tt))) ≡ input (swap s10)
transport-1-3-2-1 = refl
occ-1-3-2-2 : P.T.Occurrence tree-1-3-2
occ-1-3-2-2 = (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.source-leg , tt)))
origin-1-3-2-2 : P.T.origin tree-1-3-2 occ-1-3-2-2 ≡ input s10
origin-1-3-2-2 = refl
transport-1-3-2-2 : P.T.origin tree-0-2-3 (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.source-leg , tt))) ≡ input (swap s10)
transport-1-3-2-2 = refl
occ-1-3-2-3 : P.T.Occurrence tree-1-3-2
occ-1-3-2-3 = (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.target-leg , tt)))
origin-1-3-2-3 : P.T.origin tree-1-3-2 occ-1-3-2-3 ≡ input s30
origin-1-3-2-3 = refl
transport-1-3-2-3 : P.T.origin tree-0-2-3 (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.target-leg , tt))) ≡ input (swap s30)
transport-1-3-2-3 = refl
occ-1-3-2-4 : P.T.Occurrence tree-1-3-2
occ-1-3-2-4 = (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.source-leg , tt)))
origin-1-3-2-4 : P.T.origin tree-1-3-2 occ-1-3-2-4 ≡ input s30
origin-1-3-2-4 = refl
transport-1-3-2-4 : P.T.origin tree-0-2-3 (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.source-leg , tt))) ≡ input (swap s30)
transport-1-3-2-4 = refl
occ-1-3-2-5 : P.T.Occurrence tree-1-3-2
occ-1-3-2-5 = (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.target-leg , tt)))
origin-1-3-2-5 : P.T.origin tree-1-3-2 occ-1-3-2-5 ≡ input s10
origin-1-3-2-5 = refl
transport-1-3-2-5 : P.T.origin tree-0-2-3 (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.target-leg , tt))) ≡ input (swap s10)
transport-1-3-2-5 = refl
occ-1-3-2-6 : P.T.Occurrence tree-1-3-2
occ-1-3-2-6 = (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-3-0)) , (P.S.source-leg , tt)))
origin-1-3-2-6 : P.T.origin tree-1-3-2 occ-1-3-2-6 ≡ input s30
origin-1-3-2-6 = refl
transport-1-3-2-6 : P.T.origin tree-0-2-3 (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-2-1)) , (P.S.source-leg , tt))) ≡ input (swap s30)
transport-1-3-2-6 = refl
occ-1-3-2-7 : P.T.Occurrence tree-1-3-2
occ-1-3-2-7 = (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-3-0)) , (P.S.target-leg , tt)))
origin-1-3-2-7 : P.T.origin tree-1-3-2 occ-1-3-2-7 ≡ input s30
origin-1-3-2-7 = refl
transport-1-3-2-7 : P.T.origin tree-0-2-3 (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-2-1)) , (P.S.target-leg , tt))) ≡ input (swap s30)
transport-1-3-2-7 = refl
occ-1-3-2-8 : P.T.Occurrence tree-1-3-2
occ-1-3-2-8 = (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-1-3-2-8 : P.T.origin tree-1-3-2 occ-1-3-2-8 ≡ input s31
origin-1-3-2-8 = refl
transport-1-3-2-8 : P.T.origin tree-0-2-3 (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-1-3-2-8 = refl
occ-1-3-2-9 : P.T.Occurrence tree-1-3-2
occ-1-3-2-9 = (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-1-3-2-9 : P.T.origin tree-1-3-2 occ-1-3-2-9 ≡ input s31
origin-1-3-2-9 = refl
transport-1-3-2-9 : P.T.origin tree-0-2-3 (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-1-3-2-9 = refl
occ-1-3-2-10 : P.T.Occurrence tree-1-3-2
occ-1-3-2-10 = (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-1-2)) , (P.S.source-leg , tt)))
origin-1-3-2-10 : P.T.origin tree-1-3-2 occ-1-3-2-10 ≡ input s12
origin-1-3-2-10 = refl
transport-1-3-2-10 : P.T.origin tree-0-2-3 (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-0-3)) , (P.S.source-leg , tt))) ≡ input (swap s12)
transport-1-3-2-10 = refl
occ-1-3-2-11 : P.T.Occurrence tree-1-3-2
occ-1-3-2-11 = (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-1-2)) , (P.S.target-leg , tt)))
origin-1-3-2-11 : P.T.origin tree-1-3-2 occ-1-3-2-11 ≡ input s12
origin-1-3-2-11 = refl
transport-1-3-2-11 : P.T.origin tree-0-2-3 (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-0-3)) , (P.S.target-leg , tt))) ≡ input (swap s12)
transport-1-3-2-11 = refl
occ-1-3-2-12 : P.T.Occurrence tree-1-3-2
occ-1-3-2-12 = (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.source-leg , tt)))
origin-1-3-2-12 : P.T.origin tree-1-3-2 occ-1-3-2-12 ≡ input s12
origin-1-3-2-12 = refl
transport-1-3-2-12 : P.T.origin tree-0-2-3 (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.source-leg , tt))) ≡ input (swap s12)
transport-1-3-2-12 = refl
occ-1-3-2-13 : P.T.Occurrence tree-1-3-2
occ-1-3-2-13 = (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.target-leg , tt)))
origin-1-3-2-13 : P.T.origin tree-1-3-2 occ-1-3-2-13 ≡ input s32
origin-1-3-2-13 = refl
transport-1-3-2-13 : P.T.origin tree-0-2-3 (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.target-leg , tt))) ≡ input (swap s32)
transport-1-3-2-13 = refl
occ-1-3-2-14 : P.T.Occurrence tree-1-3-2
occ-1-3-2-14 = (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.source-leg , tt)))
origin-1-3-2-14 : P.T.origin tree-1-3-2 occ-1-3-2-14 ≡ input s32
origin-1-3-2-14 = refl
transport-1-3-2-14 : P.T.origin tree-0-2-3 (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.source-leg , tt))) ≡ input (swap s32)
transport-1-3-2-14 = refl
occ-1-3-2-15 : P.T.Occurrence tree-1-3-2
occ-1-3-2-15 = (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.target-leg , tt)))
origin-1-3-2-15 : P.T.origin tree-1-3-2 occ-1-3-2-15 ≡ input s12
origin-1-3-2-15 = refl
transport-1-3-2-15 : P.T.origin tree-0-2-3 (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.target-leg , tt))) ≡ input (swap s12)
transport-1-3-2-15 = refl
occ-1-3-2-16 : P.T.Occurrence tree-1-3-2
occ-1-3-2-16 = (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-3-2)) , (P.S.source-leg , tt)))
origin-1-3-2-16 : P.T.origin tree-1-3-2 occ-1-3-2-16 ≡ input s32
origin-1-3-2-16 = refl
transport-1-3-2-16 : P.T.origin tree-0-2-3 (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-2-3)) , (P.S.source-leg , tt))) ≡ input (swap s32)
transport-1-3-2-16 = refl
occ-1-3-2-17 : P.T.Occurrence tree-1-3-2
occ-1-3-2-17 = (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-3-2)) , (P.S.target-leg , tt)))
origin-1-3-2-17 : P.T.origin tree-1-3-2 occ-1-3-2-17 ≡ input s32
origin-1-3-2-17 = refl
transport-1-3-2-17 : P.T.origin tree-0-2-3 (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-2-3)) , (P.S.target-leg , tt))) ≡ input (swap s32)
transport-1-3-2-17 = refl
occ-1-3-2-18 : P.T.Occurrence tree-1-3-2
occ-1-3-2-18 = (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-1-3-2-18 : P.T.origin tree-1-3-2 occ-1-3-2-18 ≡ input s13
origin-1-3-2-18 = refl
transport-1-3-2-18 : P.T.origin tree-0-2-3 (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-1-3-2-18 = refl
occ-1-3-2-19 : P.T.Occurrence tree-1-3-2
occ-1-3-2-19 = (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-1-3-2-19 : P.T.origin tree-1-3-2 occ-1-3-2-19 ≡ input s13
origin-1-3-2-19 = refl
transport-1-3-2-19 : P.T.origin tree-0-2-3 (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-1-3-2-19 = refl
occ-1-3-2-20 : P.T.Occurrence tree-1-3-2
occ-1-3-2-20 = (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-1-3-2-20 : P.T.origin tree-1-3-2 occ-1-3-2-20 ≡ input s10
origin-1-3-2-20 = refl
transport-1-3-2-20 : P.T.origin tree-0-2-3 (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s10)
transport-1-3-2-20 = refl
occ-1-3-2-21 : P.T.Occurrence tree-1-3-2
occ-1-3-2-21 = (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-1-3-2-21 : P.T.origin tree-1-3-2 occ-1-3-2-21 ≡ input s20
origin-1-3-2-21 = refl
transport-1-3-2-21 : P.T.origin tree-0-2-3 (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-1-3-2-21 = refl
occ-1-3-2-22 : P.T.Occurrence tree-1-3-2
occ-1-3-2-22 = (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-1-3-2-22 : P.T.origin tree-1-3-2 occ-1-3-2-22 ≡ input s30
origin-1-3-2-22 = refl
transport-1-3-2-22 : P.T.origin tree-0-2-3 (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s30)
transport-1-3-2-22 = refl
occ-1-3-2-23 : P.T.Occurrence tree-1-3-2
occ-1-3-2-23 = (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-1-3-2-23 : P.T.origin tree-1-3-2 occ-1-3-2-23 ≡ input s20
origin-1-3-2-23 = refl
transport-1-3-2-23 : P.T.origin tree-0-2-3 (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-1-3-2-23 = refl
occ-1-3-2-24 : P.T.Occurrence tree-1-3-2
occ-1-3-2-24 = (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.source-leg , tt)))
origin-1-3-2-24 : P.T.origin tree-1-3-2 occ-1-3-2-24 ≡ input s31
origin-1-3-2-24 = refl
transport-1-3-2-24 : P.T.origin tree-0-2-3 (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-1-3-2-24 = refl
occ-1-3-2-25 : P.T.Occurrence tree-1-3-2
occ-1-3-2-25 = (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.target-leg , tt)))
origin-1-3-2-25 : P.T.origin tree-1-3-2 occ-1-3-2-25 ≡ input s01
origin-1-3-2-25 = refl
transport-1-3-2-25 : P.T.origin tree-0-2-3 (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.target-leg , tt))) ≡ input (swap s01)
transport-1-3-2-25 = refl
occ-1-3-2-26 : P.T.Occurrence tree-1-3-2
occ-1-3-2-26 = (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.source-leg , tt)))
origin-1-3-2-26 : P.T.origin tree-1-3-2 occ-1-3-2-26 ≡ input s31
origin-1-3-2-26 = refl
transport-1-3-2-26 : P.T.origin tree-0-2-3 (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-1-3-2-26 = refl
occ-1-3-2-27 : P.T.Occurrence tree-1-3-2
occ-1-3-2-27 = (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.target-leg , tt)))
origin-1-3-2-27 : P.T.origin tree-1-3-2 occ-1-3-2-27 ≡ input s21
origin-1-3-2-27 = refl
transport-1-3-2-27 : P.T.origin tree-0-2-3 (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.target-leg , tt))) ≡ input (swap s21)
transport-1-3-2-27 = refl
occ-1-3-2-28 : P.T.Occurrence tree-1-3-2
occ-1-3-2-28 = (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-1-3-2-28 : P.T.origin tree-1-3-2 occ-1-3-2-28 ≡ input s12
origin-1-3-2-28 = refl
transport-1-3-2-28 : P.T.origin tree-0-2-3 (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s12)
transport-1-3-2-28 = refl
occ-1-3-2-29 : P.T.Occurrence tree-1-3-2
occ-1-3-2-29 = (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-1-3-2-29 : P.T.origin tree-1-3-2 occ-1-3-2-29 ≡ input s02
origin-1-3-2-29 = refl
transport-1-3-2-29 : P.T.origin tree-0-2-3 (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-1-3-2-29 = refl
occ-1-3-2-30 : P.T.Occurrence tree-1-3-2
occ-1-3-2-30 = (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-1-3-2-30 : P.T.origin tree-1-3-2 occ-1-3-2-30 ≡ input s32
origin-1-3-2-30 = refl
transport-1-3-2-30 : P.T.origin tree-0-2-3 (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s32)
transport-1-3-2-30 = refl
occ-1-3-2-31 : P.T.Occurrence tree-1-3-2
occ-1-3-2-31 = (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-1-3-2-31 : P.T.origin tree-1-3-2 occ-1-3-2-31 ≡ input s02
origin-1-3-2-31 = refl
transport-1-3-2-31 : P.T.origin tree-0-2-3 (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-1-3-2-31 = refl
occ-1-3-2-32 : P.T.Occurrence tree-1-3-2
occ-1-3-2-32 = (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.source-leg , tt)))
origin-1-3-2-32 : P.T.origin tree-1-3-2 occ-1-3-2-32 ≡ input s13
origin-1-3-2-32 = refl
transport-1-3-2-32 : P.T.origin tree-0-2-3 (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-1-3-2-32 = refl
occ-1-3-2-33 : P.T.Occurrence tree-1-3-2
occ-1-3-2-33 = (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.target-leg , tt)))
origin-1-3-2-33 : P.T.origin tree-1-3-2 occ-1-3-2-33 ≡ input s03
origin-1-3-2-33 = refl
transport-1-3-2-33 : P.T.origin tree-0-2-3 (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.target-leg , tt))) ≡ input (swap s03)
transport-1-3-2-33 = refl
occ-1-3-2-34 : P.T.Occurrence tree-1-3-2
occ-1-3-2-34 = (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.source-leg , tt)))
origin-1-3-2-34 : P.T.origin tree-1-3-2 occ-1-3-2-34 ≡ input s13
origin-1-3-2-34 = refl
transport-1-3-2-34 : P.T.origin tree-0-2-3 (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-1-3-2-34 = refl
occ-1-3-2-35 : P.T.Occurrence tree-1-3-2
occ-1-3-2-35 = (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.target-leg , tt)))
origin-1-3-2-35 : P.T.origin tree-1-3-2 occ-1-3-2-35 ≡ input s23
origin-1-3-2-35 = refl
transport-1-3-2-35 : P.T.origin tree-0-2-3 (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.target-leg , tt))) ≡ input (swap s23)
transport-1-3-2-35 = refl
occ-1-3-2-36 : P.T.Occurrence tree-1-3-2
occ-1-3-2-36 = (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-1-3-2-36 : P.T.origin tree-1-3-2 occ-1-3-2-36 ≡ input s10
origin-1-3-2-36 = refl
transport-1-3-2-36 : P.T.origin tree-0-2-3 (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s10)
transport-1-3-2-36 = refl
occ-1-3-2-37 : P.T.Occurrence tree-1-3-2
occ-1-3-2-37 = (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-1-3-2-37 : P.T.origin tree-1-3-2 occ-1-3-2-37 ≡ input s20
origin-1-3-2-37 = refl
transport-1-3-2-37 : P.T.origin tree-0-2-3 (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-1-3-2-37 = refl
occ-1-3-2-38 : P.T.Occurrence tree-1-3-2
occ-1-3-2-38 = (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-1-3-2-38 : P.T.origin tree-1-3-2 occ-1-3-2-38 ≡ input s30
origin-1-3-2-38 = refl
transport-1-3-2-38 : P.T.origin tree-0-2-3 (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s30)
transport-1-3-2-38 = refl
occ-1-3-2-39 : P.T.Occurrence tree-1-3-2
occ-1-3-2-39 = (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-1-3-2-39 : P.T.origin tree-1-3-2 occ-1-3-2-39 ≡ input s20
origin-1-3-2-39 = refl
transport-1-3-2-39 : P.T.origin tree-0-2-3 (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-1-3-2-39 = refl
occ-1-3-2-40 : P.T.Occurrence tree-1-3-2
occ-1-3-2-40 = (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.source-leg , tt)))
origin-1-3-2-40 : P.T.origin tree-1-3-2 occ-1-3-2-40 ≡ input s31
origin-1-3-2-40 = refl
transport-1-3-2-40 : P.T.origin tree-0-2-3 (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-1-3-2-40 = refl
occ-1-3-2-41 : P.T.Occurrence tree-1-3-2
occ-1-3-2-41 = (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.target-leg , tt)))
origin-1-3-2-41 : P.T.origin tree-1-3-2 occ-1-3-2-41 ≡ input s01
origin-1-3-2-41 = refl
transport-1-3-2-41 : P.T.origin tree-0-2-3 (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.target-leg , tt))) ≡ input (swap s01)
transport-1-3-2-41 = refl
occ-1-3-2-42 : P.T.Occurrence tree-1-3-2
occ-1-3-2-42 = (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.source-leg , tt)))
origin-1-3-2-42 : P.T.origin tree-1-3-2 occ-1-3-2-42 ≡ input s31
origin-1-3-2-42 = refl
transport-1-3-2-42 : P.T.origin tree-0-2-3 (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-1-3-2-42 = refl
occ-1-3-2-43 : P.T.Occurrence tree-1-3-2
occ-1-3-2-43 = (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.target-leg , tt)))
origin-1-3-2-43 : P.T.origin tree-1-3-2 occ-1-3-2-43 ≡ input s21
origin-1-3-2-43 = refl
transport-1-3-2-43 : P.T.origin tree-0-2-3 (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.target-leg , tt))) ≡ input (swap s21)
transport-1-3-2-43 = refl
occ-1-3-2-44 : P.T.Occurrence tree-1-3-2
occ-1-3-2-44 = (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-1-3-2-44 : P.T.origin tree-1-3-2 occ-1-3-2-44 ≡ input s12
origin-1-3-2-44 = refl
transport-1-3-2-44 : P.T.origin tree-0-2-3 (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s12)
transport-1-3-2-44 = refl
occ-1-3-2-45 : P.T.Occurrence tree-1-3-2
occ-1-3-2-45 = (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-1-3-2-45 : P.T.origin tree-1-3-2 occ-1-3-2-45 ≡ input s02
origin-1-3-2-45 = refl
transport-1-3-2-45 : P.T.origin tree-0-2-3 (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-1-3-2-45 = refl
occ-1-3-2-46 : P.T.Occurrence tree-1-3-2
occ-1-3-2-46 = (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-1-3-2-46 : P.T.origin tree-1-3-2 occ-1-3-2-46 ≡ input s32
origin-1-3-2-46 = refl
transport-1-3-2-46 : P.T.origin tree-0-2-3 (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s32)
transport-1-3-2-46 = refl
occ-1-3-2-47 : P.T.Occurrence tree-1-3-2
occ-1-3-2-47 = (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-1-3-2-47 : P.T.origin tree-1-3-2 occ-1-3-2-47 ≡ input s02
origin-1-3-2-47 = refl
transport-1-3-2-47 : P.T.origin tree-0-2-3 (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-1-3-2-47 = refl
occ-1-3-2-48 : P.T.Occurrence tree-1-3-2
occ-1-3-2-48 = (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.source-leg , tt)))
origin-1-3-2-48 : P.T.origin tree-1-3-2 occ-1-3-2-48 ≡ input s13
origin-1-3-2-48 = refl
transport-1-3-2-48 : P.T.origin tree-0-2-3 (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-1-3-2-48 = refl
occ-1-3-2-49 : P.T.Occurrence tree-1-3-2
occ-1-3-2-49 = (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.target-leg , tt)))
origin-1-3-2-49 : P.T.origin tree-1-3-2 occ-1-3-2-49 ≡ input s03
origin-1-3-2-49 = refl
transport-1-3-2-49 : P.T.origin tree-0-2-3 (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.target-leg , tt))) ≡ input (swap s03)
transport-1-3-2-49 = refl
occ-1-3-2-50 : P.T.Occurrence tree-1-3-2
occ-1-3-2-50 = (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.source-leg , tt)))
origin-1-3-2-50 : P.T.origin tree-1-3-2 occ-1-3-2-50 ≡ input s13
origin-1-3-2-50 = refl
transport-1-3-2-50 : P.T.origin tree-0-2-3 (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-1-3-2-50 = refl
occ-1-3-2-51 : P.T.Occurrence tree-1-3-2
occ-1-3-2-51 = (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.target-leg , tt)))
origin-1-3-2-51 : P.T.origin tree-1-3-2 occ-1-3-2-51 ≡ input s23
origin-1-3-2-51 = refl
transport-1-3-2-51 : P.T.origin tree-0-2-3 (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.target-leg , tt))) ≡ input (swap s23)
transport-1-3-2-51 = refl
occ-1-3-2-52 : P.T.Occurrence tree-1-3-2
occ-1-3-2-52 = (P.S.full-source , (P.S.first-port , tt))
origin-1-3-2-52 : P.T.origin tree-1-3-2 occ-1-3-2-52 ≡ input s10
origin-1-3-2-52 = refl
transport-1-3-2-52 : P.T.origin tree-0-2-3 (P.S.full-source , (P.S.first-port , tt)) ≡ input (swap s10)
transport-1-3-2-52 = refl
occ-1-3-2-53 : P.T.Occurrence tree-1-3-2
occ-1-3-2-53 = (P.S.full-source , (P.S.middle-port , tt))
origin-1-3-2-53 : P.T.origin tree-1-3-2 occ-1-3-2-53 ≡ input s30
origin-1-3-2-53 = refl
transport-1-3-2-53 : P.T.origin tree-0-2-3 (P.S.full-source , (P.S.middle-port , tt)) ≡ input (swap s30)
transport-1-3-2-53 = refl
occ-1-3-2-54 : P.T.Occurrence tree-1-3-2
occ-1-3-2-54 = (P.S.full-source , (P.S.final-port , tt))
origin-1-3-2-54 : P.T.origin tree-1-3-2 occ-1-3-2-54 ≡ input s20
origin-1-3-2-54 = refl
transport-1-3-2-54 : P.T.origin tree-0-2-3 (P.S.full-source , (P.S.final-port , tt)) ≡ input (swap s20)
transport-1-3-2-54 = refl
selected-source-1-3-2-AB : P.S.ab-index {a = C.q7} {b = C.q7} {c = C.q0} F.triple-1-3-2 ≡ (c0 , (F.vp-1-0 , F.vp-3-0))
selected-source-1-3-2-AB = refl
selected-target-1-3-2-AB : P.S.ab-index {a = C.q0} {b = C.q0} {c = C.q7} F.triple-0-2-3 ≡ (m0 , (F.vp-0-1 , F.vp-2-1))
selected-target-1-3-2-AB = refl
selected-source-1-3-2-BC : P.S.bc-index {a = C.q7} {b = C.q7} {c = C.q0} F.triple-1-3-2 ≡ (c0 , (F.vp-3-0 , F.vp-2-0))
selected-source-1-3-2-BC = refl
selected-target-1-3-2-BC : P.S.bc-index {a = C.q0} {b = C.q0} {c = C.q7} F.triple-0-2-3 ≡ (m0 , (F.vp-2-1 , F.vp-3-1))
selected-target-1-3-2-BC = refl
selected-source-1-3-2-AC : P.S.ac-index {a = C.q7} {b = C.q7} {c = C.q0} F.triple-1-3-2 ≡ (c0 , (F.vp-1-0 , F.vp-2-0))
selected-source-1-3-2-AC = refl
selected-target-1-3-2-AC : P.S.ac-index {a = C.q0} {b = C.q0} {c = C.q7} F.triple-0-2-3 ≡ (m0 , (F.vp-0-1 , F.vp-3-1))
selected-target-1-3-2-AC = refl
occ-2-0-1-0 : P.T.Occurrence tree-2-0-1
occ-2-0-1-0 = (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-2-0-1-0 : P.T.origin tree-2-0-1 occ-2-0-1-0 ≡ input s20
origin-2-0-1-0 = refl
transport-2-0-1-0 : P.T.origin tree-3-1-0 (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-2-0-1-0 = refl
occ-2-0-1-1 : P.T.Occurrence tree-2-0-1
occ-2-0-1-1 = (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-2-0-1-1 : P.T.origin tree-2-0-1 occ-2-0-1-1 ≡ input s20
origin-2-0-1-1 = refl
transport-2-0-1-1 : P.T.origin tree-3-1-0 (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-2-0-1-1 = refl
occ-2-0-1-2 : P.T.Occurrence tree-2-0-1
occ-2-0-1-2 = (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-0-1)) , (P.S.source-leg , tt)))
origin-2-0-1-2 : P.T.origin tree-2-0-1 occ-2-0-1-2 ≡ input s01
origin-2-0-1-2 = refl
transport-2-0-1-2 : P.T.origin tree-3-1-0 (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-1-0)) , (P.S.source-leg , tt))) ≡ input (swap s01)
transport-2-0-1-2 = refl
occ-2-0-1-3 : P.T.Occurrence tree-2-0-1
occ-2-0-1-3 = (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-0-1)) , (P.S.target-leg , tt)))
origin-2-0-1-3 : P.T.origin tree-2-0-1 occ-2-0-1-3 ≡ input s01
origin-2-0-1-3 = refl
transport-2-0-1-3 : P.T.origin tree-3-1-0 (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-1-0)) , (P.S.target-leg , tt))) ≡ input (swap s01)
transport-2-0-1-3 = refl
occ-2-0-1-4 : P.T.Occurrence tree-2-0-1
occ-2-0-1-4 = (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.source-leg , tt)))
origin-2-0-1-4 : P.T.origin tree-2-0-1 occ-2-0-1-4 ≡ input s01
origin-2-0-1-4 = refl
transport-2-0-1-4 : P.T.origin tree-3-1-0 (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.source-leg , tt))) ≡ input (swap s01)
transport-2-0-1-4 = refl
occ-2-0-1-5 : P.T.Occurrence tree-2-0-1
occ-2-0-1-5 = (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.target-leg , tt)))
origin-2-0-1-5 : P.T.origin tree-2-0-1 occ-2-0-1-5 ≡ input s21
origin-2-0-1-5 = refl
transport-2-0-1-5 : P.T.origin tree-3-1-0 (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.target-leg , tt))) ≡ input (swap s21)
transport-2-0-1-5 = refl
occ-2-0-1-6 : P.T.Occurrence tree-2-0-1
occ-2-0-1-6 = (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.source-leg , tt)))
origin-2-0-1-6 : P.T.origin tree-2-0-1 occ-2-0-1-6 ≡ input s21
origin-2-0-1-6 = refl
transport-2-0-1-6 : P.T.origin tree-3-1-0 (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.source-leg , tt))) ≡ input (swap s21)
transport-2-0-1-6 = refl
occ-2-0-1-7 : P.T.Occurrence tree-2-0-1
occ-2-0-1-7 = (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.target-leg , tt)))
origin-2-0-1-7 : P.T.origin tree-2-0-1 occ-2-0-1-7 ≡ input s01
origin-2-0-1-7 = refl
transport-2-0-1-7 : P.T.origin tree-3-1-0 (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.target-leg , tt))) ≡ input (swap s01)
transport-2-0-1-7 = refl
occ-2-0-1-8 : P.T.Occurrence tree-2-0-1
occ-2-0-1-8 = (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-2-1)) , (P.S.source-leg , tt)))
origin-2-0-1-8 : P.T.origin tree-2-0-1 occ-2-0-1-8 ≡ input s21
origin-2-0-1-8 = refl
transport-2-0-1-8 : P.T.origin tree-3-1-0 (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-3-0)) , (P.S.source-leg , tt))) ≡ input (swap s21)
transport-2-0-1-8 = refl
occ-2-0-1-9 : P.T.Occurrence tree-2-0-1
occ-2-0-1-9 = (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-2-1)) , (P.S.target-leg , tt)))
origin-2-0-1-9 : P.T.origin tree-2-0-1 occ-2-0-1-9 ≡ input s21
origin-2-0-1-9 = refl
transport-2-0-1-9 : P.T.origin tree-3-1-0 (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-3-0)) , (P.S.target-leg , tt))) ≡ input (swap s21)
transport-2-0-1-9 = refl
occ-2-0-1-10 : P.T.Occurrence tree-2-0-1
occ-2-0-1-10 = (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-2-0-1-10 : P.T.origin tree-2-0-1 occ-2-0-1-10 ≡ input s02
origin-2-0-1-10 = refl
transport-2-0-1-10 : P.T.origin tree-3-1-0 (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-2-0-1-10 = refl
occ-2-0-1-11 : P.T.Occurrence tree-2-0-1
occ-2-0-1-11 = (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-2-0-1-11 : P.T.origin tree-2-0-1 occ-2-0-1-11 ≡ input s02
origin-2-0-1-11 = refl
transport-2-0-1-11 : P.T.origin tree-3-1-0 (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-2-0-1-11 = refl
occ-2-0-1-12 : P.T.Occurrence tree-2-0-1
occ-2-0-1-12 = (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-0-3)) , (P.S.source-leg , tt)))
origin-2-0-1-12 : P.T.origin tree-2-0-1 occ-2-0-1-12 ≡ input s03
origin-2-0-1-12 = refl
transport-2-0-1-12 : P.T.origin tree-3-1-0 (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-1-2)) , (P.S.source-leg , tt))) ≡ input (swap s03)
transport-2-0-1-12 = refl
occ-2-0-1-13 : P.T.Occurrence tree-2-0-1
occ-2-0-1-13 = (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-0-3)) , (P.S.target-leg , tt)))
origin-2-0-1-13 : P.T.origin tree-2-0-1 occ-2-0-1-13 ≡ input s03
origin-2-0-1-13 = refl
transport-2-0-1-13 : P.T.origin tree-3-1-0 (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-1-2)) , (P.S.target-leg , tt))) ≡ input (swap s03)
transport-2-0-1-13 = refl
occ-2-0-1-14 : P.T.Occurrence tree-2-0-1
occ-2-0-1-14 = (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.source-leg , tt)))
origin-2-0-1-14 : P.T.origin tree-2-0-1 occ-2-0-1-14 ≡ input s03
origin-2-0-1-14 = refl
transport-2-0-1-14 : P.T.origin tree-3-1-0 (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.source-leg , tt))) ≡ input (swap s03)
transport-2-0-1-14 = refl
occ-2-0-1-15 : P.T.Occurrence tree-2-0-1
occ-2-0-1-15 = (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.target-leg , tt)))
origin-2-0-1-15 : P.T.origin tree-2-0-1 occ-2-0-1-15 ≡ input s23
origin-2-0-1-15 = refl
transport-2-0-1-15 : P.T.origin tree-3-1-0 (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.target-leg , tt))) ≡ input (swap s23)
transport-2-0-1-15 = refl
occ-2-0-1-16 : P.T.Occurrence tree-2-0-1
occ-2-0-1-16 = (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.source-leg , tt)))
origin-2-0-1-16 : P.T.origin tree-2-0-1 occ-2-0-1-16 ≡ input s23
origin-2-0-1-16 = refl
transport-2-0-1-16 : P.T.origin tree-3-1-0 (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.source-leg , tt))) ≡ input (swap s23)
transport-2-0-1-16 = refl
occ-2-0-1-17 : P.T.Occurrence tree-2-0-1
occ-2-0-1-17 = (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.target-leg , tt)))
origin-2-0-1-17 : P.T.origin tree-2-0-1 occ-2-0-1-17 ≡ input s03
origin-2-0-1-17 = refl
transport-2-0-1-17 : P.T.origin tree-3-1-0 (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.target-leg , tt))) ≡ input (swap s03)
transport-2-0-1-17 = refl
occ-2-0-1-18 : P.T.Occurrence tree-2-0-1
occ-2-0-1-18 = (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-2-3)) , (P.S.source-leg , tt)))
origin-2-0-1-18 : P.T.origin tree-2-0-1 occ-2-0-1-18 ≡ input s23
origin-2-0-1-18 = refl
transport-2-0-1-18 : P.T.origin tree-3-1-0 (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-3-2)) , (P.S.source-leg , tt))) ≡ input (swap s23)
transport-2-0-1-18 = refl
occ-2-0-1-19 : P.T.Occurrence tree-2-0-1
occ-2-0-1-19 = (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-2-3)) , (P.S.target-leg , tt)))
origin-2-0-1-19 : P.T.origin tree-2-0-1 occ-2-0-1-19 ≡ input s23
origin-2-0-1-19 = refl
transport-2-0-1-19 : P.T.origin tree-3-1-0 (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-3-2)) , (P.S.target-leg , tt))) ≡ input (swap s23)
transport-2-0-1-19 = refl
occ-2-0-1-20 : P.T.Occurrence tree-2-0-1
occ-2-0-1-20 = (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.source-leg , tt)))
origin-2-0-1-20 : P.T.origin tree-2-0-1 occ-2-0-1-20 ≡ input s20
origin-2-0-1-20 = refl
transport-2-0-1-20 : P.T.origin tree-3-1-0 (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-2-0-1-20 = refl
occ-2-0-1-21 : P.T.Occurrence tree-2-0-1
occ-2-0-1-21 = (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.target-leg , tt)))
origin-2-0-1-21 : P.T.origin tree-2-0-1 occ-2-0-1-21 ≡ input s10
origin-2-0-1-21 = refl
transport-2-0-1-21 : P.T.origin tree-3-1-0 (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.target-leg , tt))) ≡ input (swap s10)
transport-2-0-1-21 = refl
occ-2-0-1-22 : P.T.Occurrence tree-2-0-1
occ-2-0-1-22 = (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.source-leg , tt)))
origin-2-0-1-22 : P.T.origin tree-2-0-1 occ-2-0-1-22 ≡ input s20
origin-2-0-1-22 = refl
transport-2-0-1-22 : P.T.origin tree-3-1-0 (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-2-0-1-22 = refl
occ-2-0-1-23 : P.T.Occurrence tree-2-0-1
occ-2-0-1-23 = (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.target-leg , tt)))
origin-2-0-1-23 : P.T.origin tree-2-0-1 occ-2-0-1-23 ≡ input s30
origin-2-0-1-23 = refl
transport-2-0-1-23 : P.T.origin tree-3-1-0 (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.target-leg , tt))) ≡ input (swap s30)
transport-2-0-1-23 = refl
occ-2-0-1-24 : P.T.Occurrence tree-2-0-1
occ-2-0-1-24 = (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-2-0-1-24 : P.T.origin tree-2-0-1 occ-2-0-1-24 ≡ input s01
origin-2-0-1-24 = refl
transport-2-0-1-24 : P.T.origin tree-3-1-0 (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s01)
transport-2-0-1-24 = refl
occ-2-0-1-25 : P.T.Occurrence tree-2-0-1
occ-2-0-1-25 = (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-2-0-1-25 : P.T.origin tree-2-0-1 occ-2-0-1-25 ≡ input s31
origin-2-0-1-25 = refl
transport-2-0-1-25 : P.T.origin tree-3-1-0 (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-2-0-1-25 = refl
occ-2-0-1-26 : P.T.Occurrence tree-2-0-1
occ-2-0-1-26 = (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-2-0-1-26 : P.T.origin tree-2-0-1 occ-2-0-1-26 ≡ input s21
origin-2-0-1-26 = refl
transport-2-0-1-26 : P.T.origin tree-3-1-0 (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s21)
transport-2-0-1-26 = refl
occ-2-0-1-27 : P.T.Occurrence tree-2-0-1
occ-2-0-1-27 = (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-2-0-1-27 : P.T.origin tree-2-0-1 occ-2-0-1-27 ≡ input s31
origin-2-0-1-27 = refl
transport-2-0-1-27 : P.T.origin tree-3-1-0 (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-2-0-1-27 = refl
occ-2-0-1-28 : P.T.Occurrence tree-2-0-1
occ-2-0-1-28 = (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.source-leg , tt)))
origin-2-0-1-28 : P.T.origin tree-2-0-1 occ-2-0-1-28 ≡ input s02
origin-2-0-1-28 = refl
transport-2-0-1-28 : P.T.origin tree-3-1-0 (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-2-0-1-28 = refl
occ-2-0-1-29 : P.T.Occurrence tree-2-0-1
occ-2-0-1-29 = (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.target-leg , tt)))
origin-2-0-1-29 : P.T.origin tree-2-0-1 occ-2-0-1-29 ≡ input s12
origin-2-0-1-29 = refl
transport-2-0-1-29 : P.T.origin tree-3-1-0 (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.target-leg , tt))) ≡ input (swap s12)
transport-2-0-1-29 = refl
occ-2-0-1-30 : P.T.Occurrence tree-2-0-1
occ-2-0-1-30 = (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.source-leg , tt)))
origin-2-0-1-30 : P.T.origin tree-2-0-1 occ-2-0-1-30 ≡ input s02
origin-2-0-1-30 = refl
transport-2-0-1-30 : P.T.origin tree-3-1-0 (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-2-0-1-30 = refl
occ-2-0-1-31 : P.T.Occurrence tree-2-0-1
occ-2-0-1-31 = (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.target-leg , tt)))
origin-2-0-1-31 : P.T.origin tree-2-0-1 occ-2-0-1-31 ≡ input s32
origin-2-0-1-31 = refl
transport-2-0-1-31 : P.T.origin tree-3-1-0 (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.target-leg , tt))) ≡ input (swap s32)
transport-2-0-1-31 = refl
occ-2-0-1-32 : P.T.Occurrence tree-2-0-1
occ-2-0-1-32 = (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-2-0-1-32 : P.T.origin tree-2-0-1 occ-2-0-1-32 ≡ input s03
origin-2-0-1-32 = refl
transport-2-0-1-32 : P.T.origin tree-3-1-0 (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s03)
transport-2-0-1-32 = refl
occ-2-0-1-33 : P.T.Occurrence tree-2-0-1
occ-2-0-1-33 = (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-2-0-1-33 : P.T.origin tree-2-0-1 occ-2-0-1-33 ≡ input s13
origin-2-0-1-33 = refl
transport-2-0-1-33 : P.T.origin tree-3-1-0 (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-2-0-1-33 = refl
occ-2-0-1-34 : P.T.Occurrence tree-2-0-1
occ-2-0-1-34 = (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-2-0-1-34 : P.T.origin tree-2-0-1 occ-2-0-1-34 ≡ input s23
origin-2-0-1-34 = refl
transport-2-0-1-34 : P.T.origin tree-3-1-0 (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s23)
transport-2-0-1-34 = refl
occ-2-0-1-35 : P.T.Occurrence tree-2-0-1
occ-2-0-1-35 = (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-2-0-1-35 : P.T.origin tree-2-0-1 occ-2-0-1-35 ≡ input s13
origin-2-0-1-35 = refl
transport-2-0-1-35 : P.T.origin tree-3-1-0 (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-2-0-1-35 = refl
occ-2-0-1-36 : P.T.Occurrence tree-2-0-1
occ-2-0-1-36 = (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.source-leg , tt)))
origin-2-0-1-36 : P.T.origin tree-2-0-1 occ-2-0-1-36 ≡ input s20
origin-2-0-1-36 = refl
transport-2-0-1-36 : P.T.origin tree-3-1-0 (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-2-0-1-36 = refl
occ-2-0-1-37 : P.T.Occurrence tree-2-0-1
occ-2-0-1-37 = (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.target-leg , tt)))
origin-2-0-1-37 : P.T.origin tree-2-0-1 occ-2-0-1-37 ≡ input s10
origin-2-0-1-37 = refl
transport-2-0-1-37 : P.T.origin tree-3-1-0 (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.target-leg , tt))) ≡ input (swap s10)
transport-2-0-1-37 = refl
occ-2-0-1-38 : P.T.Occurrence tree-2-0-1
occ-2-0-1-38 = (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.source-leg , tt)))
origin-2-0-1-38 : P.T.origin tree-2-0-1 occ-2-0-1-38 ≡ input s20
origin-2-0-1-38 = refl
transport-2-0-1-38 : P.T.origin tree-3-1-0 (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-2-0-1-38 = refl
occ-2-0-1-39 : P.T.Occurrence tree-2-0-1
occ-2-0-1-39 = (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.target-leg , tt)))
origin-2-0-1-39 : P.T.origin tree-2-0-1 occ-2-0-1-39 ≡ input s30
origin-2-0-1-39 = refl
transport-2-0-1-39 : P.T.origin tree-3-1-0 (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.target-leg , tt))) ≡ input (swap s30)
transport-2-0-1-39 = refl
occ-2-0-1-40 : P.T.Occurrence tree-2-0-1
occ-2-0-1-40 = (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-2-0-1-40 : P.T.origin tree-2-0-1 occ-2-0-1-40 ≡ input s01
origin-2-0-1-40 = refl
transport-2-0-1-40 : P.T.origin tree-3-1-0 (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s01)
transport-2-0-1-40 = refl
occ-2-0-1-41 : P.T.Occurrence tree-2-0-1
occ-2-0-1-41 = (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-2-0-1-41 : P.T.origin tree-2-0-1 occ-2-0-1-41 ≡ input s31
origin-2-0-1-41 = refl
transport-2-0-1-41 : P.T.origin tree-3-1-0 (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-2-0-1-41 = refl
occ-2-0-1-42 : P.T.Occurrence tree-2-0-1
occ-2-0-1-42 = (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-2-0-1-42 : P.T.origin tree-2-0-1 occ-2-0-1-42 ≡ input s21
origin-2-0-1-42 = refl
transport-2-0-1-42 : P.T.origin tree-3-1-0 (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s21)
transport-2-0-1-42 = refl
occ-2-0-1-43 : P.T.Occurrence tree-2-0-1
occ-2-0-1-43 = (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-2-0-1-43 : P.T.origin tree-2-0-1 occ-2-0-1-43 ≡ input s31
origin-2-0-1-43 = refl
transport-2-0-1-43 : P.T.origin tree-3-1-0 (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-2-0-1-43 = refl
occ-2-0-1-44 : P.T.Occurrence tree-2-0-1
occ-2-0-1-44 = (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.source-leg , tt)))
origin-2-0-1-44 : P.T.origin tree-2-0-1 occ-2-0-1-44 ≡ input s02
origin-2-0-1-44 = refl
transport-2-0-1-44 : P.T.origin tree-3-1-0 (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-2-0-1-44 = refl
occ-2-0-1-45 : P.T.Occurrence tree-2-0-1
occ-2-0-1-45 = (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.target-leg , tt)))
origin-2-0-1-45 : P.T.origin tree-2-0-1 occ-2-0-1-45 ≡ input s12
origin-2-0-1-45 = refl
transport-2-0-1-45 : P.T.origin tree-3-1-0 (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.target-leg , tt))) ≡ input (swap s12)
transport-2-0-1-45 = refl
occ-2-0-1-46 : P.T.Occurrence tree-2-0-1
occ-2-0-1-46 = (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.source-leg , tt)))
origin-2-0-1-46 : P.T.origin tree-2-0-1 occ-2-0-1-46 ≡ input s02
origin-2-0-1-46 = refl
transport-2-0-1-46 : P.T.origin tree-3-1-0 (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-2-0-1-46 = refl
occ-2-0-1-47 : P.T.Occurrence tree-2-0-1
occ-2-0-1-47 = (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.target-leg , tt)))
origin-2-0-1-47 : P.T.origin tree-2-0-1 occ-2-0-1-47 ≡ input s32
origin-2-0-1-47 = refl
transport-2-0-1-47 : P.T.origin tree-3-1-0 (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.target-leg , tt))) ≡ input (swap s32)
transport-2-0-1-47 = refl
occ-2-0-1-48 : P.T.Occurrence tree-2-0-1
occ-2-0-1-48 = (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-2-0-1-48 : P.T.origin tree-2-0-1 occ-2-0-1-48 ≡ input s03
origin-2-0-1-48 = refl
transport-2-0-1-48 : P.T.origin tree-3-1-0 (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s03)
transport-2-0-1-48 = refl
occ-2-0-1-49 : P.T.Occurrence tree-2-0-1
occ-2-0-1-49 = (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-2-0-1-49 : P.T.origin tree-2-0-1 occ-2-0-1-49 ≡ input s13
origin-2-0-1-49 = refl
transport-2-0-1-49 : P.T.origin tree-3-1-0 (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-2-0-1-49 = refl
occ-2-0-1-50 : P.T.Occurrence tree-2-0-1
occ-2-0-1-50 = (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-2-0-1-50 : P.T.origin tree-2-0-1 occ-2-0-1-50 ≡ input s23
origin-2-0-1-50 = refl
transport-2-0-1-50 : P.T.origin tree-3-1-0 (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s23)
transport-2-0-1-50 = refl
occ-2-0-1-51 : P.T.Occurrence tree-2-0-1
occ-2-0-1-51 = (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-2-0-1-51 : P.T.origin tree-2-0-1 occ-2-0-1-51 ≡ input s13
origin-2-0-1-51 = refl
transport-2-0-1-51 : P.T.origin tree-3-1-0 (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-2-0-1-51 = refl
occ-2-0-1-52 : P.T.Occurrence tree-2-0-1
occ-2-0-1-52 = (P.S.full-source , (P.S.first-port , tt))
origin-2-0-1-52 : P.T.origin tree-2-0-1 occ-2-0-1-52 ≡ input s23
origin-2-0-1-52 = refl
transport-2-0-1-52 : P.T.origin tree-3-1-0 (P.S.full-source , (P.S.first-port , tt)) ≡ input (swap s23)
transport-2-0-1-52 = refl
occ-2-0-1-53 : P.T.Occurrence tree-2-0-1
occ-2-0-1-53 = (P.S.full-source , (P.S.middle-port , tt))
origin-2-0-1-53 : P.T.origin tree-2-0-1 occ-2-0-1-53 ≡ input s03
origin-2-0-1-53 = refl
transport-2-0-1-53 : P.T.origin tree-3-1-0 (P.S.full-source , (P.S.middle-port , tt)) ≡ input (swap s03)
transport-2-0-1-53 = refl
occ-2-0-1-54 : P.T.Occurrence tree-2-0-1
occ-2-0-1-54 = (P.S.full-source , (P.S.final-port , tt))
origin-2-0-1-54 : P.T.origin tree-2-0-1 occ-2-0-1-54 ≡ input s13
origin-2-0-1-54 = refl
transport-2-0-1-54 : P.T.origin tree-3-1-0 (P.S.full-source , (P.S.final-port , tt)) ≡ input (swap s13)
transport-2-0-1-54 = refl
selected-source-2-0-1-AB : P.S.ab-index {a = C.q0} {b = C.q0} {c = C.q7} F.triple-2-0-1 ≡ (m1 , (F.vp-2-3 , F.vp-0-3))
selected-source-2-0-1-AB = refl
selected-target-2-0-1-AB : P.S.ab-index {a = C.q7} {b = C.q7} {c = C.q0} F.triple-3-1-0 ≡ (c1 , (F.vp-3-2 , F.vp-1-2))
selected-target-2-0-1-AB = refl
selected-source-2-0-1-BC : P.S.bc-index {a = C.q0} {b = C.q0} {c = C.q7} F.triple-2-0-1 ≡ (m1 , (F.vp-0-3 , F.vp-1-3))
selected-source-2-0-1-BC = refl
selected-target-2-0-1-BC : P.S.bc-index {a = C.q7} {b = C.q7} {c = C.q0} F.triple-3-1-0 ≡ (c1 , (F.vp-1-2 , F.vp-0-2))
selected-target-2-0-1-BC = refl
selected-source-2-0-1-AC : P.S.ac-index {a = C.q0} {b = C.q0} {c = C.q7} F.triple-2-0-1 ≡ (m1 , (F.vp-2-3 , F.vp-1-3))
selected-source-2-0-1-AC = refl
selected-target-2-0-1-AC : P.S.ac-index {a = C.q7} {b = C.q7} {c = C.q0} F.triple-3-1-0 ≡ (c1 , (F.vp-3-2 , F.vp-0-2))
selected-target-2-0-1-AC = refl
occ-2-0-3-0 : P.T.Occurrence tree-2-0-3
occ-2-0-3-0 = (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-2-0-3-0 : P.T.origin tree-2-0-3 occ-2-0-3-0 ≡ input s20
origin-2-0-3-0 = refl
transport-2-0-3-0 : P.T.origin tree-3-1-2 (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-2-0-3-0 = refl
occ-2-0-3-1 : P.T.Occurrence tree-2-0-3
occ-2-0-3-1 = (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-2-0-3-1 : P.T.origin tree-2-0-3 occ-2-0-3-1 ≡ input s20
origin-2-0-3-1 = refl
transport-2-0-3-1 : P.T.origin tree-3-1-2 (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-2-0-3-1 = refl
occ-2-0-3-2 : P.T.Occurrence tree-2-0-3
occ-2-0-3-2 = (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-0-1)) , (P.S.source-leg , tt)))
origin-2-0-3-2 : P.T.origin tree-2-0-3 occ-2-0-3-2 ≡ input s01
origin-2-0-3-2 = refl
transport-2-0-3-2 : P.T.origin tree-3-1-2 (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-1-0)) , (P.S.source-leg , tt))) ≡ input (swap s01)
transport-2-0-3-2 = refl
occ-2-0-3-3 : P.T.Occurrence tree-2-0-3
occ-2-0-3-3 = (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-0-1)) , (P.S.target-leg , tt)))
origin-2-0-3-3 : P.T.origin tree-2-0-3 occ-2-0-3-3 ≡ input s01
origin-2-0-3-3 = refl
transport-2-0-3-3 : P.T.origin tree-3-1-2 (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-1-0)) , (P.S.target-leg , tt))) ≡ input (swap s01)
transport-2-0-3-3 = refl
occ-2-0-3-4 : P.T.Occurrence tree-2-0-3
occ-2-0-3-4 = (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.source-leg , tt)))
origin-2-0-3-4 : P.T.origin tree-2-0-3 occ-2-0-3-4 ≡ input s01
origin-2-0-3-4 = refl
transport-2-0-3-4 : P.T.origin tree-3-1-2 (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.source-leg , tt))) ≡ input (swap s01)
transport-2-0-3-4 = refl
occ-2-0-3-5 : P.T.Occurrence tree-2-0-3
occ-2-0-3-5 = (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.target-leg , tt)))
origin-2-0-3-5 : P.T.origin tree-2-0-3 occ-2-0-3-5 ≡ input s21
origin-2-0-3-5 = refl
transport-2-0-3-5 : P.T.origin tree-3-1-2 (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.target-leg , tt))) ≡ input (swap s21)
transport-2-0-3-5 = refl
occ-2-0-3-6 : P.T.Occurrence tree-2-0-3
occ-2-0-3-6 = (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.source-leg , tt)))
origin-2-0-3-6 : P.T.origin tree-2-0-3 occ-2-0-3-6 ≡ input s21
origin-2-0-3-6 = refl
transport-2-0-3-6 : P.T.origin tree-3-1-2 (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.source-leg , tt))) ≡ input (swap s21)
transport-2-0-3-6 = refl
occ-2-0-3-7 : P.T.Occurrence tree-2-0-3
occ-2-0-3-7 = (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.target-leg , tt)))
origin-2-0-3-7 : P.T.origin tree-2-0-3 occ-2-0-3-7 ≡ input s01
origin-2-0-3-7 = refl
transport-2-0-3-7 : P.T.origin tree-3-1-2 (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.target-leg , tt))) ≡ input (swap s01)
transport-2-0-3-7 = refl
occ-2-0-3-8 : P.T.Occurrence tree-2-0-3
occ-2-0-3-8 = (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-2-1)) , (P.S.source-leg , tt)))
origin-2-0-3-8 : P.T.origin tree-2-0-3 occ-2-0-3-8 ≡ input s21
origin-2-0-3-8 = refl
transport-2-0-3-8 : P.T.origin tree-3-1-2 (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-3-0)) , (P.S.source-leg , tt))) ≡ input (swap s21)
transport-2-0-3-8 = refl
occ-2-0-3-9 : P.T.Occurrence tree-2-0-3
occ-2-0-3-9 = (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-2-1)) , (P.S.target-leg , tt)))
origin-2-0-3-9 : P.T.origin tree-2-0-3 occ-2-0-3-9 ≡ input s21
origin-2-0-3-9 = refl
transport-2-0-3-9 : P.T.origin tree-3-1-2 (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-3-0)) , (P.S.target-leg , tt))) ≡ input (swap s21)
transport-2-0-3-9 = refl
occ-2-0-3-10 : P.T.Occurrence tree-2-0-3
occ-2-0-3-10 = (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-2-0-3-10 : P.T.origin tree-2-0-3 occ-2-0-3-10 ≡ input s02
origin-2-0-3-10 = refl
transport-2-0-3-10 : P.T.origin tree-3-1-2 (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-2-0-3-10 = refl
occ-2-0-3-11 : P.T.Occurrence tree-2-0-3
occ-2-0-3-11 = (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-2-0-3-11 : P.T.origin tree-2-0-3 occ-2-0-3-11 ≡ input s02
origin-2-0-3-11 = refl
transport-2-0-3-11 : P.T.origin tree-3-1-2 (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-2-0-3-11 = refl
occ-2-0-3-12 : P.T.Occurrence tree-2-0-3
occ-2-0-3-12 = (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-0-3)) , (P.S.source-leg , tt)))
origin-2-0-3-12 : P.T.origin tree-2-0-3 occ-2-0-3-12 ≡ input s03
origin-2-0-3-12 = refl
transport-2-0-3-12 : P.T.origin tree-3-1-2 (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-1-2)) , (P.S.source-leg , tt))) ≡ input (swap s03)
transport-2-0-3-12 = refl
occ-2-0-3-13 : P.T.Occurrence tree-2-0-3
occ-2-0-3-13 = (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-0-3)) , (P.S.target-leg , tt)))
origin-2-0-3-13 : P.T.origin tree-2-0-3 occ-2-0-3-13 ≡ input s03
origin-2-0-3-13 = refl
transport-2-0-3-13 : P.T.origin tree-3-1-2 (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-1-2)) , (P.S.target-leg , tt))) ≡ input (swap s03)
transport-2-0-3-13 = refl
occ-2-0-3-14 : P.T.Occurrence tree-2-0-3
occ-2-0-3-14 = (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.source-leg , tt)))
origin-2-0-3-14 : P.T.origin tree-2-0-3 occ-2-0-3-14 ≡ input s03
origin-2-0-3-14 = refl
transport-2-0-3-14 : P.T.origin tree-3-1-2 (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.source-leg , tt))) ≡ input (swap s03)
transport-2-0-3-14 = refl
occ-2-0-3-15 : P.T.Occurrence tree-2-0-3
occ-2-0-3-15 = (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.target-leg , tt)))
origin-2-0-3-15 : P.T.origin tree-2-0-3 occ-2-0-3-15 ≡ input s23
origin-2-0-3-15 = refl
transport-2-0-3-15 : P.T.origin tree-3-1-2 (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.target-leg , tt))) ≡ input (swap s23)
transport-2-0-3-15 = refl
occ-2-0-3-16 : P.T.Occurrence tree-2-0-3
occ-2-0-3-16 = (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.source-leg , tt)))
origin-2-0-3-16 : P.T.origin tree-2-0-3 occ-2-0-3-16 ≡ input s23
origin-2-0-3-16 = refl
transport-2-0-3-16 : P.T.origin tree-3-1-2 (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.source-leg , tt))) ≡ input (swap s23)
transport-2-0-3-16 = refl
occ-2-0-3-17 : P.T.Occurrence tree-2-0-3
occ-2-0-3-17 = (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.target-leg , tt)))
origin-2-0-3-17 : P.T.origin tree-2-0-3 occ-2-0-3-17 ≡ input s03
origin-2-0-3-17 = refl
transport-2-0-3-17 : P.T.origin tree-3-1-2 (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.target-leg , tt))) ≡ input (swap s03)
transport-2-0-3-17 = refl
occ-2-0-3-18 : P.T.Occurrence tree-2-0-3
occ-2-0-3-18 = (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-2-3)) , (P.S.source-leg , tt)))
origin-2-0-3-18 : P.T.origin tree-2-0-3 occ-2-0-3-18 ≡ input s23
origin-2-0-3-18 = refl
transport-2-0-3-18 : P.T.origin tree-3-1-2 (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-3-2)) , (P.S.source-leg , tt))) ≡ input (swap s23)
transport-2-0-3-18 = refl
occ-2-0-3-19 : P.T.Occurrence tree-2-0-3
occ-2-0-3-19 = (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-2-3)) , (P.S.target-leg , tt)))
origin-2-0-3-19 : P.T.origin tree-2-0-3 occ-2-0-3-19 ≡ input s23
origin-2-0-3-19 = refl
transport-2-0-3-19 : P.T.origin tree-3-1-2 (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-3-2)) , (P.S.target-leg , tt))) ≡ input (swap s23)
transport-2-0-3-19 = refl
occ-2-0-3-20 : P.T.Occurrence tree-2-0-3
occ-2-0-3-20 = (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.source-leg , tt)))
origin-2-0-3-20 : P.T.origin tree-2-0-3 occ-2-0-3-20 ≡ input s20
origin-2-0-3-20 = refl
transport-2-0-3-20 : P.T.origin tree-3-1-2 (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-2-0-3-20 = refl
occ-2-0-3-21 : P.T.Occurrence tree-2-0-3
occ-2-0-3-21 = (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.target-leg , tt)))
origin-2-0-3-21 : P.T.origin tree-2-0-3 occ-2-0-3-21 ≡ input s10
origin-2-0-3-21 = refl
transport-2-0-3-21 : P.T.origin tree-3-1-2 (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.target-leg , tt))) ≡ input (swap s10)
transport-2-0-3-21 = refl
occ-2-0-3-22 : P.T.Occurrence tree-2-0-3
occ-2-0-3-22 = (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.source-leg , tt)))
origin-2-0-3-22 : P.T.origin tree-2-0-3 occ-2-0-3-22 ≡ input s20
origin-2-0-3-22 = refl
transport-2-0-3-22 : P.T.origin tree-3-1-2 (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-2-0-3-22 = refl
occ-2-0-3-23 : P.T.Occurrence tree-2-0-3
occ-2-0-3-23 = (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.target-leg , tt)))
origin-2-0-3-23 : P.T.origin tree-2-0-3 occ-2-0-3-23 ≡ input s30
origin-2-0-3-23 = refl
transport-2-0-3-23 : P.T.origin tree-3-1-2 (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.target-leg , tt))) ≡ input (swap s30)
transport-2-0-3-23 = refl
occ-2-0-3-24 : P.T.Occurrence tree-2-0-3
occ-2-0-3-24 = (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-2-0-3-24 : P.T.origin tree-2-0-3 occ-2-0-3-24 ≡ input s01
origin-2-0-3-24 = refl
transport-2-0-3-24 : P.T.origin tree-3-1-2 (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s01)
transport-2-0-3-24 = refl
occ-2-0-3-25 : P.T.Occurrence tree-2-0-3
occ-2-0-3-25 = (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-2-0-3-25 : P.T.origin tree-2-0-3 occ-2-0-3-25 ≡ input s31
origin-2-0-3-25 = refl
transport-2-0-3-25 : P.T.origin tree-3-1-2 (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-2-0-3-25 = refl
occ-2-0-3-26 : P.T.Occurrence tree-2-0-3
occ-2-0-3-26 = (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-2-0-3-26 : P.T.origin tree-2-0-3 occ-2-0-3-26 ≡ input s21
origin-2-0-3-26 = refl
transport-2-0-3-26 : P.T.origin tree-3-1-2 (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s21)
transport-2-0-3-26 = refl
occ-2-0-3-27 : P.T.Occurrence tree-2-0-3
occ-2-0-3-27 = (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-2-0-3-27 : P.T.origin tree-2-0-3 occ-2-0-3-27 ≡ input s31
origin-2-0-3-27 = refl
transport-2-0-3-27 : P.T.origin tree-3-1-2 (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-2-0-3-27 = refl
occ-2-0-3-28 : P.T.Occurrence tree-2-0-3
occ-2-0-3-28 = (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.source-leg , tt)))
origin-2-0-3-28 : P.T.origin tree-2-0-3 occ-2-0-3-28 ≡ input s02
origin-2-0-3-28 = refl
transport-2-0-3-28 : P.T.origin tree-3-1-2 (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-2-0-3-28 = refl
occ-2-0-3-29 : P.T.Occurrence tree-2-0-3
occ-2-0-3-29 = (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.target-leg , tt)))
origin-2-0-3-29 : P.T.origin tree-2-0-3 occ-2-0-3-29 ≡ input s12
origin-2-0-3-29 = refl
transport-2-0-3-29 : P.T.origin tree-3-1-2 (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.target-leg , tt))) ≡ input (swap s12)
transport-2-0-3-29 = refl
occ-2-0-3-30 : P.T.Occurrence tree-2-0-3
occ-2-0-3-30 = (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.source-leg , tt)))
origin-2-0-3-30 : P.T.origin tree-2-0-3 occ-2-0-3-30 ≡ input s02
origin-2-0-3-30 = refl
transport-2-0-3-30 : P.T.origin tree-3-1-2 (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-2-0-3-30 = refl
occ-2-0-3-31 : P.T.Occurrence tree-2-0-3
occ-2-0-3-31 = (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.target-leg , tt)))
origin-2-0-3-31 : P.T.origin tree-2-0-3 occ-2-0-3-31 ≡ input s32
origin-2-0-3-31 = refl
transport-2-0-3-31 : P.T.origin tree-3-1-2 (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.target-leg , tt))) ≡ input (swap s32)
transport-2-0-3-31 = refl
occ-2-0-3-32 : P.T.Occurrence tree-2-0-3
occ-2-0-3-32 = (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-2-0-3-32 : P.T.origin tree-2-0-3 occ-2-0-3-32 ≡ input s03
origin-2-0-3-32 = refl
transport-2-0-3-32 : P.T.origin tree-3-1-2 (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s03)
transport-2-0-3-32 = refl
occ-2-0-3-33 : P.T.Occurrence tree-2-0-3
occ-2-0-3-33 = (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-2-0-3-33 : P.T.origin tree-2-0-3 occ-2-0-3-33 ≡ input s13
origin-2-0-3-33 = refl
transport-2-0-3-33 : P.T.origin tree-3-1-2 (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-2-0-3-33 = refl
occ-2-0-3-34 : P.T.Occurrence tree-2-0-3
occ-2-0-3-34 = (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-2-0-3-34 : P.T.origin tree-2-0-3 occ-2-0-3-34 ≡ input s23
origin-2-0-3-34 = refl
transport-2-0-3-34 : P.T.origin tree-3-1-2 (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s23)
transport-2-0-3-34 = refl
occ-2-0-3-35 : P.T.Occurrence tree-2-0-3
occ-2-0-3-35 = (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-2-0-3-35 : P.T.origin tree-2-0-3 occ-2-0-3-35 ≡ input s13
origin-2-0-3-35 = refl
transport-2-0-3-35 : P.T.origin tree-3-1-2 (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-2-0-3-35 = refl
occ-2-0-3-36 : P.T.Occurrence tree-2-0-3
occ-2-0-3-36 = (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.source-leg , tt)))
origin-2-0-3-36 : P.T.origin tree-2-0-3 occ-2-0-3-36 ≡ input s20
origin-2-0-3-36 = refl
transport-2-0-3-36 : P.T.origin tree-3-1-2 (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-2-0-3-36 = refl
occ-2-0-3-37 : P.T.Occurrence tree-2-0-3
occ-2-0-3-37 = (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.target-leg , tt)))
origin-2-0-3-37 : P.T.origin tree-2-0-3 occ-2-0-3-37 ≡ input s10
origin-2-0-3-37 = refl
transport-2-0-3-37 : P.T.origin tree-3-1-2 (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.target-leg , tt))) ≡ input (swap s10)
transport-2-0-3-37 = refl
occ-2-0-3-38 : P.T.Occurrence tree-2-0-3
occ-2-0-3-38 = (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.source-leg , tt)))
origin-2-0-3-38 : P.T.origin tree-2-0-3 occ-2-0-3-38 ≡ input s20
origin-2-0-3-38 = refl
transport-2-0-3-38 : P.T.origin tree-3-1-2 (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-2-0-3-38 = refl
occ-2-0-3-39 : P.T.Occurrence tree-2-0-3
occ-2-0-3-39 = (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.target-leg , tt)))
origin-2-0-3-39 : P.T.origin tree-2-0-3 occ-2-0-3-39 ≡ input s30
origin-2-0-3-39 = refl
transport-2-0-3-39 : P.T.origin tree-3-1-2 (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.target-leg , tt))) ≡ input (swap s30)
transport-2-0-3-39 = refl
occ-2-0-3-40 : P.T.Occurrence tree-2-0-3
occ-2-0-3-40 = (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-2-0-3-40 : P.T.origin tree-2-0-3 occ-2-0-3-40 ≡ input s01
origin-2-0-3-40 = refl
transport-2-0-3-40 : P.T.origin tree-3-1-2 (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s01)
transport-2-0-3-40 = refl
occ-2-0-3-41 : P.T.Occurrence tree-2-0-3
occ-2-0-3-41 = (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-2-0-3-41 : P.T.origin tree-2-0-3 occ-2-0-3-41 ≡ input s31
origin-2-0-3-41 = refl
transport-2-0-3-41 : P.T.origin tree-3-1-2 (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-2-0-3-41 = refl
occ-2-0-3-42 : P.T.Occurrence tree-2-0-3
occ-2-0-3-42 = (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-2-0-3-42 : P.T.origin tree-2-0-3 occ-2-0-3-42 ≡ input s21
origin-2-0-3-42 = refl
transport-2-0-3-42 : P.T.origin tree-3-1-2 (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s21)
transport-2-0-3-42 = refl
occ-2-0-3-43 : P.T.Occurrence tree-2-0-3
occ-2-0-3-43 = (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-2-0-3-43 : P.T.origin tree-2-0-3 occ-2-0-3-43 ≡ input s31
origin-2-0-3-43 = refl
transport-2-0-3-43 : P.T.origin tree-3-1-2 (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-2-0-3-43 = refl
occ-2-0-3-44 : P.T.Occurrence tree-2-0-3
occ-2-0-3-44 = (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.source-leg , tt)))
origin-2-0-3-44 : P.T.origin tree-2-0-3 occ-2-0-3-44 ≡ input s02
origin-2-0-3-44 = refl
transport-2-0-3-44 : P.T.origin tree-3-1-2 (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-2-0-3-44 = refl
occ-2-0-3-45 : P.T.Occurrence tree-2-0-3
occ-2-0-3-45 = (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.target-leg , tt)))
origin-2-0-3-45 : P.T.origin tree-2-0-3 occ-2-0-3-45 ≡ input s12
origin-2-0-3-45 = refl
transport-2-0-3-45 : P.T.origin tree-3-1-2 (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.target-leg , tt))) ≡ input (swap s12)
transport-2-0-3-45 = refl
occ-2-0-3-46 : P.T.Occurrence tree-2-0-3
occ-2-0-3-46 = (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.source-leg , tt)))
origin-2-0-3-46 : P.T.origin tree-2-0-3 occ-2-0-3-46 ≡ input s02
origin-2-0-3-46 = refl
transport-2-0-3-46 : P.T.origin tree-3-1-2 (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-2-0-3-46 = refl
occ-2-0-3-47 : P.T.Occurrence tree-2-0-3
occ-2-0-3-47 = (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.target-leg , tt)))
origin-2-0-3-47 : P.T.origin tree-2-0-3 occ-2-0-3-47 ≡ input s32
origin-2-0-3-47 = refl
transport-2-0-3-47 : P.T.origin tree-3-1-2 (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.target-leg , tt))) ≡ input (swap s32)
transport-2-0-3-47 = refl
occ-2-0-3-48 : P.T.Occurrence tree-2-0-3
occ-2-0-3-48 = (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-2-0-3-48 : P.T.origin tree-2-0-3 occ-2-0-3-48 ≡ input s03
origin-2-0-3-48 = refl
transport-2-0-3-48 : P.T.origin tree-3-1-2 (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s03)
transport-2-0-3-48 = refl
occ-2-0-3-49 : P.T.Occurrence tree-2-0-3
occ-2-0-3-49 = (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-2-0-3-49 : P.T.origin tree-2-0-3 occ-2-0-3-49 ≡ input s13
origin-2-0-3-49 = refl
transport-2-0-3-49 : P.T.origin tree-3-1-2 (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-2-0-3-49 = refl
occ-2-0-3-50 : P.T.Occurrence tree-2-0-3
occ-2-0-3-50 = (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-2-0-3-50 : P.T.origin tree-2-0-3 occ-2-0-3-50 ≡ input s23
origin-2-0-3-50 = refl
transport-2-0-3-50 : P.T.origin tree-3-1-2 (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s23)
transport-2-0-3-50 = refl
occ-2-0-3-51 : P.T.Occurrence tree-2-0-3
occ-2-0-3-51 = (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-2-0-3-51 : P.T.origin tree-2-0-3 occ-2-0-3-51 ≡ input s13
origin-2-0-3-51 = refl
transport-2-0-3-51 : P.T.origin tree-3-1-2 (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-2-0-3-51 = refl
occ-2-0-3-52 : P.T.Occurrence tree-2-0-3
occ-2-0-3-52 = (P.S.full-source , (P.S.first-port , tt))
origin-2-0-3-52 : P.T.origin tree-2-0-3 occ-2-0-3-52 ≡ input s21
origin-2-0-3-52 = refl
transport-2-0-3-52 : P.T.origin tree-3-1-2 (P.S.full-source , (P.S.first-port , tt)) ≡ input (swap s21)
transport-2-0-3-52 = refl
occ-2-0-3-53 : P.T.Occurrence tree-2-0-3
occ-2-0-3-53 = (P.S.full-source , (P.S.middle-port , tt))
origin-2-0-3-53 : P.T.origin tree-2-0-3 occ-2-0-3-53 ≡ input s01
origin-2-0-3-53 = refl
transport-2-0-3-53 : P.T.origin tree-3-1-2 (P.S.full-source , (P.S.middle-port , tt)) ≡ input (swap s01)
transport-2-0-3-53 = refl
occ-2-0-3-54 : P.T.Occurrence tree-2-0-3
occ-2-0-3-54 = (P.S.full-source , (P.S.final-port , tt))
origin-2-0-3-54 : P.T.origin tree-2-0-3 occ-2-0-3-54 ≡ input s31
origin-2-0-3-54 = refl
transport-2-0-3-54 : P.T.origin tree-3-1-2 (P.S.full-source , (P.S.final-port , tt)) ≡ input (swap s31)
transport-2-0-3-54 = refl
selected-source-2-0-3-AB : P.S.ab-index {a = C.q0} {b = C.q0} {c = C.q7} F.triple-2-0-3 ≡ (m0 , (F.vp-2-1 , F.vp-0-1))
selected-source-2-0-3-AB = refl
selected-target-2-0-3-AB : P.S.ab-index {a = C.q7} {b = C.q7} {c = C.q0} F.triple-3-1-2 ≡ (c0 , (F.vp-3-0 , F.vp-1-0))
selected-target-2-0-3-AB = refl
selected-source-2-0-3-BC : P.S.bc-index {a = C.q0} {b = C.q0} {c = C.q7} F.triple-2-0-3 ≡ (m0 , (F.vp-0-1 , F.vp-3-1))
selected-source-2-0-3-BC = refl
selected-target-2-0-3-BC : P.S.bc-index {a = C.q7} {b = C.q7} {c = C.q0} F.triple-3-1-2 ≡ (c0 , (F.vp-1-0 , F.vp-2-0))
selected-target-2-0-3-BC = refl
selected-source-2-0-3-AC : P.S.ac-index {a = C.q0} {b = C.q0} {c = C.q7} F.triple-2-0-3 ≡ (m0 , (F.vp-2-1 , F.vp-3-1))
selected-source-2-0-3-AC = refl
selected-target-2-0-3-AC : P.S.ac-index {a = C.q7} {b = C.q7} {c = C.q0} F.triple-3-1-2 ≡ (c0 , (F.vp-3-0 , F.vp-2-0))
selected-target-2-0-3-AC = refl
occ-2-1-0-0 : P.T.Occurrence tree-2-1-0
occ-2-1-0-0 = (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.source-leg , tt)))
origin-2-1-0-0 : P.T.origin tree-2-1-0 occ-2-1-0-0 ≡ input s20
origin-2-1-0-0 = refl
transport-2-1-0-0 : P.T.origin tree-3-0-1 (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-2-1-0-0 = refl
occ-2-1-0-1 : P.T.Occurrence tree-2-1-0
occ-2-1-0-1 = (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.target-leg , tt)))
origin-2-1-0-1 : P.T.origin tree-2-1-0 occ-2-1-0-1 ≡ input s10
origin-2-1-0-1 = refl
transport-2-1-0-1 : P.T.origin tree-3-0-1 (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.target-leg , tt))) ≡ input (swap s10)
transport-2-1-0-1 = refl
occ-2-1-0-2 : P.T.Occurrence tree-2-1-0
occ-2-1-0-2 = (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.source-leg , tt)))
origin-2-1-0-2 : P.T.origin tree-2-1-0 occ-2-1-0-2 ≡ input s20
origin-2-1-0-2 = refl
transport-2-1-0-2 : P.T.origin tree-3-0-1 (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-2-1-0-2 = refl
occ-2-1-0-3 : P.T.Occurrence tree-2-1-0
occ-2-1-0-3 = (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.target-leg , tt)))
origin-2-1-0-3 : P.T.origin tree-2-1-0 occ-2-1-0-3 ≡ input s30
origin-2-1-0-3 = refl
transport-2-1-0-3 : P.T.origin tree-3-0-1 (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.target-leg , tt))) ≡ input (swap s30)
transport-2-1-0-3 = refl
occ-2-1-0-4 : P.T.Occurrence tree-2-1-0
occ-2-1-0-4 = (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-2-1-0-4 : P.T.origin tree-2-1-0 occ-2-1-0-4 ≡ input s01
origin-2-1-0-4 = refl
transport-2-1-0-4 : P.T.origin tree-3-0-1 (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s01)
transport-2-1-0-4 = refl
occ-2-1-0-5 : P.T.Occurrence tree-2-1-0
occ-2-1-0-5 = (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-2-1-0-5 : P.T.origin tree-2-1-0 occ-2-1-0-5 ≡ input s31
origin-2-1-0-5 = refl
transport-2-1-0-5 : P.T.origin tree-3-0-1 (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-2-1-0-5 = refl
occ-2-1-0-6 : P.T.Occurrence tree-2-1-0
occ-2-1-0-6 = (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-2-1-0-6 : P.T.origin tree-2-1-0 occ-2-1-0-6 ≡ input s21
origin-2-1-0-6 = refl
transport-2-1-0-6 : P.T.origin tree-3-0-1 (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s21)
transport-2-1-0-6 = refl
occ-2-1-0-7 : P.T.Occurrence tree-2-1-0
occ-2-1-0-7 = (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-2-1-0-7 : P.T.origin tree-2-1-0 occ-2-1-0-7 ≡ input s31
origin-2-1-0-7 = refl
transport-2-1-0-7 : P.T.origin tree-3-0-1 (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-2-1-0-7 = refl
occ-2-1-0-8 : P.T.Occurrence tree-2-1-0
occ-2-1-0-8 = (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.source-leg , tt)))
origin-2-1-0-8 : P.T.origin tree-2-1-0 occ-2-1-0-8 ≡ input s02
origin-2-1-0-8 = refl
transport-2-1-0-8 : P.T.origin tree-3-0-1 (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-2-1-0-8 = refl
occ-2-1-0-9 : P.T.Occurrence tree-2-1-0
occ-2-1-0-9 = (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.target-leg , tt)))
origin-2-1-0-9 : P.T.origin tree-2-1-0 occ-2-1-0-9 ≡ input s12
origin-2-1-0-9 = refl
transport-2-1-0-9 : P.T.origin tree-3-0-1 (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.target-leg , tt))) ≡ input (swap s12)
transport-2-1-0-9 = refl
occ-2-1-0-10 : P.T.Occurrence tree-2-1-0
occ-2-1-0-10 = (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.source-leg , tt)))
origin-2-1-0-10 : P.T.origin tree-2-1-0 occ-2-1-0-10 ≡ input s02
origin-2-1-0-10 = refl
transport-2-1-0-10 : P.T.origin tree-3-0-1 (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-2-1-0-10 = refl
occ-2-1-0-11 : P.T.Occurrence tree-2-1-0
occ-2-1-0-11 = (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.target-leg , tt)))
origin-2-1-0-11 : P.T.origin tree-2-1-0 occ-2-1-0-11 ≡ input s32
origin-2-1-0-11 = refl
transport-2-1-0-11 : P.T.origin tree-3-0-1 (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.target-leg , tt))) ≡ input (swap s32)
transport-2-1-0-11 = refl
occ-2-1-0-12 : P.T.Occurrence tree-2-1-0
occ-2-1-0-12 = (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-2-1-0-12 : P.T.origin tree-2-1-0 occ-2-1-0-12 ≡ input s03
origin-2-1-0-12 = refl
transport-2-1-0-12 : P.T.origin tree-3-0-1 (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s03)
transport-2-1-0-12 = refl
occ-2-1-0-13 : P.T.Occurrence tree-2-1-0
occ-2-1-0-13 = (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-2-1-0-13 : P.T.origin tree-2-1-0 occ-2-1-0-13 ≡ input s13
origin-2-1-0-13 = refl
transport-2-1-0-13 : P.T.origin tree-3-0-1 (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-2-1-0-13 = refl
occ-2-1-0-14 : P.T.Occurrence tree-2-1-0
occ-2-1-0-14 = (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-2-1-0-14 : P.T.origin tree-2-1-0 occ-2-1-0-14 ≡ input s23
origin-2-1-0-14 = refl
transport-2-1-0-14 : P.T.origin tree-3-0-1 (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s23)
transport-2-1-0-14 = refl
occ-2-1-0-15 : P.T.Occurrence tree-2-1-0
occ-2-1-0-15 = (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-2-1-0-15 : P.T.origin tree-2-1-0 occ-2-1-0-15 ≡ input s13
origin-2-1-0-15 = refl
transport-2-1-0-15 : P.T.origin tree-3-0-1 (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-2-1-0-15 = refl
occ-2-1-0-16 : P.T.Occurrence tree-2-1-0
occ-2-1-0-16 = (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-2-1-0-16 : P.T.origin tree-2-1-0 occ-2-1-0-16 ≡ input s10
origin-2-1-0-16 = refl
transport-2-1-0-16 : P.T.origin tree-3-0-1 (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s10)
transport-2-1-0-16 = refl
occ-2-1-0-17 : P.T.Occurrence tree-2-1-0
occ-2-1-0-17 = (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-2-1-0-17 : P.T.origin tree-2-1-0 occ-2-1-0-17 ≡ input s20
origin-2-1-0-17 = refl
transport-2-1-0-17 : P.T.origin tree-3-0-1 (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-2-1-0-17 = refl
occ-2-1-0-18 : P.T.Occurrence tree-2-1-0
occ-2-1-0-18 = (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-2-1-0-18 : P.T.origin tree-2-1-0 occ-2-1-0-18 ≡ input s30
origin-2-1-0-18 = refl
transport-2-1-0-18 : P.T.origin tree-3-0-1 (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s30)
transport-2-1-0-18 = refl
occ-2-1-0-19 : P.T.Occurrence tree-2-1-0
occ-2-1-0-19 = (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-2-1-0-19 : P.T.origin tree-2-1-0 occ-2-1-0-19 ≡ input s20
origin-2-1-0-19 = refl
transport-2-1-0-19 : P.T.origin tree-3-0-1 (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-2-1-0-19 = refl
occ-2-1-0-20 : P.T.Occurrence tree-2-1-0
occ-2-1-0-20 = (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.source-leg , tt)))
origin-2-1-0-20 : P.T.origin tree-2-1-0 occ-2-1-0-20 ≡ input s31
origin-2-1-0-20 = refl
transport-2-1-0-20 : P.T.origin tree-3-0-1 (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-2-1-0-20 = refl
occ-2-1-0-21 : P.T.Occurrence tree-2-1-0
occ-2-1-0-21 = (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.target-leg , tt)))
origin-2-1-0-21 : P.T.origin tree-2-1-0 occ-2-1-0-21 ≡ input s01
origin-2-1-0-21 = refl
transport-2-1-0-21 : P.T.origin tree-3-0-1 (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.target-leg , tt))) ≡ input (swap s01)
transport-2-1-0-21 = refl
occ-2-1-0-22 : P.T.Occurrence tree-2-1-0
occ-2-1-0-22 = (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.source-leg , tt)))
origin-2-1-0-22 : P.T.origin tree-2-1-0 occ-2-1-0-22 ≡ input s31
origin-2-1-0-22 = refl
transport-2-1-0-22 : P.T.origin tree-3-0-1 (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-2-1-0-22 = refl
occ-2-1-0-23 : P.T.Occurrence tree-2-1-0
occ-2-1-0-23 = (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.target-leg , tt)))
origin-2-1-0-23 : P.T.origin tree-2-1-0 occ-2-1-0-23 ≡ input s21
origin-2-1-0-23 = refl
transport-2-1-0-23 : P.T.origin tree-3-0-1 (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.target-leg , tt))) ≡ input (swap s21)
transport-2-1-0-23 = refl
occ-2-1-0-24 : P.T.Occurrence tree-2-1-0
occ-2-1-0-24 = (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-2-1-0-24 : P.T.origin tree-2-1-0 occ-2-1-0-24 ≡ input s12
origin-2-1-0-24 = refl
transport-2-1-0-24 : P.T.origin tree-3-0-1 (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s12)
transport-2-1-0-24 = refl
occ-2-1-0-25 : P.T.Occurrence tree-2-1-0
occ-2-1-0-25 = (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-2-1-0-25 : P.T.origin tree-2-1-0 occ-2-1-0-25 ≡ input s02
origin-2-1-0-25 = refl
transport-2-1-0-25 : P.T.origin tree-3-0-1 (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-2-1-0-25 = refl
occ-2-1-0-26 : P.T.Occurrence tree-2-1-0
occ-2-1-0-26 = (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-2-1-0-26 : P.T.origin tree-2-1-0 occ-2-1-0-26 ≡ input s32
origin-2-1-0-26 = refl
transport-2-1-0-26 : P.T.origin tree-3-0-1 (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s32)
transport-2-1-0-26 = refl
occ-2-1-0-27 : P.T.Occurrence tree-2-1-0
occ-2-1-0-27 = (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-2-1-0-27 : P.T.origin tree-2-1-0 occ-2-1-0-27 ≡ input s02
origin-2-1-0-27 = refl
transport-2-1-0-27 : P.T.origin tree-3-0-1 (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-2-1-0-27 = refl
occ-2-1-0-28 : P.T.Occurrence tree-2-1-0
occ-2-1-0-28 = (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.source-leg , tt)))
origin-2-1-0-28 : P.T.origin tree-2-1-0 occ-2-1-0-28 ≡ input s13
origin-2-1-0-28 = refl
transport-2-1-0-28 : P.T.origin tree-3-0-1 (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-2-1-0-28 = refl
occ-2-1-0-29 : P.T.Occurrence tree-2-1-0
occ-2-1-0-29 = (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.target-leg , tt)))
origin-2-1-0-29 : P.T.origin tree-2-1-0 occ-2-1-0-29 ≡ input s03
origin-2-1-0-29 = refl
transport-2-1-0-29 : P.T.origin tree-3-0-1 (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.target-leg , tt))) ≡ input (swap s03)
transport-2-1-0-29 = refl
occ-2-1-0-30 : P.T.Occurrence tree-2-1-0
occ-2-1-0-30 = (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.source-leg , tt)))
origin-2-1-0-30 : P.T.origin tree-2-1-0 occ-2-1-0-30 ≡ input s13
origin-2-1-0-30 = refl
transport-2-1-0-30 : P.T.origin tree-3-0-1 (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-2-1-0-30 = refl
occ-2-1-0-31 : P.T.Occurrence tree-2-1-0
occ-2-1-0-31 = (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.target-leg , tt)))
origin-2-1-0-31 : P.T.origin tree-2-1-0 occ-2-1-0-31 ≡ input s23
origin-2-1-0-31 = refl
transport-2-1-0-31 : P.T.origin tree-3-0-1 (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.target-leg , tt))) ≡ input (swap s23)
transport-2-1-0-31 = refl
occ-2-1-0-32 : P.T.Occurrence tree-2-1-0
occ-2-1-0-32 = (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-2-1-0-32 : P.T.origin tree-2-1-0 occ-2-1-0-32 ≡ input s20
origin-2-1-0-32 = refl
transport-2-1-0-32 : P.T.origin tree-3-0-1 (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-2-1-0-32 = refl
occ-2-1-0-33 : P.T.Occurrence tree-2-1-0
occ-2-1-0-33 = (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-2-1-0-33 : P.T.origin tree-2-1-0 occ-2-1-0-33 ≡ input s20
origin-2-1-0-33 = refl
transport-2-1-0-33 : P.T.origin tree-3-0-1 (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-2-1-0-33 = refl
occ-2-1-0-34 : P.T.Occurrence tree-2-1-0
occ-2-1-0-34 = (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-0-1)) , (P.S.source-leg , tt)))
origin-2-1-0-34 : P.T.origin tree-2-1-0 occ-2-1-0-34 ≡ input s01
origin-2-1-0-34 = refl
transport-2-1-0-34 : P.T.origin tree-3-0-1 (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-1-0)) , (P.S.source-leg , tt))) ≡ input (swap s01)
transport-2-1-0-34 = refl
occ-2-1-0-35 : P.T.Occurrence tree-2-1-0
occ-2-1-0-35 = (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-0-1)) , (P.S.target-leg , tt)))
origin-2-1-0-35 : P.T.origin tree-2-1-0 occ-2-1-0-35 ≡ input s01
origin-2-1-0-35 = refl
transport-2-1-0-35 : P.T.origin tree-3-0-1 (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-1-0)) , (P.S.target-leg , tt))) ≡ input (swap s01)
transport-2-1-0-35 = refl
occ-2-1-0-36 : P.T.Occurrence tree-2-1-0
occ-2-1-0-36 = (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.source-leg , tt)))
origin-2-1-0-36 : P.T.origin tree-2-1-0 occ-2-1-0-36 ≡ input s01
origin-2-1-0-36 = refl
transport-2-1-0-36 : P.T.origin tree-3-0-1 (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.source-leg , tt))) ≡ input (swap s01)
transport-2-1-0-36 = refl
occ-2-1-0-37 : P.T.Occurrence tree-2-1-0
occ-2-1-0-37 = (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.target-leg , tt)))
origin-2-1-0-37 : P.T.origin tree-2-1-0 occ-2-1-0-37 ≡ input s21
origin-2-1-0-37 = refl
transport-2-1-0-37 : P.T.origin tree-3-0-1 (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.target-leg , tt))) ≡ input (swap s21)
transport-2-1-0-37 = refl
occ-2-1-0-38 : P.T.Occurrence tree-2-1-0
occ-2-1-0-38 = (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.source-leg , tt)))
origin-2-1-0-38 : P.T.origin tree-2-1-0 occ-2-1-0-38 ≡ input s21
origin-2-1-0-38 = refl
transport-2-1-0-38 : P.T.origin tree-3-0-1 (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.source-leg , tt))) ≡ input (swap s21)
transport-2-1-0-38 = refl
occ-2-1-0-39 : P.T.Occurrence tree-2-1-0
occ-2-1-0-39 = (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.target-leg , tt)))
origin-2-1-0-39 : P.T.origin tree-2-1-0 occ-2-1-0-39 ≡ input s01
origin-2-1-0-39 = refl
transport-2-1-0-39 : P.T.origin tree-3-0-1 (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.target-leg , tt))) ≡ input (swap s01)
transport-2-1-0-39 = refl
occ-2-1-0-40 : P.T.Occurrence tree-2-1-0
occ-2-1-0-40 = (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-2-1)) , (P.S.source-leg , tt)))
origin-2-1-0-40 : P.T.origin tree-2-1-0 occ-2-1-0-40 ≡ input s21
origin-2-1-0-40 = refl
transport-2-1-0-40 : P.T.origin tree-3-0-1 (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-3-0)) , (P.S.source-leg , tt))) ≡ input (swap s21)
transport-2-1-0-40 = refl
occ-2-1-0-41 : P.T.Occurrence tree-2-1-0
occ-2-1-0-41 = (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-2-1)) , (P.S.target-leg , tt)))
origin-2-1-0-41 : P.T.origin tree-2-1-0 occ-2-1-0-41 ≡ input s21
origin-2-1-0-41 = refl
transport-2-1-0-41 : P.T.origin tree-3-0-1 (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-3-0)) , (P.S.target-leg , tt))) ≡ input (swap s21)
transport-2-1-0-41 = refl
occ-2-1-0-42 : P.T.Occurrence tree-2-1-0
occ-2-1-0-42 = (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-2-1-0-42 : P.T.origin tree-2-1-0 occ-2-1-0-42 ≡ input s02
origin-2-1-0-42 = refl
transport-2-1-0-42 : P.T.origin tree-3-0-1 (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-2-1-0-42 = refl
occ-2-1-0-43 : P.T.Occurrence tree-2-1-0
occ-2-1-0-43 = (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-2-1-0-43 : P.T.origin tree-2-1-0 occ-2-1-0-43 ≡ input s02
origin-2-1-0-43 = refl
transport-2-1-0-43 : P.T.origin tree-3-0-1 (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-2-1-0-43 = refl
occ-2-1-0-44 : P.T.Occurrence tree-2-1-0
occ-2-1-0-44 = (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-0-3)) , (P.S.source-leg , tt)))
origin-2-1-0-44 : P.T.origin tree-2-1-0 occ-2-1-0-44 ≡ input s03
origin-2-1-0-44 = refl
transport-2-1-0-44 : P.T.origin tree-3-0-1 (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-1-2)) , (P.S.source-leg , tt))) ≡ input (swap s03)
transport-2-1-0-44 = refl
occ-2-1-0-45 : P.T.Occurrence tree-2-1-0
occ-2-1-0-45 = (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-0-3)) , (P.S.target-leg , tt)))
origin-2-1-0-45 : P.T.origin tree-2-1-0 occ-2-1-0-45 ≡ input s03
origin-2-1-0-45 = refl
transport-2-1-0-45 : P.T.origin tree-3-0-1 (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-1-2)) , (P.S.target-leg , tt))) ≡ input (swap s03)
transport-2-1-0-45 = refl
occ-2-1-0-46 : P.T.Occurrence tree-2-1-0
occ-2-1-0-46 = (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.source-leg , tt)))
origin-2-1-0-46 : P.T.origin tree-2-1-0 occ-2-1-0-46 ≡ input s03
origin-2-1-0-46 = refl
transport-2-1-0-46 : P.T.origin tree-3-0-1 (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.source-leg , tt))) ≡ input (swap s03)
transport-2-1-0-46 = refl
occ-2-1-0-47 : P.T.Occurrence tree-2-1-0
occ-2-1-0-47 = (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.target-leg , tt)))
origin-2-1-0-47 : P.T.origin tree-2-1-0 occ-2-1-0-47 ≡ input s23
origin-2-1-0-47 = refl
transport-2-1-0-47 : P.T.origin tree-3-0-1 (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.target-leg , tt))) ≡ input (swap s23)
transport-2-1-0-47 = refl
occ-2-1-0-48 : P.T.Occurrence tree-2-1-0
occ-2-1-0-48 = (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.source-leg , tt)))
origin-2-1-0-48 : P.T.origin tree-2-1-0 occ-2-1-0-48 ≡ input s23
origin-2-1-0-48 = refl
transport-2-1-0-48 : P.T.origin tree-3-0-1 (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.source-leg , tt))) ≡ input (swap s23)
transport-2-1-0-48 = refl
occ-2-1-0-49 : P.T.Occurrence tree-2-1-0
occ-2-1-0-49 = (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.target-leg , tt)))
origin-2-1-0-49 : P.T.origin tree-2-1-0 occ-2-1-0-49 ≡ input s03
origin-2-1-0-49 = refl
transport-2-1-0-49 : P.T.origin tree-3-0-1 (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.target-leg , tt))) ≡ input (swap s03)
transport-2-1-0-49 = refl
occ-2-1-0-50 : P.T.Occurrence tree-2-1-0
occ-2-1-0-50 = (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-2-3)) , (P.S.source-leg , tt)))
origin-2-1-0-50 : P.T.origin tree-2-1-0 occ-2-1-0-50 ≡ input s23
origin-2-1-0-50 = refl
transport-2-1-0-50 : P.T.origin tree-3-0-1 (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-3-2)) , (P.S.source-leg , tt))) ≡ input (swap s23)
transport-2-1-0-50 = refl
occ-2-1-0-51 : P.T.Occurrence tree-2-1-0
occ-2-1-0-51 = (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-2-3)) , (P.S.target-leg , tt)))
origin-2-1-0-51 : P.T.origin tree-2-1-0 occ-2-1-0-51 ≡ input s23
origin-2-1-0-51 = refl
transport-2-1-0-51 : P.T.origin tree-3-0-1 (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-3-2)) , (P.S.target-leg , tt))) ≡ input (swap s23)
transport-2-1-0-51 = refl
occ-2-1-0-52 : P.T.Occurrence tree-2-1-0
occ-2-1-0-52 = (P.S.full-source , (P.S.first-port , tt))
origin-2-1-0-52 : P.T.origin tree-2-1-0 occ-2-1-0-52 ≡ input s23
origin-2-1-0-52 = refl
transport-2-1-0-52 : P.T.origin tree-3-0-1 (P.S.full-source , (P.S.first-port , tt)) ≡ input (swap s23)
transport-2-1-0-52 = refl
occ-2-1-0-53 : P.T.Occurrence tree-2-1-0
occ-2-1-0-53 = (P.S.full-source , (P.S.middle-port , tt))
origin-2-1-0-53 : P.T.origin tree-2-1-0 occ-2-1-0-53 ≡ input s13
origin-2-1-0-53 = refl
transport-2-1-0-53 : P.T.origin tree-3-0-1 (P.S.full-source , (P.S.middle-port , tt)) ≡ input (swap s13)
transport-2-1-0-53 = refl
occ-2-1-0-54 : P.T.Occurrence tree-2-1-0
occ-2-1-0-54 = (P.S.full-source , (P.S.final-port , tt))
origin-2-1-0-54 : P.T.origin tree-2-1-0 occ-2-1-0-54 ≡ input s03
origin-2-1-0-54 = refl
transport-2-1-0-54 : P.T.origin tree-3-0-1 (P.S.full-source , (P.S.final-port , tt)) ≡ input (swap s03)
transport-2-1-0-54 = refl
selected-source-2-1-0-AB : P.S.ab-index {a = C.q0} {b = C.q7} {c = C.q0} F.triple-2-1-0 ≡ (m1 , (F.vp-2-3 , F.vp-1-3))
selected-source-2-1-0-AB = refl
selected-target-2-1-0-AB : P.S.ab-index {a = C.q7} {b = C.q0} {c = C.q7} F.triple-3-0-1 ≡ (c1 , (F.vp-3-2 , F.vp-0-2))
selected-target-2-1-0-AB = refl
selected-source-2-1-0-BC : P.S.bc-index {a = C.q0} {b = C.q7} {c = C.q0} F.triple-2-1-0 ≡ (m1 , (F.vp-1-3 , F.vp-0-3))
selected-source-2-1-0-BC = refl
selected-target-2-1-0-BC : P.S.bc-index {a = C.q7} {b = C.q0} {c = C.q7} F.triple-3-0-1 ≡ (c1 , (F.vp-0-2 , F.vp-1-2))
selected-target-2-1-0-BC = refl
selected-source-2-1-0-AC : P.S.ac-index {a = C.q0} {b = C.q7} {c = C.q0} F.triple-2-1-0 ≡ (m1 , (F.vp-2-3 , F.vp-0-3))
selected-source-2-1-0-AC = refl
selected-target-2-1-0-AC : P.S.ac-index {a = C.q7} {b = C.q0} {c = C.q7} F.triple-3-0-1 ≡ (c1 , (F.vp-3-2 , F.vp-1-2))
selected-target-2-1-0-AC = refl
occ-2-1-3-0 : P.T.Occurrence tree-2-1-3
occ-2-1-3-0 = (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.source-leg , tt)))
origin-2-1-3-0 : P.T.origin tree-2-1-3 occ-2-1-3-0 ≡ input s20
origin-2-1-3-0 = refl
transport-2-1-3-0 : P.T.origin tree-3-0-2 (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-2-1-3-0 = refl
occ-2-1-3-1 : P.T.Occurrence tree-2-1-3
occ-2-1-3-1 = (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.target-leg , tt)))
origin-2-1-3-1 : P.T.origin tree-2-1-3 occ-2-1-3-1 ≡ input s10
origin-2-1-3-1 = refl
transport-2-1-3-1 : P.T.origin tree-3-0-2 (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.target-leg , tt))) ≡ input (swap s10)
transport-2-1-3-1 = refl
occ-2-1-3-2 : P.T.Occurrence tree-2-1-3
occ-2-1-3-2 = (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.source-leg , tt)))
origin-2-1-3-2 : P.T.origin tree-2-1-3 occ-2-1-3-2 ≡ input s20
origin-2-1-3-2 = refl
transport-2-1-3-2 : P.T.origin tree-3-0-2 (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-2-1-3-2 = refl
occ-2-1-3-3 : P.T.Occurrence tree-2-1-3
occ-2-1-3-3 = (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.target-leg , tt)))
origin-2-1-3-3 : P.T.origin tree-2-1-3 occ-2-1-3-3 ≡ input s30
origin-2-1-3-3 = refl
transport-2-1-3-3 : P.T.origin tree-3-0-2 (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.target-leg , tt))) ≡ input (swap s30)
transport-2-1-3-3 = refl
occ-2-1-3-4 : P.T.Occurrence tree-2-1-3
occ-2-1-3-4 = (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-2-1-3-4 : P.T.origin tree-2-1-3 occ-2-1-3-4 ≡ input s01
origin-2-1-3-4 = refl
transport-2-1-3-4 : P.T.origin tree-3-0-2 (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s01)
transport-2-1-3-4 = refl
occ-2-1-3-5 : P.T.Occurrence tree-2-1-3
occ-2-1-3-5 = (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-2-1-3-5 : P.T.origin tree-2-1-3 occ-2-1-3-5 ≡ input s31
origin-2-1-3-5 = refl
transport-2-1-3-5 : P.T.origin tree-3-0-2 (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-2-1-3-5 = refl
occ-2-1-3-6 : P.T.Occurrence tree-2-1-3
occ-2-1-3-6 = (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-2-1-3-6 : P.T.origin tree-2-1-3 occ-2-1-3-6 ≡ input s21
origin-2-1-3-6 = refl
transport-2-1-3-6 : P.T.origin tree-3-0-2 (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s21)
transport-2-1-3-6 = refl
occ-2-1-3-7 : P.T.Occurrence tree-2-1-3
occ-2-1-3-7 = (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-2-1-3-7 : P.T.origin tree-2-1-3 occ-2-1-3-7 ≡ input s31
origin-2-1-3-7 = refl
transport-2-1-3-7 : P.T.origin tree-3-0-2 (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-2-1-3-7 = refl
occ-2-1-3-8 : P.T.Occurrence tree-2-1-3
occ-2-1-3-8 = (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.source-leg , tt)))
origin-2-1-3-8 : P.T.origin tree-2-1-3 occ-2-1-3-8 ≡ input s02
origin-2-1-3-8 = refl
transport-2-1-3-8 : P.T.origin tree-3-0-2 (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-2-1-3-8 = refl
occ-2-1-3-9 : P.T.Occurrence tree-2-1-3
occ-2-1-3-9 = (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.target-leg , tt)))
origin-2-1-3-9 : P.T.origin tree-2-1-3 occ-2-1-3-9 ≡ input s12
origin-2-1-3-9 = refl
transport-2-1-3-9 : P.T.origin tree-3-0-2 (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.target-leg , tt))) ≡ input (swap s12)
transport-2-1-3-9 = refl
occ-2-1-3-10 : P.T.Occurrence tree-2-1-3
occ-2-1-3-10 = (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.source-leg , tt)))
origin-2-1-3-10 : P.T.origin tree-2-1-3 occ-2-1-3-10 ≡ input s02
origin-2-1-3-10 = refl
transport-2-1-3-10 : P.T.origin tree-3-0-2 (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-2-1-3-10 = refl
occ-2-1-3-11 : P.T.Occurrence tree-2-1-3
occ-2-1-3-11 = (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.target-leg , tt)))
origin-2-1-3-11 : P.T.origin tree-2-1-3 occ-2-1-3-11 ≡ input s32
origin-2-1-3-11 = refl
transport-2-1-3-11 : P.T.origin tree-3-0-2 (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.target-leg , tt))) ≡ input (swap s32)
transport-2-1-3-11 = refl
occ-2-1-3-12 : P.T.Occurrence tree-2-1-3
occ-2-1-3-12 = (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-2-1-3-12 : P.T.origin tree-2-1-3 occ-2-1-3-12 ≡ input s03
origin-2-1-3-12 = refl
transport-2-1-3-12 : P.T.origin tree-3-0-2 (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s03)
transport-2-1-3-12 = refl
occ-2-1-3-13 : P.T.Occurrence tree-2-1-3
occ-2-1-3-13 = (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-2-1-3-13 : P.T.origin tree-2-1-3 occ-2-1-3-13 ≡ input s13
origin-2-1-3-13 = refl
transport-2-1-3-13 : P.T.origin tree-3-0-2 (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-2-1-3-13 = refl
occ-2-1-3-14 : P.T.Occurrence tree-2-1-3
occ-2-1-3-14 = (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-2-1-3-14 : P.T.origin tree-2-1-3 occ-2-1-3-14 ≡ input s23
origin-2-1-3-14 = refl
transport-2-1-3-14 : P.T.origin tree-3-0-2 (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s23)
transport-2-1-3-14 = refl
occ-2-1-3-15 : P.T.Occurrence tree-2-1-3
occ-2-1-3-15 = (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-2-1-3-15 : P.T.origin tree-2-1-3 occ-2-1-3-15 ≡ input s13
origin-2-1-3-15 = refl
transport-2-1-3-15 : P.T.origin tree-3-0-2 (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-2-1-3-15 = refl
occ-2-1-3-16 : P.T.Occurrence tree-2-1-3
occ-2-1-3-16 = (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-1-0)) , (P.S.source-leg , tt)))
origin-2-1-3-16 : P.T.origin tree-2-1-3 occ-2-1-3-16 ≡ input s10
origin-2-1-3-16 = refl
transport-2-1-3-16 : P.T.origin tree-3-0-2 (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-0-1)) , (P.S.source-leg , tt))) ≡ input (swap s10)
transport-2-1-3-16 = refl
occ-2-1-3-17 : P.T.Occurrence tree-2-1-3
occ-2-1-3-17 = (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-1-0)) , (P.S.target-leg , tt)))
origin-2-1-3-17 : P.T.origin tree-2-1-3 occ-2-1-3-17 ≡ input s10
origin-2-1-3-17 = refl
transport-2-1-3-17 : P.T.origin tree-3-0-2 (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-0-1)) , (P.S.target-leg , tt))) ≡ input (swap s10)
transport-2-1-3-17 = refl
occ-2-1-3-18 : P.T.Occurrence tree-2-1-3
occ-2-1-3-18 = (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.source-leg , tt)))
origin-2-1-3-18 : P.T.origin tree-2-1-3 occ-2-1-3-18 ≡ input s10
origin-2-1-3-18 = refl
transport-2-1-3-18 : P.T.origin tree-3-0-2 (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.source-leg , tt))) ≡ input (swap s10)
transport-2-1-3-18 = refl
occ-2-1-3-19 : P.T.Occurrence tree-2-1-3
occ-2-1-3-19 = (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.target-leg , tt)))
origin-2-1-3-19 : P.T.origin tree-2-1-3 occ-2-1-3-19 ≡ input s30
origin-2-1-3-19 = refl
transport-2-1-3-19 : P.T.origin tree-3-0-2 (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.target-leg , tt))) ≡ input (swap s30)
transport-2-1-3-19 = refl
occ-2-1-3-20 : P.T.Occurrence tree-2-1-3
occ-2-1-3-20 = (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.source-leg , tt)))
origin-2-1-3-20 : P.T.origin tree-2-1-3 occ-2-1-3-20 ≡ input s30
origin-2-1-3-20 = refl
transport-2-1-3-20 : P.T.origin tree-3-0-2 (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.source-leg , tt))) ≡ input (swap s30)
transport-2-1-3-20 = refl
occ-2-1-3-21 : P.T.Occurrence tree-2-1-3
occ-2-1-3-21 = (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.target-leg , tt)))
origin-2-1-3-21 : P.T.origin tree-2-1-3 occ-2-1-3-21 ≡ input s10
origin-2-1-3-21 = refl
transport-2-1-3-21 : P.T.origin tree-3-0-2 (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.target-leg , tt))) ≡ input (swap s10)
transport-2-1-3-21 = refl
occ-2-1-3-22 : P.T.Occurrence tree-2-1-3
occ-2-1-3-22 = (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-3-0)) , (P.S.source-leg , tt)))
origin-2-1-3-22 : P.T.origin tree-2-1-3 occ-2-1-3-22 ≡ input s30
origin-2-1-3-22 = refl
transport-2-1-3-22 : P.T.origin tree-3-0-2 (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-2-1)) , (P.S.source-leg , tt))) ≡ input (swap s30)
transport-2-1-3-22 = refl
occ-2-1-3-23 : P.T.Occurrence tree-2-1-3
occ-2-1-3-23 = (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-3-0)) , (P.S.target-leg , tt)))
origin-2-1-3-23 : P.T.origin tree-2-1-3 occ-2-1-3-23 ≡ input s30
origin-2-1-3-23 = refl
transport-2-1-3-23 : P.T.origin tree-3-0-2 (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-2-1)) , (P.S.target-leg , tt))) ≡ input (swap s30)
transport-2-1-3-23 = refl
occ-2-1-3-24 : P.T.Occurrence tree-2-1-3
occ-2-1-3-24 = (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-2-1-3-24 : P.T.origin tree-2-1-3 occ-2-1-3-24 ≡ input s31
origin-2-1-3-24 = refl
transport-2-1-3-24 : P.T.origin tree-3-0-2 (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-2-1-3-24 = refl
occ-2-1-3-25 : P.T.Occurrence tree-2-1-3
occ-2-1-3-25 = (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-2-1-3-25 : P.T.origin tree-2-1-3 occ-2-1-3-25 ≡ input s31
origin-2-1-3-25 = refl
transport-2-1-3-25 : P.T.origin tree-3-0-2 (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-2-1-3-25 = refl
occ-2-1-3-26 : P.T.Occurrence tree-2-1-3
occ-2-1-3-26 = (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-1-2)) , (P.S.source-leg , tt)))
origin-2-1-3-26 : P.T.origin tree-2-1-3 occ-2-1-3-26 ≡ input s12
origin-2-1-3-26 = refl
transport-2-1-3-26 : P.T.origin tree-3-0-2 (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-0-3)) , (P.S.source-leg , tt))) ≡ input (swap s12)
transport-2-1-3-26 = refl
occ-2-1-3-27 : P.T.Occurrence tree-2-1-3
occ-2-1-3-27 = (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-1-2)) , (P.S.target-leg , tt)))
origin-2-1-3-27 : P.T.origin tree-2-1-3 occ-2-1-3-27 ≡ input s12
origin-2-1-3-27 = refl
transport-2-1-3-27 : P.T.origin tree-3-0-2 (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-0-3)) , (P.S.target-leg , tt))) ≡ input (swap s12)
transport-2-1-3-27 = refl
occ-2-1-3-28 : P.T.Occurrence tree-2-1-3
occ-2-1-3-28 = (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.source-leg , tt)))
origin-2-1-3-28 : P.T.origin tree-2-1-3 occ-2-1-3-28 ≡ input s12
origin-2-1-3-28 = refl
transport-2-1-3-28 : P.T.origin tree-3-0-2 (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.source-leg , tt))) ≡ input (swap s12)
transport-2-1-3-28 = refl
occ-2-1-3-29 : P.T.Occurrence tree-2-1-3
occ-2-1-3-29 = (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.target-leg , tt)))
origin-2-1-3-29 : P.T.origin tree-2-1-3 occ-2-1-3-29 ≡ input s32
origin-2-1-3-29 = refl
transport-2-1-3-29 : P.T.origin tree-3-0-2 (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.target-leg , tt))) ≡ input (swap s32)
transport-2-1-3-29 = refl
occ-2-1-3-30 : P.T.Occurrence tree-2-1-3
occ-2-1-3-30 = (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.source-leg , tt)))
origin-2-1-3-30 : P.T.origin tree-2-1-3 occ-2-1-3-30 ≡ input s32
origin-2-1-3-30 = refl
transport-2-1-3-30 : P.T.origin tree-3-0-2 (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.source-leg , tt))) ≡ input (swap s32)
transport-2-1-3-30 = refl
occ-2-1-3-31 : P.T.Occurrence tree-2-1-3
occ-2-1-3-31 = (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.target-leg , tt)))
origin-2-1-3-31 : P.T.origin tree-2-1-3 occ-2-1-3-31 ≡ input s12
origin-2-1-3-31 = refl
transport-2-1-3-31 : P.T.origin tree-3-0-2 (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.target-leg , tt))) ≡ input (swap s12)
transport-2-1-3-31 = refl
occ-2-1-3-32 : P.T.Occurrence tree-2-1-3
occ-2-1-3-32 = (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-3-2)) , (P.S.source-leg , tt)))
origin-2-1-3-32 : P.T.origin tree-2-1-3 occ-2-1-3-32 ≡ input s32
origin-2-1-3-32 = refl
transport-2-1-3-32 : P.T.origin tree-3-0-2 (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-2-3)) , (P.S.source-leg , tt))) ≡ input (swap s32)
transport-2-1-3-32 = refl
occ-2-1-3-33 : P.T.Occurrence tree-2-1-3
occ-2-1-3-33 = (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-3-2)) , (P.S.target-leg , tt)))
origin-2-1-3-33 : P.T.origin tree-2-1-3 occ-2-1-3-33 ≡ input s32
origin-2-1-3-33 = refl
transport-2-1-3-33 : P.T.origin tree-3-0-2 (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-2-3)) , (P.S.target-leg , tt))) ≡ input (swap s32)
transport-2-1-3-33 = refl
occ-2-1-3-34 : P.T.Occurrence tree-2-1-3
occ-2-1-3-34 = (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-2-1-3-34 : P.T.origin tree-2-1-3 occ-2-1-3-34 ≡ input s13
origin-2-1-3-34 = refl
transport-2-1-3-34 : P.T.origin tree-3-0-2 (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-2-1-3-34 = refl
occ-2-1-3-35 : P.T.Occurrence tree-2-1-3
occ-2-1-3-35 = (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-2-1-3-35 : P.T.origin tree-2-1-3 occ-2-1-3-35 ≡ input s13
origin-2-1-3-35 = refl
transport-2-1-3-35 : P.T.origin tree-3-0-2 (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-2-1-3-35 = refl
occ-2-1-3-36 : P.T.Occurrence tree-2-1-3
occ-2-1-3-36 = (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.source-leg , tt)))
origin-2-1-3-36 : P.T.origin tree-2-1-3 occ-2-1-3-36 ≡ input s20
origin-2-1-3-36 = refl
transport-2-1-3-36 : P.T.origin tree-3-0-2 (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-2-1-3-36 = refl
occ-2-1-3-37 : P.T.Occurrence tree-2-1-3
occ-2-1-3-37 = (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.target-leg , tt)))
origin-2-1-3-37 : P.T.origin tree-2-1-3 occ-2-1-3-37 ≡ input s10
origin-2-1-3-37 = refl
transport-2-1-3-37 : P.T.origin tree-3-0-2 (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.target-leg , tt))) ≡ input (swap s10)
transport-2-1-3-37 = refl
occ-2-1-3-38 : P.T.Occurrence tree-2-1-3
occ-2-1-3-38 = (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.source-leg , tt)))
origin-2-1-3-38 : P.T.origin tree-2-1-3 occ-2-1-3-38 ≡ input s20
origin-2-1-3-38 = refl
transport-2-1-3-38 : P.T.origin tree-3-0-2 (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-2-1-3-38 = refl
occ-2-1-3-39 : P.T.Occurrence tree-2-1-3
occ-2-1-3-39 = (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.target-leg , tt)))
origin-2-1-3-39 : P.T.origin tree-2-1-3 occ-2-1-3-39 ≡ input s30
origin-2-1-3-39 = refl
transport-2-1-3-39 : P.T.origin tree-3-0-2 (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.target-leg , tt))) ≡ input (swap s30)
transport-2-1-3-39 = refl
occ-2-1-3-40 : P.T.Occurrence tree-2-1-3
occ-2-1-3-40 = (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-2-1-3-40 : P.T.origin tree-2-1-3 occ-2-1-3-40 ≡ input s01
origin-2-1-3-40 = refl
transport-2-1-3-40 : P.T.origin tree-3-0-2 (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s01)
transport-2-1-3-40 = refl
occ-2-1-3-41 : P.T.Occurrence tree-2-1-3
occ-2-1-3-41 = (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-2-1-3-41 : P.T.origin tree-2-1-3 occ-2-1-3-41 ≡ input s31
origin-2-1-3-41 = refl
transport-2-1-3-41 : P.T.origin tree-3-0-2 (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-2-1-3-41 = refl
occ-2-1-3-42 : P.T.Occurrence tree-2-1-3
occ-2-1-3-42 = (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-2-1-3-42 : P.T.origin tree-2-1-3 occ-2-1-3-42 ≡ input s21
origin-2-1-3-42 = refl
transport-2-1-3-42 : P.T.origin tree-3-0-2 (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s21)
transport-2-1-3-42 = refl
occ-2-1-3-43 : P.T.Occurrence tree-2-1-3
occ-2-1-3-43 = (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-2-1-3-43 : P.T.origin tree-2-1-3 occ-2-1-3-43 ≡ input s31
origin-2-1-3-43 = refl
transport-2-1-3-43 : P.T.origin tree-3-0-2 (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-2-1-3-43 = refl
occ-2-1-3-44 : P.T.Occurrence tree-2-1-3
occ-2-1-3-44 = (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.source-leg , tt)))
origin-2-1-3-44 : P.T.origin tree-2-1-3 occ-2-1-3-44 ≡ input s02
origin-2-1-3-44 = refl
transport-2-1-3-44 : P.T.origin tree-3-0-2 (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-2-1-3-44 = refl
occ-2-1-3-45 : P.T.Occurrence tree-2-1-3
occ-2-1-3-45 = (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.target-leg , tt)))
origin-2-1-3-45 : P.T.origin tree-2-1-3 occ-2-1-3-45 ≡ input s12
origin-2-1-3-45 = refl
transport-2-1-3-45 : P.T.origin tree-3-0-2 (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.target-leg , tt))) ≡ input (swap s12)
transport-2-1-3-45 = refl
occ-2-1-3-46 : P.T.Occurrence tree-2-1-3
occ-2-1-3-46 = (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.source-leg , tt)))
origin-2-1-3-46 : P.T.origin tree-2-1-3 occ-2-1-3-46 ≡ input s02
origin-2-1-3-46 = refl
transport-2-1-3-46 : P.T.origin tree-3-0-2 (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-2-1-3-46 = refl
occ-2-1-3-47 : P.T.Occurrence tree-2-1-3
occ-2-1-3-47 = (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.target-leg , tt)))
origin-2-1-3-47 : P.T.origin tree-2-1-3 occ-2-1-3-47 ≡ input s32
origin-2-1-3-47 = refl
transport-2-1-3-47 : P.T.origin tree-3-0-2 (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.target-leg , tt))) ≡ input (swap s32)
transport-2-1-3-47 = refl
occ-2-1-3-48 : P.T.Occurrence tree-2-1-3
occ-2-1-3-48 = (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-2-1-3-48 : P.T.origin tree-2-1-3 occ-2-1-3-48 ≡ input s03
origin-2-1-3-48 = refl
transport-2-1-3-48 : P.T.origin tree-3-0-2 (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s03)
transport-2-1-3-48 = refl
occ-2-1-3-49 : P.T.Occurrence tree-2-1-3
occ-2-1-3-49 = (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-2-1-3-49 : P.T.origin tree-2-1-3 occ-2-1-3-49 ≡ input s13
origin-2-1-3-49 = refl
transport-2-1-3-49 : P.T.origin tree-3-0-2 (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-2-1-3-49 = refl
occ-2-1-3-50 : P.T.Occurrence tree-2-1-3
occ-2-1-3-50 = (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-2-1-3-50 : P.T.origin tree-2-1-3 occ-2-1-3-50 ≡ input s23
origin-2-1-3-50 = refl
transport-2-1-3-50 : P.T.origin tree-3-0-2 (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s23)
transport-2-1-3-50 = refl
occ-2-1-3-51 : P.T.Occurrence tree-2-1-3
occ-2-1-3-51 = (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-2-1-3-51 : P.T.origin tree-2-1-3 occ-2-1-3-51 ≡ input s13
origin-2-1-3-51 = refl
transport-2-1-3-51 : P.T.origin tree-3-0-2 (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-2-1-3-51 = refl
occ-2-1-3-52 : P.T.Occurrence tree-2-1-3
occ-2-1-3-52 = (P.S.full-source , (P.S.first-port , tt))
origin-2-1-3-52 : P.T.origin tree-2-1-3 occ-2-1-3-52 ≡ input s20
origin-2-1-3-52 = refl
transport-2-1-3-52 : P.T.origin tree-3-0-2 (P.S.full-source , (P.S.first-port , tt)) ≡ input (swap s20)
transport-2-1-3-52 = refl
occ-2-1-3-53 : P.T.Occurrence tree-2-1-3
occ-2-1-3-53 = (P.S.full-source , (P.S.middle-port , tt))
origin-2-1-3-53 : P.T.origin tree-2-1-3 occ-2-1-3-53 ≡ input s10
origin-2-1-3-53 = refl
transport-2-1-3-53 : P.T.origin tree-3-0-2 (P.S.full-source , (P.S.middle-port , tt)) ≡ input (swap s10)
transport-2-1-3-53 = refl
occ-2-1-3-54 : P.T.Occurrence tree-2-1-3
occ-2-1-3-54 = (P.S.full-source , (P.S.final-port , tt))
origin-2-1-3-54 : P.T.origin tree-2-1-3 occ-2-1-3-54 ≡ input s30
origin-2-1-3-54 = refl
transport-2-1-3-54 : P.T.origin tree-3-0-2 (P.S.full-source , (P.S.final-port , tt)) ≡ input (swap s30)
transport-2-1-3-54 = refl
selected-source-2-1-3-AB : P.S.ab-index {a = C.q0} {b = C.q7} {c = C.q7} F.triple-2-1-3 ≡ (c0 , (F.vp-2-0 , F.vp-1-0))
selected-source-2-1-3-AB = refl
selected-target-2-1-3-AB : P.S.ab-index {a = C.q7} {b = C.q0} {c = C.q0} F.triple-3-0-2 ≡ (m0 , (F.vp-3-1 , F.vp-0-1))
selected-target-2-1-3-AB = refl
selected-source-2-1-3-BC : P.S.bc-index {a = C.q0} {b = C.q7} {c = C.q7} F.triple-2-1-3 ≡ (c0 , (F.vp-1-0 , F.vp-3-0))
selected-source-2-1-3-BC = refl
selected-target-2-1-3-BC : P.S.bc-index {a = C.q7} {b = C.q0} {c = C.q0} F.triple-3-0-2 ≡ (m0 , (F.vp-0-1 , F.vp-2-1))
selected-target-2-1-3-BC = refl
selected-source-2-1-3-AC : P.S.ac-index {a = C.q0} {b = C.q7} {c = C.q7} F.triple-2-1-3 ≡ (c0 , (F.vp-2-0 , F.vp-3-0))
selected-source-2-1-3-AC = refl
selected-target-2-1-3-AC : P.S.ac-index {a = C.q7} {b = C.q0} {c = C.q0} F.triple-3-0-2 ≡ (m0 , (F.vp-3-1 , F.vp-2-1))
selected-target-2-1-3-AC = refl
occ-2-3-0-0 : P.T.Occurrence tree-2-3-0
occ-2-3-0-0 = (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.source-leg , tt)))
origin-2-3-0-0 : P.T.origin tree-2-3-0 occ-2-3-0-0 ≡ input s20
origin-2-3-0-0 = refl
transport-2-3-0-0 : P.T.origin tree-3-2-1 (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-2-3-0-0 = refl
occ-2-3-0-1 : P.T.Occurrence tree-2-3-0
occ-2-3-0-1 = (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.target-leg , tt)))
origin-2-3-0-1 : P.T.origin tree-2-3-0 occ-2-3-0-1 ≡ input s10
origin-2-3-0-1 = refl
transport-2-3-0-1 : P.T.origin tree-3-2-1 (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.target-leg , tt))) ≡ input (swap s10)
transport-2-3-0-1 = refl
occ-2-3-0-2 : P.T.Occurrence tree-2-3-0
occ-2-3-0-2 = (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.source-leg , tt)))
origin-2-3-0-2 : P.T.origin tree-2-3-0 occ-2-3-0-2 ≡ input s20
origin-2-3-0-2 = refl
transport-2-3-0-2 : P.T.origin tree-3-2-1 (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-2-3-0-2 = refl
occ-2-3-0-3 : P.T.Occurrence tree-2-3-0
occ-2-3-0-3 = (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.target-leg , tt)))
origin-2-3-0-3 : P.T.origin tree-2-3-0 occ-2-3-0-3 ≡ input s30
origin-2-3-0-3 = refl
transport-2-3-0-3 : P.T.origin tree-3-2-1 (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.target-leg , tt))) ≡ input (swap s30)
transport-2-3-0-3 = refl
occ-2-3-0-4 : P.T.Occurrence tree-2-3-0
occ-2-3-0-4 = (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-2-3-0-4 : P.T.origin tree-2-3-0 occ-2-3-0-4 ≡ input s01
origin-2-3-0-4 = refl
transport-2-3-0-4 : P.T.origin tree-3-2-1 (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s01)
transport-2-3-0-4 = refl
occ-2-3-0-5 : P.T.Occurrence tree-2-3-0
occ-2-3-0-5 = (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-2-3-0-5 : P.T.origin tree-2-3-0 occ-2-3-0-5 ≡ input s31
origin-2-3-0-5 = refl
transport-2-3-0-5 : P.T.origin tree-3-2-1 (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-2-3-0-5 = refl
occ-2-3-0-6 : P.T.Occurrence tree-2-3-0
occ-2-3-0-6 = (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-2-3-0-6 : P.T.origin tree-2-3-0 occ-2-3-0-6 ≡ input s21
origin-2-3-0-6 = refl
transport-2-3-0-6 : P.T.origin tree-3-2-1 (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s21)
transport-2-3-0-6 = refl
occ-2-3-0-7 : P.T.Occurrence tree-2-3-0
occ-2-3-0-7 = (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-2-3-0-7 : P.T.origin tree-2-3-0 occ-2-3-0-7 ≡ input s31
origin-2-3-0-7 = refl
transport-2-3-0-7 : P.T.origin tree-3-2-1 (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-2-3-0-7 = refl
occ-2-3-0-8 : P.T.Occurrence tree-2-3-0
occ-2-3-0-8 = (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.source-leg , tt)))
origin-2-3-0-8 : P.T.origin tree-2-3-0 occ-2-3-0-8 ≡ input s02
origin-2-3-0-8 = refl
transport-2-3-0-8 : P.T.origin tree-3-2-1 (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-2-3-0-8 = refl
occ-2-3-0-9 : P.T.Occurrence tree-2-3-0
occ-2-3-0-9 = (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.target-leg , tt)))
origin-2-3-0-9 : P.T.origin tree-2-3-0 occ-2-3-0-9 ≡ input s12
origin-2-3-0-9 = refl
transport-2-3-0-9 : P.T.origin tree-3-2-1 (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.target-leg , tt))) ≡ input (swap s12)
transport-2-3-0-9 = refl
occ-2-3-0-10 : P.T.Occurrence tree-2-3-0
occ-2-3-0-10 = (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.source-leg , tt)))
origin-2-3-0-10 : P.T.origin tree-2-3-0 occ-2-3-0-10 ≡ input s02
origin-2-3-0-10 = refl
transport-2-3-0-10 : P.T.origin tree-3-2-1 (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-2-3-0-10 = refl
occ-2-3-0-11 : P.T.Occurrence tree-2-3-0
occ-2-3-0-11 = (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.target-leg , tt)))
origin-2-3-0-11 : P.T.origin tree-2-3-0 occ-2-3-0-11 ≡ input s32
origin-2-3-0-11 = refl
transport-2-3-0-11 : P.T.origin tree-3-2-1 (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.target-leg , tt))) ≡ input (swap s32)
transport-2-3-0-11 = refl
occ-2-3-0-12 : P.T.Occurrence tree-2-3-0
occ-2-3-0-12 = (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-2-3-0-12 : P.T.origin tree-2-3-0 occ-2-3-0-12 ≡ input s03
origin-2-3-0-12 = refl
transport-2-3-0-12 : P.T.origin tree-3-2-1 (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s03)
transport-2-3-0-12 = refl
occ-2-3-0-13 : P.T.Occurrence tree-2-3-0
occ-2-3-0-13 = (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-2-3-0-13 : P.T.origin tree-2-3-0 occ-2-3-0-13 ≡ input s13
origin-2-3-0-13 = refl
transport-2-3-0-13 : P.T.origin tree-3-2-1 (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-2-3-0-13 = refl
occ-2-3-0-14 : P.T.Occurrence tree-2-3-0
occ-2-3-0-14 = (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-2-3-0-14 : P.T.origin tree-2-3-0 occ-2-3-0-14 ≡ input s23
origin-2-3-0-14 = refl
transport-2-3-0-14 : P.T.origin tree-3-2-1 (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s23)
transport-2-3-0-14 = refl
occ-2-3-0-15 : P.T.Occurrence tree-2-3-0
occ-2-3-0-15 = (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-2-3-0-15 : P.T.origin tree-2-3-0 occ-2-3-0-15 ≡ input s13
origin-2-3-0-15 = refl
transport-2-3-0-15 : P.T.origin tree-3-2-1 (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-2-3-0-15 = refl
occ-2-3-0-16 : P.T.Occurrence tree-2-3-0
occ-2-3-0-16 = (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-2-3-0-16 : P.T.origin tree-2-3-0 occ-2-3-0-16 ≡ input s10
origin-2-3-0-16 = refl
transport-2-3-0-16 : P.T.origin tree-3-2-1 (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s10)
transport-2-3-0-16 = refl
occ-2-3-0-17 : P.T.Occurrence tree-2-3-0
occ-2-3-0-17 = (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-2-3-0-17 : P.T.origin tree-2-3-0 occ-2-3-0-17 ≡ input s20
origin-2-3-0-17 = refl
transport-2-3-0-17 : P.T.origin tree-3-2-1 (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-2-3-0-17 = refl
occ-2-3-0-18 : P.T.Occurrence tree-2-3-0
occ-2-3-0-18 = (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-2-3-0-18 : P.T.origin tree-2-3-0 occ-2-3-0-18 ≡ input s30
origin-2-3-0-18 = refl
transport-2-3-0-18 : P.T.origin tree-3-2-1 (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s30)
transport-2-3-0-18 = refl
occ-2-3-0-19 : P.T.Occurrence tree-2-3-0
occ-2-3-0-19 = (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-2-3-0-19 : P.T.origin tree-2-3-0 occ-2-3-0-19 ≡ input s20
origin-2-3-0-19 = refl
transport-2-3-0-19 : P.T.origin tree-3-2-1 (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-2-3-0-19 = refl
occ-2-3-0-20 : P.T.Occurrence tree-2-3-0
occ-2-3-0-20 = (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.source-leg , tt)))
origin-2-3-0-20 : P.T.origin tree-2-3-0 occ-2-3-0-20 ≡ input s31
origin-2-3-0-20 = refl
transport-2-3-0-20 : P.T.origin tree-3-2-1 (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-2-3-0-20 = refl
occ-2-3-0-21 : P.T.Occurrence tree-2-3-0
occ-2-3-0-21 = (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.target-leg , tt)))
origin-2-3-0-21 : P.T.origin tree-2-3-0 occ-2-3-0-21 ≡ input s01
origin-2-3-0-21 = refl
transport-2-3-0-21 : P.T.origin tree-3-2-1 (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.target-leg , tt))) ≡ input (swap s01)
transport-2-3-0-21 = refl
occ-2-3-0-22 : P.T.Occurrence tree-2-3-0
occ-2-3-0-22 = (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.source-leg , tt)))
origin-2-3-0-22 : P.T.origin tree-2-3-0 occ-2-3-0-22 ≡ input s31
origin-2-3-0-22 = refl
transport-2-3-0-22 : P.T.origin tree-3-2-1 (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-2-3-0-22 = refl
occ-2-3-0-23 : P.T.Occurrence tree-2-3-0
occ-2-3-0-23 = (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.target-leg , tt)))
origin-2-3-0-23 : P.T.origin tree-2-3-0 occ-2-3-0-23 ≡ input s21
origin-2-3-0-23 = refl
transport-2-3-0-23 : P.T.origin tree-3-2-1 (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.target-leg , tt))) ≡ input (swap s21)
transport-2-3-0-23 = refl
occ-2-3-0-24 : P.T.Occurrence tree-2-3-0
occ-2-3-0-24 = (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-2-3-0-24 : P.T.origin tree-2-3-0 occ-2-3-0-24 ≡ input s12
origin-2-3-0-24 = refl
transport-2-3-0-24 : P.T.origin tree-3-2-1 (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s12)
transport-2-3-0-24 = refl
occ-2-3-0-25 : P.T.Occurrence tree-2-3-0
occ-2-3-0-25 = (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-2-3-0-25 : P.T.origin tree-2-3-0 occ-2-3-0-25 ≡ input s02
origin-2-3-0-25 = refl
transport-2-3-0-25 : P.T.origin tree-3-2-1 (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-2-3-0-25 = refl
occ-2-3-0-26 : P.T.Occurrence tree-2-3-0
occ-2-3-0-26 = (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-2-3-0-26 : P.T.origin tree-2-3-0 occ-2-3-0-26 ≡ input s32
origin-2-3-0-26 = refl
transport-2-3-0-26 : P.T.origin tree-3-2-1 (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s32)
transport-2-3-0-26 = refl
occ-2-3-0-27 : P.T.Occurrence tree-2-3-0
occ-2-3-0-27 = (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-2-3-0-27 : P.T.origin tree-2-3-0 occ-2-3-0-27 ≡ input s02
origin-2-3-0-27 = refl
transport-2-3-0-27 : P.T.origin tree-3-2-1 (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-2-3-0-27 = refl
occ-2-3-0-28 : P.T.Occurrence tree-2-3-0
occ-2-3-0-28 = (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.source-leg , tt)))
origin-2-3-0-28 : P.T.origin tree-2-3-0 occ-2-3-0-28 ≡ input s13
origin-2-3-0-28 = refl
transport-2-3-0-28 : P.T.origin tree-3-2-1 (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-2-3-0-28 = refl
occ-2-3-0-29 : P.T.Occurrence tree-2-3-0
occ-2-3-0-29 = (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.target-leg , tt)))
origin-2-3-0-29 : P.T.origin tree-2-3-0 occ-2-3-0-29 ≡ input s03
origin-2-3-0-29 = refl
transport-2-3-0-29 : P.T.origin tree-3-2-1 (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.target-leg , tt))) ≡ input (swap s03)
transport-2-3-0-29 = refl
occ-2-3-0-30 : P.T.Occurrence tree-2-3-0
occ-2-3-0-30 = (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.source-leg , tt)))
origin-2-3-0-30 : P.T.origin tree-2-3-0 occ-2-3-0-30 ≡ input s13
origin-2-3-0-30 = refl
transport-2-3-0-30 : P.T.origin tree-3-2-1 (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-2-3-0-30 = refl
occ-2-3-0-31 : P.T.Occurrence tree-2-3-0
occ-2-3-0-31 = (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.target-leg , tt)))
origin-2-3-0-31 : P.T.origin tree-2-3-0 occ-2-3-0-31 ≡ input s23
origin-2-3-0-31 = refl
transport-2-3-0-31 : P.T.origin tree-3-2-1 (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.target-leg , tt))) ≡ input (swap s23)
transport-2-3-0-31 = refl
occ-2-3-0-32 : P.T.Occurrence tree-2-3-0
occ-2-3-0-32 = (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-2-3-0-32 : P.T.origin tree-2-3-0 occ-2-3-0-32 ≡ input s20
origin-2-3-0-32 = refl
transport-2-3-0-32 : P.T.origin tree-3-2-1 (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-2-3-0-32 = refl
occ-2-3-0-33 : P.T.Occurrence tree-2-3-0
occ-2-3-0-33 = (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-2-3-0-33 : P.T.origin tree-2-3-0 occ-2-3-0-33 ≡ input s20
origin-2-3-0-33 = refl
transport-2-3-0-33 : P.T.origin tree-3-2-1 (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-2-3-0-33 = refl
occ-2-3-0-34 : P.T.Occurrence tree-2-3-0
occ-2-3-0-34 = (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-0-1)) , (P.S.source-leg , tt)))
origin-2-3-0-34 : P.T.origin tree-2-3-0 occ-2-3-0-34 ≡ input s01
origin-2-3-0-34 = refl
transport-2-3-0-34 : P.T.origin tree-3-2-1 (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-1-0)) , (P.S.source-leg , tt))) ≡ input (swap s01)
transport-2-3-0-34 = refl
occ-2-3-0-35 : P.T.Occurrence tree-2-3-0
occ-2-3-0-35 = (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-0-1)) , (P.S.target-leg , tt)))
origin-2-3-0-35 : P.T.origin tree-2-3-0 occ-2-3-0-35 ≡ input s01
origin-2-3-0-35 = refl
transport-2-3-0-35 : P.T.origin tree-3-2-1 (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-1-0)) , (P.S.target-leg , tt))) ≡ input (swap s01)
transport-2-3-0-35 = refl
occ-2-3-0-36 : P.T.Occurrence tree-2-3-0
occ-2-3-0-36 = (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.source-leg , tt)))
origin-2-3-0-36 : P.T.origin tree-2-3-0 occ-2-3-0-36 ≡ input s01
origin-2-3-0-36 = refl
transport-2-3-0-36 : P.T.origin tree-3-2-1 (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.source-leg , tt))) ≡ input (swap s01)
transport-2-3-0-36 = refl
occ-2-3-0-37 : P.T.Occurrence tree-2-3-0
occ-2-3-0-37 = (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.target-leg , tt)))
origin-2-3-0-37 : P.T.origin tree-2-3-0 occ-2-3-0-37 ≡ input s21
origin-2-3-0-37 = refl
transport-2-3-0-37 : P.T.origin tree-3-2-1 (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.target-leg , tt))) ≡ input (swap s21)
transport-2-3-0-37 = refl
occ-2-3-0-38 : P.T.Occurrence tree-2-3-0
occ-2-3-0-38 = (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.source-leg , tt)))
origin-2-3-0-38 : P.T.origin tree-2-3-0 occ-2-3-0-38 ≡ input s21
origin-2-3-0-38 = refl
transport-2-3-0-38 : P.T.origin tree-3-2-1 (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.source-leg , tt))) ≡ input (swap s21)
transport-2-3-0-38 = refl
occ-2-3-0-39 : P.T.Occurrence tree-2-3-0
occ-2-3-0-39 = (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.target-leg , tt)))
origin-2-3-0-39 : P.T.origin tree-2-3-0 occ-2-3-0-39 ≡ input s01
origin-2-3-0-39 = refl
transport-2-3-0-39 : P.T.origin tree-3-2-1 (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.target-leg , tt))) ≡ input (swap s01)
transport-2-3-0-39 = refl
occ-2-3-0-40 : P.T.Occurrence tree-2-3-0
occ-2-3-0-40 = (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-2-1)) , (P.S.source-leg , tt)))
origin-2-3-0-40 : P.T.origin tree-2-3-0 occ-2-3-0-40 ≡ input s21
origin-2-3-0-40 = refl
transport-2-3-0-40 : P.T.origin tree-3-2-1 (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-3-0)) , (P.S.source-leg , tt))) ≡ input (swap s21)
transport-2-3-0-40 = refl
occ-2-3-0-41 : P.T.Occurrence tree-2-3-0
occ-2-3-0-41 = (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-2-1)) , (P.S.target-leg , tt)))
origin-2-3-0-41 : P.T.origin tree-2-3-0 occ-2-3-0-41 ≡ input s21
origin-2-3-0-41 = refl
transport-2-3-0-41 : P.T.origin tree-3-2-1 (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-3-0)) , (P.S.target-leg , tt))) ≡ input (swap s21)
transport-2-3-0-41 = refl
occ-2-3-0-42 : P.T.Occurrence tree-2-3-0
occ-2-3-0-42 = (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-2-3-0-42 : P.T.origin tree-2-3-0 occ-2-3-0-42 ≡ input s02
origin-2-3-0-42 = refl
transport-2-3-0-42 : P.T.origin tree-3-2-1 (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-2-3-0-42 = refl
occ-2-3-0-43 : P.T.Occurrence tree-2-3-0
occ-2-3-0-43 = (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-2-3-0-43 : P.T.origin tree-2-3-0 occ-2-3-0-43 ≡ input s02
origin-2-3-0-43 = refl
transport-2-3-0-43 : P.T.origin tree-3-2-1 (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-2-3-0-43 = refl
occ-2-3-0-44 : P.T.Occurrence tree-2-3-0
occ-2-3-0-44 = (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-0-3)) , (P.S.source-leg , tt)))
origin-2-3-0-44 : P.T.origin tree-2-3-0 occ-2-3-0-44 ≡ input s03
origin-2-3-0-44 = refl
transport-2-3-0-44 : P.T.origin tree-3-2-1 (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-1-2)) , (P.S.source-leg , tt))) ≡ input (swap s03)
transport-2-3-0-44 = refl
occ-2-3-0-45 : P.T.Occurrence tree-2-3-0
occ-2-3-0-45 = (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-0-3)) , (P.S.target-leg , tt)))
origin-2-3-0-45 : P.T.origin tree-2-3-0 occ-2-3-0-45 ≡ input s03
origin-2-3-0-45 = refl
transport-2-3-0-45 : P.T.origin tree-3-2-1 (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-1-2)) , (P.S.target-leg , tt))) ≡ input (swap s03)
transport-2-3-0-45 = refl
occ-2-3-0-46 : P.T.Occurrence tree-2-3-0
occ-2-3-0-46 = (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.source-leg , tt)))
origin-2-3-0-46 : P.T.origin tree-2-3-0 occ-2-3-0-46 ≡ input s03
origin-2-3-0-46 = refl
transport-2-3-0-46 : P.T.origin tree-3-2-1 (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.source-leg , tt))) ≡ input (swap s03)
transport-2-3-0-46 = refl
occ-2-3-0-47 : P.T.Occurrence tree-2-3-0
occ-2-3-0-47 = (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.target-leg , tt)))
origin-2-3-0-47 : P.T.origin tree-2-3-0 occ-2-3-0-47 ≡ input s23
origin-2-3-0-47 = refl
transport-2-3-0-47 : P.T.origin tree-3-2-1 (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.target-leg , tt))) ≡ input (swap s23)
transport-2-3-0-47 = refl
occ-2-3-0-48 : P.T.Occurrence tree-2-3-0
occ-2-3-0-48 = (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.source-leg , tt)))
origin-2-3-0-48 : P.T.origin tree-2-3-0 occ-2-3-0-48 ≡ input s23
origin-2-3-0-48 = refl
transport-2-3-0-48 : P.T.origin tree-3-2-1 (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.source-leg , tt))) ≡ input (swap s23)
transport-2-3-0-48 = refl
occ-2-3-0-49 : P.T.Occurrence tree-2-3-0
occ-2-3-0-49 = (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.target-leg , tt)))
origin-2-3-0-49 : P.T.origin tree-2-3-0 occ-2-3-0-49 ≡ input s03
origin-2-3-0-49 = refl
transport-2-3-0-49 : P.T.origin tree-3-2-1 (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.target-leg , tt))) ≡ input (swap s03)
transport-2-3-0-49 = refl
occ-2-3-0-50 : P.T.Occurrence tree-2-3-0
occ-2-3-0-50 = (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-2-3)) , (P.S.source-leg , tt)))
origin-2-3-0-50 : P.T.origin tree-2-3-0 occ-2-3-0-50 ≡ input s23
origin-2-3-0-50 = refl
transport-2-3-0-50 : P.T.origin tree-3-2-1 (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-3-2)) , (P.S.source-leg , tt))) ≡ input (swap s23)
transport-2-3-0-50 = refl
occ-2-3-0-51 : P.T.Occurrence tree-2-3-0
occ-2-3-0-51 = (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-2-3)) , (P.S.target-leg , tt)))
origin-2-3-0-51 : P.T.origin tree-2-3-0 occ-2-3-0-51 ≡ input s23
origin-2-3-0-51 = refl
transport-2-3-0-51 : P.T.origin tree-3-2-1 (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-3-2)) , (P.S.target-leg , tt))) ≡ input (swap s23)
transport-2-3-0-51 = refl
occ-2-3-0-52 : P.T.Occurrence tree-2-3-0
occ-2-3-0-52 = (P.S.full-source , (P.S.first-port , tt))
origin-2-3-0-52 : P.T.origin tree-2-3-0 occ-2-3-0-52 ≡ input s21
origin-2-3-0-52 = refl
transport-2-3-0-52 : P.T.origin tree-3-2-1 (P.S.full-source , (P.S.first-port , tt)) ≡ input (swap s21)
transport-2-3-0-52 = refl
occ-2-3-0-53 : P.T.Occurrence tree-2-3-0
occ-2-3-0-53 = (P.S.full-source , (P.S.middle-port , tt))
origin-2-3-0-53 : P.T.origin tree-2-3-0 occ-2-3-0-53 ≡ input s31
origin-2-3-0-53 = refl
transport-2-3-0-53 : P.T.origin tree-3-2-1 (P.S.full-source , (P.S.middle-port , tt)) ≡ input (swap s31)
transport-2-3-0-53 = refl
occ-2-3-0-54 : P.T.Occurrence tree-2-3-0
occ-2-3-0-54 = (P.S.full-source , (P.S.final-port , tt))
origin-2-3-0-54 : P.T.origin tree-2-3-0 occ-2-3-0-54 ≡ input s01
origin-2-3-0-54 = refl
transport-2-3-0-54 : P.T.origin tree-3-2-1 (P.S.full-source , (P.S.final-port , tt)) ≡ input (swap s01)
transport-2-3-0-54 = refl
selected-source-2-3-0-AB : P.S.ab-index {a = C.q0} {b = C.q7} {c = C.q0} F.triple-2-3-0 ≡ (m0 , (F.vp-2-1 , F.vp-3-1))
selected-source-2-3-0-AB = refl
selected-target-2-3-0-AB : P.S.ab-index {a = C.q7} {b = C.q0} {c = C.q7} F.triple-3-2-1 ≡ (c0 , (F.vp-3-0 , F.vp-2-0))
selected-target-2-3-0-AB = refl
selected-source-2-3-0-BC : P.S.bc-index {a = C.q0} {b = C.q7} {c = C.q0} F.triple-2-3-0 ≡ (m0 , (F.vp-3-1 , F.vp-0-1))
selected-source-2-3-0-BC = refl
selected-target-2-3-0-BC : P.S.bc-index {a = C.q7} {b = C.q0} {c = C.q7} F.triple-3-2-1 ≡ (c0 , (F.vp-2-0 , F.vp-1-0))
selected-target-2-3-0-BC = refl
selected-source-2-3-0-AC : P.S.ac-index {a = C.q0} {b = C.q7} {c = C.q0} F.triple-2-3-0 ≡ (m0 , (F.vp-2-1 , F.vp-0-1))
selected-source-2-3-0-AC = refl
selected-target-2-3-0-AC : P.S.ac-index {a = C.q7} {b = C.q0} {c = C.q7} F.triple-3-2-1 ≡ (c0 , (F.vp-3-0 , F.vp-1-0))
selected-target-2-3-0-AC = refl
occ-2-3-1-0 : P.T.Occurrence tree-2-3-1
occ-2-3-1-0 = (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.source-leg , tt)))
origin-2-3-1-0 : P.T.origin tree-2-3-1 occ-2-3-1-0 ≡ input s20
origin-2-3-1-0 = refl
transport-2-3-1-0 : P.T.origin tree-3-2-0 (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-2-3-1-0 = refl
occ-2-3-1-1 : P.T.Occurrence tree-2-3-1
occ-2-3-1-1 = (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.target-leg , tt)))
origin-2-3-1-1 : P.T.origin tree-2-3-1 occ-2-3-1-1 ≡ input s10
origin-2-3-1-1 = refl
transport-2-3-1-1 : P.T.origin tree-3-2-0 (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.target-leg , tt))) ≡ input (swap s10)
transport-2-3-1-1 = refl
occ-2-3-1-2 : P.T.Occurrence tree-2-3-1
occ-2-3-1-2 = (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.source-leg , tt)))
origin-2-3-1-2 : P.T.origin tree-2-3-1 occ-2-3-1-2 ≡ input s20
origin-2-3-1-2 = refl
transport-2-3-1-2 : P.T.origin tree-3-2-0 (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-2-3-1-2 = refl
occ-2-3-1-3 : P.T.Occurrence tree-2-3-1
occ-2-3-1-3 = (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.target-leg , tt)))
origin-2-3-1-3 : P.T.origin tree-2-3-1 occ-2-3-1-3 ≡ input s30
origin-2-3-1-3 = refl
transport-2-3-1-3 : P.T.origin tree-3-2-0 (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.target-leg , tt))) ≡ input (swap s30)
transport-2-3-1-3 = refl
occ-2-3-1-4 : P.T.Occurrence tree-2-3-1
occ-2-3-1-4 = (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-2-3-1-4 : P.T.origin tree-2-3-1 occ-2-3-1-4 ≡ input s01
origin-2-3-1-4 = refl
transport-2-3-1-4 : P.T.origin tree-3-2-0 (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s01)
transport-2-3-1-4 = refl
occ-2-3-1-5 : P.T.Occurrence tree-2-3-1
occ-2-3-1-5 = (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-2-3-1-5 : P.T.origin tree-2-3-1 occ-2-3-1-5 ≡ input s31
origin-2-3-1-5 = refl
transport-2-3-1-5 : P.T.origin tree-3-2-0 (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-2-3-1-5 = refl
occ-2-3-1-6 : P.T.Occurrence tree-2-3-1
occ-2-3-1-6 = (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-2-3-1-6 : P.T.origin tree-2-3-1 occ-2-3-1-6 ≡ input s21
origin-2-3-1-6 = refl
transport-2-3-1-6 : P.T.origin tree-3-2-0 (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s21)
transport-2-3-1-6 = refl
occ-2-3-1-7 : P.T.Occurrence tree-2-3-1
occ-2-3-1-7 = (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-2-3-1-7 : P.T.origin tree-2-3-1 occ-2-3-1-7 ≡ input s31
origin-2-3-1-7 = refl
transport-2-3-1-7 : P.T.origin tree-3-2-0 (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-2-3-1-7 = refl
occ-2-3-1-8 : P.T.Occurrence tree-2-3-1
occ-2-3-1-8 = (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.source-leg , tt)))
origin-2-3-1-8 : P.T.origin tree-2-3-1 occ-2-3-1-8 ≡ input s02
origin-2-3-1-8 = refl
transport-2-3-1-8 : P.T.origin tree-3-2-0 (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-2-3-1-8 = refl
occ-2-3-1-9 : P.T.Occurrence tree-2-3-1
occ-2-3-1-9 = (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.target-leg , tt)))
origin-2-3-1-9 : P.T.origin tree-2-3-1 occ-2-3-1-9 ≡ input s12
origin-2-3-1-9 = refl
transport-2-3-1-9 : P.T.origin tree-3-2-0 (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.target-leg , tt))) ≡ input (swap s12)
transport-2-3-1-9 = refl
occ-2-3-1-10 : P.T.Occurrence tree-2-3-1
occ-2-3-1-10 = (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.source-leg , tt)))
origin-2-3-1-10 : P.T.origin tree-2-3-1 occ-2-3-1-10 ≡ input s02
origin-2-3-1-10 = refl
transport-2-3-1-10 : P.T.origin tree-3-2-0 (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-2-3-1-10 = refl
occ-2-3-1-11 : P.T.Occurrence tree-2-3-1
occ-2-3-1-11 = (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.target-leg , tt)))
origin-2-3-1-11 : P.T.origin tree-2-3-1 occ-2-3-1-11 ≡ input s32
origin-2-3-1-11 = refl
transport-2-3-1-11 : P.T.origin tree-3-2-0 (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.target-leg , tt))) ≡ input (swap s32)
transport-2-3-1-11 = refl
occ-2-3-1-12 : P.T.Occurrence tree-2-3-1
occ-2-3-1-12 = (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-2-3-1-12 : P.T.origin tree-2-3-1 occ-2-3-1-12 ≡ input s03
origin-2-3-1-12 = refl
transport-2-3-1-12 : P.T.origin tree-3-2-0 (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s03)
transport-2-3-1-12 = refl
occ-2-3-1-13 : P.T.Occurrence tree-2-3-1
occ-2-3-1-13 = (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-2-3-1-13 : P.T.origin tree-2-3-1 occ-2-3-1-13 ≡ input s13
origin-2-3-1-13 = refl
transport-2-3-1-13 : P.T.origin tree-3-2-0 (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-2-3-1-13 = refl
occ-2-3-1-14 : P.T.Occurrence tree-2-3-1
occ-2-3-1-14 = (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-2-3-1-14 : P.T.origin tree-2-3-1 occ-2-3-1-14 ≡ input s23
origin-2-3-1-14 = refl
transport-2-3-1-14 : P.T.origin tree-3-2-0 (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s23)
transport-2-3-1-14 = refl
occ-2-3-1-15 : P.T.Occurrence tree-2-3-1
occ-2-3-1-15 = (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-2-3-1-15 : P.T.origin tree-2-3-1 occ-2-3-1-15 ≡ input s13
origin-2-3-1-15 = refl
transport-2-3-1-15 : P.T.origin tree-3-2-0 (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-2-3-1-15 = refl
occ-2-3-1-16 : P.T.Occurrence tree-2-3-1
occ-2-3-1-16 = (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-1-0)) , (P.S.source-leg , tt)))
origin-2-3-1-16 : P.T.origin tree-2-3-1 occ-2-3-1-16 ≡ input s10
origin-2-3-1-16 = refl
transport-2-3-1-16 : P.T.origin tree-3-2-0 (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-0-1)) , (P.S.source-leg , tt))) ≡ input (swap s10)
transport-2-3-1-16 = refl
occ-2-3-1-17 : P.T.Occurrence tree-2-3-1
occ-2-3-1-17 = (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-1-0)) , (P.S.target-leg , tt)))
origin-2-3-1-17 : P.T.origin tree-2-3-1 occ-2-3-1-17 ≡ input s10
origin-2-3-1-17 = refl
transport-2-3-1-17 : P.T.origin tree-3-2-0 (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-0-1)) , (P.S.target-leg , tt))) ≡ input (swap s10)
transport-2-3-1-17 = refl
occ-2-3-1-18 : P.T.Occurrence tree-2-3-1
occ-2-3-1-18 = (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.source-leg , tt)))
origin-2-3-1-18 : P.T.origin tree-2-3-1 occ-2-3-1-18 ≡ input s10
origin-2-3-1-18 = refl
transport-2-3-1-18 : P.T.origin tree-3-2-0 (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.source-leg , tt))) ≡ input (swap s10)
transport-2-3-1-18 = refl
occ-2-3-1-19 : P.T.Occurrence tree-2-3-1
occ-2-3-1-19 = (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.target-leg , tt)))
origin-2-3-1-19 : P.T.origin tree-2-3-1 occ-2-3-1-19 ≡ input s30
origin-2-3-1-19 = refl
transport-2-3-1-19 : P.T.origin tree-3-2-0 (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.target-leg , tt))) ≡ input (swap s30)
transport-2-3-1-19 = refl
occ-2-3-1-20 : P.T.Occurrence tree-2-3-1
occ-2-3-1-20 = (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.source-leg , tt)))
origin-2-3-1-20 : P.T.origin tree-2-3-1 occ-2-3-1-20 ≡ input s30
origin-2-3-1-20 = refl
transport-2-3-1-20 : P.T.origin tree-3-2-0 (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.source-leg , tt))) ≡ input (swap s30)
transport-2-3-1-20 = refl
occ-2-3-1-21 : P.T.Occurrence tree-2-3-1
occ-2-3-1-21 = (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.target-leg , tt)))
origin-2-3-1-21 : P.T.origin tree-2-3-1 occ-2-3-1-21 ≡ input s10
origin-2-3-1-21 = refl
transport-2-3-1-21 : P.T.origin tree-3-2-0 (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.target-leg , tt))) ≡ input (swap s10)
transport-2-3-1-21 = refl
occ-2-3-1-22 : P.T.Occurrence tree-2-3-1
occ-2-3-1-22 = (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-3-0)) , (P.S.source-leg , tt)))
origin-2-3-1-22 : P.T.origin tree-2-3-1 occ-2-3-1-22 ≡ input s30
origin-2-3-1-22 = refl
transport-2-3-1-22 : P.T.origin tree-3-2-0 (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-2-1)) , (P.S.source-leg , tt))) ≡ input (swap s30)
transport-2-3-1-22 = refl
occ-2-3-1-23 : P.T.Occurrence tree-2-3-1
occ-2-3-1-23 = (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-3-0)) , (P.S.target-leg , tt)))
origin-2-3-1-23 : P.T.origin tree-2-3-1 occ-2-3-1-23 ≡ input s30
origin-2-3-1-23 = refl
transport-2-3-1-23 : P.T.origin tree-3-2-0 (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-2-1)) , (P.S.target-leg , tt))) ≡ input (swap s30)
transport-2-3-1-23 = refl
occ-2-3-1-24 : P.T.Occurrence tree-2-3-1
occ-2-3-1-24 = (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-2-3-1-24 : P.T.origin tree-2-3-1 occ-2-3-1-24 ≡ input s31
origin-2-3-1-24 = refl
transport-2-3-1-24 : P.T.origin tree-3-2-0 (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-2-3-1-24 = refl
occ-2-3-1-25 : P.T.Occurrence tree-2-3-1
occ-2-3-1-25 = (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-2-3-1-25 : P.T.origin tree-2-3-1 occ-2-3-1-25 ≡ input s31
origin-2-3-1-25 = refl
transport-2-3-1-25 : P.T.origin tree-3-2-0 (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-2-3-1-25 = refl
occ-2-3-1-26 : P.T.Occurrence tree-2-3-1
occ-2-3-1-26 = (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-1-2)) , (P.S.source-leg , tt)))
origin-2-3-1-26 : P.T.origin tree-2-3-1 occ-2-3-1-26 ≡ input s12
origin-2-3-1-26 = refl
transport-2-3-1-26 : P.T.origin tree-3-2-0 (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-0-3)) , (P.S.source-leg , tt))) ≡ input (swap s12)
transport-2-3-1-26 = refl
occ-2-3-1-27 : P.T.Occurrence tree-2-3-1
occ-2-3-1-27 = (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-1-2)) , (P.S.target-leg , tt)))
origin-2-3-1-27 : P.T.origin tree-2-3-1 occ-2-3-1-27 ≡ input s12
origin-2-3-1-27 = refl
transport-2-3-1-27 : P.T.origin tree-3-2-0 (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-0-3)) , (P.S.target-leg , tt))) ≡ input (swap s12)
transport-2-3-1-27 = refl
occ-2-3-1-28 : P.T.Occurrence tree-2-3-1
occ-2-3-1-28 = (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.source-leg , tt)))
origin-2-3-1-28 : P.T.origin tree-2-3-1 occ-2-3-1-28 ≡ input s12
origin-2-3-1-28 = refl
transport-2-3-1-28 : P.T.origin tree-3-2-0 (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.source-leg , tt))) ≡ input (swap s12)
transport-2-3-1-28 = refl
occ-2-3-1-29 : P.T.Occurrence tree-2-3-1
occ-2-3-1-29 = (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.target-leg , tt)))
origin-2-3-1-29 : P.T.origin tree-2-3-1 occ-2-3-1-29 ≡ input s32
origin-2-3-1-29 = refl
transport-2-3-1-29 : P.T.origin tree-3-2-0 (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.target-leg , tt))) ≡ input (swap s32)
transport-2-3-1-29 = refl
occ-2-3-1-30 : P.T.Occurrence tree-2-3-1
occ-2-3-1-30 = (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.source-leg , tt)))
origin-2-3-1-30 : P.T.origin tree-2-3-1 occ-2-3-1-30 ≡ input s32
origin-2-3-1-30 = refl
transport-2-3-1-30 : P.T.origin tree-3-2-0 (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.source-leg , tt))) ≡ input (swap s32)
transport-2-3-1-30 = refl
occ-2-3-1-31 : P.T.Occurrence tree-2-3-1
occ-2-3-1-31 = (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.target-leg , tt)))
origin-2-3-1-31 : P.T.origin tree-2-3-1 occ-2-3-1-31 ≡ input s12
origin-2-3-1-31 = refl
transport-2-3-1-31 : P.T.origin tree-3-2-0 (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.target-leg , tt))) ≡ input (swap s12)
transport-2-3-1-31 = refl
occ-2-3-1-32 : P.T.Occurrence tree-2-3-1
occ-2-3-1-32 = (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-3-2)) , (P.S.source-leg , tt)))
origin-2-3-1-32 : P.T.origin tree-2-3-1 occ-2-3-1-32 ≡ input s32
origin-2-3-1-32 = refl
transport-2-3-1-32 : P.T.origin tree-3-2-0 (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-2-3)) , (P.S.source-leg , tt))) ≡ input (swap s32)
transport-2-3-1-32 = refl
occ-2-3-1-33 : P.T.Occurrence tree-2-3-1
occ-2-3-1-33 = (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-3-2)) , (P.S.target-leg , tt)))
origin-2-3-1-33 : P.T.origin tree-2-3-1 occ-2-3-1-33 ≡ input s32
origin-2-3-1-33 = refl
transport-2-3-1-33 : P.T.origin tree-3-2-0 (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-2-3)) , (P.S.target-leg , tt))) ≡ input (swap s32)
transport-2-3-1-33 = refl
occ-2-3-1-34 : P.T.Occurrence tree-2-3-1
occ-2-3-1-34 = (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-2-3-1-34 : P.T.origin tree-2-3-1 occ-2-3-1-34 ≡ input s13
origin-2-3-1-34 = refl
transport-2-3-1-34 : P.T.origin tree-3-2-0 (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-2-3-1-34 = refl
occ-2-3-1-35 : P.T.Occurrence tree-2-3-1
occ-2-3-1-35 = (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-2-3-1-35 : P.T.origin tree-2-3-1 occ-2-3-1-35 ≡ input s13
origin-2-3-1-35 = refl
transport-2-3-1-35 : P.T.origin tree-3-2-0 (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-2-3-1-35 = refl
occ-2-3-1-36 : P.T.Occurrence tree-2-3-1
occ-2-3-1-36 = (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.source-leg , tt)))
origin-2-3-1-36 : P.T.origin tree-2-3-1 occ-2-3-1-36 ≡ input s20
origin-2-3-1-36 = refl
transport-2-3-1-36 : P.T.origin tree-3-2-0 (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-2-3-1-36 = refl
occ-2-3-1-37 : P.T.Occurrence tree-2-3-1
occ-2-3-1-37 = (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.target-leg , tt)))
origin-2-3-1-37 : P.T.origin tree-2-3-1 occ-2-3-1-37 ≡ input s10
origin-2-3-1-37 = refl
transport-2-3-1-37 : P.T.origin tree-3-2-0 (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.target-leg , tt))) ≡ input (swap s10)
transport-2-3-1-37 = refl
occ-2-3-1-38 : P.T.Occurrence tree-2-3-1
occ-2-3-1-38 = (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.source-leg , tt)))
origin-2-3-1-38 : P.T.origin tree-2-3-1 occ-2-3-1-38 ≡ input s20
origin-2-3-1-38 = refl
transport-2-3-1-38 : P.T.origin tree-3-2-0 (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-2-3-1-38 = refl
occ-2-3-1-39 : P.T.Occurrence tree-2-3-1
occ-2-3-1-39 = (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.target-leg , tt)))
origin-2-3-1-39 : P.T.origin tree-2-3-1 occ-2-3-1-39 ≡ input s30
origin-2-3-1-39 = refl
transport-2-3-1-39 : P.T.origin tree-3-2-0 (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.target-leg , tt))) ≡ input (swap s30)
transport-2-3-1-39 = refl
occ-2-3-1-40 : P.T.Occurrence tree-2-3-1
occ-2-3-1-40 = (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-2-3-1-40 : P.T.origin tree-2-3-1 occ-2-3-1-40 ≡ input s01
origin-2-3-1-40 = refl
transport-2-3-1-40 : P.T.origin tree-3-2-0 (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s01)
transport-2-3-1-40 = refl
occ-2-3-1-41 : P.T.Occurrence tree-2-3-1
occ-2-3-1-41 = (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-2-3-1-41 : P.T.origin tree-2-3-1 occ-2-3-1-41 ≡ input s31
origin-2-3-1-41 = refl
transport-2-3-1-41 : P.T.origin tree-3-2-0 (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-2-3-1-41 = refl
occ-2-3-1-42 : P.T.Occurrence tree-2-3-1
occ-2-3-1-42 = (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-2-3-1-42 : P.T.origin tree-2-3-1 occ-2-3-1-42 ≡ input s21
origin-2-3-1-42 = refl
transport-2-3-1-42 : P.T.origin tree-3-2-0 (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s21)
transport-2-3-1-42 = refl
occ-2-3-1-43 : P.T.Occurrence tree-2-3-1
occ-2-3-1-43 = (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-2-3-1-43 : P.T.origin tree-2-3-1 occ-2-3-1-43 ≡ input s31
origin-2-3-1-43 = refl
transport-2-3-1-43 : P.T.origin tree-3-2-0 (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-2-3-1-43 = refl
occ-2-3-1-44 : P.T.Occurrence tree-2-3-1
occ-2-3-1-44 = (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.source-leg , tt)))
origin-2-3-1-44 : P.T.origin tree-2-3-1 occ-2-3-1-44 ≡ input s02
origin-2-3-1-44 = refl
transport-2-3-1-44 : P.T.origin tree-3-2-0 (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-2-3-1-44 = refl
occ-2-3-1-45 : P.T.Occurrence tree-2-3-1
occ-2-3-1-45 = (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.target-leg , tt)))
origin-2-3-1-45 : P.T.origin tree-2-3-1 occ-2-3-1-45 ≡ input s12
origin-2-3-1-45 = refl
transport-2-3-1-45 : P.T.origin tree-3-2-0 (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.target-leg , tt))) ≡ input (swap s12)
transport-2-3-1-45 = refl
occ-2-3-1-46 : P.T.Occurrence tree-2-3-1
occ-2-3-1-46 = (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.source-leg , tt)))
origin-2-3-1-46 : P.T.origin tree-2-3-1 occ-2-3-1-46 ≡ input s02
origin-2-3-1-46 = refl
transport-2-3-1-46 : P.T.origin tree-3-2-0 (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-2-3-1-46 = refl
occ-2-3-1-47 : P.T.Occurrence tree-2-3-1
occ-2-3-1-47 = (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.target-leg , tt)))
origin-2-3-1-47 : P.T.origin tree-2-3-1 occ-2-3-1-47 ≡ input s32
origin-2-3-1-47 = refl
transport-2-3-1-47 : P.T.origin tree-3-2-0 (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.target-leg , tt))) ≡ input (swap s32)
transport-2-3-1-47 = refl
occ-2-3-1-48 : P.T.Occurrence tree-2-3-1
occ-2-3-1-48 = (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-2-3-1-48 : P.T.origin tree-2-3-1 occ-2-3-1-48 ≡ input s03
origin-2-3-1-48 = refl
transport-2-3-1-48 : P.T.origin tree-3-2-0 (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s03)
transport-2-3-1-48 = refl
occ-2-3-1-49 : P.T.Occurrence tree-2-3-1
occ-2-3-1-49 = (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-2-3-1-49 : P.T.origin tree-2-3-1 occ-2-3-1-49 ≡ input s13
origin-2-3-1-49 = refl
transport-2-3-1-49 : P.T.origin tree-3-2-0 (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-2-3-1-49 = refl
occ-2-3-1-50 : P.T.Occurrence tree-2-3-1
occ-2-3-1-50 = (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-2-3-1-50 : P.T.origin tree-2-3-1 occ-2-3-1-50 ≡ input s23
origin-2-3-1-50 = refl
transport-2-3-1-50 : P.T.origin tree-3-2-0 (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s23)
transport-2-3-1-50 = refl
occ-2-3-1-51 : P.T.Occurrence tree-2-3-1
occ-2-3-1-51 = (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-2-3-1-51 : P.T.origin tree-2-3-1 occ-2-3-1-51 ≡ input s13
origin-2-3-1-51 = refl
transport-2-3-1-51 : P.T.origin tree-3-2-0 (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-2-3-1-51 = refl
occ-2-3-1-52 : P.T.Occurrence tree-2-3-1
occ-2-3-1-52 = (P.S.full-source , (P.S.first-port , tt))
origin-2-3-1-52 : P.T.origin tree-2-3-1 occ-2-3-1-52 ≡ input s20
origin-2-3-1-52 = refl
transport-2-3-1-52 : P.T.origin tree-3-2-0 (P.S.full-source , (P.S.first-port , tt)) ≡ input (swap s20)
transport-2-3-1-52 = refl
occ-2-3-1-53 : P.T.Occurrence tree-2-3-1
occ-2-3-1-53 = (P.S.full-source , (P.S.middle-port , tt))
origin-2-3-1-53 : P.T.origin tree-2-3-1 occ-2-3-1-53 ≡ input s30
origin-2-3-1-53 = refl
transport-2-3-1-53 : P.T.origin tree-3-2-0 (P.S.full-source , (P.S.middle-port , tt)) ≡ input (swap s30)
transport-2-3-1-53 = refl
occ-2-3-1-54 : P.T.Occurrence tree-2-3-1
occ-2-3-1-54 = (P.S.full-source , (P.S.final-port , tt))
origin-2-3-1-54 : P.T.origin tree-2-3-1 occ-2-3-1-54 ≡ input s10
origin-2-3-1-54 = refl
transport-2-3-1-54 : P.T.origin tree-3-2-0 (P.S.full-source , (P.S.final-port , tt)) ≡ input (swap s10)
transport-2-3-1-54 = refl
selected-source-2-3-1-AB : P.S.ab-index {a = C.q0} {b = C.q7} {c = C.q7} F.triple-2-3-1 ≡ (c0 , (F.vp-2-0 , F.vp-3-0))
selected-source-2-3-1-AB = refl
selected-target-2-3-1-AB : P.S.ab-index {a = C.q7} {b = C.q0} {c = C.q0} F.triple-3-2-0 ≡ (m0 , (F.vp-3-1 , F.vp-2-1))
selected-target-2-3-1-AB = refl
selected-source-2-3-1-BC : P.S.bc-index {a = C.q0} {b = C.q7} {c = C.q7} F.triple-2-3-1 ≡ (c0 , (F.vp-3-0 , F.vp-1-0))
selected-source-2-3-1-BC = refl
selected-target-2-3-1-BC : P.S.bc-index {a = C.q7} {b = C.q0} {c = C.q0} F.triple-3-2-0 ≡ (m0 , (F.vp-2-1 , F.vp-0-1))
selected-target-2-3-1-BC = refl
selected-source-2-3-1-AC : P.S.ac-index {a = C.q0} {b = C.q7} {c = C.q7} F.triple-2-3-1 ≡ (c0 , (F.vp-2-0 , F.vp-1-0))
selected-source-2-3-1-AC = refl
selected-target-2-3-1-AC : P.S.ac-index {a = C.q7} {b = C.q0} {c = C.q0} F.triple-3-2-0 ≡ (m0 , (F.vp-3-1 , F.vp-0-1))
selected-target-2-3-1-AC = refl
occ-3-0-1-0 : P.T.Occurrence tree-3-0-1
occ-3-0-1-0 = (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-3-0-1-0 : P.T.origin tree-3-0-1 occ-3-0-1-0 ≡ input s10
origin-3-0-1-0 = refl
transport-3-0-1-0 : P.T.origin tree-2-1-0 (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s10)
transport-3-0-1-0 = refl
occ-3-0-1-1 : P.T.Occurrence tree-3-0-1
occ-3-0-1-1 = (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-3-0-1-1 : P.T.origin tree-3-0-1 occ-3-0-1-1 ≡ input s20
origin-3-0-1-1 = refl
transport-3-0-1-1 : P.T.origin tree-2-1-0 (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-3-0-1-1 = refl
occ-3-0-1-2 : P.T.Occurrence tree-3-0-1
occ-3-0-1-2 = (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-3-0-1-2 : P.T.origin tree-3-0-1 occ-3-0-1-2 ≡ input s30
origin-3-0-1-2 = refl
transport-3-0-1-2 : P.T.origin tree-2-1-0 (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s30)
transport-3-0-1-2 = refl
occ-3-0-1-3 : P.T.Occurrence tree-3-0-1
occ-3-0-1-3 = (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-3-0-1-3 : P.T.origin tree-3-0-1 occ-3-0-1-3 ≡ input s20
origin-3-0-1-3 = refl
transport-3-0-1-3 : P.T.origin tree-2-1-0 (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-3-0-1-3 = refl
occ-3-0-1-4 : P.T.Occurrence tree-3-0-1
occ-3-0-1-4 = (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.source-leg , tt)))
origin-3-0-1-4 : P.T.origin tree-3-0-1 occ-3-0-1-4 ≡ input s31
origin-3-0-1-4 = refl
transport-3-0-1-4 : P.T.origin tree-2-1-0 (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-3-0-1-4 = refl
occ-3-0-1-5 : P.T.Occurrence tree-3-0-1
occ-3-0-1-5 = (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.target-leg , tt)))
origin-3-0-1-5 : P.T.origin tree-3-0-1 occ-3-0-1-5 ≡ input s01
origin-3-0-1-5 = refl
transport-3-0-1-5 : P.T.origin tree-2-1-0 (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.target-leg , tt))) ≡ input (swap s01)
transport-3-0-1-5 = refl
occ-3-0-1-6 : P.T.Occurrence tree-3-0-1
occ-3-0-1-6 = (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.source-leg , tt)))
origin-3-0-1-6 : P.T.origin tree-3-0-1 occ-3-0-1-6 ≡ input s31
origin-3-0-1-6 = refl
transport-3-0-1-6 : P.T.origin tree-2-1-0 (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-3-0-1-6 = refl
occ-3-0-1-7 : P.T.Occurrence tree-3-0-1
occ-3-0-1-7 = (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.target-leg , tt)))
origin-3-0-1-7 : P.T.origin tree-3-0-1 occ-3-0-1-7 ≡ input s21
origin-3-0-1-7 = refl
transport-3-0-1-7 : P.T.origin tree-2-1-0 (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.target-leg , tt))) ≡ input (swap s21)
transport-3-0-1-7 = refl
occ-3-0-1-8 : P.T.Occurrence tree-3-0-1
occ-3-0-1-8 = (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-3-0-1-8 : P.T.origin tree-3-0-1 occ-3-0-1-8 ≡ input s12
origin-3-0-1-8 = refl
transport-3-0-1-8 : P.T.origin tree-2-1-0 (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s12)
transport-3-0-1-8 = refl
occ-3-0-1-9 : P.T.Occurrence tree-3-0-1
occ-3-0-1-9 = (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-3-0-1-9 : P.T.origin tree-3-0-1 occ-3-0-1-9 ≡ input s02
origin-3-0-1-9 = refl
transport-3-0-1-9 : P.T.origin tree-2-1-0 (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-3-0-1-9 = refl
occ-3-0-1-10 : P.T.Occurrence tree-3-0-1
occ-3-0-1-10 = (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-3-0-1-10 : P.T.origin tree-3-0-1 occ-3-0-1-10 ≡ input s32
origin-3-0-1-10 = refl
transport-3-0-1-10 : P.T.origin tree-2-1-0 (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s32)
transport-3-0-1-10 = refl
occ-3-0-1-11 : P.T.Occurrence tree-3-0-1
occ-3-0-1-11 = (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-3-0-1-11 : P.T.origin tree-3-0-1 occ-3-0-1-11 ≡ input s02
origin-3-0-1-11 = refl
transport-3-0-1-11 : P.T.origin tree-2-1-0 (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-3-0-1-11 = refl
occ-3-0-1-12 : P.T.Occurrence tree-3-0-1
occ-3-0-1-12 = (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.source-leg , tt)))
origin-3-0-1-12 : P.T.origin tree-3-0-1 occ-3-0-1-12 ≡ input s13
origin-3-0-1-12 = refl
transport-3-0-1-12 : P.T.origin tree-2-1-0 (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-3-0-1-12 = refl
occ-3-0-1-13 : P.T.Occurrence tree-3-0-1
occ-3-0-1-13 = (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.target-leg , tt)))
origin-3-0-1-13 : P.T.origin tree-3-0-1 occ-3-0-1-13 ≡ input s03
origin-3-0-1-13 = refl
transport-3-0-1-13 : P.T.origin tree-2-1-0 (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.target-leg , tt))) ≡ input (swap s03)
transport-3-0-1-13 = refl
occ-3-0-1-14 : P.T.Occurrence tree-3-0-1
occ-3-0-1-14 = (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.source-leg , tt)))
origin-3-0-1-14 : P.T.origin tree-3-0-1 occ-3-0-1-14 ≡ input s13
origin-3-0-1-14 = refl
transport-3-0-1-14 : P.T.origin tree-2-1-0 (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-3-0-1-14 = refl
occ-3-0-1-15 : P.T.Occurrence tree-3-0-1
occ-3-0-1-15 = (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.target-leg , tt)))
origin-3-0-1-15 : P.T.origin tree-3-0-1 occ-3-0-1-15 ≡ input s23
origin-3-0-1-15 = refl
transport-3-0-1-15 : P.T.origin tree-2-1-0 (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.target-leg , tt))) ≡ input (swap s23)
transport-3-0-1-15 = refl
occ-3-0-1-16 : P.T.Occurrence tree-3-0-1
occ-3-0-1-16 = (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.source-leg , tt)))
origin-3-0-1-16 : P.T.origin tree-3-0-1 occ-3-0-1-16 ≡ input s20
origin-3-0-1-16 = refl
transport-3-0-1-16 : P.T.origin tree-2-1-0 (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-3-0-1-16 = refl
occ-3-0-1-17 : P.T.Occurrence tree-3-0-1
occ-3-0-1-17 = (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.target-leg , tt)))
origin-3-0-1-17 : P.T.origin tree-3-0-1 occ-3-0-1-17 ≡ input s10
origin-3-0-1-17 = refl
transport-3-0-1-17 : P.T.origin tree-2-1-0 (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.target-leg , tt))) ≡ input (swap s10)
transport-3-0-1-17 = refl
occ-3-0-1-18 : P.T.Occurrence tree-3-0-1
occ-3-0-1-18 = (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.source-leg , tt)))
origin-3-0-1-18 : P.T.origin tree-3-0-1 occ-3-0-1-18 ≡ input s20
origin-3-0-1-18 = refl
transport-3-0-1-18 : P.T.origin tree-2-1-0 (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-3-0-1-18 = refl
occ-3-0-1-19 : P.T.Occurrence tree-3-0-1
occ-3-0-1-19 = (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.target-leg , tt)))
origin-3-0-1-19 : P.T.origin tree-3-0-1 occ-3-0-1-19 ≡ input s30
origin-3-0-1-19 = refl
transport-3-0-1-19 : P.T.origin tree-2-1-0 (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.target-leg , tt))) ≡ input (swap s30)
transport-3-0-1-19 = refl
occ-3-0-1-20 : P.T.Occurrence tree-3-0-1
occ-3-0-1-20 = (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-3-0-1-20 : P.T.origin tree-3-0-1 occ-3-0-1-20 ≡ input s01
origin-3-0-1-20 = refl
transport-3-0-1-20 : P.T.origin tree-2-1-0 (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s01)
transport-3-0-1-20 = refl
occ-3-0-1-21 : P.T.Occurrence tree-3-0-1
occ-3-0-1-21 = (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-3-0-1-21 : P.T.origin tree-3-0-1 occ-3-0-1-21 ≡ input s31
origin-3-0-1-21 = refl
transport-3-0-1-21 : P.T.origin tree-2-1-0 (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-3-0-1-21 = refl
occ-3-0-1-22 : P.T.Occurrence tree-3-0-1
occ-3-0-1-22 = (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-3-0-1-22 : P.T.origin tree-3-0-1 occ-3-0-1-22 ≡ input s21
origin-3-0-1-22 = refl
transport-3-0-1-22 : P.T.origin tree-2-1-0 (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s21)
transport-3-0-1-22 = refl
occ-3-0-1-23 : P.T.Occurrence tree-3-0-1
occ-3-0-1-23 = (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-3-0-1-23 : P.T.origin tree-3-0-1 occ-3-0-1-23 ≡ input s31
origin-3-0-1-23 = refl
transport-3-0-1-23 : P.T.origin tree-2-1-0 (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-3-0-1-23 = refl
occ-3-0-1-24 : P.T.Occurrence tree-3-0-1
occ-3-0-1-24 = (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.source-leg , tt)))
origin-3-0-1-24 : P.T.origin tree-3-0-1 occ-3-0-1-24 ≡ input s02
origin-3-0-1-24 = refl
transport-3-0-1-24 : P.T.origin tree-2-1-0 (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-3-0-1-24 = refl
occ-3-0-1-25 : P.T.Occurrence tree-3-0-1
occ-3-0-1-25 = (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.target-leg , tt)))
origin-3-0-1-25 : P.T.origin tree-3-0-1 occ-3-0-1-25 ≡ input s12
origin-3-0-1-25 = refl
transport-3-0-1-25 : P.T.origin tree-2-1-0 (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.target-leg , tt))) ≡ input (swap s12)
transport-3-0-1-25 = refl
occ-3-0-1-26 : P.T.Occurrence tree-3-0-1
occ-3-0-1-26 = (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.source-leg , tt)))
origin-3-0-1-26 : P.T.origin tree-3-0-1 occ-3-0-1-26 ≡ input s02
origin-3-0-1-26 = refl
transport-3-0-1-26 : P.T.origin tree-2-1-0 (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-3-0-1-26 = refl
occ-3-0-1-27 : P.T.Occurrence tree-3-0-1
occ-3-0-1-27 = (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.target-leg , tt)))
origin-3-0-1-27 : P.T.origin tree-3-0-1 occ-3-0-1-27 ≡ input s32
origin-3-0-1-27 = refl
transport-3-0-1-27 : P.T.origin tree-2-1-0 (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.target-leg , tt))) ≡ input (swap s32)
transport-3-0-1-27 = refl
occ-3-0-1-28 : P.T.Occurrence tree-3-0-1
occ-3-0-1-28 = (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-3-0-1-28 : P.T.origin tree-3-0-1 occ-3-0-1-28 ≡ input s03
origin-3-0-1-28 = refl
transport-3-0-1-28 : P.T.origin tree-2-1-0 (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s03)
transport-3-0-1-28 = refl
occ-3-0-1-29 : P.T.Occurrence tree-3-0-1
occ-3-0-1-29 = (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-3-0-1-29 : P.T.origin tree-3-0-1 occ-3-0-1-29 ≡ input s13
origin-3-0-1-29 = refl
transport-3-0-1-29 : P.T.origin tree-2-1-0 (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-3-0-1-29 = refl
occ-3-0-1-30 : P.T.Occurrence tree-3-0-1
occ-3-0-1-30 = (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-3-0-1-30 : P.T.origin tree-3-0-1 occ-3-0-1-30 ≡ input s23
origin-3-0-1-30 = refl
transport-3-0-1-30 : P.T.origin tree-2-1-0 (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s23)
transport-3-0-1-30 = refl
occ-3-0-1-31 : P.T.Occurrence tree-3-0-1
occ-3-0-1-31 = (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-3-0-1-31 : P.T.origin tree-3-0-1 occ-3-0-1-31 ≡ input s13
origin-3-0-1-31 = refl
transport-3-0-1-31 : P.T.origin tree-2-1-0 (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-3-0-1-31 = refl
occ-3-0-1-32 : P.T.Occurrence tree-3-0-1
occ-3-0-1-32 = (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-1-0)) , (P.S.source-leg , tt)))
origin-3-0-1-32 : P.T.origin tree-3-0-1 occ-3-0-1-32 ≡ input s10
origin-3-0-1-32 = refl
transport-3-0-1-32 : P.T.origin tree-2-1-0 (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-0-1)) , (P.S.source-leg , tt))) ≡ input (swap s10)
transport-3-0-1-32 = refl
occ-3-0-1-33 : P.T.Occurrence tree-3-0-1
occ-3-0-1-33 = (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-1-0)) , (P.S.target-leg , tt)))
origin-3-0-1-33 : P.T.origin tree-3-0-1 occ-3-0-1-33 ≡ input s10
origin-3-0-1-33 = refl
transport-3-0-1-33 : P.T.origin tree-2-1-0 (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-0-1)) , (P.S.target-leg , tt))) ≡ input (swap s10)
transport-3-0-1-33 = refl
occ-3-0-1-34 : P.T.Occurrence tree-3-0-1
occ-3-0-1-34 = (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.source-leg , tt)))
origin-3-0-1-34 : P.T.origin tree-3-0-1 occ-3-0-1-34 ≡ input s10
origin-3-0-1-34 = refl
transport-3-0-1-34 : P.T.origin tree-2-1-0 (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.source-leg , tt))) ≡ input (swap s10)
transport-3-0-1-34 = refl
occ-3-0-1-35 : P.T.Occurrence tree-3-0-1
occ-3-0-1-35 = (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.target-leg , tt)))
origin-3-0-1-35 : P.T.origin tree-3-0-1 occ-3-0-1-35 ≡ input s30
origin-3-0-1-35 = refl
transport-3-0-1-35 : P.T.origin tree-2-1-0 (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.target-leg , tt))) ≡ input (swap s30)
transport-3-0-1-35 = refl
occ-3-0-1-36 : P.T.Occurrence tree-3-0-1
occ-3-0-1-36 = (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.source-leg , tt)))
origin-3-0-1-36 : P.T.origin tree-3-0-1 occ-3-0-1-36 ≡ input s30
origin-3-0-1-36 = refl
transport-3-0-1-36 : P.T.origin tree-2-1-0 (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.source-leg , tt))) ≡ input (swap s30)
transport-3-0-1-36 = refl
occ-3-0-1-37 : P.T.Occurrence tree-3-0-1
occ-3-0-1-37 = (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.target-leg , tt)))
origin-3-0-1-37 : P.T.origin tree-3-0-1 occ-3-0-1-37 ≡ input s10
origin-3-0-1-37 = refl
transport-3-0-1-37 : P.T.origin tree-2-1-0 (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.target-leg , tt))) ≡ input (swap s10)
transport-3-0-1-37 = refl
occ-3-0-1-38 : P.T.Occurrence tree-3-0-1
occ-3-0-1-38 = (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-3-0)) , (P.S.source-leg , tt)))
origin-3-0-1-38 : P.T.origin tree-3-0-1 occ-3-0-1-38 ≡ input s30
origin-3-0-1-38 = refl
transport-3-0-1-38 : P.T.origin tree-2-1-0 (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-2-1)) , (P.S.source-leg , tt))) ≡ input (swap s30)
transport-3-0-1-38 = refl
occ-3-0-1-39 : P.T.Occurrence tree-3-0-1
occ-3-0-1-39 = (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-3-0)) , (P.S.target-leg , tt)))
origin-3-0-1-39 : P.T.origin tree-3-0-1 occ-3-0-1-39 ≡ input s30
origin-3-0-1-39 = refl
transport-3-0-1-39 : P.T.origin tree-2-1-0 (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-2-1)) , (P.S.target-leg , tt))) ≡ input (swap s30)
transport-3-0-1-39 = refl
occ-3-0-1-40 : P.T.Occurrence tree-3-0-1
occ-3-0-1-40 = (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-3-0-1-40 : P.T.origin tree-3-0-1 occ-3-0-1-40 ≡ input s31
origin-3-0-1-40 = refl
transport-3-0-1-40 : P.T.origin tree-2-1-0 (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-3-0-1-40 = refl
occ-3-0-1-41 : P.T.Occurrence tree-3-0-1
occ-3-0-1-41 = (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-3-0-1-41 : P.T.origin tree-3-0-1 occ-3-0-1-41 ≡ input s31
origin-3-0-1-41 = refl
transport-3-0-1-41 : P.T.origin tree-2-1-0 (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-3-0-1-41 = refl
occ-3-0-1-42 : P.T.Occurrence tree-3-0-1
occ-3-0-1-42 = (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-1-2)) , (P.S.source-leg , tt)))
origin-3-0-1-42 : P.T.origin tree-3-0-1 occ-3-0-1-42 ≡ input s12
origin-3-0-1-42 = refl
transport-3-0-1-42 : P.T.origin tree-2-1-0 (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-0-3)) , (P.S.source-leg , tt))) ≡ input (swap s12)
transport-3-0-1-42 = refl
occ-3-0-1-43 : P.T.Occurrence tree-3-0-1
occ-3-0-1-43 = (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-1-2)) , (P.S.target-leg , tt)))
origin-3-0-1-43 : P.T.origin tree-3-0-1 occ-3-0-1-43 ≡ input s12
origin-3-0-1-43 = refl
transport-3-0-1-43 : P.T.origin tree-2-1-0 (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-0-3)) , (P.S.target-leg , tt))) ≡ input (swap s12)
transport-3-0-1-43 = refl
occ-3-0-1-44 : P.T.Occurrence tree-3-0-1
occ-3-0-1-44 = (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.source-leg , tt)))
origin-3-0-1-44 : P.T.origin tree-3-0-1 occ-3-0-1-44 ≡ input s12
origin-3-0-1-44 = refl
transport-3-0-1-44 : P.T.origin tree-2-1-0 (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.source-leg , tt))) ≡ input (swap s12)
transport-3-0-1-44 = refl
occ-3-0-1-45 : P.T.Occurrence tree-3-0-1
occ-3-0-1-45 = (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.target-leg , tt)))
origin-3-0-1-45 : P.T.origin tree-3-0-1 occ-3-0-1-45 ≡ input s32
origin-3-0-1-45 = refl
transport-3-0-1-45 : P.T.origin tree-2-1-0 (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.target-leg , tt))) ≡ input (swap s32)
transport-3-0-1-45 = refl
occ-3-0-1-46 : P.T.Occurrence tree-3-0-1
occ-3-0-1-46 = (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.source-leg , tt)))
origin-3-0-1-46 : P.T.origin tree-3-0-1 occ-3-0-1-46 ≡ input s32
origin-3-0-1-46 = refl
transport-3-0-1-46 : P.T.origin tree-2-1-0 (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.source-leg , tt))) ≡ input (swap s32)
transport-3-0-1-46 = refl
occ-3-0-1-47 : P.T.Occurrence tree-3-0-1
occ-3-0-1-47 = (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.target-leg , tt)))
origin-3-0-1-47 : P.T.origin tree-3-0-1 occ-3-0-1-47 ≡ input s12
origin-3-0-1-47 = refl
transport-3-0-1-47 : P.T.origin tree-2-1-0 (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.target-leg , tt))) ≡ input (swap s12)
transport-3-0-1-47 = refl
occ-3-0-1-48 : P.T.Occurrence tree-3-0-1
occ-3-0-1-48 = (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-3-2)) , (P.S.source-leg , tt)))
origin-3-0-1-48 : P.T.origin tree-3-0-1 occ-3-0-1-48 ≡ input s32
origin-3-0-1-48 = refl
transport-3-0-1-48 : P.T.origin tree-2-1-0 (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-2-3)) , (P.S.source-leg , tt))) ≡ input (swap s32)
transport-3-0-1-48 = refl
occ-3-0-1-49 : P.T.Occurrence tree-3-0-1
occ-3-0-1-49 = (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-3-2)) , (P.S.target-leg , tt)))
origin-3-0-1-49 : P.T.origin tree-3-0-1 occ-3-0-1-49 ≡ input s32
origin-3-0-1-49 = refl
transport-3-0-1-49 : P.T.origin tree-2-1-0 (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-2-3)) , (P.S.target-leg , tt))) ≡ input (swap s32)
transport-3-0-1-49 = refl
occ-3-0-1-50 : P.T.Occurrence tree-3-0-1
occ-3-0-1-50 = (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-3-0-1-50 : P.T.origin tree-3-0-1 occ-3-0-1-50 ≡ input s13
origin-3-0-1-50 = refl
transport-3-0-1-50 : P.T.origin tree-2-1-0 (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-3-0-1-50 = refl
occ-3-0-1-51 : P.T.Occurrence tree-3-0-1
occ-3-0-1-51 = (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-3-0-1-51 : P.T.origin tree-3-0-1 occ-3-0-1-51 ≡ input s13
origin-3-0-1-51 = refl
transport-3-0-1-51 : P.T.origin tree-2-1-0 (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-3-0-1-51 = refl
occ-3-0-1-52 : P.T.Occurrence tree-3-0-1
occ-3-0-1-52 = (P.S.full-source , (P.S.first-port , tt))
origin-3-0-1-52 : P.T.origin tree-3-0-1 occ-3-0-1-52 ≡ input s32
origin-3-0-1-52 = refl
transport-3-0-1-52 : P.T.origin tree-2-1-0 (P.S.full-source , (P.S.first-port , tt)) ≡ input (swap s32)
transport-3-0-1-52 = refl
occ-3-0-1-53 : P.T.Occurrence tree-3-0-1
occ-3-0-1-53 = (P.S.full-source , (P.S.middle-port , tt))
origin-3-0-1-53 : P.T.origin tree-3-0-1 occ-3-0-1-53 ≡ input s02
origin-3-0-1-53 = refl
transport-3-0-1-53 : P.T.origin tree-2-1-0 (P.S.full-source , (P.S.middle-port , tt)) ≡ input (swap s02)
transport-3-0-1-53 = refl
occ-3-0-1-54 : P.T.Occurrence tree-3-0-1
occ-3-0-1-54 = (P.S.full-source , (P.S.final-port , tt))
origin-3-0-1-54 : P.T.origin tree-3-0-1 occ-3-0-1-54 ≡ input s12
origin-3-0-1-54 = refl
transport-3-0-1-54 : P.T.origin tree-2-1-0 (P.S.full-source , (P.S.final-port , tt)) ≡ input (swap s12)
transport-3-0-1-54 = refl
selected-source-3-0-1-AB : P.S.ab-index {a = C.q7} {b = C.q0} {c = C.q7} F.triple-3-0-1 ≡ (c1 , (F.vp-3-2 , F.vp-0-2))
selected-source-3-0-1-AB = refl
selected-target-3-0-1-AB : P.S.ab-index {a = C.q0} {b = C.q7} {c = C.q0} F.triple-2-1-0 ≡ (m1 , (F.vp-2-3 , F.vp-1-3))
selected-target-3-0-1-AB = refl
selected-source-3-0-1-BC : P.S.bc-index {a = C.q7} {b = C.q0} {c = C.q7} F.triple-3-0-1 ≡ (c1 , (F.vp-0-2 , F.vp-1-2))
selected-source-3-0-1-BC = refl
selected-target-3-0-1-BC : P.S.bc-index {a = C.q0} {b = C.q7} {c = C.q0} F.triple-2-1-0 ≡ (m1 , (F.vp-1-3 , F.vp-0-3))
selected-target-3-0-1-BC = refl
selected-source-3-0-1-AC : P.S.ac-index {a = C.q7} {b = C.q0} {c = C.q7} F.triple-3-0-1 ≡ (c1 , (F.vp-3-2 , F.vp-1-2))
selected-source-3-0-1-AC = refl
selected-target-3-0-1-AC : P.S.ac-index {a = C.q0} {b = C.q7} {c = C.q0} F.triple-2-1-0 ≡ (m1 , (F.vp-2-3 , F.vp-0-3))
selected-target-3-0-1-AC = refl
occ-3-0-2-0 : P.T.Occurrence tree-3-0-2
occ-3-0-2-0 = (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-3-0-2-0 : P.T.origin tree-3-0-2 occ-3-0-2-0 ≡ input s10
origin-3-0-2-0 = refl
transport-3-0-2-0 : P.T.origin tree-2-1-3 (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s10)
transport-3-0-2-0 = refl
occ-3-0-2-1 : P.T.Occurrence tree-3-0-2
occ-3-0-2-1 = (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-3-0-2-1 : P.T.origin tree-3-0-2 occ-3-0-2-1 ≡ input s20
origin-3-0-2-1 = refl
transport-3-0-2-1 : P.T.origin tree-2-1-3 (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-3-0-2-1 = refl
occ-3-0-2-2 : P.T.Occurrence tree-3-0-2
occ-3-0-2-2 = (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-3-0-2-2 : P.T.origin tree-3-0-2 occ-3-0-2-2 ≡ input s30
origin-3-0-2-2 = refl
transport-3-0-2-2 : P.T.origin tree-2-1-3 (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s30)
transport-3-0-2-2 = refl
occ-3-0-2-3 : P.T.Occurrence tree-3-0-2
occ-3-0-2-3 = (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-3-0-2-3 : P.T.origin tree-3-0-2 occ-3-0-2-3 ≡ input s20
origin-3-0-2-3 = refl
transport-3-0-2-3 : P.T.origin tree-2-1-3 (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-3-0-2-3 = refl
occ-3-0-2-4 : P.T.Occurrence tree-3-0-2
occ-3-0-2-4 = (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.source-leg , tt)))
origin-3-0-2-4 : P.T.origin tree-3-0-2 occ-3-0-2-4 ≡ input s31
origin-3-0-2-4 = refl
transport-3-0-2-4 : P.T.origin tree-2-1-3 (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-3-0-2-4 = refl
occ-3-0-2-5 : P.T.Occurrence tree-3-0-2
occ-3-0-2-5 = (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.target-leg , tt)))
origin-3-0-2-5 : P.T.origin tree-3-0-2 occ-3-0-2-5 ≡ input s01
origin-3-0-2-5 = refl
transport-3-0-2-5 : P.T.origin tree-2-1-3 (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.target-leg , tt))) ≡ input (swap s01)
transport-3-0-2-5 = refl
occ-3-0-2-6 : P.T.Occurrence tree-3-0-2
occ-3-0-2-6 = (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.source-leg , tt)))
origin-3-0-2-6 : P.T.origin tree-3-0-2 occ-3-0-2-6 ≡ input s31
origin-3-0-2-6 = refl
transport-3-0-2-6 : P.T.origin tree-2-1-3 (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-3-0-2-6 = refl
occ-3-0-2-7 : P.T.Occurrence tree-3-0-2
occ-3-0-2-7 = (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.target-leg , tt)))
origin-3-0-2-7 : P.T.origin tree-3-0-2 occ-3-0-2-7 ≡ input s21
origin-3-0-2-7 = refl
transport-3-0-2-7 : P.T.origin tree-2-1-3 (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.target-leg , tt))) ≡ input (swap s21)
transport-3-0-2-7 = refl
occ-3-0-2-8 : P.T.Occurrence tree-3-0-2
occ-3-0-2-8 = (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-3-0-2-8 : P.T.origin tree-3-0-2 occ-3-0-2-8 ≡ input s12
origin-3-0-2-8 = refl
transport-3-0-2-8 : P.T.origin tree-2-1-3 (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s12)
transport-3-0-2-8 = refl
occ-3-0-2-9 : P.T.Occurrence tree-3-0-2
occ-3-0-2-9 = (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-3-0-2-9 : P.T.origin tree-3-0-2 occ-3-0-2-9 ≡ input s02
origin-3-0-2-9 = refl
transport-3-0-2-9 : P.T.origin tree-2-1-3 (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-3-0-2-9 = refl
occ-3-0-2-10 : P.T.Occurrence tree-3-0-2
occ-3-0-2-10 = (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-3-0-2-10 : P.T.origin tree-3-0-2 occ-3-0-2-10 ≡ input s32
origin-3-0-2-10 = refl
transport-3-0-2-10 : P.T.origin tree-2-1-3 (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s32)
transport-3-0-2-10 = refl
occ-3-0-2-11 : P.T.Occurrence tree-3-0-2
occ-3-0-2-11 = (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-3-0-2-11 : P.T.origin tree-3-0-2 occ-3-0-2-11 ≡ input s02
origin-3-0-2-11 = refl
transport-3-0-2-11 : P.T.origin tree-2-1-3 (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-3-0-2-11 = refl
occ-3-0-2-12 : P.T.Occurrence tree-3-0-2
occ-3-0-2-12 = (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.source-leg , tt)))
origin-3-0-2-12 : P.T.origin tree-3-0-2 occ-3-0-2-12 ≡ input s13
origin-3-0-2-12 = refl
transport-3-0-2-12 : P.T.origin tree-2-1-3 (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-3-0-2-12 = refl
occ-3-0-2-13 : P.T.Occurrence tree-3-0-2
occ-3-0-2-13 = (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.target-leg , tt)))
origin-3-0-2-13 : P.T.origin tree-3-0-2 occ-3-0-2-13 ≡ input s03
origin-3-0-2-13 = refl
transport-3-0-2-13 : P.T.origin tree-2-1-3 (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.target-leg , tt))) ≡ input (swap s03)
transport-3-0-2-13 = refl
occ-3-0-2-14 : P.T.Occurrence tree-3-0-2
occ-3-0-2-14 = (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.source-leg , tt)))
origin-3-0-2-14 : P.T.origin tree-3-0-2 occ-3-0-2-14 ≡ input s13
origin-3-0-2-14 = refl
transport-3-0-2-14 : P.T.origin tree-2-1-3 (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-3-0-2-14 = refl
occ-3-0-2-15 : P.T.Occurrence tree-3-0-2
occ-3-0-2-15 = (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.target-leg , tt)))
origin-3-0-2-15 : P.T.origin tree-3-0-2 occ-3-0-2-15 ≡ input s23
origin-3-0-2-15 = refl
transport-3-0-2-15 : P.T.origin tree-2-1-3 (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.target-leg , tt))) ≡ input (swap s23)
transport-3-0-2-15 = refl
occ-3-0-2-16 : P.T.Occurrence tree-3-0-2
occ-3-0-2-16 = (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-3-0-2-16 : P.T.origin tree-3-0-2 occ-3-0-2-16 ≡ input s20
origin-3-0-2-16 = refl
transport-3-0-2-16 : P.T.origin tree-2-1-3 (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-3-0-2-16 = refl
occ-3-0-2-17 : P.T.Occurrence tree-3-0-2
occ-3-0-2-17 = (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-3-0-2-17 : P.T.origin tree-3-0-2 occ-3-0-2-17 ≡ input s20
origin-3-0-2-17 = refl
transport-3-0-2-17 : P.T.origin tree-2-1-3 (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-3-0-2-17 = refl
occ-3-0-2-18 : P.T.Occurrence tree-3-0-2
occ-3-0-2-18 = (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-0-1)) , (P.S.source-leg , tt)))
origin-3-0-2-18 : P.T.origin tree-3-0-2 occ-3-0-2-18 ≡ input s01
origin-3-0-2-18 = refl
transport-3-0-2-18 : P.T.origin tree-2-1-3 (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-1-0)) , (P.S.source-leg , tt))) ≡ input (swap s01)
transport-3-0-2-18 = refl
occ-3-0-2-19 : P.T.Occurrence tree-3-0-2
occ-3-0-2-19 = (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-0-1)) , (P.S.target-leg , tt)))
origin-3-0-2-19 : P.T.origin tree-3-0-2 occ-3-0-2-19 ≡ input s01
origin-3-0-2-19 = refl
transport-3-0-2-19 : P.T.origin tree-2-1-3 (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-1-0)) , (P.S.target-leg , tt))) ≡ input (swap s01)
transport-3-0-2-19 = refl
occ-3-0-2-20 : P.T.Occurrence tree-3-0-2
occ-3-0-2-20 = (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.source-leg , tt)))
origin-3-0-2-20 : P.T.origin tree-3-0-2 occ-3-0-2-20 ≡ input s01
origin-3-0-2-20 = refl
transport-3-0-2-20 : P.T.origin tree-2-1-3 (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.source-leg , tt))) ≡ input (swap s01)
transport-3-0-2-20 = refl
occ-3-0-2-21 : P.T.Occurrence tree-3-0-2
occ-3-0-2-21 = (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.target-leg , tt)))
origin-3-0-2-21 : P.T.origin tree-3-0-2 occ-3-0-2-21 ≡ input s21
origin-3-0-2-21 = refl
transport-3-0-2-21 : P.T.origin tree-2-1-3 (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.target-leg , tt))) ≡ input (swap s21)
transport-3-0-2-21 = refl
occ-3-0-2-22 : P.T.Occurrence tree-3-0-2
occ-3-0-2-22 = (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.source-leg , tt)))
origin-3-0-2-22 : P.T.origin tree-3-0-2 occ-3-0-2-22 ≡ input s21
origin-3-0-2-22 = refl
transport-3-0-2-22 : P.T.origin tree-2-1-3 (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.source-leg , tt))) ≡ input (swap s21)
transport-3-0-2-22 = refl
occ-3-0-2-23 : P.T.Occurrence tree-3-0-2
occ-3-0-2-23 = (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.target-leg , tt)))
origin-3-0-2-23 : P.T.origin tree-3-0-2 occ-3-0-2-23 ≡ input s01
origin-3-0-2-23 = refl
transport-3-0-2-23 : P.T.origin tree-2-1-3 (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.target-leg , tt))) ≡ input (swap s01)
transport-3-0-2-23 = refl
occ-3-0-2-24 : P.T.Occurrence tree-3-0-2
occ-3-0-2-24 = (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-2-1)) , (P.S.source-leg , tt)))
origin-3-0-2-24 : P.T.origin tree-3-0-2 occ-3-0-2-24 ≡ input s21
origin-3-0-2-24 = refl
transport-3-0-2-24 : P.T.origin tree-2-1-3 (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-3-0)) , (P.S.source-leg , tt))) ≡ input (swap s21)
transport-3-0-2-24 = refl
occ-3-0-2-25 : P.T.Occurrence tree-3-0-2
occ-3-0-2-25 = (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-2-1)) , (P.S.target-leg , tt)))
origin-3-0-2-25 : P.T.origin tree-3-0-2 occ-3-0-2-25 ≡ input s21
origin-3-0-2-25 = refl
transport-3-0-2-25 : P.T.origin tree-2-1-3 (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-3-0)) , (P.S.target-leg , tt))) ≡ input (swap s21)
transport-3-0-2-25 = refl
occ-3-0-2-26 : P.T.Occurrence tree-3-0-2
occ-3-0-2-26 = (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-3-0-2-26 : P.T.origin tree-3-0-2 occ-3-0-2-26 ≡ input s02
origin-3-0-2-26 = refl
transport-3-0-2-26 : P.T.origin tree-2-1-3 (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-3-0-2-26 = refl
occ-3-0-2-27 : P.T.Occurrence tree-3-0-2
occ-3-0-2-27 = (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-3-0-2-27 : P.T.origin tree-3-0-2 occ-3-0-2-27 ≡ input s02
origin-3-0-2-27 = refl
transport-3-0-2-27 : P.T.origin tree-2-1-3 (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-3-0-2-27 = refl
occ-3-0-2-28 : P.T.Occurrence tree-3-0-2
occ-3-0-2-28 = (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-0-3)) , (P.S.source-leg , tt)))
origin-3-0-2-28 : P.T.origin tree-3-0-2 occ-3-0-2-28 ≡ input s03
origin-3-0-2-28 = refl
transport-3-0-2-28 : P.T.origin tree-2-1-3 (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-1-2)) , (P.S.source-leg , tt))) ≡ input (swap s03)
transport-3-0-2-28 = refl
occ-3-0-2-29 : P.T.Occurrence tree-3-0-2
occ-3-0-2-29 = (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-0-3)) , (P.S.target-leg , tt)))
origin-3-0-2-29 : P.T.origin tree-3-0-2 occ-3-0-2-29 ≡ input s03
origin-3-0-2-29 = refl
transport-3-0-2-29 : P.T.origin tree-2-1-3 (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-1-2)) , (P.S.target-leg , tt))) ≡ input (swap s03)
transport-3-0-2-29 = refl
occ-3-0-2-30 : P.T.Occurrence tree-3-0-2
occ-3-0-2-30 = (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.source-leg , tt)))
origin-3-0-2-30 : P.T.origin tree-3-0-2 occ-3-0-2-30 ≡ input s03
origin-3-0-2-30 = refl
transport-3-0-2-30 : P.T.origin tree-2-1-3 (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.source-leg , tt))) ≡ input (swap s03)
transport-3-0-2-30 = refl
occ-3-0-2-31 : P.T.Occurrence tree-3-0-2
occ-3-0-2-31 = (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.target-leg , tt)))
origin-3-0-2-31 : P.T.origin tree-3-0-2 occ-3-0-2-31 ≡ input s23
origin-3-0-2-31 = refl
transport-3-0-2-31 : P.T.origin tree-2-1-3 (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.target-leg , tt))) ≡ input (swap s23)
transport-3-0-2-31 = refl
occ-3-0-2-32 : P.T.Occurrence tree-3-0-2
occ-3-0-2-32 = (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.source-leg , tt)))
origin-3-0-2-32 : P.T.origin tree-3-0-2 occ-3-0-2-32 ≡ input s23
origin-3-0-2-32 = refl
transport-3-0-2-32 : P.T.origin tree-2-1-3 (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.source-leg , tt))) ≡ input (swap s23)
transport-3-0-2-32 = refl
occ-3-0-2-33 : P.T.Occurrence tree-3-0-2
occ-3-0-2-33 = (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.target-leg , tt)))
origin-3-0-2-33 : P.T.origin tree-3-0-2 occ-3-0-2-33 ≡ input s03
origin-3-0-2-33 = refl
transport-3-0-2-33 : P.T.origin tree-2-1-3 (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.target-leg , tt))) ≡ input (swap s03)
transport-3-0-2-33 = refl
occ-3-0-2-34 : P.T.Occurrence tree-3-0-2
occ-3-0-2-34 = (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-2-3)) , (P.S.source-leg , tt)))
origin-3-0-2-34 : P.T.origin tree-3-0-2 occ-3-0-2-34 ≡ input s23
origin-3-0-2-34 = refl
transport-3-0-2-34 : P.T.origin tree-2-1-3 (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-3-2)) , (P.S.source-leg , tt))) ≡ input (swap s23)
transport-3-0-2-34 = refl
occ-3-0-2-35 : P.T.Occurrence tree-3-0-2
occ-3-0-2-35 = (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-2-3)) , (P.S.target-leg , tt)))
origin-3-0-2-35 : P.T.origin tree-3-0-2 occ-3-0-2-35 ≡ input s23
origin-3-0-2-35 = refl
transport-3-0-2-35 : P.T.origin tree-2-1-3 (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-3-2)) , (P.S.target-leg , tt))) ≡ input (swap s23)
transport-3-0-2-35 = refl
occ-3-0-2-36 : P.T.Occurrence tree-3-0-2
occ-3-0-2-36 = (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-3-0-2-36 : P.T.origin tree-3-0-2 occ-3-0-2-36 ≡ input s10
origin-3-0-2-36 = refl
transport-3-0-2-36 : P.T.origin tree-2-1-3 (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s10)
transport-3-0-2-36 = refl
occ-3-0-2-37 : P.T.Occurrence tree-3-0-2
occ-3-0-2-37 = (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-3-0-2-37 : P.T.origin tree-3-0-2 occ-3-0-2-37 ≡ input s20
origin-3-0-2-37 = refl
transport-3-0-2-37 : P.T.origin tree-2-1-3 (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-3-0-2-37 = refl
occ-3-0-2-38 : P.T.Occurrence tree-3-0-2
occ-3-0-2-38 = (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-3-0-2-38 : P.T.origin tree-3-0-2 occ-3-0-2-38 ≡ input s30
origin-3-0-2-38 = refl
transport-3-0-2-38 : P.T.origin tree-2-1-3 (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s30)
transport-3-0-2-38 = refl
occ-3-0-2-39 : P.T.Occurrence tree-3-0-2
occ-3-0-2-39 = (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-3-0-2-39 : P.T.origin tree-3-0-2 occ-3-0-2-39 ≡ input s20
origin-3-0-2-39 = refl
transport-3-0-2-39 : P.T.origin tree-2-1-3 (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-3-0-2-39 = refl
occ-3-0-2-40 : P.T.Occurrence tree-3-0-2
occ-3-0-2-40 = (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.source-leg , tt)))
origin-3-0-2-40 : P.T.origin tree-3-0-2 occ-3-0-2-40 ≡ input s31
origin-3-0-2-40 = refl
transport-3-0-2-40 : P.T.origin tree-2-1-3 (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-3-0-2-40 = refl
occ-3-0-2-41 : P.T.Occurrence tree-3-0-2
occ-3-0-2-41 = (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.target-leg , tt)))
origin-3-0-2-41 : P.T.origin tree-3-0-2 occ-3-0-2-41 ≡ input s01
origin-3-0-2-41 = refl
transport-3-0-2-41 : P.T.origin tree-2-1-3 (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.target-leg , tt))) ≡ input (swap s01)
transport-3-0-2-41 = refl
occ-3-0-2-42 : P.T.Occurrence tree-3-0-2
occ-3-0-2-42 = (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.source-leg , tt)))
origin-3-0-2-42 : P.T.origin tree-3-0-2 occ-3-0-2-42 ≡ input s31
origin-3-0-2-42 = refl
transport-3-0-2-42 : P.T.origin tree-2-1-3 (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-3-0-2-42 = refl
occ-3-0-2-43 : P.T.Occurrence tree-3-0-2
occ-3-0-2-43 = (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.target-leg , tt)))
origin-3-0-2-43 : P.T.origin tree-3-0-2 occ-3-0-2-43 ≡ input s21
origin-3-0-2-43 = refl
transport-3-0-2-43 : P.T.origin tree-2-1-3 (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.target-leg , tt))) ≡ input (swap s21)
transport-3-0-2-43 = refl
occ-3-0-2-44 : P.T.Occurrence tree-3-0-2
occ-3-0-2-44 = (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-3-0-2-44 : P.T.origin tree-3-0-2 occ-3-0-2-44 ≡ input s12
origin-3-0-2-44 = refl
transport-3-0-2-44 : P.T.origin tree-2-1-3 (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s12)
transport-3-0-2-44 = refl
occ-3-0-2-45 : P.T.Occurrence tree-3-0-2
occ-3-0-2-45 = (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-3-0-2-45 : P.T.origin tree-3-0-2 occ-3-0-2-45 ≡ input s02
origin-3-0-2-45 = refl
transport-3-0-2-45 : P.T.origin tree-2-1-3 (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-3-0-2-45 = refl
occ-3-0-2-46 : P.T.Occurrence tree-3-0-2
occ-3-0-2-46 = (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-3-0-2-46 : P.T.origin tree-3-0-2 occ-3-0-2-46 ≡ input s32
origin-3-0-2-46 = refl
transport-3-0-2-46 : P.T.origin tree-2-1-3 (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s32)
transport-3-0-2-46 = refl
occ-3-0-2-47 : P.T.Occurrence tree-3-0-2
occ-3-0-2-47 = (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-3-0-2-47 : P.T.origin tree-3-0-2 occ-3-0-2-47 ≡ input s02
origin-3-0-2-47 = refl
transport-3-0-2-47 : P.T.origin tree-2-1-3 (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-3-0-2-47 = refl
occ-3-0-2-48 : P.T.Occurrence tree-3-0-2
occ-3-0-2-48 = (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.source-leg , tt)))
origin-3-0-2-48 : P.T.origin tree-3-0-2 occ-3-0-2-48 ≡ input s13
origin-3-0-2-48 = refl
transport-3-0-2-48 : P.T.origin tree-2-1-3 (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-3-0-2-48 = refl
occ-3-0-2-49 : P.T.Occurrence tree-3-0-2
occ-3-0-2-49 = (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.target-leg , tt)))
origin-3-0-2-49 : P.T.origin tree-3-0-2 occ-3-0-2-49 ≡ input s03
origin-3-0-2-49 = refl
transport-3-0-2-49 : P.T.origin tree-2-1-3 (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.target-leg , tt))) ≡ input (swap s03)
transport-3-0-2-49 = refl
occ-3-0-2-50 : P.T.Occurrence tree-3-0-2
occ-3-0-2-50 = (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.source-leg , tt)))
origin-3-0-2-50 : P.T.origin tree-3-0-2 occ-3-0-2-50 ≡ input s13
origin-3-0-2-50 = refl
transport-3-0-2-50 : P.T.origin tree-2-1-3 (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-3-0-2-50 = refl
occ-3-0-2-51 : P.T.Occurrence tree-3-0-2
occ-3-0-2-51 = (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.target-leg , tt)))
origin-3-0-2-51 : P.T.origin tree-3-0-2 occ-3-0-2-51 ≡ input s23
origin-3-0-2-51 = refl
transport-3-0-2-51 : P.T.origin tree-2-1-3 (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.target-leg , tt))) ≡ input (swap s23)
transport-3-0-2-51 = refl
occ-3-0-2-52 : P.T.Occurrence tree-3-0-2
occ-3-0-2-52 = (P.S.full-source , (P.S.first-port , tt))
origin-3-0-2-52 : P.T.origin tree-3-0-2 occ-3-0-2-52 ≡ input s31
origin-3-0-2-52 = refl
transport-3-0-2-52 : P.T.origin tree-2-1-3 (P.S.full-source , (P.S.first-port , tt)) ≡ input (swap s31)
transport-3-0-2-52 = refl
occ-3-0-2-53 : P.T.Occurrence tree-3-0-2
occ-3-0-2-53 = (P.S.full-source , (P.S.middle-port , tt))
origin-3-0-2-53 : P.T.origin tree-3-0-2 occ-3-0-2-53 ≡ input s01
origin-3-0-2-53 = refl
transport-3-0-2-53 : P.T.origin tree-2-1-3 (P.S.full-source , (P.S.middle-port , tt)) ≡ input (swap s01)
transport-3-0-2-53 = refl
occ-3-0-2-54 : P.T.Occurrence tree-3-0-2
occ-3-0-2-54 = (P.S.full-source , (P.S.final-port , tt))
origin-3-0-2-54 : P.T.origin tree-3-0-2 occ-3-0-2-54 ≡ input s21
origin-3-0-2-54 = refl
transport-3-0-2-54 : P.T.origin tree-2-1-3 (P.S.full-source , (P.S.final-port , tt)) ≡ input (swap s21)
transport-3-0-2-54 = refl
selected-source-3-0-2-AB : P.S.ab-index {a = C.q7} {b = C.q0} {c = C.q0} F.triple-3-0-2 ≡ (m0 , (F.vp-3-1 , F.vp-0-1))
selected-source-3-0-2-AB = refl
selected-target-3-0-2-AB : P.S.ab-index {a = C.q0} {b = C.q7} {c = C.q7} F.triple-2-1-3 ≡ (c0 , (F.vp-2-0 , F.vp-1-0))
selected-target-3-0-2-AB = refl
selected-source-3-0-2-BC : P.S.bc-index {a = C.q7} {b = C.q0} {c = C.q0} F.triple-3-0-2 ≡ (m0 , (F.vp-0-1 , F.vp-2-1))
selected-source-3-0-2-BC = refl
selected-target-3-0-2-BC : P.S.bc-index {a = C.q0} {b = C.q7} {c = C.q7} F.triple-2-1-3 ≡ (c0 , (F.vp-1-0 , F.vp-3-0))
selected-target-3-0-2-BC = refl
selected-source-3-0-2-AC : P.S.ac-index {a = C.q7} {b = C.q0} {c = C.q0} F.triple-3-0-2 ≡ (m0 , (F.vp-3-1 , F.vp-2-1))
selected-source-3-0-2-AC = refl
selected-target-3-0-2-AC : P.S.ac-index {a = C.q0} {b = C.q7} {c = C.q7} F.triple-2-1-3 ≡ (c0 , (F.vp-2-0 , F.vp-3-0))
selected-target-3-0-2-AC = refl
occ-3-1-0-0 : P.T.Occurrence tree-3-1-0
occ-3-1-0-0 = (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-1-0)) , (P.S.source-leg , tt)))
origin-3-1-0-0 : P.T.origin tree-3-1-0 occ-3-1-0-0 ≡ input s10
origin-3-1-0-0 = refl
transport-3-1-0-0 : P.T.origin tree-2-0-1 (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-0-1)) , (P.S.source-leg , tt))) ≡ input (swap s10)
transport-3-1-0-0 = refl
occ-3-1-0-1 : P.T.Occurrence tree-3-1-0
occ-3-1-0-1 = (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-1-0)) , (P.S.target-leg , tt)))
origin-3-1-0-1 : P.T.origin tree-3-1-0 occ-3-1-0-1 ≡ input s10
origin-3-1-0-1 = refl
transport-3-1-0-1 : P.T.origin tree-2-0-1 (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-0-1)) , (P.S.target-leg , tt))) ≡ input (swap s10)
transport-3-1-0-1 = refl
occ-3-1-0-2 : P.T.Occurrence tree-3-1-0
occ-3-1-0-2 = (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.source-leg , tt)))
origin-3-1-0-2 : P.T.origin tree-3-1-0 occ-3-1-0-2 ≡ input s10
origin-3-1-0-2 = refl
transport-3-1-0-2 : P.T.origin tree-2-0-1 (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.source-leg , tt))) ≡ input (swap s10)
transport-3-1-0-2 = refl
occ-3-1-0-3 : P.T.Occurrence tree-3-1-0
occ-3-1-0-3 = (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.target-leg , tt)))
origin-3-1-0-3 : P.T.origin tree-3-1-0 occ-3-1-0-3 ≡ input s30
origin-3-1-0-3 = refl
transport-3-1-0-3 : P.T.origin tree-2-0-1 (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.target-leg , tt))) ≡ input (swap s30)
transport-3-1-0-3 = refl
occ-3-1-0-4 : P.T.Occurrence tree-3-1-0
occ-3-1-0-4 = (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.source-leg , tt)))
origin-3-1-0-4 : P.T.origin tree-3-1-0 occ-3-1-0-4 ≡ input s30
origin-3-1-0-4 = refl
transport-3-1-0-4 : P.T.origin tree-2-0-1 (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.source-leg , tt))) ≡ input (swap s30)
transport-3-1-0-4 = refl
occ-3-1-0-5 : P.T.Occurrence tree-3-1-0
occ-3-1-0-5 = (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.target-leg , tt)))
origin-3-1-0-5 : P.T.origin tree-3-1-0 occ-3-1-0-5 ≡ input s10
origin-3-1-0-5 = refl
transport-3-1-0-5 : P.T.origin tree-2-0-1 (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.target-leg , tt))) ≡ input (swap s10)
transport-3-1-0-5 = refl
occ-3-1-0-6 : P.T.Occurrence tree-3-1-0
occ-3-1-0-6 = (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-3-0)) , (P.S.source-leg , tt)))
origin-3-1-0-6 : P.T.origin tree-3-1-0 occ-3-1-0-6 ≡ input s30
origin-3-1-0-6 = refl
transport-3-1-0-6 : P.T.origin tree-2-0-1 (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-2-1)) , (P.S.source-leg , tt))) ≡ input (swap s30)
transport-3-1-0-6 = refl
occ-3-1-0-7 : P.T.Occurrence tree-3-1-0
occ-3-1-0-7 = (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-3-0)) , (P.S.target-leg , tt)))
origin-3-1-0-7 : P.T.origin tree-3-1-0 occ-3-1-0-7 ≡ input s30
origin-3-1-0-7 = refl
transport-3-1-0-7 : P.T.origin tree-2-0-1 (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-2-1)) , (P.S.target-leg , tt))) ≡ input (swap s30)
transport-3-1-0-7 = refl
occ-3-1-0-8 : P.T.Occurrence tree-3-1-0
occ-3-1-0-8 = (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-3-1-0-8 : P.T.origin tree-3-1-0 occ-3-1-0-8 ≡ input s31
origin-3-1-0-8 = refl
transport-3-1-0-8 : P.T.origin tree-2-0-1 (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-3-1-0-8 = refl
occ-3-1-0-9 : P.T.Occurrence tree-3-1-0
occ-3-1-0-9 = (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-3-1-0-9 : P.T.origin tree-3-1-0 occ-3-1-0-9 ≡ input s31
origin-3-1-0-9 = refl
transport-3-1-0-9 : P.T.origin tree-2-0-1 (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-3-1-0-9 = refl
occ-3-1-0-10 : P.T.Occurrence tree-3-1-0
occ-3-1-0-10 = (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-1-2)) , (P.S.source-leg , tt)))
origin-3-1-0-10 : P.T.origin tree-3-1-0 occ-3-1-0-10 ≡ input s12
origin-3-1-0-10 = refl
transport-3-1-0-10 : P.T.origin tree-2-0-1 (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-0-3)) , (P.S.source-leg , tt))) ≡ input (swap s12)
transport-3-1-0-10 = refl
occ-3-1-0-11 : P.T.Occurrence tree-3-1-0
occ-3-1-0-11 = (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-1-2)) , (P.S.target-leg , tt)))
origin-3-1-0-11 : P.T.origin tree-3-1-0 occ-3-1-0-11 ≡ input s12
origin-3-1-0-11 = refl
transport-3-1-0-11 : P.T.origin tree-2-0-1 (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-0-3)) , (P.S.target-leg , tt))) ≡ input (swap s12)
transport-3-1-0-11 = refl
occ-3-1-0-12 : P.T.Occurrence tree-3-1-0
occ-3-1-0-12 = (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.source-leg , tt)))
origin-3-1-0-12 : P.T.origin tree-3-1-0 occ-3-1-0-12 ≡ input s12
origin-3-1-0-12 = refl
transport-3-1-0-12 : P.T.origin tree-2-0-1 (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.source-leg , tt))) ≡ input (swap s12)
transport-3-1-0-12 = refl
occ-3-1-0-13 : P.T.Occurrence tree-3-1-0
occ-3-1-0-13 = (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.target-leg , tt)))
origin-3-1-0-13 : P.T.origin tree-3-1-0 occ-3-1-0-13 ≡ input s32
origin-3-1-0-13 = refl
transport-3-1-0-13 : P.T.origin tree-2-0-1 (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.target-leg , tt))) ≡ input (swap s32)
transport-3-1-0-13 = refl
occ-3-1-0-14 : P.T.Occurrence tree-3-1-0
occ-3-1-0-14 = (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.source-leg , tt)))
origin-3-1-0-14 : P.T.origin tree-3-1-0 occ-3-1-0-14 ≡ input s32
origin-3-1-0-14 = refl
transport-3-1-0-14 : P.T.origin tree-2-0-1 (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.source-leg , tt))) ≡ input (swap s32)
transport-3-1-0-14 = refl
occ-3-1-0-15 : P.T.Occurrence tree-3-1-0
occ-3-1-0-15 = (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.target-leg , tt)))
origin-3-1-0-15 : P.T.origin tree-3-1-0 occ-3-1-0-15 ≡ input s12
origin-3-1-0-15 = refl
transport-3-1-0-15 : P.T.origin tree-2-0-1 (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.target-leg , tt))) ≡ input (swap s12)
transport-3-1-0-15 = refl
occ-3-1-0-16 : P.T.Occurrence tree-3-1-0
occ-3-1-0-16 = (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-3-2)) , (P.S.source-leg , tt)))
origin-3-1-0-16 : P.T.origin tree-3-1-0 occ-3-1-0-16 ≡ input s32
origin-3-1-0-16 = refl
transport-3-1-0-16 : P.T.origin tree-2-0-1 (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-2-3)) , (P.S.source-leg , tt))) ≡ input (swap s32)
transport-3-1-0-16 = refl
occ-3-1-0-17 : P.T.Occurrence tree-3-1-0
occ-3-1-0-17 = (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-3-2)) , (P.S.target-leg , tt)))
origin-3-1-0-17 : P.T.origin tree-3-1-0 occ-3-1-0-17 ≡ input s32
origin-3-1-0-17 = refl
transport-3-1-0-17 : P.T.origin tree-2-0-1 (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-2-3)) , (P.S.target-leg , tt))) ≡ input (swap s32)
transport-3-1-0-17 = refl
occ-3-1-0-18 : P.T.Occurrence tree-3-1-0
occ-3-1-0-18 = (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-3-1-0-18 : P.T.origin tree-3-1-0 occ-3-1-0-18 ≡ input s13
origin-3-1-0-18 = refl
transport-3-1-0-18 : P.T.origin tree-2-0-1 (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-3-1-0-18 = refl
occ-3-1-0-19 : P.T.Occurrence tree-3-1-0
occ-3-1-0-19 = (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-3-1-0-19 : P.T.origin tree-3-1-0 occ-3-1-0-19 ≡ input s13
origin-3-1-0-19 = refl
transport-3-1-0-19 : P.T.origin tree-2-0-1 (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-3-1-0-19 = refl
occ-3-1-0-20 : P.T.Occurrence tree-3-1-0
occ-3-1-0-20 = (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-3-1-0-20 : P.T.origin tree-3-1-0 occ-3-1-0-20 ≡ input s10
origin-3-1-0-20 = refl
transport-3-1-0-20 : P.T.origin tree-2-0-1 (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s10)
transport-3-1-0-20 = refl
occ-3-1-0-21 : P.T.Occurrence tree-3-1-0
occ-3-1-0-21 = (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-3-1-0-21 : P.T.origin tree-3-1-0 occ-3-1-0-21 ≡ input s20
origin-3-1-0-21 = refl
transport-3-1-0-21 : P.T.origin tree-2-0-1 (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-3-1-0-21 = refl
occ-3-1-0-22 : P.T.Occurrence tree-3-1-0
occ-3-1-0-22 = (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-3-1-0-22 : P.T.origin tree-3-1-0 occ-3-1-0-22 ≡ input s30
origin-3-1-0-22 = refl
transport-3-1-0-22 : P.T.origin tree-2-0-1 (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s30)
transport-3-1-0-22 = refl
occ-3-1-0-23 : P.T.Occurrence tree-3-1-0
occ-3-1-0-23 = (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-3-1-0-23 : P.T.origin tree-3-1-0 occ-3-1-0-23 ≡ input s20
origin-3-1-0-23 = refl
transport-3-1-0-23 : P.T.origin tree-2-0-1 (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-3-1-0-23 = refl
occ-3-1-0-24 : P.T.Occurrence tree-3-1-0
occ-3-1-0-24 = (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.source-leg , tt)))
origin-3-1-0-24 : P.T.origin tree-3-1-0 occ-3-1-0-24 ≡ input s31
origin-3-1-0-24 = refl
transport-3-1-0-24 : P.T.origin tree-2-0-1 (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-3-1-0-24 = refl
occ-3-1-0-25 : P.T.Occurrence tree-3-1-0
occ-3-1-0-25 = (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.target-leg , tt)))
origin-3-1-0-25 : P.T.origin tree-3-1-0 occ-3-1-0-25 ≡ input s01
origin-3-1-0-25 = refl
transport-3-1-0-25 : P.T.origin tree-2-0-1 (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.target-leg , tt))) ≡ input (swap s01)
transport-3-1-0-25 = refl
occ-3-1-0-26 : P.T.Occurrence tree-3-1-0
occ-3-1-0-26 = (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.source-leg , tt)))
origin-3-1-0-26 : P.T.origin tree-3-1-0 occ-3-1-0-26 ≡ input s31
origin-3-1-0-26 = refl
transport-3-1-0-26 : P.T.origin tree-2-0-1 (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-3-1-0-26 = refl
occ-3-1-0-27 : P.T.Occurrence tree-3-1-0
occ-3-1-0-27 = (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.target-leg , tt)))
origin-3-1-0-27 : P.T.origin tree-3-1-0 occ-3-1-0-27 ≡ input s21
origin-3-1-0-27 = refl
transport-3-1-0-27 : P.T.origin tree-2-0-1 (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.target-leg , tt))) ≡ input (swap s21)
transport-3-1-0-27 = refl
occ-3-1-0-28 : P.T.Occurrence tree-3-1-0
occ-3-1-0-28 = (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-3-1-0-28 : P.T.origin tree-3-1-0 occ-3-1-0-28 ≡ input s12
origin-3-1-0-28 = refl
transport-3-1-0-28 : P.T.origin tree-2-0-1 (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s12)
transport-3-1-0-28 = refl
occ-3-1-0-29 : P.T.Occurrence tree-3-1-0
occ-3-1-0-29 = (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-3-1-0-29 : P.T.origin tree-3-1-0 occ-3-1-0-29 ≡ input s02
origin-3-1-0-29 = refl
transport-3-1-0-29 : P.T.origin tree-2-0-1 (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-3-1-0-29 = refl
occ-3-1-0-30 : P.T.Occurrence tree-3-1-0
occ-3-1-0-30 = (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-3-1-0-30 : P.T.origin tree-3-1-0 occ-3-1-0-30 ≡ input s32
origin-3-1-0-30 = refl
transport-3-1-0-30 : P.T.origin tree-2-0-1 (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s32)
transport-3-1-0-30 = refl
occ-3-1-0-31 : P.T.Occurrence tree-3-1-0
occ-3-1-0-31 = (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-3-1-0-31 : P.T.origin tree-3-1-0 occ-3-1-0-31 ≡ input s02
origin-3-1-0-31 = refl
transport-3-1-0-31 : P.T.origin tree-2-0-1 (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-3-1-0-31 = refl
occ-3-1-0-32 : P.T.Occurrence tree-3-1-0
occ-3-1-0-32 = (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.source-leg , tt)))
origin-3-1-0-32 : P.T.origin tree-3-1-0 occ-3-1-0-32 ≡ input s13
origin-3-1-0-32 = refl
transport-3-1-0-32 : P.T.origin tree-2-0-1 (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-3-1-0-32 = refl
occ-3-1-0-33 : P.T.Occurrence tree-3-1-0
occ-3-1-0-33 = (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.target-leg , tt)))
origin-3-1-0-33 : P.T.origin tree-3-1-0 occ-3-1-0-33 ≡ input s03
origin-3-1-0-33 = refl
transport-3-1-0-33 : P.T.origin tree-2-0-1 (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.target-leg , tt))) ≡ input (swap s03)
transport-3-1-0-33 = refl
occ-3-1-0-34 : P.T.Occurrence tree-3-1-0
occ-3-1-0-34 = (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.source-leg , tt)))
origin-3-1-0-34 : P.T.origin tree-3-1-0 occ-3-1-0-34 ≡ input s13
origin-3-1-0-34 = refl
transport-3-1-0-34 : P.T.origin tree-2-0-1 (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-3-1-0-34 = refl
occ-3-1-0-35 : P.T.Occurrence tree-3-1-0
occ-3-1-0-35 = (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.target-leg , tt)))
origin-3-1-0-35 : P.T.origin tree-3-1-0 occ-3-1-0-35 ≡ input s23
origin-3-1-0-35 = refl
transport-3-1-0-35 : P.T.origin tree-2-0-1 (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.target-leg , tt))) ≡ input (swap s23)
transport-3-1-0-35 = refl
occ-3-1-0-36 : P.T.Occurrence tree-3-1-0
occ-3-1-0-36 = (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-3-1-0-36 : P.T.origin tree-3-1-0 occ-3-1-0-36 ≡ input s10
origin-3-1-0-36 = refl
transport-3-1-0-36 : P.T.origin tree-2-0-1 (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s10)
transport-3-1-0-36 = refl
occ-3-1-0-37 : P.T.Occurrence tree-3-1-0
occ-3-1-0-37 = (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-3-1-0-37 : P.T.origin tree-3-1-0 occ-3-1-0-37 ≡ input s20
origin-3-1-0-37 = refl
transport-3-1-0-37 : P.T.origin tree-2-0-1 (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-3-1-0-37 = refl
occ-3-1-0-38 : P.T.Occurrence tree-3-1-0
occ-3-1-0-38 = (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-3-1-0-38 : P.T.origin tree-3-1-0 occ-3-1-0-38 ≡ input s30
origin-3-1-0-38 = refl
transport-3-1-0-38 : P.T.origin tree-2-0-1 (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s30)
transport-3-1-0-38 = refl
occ-3-1-0-39 : P.T.Occurrence tree-3-1-0
occ-3-1-0-39 = (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-3-1-0-39 : P.T.origin tree-3-1-0 occ-3-1-0-39 ≡ input s20
origin-3-1-0-39 = refl
transport-3-1-0-39 : P.T.origin tree-2-0-1 (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-3-1-0-39 = refl
occ-3-1-0-40 : P.T.Occurrence tree-3-1-0
occ-3-1-0-40 = (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.source-leg , tt)))
origin-3-1-0-40 : P.T.origin tree-3-1-0 occ-3-1-0-40 ≡ input s31
origin-3-1-0-40 = refl
transport-3-1-0-40 : P.T.origin tree-2-0-1 (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-3-1-0-40 = refl
occ-3-1-0-41 : P.T.Occurrence tree-3-1-0
occ-3-1-0-41 = (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.target-leg , tt)))
origin-3-1-0-41 : P.T.origin tree-3-1-0 occ-3-1-0-41 ≡ input s01
origin-3-1-0-41 = refl
transport-3-1-0-41 : P.T.origin tree-2-0-1 (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.target-leg , tt))) ≡ input (swap s01)
transport-3-1-0-41 = refl
occ-3-1-0-42 : P.T.Occurrence tree-3-1-0
occ-3-1-0-42 = (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.source-leg , tt)))
origin-3-1-0-42 : P.T.origin tree-3-1-0 occ-3-1-0-42 ≡ input s31
origin-3-1-0-42 = refl
transport-3-1-0-42 : P.T.origin tree-2-0-1 (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-3-1-0-42 = refl
occ-3-1-0-43 : P.T.Occurrence tree-3-1-0
occ-3-1-0-43 = (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.target-leg , tt)))
origin-3-1-0-43 : P.T.origin tree-3-1-0 occ-3-1-0-43 ≡ input s21
origin-3-1-0-43 = refl
transport-3-1-0-43 : P.T.origin tree-2-0-1 (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.target-leg , tt))) ≡ input (swap s21)
transport-3-1-0-43 = refl
occ-3-1-0-44 : P.T.Occurrence tree-3-1-0
occ-3-1-0-44 = (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-3-1-0-44 : P.T.origin tree-3-1-0 occ-3-1-0-44 ≡ input s12
origin-3-1-0-44 = refl
transport-3-1-0-44 : P.T.origin tree-2-0-1 (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s12)
transport-3-1-0-44 = refl
occ-3-1-0-45 : P.T.Occurrence tree-3-1-0
occ-3-1-0-45 = (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-3-1-0-45 : P.T.origin tree-3-1-0 occ-3-1-0-45 ≡ input s02
origin-3-1-0-45 = refl
transport-3-1-0-45 : P.T.origin tree-2-0-1 (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-3-1-0-45 = refl
occ-3-1-0-46 : P.T.Occurrence tree-3-1-0
occ-3-1-0-46 = (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-3-1-0-46 : P.T.origin tree-3-1-0 occ-3-1-0-46 ≡ input s32
origin-3-1-0-46 = refl
transport-3-1-0-46 : P.T.origin tree-2-0-1 (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s32)
transport-3-1-0-46 = refl
occ-3-1-0-47 : P.T.Occurrence tree-3-1-0
occ-3-1-0-47 = (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-3-1-0-47 : P.T.origin tree-3-1-0 occ-3-1-0-47 ≡ input s02
origin-3-1-0-47 = refl
transport-3-1-0-47 : P.T.origin tree-2-0-1 (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-3-1-0-47 = refl
occ-3-1-0-48 : P.T.Occurrence tree-3-1-0
occ-3-1-0-48 = (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.source-leg , tt)))
origin-3-1-0-48 : P.T.origin tree-3-1-0 occ-3-1-0-48 ≡ input s13
origin-3-1-0-48 = refl
transport-3-1-0-48 : P.T.origin tree-2-0-1 (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-3-1-0-48 = refl
occ-3-1-0-49 : P.T.Occurrence tree-3-1-0
occ-3-1-0-49 = (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.target-leg , tt)))
origin-3-1-0-49 : P.T.origin tree-3-1-0 occ-3-1-0-49 ≡ input s03
origin-3-1-0-49 = refl
transport-3-1-0-49 : P.T.origin tree-2-0-1 (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.target-leg , tt))) ≡ input (swap s03)
transport-3-1-0-49 = refl
occ-3-1-0-50 : P.T.Occurrence tree-3-1-0
occ-3-1-0-50 = (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.source-leg , tt)))
origin-3-1-0-50 : P.T.origin tree-3-1-0 occ-3-1-0-50 ≡ input s13
origin-3-1-0-50 = refl
transport-3-1-0-50 : P.T.origin tree-2-0-1 (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-3-1-0-50 = refl
occ-3-1-0-51 : P.T.Occurrence tree-3-1-0
occ-3-1-0-51 = (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.target-leg , tt)))
origin-3-1-0-51 : P.T.origin tree-3-1-0 occ-3-1-0-51 ≡ input s23
origin-3-1-0-51 = refl
transport-3-1-0-51 : P.T.origin tree-2-0-1 (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.target-leg , tt))) ≡ input (swap s23)
transport-3-1-0-51 = refl
occ-3-1-0-52 : P.T.Occurrence tree-3-1-0
occ-3-1-0-52 = (P.S.full-source , (P.S.first-port , tt))
origin-3-1-0-52 : P.T.origin tree-3-1-0 occ-3-1-0-52 ≡ input s32
origin-3-1-0-52 = refl
transport-3-1-0-52 : P.T.origin tree-2-0-1 (P.S.full-source , (P.S.first-port , tt)) ≡ input (swap s32)
transport-3-1-0-52 = refl
occ-3-1-0-53 : P.T.Occurrence tree-3-1-0
occ-3-1-0-53 = (P.S.full-source , (P.S.middle-port , tt))
origin-3-1-0-53 : P.T.origin tree-3-1-0 occ-3-1-0-53 ≡ input s12
origin-3-1-0-53 = refl
transport-3-1-0-53 : P.T.origin tree-2-0-1 (P.S.full-source , (P.S.middle-port , tt)) ≡ input (swap s12)
transport-3-1-0-53 = refl
occ-3-1-0-54 : P.T.Occurrence tree-3-1-0
occ-3-1-0-54 = (P.S.full-source , (P.S.final-port , tt))
origin-3-1-0-54 : P.T.origin tree-3-1-0 occ-3-1-0-54 ≡ input s02
origin-3-1-0-54 = refl
transport-3-1-0-54 : P.T.origin tree-2-0-1 (P.S.full-source , (P.S.final-port , tt)) ≡ input (swap s02)
transport-3-1-0-54 = refl
selected-source-3-1-0-AB : P.S.ab-index {a = C.q7} {b = C.q7} {c = C.q0} F.triple-3-1-0 ≡ (c1 , (F.vp-3-2 , F.vp-1-2))
selected-source-3-1-0-AB = refl
selected-target-3-1-0-AB : P.S.ab-index {a = C.q0} {b = C.q0} {c = C.q7} F.triple-2-0-1 ≡ (m1 , (F.vp-2-3 , F.vp-0-3))
selected-target-3-1-0-AB = refl
selected-source-3-1-0-BC : P.S.bc-index {a = C.q7} {b = C.q7} {c = C.q0} F.triple-3-1-0 ≡ (c1 , (F.vp-1-2 , F.vp-0-2))
selected-source-3-1-0-BC = refl
selected-target-3-1-0-BC : P.S.bc-index {a = C.q0} {b = C.q0} {c = C.q7} F.triple-2-0-1 ≡ (m1 , (F.vp-0-3 , F.vp-1-3))
selected-target-3-1-0-BC = refl
selected-source-3-1-0-AC : P.S.ac-index {a = C.q7} {b = C.q7} {c = C.q0} F.triple-3-1-0 ≡ (c1 , (F.vp-3-2 , F.vp-0-2))
selected-source-3-1-0-AC = refl
selected-target-3-1-0-AC : P.S.ac-index {a = C.q0} {b = C.q0} {c = C.q7} F.triple-2-0-1 ≡ (m1 , (F.vp-2-3 , F.vp-1-3))
selected-target-3-1-0-AC = refl
occ-3-1-2-0 : P.T.Occurrence tree-3-1-2
occ-3-1-2-0 = (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-1-0)) , (P.S.source-leg , tt)))
origin-3-1-2-0 : P.T.origin tree-3-1-2 occ-3-1-2-0 ≡ input s10
origin-3-1-2-0 = refl
transport-3-1-2-0 : P.T.origin tree-2-0-3 (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-0-1)) , (P.S.source-leg , tt))) ≡ input (swap s10)
transport-3-1-2-0 = refl
occ-3-1-2-1 : P.T.Occurrence tree-3-1-2
occ-3-1-2-1 = (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-1-0)) , (P.S.target-leg , tt)))
origin-3-1-2-1 : P.T.origin tree-3-1-2 occ-3-1-2-1 ≡ input s10
origin-3-1-2-1 = refl
transport-3-1-2-1 : P.T.origin tree-2-0-3 (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-0-1)) , (P.S.target-leg , tt))) ≡ input (swap s10)
transport-3-1-2-1 = refl
occ-3-1-2-2 : P.T.Occurrence tree-3-1-2
occ-3-1-2-2 = (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.source-leg , tt)))
origin-3-1-2-2 : P.T.origin tree-3-1-2 occ-3-1-2-2 ≡ input s10
origin-3-1-2-2 = refl
transport-3-1-2-2 : P.T.origin tree-2-0-3 (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.source-leg , tt))) ≡ input (swap s10)
transport-3-1-2-2 = refl
occ-3-1-2-3 : P.T.Occurrence tree-3-1-2
occ-3-1-2-3 = (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.target-leg , tt)))
origin-3-1-2-3 : P.T.origin tree-3-1-2 occ-3-1-2-3 ≡ input s30
origin-3-1-2-3 = refl
transport-3-1-2-3 : P.T.origin tree-2-0-3 (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.target-leg , tt))) ≡ input (swap s30)
transport-3-1-2-3 = refl
occ-3-1-2-4 : P.T.Occurrence tree-3-1-2
occ-3-1-2-4 = (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.source-leg , tt)))
origin-3-1-2-4 : P.T.origin tree-3-1-2 occ-3-1-2-4 ≡ input s30
origin-3-1-2-4 = refl
transport-3-1-2-4 : P.T.origin tree-2-0-3 (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.source-leg , tt))) ≡ input (swap s30)
transport-3-1-2-4 = refl
occ-3-1-2-5 : P.T.Occurrence tree-3-1-2
occ-3-1-2-5 = (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.target-leg , tt)))
origin-3-1-2-5 : P.T.origin tree-3-1-2 occ-3-1-2-5 ≡ input s10
origin-3-1-2-5 = refl
transport-3-1-2-5 : P.T.origin tree-2-0-3 (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.target-leg , tt))) ≡ input (swap s10)
transport-3-1-2-5 = refl
occ-3-1-2-6 : P.T.Occurrence tree-3-1-2
occ-3-1-2-6 = (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-3-0)) , (P.S.source-leg , tt)))
origin-3-1-2-6 : P.T.origin tree-3-1-2 occ-3-1-2-6 ≡ input s30
origin-3-1-2-6 = refl
transport-3-1-2-6 : P.T.origin tree-2-0-3 (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-2-1)) , (P.S.source-leg , tt))) ≡ input (swap s30)
transport-3-1-2-6 = refl
occ-3-1-2-7 : P.T.Occurrence tree-3-1-2
occ-3-1-2-7 = (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-3-0)) , (P.S.target-leg , tt)))
origin-3-1-2-7 : P.T.origin tree-3-1-2 occ-3-1-2-7 ≡ input s30
origin-3-1-2-7 = refl
transport-3-1-2-7 : P.T.origin tree-2-0-3 (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-2-1)) , (P.S.target-leg , tt))) ≡ input (swap s30)
transport-3-1-2-7 = refl
occ-3-1-2-8 : P.T.Occurrence tree-3-1-2
occ-3-1-2-8 = (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-3-1-2-8 : P.T.origin tree-3-1-2 occ-3-1-2-8 ≡ input s31
origin-3-1-2-8 = refl
transport-3-1-2-8 : P.T.origin tree-2-0-3 (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-3-1-2-8 = refl
occ-3-1-2-9 : P.T.Occurrence tree-3-1-2
occ-3-1-2-9 = (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-3-1-2-9 : P.T.origin tree-3-1-2 occ-3-1-2-9 ≡ input s31
origin-3-1-2-9 = refl
transport-3-1-2-9 : P.T.origin tree-2-0-3 (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-3-1-2-9 = refl
occ-3-1-2-10 : P.T.Occurrence tree-3-1-2
occ-3-1-2-10 = (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-1-2)) , (P.S.source-leg , tt)))
origin-3-1-2-10 : P.T.origin tree-3-1-2 occ-3-1-2-10 ≡ input s12
origin-3-1-2-10 = refl
transport-3-1-2-10 : P.T.origin tree-2-0-3 (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-0-3)) , (P.S.source-leg , tt))) ≡ input (swap s12)
transport-3-1-2-10 = refl
occ-3-1-2-11 : P.T.Occurrence tree-3-1-2
occ-3-1-2-11 = (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-1-2)) , (P.S.target-leg , tt)))
origin-3-1-2-11 : P.T.origin tree-3-1-2 occ-3-1-2-11 ≡ input s12
origin-3-1-2-11 = refl
transport-3-1-2-11 : P.T.origin tree-2-0-3 (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-0-3)) , (P.S.target-leg , tt))) ≡ input (swap s12)
transport-3-1-2-11 = refl
occ-3-1-2-12 : P.T.Occurrence tree-3-1-2
occ-3-1-2-12 = (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.source-leg , tt)))
origin-3-1-2-12 : P.T.origin tree-3-1-2 occ-3-1-2-12 ≡ input s12
origin-3-1-2-12 = refl
transport-3-1-2-12 : P.T.origin tree-2-0-3 (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.source-leg , tt))) ≡ input (swap s12)
transport-3-1-2-12 = refl
occ-3-1-2-13 : P.T.Occurrence tree-3-1-2
occ-3-1-2-13 = (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.target-leg , tt)))
origin-3-1-2-13 : P.T.origin tree-3-1-2 occ-3-1-2-13 ≡ input s32
origin-3-1-2-13 = refl
transport-3-1-2-13 : P.T.origin tree-2-0-3 (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.target-leg , tt))) ≡ input (swap s32)
transport-3-1-2-13 = refl
occ-3-1-2-14 : P.T.Occurrence tree-3-1-2
occ-3-1-2-14 = (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.source-leg , tt)))
origin-3-1-2-14 : P.T.origin tree-3-1-2 occ-3-1-2-14 ≡ input s32
origin-3-1-2-14 = refl
transport-3-1-2-14 : P.T.origin tree-2-0-3 (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.source-leg , tt))) ≡ input (swap s32)
transport-3-1-2-14 = refl
occ-3-1-2-15 : P.T.Occurrence tree-3-1-2
occ-3-1-2-15 = (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.target-leg , tt)))
origin-3-1-2-15 : P.T.origin tree-3-1-2 occ-3-1-2-15 ≡ input s12
origin-3-1-2-15 = refl
transport-3-1-2-15 : P.T.origin tree-2-0-3 (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.target-leg , tt))) ≡ input (swap s12)
transport-3-1-2-15 = refl
occ-3-1-2-16 : P.T.Occurrence tree-3-1-2
occ-3-1-2-16 = (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-3-2)) , (P.S.source-leg , tt)))
origin-3-1-2-16 : P.T.origin tree-3-1-2 occ-3-1-2-16 ≡ input s32
origin-3-1-2-16 = refl
transport-3-1-2-16 : P.T.origin tree-2-0-3 (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-2-3)) , (P.S.source-leg , tt))) ≡ input (swap s32)
transport-3-1-2-16 = refl
occ-3-1-2-17 : P.T.Occurrence tree-3-1-2
occ-3-1-2-17 = (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-3-2)) , (P.S.target-leg , tt)))
origin-3-1-2-17 : P.T.origin tree-3-1-2 occ-3-1-2-17 ≡ input s32
origin-3-1-2-17 = refl
transport-3-1-2-17 : P.T.origin tree-2-0-3 (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-2-3)) , (P.S.target-leg , tt))) ≡ input (swap s32)
transport-3-1-2-17 = refl
occ-3-1-2-18 : P.T.Occurrence tree-3-1-2
occ-3-1-2-18 = (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-3-1-2-18 : P.T.origin tree-3-1-2 occ-3-1-2-18 ≡ input s13
origin-3-1-2-18 = refl
transport-3-1-2-18 : P.T.origin tree-2-0-3 (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-3-1-2-18 = refl
occ-3-1-2-19 : P.T.Occurrence tree-3-1-2
occ-3-1-2-19 = (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-3-1-2-19 : P.T.origin tree-3-1-2 occ-3-1-2-19 ≡ input s13
origin-3-1-2-19 = refl
transport-3-1-2-19 : P.T.origin tree-2-0-3 (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-3-1-2-19 = refl
occ-3-1-2-20 : P.T.Occurrence tree-3-1-2
occ-3-1-2-20 = (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-3-1-2-20 : P.T.origin tree-3-1-2 occ-3-1-2-20 ≡ input s10
origin-3-1-2-20 = refl
transport-3-1-2-20 : P.T.origin tree-2-0-3 (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s10)
transport-3-1-2-20 = refl
occ-3-1-2-21 : P.T.Occurrence tree-3-1-2
occ-3-1-2-21 = (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-3-1-2-21 : P.T.origin tree-3-1-2 occ-3-1-2-21 ≡ input s20
origin-3-1-2-21 = refl
transport-3-1-2-21 : P.T.origin tree-2-0-3 (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-3-1-2-21 = refl
occ-3-1-2-22 : P.T.Occurrence tree-3-1-2
occ-3-1-2-22 = (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-3-1-2-22 : P.T.origin tree-3-1-2 occ-3-1-2-22 ≡ input s30
origin-3-1-2-22 = refl
transport-3-1-2-22 : P.T.origin tree-2-0-3 (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s30)
transport-3-1-2-22 = refl
occ-3-1-2-23 : P.T.Occurrence tree-3-1-2
occ-3-1-2-23 = (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-3-1-2-23 : P.T.origin tree-3-1-2 occ-3-1-2-23 ≡ input s20
origin-3-1-2-23 = refl
transport-3-1-2-23 : P.T.origin tree-2-0-3 (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-3-1-2-23 = refl
occ-3-1-2-24 : P.T.Occurrence tree-3-1-2
occ-3-1-2-24 = (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.source-leg , tt)))
origin-3-1-2-24 : P.T.origin tree-3-1-2 occ-3-1-2-24 ≡ input s31
origin-3-1-2-24 = refl
transport-3-1-2-24 : P.T.origin tree-2-0-3 (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-3-1-2-24 = refl
occ-3-1-2-25 : P.T.Occurrence tree-3-1-2
occ-3-1-2-25 = (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.target-leg , tt)))
origin-3-1-2-25 : P.T.origin tree-3-1-2 occ-3-1-2-25 ≡ input s01
origin-3-1-2-25 = refl
transport-3-1-2-25 : P.T.origin tree-2-0-3 (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.target-leg , tt))) ≡ input (swap s01)
transport-3-1-2-25 = refl
occ-3-1-2-26 : P.T.Occurrence tree-3-1-2
occ-3-1-2-26 = (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.source-leg , tt)))
origin-3-1-2-26 : P.T.origin tree-3-1-2 occ-3-1-2-26 ≡ input s31
origin-3-1-2-26 = refl
transport-3-1-2-26 : P.T.origin tree-2-0-3 (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-3-1-2-26 = refl
occ-3-1-2-27 : P.T.Occurrence tree-3-1-2
occ-3-1-2-27 = (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.target-leg , tt)))
origin-3-1-2-27 : P.T.origin tree-3-1-2 occ-3-1-2-27 ≡ input s21
origin-3-1-2-27 = refl
transport-3-1-2-27 : P.T.origin tree-2-0-3 (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.target-leg , tt))) ≡ input (swap s21)
transport-3-1-2-27 = refl
occ-3-1-2-28 : P.T.Occurrence tree-3-1-2
occ-3-1-2-28 = (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-3-1-2-28 : P.T.origin tree-3-1-2 occ-3-1-2-28 ≡ input s12
origin-3-1-2-28 = refl
transport-3-1-2-28 : P.T.origin tree-2-0-3 (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s12)
transport-3-1-2-28 = refl
occ-3-1-2-29 : P.T.Occurrence tree-3-1-2
occ-3-1-2-29 = (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-3-1-2-29 : P.T.origin tree-3-1-2 occ-3-1-2-29 ≡ input s02
origin-3-1-2-29 = refl
transport-3-1-2-29 : P.T.origin tree-2-0-3 (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-3-1-2-29 = refl
occ-3-1-2-30 : P.T.Occurrence tree-3-1-2
occ-3-1-2-30 = (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-3-1-2-30 : P.T.origin tree-3-1-2 occ-3-1-2-30 ≡ input s32
origin-3-1-2-30 = refl
transport-3-1-2-30 : P.T.origin tree-2-0-3 (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s32)
transport-3-1-2-30 = refl
occ-3-1-2-31 : P.T.Occurrence tree-3-1-2
occ-3-1-2-31 = (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-3-1-2-31 : P.T.origin tree-3-1-2 occ-3-1-2-31 ≡ input s02
origin-3-1-2-31 = refl
transport-3-1-2-31 : P.T.origin tree-2-0-3 (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-3-1-2-31 = refl
occ-3-1-2-32 : P.T.Occurrence tree-3-1-2
occ-3-1-2-32 = (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.source-leg , tt)))
origin-3-1-2-32 : P.T.origin tree-3-1-2 occ-3-1-2-32 ≡ input s13
origin-3-1-2-32 = refl
transport-3-1-2-32 : P.T.origin tree-2-0-3 (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-3-1-2-32 = refl
occ-3-1-2-33 : P.T.Occurrence tree-3-1-2
occ-3-1-2-33 = (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.target-leg , tt)))
origin-3-1-2-33 : P.T.origin tree-3-1-2 occ-3-1-2-33 ≡ input s03
origin-3-1-2-33 = refl
transport-3-1-2-33 : P.T.origin tree-2-0-3 (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.target-leg , tt))) ≡ input (swap s03)
transport-3-1-2-33 = refl
occ-3-1-2-34 : P.T.Occurrence tree-3-1-2
occ-3-1-2-34 = (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.source-leg , tt)))
origin-3-1-2-34 : P.T.origin tree-3-1-2 occ-3-1-2-34 ≡ input s13
origin-3-1-2-34 = refl
transport-3-1-2-34 : P.T.origin tree-2-0-3 (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-3-1-2-34 = refl
occ-3-1-2-35 : P.T.Occurrence tree-3-1-2
occ-3-1-2-35 = (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.target-leg , tt)))
origin-3-1-2-35 : P.T.origin tree-3-1-2 occ-3-1-2-35 ≡ input s23
origin-3-1-2-35 = refl
transport-3-1-2-35 : P.T.origin tree-2-0-3 (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.target-leg , tt))) ≡ input (swap s23)
transport-3-1-2-35 = refl
occ-3-1-2-36 : P.T.Occurrence tree-3-1-2
occ-3-1-2-36 = (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-3-1-2-36 : P.T.origin tree-3-1-2 occ-3-1-2-36 ≡ input s10
origin-3-1-2-36 = refl
transport-3-1-2-36 : P.T.origin tree-2-0-3 (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s10)
transport-3-1-2-36 = refl
occ-3-1-2-37 : P.T.Occurrence tree-3-1-2
occ-3-1-2-37 = (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-3-1-2-37 : P.T.origin tree-3-1-2 occ-3-1-2-37 ≡ input s20
origin-3-1-2-37 = refl
transport-3-1-2-37 : P.T.origin tree-2-0-3 (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-3-1-2-37 = refl
occ-3-1-2-38 : P.T.Occurrence tree-3-1-2
occ-3-1-2-38 = (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-3-1-2-38 : P.T.origin tree-3-1-2 occ-3-1-2-38 ≡ input s30
origin-3-1-2-38 = refl
transport-3-1-2-38 : P.T.origin tree-2-0-3 (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s30)
transport-3-1-2-38 = refl
occ-3-1-2-39 : P.T.Occurrence tree-3-1-2
occ-3-1-2-39 = (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-3-1-2-39 : P.T.origin tree-3-1-2 occ-3-1-2-39 ≡ input s20
origin-3-1-2-39 = refl
transport-3-1-2-39 : P.T.origin tree-2-0-3 (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-3-1-2-39 = refl
occ-3-1-2-40 : P.T.Occurrence tree-3-1-2
occ-3-1-2-40 = (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.source-leg , tt)))
origin-3-1-2-40 : P.T.origin tree-3-1-2 occ-3-1-2-40 ≡ input s31
origin-3-1-2-40 = refl
transport-3-1-2-40 : P.T.origin tree-2-0-3 (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-3-1-2-40 = refl
occ-3-1-2-41 : P.T.Occurrence tree-3-1-2
occ-3-1-2-41 = (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.target-leg , tt)))
origin-3-1-2-41 : P.T.origin tree-3-1-2 occ-3-1-2-41 ≡ input s01
origin-3-1-2-41 = refl
transport-3-1-2-41 : P.T.origin tree-2-0-3 (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.target-leg , tt))) ≡ input (swap s01)
transport-3-1-2-41 = refl
occ-3-1-2-42 : P.T.Occurrence tree-3-1-2
occ-3-1-2-42 = (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.source-leg , tt)))
origin-3-1-2-42 : P.T.origin tree-3-1-2 occ-3-1-2-42 ≡ input s31
origin-3-1-2-42 = refl
transport-3-1-2-42 : P.T.origin tree-2-0-3 (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-3-1-2-42 = refl
occ-3-1-2-43 : P.T.Occurrence tree-3-1-2
occ-3-1-2-43 = (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.target-leg , tt)))
origin-3-1-2-43 : P.T.origin tree-3-1-2 occ-3-1-2-43 ≡ input s21
origin-3-1-2-43 = refl
transport-3-1-2-43 : P.T.origin tree-2-0-3 (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.target-leg , tt))) ≡ input (swap s21)
transport-3-1-2-43 = refl
occ-3-1-2-44 : P.T.Occurrence tree-3-1-2
occ-3-1-2-44 = (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-3-1-2-44 : P.T.origin tree-3-1-2 occ-3-1-2-44 ≡ input s12
origin-3-1-2-44 = refl
transport-3-1-2-44 : P.T.origin tree-2-0-3 (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s12)
transport-3-1-2-44 = refl
occ-3-1-2-45 : P.T.Occurrence tree-3-1-2
occ-3-1-2-45 = (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-3-1-2-45 : P.T.origin tree-3-1-2 occ-3-1-2-45 ≡ input s02
origin-3-1-2-45 = refl
transport-3-1-2-45 : P.T.origin tree-2-0-3 (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-3-1-2-45 = refl
occ-3-1-2-46 : P.T.Occurrence tree-3-1-2
occ-3-1-2-46 = (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-3-1-2-46 : P.T.origin tree-3-1-2 occ-3-1-2-46 ≡ input s32
origin-3-1-2-46 = refl
transport-3-1-2-46 : P.T.origin tree-2-0-3 (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s32)
transport-3-1-2-46 = refl
occ-3-1-2-47 : P.T.Occurrence tree-3-1-2
occ-3-1-2-47 = (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-3-1-2-47 : P.T.origin tree-3-1-2 occ-3-1-2-47 ≡ input s02
origin-3-1-2-47 = refl
transport-3-1-2-47 : P.T.origin tree-2-0-3 (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-3-1-2-47 = refl
occ-3-1-2-48 : P.T.Occurrence tree-3-1-2
occ-3-1-2-48 = (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.source-leg , tt)))
origin-3-1-2-48 : P.T.origin tree-3-1-2 occ-3-1-2-48 ≡ input s13
origin-3-1-2-48 = refl
transport-3-1-2-48 : P.T.origin tree-2-0-3 (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-3-1-2-48 = refl
occ-3-1-2-49 : P.T.Occurrence tree-3-1-2
occ-3-1-2-49 = (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.target-leg , tt)))
origin-3-1-2-49 : P.T.origin tree-3-1-2 occ-3-1-2-49 ≡ input s03
origin-3-1-2-49 = refl
transport-3-1-2-49 : P.T.origin tree-2-0-3 (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.target-leg , tt))) ≡ input (swap s03)
transport-3-1-2-49 = refl
occ-3-1-2-50 : P.T.Occurrence tree-3-1-2
occ-3-1-2-50 = (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.source-leg , tt)))
origin-3-1-2-50 : P.T.origin tree-3-1-2 occ-3-1-2-50 ≡ input s13
origin-3-1-2-50 = refl
transport-3-1-2-50 : P.T.origin tree-2-0-3 (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-3-1-2-50 = refl
occ-3-1-2-51 : P.T.Occurrence tree-3-1-2
occ-3-1-2-51 = (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.target-leg , tt)))
origin-3-1-2-51 : P.T.origin tree-3-1-2 occ-3-1-2-51 ≡ input s23
origin-3-1-2-51 = refl
transport-3-1-2-51 : P.T.origin tree-2-0-3 (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.target-leg , tt))) ≡ input (swap s23)
transport-3-1-2-51 = refl
occ-3-1-2-52 : P.T.Occurrence tree-3-1-2
occ-3-1-2-52 = (P.S.full-source , (P.S.first-port , tt))
origin-3-1-2-52 : P.T.origin tree-3-1-2 occ-3-1-2-52 ≡ input s30
origin-3-1-2-52 = refl
transport-3-1-2-52 : P.T.origin tree-2-0-3 (P.S.full-source , (P.S.first-port , tt)) ≡ input (swap s30)
transport-3-1-2-52 = refl
occ-3-1-2-53 : P.T.Occurrence tree-3-1-2
occ-3-1-2-53 = (P.S.full-source , (P.S.middle-port , tt))
origin-3-1-2-53 : P.T.origin tree-3-1-2 occ-3-1-2-53 ≡ input s10
origin-3-1-2-53 = refl
transport-3-1-2-53 : P.T.origin tree-2-0-3 (P.S.full-source , (P.S.middle-port , tt)) ≡ input (swap s10)
transport-3-1-2-53 = refl
occ-3-1-2-54 : P.T.Occurrence tree-3-1-2
occ-3-1-2-54 = (P.S.full-source , (P.S.final-port , tt))
origin-3-1-2-54 : P.T.origin tree-3-1-2 occ-3-1-2-54 ≡ input s20
origin-3-1-2-54 = refl
transport-3-1-2-54 : P.T.origin tree-2-0-3 (P.S.full-source , (P.S.final-port , tt)) ≡ input (swap s20)
transport-3-1-2-54 = refl
selected-source-3-1-2-AB : P.S.ab-index {a = C.q7} {b = C.q7} {c = C.q0} F.triple-3-1-2 ≡ (c0 , (F.vp-3-0 , F.vp-1-0))
selected-source-3-1-2-AB = refl
selected-target-3-1-2-AB : P.S.ab-index {a = C.q0} {b = C.q0} {c = C.q7} F.triple-2-0-3 ≡ (m0 , (F.vp-2-1 , F.vp-0-1))
selected-target-3-1-2-AB = refl
selected-source-3-1-2-BC : P.S.bc-index {a = C.q7} {b = C.q7} {c = C.q0} F.triple-3-1-2 ≡ (c0 , (F.vp-1-0 , F.vp-2-0))
selected-source-3-1-2-BC = refl
selected-target-3-1-2-BC : P.S.bc-index {a = C.q0} {b = C.q0} {c = C.q7} F.triple-2-0-3 ≡ (m0 , (F.vp-0-1 , F.vp-3-1))
selected-target-3-1-2-BC = refl
selected-source-3-1-2-AC : P.S.ac-index {a = C.q7} {b = C.q7} {c = C.q0} F.triple-3-1-2 ≡ (c0 , (F.vp-3-0 , F.vp-2-0))
selected-source-3-1-2-AC = refl
selected-target-3-1-2-AC : P.S.ac-index {a = C.q0} {b = C.q0} {c = C.q7} F.triple-2-0-3 ≡ (m0 , (F.vp-2-1 , F.vp-3-1))
selected-target-3-1-2-AC = refl
occ-3-2-0-0 : P.T.Occurrence tree-3-2-0
occ-3-2-0-0 = (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-3-2-0-0 : P.T.origin tree-3-2-0 occ-3-2-0-0 ≡ input s10
origin-3-2-0-0 = refl
transport-3-2-0-0 : P.T.origin tree-2-3-1 (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s10)
transport-3-2-0-0 = refl
occ-3-2-0-1 : P.T.Occurrence tree-3-2-0
occ-3-2-0-1 = (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-3-2-0-1 : P.T.origin tree-3-2-0 occ-3-2-0-1 ≡ input s20
origin-3-2-0-1 = refl
transport-3-2-0-1 : P.T.origin tree-2-3-1 (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-3-2-0-1 = refl
occ-3-2-0-2 : P.T.Occurrence tree-3-2-0
occ-3-2-0-2 = (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-3-2-0-2 : P.T.origin tree-3-2-0 occ-3-2-0-2 ≡ input s30
origin-3-2-0-2 = refl
transport-3-2-0-2 : P.T.origin tree-2-3-1 (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s30)
transport-3-2-0-2 = refl
occ-3-2-0-3 : P.T.Occurrence tree-3-2-0
occ-3-2-0-3 = (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-3-2-0-3 : P.T.origin tree-3-2-0 occ-3-2-0-3 ≡ input s20
origin-3-2-0-3 = refl
transport-3-2-0-3 : P.T.origin tree-2-3-1 (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-3-2-0-3 = refl
occ-3-2-0-4 : P.T.Occurrence tree-3-2-0
occ-3-2-0-4 = (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.source-leg , tt)))
origin-3-2-0-4 : P.T.origin tree-3-2-0 occ-3-2-0-4 ≡ input s31
origin-3-2-0-4 = refl
transport-3-2-0-4 : P.T.origin tree-2-3-1 (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-3-2-0-4 = refl
occ-3-2-0-5 : P.T.Occurrence tree-3-2-0
occ-3-2-0-5 = (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.target-leg , tt)))
origin-3-2-0-5 : P.T.origin tree-3-2-0 occ-3-2-0-5 ≡ input s01
origin-3-2-0-5 = refl
transport-3-2-0-5 : P.T.origin tree-2-3-1 (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.target-leg , tt))) ≡ input (swap s01)
transport-3-2-0-5 = refl
occ-3-2-0-6 : P.T.Occurrence tree-3-2-0
occ-3-2-0-6 = (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.source-leg , tt)))
origin-3-2-0-6 : P.T.origin tree-3-2-0 occ-3-2-0-6 ≡ input s31
origin-3-2-0-6 = refl
transport-3-2-0-6 : P.T.origin tree-2-3-1 (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-3-2-0-6 = refl
occ-3-2-0-7 : P.T.Occurrence tree-3-2-0
occ-3-2-0-7 = (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.target-leg , tt)))
origin-3-2-0-7 : P.T.origin tree-3-2-0 occ-3-2-0-7 ≡ input s21
origin-3-2-0-7 = refl
transport-3-2-0-7 : P.T.origin tree-2-3-1 (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.target-leg , tt))) ≡ input (swap s21)
transport-3-2-0-7 = refl
occ-3-2-0-8 : P.T.Occurrence tree-3-2-0
occ-3-2-0-8 = (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-3-2-0-8 : P.T.origin tree-3-2-0 occ-3-2-0-8 ≡ input s12
origin-3-2-0-8 = refl
transport-3-2-0-8 : P.T.origin tree-2-3-1 (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s12)
transport-3-2-0-8 = refl
occ-3-2-0-9 : P.T.Occurrence tree-3-2-0
occ-3-2-0-9 = (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-3-2-0-9 : P.T.origin tree-3-2-0 occ-3-2-0-9 ≡ input s02
origin-3-2-0-9 = refl
transport-3-2-0-9 : P.T.origin tree-2-3-1 (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-3-2-0-9 = refl
occ-3-2-0-10 : P.T.Occurrence tree-3-2-0
occ-3-2-0-10 = (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-3-2-0-10 : P.T.origin tree-3-2-0 occ-3-2-0-10 ≡ input s32
origin-3-2-0-10 = refl
transport-3-2-0-10 : P.T.origin tree-2-3-1 (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s32)
transport-3-2-0-10 = refl
occ-3-2-0-11 : P.T.Occurrence tree-3-2-0
occ-3-2-0-11 = (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-3-2-0-11 : P.T.origin tree-3-2-0 occ-3-2-0-11 ≡ input s02
origin-3-2-0-11 = refl
transport-3-2-0-11 : P.T.origin tree-2-3-1 (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-3-2-0-11 = refl
occ-3-2-0-12 : P.T.Occurrence tree-3-2-0
occ-3-2-0-12 = (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.source-leg , tt)))
origin-3-2-0-12 : P.T.origin tree-3-2-0 occ-3-2-0-12 ≡ input s13
origin-3-2-0-12 = refl
transport-3-2-0-12 : P.T.origin tree-2-3-1 (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-3-2-0-12 = refl
occ-3-2-0-13 : P.T.Occurrence tree-3-2-0
occ-3-2-0-13 = (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.target-leg , tt)))
origin-3-2-0-13 : P.T.origin tree-3-2-0 occ-3-2-0-13 ≡ input s03
origin-3-2-0-13 = refl
transport-3-2-0-13 : P.T.origin tree-2-3-1 (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.target-leg , tt))) ≡ input (swap s03)
transport-3-2-0-13 = refl
occ-3-2-0-14 : P.T.Occurrence tree-3-2-0
occ-3-2-0-14 = (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.source-leg , tt)))
origin-3-2-0-14 : P.T.origin tree-3-2-0 occ-3-2-0-14 ≡ input s13
origin-3-2-0-14 = refl
transport-3-2-0-14 : P.T.origin tree-2-3-1 (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-3-2-0-14 = refl
occ-3-2-0-15 : P.T.Occurrence tree-3-2-0
occ-3-2-0-15 = (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.target-leg , tt)))
origin-3-2-0-15 : P.T.origin tree-3-2-0 occ-3-2-0-15 ≡ input s23
origin-3-2-0-15 = refl
transport-3-2-0-15 : P.T.origin tree-2-3-1 (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.target-leg , tt))) ≡ input (swap s23)
transport-3-2-0-15 = refl
occ-3-2-0-16 : P.T.Occurrence tree-3-2-0
occ-3-2-0-16 = (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-3-2-0-16 : P.T.origin tree-3-2-0 occ-3-2-0-16 ≡ input s20
origin-3-2-0-16 = refl
transport-3-2-0-16 : P.T.origin tree-2-3-1 (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-3-2-0-16 = refl
occ-3-2-0-17 : P.T.Occurrence tree-3-2-0
occ-3-2-0-17 = (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-3-2-0-17 : P.T.origin tree-3-2-0 occ-3-2-0-17 ≡ input s20
origin-3-2-0-17 = refl
transport-3-2-0-17 : P.T.origin tree-2-3-1 (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-3-2-0-17 = refl
occ-3-2-0-18 : P.T.Occurrence tree-3-2-0
occ-3-2-0-18 = (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-0-1)) , (P.S.source-leg , tt)))
origin-3-2-0-18 : P.T.origin tree-3-2-0 occ-3-2-0-18 ≡ input s01
origin-3-2-0-18 = refl
transport-3-2-0-18 : P.T.origin tree-2-3-1 (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-1-0)) , (P.S.source-leg , tt))) ≡ input (swap s01)
transport-3-2-0-18 = refl
occ-3-2-0-19 : P.T.Occurrence tree-3-2-0
occ-3-2-0-19 = (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-0-1)) , (P.S.target-leg , tt)))
origin-3-2-0-19 : P.T.origin tree-3-2-0 occ-3-2-0-19 ≡ input s01
origin-3-2-0-19 = refl
transport-3-2-0-19 : P.T.origin tree-2-3-1 (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-1-0)) , (P.S.target-leg , tt))) ≡ input (swap s01)
transport-3-2-0-19 = refl
occ-3-2-0-20 : P.T.Occurrence tree-3-2-0
occ-3-2-0-20 = (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.source-leg , tt)))
origin-3-2-0-20 : P.T.origin tree-3-2-0 occ-3-2-0-20 ≡ input s01
origin-3-2-0-20 = refl
transport-3-2-0-20 : P.T.origin tree-2-3-1 (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.source-leg , tt))) ≡ input (swap s01)
transport-3-2-0-20 = refl
occ-3-2-0-21 : P.T.Occurrence tree-3-2-0
occ-3-2-0-21 = (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.target-leg , tt)))
origin-3-2-0-21 : P.T.origin tree-3-2-0 occ-3-2-0-21 ≡ input s21
origin-3-2-0-21 = refl
transport-3-2-0-21 : P.T.origin tree-2-3-1 (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.target-leg , tt))) ≡ input (swap s21)
transport-3-2-0-21 = refl
occ-3-2-0-22 : P.T.Occurrence tree-3-2-0
occ-3-2-0-22 = (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.source-leg , tt)))
origin-3-2-0-22 : P.T.origin tree-3-2-0 occ-3-2-0-22 ≡ input s21
origin-3-2-0-22 = refl
transport-3-2-0-22 : P.T.origin tree-2-3-1 (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.source-leg , tt))) ≡ input (swap s21)
transport-3-2-0-22 = refl
occ-3-2-0-23 : P.T.Occurrence tree-3-2-0
occ-3-2-0-23 = (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.target-leg , tt)))
origin-3-2-0-23 : P.T.origin tree-3-2-0 occ-3-2-0-23 ≡ input s01
origin-3-2-0-23 = refl
transport-3-2-0-23 : P.T.origin tree-2-3-1 (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.target-leg , tt))) ≡ input (swap s01)
transport-3-2-0-23 = refl
occ-3-2-0-24 : P.T.Occurrence tree-3-2-0
occ-3-2-0-24 = (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-2-1)) , (P.S.source-leg , tt)))
origin-3-2-0-24 : P.T.origin tree-3-2-0 occ-3-2-0-24 ≡ input s21
origin-3-2-0-24 = refl
transport-3-2-0-24 : P.T.origin tree-2-3-1 (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-3-0)) , (P.S.source-leg , tt))) ≡ input (swap s21)
transport-3-2-0-24 = refl
occ-3-2-0-25 : P.T.Occurrence tree-3-2-0
occ-3-2-0-25 = (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-2-1)) , (P.S.target-leg , tt)))
origin-3-2-0-25 : P.T.origin tree-3-2-0 occ-3-2-0-25 ≡ input s21
origin-3-2-0-25 = refl
transport-3-2-0-25 : P.T.origin tree-2-3-1 (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-3-0)) , (P.S.target-leg , tt))) ≡ input (swap s21)
transport-3-2-0-25 = refl
occ-3-2-0-26 : P.T.Occurrence tree-3-2-0
occ-3-2-0-26 = (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-3-2-0-26 : P.T.origin tree-3-2-0 occ-3-2-0-26 ≡ input s02
origin-3-2-0-26 = refl
transport-3-2-0-26 : P.T.origin tree-2-3-1 (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-3-2-0-26 = refl
occ-3-2-0-27 : P.T.Occurrence tree-3-2-0
occ-3-2-0-27 = (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-3-2-0-27 : P.T.origin tree-3-2-0 occ-3-2-0-27 ≡ input s02
origin-3-2-0-27 = refl
transport-3-2-0-27 : P.T.origin tree-2-3-1 (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-3-2-0-27 = refl
occ-3-2-0-28 : P.T.Occurrence tree-3-2-0
occ-3-2-0-28 = (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-0-3)) , (P.S.source-leg , tt)))
origin-3-2-0-28 : P.T.origin tree-3-2-0 occ-3-2-0-28 ≡ input s03
origin-3-2-0-28 = refl
transport-3-2-0-28 : P.T.origin tree-2-3-1 (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-1-2)) , (P.S.source-leg , tt))) ≡ input (swap s03)
transport-3-2-0-28 = refl
occ-3-2-0-29 : P.T.Occurrence tree-3-2-0
occ-3-2-0-29 = (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-0-3)) , (P.S.target-leg , tt)))
origin-3-2-0-29 : P.T.origin tree-3-2-0 occ-3-2-0-29 ≡ input s03
origin-3-2-0-29 = refl
transport-3-2-0-29 : P.T.origin tree-2-3-1 (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-1-2)) , (P.S.target-leg , tt))) ≡ input (swap s03)
transport-3-2-0-29 = refl
occ-3-2-0-30 : P.T.Occurrence tree-3-2-0
occ-3-2-0-30 = (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.source-leg , tt)))
origin-3-2-0-30 : P.T.origin tree-3-2-0 occ-3-2-0-30 ≡ input s03
origin-3-2-0-30 = refl
transport-3-2-0-30 : P.T.origin tree-2-3-1 (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.source-leg , tt))) ≡ input (swap s03)
transport-3-2-0-30 = refl
occ-3-2-0-31 : P.T.Occurrence tree-3-2-0
occ-3-2-0-31 = (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.target-leg , tt)))
origin-3-2-0-31 : P.T.origin tree-3-2-0 occ-3-2-0-31 ≡ input s23
origin-3-2-0-31 = refl
transport-3-2-0-31 : P.T.origin tree-2-3-1 (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.target-leg , tt))) ≡ input (swap s23)
transport-3-2-0-31 = refl
occ-3-2-0-32 : P.T.Occurrence tree-3-2-0
occ-3-2-0-32 = (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.source-leg , tt)))
origin-3-2-0-32 : P.T.origin tree-3-2-0 occ-3-2-0-32 ≡ input s23
origin-3-2-0-32 = refl
transport-3-2-0-32 : P.T.origin tree-2-3-1 (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.source-leg , tt))) ≡ input (swap s23)
transport-3-2-0-32 = refl
occ-3-2-0-33 : P.T.Occurrence tree-3-2-0
occ-3-2-0-33 = (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.target-leg , tt)))
origin-3-2-0-33 : P.T.origin tree-3-2-0 occ-3-2-0-33 ≡ input s03
origin-3-2-0-33 = refl
transport-3-2-0-33 : P.T.origin tree-2-3-1 (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.target-leg , tt))) ≡ input (swap s03)
transport-3-2-0-33 = refl
occ-3-2-0-34 : P.T.Occurrence tree-3-2-0
occ-3-2-0-34 = (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-2-3)) , (P.S.source-leg , tt)))
origin-3-2-0-34 : P.T.origin tree-3-2-0 occ-3-2-0-34 ≡ input s23
origin-3-2-0-34 = refl
transport-3-2-0-34 : P.T.origin tree-2-3-1 (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-3-2)) , (P.S.source-leg , tt))) ≡ input (swap s23)
transport-3-2-0-34 = refl
occ-3-2-0-35 : P.T.Occurrence tree-3-2-0
occ-3-2-0-35 = (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-2-3)) , (P.S.target-leg , tt)))
origin-3-2-0-35 : P.T.origin tree-3-2-0 occ-3-2-0-35 ≡ input s23
origin-3-2-0-35 = refl
transport-3-2-0-35 : P.T.origin tree-2-3-1 (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-3-2)) , (P.S.target-leg , tt))) ≡ input (swap s23)
transport-3-2-0-35 = refl
occ-3-2-0-36 : P.T.Occurrence tree-3-2-0
occ-3-2-0-36 = (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-3-2-0-36 : P.T.origin tree-3-2-0 occ-3-2-0-36 ≡ input s10
origin-3-2-0-36 = refl
transport-3-2-0-36 : P.T.origin tree-2-3-1 (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s10)
transport-3-2-0-36 = refl
occ-3-2-0-37 : P.T.Occurrence tree-3-2-0
occ-3-2-0-37 = (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-3-2-0-37 : P.T.origin tree-3-2-0 occ-3-2-0-37 ≡ input s20
origin-3-2-0-37 = refl
transport-3-2-0-37 : P.T.origin tree-2-3-1 (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-3-2-0-37 = refl
occ-3-2-0-38 : P.T.Occurrence tree-3-2-0
occ-3-2-0-38 = (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-3-2-0-38 : P.T.origin tree-3-2-0 occ-3-2-0-38 ≡ input s30
origin-3-2-0-38 = refl
transport-3-2-0-38 : P.T.origin tree-2-3-1 (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s30)
transport-3-2-0-38 = refl
occ-3-2-0-39 : P.T.Occurrence tree-3-2-0
occ-3-2-0-39 = (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-3-2-0-39 : P.T.origin tree-3-2-0 occ-3-2-0-39 ≡ input s20
origin-3-2-0-39 = refl
transport-3-2-0-39 : P.T.origin tree-2-3-1 (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-3-2-0-39 = refl
occ-3-2-0-40 : P.T.Occurrence tree-3-2-0
occ-3-2-0-40 = (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.source-leg , tt)))
origin-3-2-0-40 : P.T.origin tree-3-2-0 occ-3-2-0-40 ≡ input s31
origin-3-2-0-40 = refl
transport-3-2-0-40 : P.T.origin tree-2-3-1 (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-3-2-0-40 = refl
occ-3-2-0-41 : P.T.Occurrence tree-3-2-0
occ-3-2-0-41 = (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.target-leg , tt)))
origin-3-2-0-41 : P.T.origin tree-3-2-0 occ-3-2-0-41 ≡ input s01
origin-3-2-0-41 = refl
transport-3-2-0-41 : P.T.origin tree-2-3-1 (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.target-leg , tt))) ≡ input (swap s01)
transport-3-2-0-41 = refl
occ-3-2-0-42 : P.T.Occurrence tree-3-2-0
occ-3-2-0-42 = (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.source-leg , tt)))
origin-3-2-0-42 : P.T.origin tree-3-2-0 occ-3-2-0-42 ≡ input s31
origin-3-2-0-42 = refl
transport-3-2-0-42 : P.T.origin tree-2-3-1 (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-3-2-0-42 = refl
occ-3-2-0-43 : P.T.Occurrence tree-3-2-0
occ-3-2-0-43 = (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.target-leg , tt)))
origin-3-2-0-43 : P.T.origin tree-3-2-0 occ-3-2-0-43 ≡ input s21
origin-3-2-0-43 = refl
transport-3-2-0-43 : P.T.origin tree-2-3-1 (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.target-leg , tt))) ≡ input (swap s21)
transport-3-2-0-43 = refl
occ-3-2-0-44 : P.T.Occurrence tree-3-2-0
occ-3-2-0-44 = (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-3-2-0-44 : P.T.origin tree-3-2-0 occ-3-2-0-44 ≡ input s12
origin-3-2-0-44 = refl
transport-3-2-0-44 : P.T.origin tree-2-3-1 (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s12)
transport-3-2-0-44 = refl
occ-3-2-0-45 : P.T.Occurrence tree-3-2-0
occ-3-2-0-45 = (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-3-2-0-45 : P.T.origin tree-3-2-0 occ-3-2-0-45 ≡ input s02
origin-3-2-0-45 = refl
transport-3-2-0-45 : P.T.origin tree-2-3-1 (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-3-2-0-45 = refl
occ-3-2-0-46 : P.T.Occurrence tree-3-2-0
occ-3-2-0-46 = (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-3-2-0-46 : P.T.origin tree-3-2-0 occ-3-2-0-46 ≡ input s32
origin-3-2-0-46 = refl
transport-3-2-0-46 : P.T.origin tree-2-3-1 (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s32)
transport-3-2-0-46 = refl
occ-3-2-0-47 : P.T.Occurrence tree-3-2-0
occ-3-2-0-47 = (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-3-2-0-47 : P.T.origin tree-3-2-0 occ-3-2-0-47 ≡ input s02
origin-3-2-0-47 = refl
transport-3-2-0-47 : P.T.origin tree-2-3-1 (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-3-2-0-47 = refl
occ-3-2-0-48 : P.T.Occurrence tree-3-2-0
occ-3-2-0-48 = (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.source-leg , tt)))
origin-3-2-0-48 : P.T.origin tree-3-2-0 occ-3-2-0-48 ≡ input s13
origin-3-2-0-48 = refl
transport-3-2-0-48 : P.T.origin tree-2-3-1 (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-3-2-0-48 = refl
occ-3-2-0-49 : P.T.Occurrence tree-3-2-0
occ-3-2-0-49 = (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.target-leg , tt)))
origin-3-2-0-49 : P.T.origin tree-3-2-0 occ-3-2-0-49 ≡ input s03
origin-3-2-0-49 = refl
transport-3-2-0-49 : P.T.origin tree-2-3-1 (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.target-leg , tt))) ≡ input (swap s03)
transport-3-2-0-49 = refl
occ-3-2-0-50 : P.T.Occurrence tree-3-2-0
occ-3-2-0-50 = (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.source-leg , tt)))
origin-3-2-0-50 : P.T.origin tree-3-2-0 occ-3-2-0-50 ≡ input s13
origin-3-2-0-50 = refl
transport-3-2-0-50 : P.T.origin tree-2-3-1 (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-3-2-0-50 = refl
occ-3-2-0-51 : P.T.Occurrence tree-3-2-0
occ-3-2-0-51 = (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.target-leg , tt)))
origin-3-2-0-51 : P.T.origin tree-3-2-0 occ-3-2-0-51 ≡ input s23
origin-3-2-0-51 = refl
transport-3-2-0-51 : P.T.origin tree-2-3-1 (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.target-leg , tt))) ≡ input (swap s23)
transport-3-2-0-51 = refl
occ-3-2-0-52 : P.T.Occurrence tree-3-2-0
occ-3-2-0-52 = (P.S.full-source , (P.S.first-port , tt))
origin-3-2-0-52 : P.T.origin tree-3-2-0 occ-3-2-0-52 ≡ input s31
origin-3-2-0-52 = refl
transport-3-2-0-52 : P.T.origin tree-2-3-1 (P.S.full-source , (P.S.first-port , tt)) ≡ input (swap s31)
transport-3-2-0-52 = refl
occ-3-2-0-53 : P.T.Occurrence tree-3-2-0
occ-3-2-0-53 = (P.S.full-source , (P.S.middle-port , tt))
origin-3-2-0-53 : P.T.origin tree-3-2-0 occ-3-2-0-53 ≡ input s21
origin-3-2-0-53 = refl
transport-3-2-0-53 : P.T.origin tree-2-3-1 (P.S.full-source , (P.S.middle-port , tt)) ≡ input (swap s21)
transport-3-2-0-53 = refl
occ-3-2-0-54 : P.T.Occurrence tree-3-2-0
occ-3-2-0-54 = (P.S.full-source , (P.S.final-port , tt))
origin-3-2-0-54 : P.T.origin tree-3-2-0 occ-3-2-0-54 ≡ input s01
origin-3-2-0-54 = refl
transport-3-2-0-54 : P.T.origin tree-2-3-1 (P.S.full-source , (P.S.final-port , tt)) ≡ input (swap s01)
transport-3-2-0-54 = refl
selected-source-3-2-0-AB : P.S.ab-index {a = C.q7} {b = C.q0} {c = C.q0} F.triple-3-2-0 ≡ (m0 , (F.vp-3-1 , F.vp-2-1))
selected-source-3-2-0-AB = refl
selected-target-3-2-0-AB : P.S.ab-index {a = C.q0} {b = C.q7} {c = C.q7} F.triple-2-3-1 ≡ (c0 , (F.vp-2-0 , F.vp-3-0))
selected-target-3-2-0-AB = refl
selected-source-3-2-0-BC : P.S.bc-index {a = C.q7} {b = C.q0} {c = C.q0} F.triple-3-2-0 ≡ (m0 , (F.vp-2-1 , F.vp-0-1))
selected-source-3-2-0-BC = refl
selected-target-3-2-0-BC : P.S.bc-index {a = C.q0} {b = C.q7} {c = C.q7} F.triple-2-3-1 ≡ (c0 , (F.vp-3-0 , F.vp-1-0))
selected-target-3-2-0-BC = refl
selected-source-3-2-0-AC : P.S.ac-index {a = C.q7} {b = C.q0} {c = C.q0} F.triple-3-2-0 ≡ (m0 , (F.vp-3-1 , F.vp-0-1))
selected-source-3-2-0-AC = refl
selected-target-3-2-0-AC : P.S.ac-index {a = C.q0} {b = C.q7} {c = C.q7} F.triple-2-3-1 ≡ (c0 , (F.vp-2-0 , F.vp-1-0))
selected-target-3-2-0-AC = refl
occ-3-2-1-0 : P.T.Occurrence tree-3-2-1
occ-3-2-1-0 = (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-3-2-1-0 : P.T.origin tree-3-2-1 occ-3-2-1-0 ≡ input s10
origin-3-2-1-0 = refl
transport-3-2-1-0 : P.T.origin tree-2-3-0 (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s10)
transport-3-2-1-0 = refl
occ-3-2-1-1 : P.T.Occurrence tree-3-2-1
occ-3-2-1-1 = (P.S.AB , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-3-2-1-1 : P.T.origin tree-3-2-1 occ-3-2-1-1 ≡ input s20
origin-3-2-1-1 = refl
transport-3-2-1-1 : P.T.origin tree-2-3-0 (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-3-2-1-1 = refl
occ-3-2-1-2 : P.T.Occurrence tree-3-2-1
occ-3-2-1-2 = (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.source-leg , tt)))
origin-3-2-1-2 : P.T.origin tree-3-2-1 occ-3-2-1-2 ≡ input s30
origin-3-2-1-2 = refl
transport-3-2-1-2 : P.T.origin tree-2-3-0 (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.source-leg , tt))) ≡ input (swap s30)
transport-3-2-1-2 = refl
occ-3-2-1-3 : P.T.Occurrence tree-3-2-1
occ-3-2-1-3 = (P.S.AB , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.target-leg , tt)))
origin-3-2-1-3 : P.T.origin tree-3-2-1 occ-3-2-1-3 ≡ input s20
origin-3-2-1-3 = refl
transport-3-2-1-3 : P.T.origin tree-2-3-0 (P.S.AB , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.target-leg , tt))) ≡ input (swap s20)
transport-3-2-1-3 = refl
occ-3-2-1-4 : P.T.Occurrence tree-3-2-1
occ-3-2-1-4 = (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.source-leg , tt)))
origin-3-2-1-4 : P.T.origin tree-3-2-1 occ-3-2-1-4 ≡ input s31
origin-3-2-1-4 = refl
transport-3-2-1-4 : P.T.origin tree-2-3-0 (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-3-2-1-4 = refl
occ-3-2-1-5 : P.T.Occurrence tree-3-2-1
occ-3-2-1-5 = (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.target-leg , tt)))
origin-3-2-1-5 : P.T.origin tree-3-2-1 occ-3-2-1-5 ≡ input s01
origin-3-2-1-5 = refl
transport-3-2-1-5 : P.T.origin tree-2-3-0 (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.target-leg , tt))) ≡ input (swap s01)
transport-3-2-1-5 = refl
occ-3-2-1-6 : P.T.Occurrence tree-3-2-1
occ-3-2-1-6 = (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.source-leg , tt)))
origin-3-2-1-6 : P.T.origin tree-3-2-1 occ-3-2-1-6 ≡ input s31
origin-3-2-1-6 = refl
transport-3-2-1-6 : P.T.origin tree-2-3-0 (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-3-2-1-6 = refl
occ-3-2-1-7 : P.T.Occurrence tree-3-2-1
occ-3-2-1-7 = (P.S.AB , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.target-leg , tt)))
origin-3-2-1-7 : P.T.origin tree-3-2-1 occ-3-2-1-7 ≡ input s21
origin-3-2-1-7 = refl
transport-3-2-1-7 : P.T.origin tree-2-3-0 (P.S.AB , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.target-leg , tt))) ≡ input (swap s21)
transport-3-2-1-7 = refl
occ-3-2-1-8 : P.T.Occurrence tree-3-2-1
occ-3-2-1-8 = (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-3-2-1-8 : P.T.origin tree-3-2-1 occ-3-2-1-8 ≡ input s12
origin-3-2-1-8 = refl
transport-3-2-1-8 : P.T.origin tree-2-3-0 (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s12)
transport-3-2-1-8 = refl
occ-3-2-1-9 : P.T.Occurrence tree-3-2-1
occ-3-2-1-9 = (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-3-2-1-9 : P.T.origin tree-3-2-1 occ-3-2-1-9 ≡ input s02
origin-3-2-1-9 = refl
transport-3-2-1-9 : P.T.origin tree-2-3-0 (P.S.AB , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-3-2-1-9 = refl
occ-3-2-1-10 : P.T.Occurrence tree-3-2-1
occ-3-2-1-10 = (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
origin-3-2-1-10 : P.T.origin tree-3-2-1 occ-3-2-1-10 ≡ input s32
origin-3-2-1-10 = refl
transport-3-2-1-10 : P.T.origin tree-2-3-0 (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.source-leg , tt))) ≡ input (swap s32)
transport-3-2-1-10 = refl
occ-3-2-1-11 : P.T.Occurrence tree-3-2-1
occ-3-2-1-11 = (P.S.AB , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.target-leg , tt)))
origin-3-2-1-11 : P.T.origin tree-3-2-1 occ-3-2-1-11 ≡ input s02
origin-3-2-1-11 = refl
transport-3-2-1-11 : P.T.origin tree-2-3-0 (P.S.AB , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.target-leg , tt))) ≡ input (swap s02)
transport-3-2-1-11 = refl
occ-3-2-1-12 : P.T.Occurrence tree-3-2-1
occ-3-2-1-12 = (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.source-leg , tt)))
origin-3-2-1-12 : P.T.origin tree-3-2-1 occ-3-2-1-12 ≡ input s13
origin-3-2-1-12 = refl
transport-3-2-1-12 : P.T.origin tree-2-3-0 (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-3-2-1-12 = refl
occ-3-2-1-13 : P.T.Occurrence tree-3-2-1
occ-3-2-1-13 = (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.target-leg , tt)))
origin-3-2-1-13 : P.T.origin tree-3-2-1 occ-3-2-1-13 ≡ input s03
origin-3-2-1-13 = refl
transport-3-2-1-13 : P.T.origin tree-2-3-0 (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.target-leg , tt))) ≡ input (swap s03)
transport-3-2-1-13 = refl
occ-3-2-1-14 : P.T.Occurrence tree-3-2-1
occ-3-2-1-14 = (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.source-leg , tt)))
origin-3-2-1-14 : P.T.origin tree-3-2-1 occ-3-2-1-14 ≡ input s13
origin-3-2-1-14 = refl
transport-3-2-1-14 : P.T.origin tree-2-3-0 (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-3-2-1-14 = refl
occ-3-2-1-15 : P.T.Occurrence tree-3-2-1
occ-3-2-1-15 = (P.S.AB , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.target-leg , tt)))
origin-3-2-1-15 : P.T.origin tree-3-2-1 occ-3-2-1-15 ≡ input s23
origin-3-2-1-15 = refl
transport-3-2-1-15 : P.T.origin tree-2-3-0 (P.S.AB , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.target-leg , tt))) ≡ input (swap s23)
transport-3-2-1-15 = refl
occ-3-2-1-16 : P.T.Occurrence tree-3-2-1
occ-3-2-1-16 = (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.source-leg , tt)))
origin-3-2-1-16 : P.T.origin tree-3-2-1 occ-3-2-1-16 ≡ input s20
origin-3-2-1-16 = refl
transport-3-2-1-16 : P.T.origin tree-2-3-0 (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-3-2-1-16 = refl
occ-3-2-1-17 : P.T.Occurrence tree-3-2-1
occ-3-2-1-17 = (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-1-0)) , (P.S.target-leg , tt)))
origin-3-2-1-17 : P.T.origin tree-3-2-1 occ-3-2-1-17 ≡ input s10
origin-3-2-1-17 = refl
transport-3-2-1-17 : P.T.origin tree-2-3-0 (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-0-1)) , (P.S.target-leg , tt))) ≡ input (swap s10)
transport-3-2-1-17 = refl
occ-3-2-1-18 : P.T.Occurrence tree-3-2-1
occ-3-2-1-18 = (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.source-leg , tt)))
origin-3-2-1-18 : P.T.origin tree-3-2-1 occ-3-2-1-18 ≡ input s20
origin-3-2-1-18 = refl
transport-3-2-1-18 : P.T.origin tree-2-3-0 (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.source-leg , tt))) ≡ input (swap s20)
transport-3-2-1-18 = refl
occ-3-2-1-19 : P.T.Occurrence tree-3-2-1
occ-3-2-1-19 = (P.S.BC , ((c0 , (F.vp-2-0 , F.vp-3-0)) , (P.S.target-leg , tt)))
origin-3-2-1-19 : P.T.origin tree-3-2-1 occ-3-2-1-19 ≡ input s30
origin-3-2-1-19 = refl
transport-3-2-1-19 : P.T.origin tree-2-3-0 (P.S.BC , ((m0 , (F.vp-3-1 , F.vp-2-1)) , (P.S.target-leg , tt))) ≡ input (swap s30)
transport-3-2-1-19 = refl
occ-3-2-1-20 : P.T.Occurrence tree-3-2-1
occ-3-2-1-20 = (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-3-2-1-20 : P.T.origin tree-3-2-1 occ-3-2-1-20 ≡ input s01
origin-3-2-1-20 = refl
transport-3-2-1-20 : P.T.origin tree-2-3-0 (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s01)
transport-3-2-1-20 = refl
occ-3-2-1-21 : P.T.Occurrence tree-3-2-1
occ-3-2-1-21 = (P.S.BC , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-3-2-1-21 : P.T.origin tree-3-2-1 occ-3-2-1-21 ≡ input s31
origin-3-2-1-21 = refl
transport-3-2-1-21 : P.T.origin tree-2-3-0 (P.S.BC , ((c0 , (F.vp-1-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-3-2-1-21 = refl
occ-3-2-1-22 : P.T.Occurrence tree-3-2-1
occ-3-2-1-22 = (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-3-2-1-22 : P.T.origin tree-3-2-1 occ-3-2-1-22 ≡ input s21
origin-3-2-1-22 = refl
transport-3-2-1-22 : P.T.origin tree-2-3-0 (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s21)
transport-3-2-1-22 = refl
occ-3-2-1-23 : P.T.Occurrence tree-3-2-1
occ-3-2-1-23 = (P.S.BC , ((m0 , (F.vp-2-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-3-2-1-23 : P.T.origin tree-3-2-1 occ-3-2-1-23 ≡ input s31
origin-3-2-1-23 = refl
transport-3-2-1-23 : P.T.origin tree-2-3-0 (P.S.BC , ((c0 , (F.vp-3-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-3-2-1-23 = refl
occ-3-2-1-24 : P.T.Occurrence tree-3-2-1
occ-3-2-1-24 = (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.source-leg , tt)))
origin-3-2-1-24 : P.T.origin tree-3-2-1 occ-3-2-1-24 ≡ input s02
origin-3-2-1-24 = refl
transport-3-2-1-24 : P.T.origin tree-2-3-0 (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-3-2-1-24 = refl
occ-3-2-1-25 : P.T.Occurrence tree-3-2-1
occ-3-2-1-25 = (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-1-2)) , (P.S.target-leg , tt)))
origin-3-2-1-25 : P.T.origin tree-3-2-1 occ-3-2-1-25 ≡ input s12
origin-3-2-1-25 = refl
transport-3-2-1-25 : P.T.origin tree-2-3-0 (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-0-3)) , (P.S.target-leg , tt))) ≡ input (swap s12)
transport-3-2-1-25 = refl
occ-3-2-1-26 : P.T.Occurrence tree-3-2-1
occ-3-2-1-26 = (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.source-leg , tt)))
origin-3-2-1-26 : P.T.origin tree-3-2-1 occ-3-2-1-26 ≡ input s02
origin-3-2-1-26 = refl
transport-3-2-1-26 : P.T.origin tree-2-3-0 (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.source-leg , tt))) ≡ input (swap s02)
transport-3-2-1-26 = refl
occ-3-2-1-27 : P.T.Occurrence tree-3-2-1
occ-3-2-1-27 = (P.S.BC , ((c1 , (F.vp-0-2 , F.vp-3-2)) , (P.S.target-leg , tt)))
origin-3-2-1-27 : P.T.origin tree-3-2-1 occ-3-2-1-27 ≡ input s32
origin-3-2-1-27 = refl
transport-3-2-1-27 : P.T.origin tree-2-3-0 (P.S.BC , ((m1 , (F.vp-1-3 , F.vp-2-3)) , (P.S.target-leg , tt))) ≡ input (swap s32)
transport-3-2-1-27 = refl
occ-3-2-1-28 : P.T.Occurrence tree-3-2-1
occ-3-2-1-28 = (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-3-2-1-28 : P.T.origin tree-3-2-1 occ-3-2-1-28 ≡ input s03
origin-3-2-1-28 = refl
transport-3-2-1-28 : P.T.origin tree-2-3-0 (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s03)
transport-3-2-1-28 = refl
occ-3-2-1-29 : P.T.Occurrence tree-3-2-1
occ-3-2-1-29 = (P.S.BC , ((m1 , (F.vp-0-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-3-2-1-29 : P.T.origin tree-3-2-1 occ-3-2-1-29 ≡ input s13
origin-3-2-1-29 = refl
transport-3-2-1-29 : P.T.origin tree-2-3-0 (P.S.BC , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-3-2-1-29 = refl
occ-3-2-1-30 : P.T.Occurrence tree-3-2-1
occ-3-2-1-30 = (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-3-2-1-30 : P.T.origin tree-3-2-1 occ-3-2-1-30 ≡ input s23
origin-3-2-1-30 = refl
transport-3-2-1-30 : P.T.origin tree-2-3-0 (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s23)
transport-3-2-1-30 = refl
occ-3-2-1-31 : P.T.Occurrence tree-3-2-1
occ-3-2-1-31 = (P.S.BC , ((m1 , (F.vp-2-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-3-2-1-31 : P.T.origin tree-3-2-1 occ-3-2-1-31 ≡ input s13
origin-3-2-1-31 = refl
transport-3-2-1-31 : P.T.origin tree-2-3-0 (P.S.BC , ((c1 , (F.vp-3-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-3-2-1-31 = refl
occ-3-2-1-32 : P.T.Occurrence tree-3-2-1
occ-3-2-1-32 = (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-1-0)) , (P.S.source-leg , tt)))
origin-3-2-1-32 : P.T.origin tree-3-2-1 occ-3-2-1-32 ≡ input s10
origin-3-2-1-32 = refl
transport-3-2-1-32 : P.T.origin tree-2-3-0 (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-0-1)) , (P.S.source-leg , tt))) ≡ input (swap s10)
transport-3-2-1-32 = refl
occ-3-2-1-33 : P.T.Occurrence tree-3-2-1
occ-3-2-1-33 = (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-1-0)) , (P.S.target-leg , tt)))
origin-3-2-1-33 : P.T.origin tree-3-2-1 occ-3-2-1-33 ≡ input s10
origin-3-2-1-33 = refl
transport-3-2-1-33 : P.T.origin tree-2-3-0 (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-0-1)) , (P.S.target-leg , tt))) ≡ input (swap s10)
transport-3-2-1-33 = refl
occ-3-2-1-34 : P.T.Occurrence tree-3-2-1
occ-3-2-1-34 = (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.source-leg , tt)))
origin-3-2-1-34 : P.T.origin tree-3-2-1 occ-3-2-1-34 ≡ input s10
origin-3-2-1-34 = refl
transport-3-2-1-34 : P.T.origin tree-2-3-0 (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.source-leg , tt))) ≡ input (swap s10)
transport-3-2-1-34 = refl
occ-3-2-1-35 : P.T.Occurrence tree-3-2-1
occ-3-2-1-35 = (P.S.AC , ((c0 , (F.vp-1-0 , F.vp-3-0)) , (P.S.target-leg , tt)))
origin-3-2-1-35 : P.T.origin tree-3-2-1 occ-3-2-1-35 ≡ input s30
origin-3-2-1-35 = refl
transport-3-2-1-35 : P.T.origin tree-2-3-0 (P.S.AC , ((m0 , (F.vp-0-1 , F.vp-2-1)) , (P.S.target-leg , tt))) ≡ input (swap s30)
transport-3-2-1-35 = refl
occ-3-2-1-36 : P.T.Occurrence tree-3-2-1
occ-3-2-1-36 = (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.source-leg , tt)))
origin-3-2-1-36 : P.T.origin tree-3-2-1 occ-3-2-1-36 ≡ input s30
origin-3-2-1-36 = refl
transport-3-2-1-36 : P.T.origin tree-2-3-0 (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.source-leg , tt))) ≡ input (swap s30)
transport-3-2-1-36 = refl
occ-3-2-1-37 : P.T.Occurrence tree-3-2-1
occ-3-2-1-37 = (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-1-0)) , (P.S.target-leg , tt)))
origin-3-2-1-37 : P.T.origin tree-3-2-1 occ-3-2-1-37 ≡ input s10
origin-3-2-1-37 = refl
transport-3-2-1-37 : P.T.origin tree-2-3-0 (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-0-1)) , (P.S.target-leg , tt))) ≡ input (swap s10)
transport-3-2-1-37 = refl
occ-3-2-1-38 : P.T.Occurrence tree-3-2-1
occ-3-2-1-38 = (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-3-0)) , (P.S.source-leg , tt)))
origin-3-2-1-38 : P.T.origin tree-3-2-1 occ-3-2-1-38 ≡ input s30
origin-3-2-1-38 = refl
transport-3-2-1-38 : P.T.origin tree-2-3-0 (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-2-1)) , (P.S.source-leg , tt))) ≡ input (swap s30)
transport-3-2-1-38 = refl
occ-3-2-1-39 : P.T.Occurrence tree-3-2-1
occ-3-2-1-39 = (P.S.AC , ((c0 , (F.vp-3-0 , F.vp-3-0)) , (P.S.target-leg , tt)))
origin-3-2-1-39 : P.T.origin tree-3-2-1 occ-3-2-1-39 ≡ input s30
origin-3-2-1-39 = refl
transport-3-2-1-39 : P.T.origin tree-2-3-0 (P.S.AC , ((m0 , (F.vp-2-1 , F.vp-2-1)) , (P.S.target-leg , tt))) ≡ input (swap s30)
transport-3-2-1-39 = refl
occ-3-2-1-40 : P.T.Occurrence tree-3-2-1
occ-3-2-1-40 = (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
origin-3-2-1-40 : P.T.origin tree-3-2-1 occ-3-2-1-40 ≡ input s31
origin-3-2-1-40 = refl
transport-3-2-1-40 : P.T.origin tree-2-3-0 (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-2-0)) , (P.S.source-leg , tt))) ≡ input (swap s31)
transport-3-2-1-40 = refl
occ-3-2-1-41 : P.T.Occurrence tree-3-2-1
occ-3-2-1-41 = (P.S.AC , ((m0 , (F.vp-3-1 , F.vp-3-1)) , (P.S.target-leg , tt)))
origin-3-2-1-41 : P.T.origin tree-3-2-1 occ-3-2-1-41 ≡ input s31
origin-3-2-1-41 = refl
transport-3-2-1-41 : P.T.origin tree-2-3-0 (P.S.AC , ((c0 , (F.vp-2-0 , F.vp-2-0)) , (P.S.target-leg , tt))) ≡ input (swap s31)
transport-3-2-1-41 = refl
occ-3-2-1-42 : P.T.Occurrence tree-3-2-1
occ-3-2-1-42 = (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-1-2)) , (P.S.source-leg , tt)))
origin-3-2-1-42 : P.T.origin tree-3-2-1 occ-3-2-1-42 ≡ input s12
origin-3-2-1-42 = refl
transport-3-2-1-42 : P.T.origin tree-2-3-0 (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-0-3)) , (P.S.source-leg , tt))) ≡ input (swap s12)
transport-3-2-1-42 = refl
occ-3-2-1-43 : P.T.Occurrence tree-3-2-1
occ-3-2-1-43 = (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-1-2)) , (P.S.target-leg , tt)))
origin-3-2-1-43 : P.T.origin tree-3-2-1 occ-3-2-1-43 ≡ input s12
origin-3-2-1-43 = refl
transport-3-2-1-43 : P.T.origin tree-2-3-0 (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-0-3)) , (P.S.target-leg , tt))) ≡ input (swap s12)
transport-3-2-1-43 = refl
occ-3-2-1-44 : P.T.Occurrence tree-3-2-1
occ-3-2-1-44 = (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.source-leg , tt)))
origin-3-2-1-44 : P.T.origin tree-3-2-1 occ-3-2-1-44 ≡ input s12
origin-3-2-1-44 = refl
transport-3-2-1-44 : P.T.origin tree-2-3-0 (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.source-leg , tt))) ≡ input (swap s12)
transport-3-2-1-44 = refl
occ-3-2-1-45 : P.T.Occurrence tree-3-2-1
occ-3-2-1-45 = (P.S.AC , ((c1 , (F.vp-1-2 , F.vp-3-2)) , (P.S.target-leg , tt)))
origin-3-2-1-45 : P.T.origin tree-3-2-1 occ-3-2-1-45 ≡ input s32
origin-3-2-1-45 = refl
transport-3-2-1-45 : P.T.origin tree-2-3-0 (P.S.AC , ((m1 , (F.vp-0-3 , F.vp-2-3)) , (P.S.target-leg , tt))) ≡ input (swap s32)
transport-3-2-1-45 = refl
occ-3-2-1-46 : P.T.Occurrence tree-3-2-1
occ-3-2-1-46 = (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.source-leg , tt)))
origin-3-2-1-46 : P.T.origin tree-3-2-1 occ-3-2-1-46 ≡ input s32
origin-3-2-1-46 = refl
transport-3-2-1-46 : P.T.origin tree-2-3-0 (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.source-leg , tt))) ≡ input (swap s32)
transport-3-2-1-46 = refl
occ-3-2-1-47 : P.T.Occurrence tree-3-2-1
occ-3-2-1-47 = (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-1-2)) , (P.S.target-leg , tt)))
origin-3-2-1-47 : P.T.origin tree-3-2-1 occ-3-2-1-47 ≡ input s12
origin-3-2-1-47 = refl
transport-3-2-1-47 : P.T.origin tree-2-3-0 (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-0-3)) , (P.S.target-leg , tt))) ≡ input (swap s12)
transport-3-2-1-47 = refl
occ-3-2-1-48 : P.T.Occurrence tree-3-2-1
occ-3-2-1-48 = (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-3-2)) , (P.S.source-leg , tt)))
origin-3-2-1-48 : P.T.origin tree-3-2-1 occ-3-2-1-48 ≡ input s32
origin-3-2-1-48 = refl
transport-3-2-1-48 : P.T.origin tree-2-3-0 (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-2-3)) , (P.S.source-leg , tt))) ≡ input (swap s32)
transport-3-2-1-48 = refl
occ-3-2-1-49 : P.T.Occurrence tree-3-2-1
occ-3-2-1-49 = (P.S.AC , ((c1 , (F.vp-3-2 , F.vp-3-2)) , (P.S.target-leg , tt)))
origin-3-2-1-49 : P.T.origin tree-3-2-1 occ-3-2-1-49 ≡ input s32
origin-3-2-1-49 = refl
transport-3-2-1-49 : P.T.origin tree-2-3-0 (P.S.AC , ((m1 , (F.vp-2-3 , F.vp-2-3)) , (P.S.target-leg , tt))) ≡ input (swap s32)
transport-3-2-1-49 = refl
occ-3-2-1-50 : P.T.Occurrence tree-3-2-1
occ-3-2-1-50 = (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-1-3)) , (P.S.source-leg , tt)))
origin-3-2-1-50 : P.T.origin tree-3-2-1 occ-3-2-1-50 ≡ input s13
origin-3-2-1-50 = refl
transport-3-2-1-50 : P.T.origin tree-2-3-0 (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-0-2)) , (P.S.source-leg , tt))) ≡ input (swap s13)
transport-3-2-1-50 = refl
occ-3-2-1-51 : P.T.Occurrence tree-3-2-1
occ-3-2-1-51 = (P.S.AC , ((m1 , (F.vp-1-3 , F.vp-1-3)) , (P.S.target-leg , tt)))
origin-3-2-1-51 : P.T.origin tree-3-2-1 occ-3-2-1-51 ≡ input s13
origin-3-2-1-51 = refl
transport-3-2-1-51 : P.T.origin tree-2-3-0 (P.S.AC , ((c1 , (F.vp-0-2 , F.vp-0-2)) , (P.S.target-leg , tt))) ≡ input (swap s13)
transport-3-2-1-51 = refl
occ-3-2-1-52 : P.T.Occurrence tree-3-2-1
occ-3-2-1-52 = (P.S.full-source , (P.S.first-port , tt))
origin-3-2-1-52 : P.T.origin tree-3-2-1 occ-3-2-1-52 ≡ input s30
origin-3-2-1-52 = refl
transport-3-2-1-52 : P.T.origin tree-2-3-0 (P.S.full-source , (P.S.first-port , tt)) ≡ input (swap s30)
transport-3-2-1-52 = refl
occ-3-2-1-53 : P.T.Occurrence tree-3-2-1
occ-3-2-1-53 = (P.S.full-source , (P.S.middle-port , tt))
origin-3-2-1-53 : P.T.origin tree-3-2-1 occ-3-2-1-53 ≡ input s20
origin-3-2-1-53 = refl
transport-3-2-1-53 : P.T.origin tree-2-3-0 (P.S.full-source , (P.S.middle-port , tt)) ≡ input (swap s20)
transport-3-2-1-53 = refl
occ-3-2-1-54 : P.T.Occurrence tree-3-2-1
occ-3-2-1-54 = (P.S.full-source , (P.S.final-port , tt))
origin-3-2-1-54 : P.T.origin tree-3-2-1 occ-3-2-1-54 ≡ input s10
origin-3-2-1-54 = refl
transport-3-2-1-54 : P.T.origin tree-2-3-0 (P.S.full-source , (P.S.final-port , tt)) ≡ input (swap s10)
transport-3-2-1-54 = refl
selected-source-3-2-1-AB : P.S.ab-index {a = C.q7} {b = C.q0} {c = C.q7} F.triple-3-2-1 ≡ (c0 , (F.vp-3-0 , F.vp-2-0))
selected-source-3-2-1-AB = refl
selected-target-3-2-1-AB : P.S.ab-index {a = C.q0} {b = C.q7} {c = C.q0} F.triple-2-3-0 ≡ (m0 , (F.vp-2-1 , F.vp-3-1))
selected-target-3-2-1-AB = refl
selected-source-3-2-1-BC : P.S.bc-index {a = C.q7} {b = C.q0} {c = C.q7} F.triple-3-2-1 ≡ (c0 , (F.vp-2-0 , F.vp-1-0))
selected-source-3-2-1-BC = refl
selected-target-3-2-1-BC : P.S.bc-index {a = C.q0} {b = C.q7} {c = C.q0} F.triple-2-3-0 ≡ (m0 , (F.vp-3-1 , F.vp-0-1))
selected-target-3-2-1-BC = refl
selected-source-3-2-1-AC : P.S.ac-index {a = C.q7} {b = C.q0} {c = C.q7} F.triple-3-2-1 ≡ (c0 , (F.vp-3-0 , F.vp-1-0))
selected-source-3-2-1-AC = refl
selected-target-3-2-1-AC : P.S.ac-index {a = C.q0} {b = C.q7} {c = C.q0} F.triple-2-3-0 ≡ (m0 , (F.vp-2-1 , F.vp-0-1))
selected-target-3-2-1-AC = refl
