{-# OPTIONS --safe --cubical --guardedness #-}
module IteratedRegularImmersionPurity where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)

-- Ordered determinant bookkeeping for iterated regular immersions. Normal
-- labels are retained, so permutation signs cannot be hidden by identifying
-- determinant frames definitionally.
record OrderedNormalDeterminant {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    Normal Unit Sign : Type ℓ
    plus minus : Sign
    signNegates : plus ≡ minus → ⊥
    multiplySign : Sign → Sign → Sign
    signSquare : multiplySign minus minus ≡ plus

    Line DualLine : Type ℓ
    wedge₁ : Normal → Line
    wedge₂ : Normal → Normal → Line
    wedge₃ : Normal → Normal → Normal → Line
    dual₁ : Normal → DualLine
    dual₂ : Normal → Normal → DualLine
    dual₃ : Normal → Normal → Normal → DualLine
    signLine : Sign → Line → Line
    signDual : Sign → DualLine → DualLine

    swapWedge₂ : (s t : Normal) → wedge₂ t s ≡ signLine minus (wedge₂ s t)
    swapWedge₃₁₂ : (r s t : Normal) →
      wedge₃ s r t ≡ signLine minus (wedge₃ r s t)
    swapWedge₃₂₃ : (r s t : Normal) →
      wedge₃ r t s ≡ signLine minus (wedge₃ r s t)
    swapDual₂ : (s t : Normal) → dual₂ t s ≡ signDual minus (dual₂ s t)
    swapDual₃₁₂ : (r s t : Normal) →
      dual₃ s r t ≡ signDual minus (dual₃ r s t)
    swapDual₃₂₃ : (r s t : Normal) →
      dual₃ r t s ≡ signDual minus (dual₃ r s t)

    multiplyUnit : Unit → Unit → Unit
    oneUnit : Unit
    inverseUnit : Unit → Unit
    inverseLeft : (a : Unit) → multiplyUnit (inverseUnit a) a ≡ oneUnit
    inverseProduct : (a b : Unit) →
      inverseUnit (multiplyUnit a b) ≡
      multiplyUnit (inverseUnit b) (inverseUnit a)

    rescaleNormal : Unit → Normal → Normal
    rescaleLine : Unit → Line → Line
    rescaleDual : Unit → DualLine → DualLine
    frameChange₂ : (a b : Unit) (s t : Normal) →
      wedge₂ (rescaleNormal a s) (rescaleNormal b t) ≡
      rescaleLine (multiplyUnit a b) (wedge₂ s t)
    dualFrameChange₂ : (a b : Unit) (s t : Normal) →
      dual₂ (rescaleNormal a s) (rescaleNormal b t) ≡
      rescaleDual (inverseUnit (multiplyUnit a b)) (dual₂ s t)
    dualFrameChange₃ : (a b c : Unit) (r s t : Normal) →
      dual₃ (rescaleNormal a r) (rescaleNormal b s) (rescaleNormal c t) ≡
      rescaleDual
        (inverseUnit (multiplyUnit (multiplyUnit a b) c))
        (dual₃ r s t)

-- Direct and iterated purity are compared in the same ordered determinant and
-- shift frame. This prevents an unrecorded permutation or unit determinant
-- from entering when codimension-one Cartier maps are composed.
record IteratedRegularPurityCertificate {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    determinant : OrderedNormalDeterminant {ℓ}

  open OrderedNormalDeterminant determinant

  field
    Object : Type ℓ
    restrict₁ : Normal → Object → Object
    cartierPurity₁ : Normal → Object → Object
    directPurity₂ : Normal → Normal → Object → Object
    directPurity₃ : Normal → Normal → Normal → Object → Object
    attachDual₁ : DualLine → Object → Object
    attachDual₂ : DualLine → Object → Object
    attachDual₃ : DualLine → Object → Object
    shift₁ shift₂ shift₃ : Object → Object

    iteratedPurity₂ : Normal → Normal → Object → Object
    iteratedPurity₃ : Normal → Normal → Normal → Object → Object

    iterated₂Definition : (s t : Normal) (M : Object) →
      iteratedPurity₂ s t M ≡
      cartierPurity₁ t (cartierPurity₁ s M)
    iterated₃Definition : (r s t : Normal) (M : Object) →
      iteratedPurity₃ r s t M ≡
      cartierPurity₁ t (cartierPurity₁ s (cartierPurity₁ r M))

    direct₂Frame : (s t : Normal) (M : Object) →
      directPurity₂ s t M ≡ attachDual₂ (dual₂ s t) (shift₂ M)
    direct₃Frame : (r s t : Normal) (M : Object) →
      directPurity₃ r s t M ≡ attachDual₃ (dual₃ r s t) (shift₃ M)

    iteratedEqualsDirect₂ : (s t : Normal) (M : Object) →
      iteratedPurity₂ s t M ≡ directPurity₂ s t M
    iteratedEqualsDirect₃ : (r s t : Normal) (M : Object) →
      iteratedPurity₃ r s t M ≡ directPurity₃ r s t M

    permutationAction₂ : Sign → Object → Object
    swapPurity₂ : (s t : Normal) (M : Object) →
      directPurity₂ t s M ≡ permutationAction₂ minus (directPurity₂ s t M)
    permutationAction3 : Sign → Object → Object
    swapPurity3First : (r s t : Normal) (M : Object) →
      directPurity₃ s r t M ≡ permutationAction3 minus (directPurity₃ r s t M)
    swapPurity3Last : (r s t : Normal) (M : Object) →
      directPurity₃ r t s M ≡ permutationAction3 minus (directPurity₃ r s t M)

    changeFrame₂ : Unit → Unit → Normal → Normal → Object → Object
    frameChangePurity₂ : (a b : Unit) (s t : Normal) (M : Object) →
      changeFrame₂ a b s t M ≡
      attachDual₂
        (rescaleDual (inverseUnit (multiplyUnit a b)) (dual₂ s t))
        (shift₂ M)

    changeFrame₃ : Unit → Unit → Unit → Normal → Normal → Normal → Object → Object
    frameChangePurity₃ : (a b c : Unit) (r s t : Normal) (M : Object) →
      changeFrame₃ a b c r s t M ≡
      attachDual₃
        (rescaleDual
          (inverseUnit (multiplyUnit (multiplyUnit a b) c))
          (dual₃ r s t))
        (shift₃ M)

open IteratedRegularPurityCertificate public
