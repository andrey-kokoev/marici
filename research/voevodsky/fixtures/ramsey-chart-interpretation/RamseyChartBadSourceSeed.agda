{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyChartBadSourceSeed where
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
bad : M.T.Resolve (M.source-fiber (zero3 , tt))
bad = M.T.seed ((zero3 , tt) , refl)
