{-# OPTIONS --safe --cubical --guardedness #-}
module ObserverFiniteCyclicBoundary where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.Univalence using (ua; uaβ)
open import Cubical.Foundations.Transport using (substComposite)
open import Cubical.Data.Sigma.Base using (Σ; _,_; snd)
open import Cubical.Data.Nat.Base using (ℕ; zero; suc; _·_)
open import Cubical.Data.Nat.Properties using (snotz; ·-comm; ·-assoc; integral-domain-·)
open import Cubical.Data.Nat.Order using (_<_)
open import Cubical.Data.Nat.Mod using (_mod_; mod<; zero-charac-gen)
open import Cubical.Data.List.Base using (List; []; _∷_)
open import Cubical.Data.Int.Base using (ℤ; pos; abs; sucℤ; predℤ)
open import Cubical.Data.Int.Properties using (sucPred; predSuc)
open import Cubical.Data.Empty.Base using (⊥)
import ObserverInternalComparison as C
import ObserverComparisonCompression as P
import ObserverJointRefinement as J
import IndexIdentityCoherenceRegression as Cover

-- Semantic winding readout, obtained from an actual integer cover.
shift : ℤ ≃ ℤ
shift = isoToEquiv (iso sucℤ predℤ sucPred predSuc)

integer-cover : Cover.Circle → Type
integer-cover Cover.base = ℤ
integer-cover (Cover.loop i) = ua shift i

IntegerFibre : C.Reply → Type
IntegerFibre x = integer-cover (snd x)

winding : (C.base ≡ C.base) → ℤ
winding p = subst IntegerFibre p (pos zero)

power-winding : (n : ℕ) → winding (P.path (J.power n)) ≡ pos n
power-winding zero = substRefl {B = IntegerFibre} {x = C.base} (pos zero)
power-winding (suc n) = substComposite IntegerFibre (P.path (J.power n)) (P.path P.turn) (pos zero)
  ∙ cong (subst IntegerFibre (P.path P.turn)) (power-winding n) ∙ uaβ shift (pos n)

-- A probe code n means positive period suc n. These are bounded residue
-- observers of semantic winding, cyclic on the positive-power fragment.
-- abs is explicit: no signed-monodromy claim is made for negative loops.
observe : ℕ → (C.base ≡ C.base) → ℕ
observe n p = abs (winding p) mod (suc n)

bounded : (n : ℕ) (p : C.base ≡ C.base) → observe n p < suc n
bounded n p = mod< n (abs (winding p))

power-observation : (n k : ℕ) → observe n (P.path (J.power k)) ≡ k mod (suc n)
power-observation n k = cong (λ z → abs z mod (suc n)) (power-winding k)

data Member (p : ℕ) : List ℕ → Type where
  here : {ps : List ℕ} → Member p (p ∷ ps)
  there : {q : ℕ} {ps : List ℕ} → Member p ps → Member p (q ∷ ps)

common : List ℕ → ℕ
common [] = suc zero
common (p ∷ ps) = suc p · common ps

common-positive : (ps : List ℕ) → common ps ≡ zero → ⊥
common-positive [] = snotz
common-positive (p ∷ ps) = integral-domain-· {k = suc p} {l = common ps} snotz (common-positive ps)

factor : {p : ℕ} {ps : List ℕ} → Member p ps → Σ ℕ (λ k → common ps ≡ k · suc p)
factor {p} (here {ps}) = common ps , ·-comm (suc p) (common ps)
factor {p} (there {q} {ps} member) with factor member
... | k , e = suc q · k , cong (suc q ·_) e ∙ ·-assoc (suc q) k (suc p)

invisible : (ps : List ℕ) (p : ℕ) → Member p ps
  → observe p (P.path (J.power (common ps))) ≡ observe p (P.path (J.power zero))
invisible ps p member with factor member
... | k , e = power-observation p (common ps)
  ∙ cong (_mod (suc p)) e ∙ zero-charac-gen (suc p) k
  ∙ sym (zero-charac-gen (suc p) zero) ∙ sym (power-observation p zero)

nontrivial : (ps : List ℕ) → P.path (J.power (common ps)) ≡ P.path (J.power zero) → ⊥
nontrivial ps e = common-positive ps (cong abs
  (sym (power-winding (common ps)) ∙ cong winding e ∙ power-winding zero))

Readings : List ℕ → Type
Readings ps = (p : ℕ) → Member p ps → ℕ

joint : (ps : List ℕ) → (C.base ≡ C.base) → Readings ps
joint ps path p _ = observe p path

joint-invisible : (ps : List ℕ)
  → joint ps (P.path (J.power (common ps))) ≡ joint ps (P.path (J.power zero))
joint-invisible ps = funExt (λ p → funExt (invisible ps p))

no-joint-path-recovery : (ps : List ℕ) (recover : Readings ps → C.base ≡ C.base)
  → ((n : ℕ) → recover (joint ps (P.path (J.power n))) ≡ P.path (J.power n)) → ⊥
no-joint-path-recovery ps recover exact = nontrivial ps
  (sym (exact (common ps)) ∙ cong recover (joint-invisible ps) ∙ exact zero)
