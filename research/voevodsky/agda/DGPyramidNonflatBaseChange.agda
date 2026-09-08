{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidNonflatBaseChange where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)

-- RHom has a canonical directional base-change map. Being an equivalence is a
-- separate obligation; it is not available merely from a coefficient map.
record RHomBaseChangeCertificate {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    SourceRegime TargetRegime : Type ℓ
    sourceRegime : SourceRegime
    targetRegime : TargetRegime
    SourceRHom DerivedBaseChange TargetRHom : Type ℓ
    baseChangeMap : DerivedBaseChange → TargetRHom
    derivesFromSourceRHom : SourceRHom → DerivedBaseChange

    IsBaseChangeEquivalence : (DerivedBaseChange → TargetRHom) → Type ℓ
    EquivalenceHypothesis : Type ℓ
    equivalenceFromHypothesis :
      EquivalenceHypothesis → IsBaseChangeEquivalence baseChangeMap

    -- Concrete nonflat control used by the alternating-sheet/Rees update.
    Nonflat : Type ℓ
    nonflatWitness : Nonflat
    OldMultiplier OldTopRepresentative TargetValue : Type ℓ
    oldMultiplier : OldMultiplier
    oldTopRepresentative : OldTopRepresentative
    zeroTarget : TargetValue
    mapOldMultiplier : OldMultiplier → TargetValue
    mapOldTopRepresentative : OldTopRepresentative → TargetValue
    oldMultiplierMapsToZero : mapOldMultiplier oldMultiplier ≡ zeroTarget
    oldTopMapsToZero : mapOldTopRepresentative oldTopRepresentative ≡ zeroTarget

    -- The independently recomputed target certificate cannot be replaced by
    -- homology-level substitution through this nonflat map.
    TransportedHomologyFormula : Type ℓ
    transportedFormulaInvalid : TransportedHomologyFormula → ⊥

open RHomBaseChangeCertificate public

cannotUseOldHomologyFormula : {ℓ : Level}
  (C : RHomBaseChangeCertificate {ℓ}) → TransportedHomologyFormula C → ⊥
cannotUseOldHomologyFormula C = transportedFormulaInvalid C

-- No unconditional inhabitant of IsBaseChangeEquivalence is exported.
