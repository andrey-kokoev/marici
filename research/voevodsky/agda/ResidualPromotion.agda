{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module ResidualPromotion where

open import Cubical.Foundations.Prelude

-- Residual feedback remains in a child tower. No constructor below maps a
-- child state to a parent state without a separately supplied authority type.
record ChildTower : Type₁ where
  field
    State : Type
    residualStep : State → State

record ParentTower : Type₁ where
  field
    State : Type

record PromotionGate (child : ChildTower) (parent : ParentTower) : Type₁ where
  field
    Authority : Type
    promote : Authority → ChildTower.State child → ParentTower.State parent
open PromotionGate public

-- The caller must provide both the gate and an inhabitant of its opaque
-- authority type. This module provides no authority constructor.
reenterParent :
  {child : ChildTower} {parent : ParentTower} →
  (gate : PromotionGate child parent) →
  Authority gate →
  ChildTower.State child →
  ParentTower.State parent
reenterParent gate authority childState = promote gate authority childState
