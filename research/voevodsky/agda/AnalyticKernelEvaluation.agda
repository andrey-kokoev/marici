{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module AnalyticKernelEvaluation where

open import Cubical.Foundations.Prelude
open import Cubical.Algebra.AbGroup
open import Cubical.Algebra.Group.Morphisms
open import SymbolicKernelCoefficients
open import KernelEvaluation

private variable ℓ : Level

record AnalyticOperations (ℓ : Level) : Type (ℓ-suc ℓ) where
  field
    ValueGroup : AbGroup ℓ
    multiply : ValueGroup .fst → ValueGroup .fst → ValueGroup .fst
    exponential : ValueGroup .fst → ValueGroup .fst
    cosine : ValueGroup .fst → ValueGroup .fst
    half : ValueGroup .fst → ValueGroup .fst
open AnalyticOperations public

record KernelParameters (ops : AnalyticOperations ℓ) : Type ℓ where
  field
    t z a b epsilon delta tau : ValueGroup ops .fst
open KernelParameters public

module AnalyticModel (ops : AnalyticOperations ℓ) where
  open AbGroupStr (ValueGroup ops .snd)
  module S = SymbolicKernel (KernelParameters ops)

  square : ValueGroup ops .fst → ValueGroup ops .fst
  square x = multiply ops x x

  positive-term : KernelParameters ops → ValueGroup ops .fst
  positive-term p =
    multiply ops
      (exponential ops (- multiply ops (t p) (square (a p))))
      (cosine ops (multiply ops (a p) (z p)))

  H : KernelParameters ops → ValueGroup ops .fst
  H p =
    multiply ops
      (exponential ops (- multiply ops (t p) (square (b p))))
      (cosine ops (multiply ops (b p) (z p)))

  negative-term : KernelParameters ops → ValueGroup ops .fst
  negative-term p = - multiply ops (epsilon p) (H p)

  tail-term : KernelParameters ops → ValueGroup ops .fst
  tail-term p = multiply ops (tau p) (H p)

  atom-value : S.KernelAtom → ValueGroup ops .fst
  atom-value (S.positive-frequency p) = positive-term p
  atom-value (S.negative-frequency p) = negative-term p
  atom-value (S.tail-discrepancy p) = tail-term p
  atom-value (S.normalization-residue p) = delta p
  atom-value (S.deformation-residue p) = epsilon p

  module E = Evaluate (ValueGroup ops) atom-value

  analytic-evaluation : AbGroupHom S.KernelCoefficientGroup (ValueGroup ops)
  analytic-evaluation = E.evaluation-homomorphism

  tail-evaluates-to-tau-H :
    (p : KernelParameters ops) → E.evaluate (S.tail p) ≡ multiply ops (tau p) (H p)
  tail-evaluates-to-tau-H p = refl

  kernel-value : KernelParameters ops → ValueGroup ops .fst
  kernel-value p = positive-term p + negative-term p
