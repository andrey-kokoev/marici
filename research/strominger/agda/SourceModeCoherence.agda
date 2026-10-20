{-# OPTIONS --safe --cubical --guardedness #-}
module SourceModeCoherence where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.GroupoidLaws using (lUnit; rUnit)
open import InternalSourceComparisons using (Mode; stay; exchange)
open import RetainedPackageFeedback using (Total; closure)
import RetainedFeedbackCovariance as R
import ForwardSourceLiftComposition as F
import SourceChainOverlap as C

product-assoc : (m n k : Mode) → F.product (F.product m n) k ≡ F.product m (F.product n k)
product-assoc stay n k = refl
product-assoc exchange stay k = refl
product-assoc exchange exchange stay = refl
product-assoc exchange exchange exchange = refl

-- This is an equality of the ACTUAL composition paths, not just associativity
-- of the mode table. PathP explicitly accounts for the mode endpoint path.
associative-overlap : (m n k : Mode) (c : Total)
  → PathP (λ i → F.action m (F.action n (F.action k c)) ≡ F.action (product-assoc m n k i) c)
      (F.composition-law m n (F.action k c) ∙ F.composition-law (F.product m n) k c)
      (cong (F.action m) (F.composition-law n k c) ∙ F.composition-law m (F.product n k) c)
associative-overlap stay n k c = sym (lUnit (F.composition-law n k c)) ∙ rUnit (F.composition-law n k c)
associative-overlap exchange stay k c = refl
associative-overlap exchange exchange stay c = sym (rUnit (F.forward-square c)) ∙ lUnit (F.forward-square c)
associative-overlap exchange exchange exchange c = cong (λ p → p ∙ refl) (C.triple-exchange-overlap c)

left-unit-coherence : (m : Mode) (c : Total)
  → F.composition-law stay m c ≡ F.unit-law (F.action m c)
left-unit-coherence m c = refl
right-unit-product : (m : Mode) → F.product m stay ≡ m
right-unit-product stay = refl
right-unit-product exchange = refl
right-unit-coherence : (m : Mode) (c : Total)
  → PathP (λ i → F.action m (F.action stay c) ≡ F.action (right-unit-product m i) c)
      (F.composition-law m stay c) (cong (F.action m) (F.unit-law c))
right-unit-coherence stay c = refl
right-unit-coherence exchange c = refl

native-triple-overlap : (c : Total)
  → cong closure (F.forward-square (R.move c))
    ≡ cong (λ q → closure (R.move q)) (F.forward-square c)
native-triple-overlap c = cong (cong closure) (C.triple-exchange-overlap c)
