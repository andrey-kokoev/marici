{-# OPTIONS --safe --cubical --guardedness #-}
module FreshWrongConclusion where
open import Cubical.Foundations.Prelude
import FreshEquationalConsequences as F
module Bad {ℓ : Level} (A : Type ℓ) (stroke : A → A → A)
  (hypothesis : (x0 x1 x2 : A) → (stroke (stroke (stroke x0 x1) x2) (stroke x0 (stroke (stroke x0 x2) x0))) ≡ x2) where
  module D = F.Derived A stroke hypothesis
  bad : (x0 x1 x2 fresh : A) → fresh ≡ x0
  bad x0 x1 x2 fresh = D.f0 x0 x1 x2
