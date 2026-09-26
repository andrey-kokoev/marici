{-# OPTIONS --safe --cubical --guardedness #-}
module negative.GraphActionBadScreening where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Int.Base using (pos)
open import GraphAction
-- EXPECTED FAILURE: the old Poisson stationary point is not stationary
-- after adding the screening term.
bad : pEval (pDerivative screened) (pos 1) ≡ pos 0
bad = refl
