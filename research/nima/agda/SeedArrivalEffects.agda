{-# OPTIONS --safe --cubical --guardedness #-}
module SeedArrivalEffects where

open import Cubical.Foundations.Prelude hiding (Path)
open import Cubical.Foundations.Isomorphism using (Iso)
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (true≢false)
open import Cubical.Data.Empty.Base using (⊥)
open import ActualSeedEndpointTable
open import SeedSeamPathComparisonBoundary using (Path; x0; x1; y0; y1)
import SeedFirstReturnActions as Actions
open Actions using (r00; r01; r10; r11; is-AB)
import TableFibrationCycle as T

-- Existing target-grouped row fibers, not invented physical payloads.
Arrival : Vertex → Type
Arrival = T.Grouped.Family (T.group-to seed)

-- Read the supplied occurrence as the new active arriving row.
-- This observation update is not inferred dynamics or an invertible transport.
arrive : (e : Occurrence) → Arrival (source e) → Arrival (target e)
arrive e previous = e , refl

module Read = Actions.Effects Arrival arrive

forward-direct : (a : Arrival A) → Read.run x0 a ≡ (AB , refl)
forward-direct a = refl
forward-indirect : (a : Arrival A) → Read.run x1 a ≡ (DB , refl)
forward-indirect a = refl
return-direct : (b : Arrival B) → Read.run y0 b ≡ (BA , refl)
return-direct b = refl
return-indirect : (b : Arrival B) → Read.run y1 b ≡ (CA , refl)
return-indirect b = refl

is-BA : Occurrence → Bool
is-BA AB = false
is-BA BC = false
is-BA CA = false
is-BA AD = false
is-BA DB = false
is-BA BA = true

forward-discrepancy : (a : Arrival A) → Read.run x0 a ≡ Read.run x1 a → ⊥
forward-discrepancy a p = true≢false (cong (λ v → is-AB (fst v)) p)
return-discrepancy : (b : Arrival B) → Read.run y0 b ≡ Read.run y1 b → ⊥
return-discrepancy b p = true≢false (cong (λ v → is-BA (fst v)) p)

-- The active arrival forgets the outward choice, but not the returning choice.
return-00-10 : (a : Arrival A) → Read.run r00 a ≡ Read.run r10 a
return-00-10 a = refl
return-01-11 : (a : Arrival A) → Read.run r01 a ≡ Read.run r11 a
return-01-11 a = refl
return-00-01-discrepancy : (a : Arrival A) → Read.run r00 a ≡ Read.run r01 a → ⊥
return-00-01-discrepancy a p = true≢false (cong (λ v → is-BA (fst v)) p)

-- Keep the initial value as well as the full route and current arrival.
-- The unchanged six-row seed (including off-route rows) remains the source.
trace : (p : Path A A) (a : Arrival A) → Σ (Arrival A) (λ _ → Read.Retained A)
trace p a = a , Read.returned p a
initial-recovery : (p : Path A A) (a : Arrival A) → fst (trace p a) ≡ a
initial-recovery p a = refl
history-recovery : (p : Path A A) (a : Arrival A) → fst (snd (trace p a)) ≡ p
history-recovery p a = refl

-- Test all three existing column-grouping/recovery operations on active rows.
-- Embedding in the grouped presentation and recovering preserves the row.
regroup-row : T.Column → Occurrence → Occurrence
regroup-row k e = Iso.fun rows (Iso.inv rows e)
  where
  rows = T.TableIso.rows (T.restore-correct seed k)
regroup-correct : (k : T.Column) (e : Occurrence) → regroup-row k e ≡ e
regroup-correct k e = Iso.rightInv (T.TableIso.rows (T.restore-correct seed k)) e

regroup-forward-discrepancy : (k l : T.Column)
  → regroup-row k AB ≡ regroup-row l DB → ⊥
regroup-forward-discrepancy k l p = true≢false
  (cong is-AB (sym (regroup-correct k AB) ∙ p ∙ regroup-correct l DB))
regroup-return-discrepancy : (k l : T.Column)
  → regroup-row k BA ≡ regroup-row l CA → ⊥
regroup-return-discrepancy k l p = true≢false
  (cong is-BA (sym (regroup-correct k BA) ∙ p ∙ regroup-correct l CA))

four-row : Occurrence → Occurrence
four-row e = Iso.fun rows (Iso.inv rows e)
  where
  rows = T.TableIso.rows four-recovery
four-row-correct : (e : Occurrence) → four-row e ≡ e
four-row-correct e = Iso.rightInv (T.TableIso.rows four-recovery) e
