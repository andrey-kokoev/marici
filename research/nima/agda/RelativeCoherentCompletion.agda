{-# OPTIONS --safe --cubical --guardedness #-}
module RelativeCoherentCompletion where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.HLevels using (isOfHLevelRespectEquiv; isPropΠ)
open import Cubical.Functions.Fibration using (fiberEquiv)

-- Shared constructor: a marked base, its completion family, and a proof that
-- every admitted base has a contractible completion space. Applications must
-- construct the last argument; it is not obtained merely by naming a family.
module Completion {ℓB ℓF : Level}
  (B : Type ℓB) (F : B → Type ℓF)
  (fill : (b : B) → isContr (F b)) where

  Total : Type (ℓ-max ℓB ℓF)
  Total = Σ[ b ∈ B ] F b

  complete : B → Total
  complete b = b , fst (fill b)

  forget : Total → B
  forget = fst

  forget-complete : (b : B) → forget (complete b) ≡ b
  forget-complete b = refl

  complete-forget : (t : Total) → complete (forget t) ≡ t
  complete-forget (b , c) i = b , snd (fill b) c i

  base-fixed : (t : Total) → cong forget (complete-forget t) ≡ refl
  base-fixed t = refl

  total-iso : Iso Total B
  total-iso = record
    { fun = forget ; inv = complete
    ; rightInv = forget-complete ; leftInv = complete-forget }

  dependent-interpretation-iso : {ℓY : Level} (Y : B → Type ℓY)
    → Iso ((t : Total) → Y (forget t)) ((b : B) → Y b)
  dependent-interpretation-iso Y = record
    { fun = λ g b → g (complete b)
    ; inv = λ f t → f (forget t)
    ; rightInv = λ f → refl
    ; leftInv = λ g → funExt λ { (b , c) →
        cong (λ c' → g (b , c')) (snd (fill b) c) } }

  Extension : {ℓY : Level} (Y : B → Type ℓY)
    (f : (b : B) → Y b) → Type (ℓ-max (ℓ-max ℓB ℓF) ℓY)
  Extension Y f = Σ[ g ∈ ((t : Total) → Y (forget t)) ]
    ((λ b → g (complete b)) ≡ f)

  unique-extension : {ℓY : Level} (Y : B → Type ℓY) (f : (b : B) → Y b)
    → isContr (Extension Y f)
  unique-extension Y f = equiv-proof (snd (isoToEquiv (dependent-interpretation-iso Y))) f

-- Characterization, not an extra axiom: coherent completion is exactly an
-- equivalence of the forgetful projection. This projection is not the earlier
-- possibly nonfaithful realization j:E->K.
module Criterion {ℓB ℓF : Level} (B : Type ℓB) (F : B → Type ℓF) where
  projection : (Σ[ b ∈ B ] F b) → B
  projection = fst

  completion-to-equivalence : ((b : B) → isContr (F b)) → isEquiv projection
  completion-to-equivalence fill = snd (isoToEquiv C.total-iso)
    where module C = Completion B F fill

  equivalence-to-completion : isEquiv projection → (b : B) → isContr (F b)
  equivalence-to-completion e b =
    isOfHLevelRespectEquiv 0 (fiberEquiv F b) (equiv-proof e b)

  completion-criterion : ((b : B) → isContr (F b)) ≃ isEquiv projection
  completion-criterion = propBiimpl→Equiv
    (isPropΠ (λ _ → isPropIsContr)) (isPropIsEquiv projection)
    completion-to-equivalence equivalence-to-completion
