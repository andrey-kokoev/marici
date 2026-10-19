{-# OPTIONS --safe --cubical --guardedness #-}
module RetainedHistoryTransport where

open import Cubical.Foundations.Prelude
open import TypedGeneratorLayers using (Layer1; module Histories)
open import ComposableWitnessSpecialization using (Refinement; compile; compose; module Composite)

module Transport {ℓ : Level} {L : Layer1 ℓ}
  (F : Refinement L) (G : Refinement (compile F)) where
  module C = Composite F G
  module N = Layer1 (compile G)
  module K = Layer1 (compile (compose F G))
  module NH = Histories (compile G)
  module KH = Histories (compile (compose F G))

  forward : {s t : N.State} → NH.History s t
    → KH.History (C.flatten s) (C.flatten t)
  forward NH.empty = KH.empty
  forward (NH.link w h) = KH.link (C.flatten-edge w) (forward h)

  backward : {s t : K.State} → KH.History s t
    → NH.History (C.unflatten s) (C.unflatten t)
  backward KH.empty = NH.empty
  backward (KH.link w h) = NH.link (C.unflatten-edge w) (backward h)

  backward-forward : {s t : N.State} (h : NH.History s t)
    → backward (forward h) ≡ h
  backward-forward NH.empty = refl
  backward-forward (NH.link w h) = cong (NH.link w) (backward-forward h)

  forward-backward : {s t : K.State} (h : KH.History s t)
    → forward (backward h) ≡ h
  forward-backward KH.empty = refl
  forward-backward (KH.link w h) = cong (KH.link w) (forward-backward h)

  forward-join : {s t u : N.State}
    (h : NH.History s t) (k : NH.History t u)
    → forward (NH.join h k) ≡ KH.join (forward h) (forward k)
  forward-join NH.empty k = refl
  forward-join (NH.link w h) k = cong (KH.link (C.flatten-edge w)) (forward-join h k)

  backward-join : {s t u : K.State}
    (h : KH.History s t) (k : KH.History t u)
    → backward (KH.join h k) ≡ NH.join (backward h) (backward k)
  backward-join KH.empty k = refl
  backward-join (KH.link w h) k = cong (NH.link (C.unflatten-edge w)) (backward-join h k)

  next-square : (s : N.State) → C.flatten (N.next s) ≡ K.next (C.flatten s)
  next-square s = refl

  edge-square : (s : N.State) → C.flatten-edge (N.edge s) ≡ K.edge (C.flatten s)
  edge-square s = refl
