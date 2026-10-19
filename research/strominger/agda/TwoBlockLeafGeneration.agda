{-# OPTIONS --safe --cubical --guardedness #-}
module TwoBlockLeafGeneration where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (ℕ; zero; suc; _+_)
open import Cubical.Data.List.Base using (List; []; _∷_; _++_; map; length)
import WholePackageSigmaPi as W

data Kind : Type where
  arrow state : Kind

data Leaf : Kind → Type where
  edge : ℕ → ℕ → Leaf arrow
  point : ℕ → Leaf state
  pair : {k : Kind} → Leaf k → Leaf k → Leaf k

-- Ordered independent comparison. Mixed branches are not in this domain.
product : {k : Kind} → List (Leaf k) → List (Leaf k) → List (Leaf k)
product [] ys = []
product (x ∷ xs) ys = map (pair x) ys ++ product xs ys

record Blocks : Type where
  constructor blocks
  field
    arrows : List (Leaf arrow)
    states : List (Leaf state)
open Blocks

compare : Blocks → Blocks
compare b = blocks (product (arrows b) (arrows b)) (product (states b) (states b))
count : Blocks → ℕ
count b = length (arrows b) + length (states b)

-- The reference is retained but not counted in the selected arrow branch.
record Frame : Type where
  constructor frame
  field
    reference : Leaf arrow
    selected : List (Leaf arrow)
    state-roots : List (Leaf state)

full-arrows : Frame → List (Leaf arrow)
full-arrows f = Frame.reference f ∷ Frame.selected f
input : Frame → Blocks
input f = blocks (Frame.selected f) (Frame.state-roots f)

actual-frame : Frame
actual-frame = frame (edge 0 1)
  (edge 0 2 ∷ edge 0 3 ∷ edge 1 0 ∷ edge 1 2 ∷ edge 1 3 ∷
   edge 2 0 ∷ edge 2 1 ∷ edge 2 3 ∷ edge 3 0 ∷ edge 3 1 ∷ edge 3 2 ∷ [])
  (point 0 ∷ point 1 ∷ point 2 ∷ point 3 ∷ [])

-- Each operation retains its entire predecessor. History is a constructor
-- trace, not a claim that its stage number has the operator's rung meaning.
data History : Type where
  start : Frame → History
  step : History → History

value : History → Blocks
value (start f) = input f
value (step h) = compare (value h)
origin : History → Frame
origin (start f) = f
origin (step h) = origin h

actual-first : History
actual-first = step (start actual-frame)
complete-generation : History → W.Universe.Complete ℓ-zero
complete-generation h = W.Universe.pack (W.Universe.atom History) (step h)

full-frame-count : length (full-arrows actual-frame) ≡ 12
full-frame-count = refl
counted-input : count (input actual-frame) ≡ 15
counted-input = refl
arrow-output : length (arrows (value actual-first)) ≡ 121
arrow-output = refl
state-output : length (states (value actual-first)) ≡ 16
state-output = refl
generated-count : count (value actual-first) ≡ 137
generated-count = refl

recover-parent : History → History
recover-parent (start f) = start f
recover-parent (step h) = h
parent-retention : (h : History)
  → recover-parent (W.Universe.value (complete-generation h)) ≡ h
parent-retention h = refl
origin-retention : (h : History)
  → origin (W.Universe.value (complete-generation h)) ≡ origin h
origin-retention h = refl
