{-# OPTIONS --safe --cubical --guardedness #-}
module NativeFeedbackFixedPointBridge where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty.Base using (⊥)
import AgreementPolicyBoundary as Source
module F = Source.F
module N = Source.N

-- A decoder-only readout cannot distinguish this source exchange. This does
-- not erase the retained records: the existing proof shows they differ.
module PayloadOnly {ℓ : Level} (Y : Type ℓ) (read : F.V.View → Y) where
  observed : N.Compared → Y
  observed c = read (F.decode-initial c)
  exchange-invisible : (c : N.Compared) → observed (F.F.exchange c) ≡ observed c
  exchange-invisible c = refl

-- If a proposed dynamics adapter starts the actual comparison at a fixed
-- target state and intertwines exchange, its first two source records MUST
-- have identical numerical images. It cannot be injective on this pair.
module FixedImage {ℓ : Level} (Y : Type ℓ) (update : Y → Y)
  (y : Y) (fixed : update y ≡ y)
  (encode : N.Compared → Y)
  (initial : encode Source.comparison ≡ y)
  (intertwines : (c : N.Compared) → encode (F.F.exchange c) ≡ update (encode c)) where

  next-image : encode (F.F.exchange Source.comparison) ≡ y
  next-image = intertwines Source.comparison ∙ cong update initial ∙ fixed

  images-agree : encode (F.F.exchange Source.comparison) ≡ encode Source.comparison
  images-agree = next-image ∙ sym initial

  not-injective :
    ((c d : N.Compared) → encode c ≡ encode d → c ≡ d) → ⊥
  not-injective faithful = Source.record-changes
    (faithful (F.F.exchange Source.comparison) Source.comparison images-agree)
