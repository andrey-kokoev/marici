{-# OPTIONS --safe --cubical --guardedness #-}
module ObserverPhaseFamily where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Transport using (substComposite)
open import Cubical.Data.Sigma.Base using (Σ; _,_)
open import Cubical.Data.Sigma.Properties using (Σ≡Prop)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Nat.Base using (ℕ; zero; suc; _+_)
open import Cubical.Data.Nat.Order using (isProp≤)
open import Cubical.Data.Nat.Mod using (_mod_; zero-charac-gen)
open import Cubical.Data.Fin.Base using (fzero)
open import Cubical.Data.Fin.Arithmetic
open import Cubical.Data.List.Base using (List; []; _∷_)
open import Cubical.Data.Empty.Base using (⊥)
import ObserverInternalComparison as C
import ObserverComparisonCompression as P
import ObserverJointRefinement as J
import ObserverFiniteCyclicBoundary as B
import ObserverSignedCyclicCover as S
import ObserverSignedNormalization as N
import ObserverSignedBounded as D

record Probe : Type where
  constructor probe
  field
    period-code : ℕ
    phase : S.State period-code
open Probe

read : (q : Probe) → N.Loop → S.State (period-code q)
read q p = subst (S.Fibre (period-code q)) p (phase q)

-- Explicitly includes the previously used calibrated observers.
calibrated : ℕ → Probe
calibrated bound = probe (bound + bound) (D.seed bound)

calibration-agrees : (bound : ℕ) (p : N.Loop) → read (calibrated bound) p ≡ D.read bound p
calibration-agrees bound p = refl

zero-residue : (n : ℕ) → fzero ≡ S.residue n zero
zero-residue n = Σ≡Prop (λ _ → isProp≤) refl

power-action : (n k : ℕ) (x : S.State n)
  → subst (S.Fibre n) (P.path (J.power k)) x ≡ x +ₘ S.residue n k
power-action n zero x = substRefl {B = S.Fibre n} {x = C.base} x ∙ sym (+ₘ-rUnit x)
  ∙ cong (x +ₘ_) (zero-residue n)
power-action n (suc k) x = substComposite (S.Fibre n) (P.path (J.power k)) (P.path P.turn) x
  ∙ cong (subst (S.Fibre n) (P.path P.turn)) (power-action n k x)
  ∙ S.forward-transport n (x +ₘ S.residue n k)
  ∙ +ₘ-assoc x (S.residue n k) (S.residue n 1)
  ∙ cong (x +ₘ_) (S.residue-step n k)

residue-zero : (ps : List ℕ) (n : ℕ) → B.Member n ps
  → S.residue n (B.common ps) ≡ fzero
residue-zero ps n member with B.factor member
... | k , e = Σ≡Prop (λ _ → isProp≤)
  (cong (_mod (suc n)) e ∙ zero-charac-gen (suc n) k)

periods : List Probe → List ℕ
periods [] = []
periods (q ∷ qs) = period-code q ∷ periods qs

Readings : List Probe → Type
Readings [] = Unit
Readings (q ∷ qs) = Σ (S.State (period-code q)) (λ _ → Readings qs)

initial : (qs : List Probe) → Readings qs
initial [] = tt
initial (q ∷ qs) = phase q , initial qs

joint : (qs : List Probe) → N.Loop → Readings qs
joint [] p = tt
joint (q ∷ qs) p = read q p , joint qs p

restores : (k : ℕ) (qs : List Probe)
  → ((n : ℕ) → B.Member n (periods qs) → S.residue n k ≡ fzero)
  → joint qs (P.path (J.power k)) ≡ initial qs
restores k [] zeros = refl
restores k (q ∷ qs) zeros i =
  (power-action (period-code q) k (phase q)
    ∙ cong (phase q +ₘ_) (zeros (period-code q) B.here) ∙ +ₘ-rUnit (phase q)) i ,
  restores k qs (λ n member → zeros n (B.there member)) i

zero-reading : (qs : List Probe) → joint qs (P.path (J.power zero)) ≡ initial qs
zero-reading [] = refl
zero-reading (q ∷ qs) i = substRefl {B = S.Fibre (period-code q)} {x = C.base} (phase q) i , zero-reading qs i

invisible : (qs : List Probe)
  → joint qs (P.path (J.power (B.common (periods qs)))) ≡ joint qs (P.path (J.power zero))
invisible qs = restores (B.common (periods qs)) qs (residue-zero (periods qs)) ∙ sym (zero-reading qs)

no-path-recovery : (qs : List Probe) (recover : Readings qs → N.Loop)
  → ((k : ℕ) → recover (joint qs (P.path (J.power k))) ≡ P.path (J.power k)) → ⊥
no-path-recovery qs recover exact = B.nontrivial (periods qs)
  (sym (exact (B.common (periods qs))) ∙ cong recover (invisible qs) ∙ exact zero)
