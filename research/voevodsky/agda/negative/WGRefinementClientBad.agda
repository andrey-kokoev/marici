{-# OPTIONS --safe --cubical --guardedness #-}
module WGRefinementClientBad where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (false; true)
open import ComposableWitnessSpecialization using (Refinement)
import WGRefinementClient as W
-- Must fail for the identical false = true obligation, not a missing import.
bad : Refinement.Extra W.second
  ((false , true) , false) ((true , false) , true) (refl , false)
bad = refl
