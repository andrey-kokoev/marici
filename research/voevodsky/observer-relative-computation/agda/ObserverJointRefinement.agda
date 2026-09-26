{-# OPTIONS --safe --cubical --guardedness #-}
module ObserverJointRefinement where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.Univalence using (ua; uaβ)
open import Cubical.Foundations.Transport using (substComposite)
open import Cubical.Data.Sigma.Base using (Σ; _,_; fst; snd)
open import Cubical.Data.Sigma.Properties using (Σ≡Prop)
open import Cubical.Data.Bool.Base using (Bool; true; false; not)
open import Cubical.Data.Bool.Properties using (true≢false)
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.HITs.PropositionalTruncation.Base using (∥_∥₁; ∣_∣₁; squash₁)
import ObserverComparisonCompression as P
import ObserverInternalComparison as C
import IndexIdentityCoherenceRegression as Cover

act3 : P.Word → P.Three → P.Three
act3 P.stay x = x
act3 P.turn x = P.cycle x
act3 (P.then u v) x = act3 v (act3 u x)

correct3 : (w : P.Word) (x : P.Three) → subst P.Fibre3 (P.path w) x ≡ act3 w x
correct3 P.stay x = substRefl {B = P.Fibre3} {x = C.base} x
correct3 P.turn x = uaβ P.cycle-equiv x
correct3 (P.then u v) x = substComposite P.Fibre3 (P.path u) (P.path v) x
  ∙ cong (subst P.Fibre3 (P.path v)) (correct3 u x) ∙ correct3 v (act3 u x)

Six = Σ Bool (λ _ → P.Three)
joint : P.Word → Six
joint w = P.parity w , act3 w P.zero3

power : ℕ → P.Word
power zero = P.stay
power (suc n) = P.then (power n) P.turn

representative : Six → P.Word
representative (false , P.zero3) = power 0
representative (false , P.one3) = power 4
representative (false , P.two3) = power 2
representative (true , P.zero3) = power 3
representative (true , P.one3) = power 1
representative (true , P.two3) = power 5

realizes : (x : Six) → joint (representative x) ≡ x
realizes (false , P.zero3) = refl
realizes (false , P.one3) = refl
realizes (false , P.two3) = refl
realizes (true , P.zero3) = refl
realizes (true , P.one3) = refl
realizes (true , P.two3) = refl

Image = Σ Six (λ x → ∥ Σ P.Word (λ w → joint w ≡ x) ∥₁)
image-equiv-six : Image ≃ Six
image-equiv-six = isoToEquiv (iso fst
  (λ x → x , ∣ representative x , realizes x ∣₁)
  (λ _ → refl) (λ _ → Σ≡Prop (λ _ → squash₁) refl))

-- Joint equality is exactly the intersection of the two observations.
joint-equality : (u v : P.Word) → (joint u ≡ joint v) ≃
  Σ (P.parity u ≡ P.parity v) (λ _ → act3 u P.zero3 ≡ act3 v P.zero3)
joint-equality u v = isoToEquiv (iso (λ p → cong fst p , cong snd p)
  (λ { (p , q) i → p i , q i }) (λ _ → refl) (λ _ → refl))

-- Neither individual observation determines the other.
no-three-from-binary : (f : Bool → P.Three)
  → ((w : P.Word) → f (P.parity w) ≡ act3 w P.zero3) → ⊥
no-three-from-binary f exact = true≢false
  (cong P.is-zero (sym (exact (power 0)) ∙ exact (power 2)))

no-binary-from-three : (f : P.Three → Bool)
  → ((w : P.Word) → f (act3 w P.zero3) ≡ P.parity w) → ⊥
no-binary-from-three f exact = true≢false (sym (exact (power 3)) ∙ exact (power 0))

-- Four-state cover: six turns remain visible even though both the
-- binary and ternary observers return to their original readings.
Four = Σ Bool (λ _ → Bool)
rotate unrotate : Four → Four
rotate (a , b) = not b , a
unrotate (a , b) = b , not a

rotate-unrotate : (x : Four) → rotate (unrotate x) ≡ x
rotate-unrotate (true , b) = refl
rotate-unrotate (false , b) = refl
unrotate-rotate : (x : Four) → unrotate (rotate x) ≡ x
unrotate-rotate (a , true) = refl
unrotate-rotate (a , false) = refl

rotate-equiv : Four ≃ Four
rotate-equiv = isoToEquiv (iso rotate unrotate rotate-unrotate unrotate-rotate)

cover4 : Cover.Circle → Type
cover4 Cover.base = Four
cover4 (Cover.loop i) = ua rotate-equiv i
Fibre4 : C.Reply → Type
Fibre4 x = cover4 (snd x)

act4 : P.Word → Four → Four
act4 P.stay x = x
act4 P.turn x = rotate x
act4 (P.then u v) x = act4 v (act4 u x)

correct4 : (w : P.Word) (x : Four) → subst Fibre4 (P.path w) x ≡ act4 w x
correct4 P.stay x = substRefl {B = Fibre4} {x = C.base} x
correct4 P.turn x = uaβ rotate-equiv x
correct4 (P.then u v) x = substComposite Fibre4 (P.path u) (P.path v) x
  ∙ cong (subst Fibre4 (P.path v)) (correct4 u x) ∙ correct4 v (act4 u x)

six-invisible : joint (power 6) ≡ joint (power 0)
six-invisible = refl

six-path-distinct : P.path (power 6) ≡ P.path (power 0) → ⊥
six-path-distinct e = true≢false (cong fst
  (sym (correct4 (power 6) (false , false))
    ∙ cong (λ p → subst Fibre4 p (false , false)) e
    ∙ correct4 (power 0) (false , false)))

no-joint-path-recovery : (recover : Six → C.base ≡ C.base)
  → ((w : P.Word) → recover (joint w) ≡ P.path w) → ⊥
no-joint-path-recovery recover exact = six-path-distinct
  (sym (exact (power 6)) ∙ cong recover six-invisible ∙ exact (power 0))
