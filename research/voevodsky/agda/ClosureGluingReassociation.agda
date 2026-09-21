{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureGluingReassociation where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Function using (idfun)
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Bool using (Bool; false; true)
open import Cubical.Data.Unit
import Cubical.HITs.Pushout.Base as PO
open import ClosureDependentRefinementTrees
open import ClosureReferenceNormalForm using (module Model)

-- A chain of three pieces joined across two independently specified spans.
module Chain (A B C S T : Type)
  (f : S → A) (g : S → B) (h : T → B) (k : T → C) where

  AB BC : Type
  AB = PO.Pushout f g
  BC = PO.Pushout h k

  attachLeft : T → AB
  attachLeft t = PO.inr (h t)

  attachRight : S → BC
  attachRight s = PO.inl (g s)

  Left Right : Type
  Left = PO.Pushout attachLeft k
  Right = PO.Pushout f attachRight

  -- These maps are defined on ALL point and attachment constructors,
  -- independently of the common-reference coherence machinery.
  associate : Left → Right
  associate (PO.inl (PO.inl a)) = PO.inl a
  associate (PO.inl (PO.inr b)) = PO.inr (PO.inl b)
  associate (PO.inl (PO.push s i)) = PO.push s i
  associate (PO.inr c) = PO.inr (PO.inr c)
  associate (PO.push t i) = PO.inr (PO.push t i)

  unassociate : Right → Left
  unassociate (PO.inl a) = PO.inl (PO.inl a)
  unassociate (PO.inr (PO.inl b)) = PO.inl (PO.inr b)
  unassociate (PO.inr (PO.inr c)) = PO.inr c
  unassociate (PO.inr (PO.push t i)) = PO.push t i
  unassociate (PO.push s i) = PO.inl (PO.push s i)

  associateSection : (z : Right) → associate (unassociate z) ≡ z
  associateSection (PO.inl a) = refl
  associateSection (PO.inr (PO.inl b)) = refl
  associateSection (PO.inr (PO.inr c)) = refl
  associateSection (PO.inr (PO.push t i)) = refl
  associateSection (PO.push s i) = refl

  associateRetraction : (z : Left) → unassociate (associate z) ≡ z
  associateRetraction (PO.inl (PO.inl a)) = refl
  associateRetraction (PO.inl (PO.inr b)) = refl
  associateRetraction (PO.inl (PO.push s i)) = refl
  associateRetraction (PO.inr c) = refl
  associateRetraction (PO.push t i) = refl

  reassociation : Left ≃ Right
  reassociation = isoToEquiv
    (iso associate unassociate associateSection associateRetraction)

  leftInner : Tree AB 1
  leftInner = glueNode f g (idEquiv AB) leaf leaf leaf

  rightInner : Tree BC 1
  rightInner = glueNode h k (idEquiv BC) leaf leaf leaf

  -- Same left tree before and after giving its root the Right realization.
  rawLeftTree : Tree Left 2
  rawLeftTree = glueNode attachLeft k (idEquiv Left) leftInner leaf leaf

  leftTree rightTree : Tree Right 2
  leftTree = glueNode attachLeft k reassociation leftInner leaf leaf
  rightTree = glueNode f attachRight (idEquiv Right) leaf leaf rightInner

  LeftFull RightFull : Type
  LeftFull = At leftTree (full leftTree)
  RightFull = At rightTree (full rightTree)

  rawLeftFrame : LeftFull ≃ Left
  rawLeftFrame = frame rawLeftTree (full rawLeftTree)

  leftFrame : LeftFull ≃ Right
  leftFrame = frame leftTree (full leftTree)

  rightFrame : RightFull ≃ Right
  rightFrame = frame rightTree (full rightTree)

  -- Independently defined reassociation, surrounded by the necessary
  -- refined-span frames. Refined attachment maps are NOT dropped here.
  throughReassociation : LeftFull → RightFull
  throughReassociation x = invEq rightFrame (associate (equivFun rawLeftFrame x))

  tree : Bool → Tree Right 2
  tree false = leftTree
  tree true = rightTree

  -- Small indices range over cuts of BOTH arrangements, not just one tree.
  ArrangementCut : Type
  ArrangementCut = Σ[ b ∈ Bool ] Cut (tree b)

  module Views = Model ArrangementCut
    (λ _ → LeftFull) (λ c → At (tree (fst c)) (snd c)) LeftFull Right
    (λ _ → idEquiv LeftFull)
    (λ c → frame (tree (fst c)) (snd c)) (equivFun leftFrame)

  leftFull rightFull leftRoot rightRoot : ArrangementCut
  leftFull = false , full leftTree
  rightFull = true , full rightTree
  leftRoot = false , root leftTree
  rightRoot = true , root rightTree

  identityPresentation : Views.Cuts.Compatible leftFull
  identityPresentation = idfun LeftFull , refl

  reassociatedPresentation : Views.Cuts.Compatible rightFull
  reassociatedPresentation = throughReassociation , funExt
    (λ x → secEq rightFrame (associate (equivFun rawLeftFrame x)))

  -- The generated cross-arrangement operation is this actual reassociation,
  -- not merely an unspecified inhabitant of a contractible comparison type.
  generatedIsReassociation : Views.view rightFull ≡ throughReassociation
  generatedIsReassociation = refl

  changedIdentityIsReassociation :
    fst (Views.Cuts.change leftFull rightFull identityPresentation) ≡ throughReassociation
  changedIdentityIsReassociation = refl

  changeMatchesReassociation :
    Views.Cuts.change leftFull rightFull identityPresentation ≡ reassociatedPresentation
  changeMatchesReassociation = Views.Cuts.compare rightFull _ _

  cycle : Views.Cuts.Route leftFull leftFull
  cycle = Views.Cuts.step leftFull (Views.Cuts.step leftRoot
    (Views.Cuts.step rightRoot (Views.Cuts.step rightFull (Views.Cuts.stay leftFull))))

  cycleIsTrivial : Views.closedCycle cycle identityPresentation ≡ refl
  cycleIsTrivial = Views.closedCycleIsTrivial cycle identityPresentation

-- Frames for these two arrangements deliberately use the constructed
-- associator. This does not identify unrelated previously chosen associator
-- paths with the generated typed paths, nor prove a four-piece pentagon.
