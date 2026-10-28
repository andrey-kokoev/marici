{-# OPTIONS --safe --cubical --guardedness #-}
module SourceFacePairBoundary where

open import Cubical.Foundations.Prelude hiding (Path)
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (true≢false)
open import Cubical.Data.Empty.Base using (⊥)
open import ActualSeedEndpointTable
import SeedSeamPathComparisonBoundary as H
import SeedFirstReturnActions as R

-- A matching object is defined without a filler or invertible source arrows.
Match : {ℓx ℓy ℓc : Level} {X : Type ℓx} {Y : Type ℓy} {C : Type ℓc}
  → (X → C) → (Y → C) → Type (ℓ-max ℓx (ℓ-max ℓy ℓc))
Match {X = X} {Y = Y} r s = Σ X (λ x → Σ Y (λ y → r x ≡ s y))

swap : {ℓx ℓy ℓc : Level} {X : Type ℓx} {Y : Type ℓy} {C : Type ℓc}
  {r : X → C} {s : Y → C} → Match r s → Match s r
swap (x , y , p) = y , x , sym p

swap-involutive : {ℓx ℓy ℓc : Level} {X : Type ℓx} {Y : Type ℓy} {C : Type ℓc}
  {r : X → C} {s : Y → C} (p : Match r s) → swap (swap p) ≡ p
swap-involutive p = refl

-- First source specialization: full outgoing histories and endpoint restriction.
-- This is endpoint matching, not an asserted simplicial two-face filler rule.
FaceRecord : Type
FaceRecord = Σ Vertex (λ t → H.Path A t)

endpoint : FaceRecord → Vertex
endpoint = fst

FacePair : Type
FacePair = Match endpoint endpoint

left right : FacePair → FaceRecord
left p = fst p
right p = fst (snd p)

retains-left : (p : FacePair) → right (swap p) ≡ left p
retains-left p = refl

retains-right : (p : FacePair) → left (swap p) ≡ right p
retains-right p = refl

-- Explicit, deliberately restrictive filler: one history realizing both records.
-- No assertion that all conceivable higher-cell semantics have this fiber.
FullCell = FaceRecord

restricted : FullCell → FacePair
restricted c = c , c , refl

Fill : FacePair → Type
Fill p = Σ FullCell (λ c → restricted c ≡ p)

canonical-fill : (c : FullCell) → Fill (restricted c)
canonical-fill c = c , refl

boundary : FacePair
boundary = (B , H.x0) , (B , H.x1) , refl

observe : FaceRecord → Bool
observe c = H.single (snd c)

boundary-has-no-diagonal-filler : Fill boundary → ⊥
boundary-has-no-diagonal-filler (c , q) =
  true≢false (sym (cong (λ p → observe (left p)) q)
             ∙ cong (λ p → observe (right p)) q)

no-total-diagonal-section : ((p : FacePair) → Fill p) → ⊥
no-total-diagonal-section section = boundary-has-no-diagonal-filler (section boundary)

-- Any proposed identification must lose the existing single-edge observation.
no-observation-preserving-identification :
  (f : H.Path A B → H.Path A B)
  → ((h : H.Path A B) → H.single (f h) ≡ H.single h)
  → f H.x0 ≡ H.x1 → ⊥
no-observation-preserving-identification = H.forward-observed-obstruction

-- Quantifies over actual directed suffixes, not ambient group elements.
obstruction-survives-every-suffix : {t : Vertex} (q : H.Path B t)
  → R.append H.x0 q ≡ R.append H.x1 q → ⊥
obstruction-survives-every-suffix q p = true≢false (cong R.starts-AB p)

-- Strict shared-endpoint slice: exchange commutes with every common suffix.
ParallelPair : Vertex → Type
ParallelPair t = Σ (H.Path A t) (λ _ → H.Path A t)

exchange : {t : Vertex} → ParallelPair t → ParallelPair t
exchange (h , k) = k , h

extend : {s t : Vertex} → H.Path s t → ParallelPair s → ParallelPair t
extend q (h , k) = R.append h q , R.append k q

exchange-natural : {s t : Vertex} (q : H.Path s t) (p : ParallelPair s)
  → exchange (extend q p) ≡ extend q (exchange p)
exchange-natural q p = refl

exchange-return : {t : Vertex} (p : ParallelPair t)
  → exchange (exchange p) ≡ p
exchange-return p = refl
