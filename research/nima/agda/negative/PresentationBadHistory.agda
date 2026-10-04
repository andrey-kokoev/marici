{-# OPTIONS --safe --cubical --guardedness #-}
module PresentationBadHistory where
open import Cubical.Foundations.Prelude
open import TypedGeneratorPresentation
open Controls

-- The equal output scores do not make the compacted history marks equal.
bad : MB.is-empty (fst (Q.compact idle)) ≡ MB.is-empty (fst (Q.compact twice))
bad = refl
