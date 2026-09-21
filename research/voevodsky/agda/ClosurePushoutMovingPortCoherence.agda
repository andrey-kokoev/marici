{-# OPTIONS --safe --cubical --guardedness #-}
module ClosurePushoutMovingPortCoherence where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.GroupoidLaws using (lUnit; assoc; lCancel)
open import Cubical.Foundations.Path using (compPath→Square)
import Cubical.HITs.Pushout.Base as PO
open import ClosurePushoutTransportCoherence using (module FixedLeft)

-- Coherence on the changing RIGHT piece of the existing transport frame.
-- The selected framePath is retained; it is not replaced by a new comparison.
module MovingRight {S A : Type} (f : S → A) where
  module T = FixedLeft f

  rightIn : (D : T.Diagram) → fst D → T.Realize D
  rightIn D = PO.inr

  MovingSquare : {D E : T.Diagram} (p : D ≡ E)
    {x : fst D} {y : fst E} → PathP (λ i → fst (p i)) x y → Type
  MovingSquare {D} {E} p {x} {y} q =
    PathP (λ i → equivFun (T.framePath p i) (PO.inr x) ≡ PO.inr y)
      (fromPathP {A = λ i → T.Realize (p i)} (λ i → PO.inr (q i)))
      (cong (rightIn E) (fromPathP {A = λ i → fst (p i)} q))

  module Constant (D : T.Diagram) (x : fst D) where
    include : fst D → T.Realize D
    include = PO.inr
    whole : transport refl (include x) ≡ include x
    whole = transportRefl (include x)
    piece : include (transport refl x) ≡ include x
    piece = cong include (transportRefl x)

    computes : T.agreesWithTransport refl (include x) ≡ T.Constant.homotopy D (include x)
    computes = cong (λ witness → fst witness (include x))
      (JRefl (λ (E : T.Diagram) (p : D ≡ E) → T.ComparisonData p) (T.Constant.comparison D))

    square : MovingSquare (refl {x = D}) (refl {x = x})
    square = compPath→Square
      (cong (λ h → h ∙ piece) computes
        ∙ cong (λ r → (whole ∙ r) ∙ piece) (sym (lUnit (sym piece)))
        ∙ sym (assoc whole (sym piece) piece)
        ∙ cong (λ r → whole ∙ r) (lCancel piece))

  PointedDiagram : Type₁
  PointedDiagram = Σ[ D ∈ T.Diagram ] fst D

  movingSquare : {D E : T.Diagram} (p : D ≡ E)
    {x : fst D} {y : fst E} (q : PathP (λ i → fst (p i)) x y) → MovingSquare p q
  movingSquare {D} p {x} q =
    J (λ (end : PointedDiagram) (r : (D , x) ≡ end) →
      MovingSquare (λ i → fst (r i)) (λ i → snd (r i)))
      (Constant.square D x) (λ i → p i , q i)

  PortSquare : {D E : T.Diagram} (p : D ≡ E)
    {x₀ x : fst D} {y : fst E} (r : x₀ ≡ x) (q : PathP (λ i → fst (p i)) x y) → Type
  PortSquare {D} {E} p {x₀} {x} {y} r q =
    PathP (λ i → equivFun (T.framePath p i) (PO.inr x₀) ≡ PO.inr y)
      (cong (transport (cong T.Realize p)) (cong (rightIn D) r)
        ∙ fromPathP {A = λ i → T.Realize (p i)} (λ i → PO.inr (q i)))
      (cong (rightIn E) (cong (transport (λ i → fst (p i))) r
        ∙ fromPathP {A = λ i → fst (p i)} q))

  sourcePort : {D E : T.Diagram} (p : D ≡ E)
    {x₀ x : fst D} {y : fst E} (r : x₀ ≡ x) (q : PathP (λ i → fst (p i)) x y) → PortSquare p r q
  sourcePort {D} {E} p {x₀} {y = y} r q =
    J (λ x r → (q : PathP (λ i → fst (p i)) x y) → PortSquare p r q) baseCase r q
    where
    baseCase : (q : PathP (λ i → fst (p i)) x₀ y) → PortSquare p refl q
    baseCase q = subst2
      (λ start finish → PathP (λ i → equivFun (T.framePath p i) (PO.inr x₀) ≡ PO.inr y) start finish)
      (lUnit (fromPathP {A = λ i → T.Realize (p i)} (λ i → PO.inr (q i))))
      (cong (cong (rightIn E)) (lUnit (fromPathP {A = λ i → fst (p i)} q)))
      (movingSquare p q)

-- This also applies to moving last endpoints. Neither the piece path nor
-- the dependent endpoint path is assumed constant or contractible.
