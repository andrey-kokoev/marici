{-# OPTIONS --safe --cubical --guardedness #-}
module MarkedArrivalComparison where

open import Cubical.Foundations.Prelude hiding (Path)
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (true≢false)
open import Cubical.Data.Empty.Base using (⊥)
open import ActualSeedEndpointTable
import SeedSeamPathComparisonBoundary as H
import SeedFirstReturnActions as R

-- Terminal mark = the history before the final step together with that step.
Arrival = Σ Occurrence (λ e → H.Path A (source e))
word : (m : Arrival) → H.Path A (target (fst m))
word (e , prefix) = R.append prefix (H.step e H.stop)

direct detour : Arrival
direct = AB , H.stop
detour = DB , H.step AD H.stop

direct-word : word direct ≡ H.x0
direct-word = refl
detour-word : word detour ≡ H.x1
detour-word = refl

same-site : target (fst direct) ≡ target (fst detour)
same-site = refl

isAB : Occurrence → Bool
isAB AB = true
isAB _ = false

-- Any proposed relation on marks must forgo incoming-arrow preservation
-- if it relates this pair. This does not assume the relation is equality.
reject-arrow-preserving : (Rel : Arrival → Arrival → Type)
  → ((x y : Arrival) → Rel x y → fst x ≡ fst y)
  → Rel direct detour → ⊥
reject-arrow-preserving Rel preserve r = true≢false (cong isAB (preserve direct detour r))
