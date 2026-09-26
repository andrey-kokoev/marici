{-# OPTIONS --safe --cubical --guardedness #-}
module ObserverComparisonCompression where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.Univalence using (ua; uaβ)
open import Cubical.Foundations.Transport using (substComposite; subst⁻Subst)
open import Cubical.Data.Sigma.Base using (_,_; snd)
open import Cubical.Data.Bool.Base using (Bool; true; false; not)
open import Cubical.Data.Bool.Properties using (notEquiv; true≢false)
open import Cubical.Data.Empty.Base using (⊥)
import ObserverInternalComparison as C
import ObserverAnchoredRecords as A
import IndexIdentityCoherenceRegression as Cover

-- Finite constructor vocabulary, arbitrarily large finite expressions.
data Word : Type where
  stay turn : Word
  then : Word → Word → Word

path : Word → C.base ≡ C.base
path stay = refl
path turn = C.interpret C.turn
path (then u v) = path u ∙ path v

xor : Bool → Bool → Bool
xor false q = q
xor true q = not q

parity : Word → Bool
parity stay = false
parity turn = true
parity (then u v) = xor (parity u) (parity v)

act : Bool → Bool → Bool
act false b = b
act true b = not b

act-compose : (p q b : Bool) → act (xor p q) b ≡ act q (act p b)
act-compose false q b = refl
act-compose true false b = refl
act-compose true true true = refl
act-compose true true false = refl

act-involutive : (p b : Bool) → act p (act p b) ≡ b
act-involutive false b = refl
act-involutive true true = refl
act-involutive true false = refl

action-correct : (w : Word) (b : Bool) → subst A.Fibre (path w) b ≡ act (parity w) b
action-correct stay b = substRefl {B = A.Fibre} {x = C.base} b
action-correct turn b = uaβ notEquiv b
action-correct (then u v) b = substComposite A.Fibre (path u) (path v) b
  ∙ cong (subst A.Fibre (path v)) (action-correct u b)
  ∙ action-correct v (act (parity u) b) ∙ sym (act-compose (parity u) (parity v) b)

-- Parity plus displayed value suffices to reproduce anchored normalization.
compressed-normalization : (w : Word) (v : Bool)
  → act (parity w) v ≡ A.anchor (C.base , path w , v)
compressed-normalization w v = sym (subst⁻Subst A.Fibre (path w) (act (parity w) v))
  ∙ cong (subst A.Fibre (sym (path w)))
    (action-correct w (act (parity w) v) ∙ act-involutive (parity w) v)

faithful-readback : (w : Word) (b : Bool)
  → act (parity w) (subst A.Fibre (path w) b) ≡ b
faithful-readback w b = cong (act (parity w)) (action-correct w b) ∙ act-involutive (parity w) b

-- A different finite observer detects semantic information lost by parity.
data Three : Type where
  zero3 one3 two3 : Three

cycle undo : Three → Three
cycle zero3 = one3
cycle one3 = two3
cycle two3 = zero3
undo zero3 = two3
undo one3 = zero3
undo two3 = one3

cycle-undo : (x : Three) → cycle (undo x) ≡ x
cycle-undo zero3 = refl
cycle-undo one3 = refl
cycle-undo two3 = refl

undo-cycle : (x : Three) → undo (cycle x) ≡ x
undo-cycle zero3 = refl
undo-cycle one3 = refl
undo-cycle two3 = refl

cycle-equiv : Three ≃ Three
cycle-equiv = isoToEquiv (iso cycle undo cycle-undo undo-cycle)

cover3 : Cover.Circle → Type
cover3 Cover.base = Three
cover3 (Cover.loop i) = ua cycle-equiv i

Fibre3 : C.Reply → Type
Fibre3 x = cover3 (snd x)

read3 : (C.base ≡ C.base) → Three
read3 p = subst Fibre3 p zero3

double-read : read3 (path (then turn turn)) ≡ two3
double-read = substComposite Fibre3 (path turn) (path turn) zero3
  ∙ cong (subst Fibre3 (path turn)) (uaβ cycle-equiv zero3) ∙ uaβ cycle-equiv one3

stay-read : read3 (path stay) ≡ zero3
stay-read = substRefl {B = Fibre3} {x = C.base} zero3

is-zero : Three → Bool
is-zero zero3 = true
is-zero one3 = false
is-zero two3 = false

semantic-paths-distinct : path (then turn turn) ≡ path stay → ⊥
semantic-paths-distinct e = true≢false (cong is-zero
  (sym stay-read ∙ sym (cong read3 e) ∙ double-read))

-- No decoder of the retained bit can faithfully reconstruct every path.
no-path-recovery : (recover : Bool → C.base ≡ C.base)
  → ((w : Word) → recover (parity w) ≡ path w) → ⊥
no-path-recovery recover exact = semantic-paths-distinct
  (sym (exact (then turn turn)) ∙ exact stay)
