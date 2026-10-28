{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyEdgeAttachmentsBadParent where
open import Cubical.Foundations.Prelude
open import RamseyEdgeAttachmentsExamples
bad : fst att-0-2-4 ≡ fst att-0-0-4
bad = refl
