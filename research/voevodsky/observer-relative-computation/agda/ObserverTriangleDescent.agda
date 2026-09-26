{-# OPTIONS --safe --cubical --guardedness #-}
module ObserverTriangleDescent where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.Transport using (substInPathsL)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Empty.Base using (⊥)
import ObserverTriangleCoherence as Previous

-- A square with its left boundary collapsed is a filled triangle.
-- This filling is SPECIFIED structure, not added to arbitrary cycles.
data Joint : Type where
  a b c : Joint
  ab : a ≡ b
  bc : b ≡ c
  ac : a ≡ c
  face : PathP (λ i → a ≡ bc i) ab ac

module Descent {ℓ : Level} (F : Joint → Type ℓ) where
  record LocalData : Type ℓ where
    constructor local-data
    field
      at-a : F a
      at-b : F b
      at-c : F c
      along-ab : PathP (λ i → F (ab i)) at-a at-b
      along-bc : PathP (λ i → F (bc i)) at-b at-c
      along-ac : PathP (λ i → F (ac i)) at-a at-c
      across-face : PathP
        (λ i → PathP (λ j → F (face i j)) at-a (along-bc i))
        along-ab along-ac
  open LocalData

  Observation = (z : Joint) → F z

  glue : LocalData → Observation
  glue d a = at-a d
  glue d b = at-b d
  glue d c = at-c d
  glue d (ab i) = along-ab d i
  glue d (bc i) = along-bc d i
  glue d (ac i) = along-ac d i
  glue d (face i j) = across-face d i j

  restrict : Observation → LocalData
  restrict s = local-data (s a) (s b) (s c)
    (λ i → s (ab i)) (λ i → s (bc i)) (λ i → s (ac i))
    (λ i j → s (face i j))

  -- The actual two-dimensional witness is recovered, not truncated.
  local-roundtrip : (d : LocalData) → restrict (glue d) ≡ d
  local-roundtrip d = refl

  global-roundtrip : (s : Observation) → glue (restrict s) ≡ s
  global-roundtrip s k a = s a
  global-roundtrip s k b = s b
  global-roundtrip s k c = s c
  global-roundtrip s k (ab i) = s (ab i)
  global-roundtrip s k (bc i) = s (bc i)
  global-roundtrip s k (ac i) = s (ac i)
  global-roundtrip s k (face i j) = s (face i j)

  descent-equiv : LocalData ≃ Observation
  descent-equiv = isoToEquiv (iso glue restrict global-roundtrip local-roundtrip)

-- Connect the square presentation to the previous p∙q=r base cell.
-- These are checked conversions; no definitional roundtrip is claimed.
module BaseCell {ℓ : Level} {X : Type ℓ} {x y z : X}
  (p : x ≡ y) (q : y ≡ z) (r : x ≡ z) where
  SquareCell = PathP (λ i → x ≡ q i) p r

  from-composite : p ∙ q ≡ r → SquareCell
  from-composite cell = toPathP (substInPathsL q p ∙ cell)

  to-composite : SquareCell → p ∙ q ≡ r
  to-composite square = sym (substInPathsL q p) ∙ fromPathP square

  probe : p ∙ q ≡ r → Joint → X
  probe cell a = x
  probe cell b = y
  probe cell c = z
  probe cell (ab i) = p i
  probe cell (bc i) = q i
  probe cell (ac i) = r i
  probe cell (face i j) = from-composite cell i j

  -- Given a base cell, dependent observations of any ambient family
  -- satisfy the proved finite descent equivalence on this probe.
  module Over (cell : p ∙ q ≡ r) (F : X → Type ℓ) where
    open Descent (λ t → F (probe cell t)) public

module Regression where
  module Constant = Descent (λ _ → Unit)
  local : Constant.LocalData
  local = Constant.local-data tt tt tt (λ _ → tt) (λ _ → tt) (λ _ → tt) (λ _ _ → tt)

  retained : Constant.restrict (Constant.glue local) ≡ local
  retained = refl

  module O = Previous.Obstruction
  module Bad = BaseCell O.p O.q O.r
  -- The earlier obstructed triangle cannot acquire a square filling
  -- merely by changing its presentation.
  no-square-filling : Bad.SquareCell → ⊥
  no-square-filling square = O.no-cell (Bad.to-composite square)
