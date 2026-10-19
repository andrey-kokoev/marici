{-# OPTIONS --safe --cubical --guardedness #-}
module SeedJointQuestionReadout where

open import Cubical.Foundations.Prelude hiding (Path)
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (true≢false)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Sigma.Base using (_×_)
import TableFibrationCycle as T
import ActualSeedEndpointTable as Seed
import SeedSeamPathComparisonBoundary as Paths
import SeedFirstReturnActions as Actions
import SeedArrivalEffects as Arrival
import SeedTriangleJointContext as Joint

-- Freeze the EXISTING two-row joint relation. Do not replace it by the
-- product of its forward and return marginals.
open Joint using (Triangle; ABC; ADB; Choice; direct; indirect)

arrived : Triangle → Arrival.Arrival Seed.A → Arrival.Arrival Seed.A
arrived t initial = Arrival.Read.run (Joint.execution t) initial

choose : Bool → Triangle
choose false = ABC
choose true = ADB

decode : Arrival.Arrival Seed.A → Triangle
decode a = choose (Arrival.is-BA (fst a))

-- A source-relative left inverse, valid for either initial arrival.
-- No claim of recovery of an arbitrary path or of the initial arrival.
triangle-recovered : (t : Triangle) (initial : Arrival.Arrival Seed.A)
  → decode (arrived t initial) ≡ t
triangle-recovered ABC initial = refl
triangle-recovered ADB initial = refl

forward-recovered : (t : Triangle) (initial : Arrival.Arrival Seed.A)
  → Joint.forward-choice (decode (arrived t initial)) ≡ Joint.forward-choice t
forward-recovered t initial = cong Joint.forward-choice (triangle-recovered t initial)

return-recovered : (t : Triangle) (initial : Arrival.Arrival Seed.A)
  → Joint.return-choice (decode (arrived t initial)) ≡ Joint.return-choice t
return-recovered t initial = cong Joint.return-choice (triangle-recovered t initial)

execution-recovered : (t : Triangle) (initial : Arrival.Arrival Seed.A)
  → Joint.execution (decode (arrived t initial)) ≡ Joint.execution t
execution-recovered t initial = cong Joint.execution (triangle-recovered t initial)

-- Every question of the currently specified joint ROW descends through
-- arrival. This is stronger than checking one numerical detector fixture.
question-descends : {Q : Type} (question : Triangle → Q)
  (t : Triangle) (initial : Arrival.Arrival Seed.A)
  → question (decode (arrived t initial)) ≡ question t
question-descends question t initial = cong question (triangle-recovered t initial)

arrival-separates-rows : (s t : Triangle) (a b : Arrival.Arrival Seed.A)
  → arrived s a ≡ arrived t b → s ≡ t
arrival-separates-rows s t a b p = sym (triangle-recovered s a)
  ∙ cong decode p ∙ triangle-recovered t b

-- Apply the already established marked column grouping, not a new T9.
GroupedRows : T.Column → Type
GroupedRows k = T.total (T.fibrate-column Joint.joint k)

original-row : (k : T.Column) → GroupedRows k → Triangle
original-row k (key , row , witness) = row

embed-row : (k : T.Column) → Triangle → GroupedRows k
embed-row k t = T.select Joint.joint k t , t , refl

grouped-arrival : (k : T.Column) → GroupedRows k
  → Arrival.Arrival Seed.A → Arrival.Arrival Seed.A
grouped-arrival k row initial = arrived (original-row k row) initial

grouped-question-square : {Q : Type} (question : Triangle → Q)
  (k : T.Column) (t : Triangle) (initial : Arrival.Arrival Seed.A)
  → question (decode (grouped-arrival k (embed-row k t) initial)) ≡ question t
grouped-question-square question k t initial = question-descends question t initial

-- Exact boundary of that positive result: the existing all-pairs domain
-- contains valid paths not belonging to the two supplied joint rows.
product-arrival : Choice × Choice → Arrival.Arrival Seed.A → Arrival.Arrival Seed.A
product-arrival p initial = Arrival.Read.run (Joint.all-pairs-execution p) initial

product-collision : (initial : Arrival.Arrival Seed.A)
  → product-arrival (direct , direct) initial
    ≡ product-arrival (indirect , direct) initial
product-collision initial = refl

no-product-history-decoder : (initial : Arrival.Arrival Seed.A)
  (recover : Arrival.Arrival Seed.A → Paths.Path Seed.A Seed.A)
  → ((p : Choice × Choice) → recover (product-arrival p initial)
       ≡ Joint.all-pairs-execution p) → ⊥
no-product-history-decoder initial recover law = Actions.distinct-00-10
  (sym (law (direct , direct))
    ∙ cong recover (product-collision initial)
    ∙ law (indirect , direct))

-- Sequential reuse is another distinct enlargement of the row task. The
-- same existing append operation generates a second traversal, while the
-- current arrival alone cannot report how many traversals were retained.
twice-ABC : Paths.Path Seed.A Seed.A
twice-ABC = Actions.append (Joint.execution ABC) (Joint.execution ABC)

repeat-arrival-collision : (initial : Arrival.Arrival Seed.A)
  → arrived ABC initial ≡ Arrival.Read.run twice-ABC initial
repeat-arrival-collision initial = refl

repeat-histories-distinct : Joint.execution ABC ≡ twice-ABC → ⊥
repeat-histories-distinct p = true≢false
  (cong (λ h → Actions.is-three (Paths.length h)) p)

-- Frozen scope: these are source-relative readout/retention theorems on
-- existing operations. They do not make arrival a physical interaction,
-- select T9, authorize extra contexts, or bind the matrix reader J4.
