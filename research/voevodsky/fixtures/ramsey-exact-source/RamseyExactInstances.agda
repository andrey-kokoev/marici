{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyExactInstances where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (zero; suc)
open import Cubical.Data.Int.Base using (pos)
open import Cubical.Data.Unit.Base using (tt)
open import RamseyUniformRelative using (Slot; first; next; nil; cons)
open import RamseyUniformSigned using (zero3)
open import RamseyExactSource
letters : Slot 1 → Shift
letters first = pos 1 , (pos 0 , pos 0)
module E = Query 0 1 0 1 letters (λ _ → first)
empty-word : E.R.Resolve (E.result-package nil)
empty-word = E.result nil
module O = Query 0 1 1 1 letters (λ _ → first)
outside-word : O.R.Resolve (O.result-package (cons first nil))
outside-word = O.result (cons first nil)
