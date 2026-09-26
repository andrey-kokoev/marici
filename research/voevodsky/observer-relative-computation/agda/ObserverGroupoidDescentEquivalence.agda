{-# OPTIONS --safe --cubical --guardedness #-}
module ObserverGroupoidDescentEquivalence where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.Function using (3-Constant)
open import Cubical.Data.Sigma.Base using (Σ; _,_; fst; snd)
open import Cubical.Data.Sigma.Properties using (Σ-cong-equiv-fst; Σ-cong-equiv-snd; fiberProjEquiv)
open import Cubical.HITs.PropositionalTruncation.Base using (∥_∥₁; ∣_∣₁)
import Cubical.HITs.PropositionalTruncation.Properties as Trunc
open import ObserverAdmissibleImages
import ObserverGroupoidImageDescent as Previous

-- Pin the point map in the library's full groupoid truncation theorem.
-- The pinning equality is retained as part of the data, not discarded.
module Pinned (A B : Type) (Bgroupoid : isGroupoid B) (k : A → B) where
  Extension = Σ (∥ A ∥₁ → B) (λ h → (λ a → h ∣ a ∣₁) ≡ k)

  equivalence : Extension ≃ 3-Constant k
  equivalence = compEquiv
    (Σ-cong-equiv-fst (Trunc.trunc→Gpd≃ Bgroupoid))
    (invEquiv (fiberProjEquiv (A → B) 3-Constant k))

module Descent {X Y Z : Type} (f : X → Y) (g : X → Z) (Zgroupoid : isGroupoid Z) where
  module C = Previous.Criterion f g
  -- The target image's groupoid proof is independent of coherence.
  open import Cubical.Foundations.HLevels using (isGroupoidΣ; isSet→isGroupoid)
  open import Cubical.HITs.PropositionalTruncation.Base using (squash₁)
  image-groupoid : isGroupoid (Image g)
  image-groupoid = isGroupoidΣ Zgroupoid (λ _ → isSet→isGroupoid (isProp→isSet squash₁))

  Raw = (y : Y) → Pinned.Extension (Fibre f y) (Image g) image-groupoid (C.origin-output y)

  raw-coherence : Raw ≃ C.CoherentFibres
  raw-coherence = equivΠCod (λ y → Pinned.equivalence (Fibre f y) (Image g) image-groupoid (C.origin-output y))

  OriginLaw : (Image f → Image g) → Type
  OriginLaw post = (y : Y) (u : Fibre f y) → post (y , ∣ u ∣₁) ≡ C.origin-output y u

  Packed = Σ (Image f → Image g) OriginLaw

  pack : Raw → Packed
  pack d = (λ i → fst (d (fst i)) (snd i)) , (λ y u i → snd (d y) i u)

  unpack : Packed → Raw
  unpack (post , law) y = (λ t → post (y , t)) , funExt (law y)

  raw-packed : Raw ≃ Packed
  raw-packed = isoToEquiv (iso pack unpack (λ _ → refl) (λ _ → refl))

  -- A law on every origin (x,e) is equivalent to its values at (x,refl).
  -- Path induction retains the equality data in both inverse laws.
  module Arrival (post : Image f → Image g) where
    D : (x : X) (y : Y) → f x ≡ y → Type
    D x y e = post (y , ∣ x , e ∣₁) ≡ arrive g x
    Short = (x : X) → post (arrive f x) ≡ arrive g x

    restrict : OriginLaw post → Short
    restrict law x = law (f x) (x , refl)

    extend : Short → OriginLaw post
    extend law y (x , e) = J (D x) (law x) e

    short-roundtrip : (law : Short) → restrict (extend law) ≡ law
    short-roundtrip law = funExt (λ x → JRefl (D x) (law x))

    origin-roundtrip : (law : OriginLaw post) → extend (restrict law) ≡ law
    origin-roundtrip law = funExt (λ y → funExt (λ { (x , e) →
      J (λ y e → J (D x) (law (f x) (x , refl)) e ≡ law y (x , e))
        (JRefl (D x) (law (f x) (x , refl))) e }))

    equivalence : OriginLaw post ≃ Short
    equivalence = isoToEquiv (iso restrict extend short-roundtrip origin-roundtrip)

  raw-factor : Raw ≃ ImageFactors f g
  raw-factor = compEquiv raw-packed (Σ-cong-equiv-snd Arrival.equivalence)

  -- Full witness-bearing type equivalence. It is stronger than merely
  -- producing a factor and a coherence record in opposite directions.
  equivalence : ImageFactors f g ≃ C.CoherentFibres
  equivalence = compEquiv (invEquiv raw-factor) raw-coherence

  encode : ImageFactors f g → C.CoherentFibres
  encode = equivFun equivalence

  decode : C.CoherentFibres → ImageFactors f g
  decode = invEq equivalence

  factor-roundtrip : (factor : ImageFactors f g) → decode (encode factor) ≡ factor
  factor-roundtrip = retEq equivalence

  coherence-roundtrip : (coherence : C.CoherentFibres) → encode (decode coherence) ≡ coherence
  coherence-roundtrip = secEq equivalence

  -- Connect the original computational groupoid constructor to the
  -- certified inverse, not just to the same endpoint type.
  raw-implementation : C.CoherentFibres → Raw
  raw-implementation coherence y =
    Trunc.rec→Gpd image-groupoid (C.origin-output y) (coherence y) , refl

  raw-implementation-correct : (coherence : C.CoherentFibres)
    → equivFun raw-coherence (raw-implementation coherence) ≡ coherence
  raw-implementation-correct coherence = funExt (λ y → substRefl {B = 3-Constant} (coherence y))

  original : C.CoherentFibres → ImageFactors f g
  original coherence = C.Sufficient.factor Zgroupoid coherence

  original-is-packed : (coherence : C.CoherentFibres)
    → equivFun raw-factor (raw-implementation coherence) ≡ original coherence
  original-is-packed coherence = refl

  encode-original : (coherence : C.CoherentFibres) → encode (original coherence) ≡ coherence
  encode-original coherence =
    cong (equivFun raw-coherence) (retEq raw-factor (raw-implementation coherence))
    ∙ raw-implementation-correct coherence

  decode-is-original : (coherence : C.CoherentFibres) → decode coherence ≡ original coherence
  decode-is-original coherence = sym (cong decode (encode-original coherence))
    ∙ factor-roundtrip (original coherence)
