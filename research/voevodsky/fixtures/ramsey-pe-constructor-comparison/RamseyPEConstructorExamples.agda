{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyPEConstructorExamples where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv using (_≃_)
open import Cubical.Foundations.Isomorphism using (iso; isoToEquiv)
open import Cubical.Data.Bool.Base using (Bool; false; true; not)
open import Agda.Builtin.String using (String)
open import RamseyPEConstructorComparison
payload : Bool → String
payload false = "left payload"
payload true = "right payload"
module C = Compare Bool payload (λ s t → t ≡ not s)
module Fixed = Compare Bool payload (λ s t → s ≡ t)
not-square : (b : Bool) → not (not b) ≡ b
not-square false = refl
not-square true = refl
swap : Bool ≃ Bool
swap = isoToEquiv (iso not not not-square not-square)
branch : (b : Bool) → C.Correspondence (C.T.leaf b) (C.T.leaf (not b))
branch b = C.leaf b (not b) refl
source target : C.T.Tree
source = C.T.selection Bool C.T.leaf false
target = C.T.selection Bool C.T.leaf true
selection-comparison : C.Correspondence source target
selection-comparison = C.selection Bool Bool swap C.T.leaf C.T.leaf false true refl branch
native-selection : C.NativeComparison (C.closed source) (C.closed target)
native-selection = C.compile selection-comparison
all-selection-premises : (b : Bool) → C.NativeComparison
  (C.T.R.premise (C.closed source) (lift b))
  (C.T.R.premise (C.closed target) (lift (not b)))
all-selection-premises = C.selection-premises Bool Bool swap C.T.leaf C.T.leaf false true refl branch
unselected-prerequisite : C.NativeComparison
  (C.T.R.premise (C.closed source) (lift true))
  (C.T.R.premise (C.closed target) (lift false))
unselected-prerequisite = all-selection-premises true
product-comparison : C.Correspondence (C.T.product Bool C.T.leaf) (C.T.product Bool C.T.leaf)
product-comparison = C.product Bool Bool swap C.T.leaf C.T.leaf branch
native-product : C.NativeComparison (C.closed (C.T.product Bool C.T.leaf)) (C.closed (C.T.product Bool C.T.leaf))
native-product = C.compile product-comparison
all-product-premises : (b : Bool) → C.NativeComparison
  (C.T.R.premise (C.closed (C.T.product Bool C.T.leaf)) (lift b))
  (C.T.R.premise (C.closed (C.T.product Bool C.T.leaf)) (lift (not b)))
all-product-premises = C.product-premises Bool Bool swap C.T.leaf C.T.leaf branch
