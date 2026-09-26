{-# OPTIONS --safe --cubical --guardedness #-}
module ObserverNonuniqueHistory where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (true≢false)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.HITs.PropositionalTruncation.Base using (∥_∥₁; ∣_∣₁; squash₁)
import ObserverFaithfulRecovery as Recovery

-- One fixed forward admissibility policy, with two distinct rule
-- witnesses at the SAME endpoints. No alternative polarity is involved.
data State : Type where
  initial terminal : State

data Step : State → State → Type where
  red blue : Step initial terminal

data Run : State → State → Type where
  stop : {s : State} → Run s s
  next : {s t u : State} → Step s t → Run t u → Run s u

History = Run initial terminal

red-history blue-history : History
red-history = next red stop
blue-history = next blue stop

-- General elimination over ALL endpoint pairs avoids unsupported
-- constructor-injectivity matching at specialized Run indices.
Shape : State → State → Type
Shape initial initial = Unit
Shape initial terminal = Bool
Shape terminal initial = ⊥
Shape terminal terminal = Unit

diagonal : (s : State) → Shape s s
diagonal initial = tt
diagonal terminal = tt

prefix : (b : Bool) {t : State} → Shape terminal t → Shape initial t
prefix b {initial} ()
prefix b {terminal} _ = b

encode : {s t : State} → Run s t → Shape s t
encode {s} stop = diagonal s
encode (next red rest) = prefix true (encode rest)
encode (next blue rest) = prefix false (encode rest)

decode : (s t : State) → Shape s t → Run s t
decode initial initial _ = stop
decode initial terminal true = red-history
decode initial terminal false = blue-history
decode terminal initial ()
decode terminal terminal _ = stop

decode-diagonal : (s : State) → decode s s (diagonal s) ≡ stop
decode-diagonal initial = refl
decode-diagonal terminal = refl

decode-red : (t : State) (v : Shape terminal t)
  → decode initial t (prefix true v) ≡ next red (decode terminal t v)
decode-red initial ()
decode-red terminal v = refl

decode-blue : (t : State) (v : Shape terminal t)
  → decode initial t (prefix false v) ≡ next blue (decode terminal t v)
decode-blue initial ()
decode-blue terminal v = refl

decode-encode : {s t : State} (r : Run s t) → decode s t (encode r) ≡ r
decode-encode {s} stop = decode-diagonal s
decode-encode {t = t} (next red rest) =
  decode-red t (encode rest) ∙ cong (next red) (decode-encode rest)
decode-encode {t = t} (next blue rest) =
  decode-blue t (encode rest) ∙ cong (next blue) (decode-encode rest)

terminal-unique : (r : Run terminal terminal) → r ≡ stop
terminal-unique r = sym (decode-encode r)

rule-observer : History → Bool
rule-observer = encode

histories-distinct : red-history ≡ blue-history → ⊥
histories-distinct e = true≢false (cong rule-observer e)

-- A one-bit rule observer suffices here; full-history storage is not
-- needed because this fixture has exactly these two possible histories.
replay : Bool → History
replay = decode initial terminal

replay-rule : (h : History) → replay (rule-observer h) ≡ h
replay-rule = decode-encode

rule-replay : (b : Bool) → rule-observer (replay b) ≡ b
rule-replay true = refl
rule-replay false = refl

history-equiv-bit : History ≃ Bool
history-equiv-bit = isoToEquiv (iso rule-observer replay rule-replay replay-rule)

result-observer : History → Unit
result-observer _ = tt

same-result : result-observer red-history ≡ result-observer blue-history
same-result = refl

same-mere-admissibility : ∣ red-history ∣₁ ≡ ∣ blue-history ∣₁
same-mere-admissibility = squash₁ _ _

positive-admissibility : ∥ History ∥₁
positive-admissibility = ∣ red-history ∣₁

no-faithful-admissibility-recovery : (recover : ∥ History ∥₁ → History)
  → ((h : History) → recover ∣ h ∣₁ ≡ h) → ⊥
no-faithful-admissibility-recovery recover exact = histories-distinct
  (Recovery.Faithful.necessary recover exact red-history blue-history)

no-faithful-result-recovery : (recover : Unit → History)
  → ((h : History) → recover (result-observer h) ≡ h) → ⊥
no-faithful-result-recovery recover exact = histories-distinct
  (sym (exact red-history) ∙ exact blue-history)

-- Choosing an allowed history is possible, but is NOT faithful readback.
choose-some : ∥ History ∥₁ → History
choose-some _ = red-history
