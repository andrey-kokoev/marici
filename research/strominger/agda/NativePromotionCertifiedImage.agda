{-# OPTIONS --safe --cubical --guardedness #-}
module NativePromotionCertifiedImage where

open import Cubical.Foundations.Prelude hiding (lift)
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Bool.Base using (false)
import NativePacketPromotionBinding as P

module F = P.F
module B = P.B
module A = P.A
module G = P.G

-- Untruncated provenance: source, actual target and its image certificate.
Generated : Type (ℓ-suc (ℓ-suc (ℓ-suc ℓ-zero)))
Generated = Σ[ c ∈ B.Compared ] Σ[ y ∈ A.Compared ] (F.run c ≡ y)

pack : B.Compared → Generated
pack c = c , F.run c , refl
origin : Generated → B.Compared
origin = fst
view : Generated → A.Compared
view x = fst (snd x)
certificate : (x : Generated) → F.run (origin x) ≡ view x
certificate x = snd (snd x)

-- This is an equality of full dependent records, not truncation of witnesses.
eta : (x : Generated) → pack (origin x) ≡ x
eta (c , y , p) i = c , p i , (λ j → p (i ∧ j))

image-iso : Iso B.Compared Generated
Iso.fun image-iso = pack
Iso.inv image-iso = origin
Iso.rightInv image-iso = eta
Iso.leftInv image-iso c = refl

-- A source continuation has a canonical lift to the certified image.
-- This specifies a continuation, rather than claiming that an independently
-- supplied ambient target operation must agree with it.
lift : (B.Compared → B.Compared) → Generated → Generated
lift f x = pack (f (origin x))

lift-unit : (x : Generated) → lift (λ c → c) x ≡ x
lift-unit = eta

lift-compose : (f g : B.Compared → B.Compared) (x : Generated)
  → lift g (lift f x) ≡ lift (λ c → g (f c)) x
lift-compose f g x = refl

-- Retain the actual previous generated record alongside each execution.
Execution : (B.Compared → B.Compared) → Type (ℓ-suc (ℓ-suc (ℓ-suc ℓ-zero)))
Execution f = Σ[ x ∈ Generated ] Σ[ z ∈ Generated ] (lift f x ≡ z)
execute : (f : B.Compared → B.Compared) → Generated → Execution f
execute f x = x , lift f x , refl
execution-input : (f : B.Compared → B.Compared) (x : Generated)
  → fst (execute f x) ≡ x
execution-input f x = refl

-- An independently supplied ambient target operation needs its own square.
AmbientCompatible : (B.Compared → B.Compared)
  → (A.Compared → A.Compared) → Type (ℓ-suc (ℓ-suc (ℓ-suc ℓ-zero)))
AmbientCompatible f h = (c : B.Compared) → F.run (f c) ≡ h (F.run c)

ambient-lift : (f : B.Compared → B.Compared)
  (h : A.Compared → A.Compared) → AmbientCompatible f h
  → Generated → Generated
ambient-lift f h square x =
  f (origin x) , h (view x) , square (origin x) ∙ cong h (certificate x)

ambient-view : (f : B.Compared → B.Compared)
  (h : A.Compared → A.Compared) (square : AmbientCompatible f h) (x : Generated)
  → view (ambient-lift f h square x) ≡ h (view x)
ambient-view f h square x = refl

compatible-compose : (f g : B.Compared → B.Compared)
  (h k : A.Compared → A.Compared)
  → AmbientCompatible f h → AmbientCompatible g k
  → AmbientCompatible (λ c → g (f c)) (λ y → k (h y))
compatible-compose f g h k first second c =
  second (f c) ∙ cong k (first c)

-- Decoding then re-promoting a source continuation supplies such a square.
induced : (B.Compared → B.Compared) → A.Compared → A.Compared
induced f y = F.run (f (F.decode y))
induced-compatible : (f : B.Compared → B.Compared) → AmbientCompatible f (induced f)
induced-compatible f c = sym (cong (λ a → F.run (f a)) (F.decode-run c))

-- The actual next-level exchange is not any compatible ambient lift of a
-- total source continuation: it sends the known generated input outside.
exchange-not-compatible : (f : B.Compared → B.Compared)
  → AmbientCompatible f G.exchange → ⊥
exchange-not-compatible f square =
  P.outside-image (f (P.source false)) (square (P.source false))
