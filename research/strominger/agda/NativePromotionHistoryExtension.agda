{-# OPTIONS --safe --cubical --guardedness #-}
module NativePromotionHistoryExtension where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false; true; not)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import Cubical.Data.Empty.Base using (⊥)
open import TypedGeneratorLayers using (Layer1; module Histories)
import NativePacketPromotionBinding as P
import NativePromotionCertifiedImage as C

module A = P.A
module G = P.G

level = ℓ-suc (ℓ-suc (ℓ-suc ℓ-zero))

exchange-WG : Layer1 level
exchange-WG = record
  { State = A.Compared
  ; Witness = λ s t → t ≡ G.exchange s
  ; generate = λ s → G.exchange s , refl }
module H = Histories exchange-WG

-- Original certified packet + current target + full existing history type.
Extended : Type level
Extended = Σ[ seed ∈ C.Generated ] Σ[ y ∈ A.Compared ] H.History (C.view seed) y

start : C.Generated → Extended
start seed = seed , C.view seed , H.empty
current : Extended → A.Compared
current x = fst (snd x)
origin : Extended → P.B.Compared
origin x = C.origin (fst x)
steps : Extended → ℕ
steps x = H.length (snd (snd x))

advance : Extended → Extended
advance (seed , y , h) = seed , G.exchange y , H.join h (H.single refl)

origin-preserved : (x : Extended) → origin (advance x) ≡ origin x
origin-preserved x = refl
seed-preserved : (x : Extended) → fst (advance x) ≡ fst x
seed-preserved x = refl
view-exchange : (x : Extended) → current (advance x) ≡ G.exchange (current x)
view-exchange x = refl

-- Any further supplied exchange history is admitted with the same seed.
continue : (x : Extended) {z : A.Compared} → H.History (current x) z → Extended
continue (seed , y , h) {z} k = seed , z , H.join h k
continue-associative : (x : Extended) {z w : A.Compared}
  (h : H.History (current x) z) (k : H.History z w)
  → continue (continue x h) k ≡ continue x (H.join h k)
continue-associative (seed , y , old) {z} {w} h k =
  cong (λ trace → seed , w , trace) (H.associative old h k)

-- Explicit bookkeeping phase of this chosen involutive action, not an
-- identification with the operator's conceptual phases or rung grades.
history-phase : {s t : A.Compared} → H.History s t → Bool
history-phase H.empty = false
history-phase (H.link w h) = not (history-phase h)
phase : Extended → Bool
phase x = history-phase (snd (snd x))

initial : Extended
initial = start (C.pack (P.source false))
once : Extended
once = advance initial
twice : Extended
twice = advance once

once-outside : (c : P.B.Compared) → P.F.run c ≡ current once → ⊥
once-outside = P.outside-image

two-step-view-return : current twice ≡ current initial
two-step-view-return = G.exchange-twice (current initial)

two-step-origin-return : origin twice ≡ origin initial
two-step-origin-return = refl
phase-one : phase once ≡ true
phase-one = refl
phase-two : phase twice ≡ false
phase-two = refl
length-two : steps twice ≡ 2
length-two = refl

is-zero : ℕ → Bool
is-zero zero = true
is-zero (suc n) = false

-- Returning view, source and parity does not erase a performed history.
no-history-erasure : twice ≡ initial → ⊥
no-history-erasure p = false≢true (cong (λ x → is-zero (steps x)) p)

-- Enlarging the context is necessary: no map back into the old certified
-- image can preserve every current view, because it would have to hit once.
no-view-preserving-normalizer : (normalize : Extended → C.Generated)
  → ((x : Extended) → C.view (normalize x) ≡ current x) → ⊥
no-view-preserving-normalizer normalize law = once-outside
  (C.origin (normalize once)) (C.certificate (normalize once) ∙ law once)

-- The complete extended construction itself supports a WG action.
WG : Layer1 level
WG = record
  { State = Extended
  ; Witness = λ x y → y ≡ advance x
  ; generate = λ x → advance x , refl }
