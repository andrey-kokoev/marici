{-# OPTIONS --safe --cubical --guardedness #-}
module ObserverFiniteAdaptive where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Sigma.Base using (fst)
open import Cubical.Data.List.Base using (List; []; _∷_; _++_)
open import Cubical.Data.Fin.Base using (fzero)
open import Cubical.Data.Fin.Arithmetic using (_+ₘ_; +ₘ-rUnit)
open import Cubical.Data.Empty.Base using (⊥)
import ObserverInternalComparison as C
import ObserverComparisonCompression as P
import ObserverJointRefinement as J
import ObserverFiniteCyclicBoundary as B
import ObserverSignedCyclicCover as S
import ObserverSignedNormalization as N
module F where
  open import ObserverPhaseFamily public
  open Probe public

-- Finite binary reply tests, with both branches stored as actual data.
data Protocol : Type where
  done : ℕ → Protocol
  query : F.Probe → ℕ → Protocol → Protocol → Protocol

data Event : Type where
  answer : (q : F.Probe) → S.State (F.period-code q) → Event
  finished : ℕ → Event

sameNat : ℕ → ℕ → Bool
sameNat zero zero = true
sameNat zero (suc n) = false
sameNat (suc n) zero = false
sameNat (suc n) (suc m) = sameNat n m

choose : {A : Type} → Bool → A → A → A
choose true x y = x
choose false x y = y

run : Protocol → N.Loop → List Event
run (done label) p = finished label ∷ []
run (query q test yes no) p = answer q (F.read q p) ∷
  choose (sameNat (fst (F.read q p)) test) (run yes p) (run no p)

periods : Protocol → List ℕ
periods (done label) = []
periods (query q test yes no) = F.period-code q ∷ (periods yes ++ periods no)

member-left : {n : ℕ} {xs : List ℕ} (ys : List ℕ) → B.Member n xs → B.Member n (xs ++ ys)
member-left ys B.here = B.here
member-left ys (B.there m) = B.there (member-left ys m)

member-right : {n : ℕ} (xs : List ℕ) {ys : List ℕ} → B.Member n ys → B.Member n (xs ++ ys)
member-right [] m = m
member-right (x ∷ xs) m = B.there (member-right xs m)

-- Pointwise agreement of actual probe transport suffices for the full
-- adaptive transcript. This is a proof premise, not a protocol callback.
replay : (t : Protocol) (p q : N.Loop)
  → ((n : ℕ) → B.Member n (periods t) → (x : S.State n)
    → subst (S.Fibre n) p x ≡ subst (S.Fibre n) q x)
  → run t p ≡ run t q
replay (done label) p q agreement = refl
replay (query sensor test yes no) p q agreement i =
  answer sensor (agreement (F.period-code sensor) B.here (F.phase sensor) i) ∷
  choose (sameNat (fst (agreement (F.period-code sensor) B.here (F.phase sensor) i)) test)
    (replay yes p q (λ n m → agreement n (B.there (member-left (periods no) m))) i)
    (replay no p q (λ n m → agreement n (B.there (member-right (periods yes) m))) i)

invisible : (t : Protocol)
  → run t (P.path (J.power (B.common (periods t)))) ≡ run t (P.path (J.power zero))
invisible t = replay t _ _ (λ n member x →
  F.power-action n (B.common (periods t)) x
    ∙ cong (x +ₘ_) (F.residue-zero (periods t) n member)
    ∙ +ₘ-rUnit x ∙ sym (substRefl {B = S.Fibre n} {x = C.base} x))

no-transcript-decoder : (t : Protocol) (recover : List Event → N.Loop)
  → ((k : ℕ) → recover (run t (P.path (J.power k))) ≡ P.path (J.power k)) → ⊥
no-transcript-decoder t recover exact = B.nontrivial (periods t)
  (sym (exact (B.common (periods t))) ∙ cong recover (invisible t) ∙ exact zero)
