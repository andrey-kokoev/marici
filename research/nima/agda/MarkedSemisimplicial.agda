{-# OPTIONS --safe --cubical --guardedness #-}
module MarkedSemisimplicial where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.GroupoidLaws using (assoc)
open import Cubical.Data.Nat.Base using (ℕ; suc)
open import Cubical.Data.Vec.Base using (Vec; []; _∷_; lookup)
open import Cubical.Data.FinData.Base using (Fin; zero; suc)
open import Cubical.Data.Sigma.Base using (_,_; Σ)

module InDimension {ℓ : Level} (A : Type ℓ) where
  VertexTuple : ℕ → Type ℓ
  VertexTuple n = Vec A (suc n)
  Edge : {n : ℕ} (v : VertexTuple n) → Fin (suc n) → Fin (suc n) → Type ℓ
  Edge v i j = lookup i v ≡ lookup j v

  Triangle : (x y z : A) → Type ℓ
  Triangle x y z = Σ (x ≡ y) λ p → Σ (y ≡ z) λ q → Σ (x ≡ z) λ r → p ∙ q ≡ r

  Tetrahedron : (x0 x1 x2 x3 : A) → Type ℓ
  Tetrahedron x0 x1 x2 x3 =
    Σ (x0 ≡ x1) λ e01 → Σ (x1 ≡ x2) λ e12 → Σ (x0 ≡ x2) λ e02 →
    Σ (x2 ≡ x3) λ e23 → Σ (x1 ≡ x3) λ e13 → Σ (x0 ≡ x3) λ e03 →
    Σ (e01 ∙ e12 ≡ e02) λ a → Σ (e12 ∙ e23 ≡ e13) λ b →
    Σ (e01 ∙ e13 ≡ e03) λ c → Σ (e02 ∙ e23 ≡ e03) λ d →
    ((cong (λ p → p ∙ e23) a ∙ d) ≡
     (sym (assoc e01 e12 e23) ∙ (cong (λ p → e01 ∙ p) b ∙ c)))

  Face012 : {x0 x1 x2 x3 : A} → Tetrahedron x0 x1 x2 x3 → Triangle x0 x1 x2
  Face012 (e01 , e12 , e02 , e23 , e13 , e03 , a , b , c , d , coh) = e01 , e12 , e02 , a
  Face123 : {x0 x1 x2 x3 : A} → Tetrahedron x0 x1 x2 x3 → Triangle x1 x2 x3
  Face123 (e01 , e12 , e02 , e23 , e13 , e03 , a , b , c , d , coh) = e12 , e23 , e13 , b
  Face013 : {x0 x1 x2 x3 : A} → Tetrahedron x0 x1 x2 x3 → Triangle x0 x1 x3
  Face013 (e01 , e12 , e02 , e23 , e13 , e03 , a , b , c , d , coh) = e01 , e13 , e03 , c
  Face023 : {x0 x1 x2 x3 : A} → Tetrahedron x0 x1 x2 x3 → Triangle x0 x2 x3
  Face023 (e01 , e12 , e02 , e23 , e13 , e03 , a , b , c , d , coh) = e02 , e23 , e03 , d

  d0 : {x y z : A} → Triangle x y z → y ≡ z
  d0 (_ , q , _ , _) = q
  d1 : {x y z : A} → Triangle x y z → x ≡ z
  d1 (_ , _ , r , _) = r
  d2 : {x y z : A} → Triangle x y z → x ≡ y
  d2 (p , _ , _ , _) = p

  d0₃ : {x0 x1 x2 x3 : A} → Tetrahedron x0 x1 x2 x3 → Triangle x1 x2 x3
  d0₃ = Face123
  d1₃ : {x0 x1 x2 x3 : A} → Tetrahedron x0 x1 x2 x3 → Triangle x0 x2 x3
  d1₃ = Face023
  d2₃ : {x0 x1 x2 x3 : A} → Tetrahedron x0 x1 x2 x3 → Triangle x0 x1 x3
  d2₃ = Face013
  d3₃ : {x0 x1 x2 x3 : A} → Tetrahedron x0 x1 x2 x3 → Triangle x0 x1 x2
  d3₃ = Face012

  face-identity-01 : {x0 x1 x2 x3 : A} (t : Tetrahedron x0 x1 x2 x3)
    → d0 (d1₃ t) ≡ d0 (d0₃ t)
  face-identity-01 t = refl
