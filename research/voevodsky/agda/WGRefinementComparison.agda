{-# OPTIONS --safe --cubical --guardedness #-}
module WGRefinementComparison where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Isomorphism using (Iso)
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.Bool.Base using (false; true)
open import TypedGeneratorLayers using (Layer1)
open import ComposableWitnessSpecialization using (compile; Refinement; Realization; Step)
import WGRefinementBaseline as B
import WGRefinementClient as W

-- All equalities quantify over the complete carriers, not eight sampled outputs.
nestedStates : B.Nested ≡ Layer1.State (compile W.second)
nestedStates = refl
flatStates : B.Flat ≡ Layer1.State (compile W.composite)
flatStates = refl
nestedEdges : (x y : B.Nested) → B.NestedEdge x y ≡ Layer1.Witness (compile W.second) x y
nestedEdges x y = refl
flatEdges : (x y : B.Flat) → B.FlatEdge x y ≡ Layer1.Witness (compile W.composite) x y
flatEdges x y = refl
nestedGenerator : (x : B.Nested)
  → (B.nextN x , B.edgeN x) ≡ Layer1.generate (compile W.second) x
nestedGenerator x = refl
flatGenerator : (x : B.Flat)
  → (B.nextF x , B.edgeF x) ≡ Layer1.generate (compile W.composite) x
flatGenerator x = refl
stateMaps : (x : B.Nested) → B.flatten x ≡ Iso.fun (Realization.states W.correct) x
stateMaps x = refl
stepMaps : (x : B.Nested) (z : Step (compile W.second) x)
  → Iso.fun (B.steps x) z ≡ Iso.fun (Realization.steps W.correct x) z
stepMaps x z = refl
inverseStepMaps : (x : B.Nested) (z : Step (compile W.composite) (B.flatten x))
  → Iso.inv (B.steps x) z ≡ Iso.inv (Realization.steps W.correct x) z
inverseStepMaps x z = refl
sources : B.sources ≡ Refinement.source W.composite
sources = refl

leftStates : B.Left ≡ Layer1.State (compile W.reused)
leftStates = refl
rightStates : B.Right ≡ Layer1.State (compile W.A.right)
rightStates = refl
leftEdges : (x y : B.Left) → B.LeftEdge x y ≡ Layer1.Witness (compile W.reused) x y
leftEdges x y = refl
rightEdges : (x y : B.Right) → B.RightEdge x y ≡ Layer1.Witness (compile W.A.right) x y
rightEdges x y = refl
leftGenerator : (x : B.Left) → (B.nextL x , B.edgeL x) ≡ Layer1.generate (compile W.reused) x
leftGenerator x = refl
rightGenerator : (x : B.Right) → (B.nextR x , B.edgeR x) ≡ Layer1.generate (compile W.A.right) x
rightGenerator x = refl
associatedStepMaps : (x : B.Left) (z : Step (compile W.reused) x)
  → Iso.fun (B.associatedSteps x) z ≡ Iso.fun (Realization.steps W.associated x) z
associatedStepMaps x z = refl
inverseAssociatedStepMaps : (x : B.Left) (z : Step (compile W.A.right) (B.associate x))
  → Iso.inv (B.associatedSteps x) z ≡ Iso.inv (Realization.steps W.associated x) z
inverseAssociatedStepMaps x z = refl
sourceMaps : (x : (B.Source × B.Source) × B.Source)
  → Iso.fun B.sourceAssociator x ≡ Iso.fun W.A.source-associator x
sourceMaps x = refl
leftSources : ((B.source₁ , B.source₂) , B.source₃) ≡ Refinement.source W.reused
leftSources = refl
rightSources : (B.source₁ , B.source₂ , B.source₃) ≡ Refinement.source W.A.right
rightSources = refl

-- Negative control: neither implementation can certify the erased payload.
rejectionTypes : B.SecondEvidence ((false , true) , false) ((true , false) , true) (refl , false)
  ≡ Refinement.Extra W.second ((false , true) , false) ((true , false) , true) (refl , false)
rejectionTypes = refl
