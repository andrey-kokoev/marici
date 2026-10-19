{-# OPTIONS --safe --cubical --guardedness #-}
module NativePacketPromotionBinding where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (true≢false)
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import Cubical.Data.Empty.Base using (⊥)
import NativePromotionConstructorTrace as T
import NativeFeedbackRouteReadout as S
import WholePackageSigmaPi as W

module F = T.F
module B = T.Before
module A = T.After
module G = T.G

-- Two actual views generated from the admitted input by the existing exchange.
-- This is a chosen two-branch family, not all possible continuations.
source : Bool → B.Compared
source false = T.input
source true = F.exchange T.input

target : Bool → A.Compared
target i = F.run (source i)

recover-port : (i : Bool) → F.decode (target i) ≡ source i
recover-port i = F.decode-run (source i)

-- Whole-family action and exact retraction; no inverse of run is assumed.
move : (Bool → B.Compared) → (Bool → A.Compared)
move x i = F.run (x i)
recover : (Bool → A.Compared) → (Bool → B.Compared)
recover y i = F.decode (y i)

recover-move : (x : Bool → B.Compared) → recover (move x) ≡ x
recover-move x = funExt (λ i → F.decode-run (x i))

generated-target : move source ≡ target
generated-target = refl

inherited-question : (i : Bool)
  → T.inherited-question (target i) ≡ S.reading (source i)
inherited-question i = T.question-square (source i)

branches-stay-distinct : T.inherited-question (target true)
  ≡ T.inherited-question (target false) → ⊥
branches-stay-distinct = T.inherited-distinction

-- Feed each actual generated packet into the existing next native constructor.
next-target : Bool → G.Next.Compared
next-target i = G.run (target i)

next-recovers : (i : Bool) → G.decode (next-target i) ≡ target i
next-recovers i = G.decode-run (target i)

-- Whole output packets retain the exact native result as their selected value.
packed : (i : Bool) → W.Universe.Complete (ℓ-suc (ℓ-suc (ℓ-suc ℓ-zero)))
packed i = F.promoted (source i)

packed-value : (i : Bool) → W.Universe.value (packed i) ≡ target i
packed-value i = refl

-- run has a proper image in the full next comparison type. A valid exchanged
-- next comparison has first-route length2; every run result has length1.
first-length : A.Compared → ℕ
first-length c = F.steps (A.Compared.first c)

outside : A.Compared
outside = G.exchange (F.run T.input)

outside-first-length : first-length outside ≡ 2
outside-first-length = F.run-second-steps T.input

is-one : ℕ → Bool
is-one (suc zero) = true
is-one _ = false

one-not-two : 1 ≡ 2 → ⊥
one-not-two p = true≢false (cong is-one p)

outside-image : (c : B.Compared) → F.run c ≡ outside → ⊥
outside-image c p = one-not-two
  (sym (F.run-first-steps c) ∙ cong first-length p ∙ outside-first-length)

-- A global right inverse of this PARTICULAR run would hit outside.
no-right-inverse : (back : A.Compared → B.Compared)
  → ((y : A.Compared) → F.run (back y) ≡ y) → ⊥
no-right-inverse back law = outside-image (back outside) (law outside)
