{-# OPTIONS --safe --cubical --guardedness #-}
module ObserverSignedCyclicCover where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.Univalence using (ua; uaβ)
open import Cubical.Foundations.Transport using (substComposite; subst⁻Subst)
open import Cubical.Data.Sigma.Base using (_,_; fst; snd)
open import Cubical.Data.Sigma.Properties using (Σ≡Prop)
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import Cubical.Data.Nat.Properties using (+-comm)
open import Cubical.Data.Nat.Order using (isProp≤)
open import Cubical.Data.Nat.Mod using (_mod_; mod<; mod+mod≡mod)
open import Cubical.Data.Fin.Base using (Fin; fzero)
open import Cubical.Data.Fin.Arithmetic
open import Cubical.Data.List.Base using (List)
open import Cubical.Data.Empty.Base using (⊥)
import ObserverInternalComparison as C
import ObserverComparisonCompression as P
import ObserverJointRefinement as J
import ObserverFiniteCyclicBoundary as B
import IndexIdentityCoherenceRegression as Cover

State : ℕ → Type
State n = Fin (suc n)

residue : (n k : ℕ) → State n
residue n k = k mod (suc n) , mod< n k

advance retreat : (n : ℕ) → State n → State n
advance n x = x +ₘ residue n 1
retreat n x = x +ₘ (-ₘ residue n 1)

advance-retreat : (n : ℕ) (x : State n) → advance n (retreat n x) ≡ x
advance-retreat n x = +ₘ-assoc x (-ₘ residue n 1) (residue n 1)
  ∙ cong (x +ₘ_) (+ₘ-lCancel (residue n 1)) ∙ +ₘ-rUnit x

retreat-advance : (n : ℕ) (x : State n) → retreat n (advance n x) ≡ x
retreat-advance n x = +ₘ-assoc x (residue n 1) (-ₘ residue n 1)
  ∙ cong (x +ₘ_) (+ₘ-rCancel (residue n 1)) ∙ +ₘ-rUnit x

rotation : (n : ℕ) → State n ≃ State n
rotation n = isoToEquiv (iso (advance n) (retreat n) (advance-retreat n) (retreat-advance n))

cover : (n : ℕ) → Cover.Circle → Type
cover n Cover.base = State n
cover n (Cover.loop i) = ua (rotation n) i

Fibre : ℕ → C.Reply → Type
Fibre n x = cover n (snd x)

forward-transport : (n : ℕ) (x : State n)
  → subst (Fibre n) (P.path P.turn) x ≡ advance n x
forward-transport n x = uaβ (rotation n) x

backward-transport : (n : ℕ) (x : State n)
  → subst (Fibre n) (sym (P.path P.turn)) x ≡ retreat n x
backward-transport n x =
  sym (cong (subst (Fibre n) (sym (P.path P.turn)))
    (forward-transport n (retreat n x) ∙ advance-retreat n x))
  ∙ subst⁻Subst (Fibre n) (P.path P.turn) (retreat n x)

-- First-order signed comparison expressions: both directions are explicit.
data Signed : Type where
  stay up down : Signed
  then : Signed → Signed → Signed

path : Signed → C.base ≡ C.base
path stay = refl
path up = P.path P.turn
path down = sym (P.path P.turn)
path (then u v) = path u ∙ path v

act : (n : ℕ) → Signed → State n → State n
act n stay x = x
act n up x = advance n x
act n down x = retreat n x
act n (then u v) x = act n v (act n u x)

correct : (n : ℕ) (w : Signed) (x : State n) → subst (Fibre n) (path w) x ≡ act n w x
correct n stay x = substRefl {B = Fibre n} {x = C.base} x
correct n up x = forward-transport n x
correct n down x = backward-transport n x
correct n (then u v) x = substComposite (Fibre n) (path u) (path v) x
  ∙ cong (subst (Fibre n) (path v)) (correct n u x) ∙ correct n v (act n u x)

residue-step : (n k : ℕ) → advance n (residue n k) ≡ residue n (suc k)
residue-step n k = Σ≡Prop (λ _ → isProp≤)
  (sym (mod+mod≡mod (suc n) k 1) ∙ cong (_mod (suc n)) (+-comm k 1))

power-reading : (n k : ℕ) → subst (Fibre n) (P.path (J.power k)) fzero ≡ residue n k
power-reading n zero = substRefl {B = Fibre n} {x = C.base} fzero ∙ Σ≡Prop (λ _ → isProp≤) refl
power-reading n (suc k) = substComposite (Fibre n) (P.path (J.power k)) (P.path P.turn) fzero
  ∙ cong (subst (Fibre n) (P.path P.turn)) (power-reading n k)
  ∙ forward-transport n (residue n k) ∙ residue-step n k

positive-bridge : (n k : ℕ)
  → fst (subst (Fibre n) (P.path (J.power k)) fzero) ≡ B.observe n (P.path (J.power k))
positive-bridge n k = cong fst (power-reading n k) ∙ sym (B.power-observation n k)

Readings : List ℕ → Type
Readings ps = (n : ℕ) → B.Member n ps → State n

joint : (ps : List ℕ) → (C.base ≡ C.base) → Readings ps
joint ps p n _ = subst (Fibre n) p fzero

joint-invisible : (ps : List ℕ)
  → joint ps (P.path (J.power (B.common ps))) ≡ joint ps (P.path (J.power zero))
joint-invisible ps = funExt (λ n → funExt (λ member → Σ≡Prop (λ _ → isProp≤)
  (positive-bridge n (B.common ps) ∙ B.invisible ps n member ∙ sym (positive-bridge n zero))))

no-path-recovery : (ps : List ℕ) (recover : Readings ps → C.base ≡ C.base)
  → ((k : ℕ) → recover (joint ps (P.path (J.power k))) ≡ P.path (J.power k)) → ⊥
no-path-recovery ps recover exact = B.nontrivial ps
  (sym (exact (B.common ps)) ∙ cong recover (joint-invisible ps) ∙ exact zero)
