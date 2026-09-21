{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureGluingPentagon where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.Univalence using (ua; uaCompEquiv)
open import Cubical.Foundations.GroupoidLaws using (rCancel)
open import Cubical.Data.Unit
import Cubical.HITs.Pushout.Base as PO
open import ClosureGluingReassociation using (module Chain)
open import ClosureReferenceNormalForm using (module Model)

module FourPieces (A B C D S T U : Type)
  (f : S → A) (g : S → B) (h : T → B) (k : T → C)
  (l : U → C) (m : U → D) where

  module ABC = Chain A B C S T f g h k
  module BCD = Chain B C D T U h k l m
  module AB-C-D = Chain ABC.AB C D T U ABC.attachLeft k l m
  module A-BC-D = Chain A ABC.BC D S U f ABC.attachRight (λ u → PO.inr (l u)) m
  module A-B-CD = Chain A B BCD.BC S T f g h BCD.attachRight

  Start Middle₁ Middle₂ Balanced Finish : Type
  Start = AB-C-D.Left
  Middle₁ = A-BC-D.Left
  Middle₂ = A-BC-D.Right
  Balanced = AB-C-D.Right
  Finish = A-B-CD.Right

  -- Rotate the left subtree, preserving the outer U attachment.
  rotateLeft : Start → Middle₁
  rotateLeft (PO.inl x) = PO.inl (ABC.associate x)
  rotateLeft (PO.inr d) = PO.inr d
  rotateLeft (PO.push u i) = PO.push u i

  unrotateLeft : Middle₁ → Start
  unrotateLeft (PO.inl x) = PO.inl (ABC.unassociate x)
  unrotateLeft (PO.inr d) = PO.inr d
  unrotateLeft (PO.push u i) = PO.push u i

  leftSection : (z : Middle₁) → rotateLeft (unrotateLeft z) ≡ z
  leftSection (PO.inl x) i = PO.inl (ABC.associateSection x i)
  leftSection (PO.inr d) = refl
  leftSection (PO.push u j) = refl

  leftRetraction : (z : Start) → unrotateLeft (rotateLeft z) ≡ z
  leftRetraction (PO.inl x) i = PO.inl (ABC.associateRetraction x i)
  leftRetraction (PO.inr d) = refl
  leftRetraction (PO.push u j) = refl

  rotateLeftEquiv : Start ≃ Middle₁
  rotateLeftEquiv = isoToEquiv (iso rotateLeft unrotateLeft leftSection leftRetraction)

  -- Rotate the right subtree, preserving the outer S attachment.
  rotateRight : Middle₂ → Finish
  rotateRight (PO.inl a) = PO.inl a
  rotateRight (PO.inr x) = PO.inr (BCD.associate x)
  rotateRight (PO.push s i) = PO.push s i

  unrotateRight : Finish → Middle₂
  unrotateRight (PO.inl a) = PO.inl a
  unrotateRight (PO.inr x) = PO.inr (BCD.unassociate x)
  unrotateRight (PO.push s i) = PO.push s i

  rightSection : (z : Finish) → rotateRight (unrotateRight z) ≡ z
  rightSection (PO.inl a) = refl
  rightSection (PO.inr x) i = PO.inr (BCD.associateSection x i)
  rightSection (PO.push s j) = refl

  rightRetraction : (z : Middle₂) → unrotateRight (rotateRight z) ≡ z
  rightRetraction (PO.inl a) = refl
  rightRetraction (PO.inr x) i = PO.inr (BCD.associateRetraction x i)
  rightRetraction (PO.push s j) = refl

  rotateRightEquiv : Middle₂ ≃ Finish
  rotateRightEquiv = isoToEquiv (iso rotateRight unrotateRight rightSection rightRetraction)

  longRoute shortRoute : Start → Finish
  longRoute x = rotateRight (A-BC-D.associate (rotateLeft x))
  shortRoute x = A-B-CD.associate (AB-C-D.associate x)

  longEquiv shortEquiv : Start ≃ Finish
  longEquiv = compEquiv (compEquiv rotateLeftEquiv A-BC-D.reassociation) rotateRightEquiv
  shortEquiv = compEquiv AB-C-D.reassociation A-B-CD.reassociation

  -- Constructor-level proof for the two actual composites. In particular,
  -- all THREE shared-boundary path families are checked, not only vertices.
  pentagonAt : (x : Start) → longRoute x ≡ shortRoute x
  pentagonAt (PO.inl (PO.inl (PO.inl a))) = refl
  pentagonAt (PO.inl (PO.inl (PO.inr b))) = refl
  pentagonAt (PO.inl (PO.inl (PO.push s i))) = refl
  pentagonAt (PO.inl (PO.inr c)) = refl
  pentagonAt (PO.inl (PO.push t i)) = refl
  pentagonAt (PO.inr d) = refl
  pentagonAt (PO.push u i) = refl

  pentagon : longRoute ≡ shortRoute
  pentagon = funExt pentagonAt

  equivalencePentagon : longEquiv ≡ shortEquiv
  equivalencePentagon = equivEq pentagon

  -- Also compare the actual concatenated universe paths of the five edges.
  -- Equality of endpoint types alone would not establish this pentagon.
  longTypeRoute shortTypeRoute : Start ≡ Finish
  longTypeRoute = (ua rotateLeftEquiv ∙ ua A-BC-D.reassociation) ∙ ua rotateRightEquiv
  shortTypeRoute = ua AB-C-D.reassociation ∙ ua A-B-CD.reassociation

  longTypeNormalForm : ua longEquiv ≡ longTypeRoute
  longTypeNormalForm = uaCompEquiv
    (compEquiv rotateLeftEquiv A-BC-D.reassociation) rotateRightEquiv
    ∙ cong (λ p → p ∙ ua rotateRightEquiv) (uaCompEquiv rotateLeftEquiv A-BC-D.reassociation)

  typePentagon : longTypeRoute ≡ shortTypeRoute
  typePentagon = sym longTypeNormalForm ∙ cong ua equivalencePentagon
    ∙ uaCompEquiv AB-C-D.reassociation A-B-CD.reassociation

  closedTypePentagon : longTypeRoute ∙ sym shortTypeRoute ≡ refl
  closedTypePentagon = cong (λ p → p ∙ sym shortTypeRoute) typePentagon
    ∙ rCancel shortTypeRoute

  residualIsIdentity : (x : Start) → transport (longTypeRoute ∙ sym shortTypeRoute) x ≡ x
  residualIsIdentity x = cong (λ p → transport p x) closedTypePentagon ∙ transportRefl x

  -- Explicit lift into compatible presentations. The short route's square
  -- is the REVERSE of the proved pentagon; it is not assumed independently.
  module Witnesses = Model Unit (λ _ → Start) (λ _ → Finish) Start Finish
    (λ _ → idEquiv Start) (λ _ → idEquiv Finish) longRoute

  longPresentation shortPresentation : Witnesses.Cuts.Compatible tt
  longPresentation = longRoute , refl
  shortPresentation = shortRoute , sym pentagon

  compatiblePentagon : longPresentation ≡ shortPresentation
  compatiblePentagon i = pentagon i , (λ j → pentagon (i ∧ ~ j))

  forgetCompatiblePentagon : cong fst compatiblePentagon ≡ pentagon
  forgetCompatiblePentagon = refl

  -- The explicit lifted pentagon agrees with the generated comparison,
  -- with the SAME fixed endpoints and square witnesses.
  agreesWithGenerated : compatiblePentagon ≡
    Witnesses.Cuts.compare tt longPresentation shortPresentation
  agreesWithGenerated = Witnesses.Cuts.Higher.fillCell tt 2
    ((tt , (longPresentation , shortPresentation)) ,
      (compatiblePentagon , Witnesses.Cuts.compare tt longPresentation shortPresentation))

-- This is the four-piece pentagon for these actual reassociation maps.
-- It does not identify arbitrary older pentagon witnesses, nor prove every
-- higher associahedral relation between arbitrary gluing-tree arrangements.
