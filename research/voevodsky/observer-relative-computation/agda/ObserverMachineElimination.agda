{-# OPTIONS --safe --cubical --guardedness #-}
module ObserverMachineElimination where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels using (isSetΣ; isSetRetract)
open import Cubical.Data.Sigma.Base using (Σ; _,_; fst; snd)
open import Cubical.Data.Sum.Base using (_⊎_; inl; inr)
open import Cubical.Data.Sum.Properties using (isSet⊎)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (isSetBool; true≢false)
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import Cubical.Data.Nat.Properties using (isSetℕ)
open import Cubical.Data.Empty.Base using (⊥)
import ResolutionNetDependentMachine as M
import ObserverExecutionBridge as B

absurd : {A : Type} → ⊥ → A
absurd ()

-- Syntax is a set, proved by explicit retractions, not by K/UIP.
index-code : M.Index ⊥ → Σ ℕ (λ _ → Bool)
index-code (M.var ())
index-code (M.lit b) = zero , b
index-code (M.flip b) = suc (fst (index-code b)) , snd (index-code b)

index-decode : Σ ℕ (λ _ → Bool) → M.Index ⊥
index-decode (zero , b) = M.lit b
index-decode (suc n , b) = M.flip (index-decode (n , b))

index-retract : (b : M.Index ⊥) → index-decode (index-code b) ≡ b
index-retract (M.var ())
index-retract (M.lit b) = refl
index-retract (M.flip b) = cong M.flip (index-retract b)

index-set : isSet (M.Index ⊥)
index-set = isSetRetract index-code index-decode index-retract (isSetΣ isSetℕ (λ _ → isSetBool))

Raw = Unit ⊎ (ℕ ⊎ Σ (M.Index ⊥) (λ _ → ℕ))
encode : B.Closed → Raw
encode (_ , M.unit) = inl tt
encode (_ , M.number n) = inr (inl n)
encode (b , M.choose .b n) = inr (inr (b , n))

decode : Raw → B.Closed
decode (inl _) = M.lit true , M.unit
decode (inr (inl n)) = M.lit false , M.number n
decode (inr (inr (b , n))) = b , M.choose b n

retract : (c : B.Closed) → decode (encode c) ≡ c
retract (_ , M.unit) = refl
retract (_ , M.number n) = refl
retract (b , M.choose .b n) = refl

closed-set : isSet B.Closed
closed-set = isSetRetract encode decode retract
  (isSet⊎ (isProp→isSet (λ _ _ → refl)) (isSet⊎ isSetℕ (isSetΣ index-set (λ _ → isSetℕ))))

-- All-index eliminators connect each actual step to the computed next step.
lift-progress : {b : M.Index ⊥} → M.IndexProgress b → M.IndexProgress (M.flip b)
lift-progress (M.ready true) = M.advance-index M.flip-true
lift-progress (M.ready false) = M.advance-index M.flip-false
lift-progress (M.advance-index s) = M.advance-index (M.under-flip s)

flip-progress : (b : M.Index ⊥) → M.index-progress (M.flip b) ≡ lift-progress (M.index-progress b)
flip-progress b with M.index-progress b
... | M.ready true = refl
... | M.ready false = refl
... | M.advance-index s = refl

index-step-computed : {b c : M.Index ⊥} (s : M.IndexStep b c)
  → M.index-progress b ≡ M.advance-index s
index-step-computed M.flip-true = refl
index-step-computed M.flip-false = refl
index-step-computed {M.flip b} (M.under-flip s) = flip-progress b ∙ cong lift-progress (index-step-computed s)

choose-progress : (n : ℕ) {b : M.Index ⊥} → M.IndexProgress b → M.Progress (b , M.choose b n)
choose-progress n (M.ready true) = M.advance (M.select-true n)
choose-progress n (M.ready false) = M.advance (M.select-false n)
choose-progress n (M.advance-index s) = M.advance (M.demand n s)

choose-computed : (b : M.Index ⊥) (n : ℕ)
  → M.progress (b , M.choose b n) ≡ choose-progress n (M.index-progress b)
choose-computed b n with M.index-progress b
... | M.ready true = refl
... | M.ready false = refl
... | M.advance-index s = refl

step-computed : {c d : B.Closed} (s : M.Step c d) → M.progress c ≡ M.advance s
step-computed (M.demand {b} n s) = choose-computed b n ∙ cong (choose-progress n) (index-step-computed s)
step-computed (M.select-true n) = refl
step-computed (M.select-false n) = refl

Outgoing : B.Closed → Type
Outgoing c = Σ B.Closed (M.Step c)

extract : {c : B.Closed} → Outgoing c → M.Progress c → Outgoing c
extract fallback (M.halt value) = fallback
extract fallback (M.advance {d} s) = d , s

outgoing-prop : {c : B.Closed} → isProp (Outgoing c)
outgoing-prop u v = cong (extract u) (sym (step-computed (snd u)) ∙ step-computed (snd v))

-- General run decomposition keeps endpoint equality explicit.
View : {c d : B.Closed} → B.Run c d → Type
View {c} {d} r =
  (Σ (c ≡ d) (λ e → PathP (λ i → B.Run c (e i)) B.stop r))
  ⊎ Σ (Outgoing c) (λ u → Σ (B.Run (fst u) d) (λ tail → B.next (snd u) tail ≡ r))

view : {c d : B.Closed} (r : B.Run c d) → View r
view B.stop = inl (refl , refl)
view (B.next s tail) = inr ((_ , s) , tail , refl)

terminal-unique : {c : B.Closed} → ((d : B.Closed) → M.Step c d → ⊥)
  → (r : B.Run c c) → r ≡ B.stop
terminal-unique {c} no-step r with view r
... | inl (e , h) = sym (subst (λ e → PathP (λ i → B.Run c (e i)) B.stop r)
  (closed-set c c e refl) h)
... | inr ((d , s) , tail , e) = absurd (no-step d s)

peel : {c m d : B.Closed} (s : M.Step c m) (rest : B.Run m d)
  → ((tail : B.Run m d) → tail ≡ rest) → (c ≡ d → ⊥)
  → (r : B.Run c d) → r ≡ B.next s rest
peel {c} {m} {d} s rest unique unequal r with view r
... | inl (e , h) = absurd (unequal e)
... | inr (u , tail , e) = sym e ∙
  J (λ u path → (t : B.Run (fst u) d) → B.next (snd u) t ≡ B.next s rest)
    (λ t → cong (B.next s) (unique t)) (outgoing-prop (m , s) u) tail

no-finished-step : (d : B.Closed) → M.Step B.finished d → ⊥
no-finished-step d ()

pending-bit : B.Closed → Bool
pending-bit (_ , M.unit) = false
pending-bit (_ , M.number n) = false
pending-bit (_ , M.choose b n) = true

middle-not-finished : B.middle ≡ B.finished → ⊥
middle-not-finished e = true≢false (cong pending-bit e)

supplied-not-finished : M.supplied ≡ B.finished → ⊥
supplied-not-finished e = true≢false (cong pending-bit e)
