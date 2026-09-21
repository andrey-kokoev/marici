{-# OPTIONS --safe --cubical --guardedness #-}
module ForgottenDiamondBoundaryRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Algebra.CommRing.Instances.Int using (ℤCommRing)
open import Cubical.Data.Int using (pos; negsuc; abs)
open import Cubical.Data.Nat.Properties using (snotz)
open import Cubical.Data.Empty using (⊥)
open import ForgottenDiamondBoundary

open Comparison ℤCommRing

integer-nontrivial : (pos 1 ≡ pos 0) → ⊥
integer-nontrivial p = snotz (cong abs p)

forgotten-cycle : V₄
forgotten-cycle = v₄ (pos 1) (negsuc 0) (pos 1) (negsuc 0)

closed : incidence forgotten-cycle ≡ zero₄
closed = cycle-closed (pos 1)

retained-endpoint-difference : project₁ forgotten-cycle ≡ v₂ (pos 1) (negsuc 0)
retained-endpoint-difference = cycle-image (pos 1)

not-zero : (forgotten-cycle ≡ zero₄) → ⊥
not-zero = cycle-nonzero integer-nontrivial

endpoint-not-zero : (endpointDifference (pos 1) ≡ zero₂) → ⊥
endpoint-not-zero = endpoint-nonzero integer-nontrivial

dual-observer-not-exact : (x : V₂) → (dualBoundary x ≡ observer) → ⊥
dual-observer-not-exact = observer-not-boundary integer-nontrivial

nonzero-dual-detection : dot₂ (endpointDifference (pos 1)) observer ≡ pos 1
nonzero-dual-detection = detects-cycle
