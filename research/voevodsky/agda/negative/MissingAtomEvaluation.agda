{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module MissingAtomEvaluation where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Unit
open import Cubical.Algebra.AbGroup
open import Cubical.Algebra.AbGroup.Instances.Int
open import SymbolicKernelCoefficients
open import KernelEvaluation

module S = SymbolicKernel Unit

-- Deliberate failure: choosing a target group does not define analytic
-- evaluation. Every symbolic atom still needs an assigned target value.
bad-evaluation : AbGroupHom S.KernelCoefficientGroup ℤAbGroup
bad-evaluation = Evaluate.evaluation-homomorphism ℤAbGroup
