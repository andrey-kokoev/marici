{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureTreeBoundarySemantics where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Equiv.Properties using (congEquiv)
open import Cubical.Foundations.Isomorphism using (isoToEquiv; invIso)
open import Cubical.Data.Sigma using (Σ-cong-equiv)
open import ClosureFiniteGluingNormalization using (module System)
open import ClosureGeneratedMapNecessity using (module Generated)

-- Recursive extension of Grothendieck's checked one-node universal law.
-- The source seed and both attachment maps remain explicit inputs.
module Semantics (K : Type) (Piece : K → Type) (Boundary : K → K → Type)
  (attachL : {a b : K} → Boundary a b → Piece a)
  (attachR : {a b : K} → Boundary a b → Piece b) where
  module N = System K Piece Boundary attachL attachR
  open N

  mutual
    Local : {a b : K} {w : Word a b} → Bracket w → Type → Type
    Local (leaf a) X = Piece a → X
    Local (fork {b = b} {c = c} p q) X =
      Σ[ l ∈ Local p X ] Σ[ r ∈ Local q X ]
        ((s : Boundary b c) →
          equivFun (realization p X) l (lastAt p (attachL s)) ≡
          equivFun (realization q X) r (firstAt q (attachR s)))

    realization : {a b : K} {w : Word a b} (t : Bracket w) (X : Type) →
      Local t X ≃ (Realize t → X)
    realization (leaf a) X = idEquiv (Piece a → X)
    realization (fork p q) X = compEquiv nodeData (isoToEquiv (invIso Node.generatedMapIso))
      where
      module Node = Generated {T = X}
        (λ s → lastAt p (attachL s)) (λ s → firstAt q (attachR s))
      nodeData : Local (fork p q) X ≃ Node.Cocone
      nodeData = Σ-cong-equiv (realization p X) (λ l →
        Σ-cong-equiv (realization q X) (λ r → idEquiv _))

  assemble : {a b : K} {w : Word a b} (t : Bracket w) {X : Type} → Local t X → Realize t → X
  assemble t {X} = equivFun (realization t X)
  restrict : {a b : K} {w : Word a b} (t : Bracket w) {X : Type} → (Realize t → X) → Local t X
  restrict t {X} = invEq (realization t X)

  assemble-restrict : {a b : K} {w : Word a b} (t : Bracket w) {X : Type}
    (F : Realize t → X) → assemble t (restrict t F) ≡ F
  assemble-restrict t {X} = secEq (realization t X)
  restrict-assemble : {a b : K} {w : Word a b} (t : Bracket w) {X : Type}
    (d : Local t X) → restrict t (assemble t d) ≡ d
  restrict-assemble t {X} = retEq (realization t X)

  determined : {a b : K} {w : Word a b} (t : Bracket w) {X : Type}
    (F G : Realize t → X) → restrict t F ≡ restrict t G → F ≡ G
  determined t F G h = sym (assemble-restrict t F)
    ∙ cong (assemble t) h ∙ assemble-restrict t G

  -- Equality of local data includes the dependent attachment cells.
  -- This equivalence can itself be iterated on identity types.
  localPaths : {a b : K} {w : Word a b} (t : Bracket w) {X : Type}
    (d e : Local t X) → (d ≡ e) ≃ (assemble t d ≡ assemble t e)
  localPaths t {X} d e = congEquiv (realization t X)

  pull : {a b c d : K} {u : Word a b} {v : Word c d}
    (p : Bracket u) (q : Bracket v) {X : Type} →
    (Realize p → Realize q) → Local q X → Local p X
  pull p q f data′ = restrict p (λ x → assemble q data′ (f x))

  pull-realizes : {a b c d : K} {u : Word a b} {v : Word c d}
    (p : Bracket u) (q : Bracket v) {X : Type}
    (f : Realize p → Realize q) (data′ : Local q X) →
    assemble p (pull p q f data′) ≡ (λ x → assemble q data′ (f x))
  pull-realizes p q f data′ = assemble-restrict p _

  pull-identity : {a b : K} {w : Word a b} (p : Bracket w) {X : Type}
    (data′ : Local p X) → pull p p (λ x → x) data′ ≡ data′
  pull-identity p = restrict-assemble p

  pull-compose : {a b c d e f : K} {u : Word a b} {v : Word c d} {w : Word e f}
    (p : Bracket u) (q : Bracket v) (r : Bracket w) {X : Type}
    (F : Realize p → Realize q) (G : Realize q → Realize r) (data′ : Local r X) →
    pull p q F (pull q r G data′) ≡ pull p r (λ x → G (F x)) data′
  pull-compose p q r F G data′ = cong (restrict p)
    (cong (λ h x → h (F x)) (pull-realizes q r G data′))

  universal : {a b : K} {w : Word a b} (q : Bracket w) → Local q (Realize q)
  universal q = restrict q (λ x → x)

  probe-realizes : {a b c d : K} {u : Word a b} {v : Word c d}
    (p : Bracket u) (q : Bracket v) (F : Realize p → Realize q) →
    assemble p (pull p q F (universal q)) ≡ F
  probe-realizes p q F = pull-realizes p q F (universal q)
    ∙ cong (λ h x → h (F x)) (assemble-restrict q (λ x → x))

  probe-reflects : {a b c d : K} {u : Word a b} {v : Word c d}
    (p : Bracket u) (q : Bracket v) (F G : Realize p → Realize q) →
    pull p q F (universal q) ≡ pull p q G (universal q) → F ≡ G
  probe-reflects p q F G h = sym (probe-realizes p q F)
    ∙ cong (assemble p) h ∙ probe-realizes p q G

-- The universal probe reflects equality of REALIZED MAPS. This does not
-- assert injectivity on free route words, or identify their chosen higher
-- witnesses. No analytical seed is manufactured by the reconstruction.
