{-# OPTIONS --safe --cubical --guardedness #-}
module BoundaryPfaffianResidualRankResetInstance where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma using (_×_; _,_)
open import Cubical.Algebra.CommRing
open import BoundaryPfaffianRankReset
open import BoundaryPfaffianResidualFold

module Instance {ℓ} (CR : CommRing ℓ) where
  module RF = ResidualFold CR
  open RF
  open CommRingStr (snd CR)

  residualRankReset : RankResetSystem {ℓ}
  residualRankReset = record
    { Primitive = OddMetric
    ; Defect = OddMetric
    ; Certificate = ResidualSummary
    ; Residual = ResidualSummary
    ; NextPrimitive = ResidualSummary
    ; expose = λ X → X
    ; reconcile = λ X → summarize X , summarize X
    ; retype = λ X → X
    ; minimize = λ X → summarize X , summarize X
    ; rankResetSquare = λ X → refl
    ; Incoming = Carrier
    ; Outgoing = Carrier
    ; residualIncoming = inn
    ; residualOutgoing = out
    ; nextIncoming = inn
    ; nextOutgoing = out
    ; incomingRetyped = λ X → refl
    ; outgoingRetyped = λ X → refl
    }

  polarizedCertificateReversal : (X : OddMetric) →
    fst (reconcile residualRankReset (reverseMetric X)) ≡
    reverseSummary (fst (reconcile residualRankReset X))
  polarizedCertificateReversal = summarizeReversal

  polarizedResidualReversal : (X : OddMetric) →
    snd (reconcile residualRankReset (reverseMetric X)) ≡
    reverseSummary (snd (reconcile residualRankReset X))
  polarizedResidualReversal = summarizeReversal

  -- A future sewing context is a separating gap and a right residual block.
  SewingContext = Carrier × ResidualSummary

  sewingValidity : ContextualValidity residualRankReset
  sewingValidity = record
    { Context = SewingContext
    ; Observation = Carrier
    ; observePrimitive = λ where (gap , Y) X → sew (summarize X) gap Y
    ; observeMinimal = λ where (gap , Y) (_ , X) → sew X gap Y
    ; behaviorPreserved = λ c X → refl
    }

  -- Instantiation of the abstract commuting square for every sewing context.
  residualBehaviorPreserved : (c : SewingContext) (X : OddMetric) →
    observePrimitive sewingValidity c X ≡
    observeMinimal sewingValidity c
      ( fst (reconcile residualRankReset (expose residualRankReset X))
      , retype residualRankReset
          (snd (reconcile residualRankReset (expose residualRankReset X))) )
  residualBehaviorPreserved =
    reconciledBehavior residualRankReset sewingValidity
