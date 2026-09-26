{-# OPTIONS --safe --cubical --guardedness #-}
module ObserverEndpointAction where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.GroupoidLaws using (assoc; lUnit; lCancel; rCancel; cong-∙)
open import Cubical.Data.Sigma.Base using (fst; snd)
open import ObserverAdmissibleImages
import ObserverCoherentImageAction as Native
import ObserverSetImageDescent as Earlier

module Paths {ℓ : Level} {A : Type ℓ} where
  conjugate : {x x' y y' : A} → x ≡ x' → y ≡ y' → x ≡ y → x' ≡ y'
  conjugate a b p = sym a ∙ p ∙ b

  unit : {x x' : A} (a : x ≡ x') → conjugate a a refl ≡ refl
  unit a = cong (sym a ∙_) (sym (lUnit a)) ∙ lCancel a

  cancel-middle : {y y' z : A} (b : y ≡ y') (t : y ≡ z)
    → b ∙ sym b ∙ t ≡ t
  cancel-middle b t = assoc b (sym b) t ∙ cong (_∙ t) (rCancel b) ∙ sym (lUnit t)

  compose : {x x' y y' z z' : A}
    (a : x ≡ x') (b : y ≡ y') (c : z ≡ z') (p : x ≡ y) (q : y ≡ z)
    → conjugate a b p ∙ conjugate b c q ≡ conjugate a c (p ∙ q)
  compose a b c p q =
    sym (assoc (sym a) (p ∙ b) (sym b ∙ q ∙ c))
    ∙ cong (sym a ∙_) (sym (assoc p b (sym b ∙ q ∙ c)))
    ∙ cong (λ t → sym a ∙ p ∙ t) (cancel-middle b (q ∙ c))
    ∙ cong (sym a ∙_) (assoc p q c)

module Endpoint {X Y Z : Type} (f : X → Y) (g : X → Z)
  (factor : ImageFactors f g) where
  module N = Native.FactorAction f g factor
  module P = Native.ImagePaths f
  module E = Earlier.Criterion f g
  open Paths {A = Z}

  act : {x y : X} → f x ≡ f y → g x ≡ g y
  act {x} {y} e = conjugate (N.output-comparison x) (N.output-comparison y) (N.act {x} {y} e)

  act-unit : (x : X) → act {x} {x} refl ≡ refl
  act-unit x = cong (conjugate (N.output-comparison x) (N.output-comparison x)) (N.act-unit x)
    ∙ unit (N.output-comparison x)

  act-compose : {x y z : X} (p : f x ≡ f y) (q : f y ≡ f z)
    → act {x} {z} (p ∙ q) ≡ act {x} {y} p ∙ act {y} {z} q
  act-compose {x} {y} {z} p q =
    cong (conjugate (N.output-comparison x) (N.output-comparison z)) (N.act-compose {x} {y} {z} p q)
    ∙ sym (compose (N.output-comparison x) (N.output-comparison y) (N.output-comparison z)
      (N.act {x} {y} p) (N.act {y} {z} q))

  -- Link to the original collision map, not merely a new similar map.
  earlier-agrees : (x y : X) (e : f x ≡ f y) → E.necessary factor x y e ≡ act {x} {y} e
  earlier-agrees x y e =
    cong-∙ fst (sym (snd factor x)) (cong (fst factor) path ∙ snd factor y)
    ∙ cong (sym (N.output-comparison x) ∙_)
      (cong-∙ fst (cong (fst factor) path) (snd factor y))
    where
    path : arrive f x ≡ arrive f y
    path = P.lift {u = arrive f x} {v = arrive f y} e

  earlier-unit : (x : X) → E.necessary factor x x refl ≡ refl
  earlier-unit x = earlier-agrees x x refl ∙ act-unit x

  earlier-compose : (x y z : X) (p : f x ≡ f y) (q : f y ≡ f z)
    → E.necessary factor x z (p ∙ q) ≡ E.necessary factor x y p ∙ E.necessary factor y z q
  earlier-compose x y z p q = earlier-agrees x z (p ∙ q)
    ∙ act-compose {x} {y} {z} p q
    ∙ cong₂ _∙_ (sym (earlier-agrees x y p)) (sym (earlier-agrees y z q))
