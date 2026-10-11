{-# OPTIONS --safe --cubical --guardedness #-}
module WGRefinementBaselineBad where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (false; true)
import WGRefinementBaseline as B
-- Must fail: same endpoints and base equality, but first payload was erased.
bad : B.SecondEvidence ((false , true) , false) ((true , false) , true) (refl , false)
bad = refl
