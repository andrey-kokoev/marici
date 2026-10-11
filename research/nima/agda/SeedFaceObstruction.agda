{-# OPTIONS --safe --cubical --guardedness #-}
module SeedFaceObstruction where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Transport using (substComposite)
open import Cubical.Foundations.Univalence using (ua; uaβ)
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (notEquiv; true≢false)
open import Cubical.Data.Empty.Base using (⊥)
open import ActualSeedEndpointTable
open import SeedTetrahedronBridge using (Realization; node; edge; ForwardFace; TriangleABC)

-- A diagnostic family on the ACTUAL free realization, not new physics.
-- Crossing AB flips its Boolean fiber. Every other primitive preserves it.
-- No face relation in Realization forbids this family.
Probe : Realization → Type
Probe (node v) = Bool
Probe (edge AB i) = ua notEquiv i
Probe (edge BC i) = Bool
Probe (edge CA i) = Bool
Probe (edge AD i) = Bool
Probe (edge DB i) = Bool
Probe (edge BA i) = Bool

forward-indirect-reading : subst Probe (edge AD ∙ edge DB) false ≡ false
forward-indirect-reading = substComposite Probe (edge AD) (edge DB) false
  ∙ (cong (subst Probe (edge DB)) (transportRefl false) ∙ transportRefl false)
forward-direct-reading : subst Probe (edge AB) false ≡ true
forward-direct-reading = uaβ notEquiv false

no-forward-face : ForwardFace → ⊥
no-forward-face h = true≢false
  (sym forward-direct-reading ∙ (sym (cong (λ p → subst Probe p false) h)
    ∙ forward-indirect-reading))

abc-route-reading : subst Probe (edge AB ∙ edge BC) false ≡ true
abc-route-reading = substComposite Probe (edge AB) (edge BC) false
  ∙ (cong (subst Probe (edge BC)) (uaβ notEquiv false) ∙ transportRefl true)
ac-route-reading : subst Probe (sym (edge CA)) false ≡ false
ac-route-reading = transportRefl false

no-abc-face : TriangleABC → ⊥
no-abc-face h = true≢false
  (sym abc-route-reading ∙ (cong (λ p → subst Probe p false) h ∙ ac-route-reading))
