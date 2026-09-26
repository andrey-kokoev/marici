{-# OPTIONS --safe --cubical --guardedness #-}
module RationalRotorNumerators where

open import Cubical.Foundations.Prelude
open import Cubical.Algebra.CommRing.Base
open import Cubical.Tactics.CommRingSolver
import RationalComponentArithmetic as Source

-- The coefficient ring is the existing constructed rational completion.
-- These polynomial identities do NOT select a Clifford multiplication or a
-- topology, and do not assert native admission of any analytic comparison.
module Polynomial (R : CommRing ℓ-zero) where
  open CommRingStr (snd R)
  Scalar = fst R
  re im den : Scalar → Scalar → Scalar
  re m n = n · n + (- (m · m))
  im m n = (1r + 1r) · m · n
  den m n = n · n + m · m

  norm-numerator : (m n : Scalar)
    → re m n · re m n + im m n · im m n ≡ den m n · den m n
  norm-numerator m n = solve! R

  composed-m composed-n : Scalar → Scalar → Scalar → Scalar → Scalar
  composed-m m n r s = m · s + n · r
  composed-n m n r s = n · s + (- (m · r))

  denominator-composes : (m n r s : Scalar)
    → den (composed-m m n r s) (composed-n m n r s)
      ≡ den m n · den r s
  denominator-composes m n r s = solve! R

  real-composes : (m n r s : Scalar)
    → re (composed-m m n r s) (composed-n m n r s)
      ≡ re m n · re r s + (- (im m n · im r s))
  real-composes m n r s = solve! R

  imaginary-composes : (m n r s : Scalar)
    → im (composed-m m n r s) (composed-n m n r s)
      ≡ re m n · im r s + im m n · re r s
  imaginary-composes m n r s = solve! R

module NativeRationalIdentities = Polynomial Source.rationalRing
