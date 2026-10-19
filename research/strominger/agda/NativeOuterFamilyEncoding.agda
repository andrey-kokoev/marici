{-# OPTIONS --safe --cubical --guardedness #-}
module NativeOuterFamilyEncoding where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (ℕ; zero; suc; _+_)
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.List.Base using (List; []; _∷_; _++_)
open import NativeGeneratingLeafTable using (Occ; at)
import TableFibrationCycle as T

data Key : Type where
  nat negative : ℕ → Key
  text : List ℕ → Key
  tuple : List Key → Key

-- Values are exact rational-payload trees; mean evaluation remains source-side.
data Row : Type where
  row : Key → Key → Key → Key → ℕ → ℕ → List Row → Row
label source target payload : Row → Key
label (row l s t v m i cs) = l
source (row l s t v m i cs) = s
target (row l s t v m i cs) = t
payload (row l s t v m i cs) = v
mass index : Row → ℕ
mass (row l s t v m i cs) = m
index (row l s t v m i cs) = i

mass-total : List Row → ℕ
mass-total [] = zero
mass-total (r ∷ rs) = mass r + mass-total rs
same : ℕ → ℕ → Bool
same zero zero = true
same (suc a) (suc b) = same a b
same _ _ = false
and : Bool → Bool → Bool
and true b = b
and false b = false
mutual
  valid : Row → Bool
  valid (row l s t v m i []) = same m 1
  valid (row l s t v m i (c ∷ cs)) = and (same m (mass-total (c ∷ cs))) (valid-all (c ∷ cs))
  valid-all : List Row → Bool
  valid-all [] = true
  valid-all (r ∷ rs) = and (valid r) (valid-all rs)
mutual
  flatten : Row → List Row
  flatten r@(row l s t v m i []) = r ∷ []
  flatten (row l s t v m i (c ∷ cs)) = flatten c ++ flatten-all cs
  flatten-all : List Row → List Row
  flatten-all [] = []
  flatten-all (r ∷ rs) = flatten r ++ flatten-all rs

leq : ℕ → ℕ → Bool
leq zero _ = true
leq (suc _) zero = false
leq (suc a) (suc b) = leq a b
insert : Row → List Row → List Row
insert r [] = r ∷ []
insert r (s ∷ ss) with leq (index r) (index s)
... | true = r ∷ s ∷ ss
... | false = s ∷ insert r ss
sort : List Row → List Row
sort [] = []
sort (r ∷ rs) = insert r (sort rs)
leaves : List Row → List Row
leaves rs = sort (flatten-all rs)

-- The carrier is OUTER occurrences, not total fibre membership occurrences.
outer-table : List Row → T.Table Key Key Key
outer-table rs = T.table (Occ rs) (λ i → label (at i))
  (λ i → source (at i)) (λ i → target (at i))

restored : (rs : List Row) (k : T.Column)
  → T.TableIso (T.restore-table k (T.fibrate-table (outer-table rs) k)) (outer-table rs)
restored rs k = T.restore-correct (outer-table rs) k
