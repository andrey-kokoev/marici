{-# OPTIONS --safe --cubical --guardedness #-}
module BoundaryPfaffianRankReset where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma using (_×_; _,_)

-- A reusable residual is not a bare state: both boundary variances are kept.
record Bicharged {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    State Incoming Outgoing : Type ℓ
    incoming : State → Incoming
    outgoing : State → Outgoing

open Bicharged public

-- One contextual Pyramid turn.  No temporal interpretation is assigned.
record RankResetSystem {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    Primitive Defect Certificate Residual NextPrimitive : Type ℓ

    expose : Primitive → Defect
    reconcile : Defect → Certificate × Residual
    retype : Residual → NextPrimitive

    -- Direct minimalization is compared with defect reconciliation.
    minimize : Primitive → Certificate × NextPrimitive
    rankResetSquare : (p : Primitive) →
      minimize p ≡
      ( fst (reconcile (expose p))
      , retype (snd (reconcile (expose p))) )

    -- Residual and next primitive use the same declared port types.
    Incoming Outgoing : Type ℓ
    residualIncoming : Residual → Incoming
    residualOutgoing : Residual → Outgoing
    nextIncoming : NextPrimitive → Incoming
    nextOutgoing : NextPrimitive → Outgoing

    incomingRetyped : (r : Residual) →
      nextIncoming (retype r) ≡ residualIncoming r
    outgoingRetyped : (r : Residual) →
      nextOutgoing (retype r) ≡ residualOutgoing r

open RankResetSystem public

-- Validity is contextual: direct and reconciled presentations must have the
-- same readout in every admitted context.
record ContextualValidity {ℓ : Level}
  (R : RankResetSystem {ℓ}) : Type (ℓ-suc ℓ) where
  field
    Context Observation : Type ℓ
    observePrimitive : Context → Primitive R → Observation
    observeMinimal : Context → Certificate R × NextPrimitive R → Observation

    behaviorPreserved : (c : Context) (p : Primitive R) →
      observePrimitive c p ≡ observeMinimal c (minimize R p)

open ContextualValidity public

-- The square makes the direct normal form replaceable by reconciliation and
-- retyping under every admitted observation.
reconciledBehavior : {ℓ : Level}
  (R : RankResetSystem {ℓ})
  (V : ContextualValidity R)
  (c : Context V) (p : Primitive R) →
  observePrimitive V c p ≡
  observeMinimal V c
    ( fst (reconcile R (expose R p))
    , retype R (snd (reconcile R (expose R p))) )
reconciledBehavior R V c p =
  behaviorPreserved V c p ∙ cong (observeMinimal V c) (rankResetSquare R p)

-- Retyping preserves both variances as one paired path.
boundaryRetyping : {ℓ : Level}
  (R : RankResetSystem {ℓ}) (r : Residual R) →
  ( nextIncoming R (retype R r)
  , nextOutgoing R (retype R r) )
  ≡
  ( residualIncoming R r
  , residualOutgoing R r )
boundaryRetyping R r =
  cong₂ _,_ (incomingRetyped R r) (outgoingRetyped R r)
