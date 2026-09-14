{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidHermitianWorkConfinement where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)

-- Algebraic interface of the source-current identity.  It deliberately does
-- not postulate an order: all analytic positivity is concentrated in the
-- cancellation field positiveBulkCancels.
record HermitianWorkProblem {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    Scalar : Type ℓ
    zero : Scalar
    _+_ _*_ : Scalar → Scalar → Scalar
    -_ : Scalar → Scalar
    addZeroRight : (x : Scalar) → x + zero ≡ x
    negZero : - zero ≡ zero

    transverse Bulk Work : Scalar
    greenIdentity : _+_ (_*_ transverse Bulk) Work ≡ zero
    workSewing : Work ≡ zero
    positiveBulkCancels : transverse * Bulk ≡ zero → transverse ≡ zero

open HermitianWorkProblem public

-- Once the source-derived endpoint sewing kills Work, the Hermitian Green
-- identity and positive bulk force the transverse coordinate to vanish.
hermitianConfinement : {ℓ : Level} →
  (P : HermitianWorkProblem {ℓ}) → transverse P ≡ zero P
hermitianConfinement P = positiveBulkCancels P productZero
  where
  productZero : _*_ P (transverse P) (Bulk P) ≡ zero P
  productZero =
    sym (addZeroRight P (_*_ P (transverse P) (Bulk P))) ∙
    cong (λ w → _+_ P (_*_ P (transverse P) (Bulk P)) w)
      (sym (workSewing P)) ∙
    greenIdentity P

-- This keeps the Mellin normalization separate from confinement.  It is the
-- source authority identifying the transverse drift with Re(s)-1/2.
record CriticalLineNormalization {ℓ : Level}
  (P : HermitianWorkProblem {ℓ}) : Type (ℓ-suc ℓ) where
  field
    Parameter : Type ℓ
    parameter : Parameter
    OnCriticalLine : Parameter → Type ℓ
    transverseZeroImpliesCritical :
      transverse P ≡ zero P → OnCriticalLine parameter

open CriticalLineNormalization public

criticalLineFromWorkSewing : {ℓ : Level} →
  (P : HermitianWorkProblem {ℓ}) →
  (N : CriticalLineNormalization P) → OnCriticalLine N (parameter N)
criticalLineFromWorkSewing P N =
  transverseZeroImpliesCritical N (hermitianConfinement P)
