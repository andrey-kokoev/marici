{-# OPTIONS --safe --cubical --guardedness #-}
module NativeFeedbackRouteReadout where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (ℕ)
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.Bool.Base using (true; false)
open import Cubical.Data.Bool.Properties using (true≢false)
open import Cubical.Data.Empty.Base using (⊥)
import TetrahedralComparisonFeedback as Existing
import AgreementPolicyBoundary as Agreement

-- Use the actual prior tetrahedral feedback, not an arbitrary instrument.
module F = Existing.Fixture.F
module N = F.N

reading : N.Compared → ℕ × ℕ
reading c = F.steps (N.Compared.first c) , F.steps (N.Compared.second c)

swap : ℕ × ℕ → ℕ × ℕ
swap (a , b) = b , a

-- The source implementation itself supplies the update on this observer.
intertwines : (c : N.Compared)
  → reading (F.F.exchange c) ≡ swap (reading c)
intertwines c = refl

payload-preserved : (c : N.Compared)
  → F.decode-initial (F.F.exchange c) ≡ F.decode-initial c
payload-preserved c = refl

input : N.Compared
input = Agreement.comparison

initial-reading : reading input ≡ (1 , 2)
initial-reading = refl
returned-reading : reading (F.F.exchange input) ≡ (2 , 1)
returned-reading = refl

reading-changes : reading (F.F.exchange input) ≡ reading input → ⊥
reading-changes p = true≢false (sym (cong (λ r → F.is-one (fst r)) p))

-- Keep the source record together with the coarse numeric observer. Neither
-- two counts nor their invariant sum is a faithful history encoding.
record Observed : Type₂ where
  constructor observed
  field
    retained : N.Compared
    values : ℕ × ℕ
    attachment : values ≡ reading retained

observe : N.Compared → Observed
observe c = observed c (reading c) refl

advance : Observed → Observed
advance o = observed (F.F.exchange (Observed.retained o))
  (swap (Observed.values o))
  (cong swap (Observed.attachment o) ∙ sym (intertwines (Observed.retained o)))

recover : (c : N.Compared) → Observed.retained (observe c) ≡ c
recover c = refl
