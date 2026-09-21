{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureContextualForkAdmission where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.GroupoidLaws using (lUnit)
open import ClosureFiniteGluingNormalization using (module LiftSpan)
open import ClosureGeneralSpanCoherence using (module Composition)
open import ClosureRotationAdmission using (module Admission)
open import ClosureContextualPortCoherence using (postPort)
import Cubical.HITs.Pushout.Base as PO

module Contextual (K : Type) (Piece : K → Type) (Boundary : K → K → Type)
  (attachL : {a b : K} → Boundary a b → Piece a)
  (attachR : {a b : K} → Boundary a b → Piece b) where
  module A = Admission K Piece Boundary attachL attachR
  open A.N

  -- The normalization path retains the actual supplied equivalence.
  record Change {a b : K} {w : Word a b} (p q : Bracket w) : Type where
    constructor change
    field
      frame : Realize p ≃ Realize q
      normalization : compEquiv frame (normalize q) ≡ normalize p
  open Change public

  fromAdmitted : {a b : K} {w : Word a b} {p q : Bracket w} →
    A.Edges.Admitted w p q → Change p q
  fromAdmitted {w = w} edge = change (A.Edges.actionEquiv w edge)
    (equivEq (funExt (A.Edges.square edge)))

  module Ports {a b : K} {w : Word a b} {p q : Bracket w} (e : Change p q) where
    First : Type
    First = (x : Piece a) → equivFun (frame e) (firstAt p x) ≡ firstAt q x
    Last : Type
    Last = (x : Piece b) → equivFun (frame e) (lastAt p x) ≡ lastAt q x

    FirstCoherence : First → Type
    FirstCoherence port = (x : Piece a) →
      PathP (λ i → equivFun (normalization e i) (firstAt p x) ≡ first w x)
        (cong (equivFun (normalize q)) (port x) ∙ normalizeFirst q x)
        (normalizeFirst p x)

    LastCoherence : Last → Type
    LastCoherence port = (x : Piece b) →
      PathP (λ i → equivFun (normalization e i) (lastAt p x) ≡ last w x)
        (cong (equivFun (normalize q)) (port x) ∙ normalizeLast q x)
        (normalizeLast p x)

  identity : {a b : K} {w : Word a b} (p : Bracket w) → Change p p
  identity p = change (idEquiv (Realize p)) (equivEq refl)

  identityFirst : {a b : K} {w : Word a b} (p : Bracket w) → Ports.First (identity p)
  identityFirst p x = refl
  identityLast : {a b : K} {w : Word a b} (p : Bracket w) → Ports.Last (identity p)
  identityLast p x = refl

  identityFirstCoherence : {a b : K} {w : Word a b} (p : Bracket w) →
    Ports.FirstCoherence (identity p) (identityFirst p)
  identityFirstCoherence p x = sym (lUnit (normalizeFirst p x))
  identityLastCoherence : {a b : K} {w : Word a b} (p : Bracket w) →
    Ports.LastCoherence (identity p) (identityLast p)
  identityLastCoherence p x = sym (lUnit (normalizeLast p x))

  module Fork {a b c d : K} {u : Word a b} {v : Word c d}
    {p p′ : Bracket u} {q q′ : Bracket v}
    (left : Change p p′) (right : Change q q′)
    (lastPort : Ports.Last left) (firstPort : Ports.First right)
    (lastCoherence : Ports.LastCoherence left lastPort)
    (firstCoherence : Ports.FirstCoherence right firstPort) where

    module C = Composition
      (λ (s : Boundary b c) → lastAt p (attachL s)) (λ s → firstAt q (attachR s))
      (λ s → lastAt p′ (attachL s)) (λ s → firstAt q′ (attachR s))
      (λ s → last u (attachL s)) (λ s → first v (attachR s))
      (frame left) (frame right) (normalize p′) (normalize q′)
      (funExt (λ s → lastPort (attachL s))) (funExt (λ s → firstPort (attachR s)))
      (funExt (λ s → normalizeLast p′ (attachL s)))
      (funExt (λ s → normalizeFirst q′ (attachR s)))

    -- Interpolate BOTH comparison frames and their attachment squares.
    children : I → Realize (fork p q) ≃ Join u v
    children i = LiftSpan.equivalence
      (λ (s : Boundary b c) → lastAt p (attachL s)) (λ s → firstAt q (attachR s))
      (λ s → last u (attachL s)) (λ s → first v (attachR s))
      (idEquiv (Boundary b c)) (normalization left i) (normalization right i)
      (funExt (λ s → lastCoherence (attachL s) i))
      (funExt (λ s → firstCoherence (attachR s) i))

    square : (x : Realize (fork p q)) →
      equivFun (normalize (fork p′ q′)) (equivFun C.First.equivalence x) ≡
      equivFun (normalize (fork p q)) x
    square x = cong (equivFun (appendFrame u v))
      (C.compositionAt x ∙ (λ i → equivFun (children i) x))

    result : Change (fork p q) (fork p′ q′)
    result = change C.First.equivalence (equivEq (funExt square))

    parentFirst : Ports.First left → Ports.First result
    parentFirst port x = cong PO.inl (port x)

    parentLast : Ports.Last right → Ports.Last result
    parentLast port x = cong PO.inr (port x)

    preserveFirst : (port : Ports.First left) → Ports.FirstCoherence left port →
      Ports.FirstCoherence result (parentFirst port)
    preserveFirst port coherence x = postPort PO.inl (equivFun (appendFrame u v))
      (λ i → equivFun (normalization left i) (firstAt p x))
      (cong (equivFun (normalize p′)) (port x)) (normalizeFirst p′ x) (normalizeFirst p x)
      (appendFirst u v x) (coherence x)

    preserveLast : (port : Ports.Last right) → Ports.LastCoherence right port →
      Ports.LastCoherence result (parentLast port)
    preserveLast port coherence x = postPort PO.inr (equivFun (appendFrame u v))
      (λ i → equivFun (normalization right i) (lastAt q x))
      (cong (equivFun (normalize q′)) (port x)) (normalizeLast q′ x) (normalizeLast q x)
      (appendLast u v x) (coherence x)

    admitted : A.Edges.Admitted (u ++ v) (fork p q) (fork p′ q′)
    admitted = A.Edges.admitted (equivFun C.First.equivalence) square

    retainsComparison : A.Edges.actionEquiv (u ++ v) admitted ≡ C.First.equivalence
    retainsComparison = equivEq refl

  -- Specializations keep the sibling's actual identity map. Its higher
  -- port cell includes the necessary left-unit contraction.
  module UnderLeft {a b c d : K} {u : Word a b} {v : Word c d}
    {p p′ : Bracket u} (q : Bracket v) (e : Change p p′)
    (port : Ports.Last e) (coherence : Ports.LastCoherence e port) =
    Fork e (identity q) port (identityFirst q) coherence (identityFirstCoherence q)

  module UnderRight {a b c d : K} {u : Word a b} {v : Word c d}
    (p : Bracket u) {q q′ : Bracket v} (e : Change q q′)
    (port : Ports.First e) (coherence : Ports.FirstCoherence e port) =
    Fork (identity p) e (identityLast p) port (identityLastCoherence p) coherence

-- This is admission of the actual LiftSpan comparison, not yet a theorem
-- identifying it with every separately specified strict contextual map.
-- General root rotations still need the relevant coherent port instances.
