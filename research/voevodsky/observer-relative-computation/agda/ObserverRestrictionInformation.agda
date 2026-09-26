{-# OPTIONS --safe --cubical --guardedness #-}
module ObserverRestrictionInformation where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma.Base using (_,_) 
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (true≢false)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Empty.Base using (⊥)
import ObserverDirectionRecords as Info
import ResolutionNetObservation as Obs
import ObserverSupportInvariance as Support

-- Work relative to a specified local observation space. No global
-- assignment to an arbitrary ambient family is assumed to exist.
module Restriction (O X : Type) (F : X → Type) (p : O → X) where
  open Obs.Observation X F
  Source = Observe p
  open Info.Information {X = Source}

  full : Source → Source
  full s = s

  access : {Q : Type} (f : Q → O) → Source → Observe (λ q → p (f q))
  access = restrict

  full-to-part : {Q : Type} (f : Q → O) → Factors full (access f)
  full-to-part f = restrict f , (λ _ → refl)

  further-restriction : {Q R : Type} (f : Q → O) (g : R → Q)
    → Factors (access f) (access (λ r → f (g r)))
  further-restriction f g = restrict g , (λ _ → refl)

module IndependentAccess where
  Source = Bool → Bool
  open Info.Information {X = Source}
  full : Source → Source
  full s = s
  left-only : Source → Unit → Bool
  left-only s _ = s true

  full-to-left : Factors full left-only
  full-to-left = left-only , (λ _ → refl)

  all-true mixed : Source
  all-true _ = true
  mixed true = true
  mixed false = false

  left-collision : left-only all-true ≡ left-only mixed
  left-collision = refl

  strict-loss : Factors left-only full → ⊥
  strict-loss (recover , exact) = true≢false (cong (λ s → s false)
    (sym (exact all-true) ∙ cong recover left-collision ∙ exact mixed))

module RepeatedAccess where
  Source = Unit → Bool
  open Info.Information {X = Source}
  full : Source → Source
  full s = s
  duplicate : Source → Bool → Bool
  duplicate s _ = s tt
  read-back : (Bool → Bool) → Source
  read-back d _ = d true

  full-to-duplicate : Factors full duplicate
  full-to-duplicate = duplicate , (λ _ → refl)

  duplicate-to-full : Factors duplicate full
  duplicate-to-full = read-back , (λ s → funExt (λ { tt → refl }))

  -- Information-equivalence of maps on this source does NOT imply an
  -- equivalence between their entire output types or surjectivity.
  not-every-output-is-attained : (s : Source) → duplicate s ≡ Support.Duplication.disagree → ⊥
  not-every-output-is-attained = Support.Duplication.disagreement-not-restricted

module UnusedOutputs where
  -- Factorization over total output types can demand behavior at
  -- outputs never realized by ANY source. This is a real boundary.
  Source = Unit → ⊥
  open Info.Information {X = Source}

  f : Source → Unit
  f _ = tt
  g : Source → ⊥
  g s = s tt

  vacuous-collision-preservation : (x y : Source) → f x ≡ f y → g x ≡ g y
  vacuous-collision-preservation x y e = absurd (x tt)
    where
    absurd : ⊥ → g x ≡ g y
    absurd ()

  no-total-factor : Factors f g → ⊥
  no-total-factor (post , _) = post tt
