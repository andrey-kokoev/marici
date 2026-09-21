{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureCoherentContextAdmission where

open import Cubical.Foundations.Prelude hiding (lift)
open import Cubical.Foundations.Equiv
open import ClosureContextualForkAdmission using (module Contextual)

module Contexts (K : Type) (Piece : K → Type) (Boundary : K → K → Type)
  (attachL : {a b : K} → Boundary a b → Piece a)
  (attachR : {a b : K} → Boundary a b → Piece b) where
  module C = Contextual K Piece Boundary attachL attachR
  open C.A.N

  record Coherent {a b : K} {w : Word a b} (p q : Bracket w) : Type where
    constructor coherent
    field
      base : C.Change p q
      firstPort : C.Ports.First base
      lastPort : C.Ports.Last base
      firstSquare : C.Ports.FirstCoherence base firstPort
      lastSquare : C.Ports.LastCoherence base lastPort

  identity : {a b : K} {w : Word a b} (p : Bracket w) → Coherent p p
  identity p = coherent (C.identity p) (C.identityFirst p) (C.identityLast p)
    (C.identityFirstCoherence p) (C.identityLastCoherence p)

  forkCoherent : {a b c d : K} {u : Word a b} {v : Word c d}
    {p p′ : Bracket u} {q q′ : Bracket v} →
    Coherent p p′ → Coherent q q′ → Coherent (fork p q) (fork p′ q′)
  forkCoherent l r = coherent F.result
    (F.parentFirst (Coherent.firstPort l)) (F.parentLast (Coherent.lastPort r))
    (F.preserveFirst (Coherent.firstPort l) (Coherent.firstSquare l))
    (F.preserveLast (Coherent.lastPort r) (Coherent.lastSquare r))
    where
    module F = C.Fork (Coherent.base l) (Coherent.base r)
      (Coherent.lastPort l) (Coherent.firstPort r)
      (Coherent.lastSquare l) (Coherent.firstSquare r)

  module InHole {start end : K} (w : Word start end) where
    data Context : {a b : K} → Word a b → Type where
      hole : Context w
      left : {a b c d : K} {u : Word a b} {v : Word c d} →
        Context u → Bracket v → Context (u ++ v)
      right : {a b c d : K} {u : Word a b} {v : Word c d} →
        Bracket u → Context v → Context (u ++ v)

    plug : {a b : K} {v : Word a b} → Context v → Bracket w → Bracket v
    plug hole p = p
    plug (left context sibling) p = fork (plug context p) sibling
    plug (right sibling context) p = fork sibling (plug context p)

    -- Recursion retains both external port cells for the NEXT ancestor.
    lift : {a b : K} {v : Word a b} (context : Context v) {p q : Bracket w} →
      Coherent p q → Coherent (plug context p) (plug context q)
    lift hole e = e
    lift (left context sibling) e = forkCoherent (lift context e) (identity sibling)
    lift (right sibling context) e = forkCoherent (identity sibling) (lift context e)

    admitted : {a b : K} {v : Word a b} (context : Context v) {p q : Bracket w} →
      Coherent p q → C.A.Edges.Admitted v (plug context p) (plug context q)
    admitted context e = C.A.Edges.admitted (equivFun (C.frame result))
      (λ x i → equivFun (C.normalization result i) x)
      where
      result = Coherent.base (lift context e)

    retainsFrame : {a b : K} {v : Word a b} (context : Context v) {p q : Bracket w}
      (e : Coherent p q) → C.A.Edges.actionEquiv v (admitted context e) ≡
        C.frame (Coherent.base (lift context e))
    retainsFrame context e = equivEq refl

-- Arbitrary finite contexts and arbitrary siblings, but with explicit
-- coherent first/last ports at the hole. No automatic conversion from an
-- unpointed Admitted edge to Coherent is asserted.
