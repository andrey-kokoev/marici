{-# OPTIONS --safe --cubical --guardedness #-}
module ObserverInternalInterface where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma.Base using (Σ; _,_; fst; snd)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Bool.Base using (Bool)
open import Cubical.Data.Empty.Base using (⊥)
import ObserverNonuniqueHistory as H

-- A finite constructor vocabulary, with compositional access codes.
-- No constructor stores a host-language function or arbitrary evaluator.
data Code : Type where
  result rule : Code
  both : Code → Code → Code

Reply : Code → Type
Reply result = Unit
Reply rule = Bool
Reply (both c d) = Σ (Reply c) (λ _ → Reply d)

readout : (c : Code) → H.History → Reply c
readout result h = H.result-observer h
readout rule h = H.rule-observer h
readout (both c d) h = readout c h , readout d h

record Package : Type where
  constructor package
  field
    history : H.History
    observer : Code
open Package

-- One uniform interpreter inspects the code carried by the package.
-- The observer description is internal data; the semantic definition
-- still lives in the surrounding type theory.
Reading = Σ Code Reply

manifest : Package → Reading
manifest p = observer p , readout (observer p) (history p)

Certificate : Package → Type
Certificate p = Σ (Reply (observer p)) (λ r → r ≡ readout (observer p) (history p))

certify : (p : Package) → Certificate p
certify p = readout (observer p) (history p) , refl

-- A code-level noninterference criterion: arbitrary combinations of
-- result-only access cannot recover distinctions between histories.
data ResultOnly : Code → Type where
  just-result : ResultOnly result
  combine-results : {c d : Code} → ResultOnly c → ResultOnly d → ResultOnly (both c d)

noninterference : {c : Code} → ResultOnly c → (h k : H.History)
  → readout c h ≡ readout c k
noninterference just-result h k = refl
noninterference (combine-results c d) h k i =
  noninterference c h k i , noninterference d h k i

no-result-only-recovery : {c : Code} (access : ResultOnly c)
  (recover : Reply c → H.History)
  → ((h : H.History) → recover (readout c h) ≡ h) → ⊥
no-result-only-recovery access recover exact = H.histories-distinct
  (sym (exact H.red-history)
    ∙ cong recover (noninterference access H.red-history H.blue-history)
    ∙ exact H.blue-history)

-- Locate an actual rule-read capability in a composite code.
data RuleAccess : Code → Type where
  here : RuleAccess rule
  on-left : {c d : Code} → RuleAccess c → RuleAccess (both c d)
  on-right : {c d : Code} → RuleAccess d → RuleAccess (both c d)

recover : {c : Code} → RuleAccess c → Reply c → H.History
recover here b = H.replay b
recover (on-left a) r = recover a (fst r)
recover (on-right a) r = recover a (snd r)

faithful : {c : Code} (access : RuleAccess c) (h : H.History)
  → recover access (readout c h) ≡ h
faithful here h = H.replay-rule h
faithful (on-left a) h = faithful a h
faithful (on-right a) h = faithful a h

same-result-manifestation :
  manifest (package H.red-history result) ≡ manifest (package H.blue-history result)
same-result-manifestation = refl

rule-readings-distinct : readout rule H.red-history ≡ readout rule H.blue-history → ⊥
rule-readings-distinct e = H.histories-distinct
  (sym (faithful here H.red-history) ∙ cong (recover here) e ∙ faithful here H.blue-history)

composite-example : (h : H.History)
  → recover {c = both result rule} (on-right here) (readout (both result rule) h) ≡ h
composite-example = faithful {c = both result rule} (on-right here)
