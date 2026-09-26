{-# OPTIONS --safe --cubical --guardedness #-}
module negative.GraphActionBadDerivative where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Int.Base using (pos)
open import GraphAction
-- EXPECTED FAILURE: derivative of q^2 at q=1 is 2, not 1.
bad : pEval (pDerivative (piece leftEdge)) (pos 1) ≡ pos 1
bad = refl
