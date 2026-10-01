{-# OPTIONS --safe --cubical --guardedness #-}
module SelfFeedingPawRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (true)
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.FinData.Base using (Fin; toℕ) renaming (zero to fzero; suc to fsuc)
open import SelfFeedingPromotion

ends0 : Fin 4 → Fin 4 × Fin 4
ends0 fzero = fzero , fsuc fzero
ends0 (fsuc fzero) = fzero , fsuc (fsuc fzero)
ends0 (fsuc (fsuc fzero)) = fsuc fzero , fsuc (fsuc fzero)
ends0 (fsuc (fsuc (fsuc fzero))) = fzero , fsuc (fsuc (fsuc fzero))
seed : Graph
seed = graph 4 4 ends0

g1 = iterate 1 seed
g2 = iterate 2 seed
g3 = iterate 3 seed
counts : Graph → ℕ × ℕ
counts g = Graph.vertex-count g , Graph.edge-count g
first-counts : counts g1 ≡ (4 , 5)
first-counts = refl
second-counts : counts g2 ≡ (5 , 8)
second-counts = refl
third-counts : counts g3 ≡ (8 , 18)
third-counts = refl

-- IDs0..3 are generated, not manually wired tetrahedral records.
a b c d : Fin (Graph.vertex-count g3)
a = fzero
b = fsuc fzero
c = fsuc (fsuc fzero)
d = fsuc (fsuc (fsuc fzero))
ab : adjacent g3 a b ≡ true
ab = refl
ac : adjacent g3 a c ≡ true
ac = refl
ad : adjacent g3 a d ≡ true
ad = refl
bc : adjacent g3 b c ≡ true
bc = refl
bd : adjacent g3 b d ≡ true
bd = refl
cd : adjacent g3 c d ≡ true
cd = refl

history3 : History g3
history3 = run 3 seed
source-retained : origin history3 ≡ seed
source-retained = origin-run 3 seed
