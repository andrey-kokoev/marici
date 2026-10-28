{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyFieldInterpretationExamples where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Bool.Base using (Bool; false; true; not)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import RamseyNativeFieldInterpretation
flip : Iso Bool Bool
Iso.fun flip = not
Iso.inv flip = not
Iso.rightInv flip false = refl
Iso.rightInv flip true = refl
Iso.leftInv flip false = refl
Iso.leftInv flip true = refl
frames : (f : Bool) → Bool ≃ Bool
frames false = idEquiv Bool
frames true = isoToEquiv flip
module S = Interpretation Bool Bool Bool Bool (λ _ → Unit) (λ f _ → f) (λ a → a) (λ _ → Bool) frames
changed-field : S.transfer false true false ≡ true
changed-field = refl
native : S.P.R.Resolve (S.P.comparison false tt false true)
native = S.P.comparison-proof false tt false true
