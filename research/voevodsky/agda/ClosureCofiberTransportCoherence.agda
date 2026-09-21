{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureCofiberTransportCoherence where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Function using (idfun)
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Univalence
open import Cubical.Data.Unit
open import Cubical.HITs.Pushout.Base
open import ClosureCofiberComposition

-- Fixed-source cofiber transport. This action is defined on the attachment
-- paths themselves. In contrast to the 3x3 implementation, it has no extra
-- reflexivity concatenations on those paths.
module Transport {A B C : Type} (f : A → B) (g : B → C) where
  direct : cofib f → cofib (λ a → g (f a))
  direct (inl tt) = inl tt
  direct (inr b) = inr (g b)
  direct (push a i) = push a i

  module Old = Composition A B C f g

  -- Comparison with the PREVIOUSLY constructed induced map, including the
  -- square on every attachment path. This is not an assumed normalization.
  normalize : (x : cofib f) → Old.induced x ≡ direct x
  normalize (inl tt) = refl
  normalize (inr b) = refl
  normalize (push a i) j = Old.induced-on-attachment a j i

  mapIdentification : Old.induced ≡ direct
  mapIdentification = funExt normalize

  -- The earlier equivalence remains available for this normalized map.
  -- This is transport of that specific theorem, not a new choice of filler.
  normalizedCofiberComposition : cofib direct ≃ cofib g
  normalizedCofiberComposition = compEquiv
    (pathToEquiv (sym (cong cofib mapIdentification)))
    Old.cofiberComposition

module Triple {A B C D : Type}
  (f : A → B) (g : B → C) (h : C → D) where

  module FG = Transport f g
  module GH = Transport (λ a → g (f a)) h
  module FGH = Transport f (λ b → h (g b))

  -- Two independent definitions: two HIT eliminations versus one.
  directComposition : (x : cofib f) →
    GH.direct (FG.direct x) ≡ FGH.direct x
  directComposition (inl tt) = refl
  directComposition (inr b) = refl
  directComposition (push a i) = refl

  -- The corresponding homotopy for the original 3x3 maps is not assumed
  -- strict. It is assembled from their explicit normalization squares.
  originalComposition : (x : cofib f) →
    GH.Old.induced (FG.Old.induced x) ≡ FGH.Old.induced x
  originalComposition x =
    cong GH.Old.induced (FG.normalize x)
    ∙ GH.normalize (FG.direct x)
    ∙ directComposition x
    ∙ sym (FGH.normalize x)

  originalFunctionComparison :
    (λ x → GH.Old.induced (FG.Old.induced x)) ≡ FGH.Old.induced
  originalFunctionComparison = funExt originalComposition

  -- The attachment-sensitive homotopy changes the presentation of the
  -- SAME second quotient. Univalence/transport must use this path, not a
  -- bare assertion that their source and target dimensions happen to match.
  compositeBoundaryCofibers :
    cofib (λ x → GH.Old.induced (FG.Old.induced x)) ≃
    cofib FGH.Old.induced
  compositeBoundaryCofibers =
    pathToEquiv (cong cofib originalFunctionComparison)

-- One higher compatibility for the normalized transports. There are two
-- ways to collapse three transport steps into one; their path witnesses agree.
module Quadruple {A B C D E : Type}
  (f : A → B) (g : B → C) (h : C → D) (k : D → E) where
  module FG = Transport f g
  module GH = Transport (λ a → g (f a)) h
  module HK = Transport (λ a → h (g (f a))) k
  module ALL = Transport f (λ b → k (h (g b)))

  left : (x : cofib f) →
    HK.direct (GH.direct (FG.direct x)) ≡ ALL.direct x
  left x =
    cong HK.direct (Triple.directComposition f g h x)
    ∙ Triple.directComposition f (λ b → h (g b)) k x

  right : (x : cofib f) →
    HK.direct (GH.direct (FG.direct x)) ≡ ALL.direct x
  right x =
    Triple.directComposition (λ a → g (f a)) h k (FG.direct x)
    ∙ Triple.directComposition f g (λ c → k (h c)) x

  comparisonOfComparisons : (x : cofib f) → left x ≡ right x
  comparisonOfComparisons (inl tt) = refl
  comparisonOfComparisons (inr b) = refl
  comparisonOfComparisons (push a i) = refl

-- The exact remaining rejoin comparison, with BOTH maps constructed from
-- the previous theorem. Merely naming this type is not a proof of inhabitance.
module RejoinNaturality {A B C D : Type}
  (f : A → B) (g : B → C) (h : C → D) where
  module P = Transport f g
  module Q = Transport (λ a → g (f a)) h
  module R = Transport f (λ b → h (g b))
  module Upper = Transport P.direct Q.direct
  module Lower = Transport g h

  boundaryAdjustment :
    cofib (λ x → Q.direct (P.direct x)) ≃ cofib R.direct
  boundaryAdjustment = pathToEquiv
    (cong cofib (funExt (Triple.directComposition f g h)))

  transportThenRejoin : cofib P.direct → cofib (λ b → h (g b))
  transportThenRejoin x = equivFun R.normalizedCofiberComposition
    (equivFun boundaryAdjustment (Upper.direct x))

  rejoinThenTransport : cofib P.direct → cofib (λ b → h (g b))
  rejoinThenTransport x = Lower.direct
    (equivFun P.normalizedCofiberComposition x)

  RejoinSquare : Type
  RejoinSquare = (x : cofib P.direct) →
    transportThenRejoin x ≡ rejoinThenTransport x

-- This module constructs boundary triangles and a higher compatibility for
-- normalized fixed-source transports. It does not yet prove the higher
-- comparison between the TWO complete cofiberComposition/rejoin assemblies.
