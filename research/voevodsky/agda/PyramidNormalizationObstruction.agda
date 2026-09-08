{-# OPTIONS --safe --cubical --guardedness #-}
module PyramidNormalizationObstruction where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ; zero; suc)
open import Cubical.Data.Nat.Properties using (znots)
open import Cubical.Data.Empty using (⊥)

-- Minimal extracted normalization test for the actual primitive cycle z.
-- The source differential sends z to zero and road augmentation sends z to 1.
data PrimitiveCycle : Type where
  z : PrimitiveCycle

sourceBoundary : PrimitiveCycle → ℕ
sourceBoundary z = zero

roadAugmentation : PrimitiveCycle → ℕ
roadAugmentation z = suc zero

-- A homotopy from the augmentation to zero in a target concentrated in the
-- augmentation degree would provide H d = augmentation. Additivity implies
-- H(0)=0; this is retained explicitly rather than assuming an arbitrary map.
record Nullhomotopy : Type where
  field
    H : ℕ → ℕ
    Hzero : H zero ≡ zero
    boundaryEquation : (v : PrimitiveCycle)
      → roadAugmentation v ≡ H (sourceBoundary v)

augmentationNotNullhomotopic : Nullhomotopy → ⊥
augmentationNotNullhomotopic witness =
  znots {n = zero} (sym (Nullhomotopy.boundaryEquation witness z
    ∙ Nullhomotopy.Hzero witness))

-- Abstract transport form: a comparison preserving the normalized class
-- cannot identify it with an exact class whose cycle value is zero.
record NormalizedComparison : Type where
  field
    transportedValue : ℕ
    preservesSourceUnit : transportedValue ≡ suc zero
    targetExactValue : transportedValue ≡ zero

normalizedComparisonImpossible : NormalizedComparison → ⊥
normalizedComparisonImpossible comparison =
  znots {n = zero} (sym (sym (NormalizedComparison.preservesSourceUnit comparison)
    ∙ NormalizedComparison.targetExactValue comparison))

-- This theorem is intentionally only the extracted cycle-level no-go.
-- It does not identify the six-point source with the corrected Morse source,
-- construct a derived localization, or assert that every physical Q map is
-- exact. It rules out only a comparison satisfying BOTH displayed values.
