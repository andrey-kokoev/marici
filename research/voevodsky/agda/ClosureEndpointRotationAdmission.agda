{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureEndpointRotationAdmission where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism using (isoToEquiv; invIso)
open import Cubical.HITs.Pushout.Properties using (PushoutAlongEquiv)
import ClosureSubtreeRotationAdmission as Earlier

module Endpoint (K : Type) (Piece : K → Type) (Boundary : K → K → Type)
  (attachL : {a b : K} → Boundary a b → Piece a)
  (attachR : {a b : K} → Boundary a b → Piece b) where
  module G = Earlier.Subtrees K Piece Boundary attachL attachR
  open G.G.A.N

  module Rotation {a b c d e f : K}
    {u : Word a b} {v : Word c d} {w : Word e f}
    (p : Bracket u) (q : Bracket v) (r : Bracket w) where
    module Indexed = G.ReindexRotation p q r
    module E = Indexed.E

    nativeLast : (x : Piece f) →
      equivFun Indexed.nativeEquivalence (lastAt Indexed.leftTree x) ≡ lastAt Indexed.rightTree x
    nativeLast x = fromPathP (λ i → lastAt (Indexed.treePath i) x)

    onLast : (x : Piece f) →
      equivFun (normalize Indexed.rightTree)
        (equivFun Indexed.nativeEquivalence (lastAt Indexed.leftTree x)) ≡
      equivFun (normalize Indexed.leftTree) (lastAt Indexed.leftTree x)
    onLast x = cong (equivFun (normalize Indexed.rightTree)) (nativeLast x)
      ∙ normalizeLast Indexed.rightTree x ∙ sym (normalizeLast Indexed.leftTree x)

    -- A genuine restriction, not an assumed normalization square.
    module WithLastEquivalence (lastIsEquiv : isEquiv (lastAt Indexed.leftTree)) where
      lastFrame : Piece f ≃ Realize Indexed.leftTree
      lastFrame = lastAt Indexed.leftTree , lastIsEquiv

      abstract
        square : Indexed.NormalizationSquare
        square y =
          sym (cong (λ z → equivFun (normalize Indexed.rightTree)
            (equivFun Indexed.nativeEquivalence z)) (secEq lastFrame y))
          ∙ onLast (invEq lastFrame y)
          ∙ cong (equivFun (normalize Indexed.leftTree)) (secEq lastFrame y)

      forward : E.Admitted Indexed.leftTree Indexed.rightTree
      forward = Indexed.admit square

      backward : E.Admitted Indexed.rightTree Indexed.leftTree
      backward = E.admitted (invEq Indexed.nativeEquivalence) (λ y →
        sym (square (invEq Indexed.nativeEquivalence y))
        ∙ cong (equivFun (normalize Indexed.rightTree)) (secEq Indexed.nativeEquivalence y))

  -- Sufficient local hypotheses for every tree's final inclusion to be an
  -- equivalence. These hypotheses DO NOT hold for the Bool->Unit fixtures.
  module InvertibleLeft (legIsEquiv : {a b : K} → isEquiv (attachL {a} {b})) where
    abstract
      lastIsEquiv : {a b : K} {w : Word a b} (t : Bracket w) → isEquiv (lastAt t)
      lastIsEquiv (leaf a) = idIsEquiv (Piece a)
      lastIsEquiv (fork {b = b} {c} l r) = snd (compEquiv
        (lastAt r , lastIsEquiv r) inclusion)
        where
        boundaryFrame : Boundary b c ≃ Realize l
        boundaryFrame = compEquiv (attachL {b} {c} , legIsEquiv) (lastAt l , lastIsEquiv l)
        inclusion : Realize r ≃ Realize (fork l r)
        inclusion = isoToEquiv (invIso (PushoutAlongEquiv boundaryFrame (λ s → firstAt r (attachR s))))
