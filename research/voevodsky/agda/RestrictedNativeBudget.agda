{-# OPTIONS --safe --cubical --guardedness #-}
module RestrictedNativeBudget where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool)
open import Cubical.Data.Nat.Base using (ℕ; suc; _+_)
open import Cubical.Data.Nat.Properties using (injSuc; snotz)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Sigma.Base using (_×_)
open import RestrictedSeedArityProfile
open import RestrictedNativeTableExecution

-- A declared big-step, unit-constructor cost model. Not Agda runtime cost.
data Exec : Term → ℕ → N.G.Package → Type₁ where
  literal-step : Exec (literal false-seed) 1 (native (literal false-seed))
  identity-step : {t : Term} {n : ℕ} {q : N.G.Package}
    → Exec t n q → Exec (identity t) (suc n) (N.identity-comparison q)
  pair-step : {t u : Term} {n m : ℕ} {q r : N.G.Package}
    → Exec t n q → Exec u m r
    → Exec (pair t u) (suc (n + m)) (N.Pi-package Bool (native-family q r))
  select-step : (b : Bool) {t u : Term} {n m : ℕ} {q r : N.G.Package}
    → Exec t n q → Exec u m r
    → Exec (select b t u) (suc (n + m)) (N.E-package Bool (native-family q r) b)

execute : (t : Term) → Exec t (cost t) (native t)
execute (literal false-seed) = literal-step
execute (identity t) = identity-step (execute t)
execute (pair t u) = pair-step (execute t) (execute u)
execute (select b t u) = select-step b (execute t) (execute u)

cost-sound : {t : Term} {n : ℕ} {q : N.G.Package} → Exec t n q → n ≡ cost t
cost-sound literal-step = refl
cost-sound (identity-step d) = cong suc (cost-sound d)
cost-sound (pair-step d e) = cong suc (cong₂ _+_ (cost-sound d) (cost-sound e))
cost-sound (select-step b d e) = cong suc (cong₂ _+_ (cost-sound d) (cost-sound e))

output-sound : {t : Term} {n : ℕ} {q : N.G.Package} → Exec t n q → q ≡ native t
output-sound literal-step = refl
output-sound (identity-step d) = cong N.identity-comparison (output-sound d)
output-sound (pair-step d e) = cong₂ (λ a b → N.Pi-package Bool (native-family a b))
  (output-sound d) (output-sound e)
output-sound (select-step b d e) = cong₂ (λ a c → N.E-package Bool (native-family a c) b)
  (output-sound d) (output-sound e)

BudgetRun : Term → ℕ → Type₁
BudgetRun t budget = Σ[ spent ∈ ℕ ] Σ[ q ∈ N.G.Package ]
  (Exec t spent q × (Σ[ remaining ∈ ℕ ] (spent + remaining ≡ budget)))

funded : (t : Term) (remaining : ℕ) → BudgetRun t (cost t + remaining)
funded t remaining = cost t , native t , execute t , remaining , refl

-- A guard equivalence at the witness level, not only sampled budgets.
guard-from-run : {t : Term} {budget : ℕ} → BudgetRun t budget
  → Σ[ remaining ∈ ℕ ] (cost t + remaining ≡ budget)
guard-from-run (spent , q , d , remaining , eq) =
  remaining , sym (cong (λ n → n + remaining) (cost-sound d)) ∙ eq

run-from-guard : {t : Term} {budget : ℕ}
  → (Σ[ remaining ∈ ℕ ] (cost t + remaining ≡ budget)) → BudgetRun t budget
run-from-guard {t} (remaining , eq) = cost t , native t , execute t , remaining , eq

no-underfunded-selected : BudgetRun selected-example 3 → ⊥
no-underfunded-selected run with guard-from-run run
... | remaining , eq = snotz (injSuc (injSuc (injSuc eq)))

RetainedBudget : ℕ → Type₁
RetainedBudget budget = Σ[ t ∈ Term ] BudgetRun t budget

retain-funded : (t : Term) (remaining : ℕ) → RetainedBudget (cost t + remaining)
retain-funded t remaining = t , funded t remaining

syntax-budget-recovered : (t : Term) (remaining : ℕ)
  → fst (retain-funded t remaining) ≡ t
syntax-budget-recovered t remaining = refl
