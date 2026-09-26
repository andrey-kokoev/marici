{-# OPTIONS --safe --cubical --guardedness #-}
module ObserverCoherentImageAction where

open import Cubical.Foundations.Prelude hiding (lift)
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.GroupoidLaws using (cong-∙)
open import Cubical.Data.Sigma.Base using (_,_; fst; snd)
open import Cubical.Data.Sigma.Properties using (isEmbeddingFstΣProp)
open import Cubical.HITs.PropositionalTruncation.Base using (squash₁)
open import ObserverAdmissibleImages

-- Lifting output paths to admissible outputs is itself coherent.
module ImagePaths {X Y : Type} (f : X → Y) where
  lower-equiv : {u v : Image f} → (u ≡ v) ≃ (fst u ≡ fst v)
  lower-equiv = cong fst , isEmbeddingFstΣProp (λ _ → squash₁)

  lift : {u v : Image f} → fst u ≡ fst v → u ≡ v
  lift = invEq lower-equiv

  reflect : {u v : Image f} (p q : u ≡ v) → cong fst p ≡ cong fst q → p ≡ q
  reflect p q e = sym (retEq lower-equiv p)
    ∙ cong (invEq lower-equiv) e ∙ retEq lower-equiv q

  lift-unit : {u : Image f} → lift {u = u} {v = u} refl ≡ refl
  lift-unit {u} = reflect (lift {u = u} {v = u} refl) refl (secEq (lower-equiv {u} {u}) refl)

  lift-compose : {u v w : Image f} (p : fst u ≡ fst v) (q : fst v ≡ fst w)
    → lift {u = u} {v = w} (p ∙ q) ≡ lift {u = u} {v = v} p ∙ lift {u = v} {v = w} q
  lift-compose {u} {v} {w} p q = reflect (lift {u} {w} (p ∙ q)) (lp ∙ lq)
    (secEq (lower-equiv {u} {w}) (p ∙ q)
      ∙ sym (cong-∙ fst lp lq
        ∙ cong₂ _∙_ (secEq (lower-equiv {u} {v}) p) (secEq (lower-equiv {v} {w}) q)))
    where
    lp : u ≡ v
    lp = lift {u} {v} p
    lq : v ≡ w
    lq = lift {v} {w} q

module FactorAction {X Y Z : Type} (f : X → Y) (g : X → Z)
  (factor : ImageFactors f g) where
  open ImagePaths f
  post = fst factor
  exact = snd factor

  -- These are the factor's actual representatives. The named outputs
  -- g(x) are related by retained paths, not silently identified.
  output : X → Z
  output x = fst (post (arrive f x))

  output-comparison : (x : X) → output x ≡ g x
  output-comparison x = cong fst (exact x)

  act : {x y : X} → f x ≡ f y → output x ≡ output y
  act {x} {y} e = cong (λ i → fst (post i)) (lift {u = arrive f x} {v = arrive f y} e)

  act-unit : (x : X) → act {x} {x} refl ≡ refl
  act-unit x = cong (cong (λ i → fst (post i))) lift-unit

  act-compose : {x y z : X} (p : f x ≡ f y) (q : f y ≡ f z)
    → act {x} {z} (p ∙ q) ≡ act {x} {y} p ∙ act {y} {z} q
  act-compose {x} {y} {z} p q =
    cong (cong (λ i → fst (post i)))
      (lift-compose {u = arrive f x} {v = arrive f y} {w = arrive f z} p q)
    ∙ cong-∙ (λ i → fst (post i))
      (lift {u = arrive f x} {v = arrive f y} p)
      (lift {u = arrive f y} {v = arrive f z} q)

  -- Specified base triangles induce triangles of observed comparisons.
  act-triangle : {x y z : X} (p : f x ≡ f y) (q : f y ≡ f z)
    (r : f x ≡ f z) → p ∙ q ≡ r
    → act {x} {y} p ∙ act {y} {z} q ≡ act {x} {z} r
  act-triangle {x} {y} {z} p q r cell =
    sym (act-compose {x} {y} {z} p q) ∙ cong (act {x} {z}) cell
