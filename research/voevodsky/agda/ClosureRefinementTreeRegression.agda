{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureRefinementTreeRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Nat using (ℕ; zero; suc)
open import Cubical.Data.Unit
open import Cubical.Data.Bool using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Empty using (⊥)
open import Cubical.Data.Sum.Base using (_⊎_; inl; inr)
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.HITs.Pushout.Base using (cofib)
open import Cubical.HITs.S1.Base using (S¹; base; loop)
open import ClosureProductBoundary using (module PointedModel)
open import ClosureCanonicalRejoin using (module Naturality)
open import ClosureRefinementTrees

-- Right-growing trees: the left branch stops at every node. Arbitrary depth
-- is generated recursively, rather than adding indices uniformly everywhere.
InputChain OutputChain : ℕ → Type
InputChain zero = S¹
InputChain (suc n) = S¹ ⊎ InputChain n
OutputChain zero = S¹
OutputChain (suc n) = S¹ × OutputChain n

inputChain : (n : ℕ) → InputTree (InputChain n)
inputChain zero = inputLeaf
inputChain (suc n) = inputFork (idEquiv _) inputLeaf (inputChain n)

outputChain : (n : ℕ) → OutputTree (OutputChain n)
outputChain zero = outputLeaf
outputChain (suc n) = outputFork (idEquiv _) outputLeaf (outputChain n)

inputChainDepth : (n : ℕ) → inputDepth (inputChain n) ≡ n
inputChainDepth zero = refl
inputChainDepth (suc n) = cong suc (inputChainDepth n)

-- Actual cofiber realizations at the roots, not arbitrary unproved root
-- frames. The initial Bool attachment domain of PointedModel is nonempty.
module Input = PointedModel (InputChain 8) (inl base)
module Output = PointedModel (OutputChain 2) (base , (base , base))

send : InputChain 8 → OutputChain 2
send (inl x) = x , (base , base)
send (inr _) = base , (base , base)

module N = Naturality Input.f Input.g send

operation : cofib Input.g → cofib Output.g
operation = N.Lower.direct

inputs : InputTree (cofib Input.g)
inputs = inputFork (invEquiv Input.coneEquiv) inputLeaf (inputChain 7)

outputs : OutputTree (cofib Output.g)
outputs = outputFork Output.coneEquiv outputLeaf (outputChain 1)

module T = Realization inputs outputs operation

inputDepthEight : inputDepth inputs ≡ 8
inputDepthEight = refl

outputDepthTwo : outputDepth outputs ≡ 2
outputDepthTwo = refl

nineInputLeaves : inputWidth inputs (inputFull inputs) ≡ 9
nineInputLeaves = refl

threeOutputLeaves : outputWidth outputs (outputFull outputs) ≡ 3
threeOutputLeaves = refl

-- Different branches can stop at different places. These two partial cuts
-- expose the root only, leaving the non-leaf right subtree unexpanded.
inputOnly outputOnly : T.Cut
inputOnly = inr (tt , inputRoot (inputChain 7)) , outputRoot outputs
outputOnly = inputRoot inputs , inr (tt , outputRoot (outputChain 1))

cycle : T.Views.Cuts.Route T.root T.root
cycle = T.Views.Cuts.step T.root (T.Views.Cuts.step outputOnly
  (T.Views.Cuts.step T.full (T.Views.Cuts.step inputOnly (T.Views.Cuts.stay T.root))))

start : T.Views.Cuts.Compatible T.root
start = T.Views.Cuts.canonical T.root

cycleIsTrivial : T.Views.closedCycle cycle start ≡ refl
cycleIsTrivial = T.Views.closedCycleIsTrivial cycle start

-- Compute the actual fully refined operation on an entire circle loop.
-- This is path data in a chosen sum component, not a point-only test.
loopAction : (i : I) → T.realize T.full (inl (loop i)) ≡ (loop i , (base , base))
loopAction i = refl

-- Arbitrary finite globular coherence is inherited at every pruning. It is
-- distinct from the structural tree depth eight checked above.
allCoherenceLevels : (c : T.Cut) (n : ℕ)
  (b : T.Views.Cuts.Higher.Boundary c n) →
  isContr (T.Views.Cuts.Higher.Cell c n b)
allCoherenceLevels c = T.Views.Cuts.Higher.allCellsContractible c

module SplitGate where
  tag : Unit ⊎ Unit → Bool
  tag (inl tt) = false
  tag (inr tt) = true

  -- A binary shape does not authorize splitting any root into arbitrary
  -- inhabited components. Such an inputFork at Unit would need an impossible
  -- local equivalence, and therefore cannot enter the construction.
  noUnitSplit : (Unit ⊎ Unit) ≃ Unit → ⊥
  noUnitSplit e = false≢true (cong tag
    (sym (retEq e (inl tt)) ∙ retEq e (inr tt)))
