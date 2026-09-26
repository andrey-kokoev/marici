{-# OPTIONS --safe --cubical --guardedness #-}
module DependentReorderingLawRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (ℕ; suc)
open import Cubical.Data.FinData.Base using (Fin; toℕ) renaming (zero to fzero)
open import Cubical.Data.Empty.Base using (⊥)
import WholePackageSigmaPi as Whole
import DependentReorderingLawInstance as Reordering
import IndexIdentityCoherenceRegression as Loop

-- Infinite first index, next three index types dependent on earlier choices,
-- and a retained higher witness rather than a proof-irrelevant leaf value.
module R = Reordering.Instance ℕ (λ n → Fin (suc n))
  (λ n j → Fin (suc (toℕ j)))
  (λ n j k → Fin (suc (toℕ k)))
  (λ n j k l → Loop.base-index ≡ Loop.base-index)

source : R.R.C.X
source n = fzero , (λ k → fzero , Loop.index-loop)

root-law = R.generated source
infinite-context-law = R.pi-generated ℕ (λ _ → source)
empty-context-law = R.pi-generated ⊥ (λ ())
selected-sum-law = R.sum-generated ℕ (λ _ → source) 0

root-histories-distinct : R.outer-history source ≡ R.inner-history source → ⊥
root-histories-distinct = R.history-records-distinct source

-- Both actual dependent rule contexts enter the normalized Generated bridge.
normalized-infinite-law = R.NG.normal-sound infinite-context-law
normalized-sum-law = R.NG.normal-sound selected-sum-law

full-next-input = R.next-Q source

retained-loop-nontrivial :
  snd (snd ((fst (Whole.Universe.value full-next-input)) 0) fzero) ≡ refl → ⊥
retained-loop-nontrivial = Loop.loop-is-not-reflexive

-- The frozen algebra's guarantee concerns every value of the input type,
-- not just the selected values stored in the Complete endpoints.
all-values-normalized : (v : R.R.C.X)
  → fst (lower (R.A.U.evaluate R.A.algebra (R.outer-history source)) v)
      ≡ R.A.N.normalize R.R.Q v
all-values-normalized = R.A.evaluation-preserves (R.outer-history source)
