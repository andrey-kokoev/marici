{-# OPTIONS --safe --cubical --guardedness #-}
module RHThetaSixNormalIncidenceAudit where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)
open import Cubical.Data.Sigma

-- The frozen six target ports.  These are labels, not six assumed source maps.
data NormalPort : Type where
  n₀ n₁ n₂ n₃ n₄ n₅ : NormalPort

-- The currently reached rank-four static stratum.
data StaticPivot : Type where
  p₀ p₁ p₂ p₃ : StaticPivot

pivotPort : StaticPivot → NormalPort
pivotPort p₀ = n₀
pivotPort p₁ = n₁
pivotPort p₂ = n₂
pivotPort p₃ = n₃

-- An incidence audit does not manufacture the two missing maps.  It records
-- exact source and target types, the static map, four split pivots, and
-- independent kernel/cokernel witnesses supplied by the source theory.
record StaticIncidenceAudit {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    Scalar Source Target : Type ℓ
    zeroS : Source
    zeroT : Target
    incidence : Source → Target

    sourcePivot : StaticPivot → Source
    targetPort : NormalPort → Target
    pivotReadout : StaticPivot → Target → Scalar
    zeroScalar : Scalar
    oneScalar : Scalar
    zeroNeOne : zeroScalar ≡ oneScalar → ⊥

    -- Exact 4-by-4 identity minor.
    pivotDiagonal : (i : StaticPivot) →
      pivotReadout i (incidence (sourcePivot i)) ≡ oneScalar
    pivotOffDiagonal : (i j : StaticPivot) →
      i ≡ j → ⊥ →
      pivotReadout i (incidence (sourcePivot j)) ≡ zeroScalar

    -- Two source residuals killed by every one of the four static readouts.
    oddKernel₀ oddKernel₁ : Source
    kernel₀ : incidence oddKernel₀ ≡ zeroT
    kernel₁ : incidence oddKernel₁ ≡ zeroT
    kernelIndependent : oddKernel₀ ≡ oddKernel₁ → ⊥

    -- Two target classifiers vanish on the whole static image and distinguish
    -- the two currently unreached normal ports.
    cokernelReadout₄ cokernelReadout₅ : Target → Scalar
    cokernel₄Vanishes : (x : Source) →
      cokernelReadout₄ (incidence x) ≡ zeroScalar
    cokernel₅Vanishes : (x : Source) →
      cokernelReadout₅ (incidence x) ≡ zeroScalar
    cokernel₄Detects : cokernelReadout₄ (targetPort n₄) ≡ oneScalar
    cokernel₄Separates : cokernelReadout₄ (targetPort n₅) ≡ zeroScalar
    cokernel₅Separates : cokernelReadout₅ (targetPort n₄) ≡ zeroScalar
    cokernel₅Detects : cokernelReadout₅ (targetPort n₅) ≡ oneScalar

open StaticIncidenceAudit public

-- Existing incidence cannot hit either distinguished missing port.
missingPort₄NotInImage : {ℓ : Level} (A : StaticIncidenceAudit {ℓ}) →
  (Σ (Source A) λ x → incidence A x ≡ targetPort A n₄) → ⊥
missingPort₄NotInImage A (x , hit) =
  zeroNeOne A
    (sym (cokernel₄Vanishes A x) ∙
     cong (cokernelReadout₄ A) hit ∙
     cokernel₄Detects A)

missingPort₅NotInImage : {ℓ : Level} (A : StaticIncidenceAudit {ℓ}) →
  (Σ (Source A) λ x → incidence A x ≡ targetPort A n₅) → ⊥
missingPort₅NotInImage A (x , hit) =
  zeroNeOne A
    (sym (cokernel₅Vanishes A x) ∙
     cong (cokernelReadout₅ A) hit ∙
     cokernel₅Detects A)

-- Any extension must supply actual source maps for both missing ports.
record TwoDirectionExtension {ℓ : Level}
  (A : StaticIncidenceAudit {ℓ}) : Type ℓ where
  field
    source₄ source₅ : Source A
    reaches₄ : incidence A source₄ ≡ targetPort A n₄
    reaches₅ : incidence A source₅ ≡ targetPort A n₅

-- Hence such an extension is impossible for the frozen static incidence.
-- A lawful constructor must change the incidence through an authorized
-- promotion, rather than merely relabel target vectors as source observations.
staticExtensionContradiction : {ℓ : Level} (A : StaticIncidenceAudit {ℓ}) →
  TwoDirectionExtension A → ⊥
staticExtensionContradiction A E =
  missingPort₄NotInImage A
    (TwoDirectionExtension.source₄ E , TwoDirectionExtension.reaches₄ E)
