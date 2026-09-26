{-# OPTIONS --safe --cubical --guardedness #-}
module ObserverCodedAnchorDescent where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma.Base using (Σ; _,_; fst; snd)
open import Cubical.Data.Sum.Base using (_⊎_; inl; inr)
open import Cubical.Data.Empty.Base using (⊥)
import ObserverInternalInterface as O
import ObserverAccessClassification as A
import ObserverInternalRestriction as R
import ObserverNonuniqueHistory as H
import ObserverInternalComparison as C
import ObserverAnchorChange as G

-- Existing first-order codes observe the anchored bit via its proved
-- History/Bool correspondence, not a new observer primitive.
observe : (c : O.Code) → G.RecordAt C.base → O.Reply c
observe c r = O.readout c (H.replay (G.normalize C.base r))

-- A specification of factorization, not a callback constructor in Code.
Descends : O.Code → Type
Descends c = Σ (G.Unanchored → O.Reply c)
  (λ f → (r : G.RecordAt C.base) → f (G.forget r) ≡ observe c r)

result-descent : {c : O.Code} → O.ResultOnly c → Descends c
result-descent {c} a = (λ _ → O.readout c H.red-history) ,
  (λ r → O.noninterference a H.red-history (H.replay (G.normalize C.base r)))

rule-obstruction : {c : O.Code} → O.RuleAccess c → Descends c → ⊥
rule-obstruction a (f , exact) = G.no-normalization-descent
  (λ q → H.rule-observer (O.recover a (f q)))
  (λ r → cong (λ x → H.rule-observer (O.recover a x)) (exact r)
    ∙ cong H.rule-observer (O.faithful a (H.replay (G.normalize C.base r)))
    ∙ H.rule-replay (G.normalize C.base r))

absurd : {X : Type} → ⊥ → X
absurd ()

-- Both implications of the exact existence criterion.
descent-necessary : (c : O.Code) → Descends c → O.ResultOnly c
descent-necessary c factor with A.classify c
... | inl a = a
... | inr a = absurd (rule-obstruction a factor)

-- Effective complete decision, retaining positive data or a refutation.
decide-descent : (c : O.Code) → Descends c ⊎ (Descends c → ⊥)
decide-descent c with A.classify c
... | inl a = inl (result-descent a)
... | inr a = inr (rule-obstruction a)

-- The descent class is closed under the internal restriction calculus.
restrict-descent : {c d : O.Code} → R.Restrict c d → Descends c → Descends d
restrict-descent r (f , exact) = (λ q → R.run r (f q)) ,
  (λ q → cong (R.run r) (exact q)
    ∙ R.preserves r (H.replay (G.normalize C.base q)))

-- Concrete boundary: duplicating rule access does not repair lost anchors.
duplicate-obstruction : Descends (O.both O.rule O.rule) → ⊥
duplicate-obstruction = rule-obstruction (O.on-left O.here)

constant-observation-exists : Descends (O.both O.result O.result)
constant-observation-exists = result-descent (O.combine-results O.just-result O.just-result)
