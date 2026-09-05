{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module KernelEvaluation where

open import Cubical.Foundations.Prelude
open import Cubical.HITs.FreeAbGroup
open import Cubical.Algebra.AbGroup
open import Cubical.Algebra.Group.Morphisms
open import Cubical.Algebra.Group.MorphismProperties
open import SymbolicKernelCoefficients

private variable ℓ ℓ' : Level

module Evaluate
  {Parameter : Type ℓ}
  (ValueGroup : AbGroup ℓ')
  (evaluate-atom : SymbolicKernel.KernelAtom Parameter → ValueGroup .fst)
  where

  open AbGroupStr (snd ValueGroup)
  module S = SymbolicKernel Parameter

  evaluate : S.KernelCoefficientGroup .fst → ValueGroup .fst
  evaluate = Rec.f is-set evaluate-atom 0g _+_ -_ +Assoc +Comm +IdR +InvR

  evaluate-generator :
    (atom : S.KernelAtom) → evaluate (S.atom atom) ≡ evaluate-atom atom
  evaluate-generator atom = refl

  evaluate-zero : evaluate (S.KernelCoefficientGroup .snd .AbGroupStr.0g) ≡ 0g
  evaluate-zero = refl

  evaluate-sum :
    (u v : S.KernelCoefficientGroup .fst) →
    evaluate (S.KernelCoefficientGroup .snd .AbGroupStr._+_ u v) ≡ evaluate u + evaluate v
  evaluate-sum u v = refl

  evaluate-negative :
    (u : S.KernelCoefficientGroup .fst) →
    evaluate (S.KernelCoefficientGroup .snd .AbGroupStr.-_ u) ≡ - evaluate u
  evaluate-negative u = refl

  evaluation-homomorphism : AbGroupHom S.KernelCoefficientGroup ValueGroup
  evaluation-homomorphism .fst = evaluate
  evaluation-homomorphism .snd = makeIsGroupHom evaluate-sum

  evaluate-tail :
    (τ : Parameter) → evaluate (S.tail τ) ≡ evaluate-atom (S.tail-discrepancy τ)
  evaluate-tail τ = refl
