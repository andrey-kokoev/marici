{-# OPTIONS --safe --cubical --guardedness #-}
module DependentTransportMachine where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Transport using (substComposite)
open import Cubical.Foundations.Univalence using (uaβ)
open import Cubical.Data.Bool.Base using (Bool; true; false; not)
open import Cubical.Data.Bool.Properties using (notEquiv; true≢false; isSetBool)
open import Cubical.Data.Sigma.Properties using (Σ≡Prop)
open import Cubical.Foundations.HLevels using (isPropIsContr)
open import Cubical.Data.Empty.Base using (⊥)
import IndexIdentityCoherenceRegression as C
import IndexIdentityCoherence as I
open I.Indexed ℓ-zero using (Fibre)

-- Companion extension of the dependent-machine experiment: all routes have
-- the SAME endpoints, but their syntax and transport actions are retained.
-- Constructors contain no host-language function callbacks.
data Route (V : Type) : Type where
  slot : V → Route V
  stay turn : Route V
  follow : Route V → Route V → Route V

data Term (V : Type) : Type where
  bit : Bool → Term V
  carry : Route V → Term V → Term V

plug : {V W : Type} → (V → Route W) → Route V → Route W
plug σ (slot v) = σ v
plug σ stay = stay
plug σ turn = turn
plug σ (follow p q) = follow (plug σ p) (plug σ q)

plug-term : {V W : Type} → (V → Route W) → Term V → Term W
plug-term σ (bit b) = bit b
plug-term σ (carry p t) = carry (plug σ p) (plug-term σ t)

plug-id : {V : Type} (p : Route V) → plug slot p ≡ p
plug-id (slot v) = refl
plug-id stay = refl
plug-id turn = refl
plug-id (follow p q) = cong₂ follow (plug-id p) (plug-id q)

plug-compose : {V W X : Type} (σ : V → Route W) (τ : W → Route X)
  (p : Route V) → plug τ (plug σ p) ≡ plug (λ v → plug τ (σ v)) p
plug-compose σ τ (slot v) = refl
plug-compose σ τ stay = refl
plug-compose σ τ turn = refl
plug-compose σ τ (follow p q) = cong₂ follow (plug-compose σ τ p) (plug-compose σ τ q)

plug-term-id : {V : Type} (t : Term V) → plug-term slot t ≡ t
plug-term-id (bit b) = refl
plug-term-id (carry p t) = cong₂ carry (plug-id p) (plug-term-id t)

plug-term-compose : {V W X : Type} (σ : V → Route W) (τ : W → Route X)
  (t : Term V) → plug-term τ (plug-term σ t) ≡ plug-term (λ v → plug τ (σ v)) t
plug-term-compose σ τ (bit b) = refl
plug-term-compose σ τ (carry p t) = cong₂ carry (plug-compose σ τ p) (plug-term-compose σ τ t)

-- Directed execution is defined BEFORE, and independently of, interpretation.
data Step {V : Type} : Term V → Term V → Type where
  idle : (t : Term V) → Step (carry stay t) t
  flip-bit : (b : Bool) → Step (carry turn (bit b)) (bit (not b))
  split : (p q : Route V) (t : Term V)
    → Step (carry (follow p q) t) (carry q (carry p t))
  under : (p : Route V) {t u : Term V} → Step t u → Step (carry p t) (carry p u)

plug-step : {V W : Type} (σ : V → Route W) {t u : Term V}
  → Step t u → Step (plug-term σ t) (plug-term σ u)
plug-step σ (idle t) = idle (plug-term σ t)
plug-step σ (flip-bit b) = flip-bit b
plug-step σ (split p q t) = split (plug σ p) (plug σ q) (plug-term σ t)
plug-step σ (under p s) = under (plug σ p) (plug-step σ s)

data Progress (t : Term ⊥) : Type where
  done : (b : Bool) → t ≡ bit b → Progress t
  next : {u : Term ⊥} → Step t u → Progress t

progress : (t : Term ⊥) → Progress t
progress (bit b) = done b refl
progress (carry (slot ()) t)
progress (carry stay t) = next (idle t)
progress (carry (follow p q) t) = next (split p q t)
progress (carry turn (bit b)) = next (flip-bit b)
progress (carry turn t@(carry p u)) with progress t
... | done b eq = next (subst (λ v → Step (carry turn v) (bit (not b))) (sym eq) (flip-bit b))
... | next s = next (under turn s)

run-route : Route ⊥ → Bool → Bool
run-route (slot ()) b
run-route stay b = b
run-route turn b = not b
run-route (follow p q) b = run-route q (run-route p b)

run : Term ⊥ → Bool
run (bit b) = b
run (carry p t) = run-route p (run t)

-- A computed finite execution trace for EVERY closed term.
data Steps {V : Type} : Term V → Term V → Type where
  stop : {t : Term V} → Steps t t
  more : {t u v : Term V} → Step t u → Steps u v → Steps t v

append : {V : Type} {t u v : Term V} → Steps t u → Steps u v → Steps t v
append stop ys = ys
append (more x xs) ys = more x (append xs ys)

lift-steps : {V : Type} (p : Route V) {t u : Term V}
  → Steps t u → Steps (carry p t) (carry p u)
lift-steps p stop = stop
lift-steps p (more x xs) = more (under p x) (lift-steps p xs)

route-normalizes : (p : Route ⊥) (b : Bool)
  → Steps (carry p (bit b)) (bit (run-route p b))
route-normalizes (slot ()) b
route-normalizes stay b = more (idle (bit b)) stop
route-normalizes turn b = more (flip-bit b) stop
route-normalizes (follow p q) b = more (split p q (bit b))
  (append (lift-steps q (route-normalizes p b)) (route-normalizes q (run-route p b)))

normalizes : (t : Term ⊥) → Steps t (bit (run t))
normalizes (bit b) = stop
normalizes (carry p t) = append (lift-steps p (normalizes t)) (route-normalizes p (run t))

-- Semantic interpretation into the already checked circle double cover.
Loop : Type
Loop = C.base-index ≡ C.base-index

path : {V : Type} → Route V → (V → Loop) → Loop
path (slot v) ρ = ρ v
path stay ρ = refl
path turn ρ = C.index-loop
path (follow p q) ρ = path p ρ ∙ path q ρ

interpret : {V : Type} → Term V → (V → Loop) → Bool
interpret (bit b) ρ = b
interpret (carry p t) ρ = subst (Fibre C.F) (path p ρ) (interpret t ρ)

turn-sound : (b : Bool) → subst (Fibre C.F) C.index-loop b ≡ not b
turn-sound b = uaβ notEquiv b

step-sound : {V : Type} {t u : Term V} → Step t u
  → (ρ : V → Loop) → interpret t ρ ≡ interpret u ρ
step-sound (idle t) ρ = substRefl {B = Fibre C.F} {x = C.base-index} (interpret t ρ)
step-sound (flip-bit b) ρ = turn-sound b
step-sound (split p q t) ρ = substComposite (Fibre C.F) (path p ρ) (path q ρ) (interpret t ρ)
step-sound (under p s) ρ = cong (subst (Fibre C.F) (path p ρ)) (step-sound s ρ)

path-substitution : {V W : Type} (σ : V → Route W) (p : Route V) (ρ : W → Loop)
  → path (plug σ p) ρ ≡ path p (λ v → path (σ v) ρ)
path-substitution σ (slot v) ρ = refl
path-substitution σ stay ρ = refl
path-substitution σ turn ρ = refl
path-substitution σ (follow p q) ρ = cong₂ _∙_ (path-substitution σ p ρ) (path-substitution σ q ρ)

substitution-sound : {V W : Type} (σ : V → Route W) (t : Term V) (ρ : W → Loop)
  → interpret (plug-term σ t) ρ ≡ interpret t (λ v → path (σ v) ρ)
substitution-sound σ (bit b) ρ = refl
substitution-sound σ (carry p t) ρ = cong₂ (subst (Fibre C.F))
  (path-substitution σ p ρ) (substitution-sound σ t ρ)

empty-env : ⊥ → Loop
empty-env ()

route-sound : (p : Route ⊥) (b : Bool)
  → subst (Fibre C.F) (path p empty-env) b ≡ run-route p b
route-sound (slot ()) b
route-sound stay b = substRefl {B = Fibre C.F} {x = C.base-index} b
route-sound turn b = turn-sound b
route-sound (follow p q) b = substComposite (Fibre C.F) (path p empty-env) (path q empty-env) b
  ∙ cong (subst (Fibre C.F) (path q empty-env)) (route-sound p b)
  ∙ route-sound q (run-route p b)

run-sound : (t : Term ⊥) → interpret t empty-env ≡ run t
run-sound (bit b) = refl
run-sound (carry p t) = route-sound p (interpret t empty-env) ∙ cong (run-route p) (run-sound t)

-- Concrete machine traces: equal endpoints, different returned values.
one-loop : progress (carry turn (bit true)) ≡ next (flip-bit true)
one-loop = refl

two-start : progress (carry (follow turn turn) (bit true)) ≡ next (split turn turn (bit true))
two-start = refl

two-middle : progress (carry turn (carry turn (bit true))) ≡ next (under turn (flip-bit true))
two-middle = refl

two-end : progress (carry turn (bit false)) ≡ next (flip-bit false)
two-end = refl

twice-restores : (b : Bool) → run (carry (follow turn turn) (bit b)) ≡ b
twice-restores true = refl
twice-restores false = refl

-- Substitution exposes the transport redex of an open route program.
open-program : Term Bool
open-program = carry (slot true) (bit true)

supplied-program : plug-term {W = ⊥} (λ _ → turn) open-program ≡ carry turn (bit true)
supplied-program = refl

-- An endpoint-only action would assign a SINGLE function to all these loops.
no-endpoint-only-action : (f : Bool → Bool)
  → ((p : Route ⊥) (b : Bool) → f b ≡ run-route p b) → ⊥
no-endpoint-only-action f sound = true≢false (sym (sound stay true) ∙ sound turn true)

-- Output agreement does not recover route syntax. Retain it separately.
is-stay : Route ⊥ → Bool
is-stay stay = true
is-stay (slot ())
is-stay turn = false
is-stay (follow p q) = false

no-route-decoder : (decode : Bool → Route ⊥)
  → ((p : Route ⊥) → decode (run-route p true) ≡ p) → ⊥
no-route-decoder decode recover = true≢false
  (cong is-stay (sym (recover stay) ∙ recover (follow turn turn)))

two-actions : run-route (follow turn turn) ≡ run-route stay
two-actions = funExt twice-restores

no-action-decoder : (decode : (Bool → Bool) → Route ⊥)
  → ((p : Route ⊥) → decode (run-route p) ≡ p) → ⊥
no-action-decoder decode recover = true≢false (cong is-stay
  (sym (recover stay) ∙ cong decode (sym two-actions) ∙ recover (follow turn turn)))

record RetainedRun (t : Term ⊥) : Type where
  field
    result : Bool
    correct : interpret t empty-env ≡ result

execute : (t : Term ⊥) → RetainedRun t
execute t = record { result = run t ; correct = run-sound t }

-- The source term is an index of the certificate, not reconstructed from Bool.
Completed : Type
Completed = Σ (Term ⊥) RetainedRun

retain : Term ⊥ → Completed
retain t = t , execute t

source-recovered : (t : Term ⊥) → fst (retain t) ≡ t
source-recovered t = refl

-- Certification concerns the output and correctness proof, with source fixed.
-- It does not identify source routes or distinct reduction traces.
result-certificate : (t : Term ⊥) → isContr (RetainedRun t)
result-certificate t = execute t , contract
  where
  contract : (r : RetainedRun t) → execute t ≡ r
  contract r i = record { result = fst (pair-path i) ; correct = snd (pair-path i) }
    where
    pair-path : (run t , run-sound t) ≡ (RetainedRun.result r , RetainedRun.correct r)
    pair-path = Σ≡Prop (λ b → isSetBool (interpret t empty-env) b)
      (sym (run-sound t) ∙ RetainedRun.correct r)

higher-certificate : (t : Term ⊥) → isContr (isContr (RetainedRun t))
higher-certificate t = result-certificate t , isPropIsContr (result-certificate t)
