{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureTreePolarizedSemantics where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import ClosureTreeBoundarySemantics using (module Semantics)

module Polarized (K : Type) (Piece : K → Type) (Boundary : K → K → Type)
  (attachL : {a b : K} → Boundary a b → Piece a)
  (attachR : {a b : K} → Boundary a b → Piece b) where
  module S = Semantics K Piece Boundary attachL attachR
  open S.N

  module At {a b : K} {w : Word a b} (p : Bracket w) (X : Type) where
    Data : Type
    Data = S.Local p (S.Local p X)

    realization : Data ≃ (Realize p → Realize p → X)
    realization = compEquiv (S.realization p (S.Local p X))
      (equivΠCod (λ _ → S.realization p X))

    restrict : (Realize p → Realize p → X) → Data
    restrict = invEq realization
    assemble : Data → Realize p → Realize p → X
    assemble = equivFun realization

    assemble-restrict : (F : Realize p → Realize p → X) → assemble (restrict F) ≡ F
    assemble-restrict = secEq realization
    restrict-assemble : (d : Data) → restrict (assemble d) ≡ d
    restrict-assemble = retEq realization

    determined : (F G : Realize p → Realize p → X) → restrict F ≡ restrict G → F ≡ G
    determined F G h = sym (assemble-restrict F) ∙ cong assemble h ∙ assemble-restrict G

-- Recursive attachment data in BOTH slots retain their mixed cells.
-- No linearity, Hermitian structure, positivity, or Green identification
-- is inferred merely from this equivalence of types.
