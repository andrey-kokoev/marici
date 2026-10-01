{-# OPTIONS --safe --cubical --guardedness #-}
module TriangleComparisonFeedbackRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (true≢false)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Nat.Base using (ℕ; suc)
import WholePackageSigmaPi as Whole
import NativeNormalizationRouteCompiler as Native
import ThreeRecordTriangleRegression as Seed

-- Chosen feedback law: previous comparisons become the data acted upon by the
-- next triangle. Exchange the two retained routes, then exchange them again;
-- compare this route with the direct identity on the entire previous record.
module Feedback (ℓ : Level) (Q : Whole.Universe.Code ℓ) where
  module Previous = Native.Compiler ℓ Q
  open Previous.Compared

  exchange : Previous.Compared → Previous.Compared
  exchange r = Previous.compared-native (source r) (target r)
    (second r) (first r) (input-value r)
    (second-native r) (first-native r)
    (second-boundaries r) (first-boundaries r) (sym (effect-witness r))

  exchange-twice : (r : Previous.Compared) → exchange (exchange r) ≡ r
  exchange-twice r = refl
  exchangeIso : Iso Previous.Compared Previous.Compared
  Iso.fun exchangeIso = exchange
  Iso.inv exchangeIso = exchange
  Iso.rightInv exchangeIso = exchange-twice
  Iso.leftInv exchangeIso = exchange-twice

  module Next = Native.Compiler (ℓ-suc ℓ) (Whole.Universe.atom Previous.Compared)
  module H = Next.H
  R = Whole.Universe.atom Previous.Compared
  A = H.original
  B = H.advance A R (isoToEquiv exchangeIso)
  C = H.advance B R (isoToEquiv exchangeIso)
  ab = H.advance-map A R (isoToEquiv exchangeIso)
  bc = H.advance-map B R (isoToEquiv exchangeIso)
  -- The composite is definitionally identity on the full prior comparison,
  -- including its two route histories and its comparison witness.
  ac : H.CoherentMap A C
  ac r = r , snd (H.compose {P = A} {R = B} {T = C} ab bc r)
  direct : H.Route A C
  direct = H.next {P = A} {R = C} {T = C} ac (H.stop {P = C})
  via : H.Route A C
  via = H.next {P = A} {R = B} {T = C} ab
    (H.next {P = B} {R = C} {T = C} bc (H.stop {P = C}))

  steps : {P T : H.Presentation} → H.Route P T → ℕ
  steps H.stop = 0
  steps (H.next f tail) = suc (steps tail)
  direct-one : steps direct ≡ 1
  direct-one = refl
  via-two : steps via ≡ 2
  via-two = refl
  distinct-routes : direct ≡ via → ⊥
  distinct-routes p = true≢false (cong (λ t → Seed.is-one (steps t)) p)
  same-effect : (r : Previous.Compared) → Next.execute via r ≡ Next.execute direct r
  same-effect r = refl

  decode : Next.Compared → Previous.Compared
  decode r = H.N.reconstruct R
    (equivFun (H.Presentation.coordinates (Next.Compared.source r))
      (Next.Compared.input-value r))

  -- Seal checked compilations to avoid repeatedly normalizing their complete
  -- proof trees when composing the next cycle's preservation theorem.
  abstract
    run : Previous.Compared → Next.Compared
    run = Next.compare-compilations direct via
    decode-run : (r : Previous.Compared) → decode (run r) ≡ r
    decode-run r = refl
    run-injective : (r s : Previous.Compared) → run r ≡ run s → r ≡ s
    run-injective r s p = cong decode p

  promoted : Previous.Compared → Whole.Universe.Complete (ℓ-suc (ℓ-suc ℓ))
  promoted r = Next.next-comparison-Q (run r)
  direct-certified = Next.compile-leaves direct
  via-certified = Next.compile-leaves via

module F1 = Feedback ℓ-zero (Whole.Universe.atom Seed.ARecord)
module F2 = Feedback (ℓ-suc ℓ-zero) (Whole.Universe.atom F1.Previous.Compared)

-- Cycle1 is the original three-record comparison. Cycles2..3 feed the exact
-- promoted payload into the next relationship construction.
cycle1 : Seed.ARecord → Seed.N.Compared
cycle1 = Seed.compared
cycle2 : Seed.ARecord → F1.Next.Compared
cycle2 x = F1.run (Whole.Universe.value (Seed.next-input x))
cycle3 : Seed.ARecord → F2.Next.Compared
cycle3 x = F2.run (Whole.Universe.value (F1.promoted (cycle1 x)))

recover-seed : F2.Next.Compared → Seed.N.Compared
recover-seed r = F1.decode (F2.decode r)
original-comparison-retained : (x : Seed.ARecord) → recover-seed (cycle3 x) ≡ cycle1 x
original-comparison-retained x =
  cong F1.decode (F2.decode-run (cycle2 x)) ∙ F1.decode-run (cycle1 x)
previous2-recovered : (x : Seed.ARecord)
  → F2.decode (cycle3 x) ≡ cycle2 x
previous2-recovered x = F2.decode-run (cycle2 x)

-- The first exchange actually changes the order of the unequal seed histories.
first-after-exchange : (x : Seed.ARecord)
  → Seed.steps (Seed.N.Compared.first (F1.exchange (cycle1 x))) ≡ 2
first-after-exchange x = refl
first-before-exchange : (x : Seed.ARecord)
  → Seed.steps (Seed.N.Compared.first (cycle1 x)) ≡ 1
first-before-exchange x = refl
exchange-is-nontrivial : (x : Seed.ARecord) → F1.exchange (cycle1 x) ≡ cycle1 x → ⊥
exchange-is-nontrivial x p = true≢false
  (sym (cong (λ r → Seed.is-one (Seed.steps (Seed.N.Compared.first r))) p))

-- Full original comparison recovery includes both distinct seed histories.
recover-initial : Seed.N.Compared → Seed.ARecord
recover-initial r = Seed.H.N.reconstruct (Whole.Universe.atom Seed.ARecord)
  (equivFun (Seed.H.Presentation.coordinates (Seed.N.Compared.source r))
    (Seed.N.Compared.input-value r))
recover-value : F2.Next.Compared → Seed.ARecord
recover-value r = recover-initial (recover-seed r)
recover-value-correct : (x : Seed.ARecord) → recover-value (cycle3 x) ≡ x
recover-value-correct x = cong recover-initial (original-comparison-retained x)
three-cycle-injective : (x y : Seed.ARecord) → cycle3 x ≡ cycle3 y → x ≡ y
three-cycle-injective x y p = sym (recover-value-correct x)
  ∙ cong recover-value p ∙ recover-value-correct y

-- An attempted feedback that resets input1 to input0 fails ancestry preservation.
seed-bit : Seed.ARecord → Bool
seed-bit (Seed.a x) = x
reset-loses-input : recover-value (cycle3 (Seed.a false)) ≡ Seed.a true → ⊥
reset-loses-input p = true≢false
  (sym (cong seed-bit (sym (recover-value-correct (Seed.a false)) ∙ p)))

output0 : F2.Next.Compared
output0 = cycle3 (Seed.a false)
output1 : F2.Next.Compared
output1 = cycle3 (Seed.a true)
