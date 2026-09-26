{-# OPTIONS --safe --cubical --guardedness #-}
module ResolutionNetLocalSimulation where

open import Cubical.Foundations.Prelude
open import CoherenceResolutionClosure

module Local {ℓ : Level}
  (P : Type ℓ) (U : P → P → Type ℓ) (V : P → P → P → Type ℓ)
  (S : P → Type ℓ) where
  open Closure P U V

  -- keep denotes an already pure retained subnet. pending's argument is pure:
  -- nested operational F regions and shared port graphs are not encoded here.
  data Term : P → Type ℓ where
    keep : {p : P} → Resolve S p → Term p
    pending : {p : P} → Resolve (Resolve S) p → Term p
    one : {p q : P} → U p q → Term p → Term q
    two : {p q r : P} → V p q r → Term p → Term q → Term r

  interpret : {p : P} → Term p → Resolve S p
  interpret (keep d) = d
  interpret (pending d) = flatten d
  interpret (one u t) = unary u (interpret t)
  interpret (two v t w) = binary v (interpret t) (interpret w)

  infix 20 _↝_ _↠_
  data _↝_ : {p : P} → Term p → Term p → Type ℓ where
    F-seed : {p : P} (d : Resolve S p) → pending (seed d) ↝ keep d
    F-unary : {p q : P} (u : U p q) (d : Resolve (Resolve S) p)
            → pending (unary u d) ↝ one u (pending d)
    F-binary : {p q r : P} (v : V p q r)
               (d : Resolve (Resolve S) p) (e : Resolve (Resolve S) q)
             → pending (binary v d e) ↝ two v (pending d) (pending e)
    under-one : {p q : P} {t t' : Term p} (u : U p q)
              → t ↝ t' → one u t ↝ one u t'
    under-left : {p q r : P} {t t' : Term p} (v : V p q r) (w : Term q)
               → t ↝ t' → two v t w ↝ two v t' w
    under-right : {p q r : P} (v : V p q r) (t : Term p) {w w' : Term q}
                → w ↝ w' → two v t w ↝ two v t w'

  step-sound : {p : P} {t w : Term p} → t ↝ w → interpret t ≡ interpret w
  step-sound (F-seed d) = refl
  step-sound (F-unary u d) = refl
  step-sound (F-binary v d e) = refl
  step-sound (under-one u r) = cong (unary u) (step-sound r)
  step-sound (under-left v w r) = cong (λ d → binary v d (interpret w)) (step-sound r)
  step-sound (under-right v t r) = cong (binary v (interpret t)) (step-sound r)

  data _↠_ : {p : P} → Term p → Term p → Type ℓ where
    stop : {p : P} {t : Term p} → t ↠ t
    more : {p : P} {t u w : Term p} → t ↝ u → u ↠ w → t ↠ w

  path-sound : {p : P} {t w : Term p} → t ↠ w → interpret t ≡ interpret w
  path-sound stop = refl
  path-sound (more r rs) = step-sound r ∙ path-sound rs

  append : {p : P} {t u w : Term p} → t ↠ u → u ↠ w → t ↠ w
  append stop rs = rs
  append (more r rs) ss = more r (append rs ss)

  lift-one : {p q : P} (u : U p q) {t w : Term p}
           → t ↠ w → one u t ↠ one u w
  lift-one u stop = stop
  lift-one u (more r rs) = more (under-one u r) (lift-one u rs)

  lift-left : {p q r : P} (v : V p q r) (w : Term q) {t t' : Term p}
            → t ↠ t' → two v t w ↠ two v t' w
  lift-left v w stop = stop
  lift-left v w (more r rs) = more (under-left v w r) (lift-left v w rs)

  lift-right : {p q r : P} (v : V p q r) (t : Term p) {w w' : Term q}
             → w ↠ w' → two v t w ↠ two v t w'
  lift-right v t stop = stop
  lift-right v t (more r rs) = more (under-right v t r) (lift-right v t rs)

  settle : {p : P} → Resolve (Resolve S) p → Term p
  settle (seed d) = keep d
  settle (unary u d) = one u (settle d)
  settle (binary v d e) = two v (settle d) (settle e)

  settle-path : {p : P} (d : Resolve (Resolve S) p) → pending d ↠ settle d
  settle-path (seed d) = more (F-seed d) stop
  settle-path (unary u d) = more (F-unary u d) (lift-one u (settle-path d))
  settle-path (binary v d e) = more (F-binary v d e)
    (append (lift-left v (pending e) (settle-path d))
            (lift-right v (settle d) (settle-path e)))

  data Finished : {p : P} → Term p → Type ℓ where
    kept : {p : P} (d : Resolve S p) → Finished (keep d)
    one-finished : {p q : P} (u : U p q) {t : Term p}
                 → Finished t → Finished (one u t)
    two-finished : {p q r : P} (v : V p q r) {t : Term p} {w : Term q}
                 → Finished t → Finished w → Finished (two v t w)

  settle-finished : {p : P} (d : Resolve (Resolve S) p) → Finished (settle d)
  settle-finished (seed d) = kept d
  settle-finished (unary u d) = one-finished u (settle-finished d)
  settle-finished (binary v d e) = two-finished v (settle-finished d) (settle-finished e)

  settle-correct : {p : P} (d : Resolve (Resolve S) p)
                 → flatten d ≡ interpret (settle d)
  settle-correct d = path-sound (settle-path d)
