{-# OPTIONS --safe --cubical --guardedness #-}
module ThreeRecordTriangleRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (true≢false)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Nat.Base using (ℕ; suc)
import WholePackageSigmaPi as Whole
import NativeNormalizationRouteCompiler as Native

-- Three distinct record presentations, each carrying a binary payload.
-- The links are supplied explicitly: AB flips, BC flips, AC preserves.
data ARecord : Type where
  a : Bool → ARecord
data BRecord : Type where
  b : Bool → BRecord
data CRecord : Type where
  c : Bool → CRecord

flip : Bool → Bool
flip false = true
flip true = false
flip-twice : (x : Bool) → flip (flip x) ≡ x
flip-twice false = refl
flip-twice true = refl

abIso : Iso ARecord BRecord
Iso.fun abIso (a x) = b (flip x)
Iso.inv abIso (b x) = a (flip x)
Iso.rightInv abIso (b x) = cong b (flip-twice x)
Iso.leftInv abIso (a x) = cong a (flip-twice x)
bcIso : Iso BRecord CRecord
Iso.fun bcIso (b x) = c (flip x)
Iso.inv bcIso (c x) = b (flip x)
Iso.rightInv bcIso (c x) = cong c (flip-twice x)
Iso.leftInv bcIso (b x) = cong b (flip-twice x)

open Whole.Universe ℓ-zero
module N = Native.Compiler ℓ-zero (atom ARecord)
module H = N.H
A = H.original
B = H.advance A (atom BRecord) (isoToEquiv abIso)
C = H.advance B (atom CRecord) (isoToEquiv bcIso)
ab = H.advance-map A (atom BRecord) (isoToEquiv abIso)
bc = H.advance-map B (atom CRecord) (isoToEquiv bcIso)

raw-ac : ARecord → CRecord
raw-ac (a x) = c x
composed-output : (x : ARecord)
  → fst (H.compose {P = A} {R = B} {T = C} ab bc x) ≡ raw-ac x
composed-output (a x) = cong c (flip-twice x)

-- Admit the independently written direct link only after checking its effect.
ac : H.CoherentMap A C
ac x = raw-ac x ,
  (cong (equivFun (H.Presentation.coordinates C)) (sym (composed-output x))
    ∙ snd (H.compose {P = A} {R = B} {T = C} ab bc x))

direct : H.Route A C
direct = H.next {P = A} {R = C} {T = C} ac (H.stop {P = C})
via : H.Route A C
via = H.next {P = A} {R = B} {T = C} ab
  (H.next {P = B} {R = C} {T = C} bc (H.stop {P = C}))

steps : {P R : H.Presentation} → H.Route P R → ℕ
steps H.stop = 0
steps (H.next f rest) = suc (steps rest)
direct-length : steps direct ≡ 1
direct-length = refl
via-length : steps via ≡ 2
via-length = refl
same-outcome : (x : ARecord) → N.execute via x ≡ N.execute direct x
same-outcome (a x) = cong c (flip-twice x)
compiler-same-outcome : (x : ARecord) → N.execute via x ≡ N.execute direct x
compiler-same-outcome = N.effects-agree via direct

is-one : ℕ → Bool
is-one 0 = false
is-one (suc 0) = true
is-one (suc (suc n)) = false
distinct-routes : direct ≡ via → ⊥
distinct-routes p = true≢false (cong (λ r → is-one (steps r)) p)

compiled-direct = N.compile direct
compiled-via = N.compile via
certified-direct = N.compile-leaves direct
certified-via = N.compile-leaves via
compared = N.compare-compilations direct via
promoted = N.next-comparison-Q
next-input : ARecord → Whole.Universe.Complete (ℓ-suc ℓ-zero)
next-input x = promoted (compared x)

retains-direct : (x : ARecord)
  → N.Compared.first (Whole.Universe.value (next-input x)) ≡ direct
retains-direct x = refl
retains-via : (x : ARecord)
  → N.Compared.second (Whole.Universe.value (next-input x)) ≡ via
retains-via x = refl
retained-routes-distinct : (x : ARecord)
  → N.Compared.first (Whole.Universe.value (next-input x))
    ≡ N.Compared.second (Whole.Universe.value (next-input x)) → ⊥
retained-routes-distinct x = distinct-routes

-- Run the promoted triangle comparison through the same native compiler again.
-- This second route is explicitly normalization followed by reconstruction.
module Next = Native.Compiler (ℓ-suc ℓ-zero)
  (Whole.Universe.atom N.Compared)
module J = Next.H
next-route : J.Route J.original J.original
next-route = J.next {P = J.original} {R = J.normal} {T = J.original}
  J.normalize-map
  (J.next {P = J.normal} {R = J.original} {T = J.original}
    J.reconstruct-map (J.stop {P = J.original}))
second-cycle : ARecord → Next.Retained
second-cycle x = Next.retain-compilation next-route
  (Whole.Universe.value (next-input x))
previous-comparison-is-input : (x : ARecord)
  → Next.Retained.input-value (second-cycle x) ≡ compared x
previous-comparison-is-input x = refl
routes-survive-second-cycle : (x : ARecord)
  → N.Compared.first (Next.Retained.input-value (second-cycle x))
    ≡ N.Compared.second (Next.Retained.input-value (second-cycle x)) → ⊥
routes-survive-second-cycle x = distinct-routes

-- A hostile direct link has a different effect and cannot satisfy the same
-- comparison. This is checked before giving it a CoherentMap certificate.
bad-ac : ARecord → CRecord
bad-ac (a x) = c (flip x)
payload : CRecord → Bool
payload (c x) = x
bad-direct-disagrees : bad-ac (a false) ≡ N.execute via (a false) → ⊥
bad-direct-disagrees p = true≢false (cong payload p)

bad-link-cannot-be-admitted : (f : H.CoherentMap A C)
  → ((x : ARecord) → fst (f x) ≡ bad-ac x) → ⊥
bad-link-cannot-be-admitted f supplied = bad-direct-disagrees
  (sym (supplied (a false))
    ∙ cong (λ g → fst (g (a false))) (H.compare-maps {P = A} {R = C} f ac))

-- Both binary inputs are exercised; each produces one joint comparison record.
triangle0 = second-cycle (a false)
triangle1 = second-cycle (a true)
