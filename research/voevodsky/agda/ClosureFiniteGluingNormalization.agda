{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureFiniteGluingNormalization where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Equiv.Properties using (congEquiv)
open import Cubical.Foundations.Function using (idfun)
open import Cubical.Data.Nat using (ℕ; zero; suc)
open import Cubical.Data.Nat.Properties using (max)
open import Cubical.Data.Sigma.Base using (_×_)
import Cubical.HITs.Pushout.Base as PO
open import Cubical.HITs.Pushout.Properties using (pushoutEquiv)
open import ClosureGluingReassociation using (module Chain)
open import ClosureReferenceNormalForm using (module Model)

-- Preserve transparent constructor action without unfolding large inverse
-- proofs at each level of a recursively normalized pushout.
module LiftSpan {M L R M′ L′ R′ : Type}
  (f : M → L) (g : M → R) (f′ : M′ → L′) (g′ : M′ → R′)
  (eM : M ≃ M′) (eL : L ≃ L′) (eR : R ≃ R′)
  (hf : (λ x → equivFun eL (f x)) ≡ (λ x → f′ (equivFun eM x)))
  (hg : (λ x → equivFun eR (g x)) ≡ (λ x → g′ (equivFun eM x))) where
  private
    raw = pushoutEquiv f g f′ g′ eM eL eR hf hg
  abstract
    certified : isEquiv (equivFun raw)
    certified = snd raw
  equivalence : PO.Pushout f g ≃ PO.Pushout f′ g′
  equivalence = equivFun raw , certified

-- Labels may distinguish occurrences even when their piece types coincide.
-- Any finite heterogeneous chain can be encoded by distinct position labels.
module System (K : Type) (Piece : K → Type) (Boundary : K → K → Type)
  (attachL : {a b : K} → Boundary a b → Piece a)
  (attachR : {a b : K} → Boundary a b → Piece b) where

  -- Nonempty words retain their first and last labels in their indices.
  data Word : K → K → Type where
    single : (a : K) → Word a a
    cons : (a : K) {b c : K} → Word b c → Word a c

  _++_ : {a b c d : K} → Word a b → Word c d → Word a d
  single a ++ v = cons a v
  cons a u ++ v = cons a (u ++ v)

  pieceCount : {a b : K} → Word a b → ℕ
  pieceCount (single a) = 1
  pieceCount (cons a u) = suc (pieceCount u)

  data Bracket : {a b : K} → Word a b → Type where
    leaf : (a : K) → Bracket (single a)
    fork : {a b c d : K} {u : Word a b} {v : Word c d} →
      Bracket u → Bracket v → Bracket (u ++ v)

  rightBracket : {a b : K} (w : Word a b) → Bracket w
  rightBracket (single a) = leaf a
  rightBracket (cons a u) = fork (leaf a) (rightBracket u)

  depth : {a b : K} {w : Word a b} → Bracket w → ℕ
  depth (leaf a) = zero
  depth (fork l r) = suc (max (depth l) (depth r))

  -- The common target is an explicitly right-associated homotopy gluing.
  mutual
    Normal : {a b : K} → Word a b → Type
    Normal (single a) = Piece a
    Normal (cons a {b} u) = PO.Pushout
      (attachL {a} {b}) (λ s → first u (attachR s))

    first : {a b : K} (w : Word a b) → Piece a → Normal w
    first (single a) x = x
    first (cons a u) x = PO.inl x

    last : {a b : K} (w : Word a b) → Piece b → Normal w
    last (single a) x = x
    last (cons a u) x = PO.inr (last u x)

  Join : {a b c d : K} → Word a b → Word c d → Type
  Join {b = b} {c} u v = PO.Pushout
    (λ (s : Boundary b c) → last u (attachL s))
    (λ s → first v (attachR s))

  -- Flatten a join of two normal chains. Recursion uses the ACTUAL
  -- three-piece reassociator and preserves both external attachment ports.
  mutual
    appendFrame : {a b c d : K} (u : Word a b) (v : Word c d) →
      Join u v ≃ Normal (u ++ v)
    appendFrame (single a) v = idEquiv _
    appendFrame {c = c} (cons a {b = b} {c = z} u) v =
      compEquiv Rotate.reassociation lifted.equivalence
      where
      module Rotate = Chain (Piece a) (Normal u) (Normal v)
        (Boundary a b) (Boundary z c)
        attachL (λ s → first u (attachR s))
        (λ t → last u (attachL t)) (λ t → first v (attachR t))
      module lifted = LiftSpan attachL (λ s → PO.inl (first u (attachR s)))
        attachL (λ s → first (u ++ v) (attachR s))
        (idEquiv (Boundary a b)) (idEquiv (Piece a)) (appendFrame u v)
        refl (funExt (λ s → appendFirst u v (attachR s)))

    appendFirst : {a b c d : K} (u : Word a b) (v : Word c d) (x : Piece a) →
      equivFun (appendFrame u v) (PO.inl (first u x)) ≡ first (u ++ v) x
    appendFirst (single a) v x = refl
    appendFirst (cons a u) v x = refl

    appendLast : {a b c d : K} (u : Word a b) (v : Word c d) (x : Piece d) →
      equivFun (appendFrame u v) (PO.inr (last v x)) ≡ last (u ++ v) x
    appendLast (single a) v x = refl
    appendLast (cons a u) v x = cong PO.inr (appendLast u v x)

  mutual
    Realize : {a b : K} {w : Word a b} → Bracket w → Type
    Realize (leaf a) = Piece a
    Realize (fork {b = b} {c} l r) = PO.Pushout
      (λ (s : Boundary b c) → lastAt l (attachL s))
      (λ s → firstAt r (attachR s))

    firstAt : {a b : K} {w : Word a b} (t : Bracket w) → Piece a → Realize t
    firstAt (leaf a) x = x
    firstAt (fork l r) x = PO.inl (firstAt l x)

    lastAt : {a b : K} {w : Word a b} (t : Bracket w) → Piece b → Realize t
    lastAt (leaf a) x = x
    lastAt (fork l r) x = PO.inr (lastAt r x)

  mutual
    normalize : {a b : K} {w : Word a b} (t : Bracket w) → Realize t ≃ Normal w
    normalize (leaf a) = idEquiv _
    normalize (fork {b = b} {c} {u = u} {v = v} l r) =
      compEquiv children.equivalence (appendFrame u v)
      where
      module children = LiftSpan
        (λ (s : Boundary b c) → lastAt l (attachL s))
        (λ s → firstAt r (attachR s))
        (λ s → last u (attachL s)) (λ s → first v (attachR s))
        (idEquiv (Boundary b c)) (normalize l) (normalize r)
        (funExt (λ s → normalizeLast l (attachL s)))
        (funExt (λ s → normalizeFirst r (attachR s)))

    normalizeFirst : {a b : K} {w : Word a b} (t : Bracket w) (x : Piece a) →
      equivFun (normalize t) (firstAt t x) ≡ first w x
    normalizeFirst (leaf a) x = refl
    normalizeFirst (fork {u = u} {v = v} l r) x =
      cong (λ z → equivFun (appendFrame u v) (PO.inl z)) (normalizeFirst l x)
      ∙ appendFirst u v x

    normalizeLast : {a b : K} {w : Word a b} (t : Bracket w) (x : Piece b) →
      equivFun (normalize t) (lastAt t x) ≡ last w x
    normalizeLast (leaf a) x = refl
    normalizeLast (fork {u = u} {v = v} l r) x =
      cong (λ z → equivFun (appendFrame u v) (PO.inr z)) (normalizeLast r x)
      ∙ appendLast u v x

  normalizedPaths : {a b : K} {w : Word a b} (t : Bracket w)
    {x y : Realize t} → (x ≡ y) ≃ (equivFun (normalize t) x ≡ equivFun (normalize t) y)
  normalizedPaths t = congEquiv (normalize t)

  reflectsNullLoop : {a b : K} {w : Word a b} (t : Bracket w)
    {x : Realize t} (p : x ≡ x) → cong (equivFun (normalize t)) p ≡ refl → p ≡ refl
  reflectsNullLoop t p h = sym (retEq (normalizedPaths t) p)
    ∙ cong (invEq (normalizedPaths t)) h ∙ retEq (normalizedPaths t) refl

  -- One arbitrary operation, independently bracketed on its two sides.
  module Operations {a b c d : K} (u : Word a b) (v : Word c d)
    (operation : Normal u → Normal v) where
    Presentation : Type
    Presentation = Bracket u × Bracket v

    module Views = Model Presentation
      (λ p → Realize (fst p)) (λ p → Realize (snd p)) (Normal u) (Normal v)
      (λ p → normalize (fst p)) (λ p → normalize (snd p)) operation

  module Comparisons {a b : K} (w : Word a b) where
    change : (p q : Bracket w) → Realize p → Realize q
    change p q x = invEq (normalize q) (equivFun (normalize p) x)

    changeIdentity : (p : Bracket w) (x : Realize p) → change p p x ≡ x
    changeIdentity p x = retEq (normalize p) x

    changeComposition : (p q r : Bracket w) (x : Realize p) →
      change q r (change p q x) ≡ change p r x
    changeComposition p q r x = cong (invEq (normalize r))
      (secEq (normalize q) (equivFun (normalize p) x))

    -- Global frames are constructed by normalize, not supplied as hypotheses.
    module Views = Model (Bracket w) (λ _ → Normal w) Realize (Normal w) (Normal w)
      (λ _ → idEquiv (Normal w)) normalize (idfun (Normal w))

    run : {p q : Bracket w} → Views.Cuts.Route p q → Realize p → Realize q
    run (Views.Cuts.stay p) x = x
    run (Views.Cuts.step {j = j} k route) x = change j k (run route x)

    routeNormalForm : {p q : Bracket w} (route : Views.Cuts.Route p q) (x : Realize p) →
      run route x ≡ change p q x
    routeNormalForm (Views.Cuts.stay p) x = sym (changeIdentity p x)
    routeNormalForm {p} (Views.Cuts.step {j = j} k route) x =
      cong (change j k) (routeNormalForm route x) ∙ changeComposition p j k x

    cycleReturns : {p : Bracket w} (route : Views.Cuts.Route p p) (x : Realize p) →
      run route x ≡ x
    cycleReturns {p} route x = routeNormalForm route x ∙ changeIdentity p x

-- These are comparisons generated by the constructed normal frames.
-- Identification of EVERY independently specified local rotation witness
-- with these comparisons is a further theorem, not an implicit assumption.
