{-# OPTIONS --safe --cubical --guardedness #-}
module ObserverAdmissibleImages where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Sigma.Base using (Σ; _,_; fst; snd)
open import Cubical.Data.Sigma.Properties using (Σ≡Prop; Σ≡PropEquiv)
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (true≢false)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Empty.Properties using (isProp⊥)
open import Cubical.HITs.PropositionalTruncation.Base using (∥_∥₁; ∣_∣₁; squash₁)
import Cubical.HITs.PropositionalTruncation.Properties as Trunc
import ObserverDirectionRecords as Prior

Fibre : {X Y : Type} → (X → Y) → Y → Type
Fibre {X} f y = Σ X (λ x → f x ≡ y)

-- Only membership is truncated. Y itself and its paths remain intact.
Image : {X Y : Type} → (X → Y) → Type
Image {Y = Y} f = Σ Y (λ y → ∥ Fibre f y ∥₁)

arrive : {X Y : Type} (f : X → Y) → X → Image f
arrive f x = f x , ∣ x , refl ∣₁

ImageFactors : {X Y Z : Type} → (X → Y) → (X → Z) → Type
ImageFactors f g = Prior.Information.Factors (arrive f) (arrive g)

forget-origin : {X Y : Type} (f : X → Y) → Prior.Records.Recorded f → Image f
forget-origin f (y , origin) = y , ∣ origin ∣₁

-- Admissibility contributes no extra identity choices. In particular,
-- retaining an image is NOT truncating the output's higher paths.
output-paths : {X Y : Type} {f : X → Y} {u v : Image f}
  → (fst u ≡ fst v) ≃ (u ≡ v)
output-paths = Σ≡PropEquiv (λ _ → squash₁)

postprocess : {X Y Z : Type} (f : X → Y) (g : Y → Z)
  → Image f → Image (λ x → g (f x))
postprocess f g (y , possible) = g y , Trunc.map (λ { (x , e) → x , cong g e }) possible

postprocess-arrival : {X Y Z : Type} (f : X → Y) (g : Y → Z) (x : X)
  → postprocess f g (arrive f x) ≡ arrive (λ x → g (f x)) x
postprocess-arrival f g x = refl

module StrictForgetting where
  erase : Bool → Unit
  erase _ = tt
  module R = Prior.Records erase

  records-distinct : R.retain true ≡ R.retain false → ⊥
  records-distinct e = true≢false (cong R.recover e)

  images-equal : arrive erase true ≡ arrive erase false
  images-equal = Σ≡Prop (λ _ → squash₁) refl

  cannot-recover : (decode : Image erase → Bool)
    → ((b : Bool) → decode (arrive erase b) ≡ b) → ⊥
  cannot-recover decode exact = true≢false
    (sym (exact true) ∙ cong decode images-equal ∙ exact false)

  no-image-restoration : ImageFactors erase (λ (b : Bool) → b) → ⊥
  no-image-restoration (post , exact) = cannot-recover
    (λ i → fst (post i)) (λ b → cong fst (exact b))

  -- Distinction is lost at forgetting the origin, not silently recovered
  -- by the admissibility proof.
  forgotten-records-agree : forget-origin erase (R.retain true) ≡ forget-origin erase (R.retain false)
  forgotten-records-agree = images-equal

module NoSource where
  f : ⊥ → Unit
  f ()
  g : ⊥ → ⊥
  g ()

  no-ghost-output : Image f → ⊥
  no-ghost-output (_ , possible) = Trunc.rec isProp⊥ fst possible

  -- A postprocessor on admissible images exists without fabricating
  -- a total Unit→Empty function at an unreachable output.
  image-factor : Image f → Image g
  image-factor i = absurd (no-ghost-output i)
    where
    absurd : ⊥ → Image g
    absurd ()

  commutes : (x : ⊥) → image-factor (arrive f x) ≡ arrive g x
  commutes ()

  no-total-postprocessor : (Unit → ⊥) → ⊥
  no-total-postprocessor post = post tt
