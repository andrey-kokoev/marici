{-# OPTIONS --safe --cubical --guardedness #-}
module SeedTriangleJointContext where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (true≢false; false≢true)
import TableFibrationCycle as T
import SeedSeamPathComparisonBoundary as S
open import ActualSeedEndpointTable using (Vertex; A; B)

data Choice : Type where
  direct indirect : Choice

data Triangle : Type where
  ABC ADB : Triangle

forward-choice return-choice : Triangle → Choice
forward-choice ABC = direct
forward-choice ADB = indirect
return-choice ABC = indirect
return-choice ADB = direct

forward-path : Choice → S.Path A B
forward-path direct = S.x0
forward-path indirect = S.x1
return-path : Choice → S.Path B A
return-path direct = S.y0
return-path indirect = S.y1

append : {a b c : Vertex} → S.Path a b → S.Path b c → S.Path a c
append S.stop q = q
append (S.step e p) q = S.step e (append p q)

joint : T.Table Triangle Choice Choice
joint = T.table Triangle (λ t → t) forward-choice return-choice

execution : Triangle → S.Path A A
execution t = append (forward-path (forward-choice t)) (return-path (return-choice t))

recovers-ABC : execution ABC ≡ append S.x0 S.y1
recovers-ABC = refl
recovers-ADB : execution ADB ≡ append S.x1 S.y0
recovers-ADB = refl

-- Grouping preserves the two actual joint rows, not just their projections.
source-group-recovery : T.TableIso (T.unpack (T.group-from joint)) joint
source-group-recovery = T.unpack-correct joint
four-step-recovery : T.TableIso (T.four joint) joint
four-step-recovery = T.four-correct joint

code : Choice → Bool
code direct = false
code indirect = true

-- Both marginal choices occur, but the diagonal pairs have no joint witness.
no-direct-direct : (t : Triangle) → forward-choice t ≡ direct
  → return-choice t ≡ direct → ⊥
no-direct-direct ABC first second = true≢false (cong code second)
no-direct-direct ADB first second = true≢false (cong code first)

no-indirect-indirect : (t : Triangle) → forward-choice t ≡ indirect
  → return-choice t ≡ indirect → ⊥
no-indirect-indirect ABC first second = false≢true (cong code first)
no-indirect-indirect ADB first second = false≢true (cong code second)

-- The product domain is a different supplied row family. Its diagonal rows
-- are valid paths but are not members of the original triangle relation.
all-pairs : T.Table (Choice × Choice) Choice Choice
all-pairs = T.table (Choice × Choice) (λ p → p) fst snd

all-pairs-execution : Choice × Choice → S.Path A A
all-pairs-execution (x , y) = append (forward-path x) (return-path y)
