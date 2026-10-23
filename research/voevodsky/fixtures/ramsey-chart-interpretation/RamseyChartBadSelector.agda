{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyChartBadSelector where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (zero; suc)
open import Cubical.Data.Int.Base using (pos)
open import Cubical.Data.Unit.Base using (tt)
open import RamseyUniformRelative using (Slot; first; next; nil; cons)
open import RamseyUniformSigned using (zero3)
open import RamseyExactSource using (Region; Shift; Member)
open import RamseyChartInterpretation
color : Region 0 → Slot 1
color _ = first
module M = Interpretation 0 1 color
F : Slot 2 → M.Program
F _ = M.input (zero3 , tt)
bad : fst (N.value (M.target (M.pick (Slot 2) F first))) ≡ next first
bad = refl
