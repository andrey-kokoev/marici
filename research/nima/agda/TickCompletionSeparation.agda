{-# OPTIONS --safe --cubical --guardedness #-}
module TickCompletionSeparation where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Unit using (Unit; tt)
open import Cubical.Data.Empty using (⊥; isProp⊥)
open import Cubical.Relation.Nullary using (Dec; yes; no)
open import Cubical.Data.Rationals as Q using (fromNatℚ)
open import Cubical.Data.Nat.Literals
import Cubical.Data.Nat.Order as NatOrder
import Cubical.Data.Rationals.Order as QOrder
open import Cubical.HITs.PropositionalTruncation as PT
open import RegularCauchyStructure
open import RationalAnalyticSubstrate using (one-half)
open import CauchyMetricEquivalence
open import MetricCompletionEffectiveness
open import CauchyCompletionAbGroup using (zeroCompletion)

Rejected : {A : Type} → Dec A → Type
Rejected (yes _) = ⊥
Rejected (no _) = Unit
reject : {A : Type} (d : Dec A) → Rejected d → A → ⊥
reject (yes _) impossible _ = impossible
reject (no notA) _ a = notA a
quarter : Q.ℚ
quarter = one-half Q.· (1 Q.+ (Q.- one-half))
quarter-nonzero : embedMetricℚ quarter ≡ zeroCompletion → ⊥
quarter-nonzero p = PT.rec isProp⊥
  (λ { (N , bounds) →
    reject (QOrder.≤Dec quarter (0 Q.+ precision 3)) tt
      (fst (bounds N NatOrder.≤-refl)) })
  (quotientPathToMetric (constantCauchy quarter) (constantCauchy 0) p 3)
