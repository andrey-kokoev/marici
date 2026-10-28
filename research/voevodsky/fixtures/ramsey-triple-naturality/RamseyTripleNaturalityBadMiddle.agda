{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyTripleNaturalityBadMiddle where
open import Cubical.Foundations.Prelude
open import RamseyNativeEdgeAttachments using (e02)
open import RamseyEndpointPolicy using (base)
import RamseyEdgeAttachmentsExamples as E
open import RamseyTripleNaturality
bad : edge-triple base base base middle-witness ≡ (e02 , (E.att-7-1-1 , (E.att-7-1-1 , E.att-7-1-1)))
bad = refl
