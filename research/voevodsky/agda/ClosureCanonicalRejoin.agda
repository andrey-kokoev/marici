{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureCanonicalRejoin where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Function using (idfun)
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Unit
open import Cubical.HITs.Pushout.Base
open import ClosureCofiberTransportCoherence using (module Transport)

module Rejoin {A B C : Type} (f : A → B) (g : B → C) where
  module T = Transport f g

  Quotient : Type
  Quotient = cofib T.direct

  -- The quotient-of-quotients map, defined on all HIT constructors.
  rejoin : Quotient → cofib g
  rejoin (inl tt) = inl tt
  rejoin (inr (inl tt)) = inl tt
  rejoin (inr (inr c)) = inr c
  rejoin (inr (push a i)) = push (f a) i
  rejoin (push (inl tt) i) = inl tt
  rejoin (push (inr b) i) = push b i
  rejoin (push (push a j) i) = push (f a) (j ∧ i)

  cut : cofib g → Quotient
  cut (inl tt) = inl tt
  cut (inr c) = inr (inr c)
  cut (push b i) = push (inr b) i

  rejoin-cut : (x : cofib g) → rejoin (cut x) ≡ x
  rejoin-cut (inl tt) = refl
  rejoin-cut (inr c) = refl
  rejoin-cut (push b i) = refl

  -- Q is the actual nested attachment square. The following cube fills the
  -- deformation of its right edge into its top edge, relative to the other
  -- boundary pieces. Keeping this cube is essential for the inverse proof.
  Q : A → I → I → Quotient
  Q a u v = push (push a u) v

  attachmentCube : A → I → I → I → Quotient
  attachmentCube a u v j = hcomp
    (λ k → λ
      { (u = i0) → Q a i0 (v ∧ j)
      ; (u = i1) → Q a i1 (v ∧ (j ∨ k))
      ; (v = i0) → inl tt
      ; (j = i0) → Q a (u ∨ k) (v ∧ u ∧ k)
      ; (j = i1) → Q a u v
      })
    (Q a u (v ∧ j))

  cut-rejoin : (x : Quotient) → cut (rejoin x) ≡ x
  cut-rejoin (inl tt) = refl
  cut-rejoin (inr (inl tt)) j = push (inl tt) j
  cut-rejoin (inr (inr c)) = refl
  cut-rejoin (inr (push a u)) j = attachmentCube a u i1 j
  cut-rejoin (push (inl tt) v) j = push (inl tt) (v ∧ j)
  cut-rejoin (push (inr b) v) = refl
  cut-rejoin (push (push a u) v) j = attachmentCube a u v j

  rejoinIso : Iso Quotient (cofib g)
  Iso.fun rejoinIso = rejoin
  Iso.inv rejoinIso = cut
  Iso.rightInv rejoinIso = rejoin-cut
  Iso.leftInv rejoinIso = cut-rejoin

  rejoinEquiv : Quotient ≃ cofib g
  rejoinEquiv = isoToEquiv rejoinIso

module Naturality {A B C D : Type}
  (f : A → B) (g : B → C) (h : C → D) where
  module P = Transport f g
  module Q = Transport (λ a → g (f a)) h
  module R = Transport f (λ b → h (g b))
  module Lower = Transport g h
  module Before = Rejoin f g
  module After = Rejoin f (λ b → h (g b))

  -- Explicit induced map of the second quotients. Its nested attachment
  -- constructor uses the same A-coordinate on both sides, so all boundaries
  -- match. No unproved commutation cell is installed as a parameter.
  upper : Before.Quotient → After.Quotient
  upper (inl tt) = inl tt
  upper (inr y) = inr (Q.direct y)
  upper (push (inl tt) i) = push (inl tt) i
  upper (push (inr b) i) = push (inr b) i
  upper (push (push a j) i) = push (push a j) i

  transportThenRejoin : Before.Quotient → cofib (λ b → h (g b))
  transportThenRejoin x = After.rejoin (upper x)

  rejoinThenTransport : Before.Quotient → cofib (λ b → h (g b))
  rejoinThenTransport x = Lower.direct (Before.rejoin x)

  -- Full naturality: equality holds on the nested attachment square too,
  -- not just on the source points or one-dimensional attachments.
  rejoinSquare : (x : Before.Quotient) →
    transportThenRejoin x ≡ rejoinThenTransport x
  rejoinSquare (inl tt) = refl
  rejoinSquare (inr (inl tt)) = refl
  rejoinSquare (inr (inr c)) = refl
  rejoinSquare (inr (push a i)) = refl
  rejoinSquare (push (inl tt) i) = refl
  rejoinSquare (push (inr b) i) = refl
  rejoinSquare (push (push a j) i) = refl

  rejoinFunctionSquare : transportThenRejoin ≡ rejoinThenTransport
  rejoinFunctionSquare = funExt rejoinSquare

  cutSquare : (x : cofib g) →
    upper (Before.cut x) ≡ After.cut (Lower.direct x)
  cutSquare (inl tt) = refl
  cutSquare (inr c) = refl
  cutSquare (push b i) = refl

-- This direct rejoin equivalence is independently proved. Identification with
-- the earlier opaque 3x3/univalence-transported equivalence is not asserted.
-- In particular, Naturality.rejoinSquare is not passed off as an inhabitant
-- of the earlier RejoinNaturality.RejoinSquare, whose chosen maps differ.
