{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidSignedLiftAudit where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Sigma.Properties using (Σ-contractFst)
open import DGPyramidBoundary
open import DGPyramidFiller

-- A horn completion includes the face AND its prescribed boundary equation.
-- This is conditional on an actual whiskering equivalence, not on faithfulness
-- alone. No semilocal analytical equivalence is postulated by this module.
module SignedHorn {ℓ : Level} {Faces Boundaries : Type ℓ}
  (whiskering : Faces ≃ Boundaries) (boundary : Boundaries) where

  Completion : Type ℓ
  Completion = fiber (equivFun whiskering) boundary

  completionContractible : isContr Completion
  completionContractible = equiv-proof (snd whiskering) boundary

  forcedCompletion : Completion
  forcedCompletion = fst completionContractible

  -- A contractible signed problem need not have an inhabited structured lift.
  -- This reduces the entire structured problem to ONE specified fiber; it
  -- does not assume a point in that fiber.
  structuredReduction : (Lift : Completion → Type ℓ) →
    (Σ Completion Lift) ≃ Lift forcedCompletion
  structuredReduction Lift = Σ-contractFst completionContractible

-- Retain the existing four frame conditions verbatim. The comparison takes
-- an actual DG boundary filler to a signed completion, INCLUDING its equation.
-- It must be constructed before this reduction can be applied analytically.
module FramedComparison {ℓ : Level} (P : DGPyramidBoundary {ℓ})
  (Frame : PyramidFrame P) (SignedCompletion : Type ℓ)
  (compare : BoundaryFiller P Frame → SignedCompletion) where

  RemainingAt : SignedCompletion → Type ℓ
  RemainingAt signed = Σ (BoundaryFiller P Frame) λ u →
    Σ (compare u ≡ signed) λ _ → PreservesFrame Frame (fst u)

  TotalLift : Type ℓ
  TotalLift = Σ SignedCompletion RemainingAt

  -- Forgetting the named signed target and its comparison loses no data up
  -- to equivalence when that target is allowed to vary. All frame witnesses
  -- are retained, not reconstructed from the signed equation.
  totalIso : Iso TotalLift (AdmissibleFiller P Frame)
  Iso.fun totalIso (signed , (K , equation) , comparison , conditions) =
    K , equation , conditions
  Iso.inv totalIso (K , equation , conditions) =
    compare (K , equation) , (K , equation) , refl , conditions
  Iso.rightInv totalIso _ = refl
  Iso.leftInv totalIso (signed , u , comparison , conditions) i =
    comparison i , u , (λ j → comparison (i ∧ j)) , conditions

  totalEquivalence : TotalLift ≃ AdmissibleFiller P Frame
  totalEquivalence = isoToEquiv totalIso

  -- Exact remaining obligation when the signed completion is forced.
  -- This proves an equivalence, not existence of a physical filler.
  remainingEquivalence : (closed : isContr SignedCompletion) →
    AdmissibleFiller P Frame ≃ RemainingAt (fst closed)
  remainingEquivalence closed =
    compEquiv (invEquiv totalEquivalence) (Σ-contractFst closed)

-- This separate comparison is necessary even to transfer a vanishing claim.
-- Closedness of the DG discrepancy is already derived in DGPyramidBoundary;
-- signed vanishing is neither that theorem nor a framed DG filler.
module DiscrepancyComparison {ℓ : Level} (P : DGPyramidBoundary {ℓ})
  (Signed : Type ℓ) (observe : JFone P → Signed)
  (signedDiscrepancy signedZero : Signed)
  (identifiesDiscrepancy : observe (pyramidDiscrepancy P) ≡ signedDiscrepancy)
  (signedCoherent : signedDiscrepancy ≡ signedZero) where

  observedDiscrepancyVanishes : observe (pyramidDiscrepancy P) ≡ signedZero
  observedDiscrepancyVanishes = identifiesDiscrepancy ∙ signedCoherent

-- No positivity, completed-domain, or physical adapter inhabitant is exported.
-- PreservesFrame contains only the existing four predicates: further analytic
-- obligations must be represented explicitly by the chosen physical frame.
