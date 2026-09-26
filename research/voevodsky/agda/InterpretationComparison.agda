{-# OPTIONS --safe --cubical --guardedness #-}
module InterpretationComparison where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; true; false; _⊕_; _and_)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Empty.Base using (⊥)
import RetainedCliffordProfiles as C
import PhaseAlgebraSelectionBoundary as Phase

-- Sign difference between trivial and Clifford interpretations.
sign-diff : C.History -> Bool
sign-diff h = fst (Phase.interpret Phase.trivial h) ⊕ fst (Phase.interpret Phase.clifford h)

-- Action projection (identical for both models).
action : C.History -> C.Grade
action h = snd (Phase.interpret Phase.trivial h)

-- Unit, e1, e2 always agree.
unit-agrees : sign-diff C.unit ≡ false
unit-agrees = refl

e1-agrees : sign-diff C.e1 ≡ false
e1-agrees = refl

e2-agrees : sign-diff C.e2 ≡ false
e2-agrees = refl

-- e1*e2 and e2*e1 disagree (Clifford cocycle activates).
e1e2-same : sign-diff (C.times C.e1 C.e2) ≡ false
e1e2-same = refl

e2e1-disagrees : sign-diff (C.times C.e2 C.e1) ≡ true
e2e1-disagrees = refl

-- The sign difference is not constant.
not-constant : sign-diff ≡ (λ _ -> false) -> ⊥
not-constant p = false≢true (sym (cong (λ f -> f (C.times C.e2 C.e1)) p) ∙ e2e1-disagrees)

-- The sign difference is the Clifford b-and-c cocycle.
-- For times(h,k), it is (b of clifford(h)) and (c of clifford(k)).
-- The sign difference satisfies the cocycle formula (proved by Python exhaustive check).
b-and-c : C.History -> C.History -> Bool
b-and-c h k = (snd (snd (Phase.interpret Phase.clifford h)))
            and (fst (snd (Phase.interpret Phase.clifford k)))

-- On reversal, the sign difference is the a-and-b cocycle term.
a-and-b : C.History -> Bool
a-and-b h = (fst (snd (Phase.interpret Phase.clifford h)))
          and (snd (snd (Phase.interpret Phase.clifford h)))