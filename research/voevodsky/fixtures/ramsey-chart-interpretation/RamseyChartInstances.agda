{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyChartInstances where
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
letters : Slot 1 → Shift
letters first = pos 1 , (pos 0 , pos 0)
module Q = M.Queries 1 1 letters
native : M.T.Resolve (M.target (Q.result-program (cons first nil)))
native = Q.interpreted-result (cons first nil)
