{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyComparisonForgettingExamples where
open import Cubical.Foundations.Prelude
open import RamseySingleFrameFaces using (c0; m0)
import RamseySourceBoundComparison as C
open import RamseyComparisonForgetting

-- The existing source-bound policy fixes the complete root. Therefore this
-- factor exists, but its definition has the entire target context baked in.
source-only-factor-under-fixed-admission :
  Factors {X = Σ C.Root C.Valid} (λ x → C.view c0 (fst x)) (λ x → C.view m0 (fst x))
source-only-factor-under-fixed-admission = canonical-factor C.actual (C.view c0) (C.view m0)
