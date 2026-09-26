{-# OPTIONS --safe --cubical --guardedness #-}
module ResolutionNetTermination where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (ℕ; zero; suc; _+_)
open import Cubical.Data.Nat.Properties using (znots; injSuc)
import Cubical.Data.Empty as Empty
open import CoherenceResolutionClosure
open import ResolutionNetLocalSimulation

plus-zero : (n : ℕ) → n + zero ≡ n
plus-zero zero = refl
plus-zero (suc n) = cong suc (plus-zero n)
plus-suc : (n m : ℕ) → n + suc m ≡ suc (n + m)
plus-suc zero m = refl
plus-suc (suc n) m = cong suc (plus-suc n m)

module Termination {ℓ : Level}
  (P : Type ℓ) (U : P → P → Type ℓ) (V : P → P → P → Type ℓ)
  (S : P → Type ℓ) where
  open Closure P U V
  open Local P U V S

  outer-size : {p : P} → Resolve (Resolve S) p → ℕ
  outer-size (seed d) = suc zero
  outer-size (unary u d) = suc (outer-size d)
  outer-size (binary v d e) = suc (outer-size d + outer-size e)

  work : {p : P} → Term p → ℕ
  work (keep d) = zero
  work (pending d) = outer-size d
  work (one u t) = work t
  work (two v t w) = work t + work w

  step-work : {p : P} {t w : Term p} → t ↝ w → work t ≡ suc (work w)
  step-work (F-seed d) = refl
  step-work (F-unary u d) = refl
  step-work (F-binary v d e) = refl
  step-work (under-one u r) = step-work r
  step-work (under-left v w r) = cong (_+ work w) (step-work r)
  step-work (under-right v t r) = cong (work t +_) (step-work r) ∙ plus-suc (work t) _

  data Accessible {p : P} (t : Term p) : Type ℓ where
    access : ((w : Term p) → t ↝ w → Accessible w) → Accessible t

  accessible-by-work : (n : ℕ) {p : P} (t : Term p) → work t ≡ n → Accessible t
  accessible-by-work zero t eq = access λ w r → Empty.rec (znots (sym eq ∙ step-work r))
  accessible-by-work (suc n) t eq = access λ w r →
    accessible-by-work n w (injSuc (sym (step-work r) ∙ eq))

  all-schedules-terminate : {p : P} (t : Term p) → Accessible t
  all-schedules-terminate t = accessible-by-work (work t) t refl

  length : {p : P} {t w : Term p} → t ↠ w → ℕ
  length stop = zero
  length (more r rs) = suc (length rs)

  path-work : {p : P} {t w : Term p} (rs : t ↠ w)
            → work t ≡ length rs + work w
  path-work stop = refl
  path-work (more r rs) = step-work r ∙ cong suc (path-work rs)

  finished-zero : {p : P} {t : Term p} → Finished t → work t ≡ zero
  finished-zero (kept d) = refl
  finished-zero (one-finished u f) = finished-zero f
  finished-zero (two-finished v f g) = cong₂ _+_ (finished-zero f) (finished-zero g)

  exact-complete-length : {p : P} {t w : Term p} (rs : t ↠ w)
                        → Finished w → work t ≡ length rs
  exact-complete-length rs f = path-work rs ∙ cong (length rs +_) (finished-zero f) ∙ plus-zero (length rs)

  -- No abstract term is stuck while pending work remains.
  data Next {p : P} (t : Term p) : Type ℓ where
    halted : Finished t → Next t
    advances : {w : Term p} → t ↝ w → Next t

  progress : {p : P} (t : Term p) → Next t
  progress (keep d) = halted (kept d)
  progress (pending (seed d)) = advances (F-seed d)
  progress (pending (unary u d)) = advances (F-unary u d)
  progress (pending (binary v d e)) = advances (F-binary v d e)
  progress (one u t) with progress t
  ... | halted f = halted (one-finished u f)
  ... | advances r = advances (under-one u r)
  progress (two v t w) with progress t
  ... | advances r = advances (under-left v w r)
  ... | halted f with progress w
  ...   | advances r = advances (under-right v t r)
  ...   | halted g = halted (two-finished v f g)
