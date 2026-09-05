{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module UnauthorizedPromotion where

open import Cubical.Foundations.Prelude
open import ResidualPromotion

-- Deliberate failure: parent re-entry is attempted without an inhabitant of
-- the gate's Authority type.
unauthorized :
  {child : ChildTower} {parent : ParentTower} →
  (gate : PromotionGate child parent) →
  ChildTower.State child →
  ParentTower.State parent
unauthorized gate childState = reenterParent gate childState
