{-# OPTIONS --safe --cubical --guardedness #-}
module TickCayleyRationalNormalization where

open import Cubical.Foundations.Prelude
open import Cubical.Algebra.CommRing.Instances.Int using (ℤCommRing)
open import Cubical.Tactics.CommRingSolver
open import Cubical.Tactics.NatSolver using (solveℕ!)
open import Cubical.Data.Nat as N using (ℕ; suc)
open import Cubical.Data.NatPlusOne using (ℕ₊₁; 1+_; ℕ₊₁→ℕ)
open import Cubical.Data.NatPlusOne.Properties using (_·₊₁_; ·₊₁-comm; ·₊₁-identityˡ)
import Cubical.Data.Int as Z
open import Cubical.Data.Rationals as Q
open import TickCayleyGridIncrement using (gridValue; gridProductInverse; inverseIndex)
open import TickCayleyOuterRotor using (cayleyReal; cayleyImaginary)

integerDenominator : ℕ₊₁ → Z.ℤ
integerDenominator D = Z.pos (ℕ₊₁→ℕ D)

abstract
  square-successor : (d : ℕ) → suc d N.· suc d ≡ suc (d N.· (d N.+ 2))
  square-successor d = solveℕ!

  unit-real-numerator : (d : ℕ) → (Z.pos (suc d N.· suc d)) Z.+ (Z.- (Z.pos 1 Z.· Z.pos 1)) ≡ Z.pos (d N.· (d N.+ 2))
  unit-real-numerator d = cong (λ n → Z.pos n Z.+ (Z.- (Z.pos 1 Z.· Z.pos 1))) (square-successor d)

  unit-imaginary-numerator : (d : ℕ) → (Z.pos 1 Z.+ Z.pos 1) Z.· Z.pos (suc d) ≡ Z.pos (2 N.· suc d)
  unit-imaginary-numerator d = sym (Z.pos·pos 2 (suc d))

  quarter-turn-real : (a b : Q.ℚ) → 0 Q.· a Q.+ (Q.- (1 Q.· b)) ≡ Q.- b
  quarter-turn-real a b = cong₂ Q._+_ (Q.·AnnihilL a) (cong Q.-_ (Q.·IdL b)) ∙ Q.+IdL (Q.- b)

  quarter-turn-imaginary : (a b : Q.ℚ) → 0 Q.· b Q.+ 1 Q.· a ≡ a
  quarter-turn-imaginary a b = cong₂ Q._+_ (Q.·AnnihilL b) (Q.·IdL a) ∙ Q.+IdL a

  negative-integer : (a : Z.ℤ) → Z.negsuc 0 Z.· a ≡ Z.- a
  negative-integer a = solve! ℤCommRing

  fraction-negative : (a : Z.ℤ) (D : ℕ₊₁) → Q.- Q.[ a / D ] ≡ Q.[ Z.- a / D ]
  fraction-negative a D = cong₂ (λ num den → Q.[ num / den ]) (negative-integer a) (·₊₁-identityˡ D)

  cancel-two-fraction : (a : Z.ℤ) (D : ℕ₊₁) →
    Q.[ Z.pos 2 Z.· a / (1+ 1) ·₊₁ D ] ≡ Q.[ a / D ]
  cancel-two-fraction a D = Q.·CancelL {a = a} {b = D} (1+ 1)

  same-denominator-add : (a b : Z.ℤ) (D : ℕ₊₁) → Q.[ a / D ] Q.+ Q.[ b / D ] ≡ Q.[ a Z.+ b / D ]
  same-denominator-add a b D = cong (λ z → Q.[ z / D ·₊₁ D ]) (sym (Z.·DistL+ a b (integerDenominator D))) ∙ Q.·CancelR D

  one-fraction : (D : ℕ₊₁) → 1 ≡ Q.[ integerDenominator D / D ]
  one-fraction D = Q.eq/ _ _ (Z.·Comm (Z.pos 1) (integerDenominator D))

  cancel-fractions : (a : Z.ℤ) (D S : ℕ₊₁) →
    Q.[ a / D ] Q.· Q.[ integerDenominator D / S ] ≡ Q.[ a / S ]
  cancel-fractions a D S = cong (λ den → Q.[ a Z.· integerDenominator D / den ]) (·₊₁-comm D S) ∙ Q.·CancelR D

  square-scale-fractions : (a : Z.ℤ) (D S : ℕ₊₁) →
    Q.[ a / D ] Q.· Q.[ integerDenominator (D ·₊₁ D) / S ] ≡ Q.[ a Z.· integerDenominator D / S ]
  square-scale-fractions a D S = cong₂ (λ num den → Q.[ num / den ])
    (cong (a Z.·_) (Z.pos·pos (ℕ₊₁→ℕ D) (ℕ₊₁→ℕ D)) ∙ Z.·Assoc a (integerDenominator D) (integerDenominator D))
    (·₊₁-comm D S) ∙ Q.·CancelR D

  cayley-real-fraction : (n d : ℕ) → cayleyReal n d ≡
    Q.[ (Z.pos (suc d N.· suc d)) Z.+ (Z.- (Z.pos n Z.· Z.pos n)) / 1+ inverseIndex n n d ]
  cayley-real-fraction n d = cong (Q._· gridProductInverse n n d)
    (cong (Q._+ (Q.- (gridValue n d Q.· gridValue n d))) (one-fraction ((1+ d) ·₊₁ (1+ d)))
      ∙ cong (Q.[ integerDenominator ((1+ d) ·₊₁ (1+ d)) / (1+ d) ·₊₁ (1+ d) ] Q.+_)
        (fraction-negative (Z.pos n Z.· Z.pos n) ((1+ d) ·₊₁ (1+ d)))
      ∙ same-denominator-add (Z.pos (suc d N.· suc d)) (Z.- (Z.pos n Z.· Z.pos n)) ((1+ d) ·₊₁ (1+ d)))
    ∙ cancel-fractions ((Z.pos (suc d N.· suc d)) Z.+ (Z.- (Z.pos n Z.· Z.pos n)))
      ((1+ d) ·₊₁ (1+ d)) (1+ inverseIndex n n d)

  cayley-imaginary-fraction : (n d : ℕ) → cayleyImaginary n d ≡
    Q.[ (Z.pos n Z.+ Z.pos n) Z.· Z.pos (suc d) / 1+ inverseIndex n n d ]
  cayley-imaginary-fraction n d = cong (Q._· gridProductInverse n n d) (same-denominator-add (Z.pos n) (Z.pos n) (1+ d))
    ∙ square-scale-fractions (Z.pos n Z.+ Z.pos n) (1+ d) (1+ inverseIndex n n d)
