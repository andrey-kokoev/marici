{-# OPTIONS --safe --cubical --guardedness #-}
module FilledSourceReturnClassification where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Equiv.Properties using (congEquiv)
open import Cubical.Foundations.Isomorphism using (iso; isoToEquiv)
open import Cubical.Foundations.Path using (compPathlEquiv; compPathrEquiv)
open import Cubical.Foundations.GroupoidLaws using (rCancel)
open import Cubical.Foundations.Univalence using (ua; uaβ)
open import Cubical.Data.Bool using (Bool; false; true; notEquiv; false≢true)
open import Cubical.Data.Empty using (⊥)
import ActualSeedEndpointTable as Seed
import SeedTetrahedronBridge as Graph
import SeedNativePromotionBindingGate as Gate
import RetainedTetrahedralPackage as Retained
import SourceGraphFreeRealization as Free

-- This is the ACTUAL filled-package interface, not new face assumptions
-- imposed on the unchanged free graph. Its vertices are ordered A,D,B,C.
module At {ℓ : Level} (X : Type ℓ) (full : Retained.Cells.Full X) where
  module C = Retained.Cells X
  vertices = fst full
  surface = fst (snd full)
  module V = C.Vertices vertices
  module O = C.Over vertices
  edges = O.Surface.edges surface
  module E = C.T.Edges edges

  points : Seed.Vertex → X
  points Seed.A = V.v0
  points Seed.B = V.v2
  points Seed.C = V.v3
  points Seed.D = V.v1

  -- The actual tetrahedral e13 is D->C, NOT the primitive BA.
  diagonal-DBC : E.e12 ∙ E.e23 ≡ E.e13
  diagonal-DBC = O.Surface.face123 surface

  Return : Type ℓ
  Return = V.v2 ≡ V.v0
  BasedLoop : Type ℓ
  BasedLoop = V.v0 ≡ V.v0
  Paths : Type ℓ
  Paths = (e : Seed.Occurrence) → points (Seed.source e) ≡ points (Seed.target e)
  paths : Return → Paths
  paths back Seed.AB = E.e02
  paths back Seed.BC = E.e23
  paths back Seed.CA = sym E.e03
  paths back Seed.AD = E.e01
  paths back Seed.DB = E.e12
  paths back Seed.BA = back

  diagram : Return → Free.Universal.Diagram X
  diagram back = points , paths back
  interpret : Return → Graph.Realization → X
  interpret back = Free.Universal.extend X (diagram back)
  BA-recovered : (back : Return) → cong (interpret back) (Graph.edge Seed.BA) ≡ back
  BA-recovered back = refl
  paths-injective : {left right : Return} → paths left ≡ paths right → left ≡ right
  paths-injective same = cong (λ p → p Seed.BA) same

  -- Classify ALL assignments at these fixed vertices with explicit matching
  -- witnesses for the five supplied edges, not only the displayed family.
  record Extension : Type ℓ where
    field
      assigned : Paths
      keepAB : assigned Seed.AB ≡ E.e02
      keepBC : assigned Seed.BC ≡ E.e23
      keepCA : assigned Seed.CA ≡ sym E.e03
      keepAD : assigned Seed.AD ≡ E.e01
      keepDB : assigned Seed.DB ≡ E.e12
  open Extension
  make : Return → Extension
  assigned (make back) = paths back
  keepAB (make back) = refl
  keepBC (make back) = refl
  keepCA (make back) = refl
  keepAD (make back) = refl
  keepDB (make back) = refl
  extract : Extension → Return
  extract ext = assigned ext Seed.BA
  recover-extension : (ext : Extension) → make (extract ext) ≡ ext
  assigned (recover-extension ext i) Seed.AB = keepAB ext (~ i)
  assigned (recover-extension ext i) Seed.BC = keepBC ext (~ i)
  assigned (recover-extension ext i) Seed.CA = keepCA ext (~ i)
  assigned (recover-extension ext i) Seed.AD = keepAD ext (~ i)
  assigned (recover-extension ext i) Seed.DB = keepDB ext (~ i)
  assigned (recover-extension ext i) Seed.BA = assigned ext Seed.BA
  keepAB (recover-extension ext i) j = keepAB ext (~ i ∨ j)
  keepBC (recover-extension ext i) j = keepBC ext (~ i ∨ j)
  keepCA (recover-extension ext i) j = keepCA ext (~ i ∨ j)
  keepAD (recover-extension ext i) j = keepAD ext (~ i ∨ j)
  keepDB (recover-extension ext i) j = keepDB ext (~ i ∨ j)
  extension-return : Extension ≃ Return
  extension-return = isoToEquiv (iso extract make (λ _ → refl) recover-extension)

  -- Full higher witnesses remain in full. They do not mention back.
  returnLoop : Return → BasedLoop
  returnLoop back = E.e02 ∙ back
  return-classification : Return ≃ BasedLoop
  return-classification = compPathlEquiv E.e02
  extension-classification : Extension ≃ BasedLoop
  extension-classification = compEquiv extension-return return-classification

  abc-null : (E.e02 ∙ E.e23) ∙ sym E.e03 ≡ refl
  abc-null = cong (_∙ sym E.e03) (O.Surface.face023 surface) ∙ rCancel E.e03
  forward-null : (E.e01 ∙ E.e12) ∙ sym E.e02 ≡ refl
  forward-null = cong (_∙ sym E.e02) (O.Surface.face012 surface) ∙ rCancel E.e02
  adb-is-return : (back : Return) → (E.e01 ∙ E.e12) ∙ back ≡ returnLoop back
  adb-is-return back = cong (_∙ back) (O.Surface.face012 surface)

  -- Choosing BA as inverse AB is possible, but is an EXTRA interpretation
  -- equation for the separately retained occurrence, not an original row law.
  reverse-choice : Return
  reverse-choice = sym E.e02
  reverse-kills-return : returnLoop reverse-choice ≡ refl
  reverse-kills-return = rCancel E.e02
  reverse-iff-null : (back : Return)
    → (back ≡ reverse-choice) ≃ (returnLoop back ≡ refl)
  reverse-iff-null back = compEquiv (congEquiv (compPathlEquiv E.e02))
    (compPathrEquiv (rCancel E.e02))
  reverse-iff-adb-null : (back : Return)
    → (back ≡ reverse-choice) ≃ ((E.e01 ∙ E.e12) ∙ back ≡ refl)
  reverse-iff-adb-null back = compEquiv (reverse-iff-null back)
    (compPathlEquiv (adb-is-return back))
  -- With the EXTRA requirement to fill the original directed ADB cycle,
  -- the return together with its full null-homotopy is contractible.
  adb-null-choices : isContr (Σ[ back ∈ Return ] ((E.e01 ∙ E.e12) ∙ back ≡ refl))
  adb-null-choices = equiv-proof (snd (compPathlEquiv (E.e01 ∙ E.e12))) refl

-- Reuse an EXISTING inhabited filled package over the universe of types.
-- Keep that very same complete package (faces and filler included) fixed.
module ExistingFilledCounterexample where
  module Prior = Retained.LossyDiagonal
  full : Retained.Cells.Full (Type ℓ-zero)
  full = Prior.v , Prior.ordinary
  module F = At (Type ℓ-zero) full
  identity-return flip-return : F.Return
  identity-return = refl
  flip-return = ua notEquiv
  distinct-returns : identity-return ≡ flip-return → ⊥
  distinct-returns same = false≢true
    (sym (transportRefl false) ∙ cong (λ p → transport p false) same ∙ uaβ notEquiv false)
  distinct-path-assignments : F.paths identity-return ≡ F.paths flip-return → ⊥
  distinct-path-assignments same = distinct-returns (F.paths-injective same)
  return-not-prop : isProp F.Return → ⊥
  return-not-prop unique = distinct-returns (unique identity-return flip-return)

-- Also instantiate the same adapter on the actual pointed typed fixture
-- consumed by the prior feedback example; do NOT assert its return space
-- has the same ambiguity as the universe-valued counterexample above.
module ExistingTypedFixture where
  module F = At (Retained.TypedValue ℓ-zero) Retained.TypedFixture.result
  interpretation = F.interpret F.reverse-choice
  return-is-null = F.reverse-kills-return

-- Reuse the stronger old binding obstruction, including propositional
-- identification of vertices. No new global absence-of-feedback inference.
no-unchanged-free-source-full = Gate.no-source-full
