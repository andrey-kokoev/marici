{-# OPTIONS --safe --cubical --guardedness #-}
module ContinuationSidePolicies where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.Transport using (substEquiv)
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (true≢false)
open import Cubical.Relation.Nullary.Base using (¬_)
open import NativeExtensionFamilyAudit using (Vertex; A; B; C; D; AB; BC; BA; sigmaEquiv)
open import SourceIndexedExtensionFamilies using (Out; vertex-is-set)
open import InternalSourceComparisons
import WholePackageSigmaPi as Whole
open Whole.Universe ℓ-zero

-- Classification of requests over the EXISTING comparison carrier. These
-- definitions do not modify Body, its target reader, or its native rules.
module Policies (m : Mode) {v : Vertex} (a : Body v) (b : Body (act m v))
  (e : El (expression (package a)) ≃ El (expression (package b)))
  (p : equivFun e (value (package a)) ≡ value (package b))
  (h : (x : El (expression (package a))) → act m (reader a x) ≡ reader b (equivFun e x)) where

  carrier = El (expression (package (compare m a b e p h)))
  source target : carrier → Vertex
  source z = reader a (fst z)
  target z = reader (compare m a b e p h) z
  ports : (z : carrier) → act m (source z) ≡ target z
  ports = comparison-reading m a b e p h
  requests : (z : carrier) → Out (source z) ≃ Out (target z)
  requests z = compEquiv (edgeEquiv m (source z)) (substEquiv Out (ports z))
  route : (z : carrier) → Out (source z) → Out (target z)
  route z = equivFun (requests z)
  Independent Synchronized : carrier → Type
  Independent z = Out (source z) × Out (target z)
  Synchronized z = Σ[ s ∈ Out (source z) ] Σ[ t ∈ Out (target z) ] route z s ≡ t
  forget : (z : carrier) → Synchronized z → Independent z
  forget z (s , t , w) = s , t
  sourceIso : (z : carrier) → Iso (Synchronized z) (Out (source z))
  Iso.fun (sourceIso z) = fst
  Iso.inv (sourceIso z) s = s , route z s , refl
  Iso.rightInv (sourceIso z) s = refl
  Iso.leftInv (sourceIso z) (s , t , w) i = s , w i , (λ j → w (i ∧ j))
  synchronized-source : (z : carrier) → Synchronized z ≃ Out (source z)
  synchronized-source z = isoToEquiv (sourceIso z)
  synchronized-target : (z : carrier) → Synchronized z ≃ Out (target z)
  synchronized-target z = compEquiv (synchronized-source z) (requests z)

-- Concrete original source fixture, not a new selected topology or task.
module Fixture = Policies exchange (seedBody A) (seedBody B) sigmaEquiv refl (λ x → refl)
z₀ : Fixture.carrier
z₀ = value (package (nonidentity A))
ab : Out A
ab = B , AB
ba bc : Out B
ba = A , BA
bc = C , BC
route-ab : Fixture.route z₀ ab ≡ ba
route-ab = cong (λ q → subst Out q ba)
  (vertex-is-set B B (Fixture.ports z₀) refl) ∙ substRefl {B = Out} ba

tag : Vertex → Bool
tag A = true
tag B = false
tag C = false
tag D = false
raw-source-not-target : ¬ (Fixture.source z₀ ≡ Fixture.target z₀)
raw-source-not-target p = true≢false (cong tag p)
off-diagonal-not-synchronized : ¬ (Fixture.route z₀ ab ≡ bc)
off-diagonal-not-synchronized p = true≢false (cong (λ e → tag (fst e)) (sym route-ab ∙ p))
independent-pair : Fixture.Independent z₀
independent-pair = ab , bc
no-synchronized-preimage : ¬ (Σ[ s ∈ Fixture.Synchronized z₀ ] Fixture.forget z₀ s ≡ independent-pair)
no-synchronized-preimage ((s , t , w) , p) = off-diagonal-not-synchronized
  (sym (cong (Fixture.route z₀) (cong fst p)) ∙ w ∙ cong snd p)
