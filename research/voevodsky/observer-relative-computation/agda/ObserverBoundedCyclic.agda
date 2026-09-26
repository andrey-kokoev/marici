{-# OPTIONS --safe --cubical --guardedness #-}
module ObserverBoundedCyclic where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Sigma.Base using (_,_; fst; snd)
open import Cubical.Data.Sigma.Properties using (Σ≡Prop)
open import Cubical.Data.Nat.Base using (ℕ; suc; _+_)
open import Cubical.Data.Nat.Order using (_≤_; isProp≤; suc-≤-suc; ≤SumLeft; ≤SumRight)
open import Cubical.Data.Nat.Mod using (modIndBase)
open import Cubical.Data.Fin.Base using (fzero)
open import Cubical.Data.Int.Base using (abs)
open import Cubical.Data.Empty.Base using (⊥)
import ObserverInternalComparison as C
import ObserverComparisonCompression as P
import ObserverJointRefinement as J
import ObserverFiniteCyclicBoundary as B
import ObserverSignedCyclicCover as S

-- A State N also represents a positive-power count at most N, carrying
-- its bound proof. Actual observation still uses transport, not projection.
read-path : (N : ℕ) → (C.base ≡ C.base) → S.State N
read-path N p = subst (S.Fibre N) p fzero

bounded-path : {N : ℕ} → S.State N → C.base ≡ C.base
bounded-path x = P.path (J.power (fst x))

read-bounded : (N : ℕ) → S.State N → S.State N
read-bounded N x = read-path N (bounded-path x)

bounded-exact : (N : ℕ) (x : S.State N) → read-bounded N x ≡ x
bounded-exact N x = S.power-reading N (fst x)
  ∙ Σ≡Prop (λ _ → isProp≤) (modIndBase N (fst x) (snd x))

bounded-observation-equivalence : (N : ℕ) → S.State N ≃ S.State N
bounded-observation-equivalence N = isoToEquiv
  (iso (read-bounded N) (λ x → x) (bounded-exact N) (bounded-exact N))

-- Recovery is of the actual interpreted comparison path.
recover-path : (N : ℕ) → S.State N → C.base ≡ C.base
recover-path N = bounded-path

faithful-path : (N : ℕ) (x : S.State N)
  → recover-path N (read-bounded N x) ≡ bounded-path x
faithful-path N x = cong (bounded-path {N}) (bounded-exact N x)

-- Distinct counts denote distinct semantic paths, not just syntax labels.
power-injective : (n m : ℕ) → P.path (J.power n) ≡ P.path (J.power m) → n ≡ m
power-injective n m e = cong abs
  (sym (B.power-winding n) ∙ cong B.winding e ∙ B.power-winding m)

within-bound : (N k : ℕ) → k ≤ N → fst (read-path N (P.path (J.power k))) ≡ k
within-bound N k bound = cong fst (bounded-exact N (k , suc-≤-suc bound))

-- A single probe chosen from the pair suffices. This swaps quantifiers
-- relative to the impossible one-fixed-finite-family-for-all-paths claim.
pair-separation : (n m : ℕ) → (n ≡ m → ⊥)
  → read-path (n + m) (P.path (J.power n))
    ≡ read-path (n + m) (P.path (J.power m)) → ⊥
pair-separation n m unequal e = unequal
  (sym (within-bound (n + m) n ≤SumLeft)
    ∙ cong fst e ∙ within-bound (n + m) m ≤SumRight)

all-probes-detect-count : (n m : ℕ)
  → ((N : ℕ) → read-path N (P.path (J.power n)) ≡ read-path N (P.path (J.power m)))
  → n ≡ m
all-probes-detect-count n m agreement =
  sym (within-bound (n + m) n ≤SumLeft)
    ∙ cong fst (agreement (n + m)) ∙ within-bound (n + m) m ≤SumRight

all-probes-detect-path : (n m : ℕ)
  → ((N : ℕ) → read-path N (P.path (J.power n)) ≡ read-path N (P.path (J.power m)))
  → P.path (J.power n) ≡ P.path (J.power m)
all-probes-detect-path n m agreement = cong (λ k → P.path (J.power k))
  (all-probes-detect-count n m agreement)
