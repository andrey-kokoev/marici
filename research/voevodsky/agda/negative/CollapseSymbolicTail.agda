{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module CollapseSymbolicTail where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Unit
open import Cubical.Algebra.AbGroup
open import SymbolicKernelCoefficients

module S = SymbolicKernel Unit

-- Deliberate failure: a free tail generator cannot be collapsed to zero by
-- definitional equality. Analytic evaluation would require a separate map.
bad-collapse : S.tail tt ≡ S.KernelCoefficientGroup .snd .AbGroupStr.0g
bad-collapse i = S.KernelCoefficientGroup .snd .AbGroupStr.0g
