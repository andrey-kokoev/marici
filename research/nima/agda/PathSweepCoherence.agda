{-# OPTIONS --safe --cubical --guardedness #-}
module PathSweepCoherence where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Path using (Square→compPath)
open import Cubical.Foundations.GroupoidLaws using (rUnit)

-- Mapping a dependent path to a fixed type agrees with mapping the canonical
-- transport filler and then the residual endpoint path. The square explicitly
-- fills the comparison; no discreteness or truncation assumption is used.
module _ {ℓ ℓ' : Level} (F : I → Type ℓ) (R : Type ℓ')
  (f : (i : I) → F i → R) {x : F i0} {y : F i1}
  (t : PathP F x y) where

  canonical-sweep : f i0 x ≡ f i1 (transport (λ i → F i) x)
  canonical-sweep i = f i (transport-filler (λ j → F j) x i)
  actual-sweep : f i0 x ≡ f i1 y
  actual-sweep i = f i (t i)

  sweep-square : Square actual-sweep (cong (f i1) (fromPathP t)) canonical-sweep refl
  sweep-square i j = f (i ∨ j)
    (transp (λ k → F (j ∨ (i ∧ k))) (j ∨ ~ i) (t j))

  mapped-pathover-pasting :
    canonical-sweep ∙ cong (f i1) (fromPathP t) ≡ actual-sweep
  mapped-pathover-pasting = Square→compPath sweep-square ∙ sym (rUnit actual-sweep)
