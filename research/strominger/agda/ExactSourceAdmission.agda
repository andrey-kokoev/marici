{-# OPTIONS --safe --cubical --guardedness #-}
module ExactSourceAdmission where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import NativeExtensionFamilyAudit using (Vertex; Edge)
open import SourceIndexedExtensionFamilies using (Out)

-- An exact representation realizes every parameterized request, with all
-- realization evidence retained. This is stronger than mere soundness or
-- a Boolean existence test. Its decoder is part of the source contract.
module Representation {ℓ : Level} (I W : Type ℓ) (decode : I → W) where
  post : (T : Type ℓ) → (T → I) → (T → W)
  post T f t = decode (f t)
  Exact : Type (ℓ-suc ℓ)
  Exact = (T : Type ℓ) → isEquiv (post T)

  exact-iso : Exact → Iso I W
  exact-iso exact = iso decode inverse right left
    where
    lifted : (T : Type ℓ) → (T → I) ≃ (T → W)
    lifted T = post T , exact T
    inverse : W → I
    inverse = invEq (lifted W) (λ w → w)
    right : (w : W) → decode (inverse w) ≡ w
    right w = funExt⁻ (secEq (lifted W) (λ w → w)) w
    function-left : (λ i → inverse (decode i)) ≡ (λ i → i)
    function-left = sym (retEq (lifted I) (λ i → inverse (decode i)))
      ∙ cong (invEq (lifted I)) (funExt (λ i → right (decode i)))
      ∙ retEq (lifted I) (λ i → i)
    left : (i : I) → inverse (decode i) ≡ i
    left = funExt⁻ function-left

  equivalence-is-exact : isEquiv decode → Exact
  equivalence-is-exact e T = snd (equivΠCod (λ (_ : T) → decode , e))

-- A candidate attachment interface must expose its actual target and original
-- incidence evidence. No separate arbitrary Admit predicate is inserted here.
module AttachmentContract (v : Vertex) (I : Type)
  (target : I → Vertex) (edge : (i : I) → Edge v (target i)) where
  decode : I → Out v
  decode i = target i , edge i
  module R = Representation I (Out v) decode
  uniquely-represents-attachments : R.Exact → Iso I (Out v)
  uniquely-represents-attachments = R.exact-iso

canonical-exact : (v : Vertex)
  → Representation.Exact (Out v) (Out v) (λ x → x)
canonical-exact v T = snd (idEquiv (T → Out v))
