{-# OPTIONS --safe --cubical --guardedness #-}
module RationalComponentArithmetic where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma using (_×_)
import Cubical.Data.Nat as N
import Cubical.Data.Int as Z
import Cubical.Data.NatPlusOne as P
import Cubical.Data.Rationals as R
import Cubical.HITs.SetQuotients as Q
import ComponentArithmetic as C
import SignedComponentArithmetic as S
import FaithfulComponentRing as F
open import Cubical.Algebra.CommRing.Base

-- Positive word denominators: zero is excluded by the constructor.
Denominator = P.ℕ₊₁
word : Denominator → C.Word
word = P.ℕ₊₁→ℕ
den-product : Denominator → Denominator → Denominator
den-product (P.1+ a) (P.1+ b) = P.1+ (C.append a (C.multiply (N.suc a) b))
den-product-word : (d e : Denominator) → word (den-product d e) ≡ C.multiply (word d) (word e)
den-product-word (P.1+ a) (P.1+ b) = refl
multiply-native : (a b : C.Word) → C.multiply a b ≡ a N.· b
multiply-native a N.zero = N.0≡m·0 a
multiply-native a (N.suc b) = S.append-native a (C.multiply a b)
  ∙ cong (a N.+_) (multiply-native a b) ∙ sym (N.·-suc a b)
den-product-native : (d e : Denominator) → den-product d e ≡ d P.·₊₁ e
den-product-native (P.1+ a) (P.1+ b) = P.ℕ₊₁→ℕ-inj (multiply-native (N.suc a) (N.suc b))
den-signed : Denominator → S.Signed
den-signed d = S.fromInt (Z.pos (word d))
den-readout : (d : Denominator) → S.asInt (den-signed d) ≡ R.ℕ₊₁→ℤ d
den-readout d = S.asInt-fromInt (Z.pos (word d))

Representative : Type
Representative = S.Signed × Denominator
Cross : Representative → Representative → Type
Cross (a , d) (b , e) = S.multiply a (den-signed e) ≡ S.multiply b (den-signed d)
Rational : Type
Rational = Representative Q./ Cross
include : Representative → Rational
include = Q.[_]
representative : Representative → R.ℚ
representative (a , d) = R.[ S.asInt a / d ]
cross-law : (a : S.Signed) (d : Denominator) → S.asInt (S.multiply a (den-signed d)) ≡ S.asInt a Z.· R.ℕ₊₁→ℤ d
cross-law a d = S.Multiply.preserves a (den-signed d) ∙ cong (S.asInt a Z.·_) (den-readout d)
cross-native : (p q : Representative) → Cross p q → R._∼_ (S.asInt (fst p) , snd p) (S.asInt (fst q) , snd q)
cross-native (a , d) (b , e) p = sym (cross-law a e) ∙ cong S.asInt p ∙ cross-law b d
asRational : Rational → R.ℚ
asRational = Q.rec R.isSetℚ representative (λ p q r → R.eq/ _ _ (cross-native p q r))
from-representative : Z.ℤ × Denominator → Rational
from-representative (a , d) = Q.[ S.fromInt a , d ]
fromRational : R.ℚ → Rational
fromRational = Q.rec Q.squash/ from-representative
  (λ { (a , d) (b , e) r → Q.eq/ _ _ (S.faithful
    (cross-law (S.fromInt a) e ∙ cong (Z._· R.ℕ₊₁→ℤ e) (S.asInt-fromInt a)
      ∙ r ∙ cong (Z._· R.ℕ₊₁→ℤ d) (sym (S.asInt-fromInt b)) ∙ sym (cross-law (S.fromInt b) d))) })
recover : (x : Rational) → fromRational (asRational x) ≡ x
recover = Q.elimProp (λ _ → Q.squash/ _ _) (λ { (a , d) → cong (λ x → include (x , d)) (S.recover a) })
readout-recover : (x : R.ℚ) → asRational (fromRational x) ≡ x
readout-recover = Q.elimProp (λ _ → R.isSetℚ _ _) (λ { (a , d) → cong (λ x → R.[ x / d ]) (S.asInt-fromInt a) })
faithful : {x y : Rational} → asRational x ≡ asRational y → x ≡ y
faithful {x} {y} p = sym (recover x) ∙ cong fromRational p ∙ recover y

add-representative multiply-representative : Representative → Representative → Representative
add-representative (a , d) (b , e) = S.add (S.multiply a (den-signed e)) (S.multiply b (den-signed d)) , den-product d e
multiply-representative (a , d) (b , e) = S.multiply a b , den-product d e
raw-add : (p q : Representative) → representative (add-representative p q) ≡ representative p R.+ representative q
raw-add (a , d) (b , e) = cong₂ (λ n t → R.[ n / t ])
  (S.Add.preserves (S.multiply a (den-signed e)) (S.multiply b (den-signed d))
    ∙ cong₂ Z._+_ (cross-law a e) (cross-law b d)) (den-product-native d e)
raw-multiply : (p q : Representative) → representative (multiply-representative p q) ≡ representative p R.· representative q
raw-multiply (a , d) (b , e) = cong₂ (λ n t → R.[ n / t ]) (S.Multiply.preserves a b) (den-product-native d e)

module QuotientOperation (raw : Representative → Representative → Representative) (op : R.ℚ → R.ℚ → R.ℚ)
  (law : (p q : Representative) → representative (raw p q) ≡ op (representative p) (representative q)) where
  operation : Rational → Rational → Rational
  operation = Q.rec2 Q.squash/ (λ p q → Q.[ raw p q ])
    (λ p p' q r → faithful (law p q ∙ cong (λ x → op x (representative q)) (cong asRational (Q.eq/ p p' r)) ∙ sym (law p' q)))
    (λ p q q' r → faithful (law p q ∙ cong (op (representative p)) (cong asRational (Q.eq/ q q' r)) ∙ sym (law p q')))
  preserves : (x y : Rational) → asRational (operation x y) ≡ op (asRational x) (asRational y)
  preserves = Q.elimProp2 (λ _ _ → R.isSetℚ _ _) law
module Add = QuotientOperation add-representative R._+_ raw-add
module Multiply = QuotientOperation multiply-representative R._·_ raw-multiply
add multiply : Rational → Rational → Rational
add = Add.operation
multiply = Multiply.operation
zero one : Rational
zero = Q.[ S.zero , P.1+ 0 ]
one = Q.[ S.one , P.1+ 0 ]
fraction : S.Signed → Denominator → Rational
fraction a d = Q.[ a , d ]

negate-representative : Representative → Representative
negate-representative (a , d) = S.negate a , d
raw-negate : (p : Representative) → representative (negate-representative p) ≡ R.- representative p
raw-negate (a , d) = cong₂ (λ x t → R.[ x / t ])
  (S.negate-preserves a ∙ Z.-DistL· (Z.pos 1) (S.asInt a)) (sym (P.·₊₁-identityˡ d))
negate : Rational → Rational
negate = Q.rec Q.squash/ (λ p → include (negate-representative p))
  (λ p q r → faithful (raw-negate p ∙ cong R.-_ (cong asRational (Q.eq/ p q r)) ∙ sym (raw-negate q)))
negate-preserves : (x : Rational) → asRational (negate x) ≡ R.- asRational x
negate-preserves = Q.elimProp (λ _ → R.isSetℚ _ _) raw-negate
readoutRing : CommRing ℓ-zero
readoutRing = makeCommRing R.[ Z.pos 0 / P.1+ 0 ] R.[ Z.pos 1 / P.1+ 0 ]
  R._+_ R._·_ R.-_ R.isSetℚ R.+Assoc R.+IdR R.+InvR R.+Comm R.·Assoc R.·IdR R.·DistL+ R.·Comm
module Ring = F.Transfer Rational Q.squash/ readoutRing asRational faithful zero one add multiply negate
  refl refl Add.preserves Multiply.preserves negate-preserves
rationalRing : CommRing ℓ-zero
rationalRing = Ring.ring

embed-signed : S.Signed → Rational
embed-signed a = fraction a (P.1+ 0)
embed-signed-add : (a b : S.Signed) → embed-signed (S.add a b) ≡ add (embed-signed a) (embed-signed b)
embed-signed-add a b = faithful
  (cong (λ n → R.[ n / P.1+ 0 ]) (S.Add.preserves a b
    ∙ sym (cong₂ Z._+_ (Z.·IdR (S.asInt a)) (Z.·IdR (S.asInt b))))
    ∙ sym (Add.preserves (embed-signed a) (embed-signed b)))
embed-signed-multiply : (a b : S.Signed) → embed-signed (S.multiply a b) ≡ multiply (embed-signed a) (embed-signed b)
embed-signed-multiply a b = faithful
  (cong (λ n → R.[ n / P.1+ 0 ]) (S.Multiply.preserves a b)
    ∙ sym (Multiply.preserves (embed-signed a) (embed-signed b)))

-- Every admitted positive component denominator is explicitly inverted.
positive-inverse-readout : (d : Denominator) →
  R.[ Z.pos (word d) / P.1+ 0 ] R.· R.[ Z.pos 1 / d ] ≡ R.[ Z.pos 1 / P.1+ 0 ]
positive-inverse-readout d = cong₂ (λ n t → R.[ n / t ])
  (Z.·IdR (Z.pos (word d))) (P.·₊₁-identityˡ d)
  ∙ R.eq/ _ _ (Z.·IdR (Z.pos (word d)))
positive-inverse : (d : Denominator) →
  multiply (fraction (den-signed d) (P.1+ 0)) (fraction S.one d) ≡ one
positive-inverse d = faithful (Multiply.preserves (fraction (den-signed d) (P.1+ 0)) (fraction S.one d)
  ∙ cong (λ q → q R.· R.[ Z.pos 1 / d ]) (cong (λ n → R.[ n / P.1+ 0 ]) (den-readout d))
  ∙ positive-inverse-readout d)
