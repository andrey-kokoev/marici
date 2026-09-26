{-# OPTIONS --safe --cubical --guardedness #-}
module FormalRotorCoefficients where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import Cubical.Algebra.CommRing.Base
import Cubical.Data.NatPlusOne as P
import SignedComponentArithmetic as S
import RationalComponentArithmetic as R

module Q = CommRingStr (snd R.rationalRing)
module Z = CommRingStr (snd S.signedRing)

one-denominator : R.Denominator
one-denominator = P.1+ 0
reciprocal : R.Denominator → R.Rational
reciprocal d = R.fraction S.one d
denominator-scalar : R.Denominator → R.Rational
denominator-scalar d = R.fraction (R.den-signed d) one-denominator

reciprocal-product : (d e : R.Denominator)
  → R.multiply (reciprocal d) (reciprocal e) ≡ reciprocal (R.den-product d e)
reciprocal-product d e = cong (λ x → R.fraction x (R.den-product d e)) (Z.·IdR S.one)

cancel-product-denominator : (d e : R.Denominator)
  → R.multiply (denominator-scalar d) (reciprocal (R.den-product d e)) ≡ reciprocal e
cancel-product-denominator d e =
  cong (R.multiply (denominator-scalar d)) (sym (reciprocal-product d e))
  ∙ Q.·Assoc (denominator-scalar d) (reciprocal d) (reciprocal e)
  ∙ cong (λ x → R.multiply x (reciprocal e)) (R.positive-inverse d)
  ∙ Q.·IdL (reciprocal e)

factorial : ℕ → R.Denominator
factorial zero = one-denominator
factorial (suc n) = R.den-product (P.1+ n) (factorial n)
coefficient : ℕ → R.Rational
coefficient n = reciprocal (factorial n)
initial-coefficient : coefficient zero ≡ R.one
initial-coefficient = refl
coefficient-recurrence : (n : ℕ)
  → R.multiply (denominator-scalar (P.1+ n)) (coefficient (suc n)) ≡ coefficient n
coefficient-recurrence n = cancel-product-denominator (P.1+ n) (factorial n)

cancel-denominator : (d : R.Denominator) (x y : R.Rational)
  → R.multiply (denominator-scalar d) x ≡ R.multiply (denominator-scalar d) y
  → x ≡ y
cancel-denominator d x y p =
  sym (Q.·IdL x)
  ∙ cong (λ v → R.multiply v x) (sym inverse-left)
  ∙ sym (Q.·Assoc (reciprocal d) (denominator-scalar d) x)
  ∙ cong (R.multiply (reciprocal d)) p
  ∙ Q.·Assoc (reciprocal d) (denominator-scalar d) y
  ∙ cong (λ v → R.multiply v y) inverse-left
  ∙ Q.·IdL y
  where
  inverse-left : R.multiply (reciprocal d) (denominator-scalar d) ≡ R.one
  inverse-left = Q.·Comm (reciprocal d) (denominator-scalar d) ∙ R.positive-inverse d

coefficients-unique : (f : ℕ → R.Rational) → f zero ≡ R.one
  → ((n : ℕ) → R.multiply (denominator-scalar (P.1+ n)) (f (suc n)) ≡ f n)
  → (n : ℕ) → f n ≡ coefficient n
coefficients-unique f f0 step zero = f0
coefficients-unique f f0 step (suc n) =
  cancel-denominator (P.1+ n) (f (suc n)) (coefficient (suc n))
    (step n ∙ coefficients-unique f f0 step n ∙ sym (coefficient-recurrence n))
