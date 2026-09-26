{-# OPTIONS --safe --cubical --guardedness #-}
module ObserverSignedBounded where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.HLevels using (isSetRetract)
open import Cubical.Foundations.GroupoidLaws using (rCancel; lCancel; rUnit)
open import Cubical.Foundations.Transport using (substComposite; subst⁻Subst)
open import Cubical.Data.Sigma.Base using (Σ; _,_; fst)
open import Cubical.Data.Nat.Base using (ℕ; zero; suc; _+_)
open import Cubical.Data.Nat.Order using (suc-≤-suc; ≤SumLeft)
open import Cubical.Data.Fin.Base using (fzero)
open import Cubical.HITs.PropositionalTruncation.Base using (∥_∥₁)
import Cubical.HITs.PropositionalTruncation.Properties as Trunc
import Cubical.Data.Int.Base as Z
import Cubical.Data.Int.Properties as ZP
import ObserverInternalComparison as C
import ObserverComparisonCompression as P
import ObserverJointRefinement as J
import ObserverSignedCyclicCover as S
import ObserverBoundedCyclic as B
import ObserverSignedNormalization as N

power-integer : (k : ℕ) → N.integer (P.path (J.power k)) ≡ Z.pos k
power-integer zero = refl
power-integer (suc k) = N.composition (P.path (J.power k)) (P.path P.turn)
  ∙ cong (λ z → z Z.+ Z.pos 1) (power-integer k)

inverse-integer : (p : N.Loop) → N.integer (sym p) ≡ Z.- N.integer p
inverse-integer p = ZP.inj-z+ {z = N.integer p}
  (sym (N.composition p (sym p)) ∙ cong N.integer (rCancel p)
    ∙ sym (ZP.-Cancel (N.integer p)))

Slot : ℕ → Type
Slot bound = S.State (bound + bound)

-- Offset k represents signed winding -bound+k, not absolute winding.
offset : (bound : ℕ) → Slot bound → N.Loop
offset bound x = sym (P.path (J.power bound)) ∙ P.path (J.power (fst x))

offset-integer : (bound : ℕ) (x : Slot bound)
  → N.integer (offset bound x) ≡ (Z.- Z.pos bound) Z.+ Z.pos (fst x)
offset-integer bound x = N.composition (sym (P.path (J.power bound))) (P.path (J.power (fst x)))
  ∙ cong₂ Z._+_ (inverse-integer (P.path (J.power bound)) ∙ cong Z.-_ (power-integer bound))
    (power-integer (fst x))

-- Calibrate the finite observer by bound forward turns. Its finite seed
-- also equals the corresponding residue by S.power-reading.
seed : (bound : ℕ) → Slot bound
seed bound = subst (S.Fibre (bound + bound)) (P.path (J.power bound)) fzero

read : (bound : ℕ) → N.Loop → Slot bound
read bound p = subst (S.Fibre (bound + bound)) p (seed bound)

read-offset : (bound : ℕ) (x : Slot bound) → read bound (offset bound x) ≡ x
read-offset bound x = substComposite (S.Fibre (bound + bound))
  (sym (P.path (J.power bound))) (P.path (J.power (fst x))) (seed bound)
  ∙ cong (subst (S.Fibre (bound + bound)) (P.path (J.power (fst x))))
    (subst⁻Subst (S.Fibre (bound + bound)) (P.path (J.power bound)) fzero)
  ∙ B.bounded-exact (bound + bound) x

observation-equivalence : (bound : ℕ) → Slot bound ≃ Slot bound
observation-equivalence bound = isoToEquiv
  (iso (λ x → read bound (offset bound x)) (λ x → x) (read-offset bound) (read-offset bound))

recover : (bound : ℕ) → Slot bound → N.Loop
recover = offset

-- A mere interval-representation certificate suffices; no chosen syntax
-- witness is extracted from the propositional truncation.
Bounded : ℕ → N.Loop → Type
Bounded bound p = ∥ Σ (Slot bound) (λ x → offset bound x ≡ p) ∥₁

loop-set : isSet N.Loop
loop-set = isSetRetract N.integer N.represent N.semantic-roundtrip ZP.isSetℤ

faithful : (bound : ℕ) (p : N.Loop) → Bounded bound p → recover bound (read bound p) ≡ p
faithful bound p = Trunc.rec (loop-set _ _)
  (λ { (x , e) → cong (λ q → recover bound (read bound q)) (sym e)
    ∙ cong (offset bound) (read-offset bound x) ∙ e })

separates : (bound : ℕ) (p q : N.Loop) → Bounded bound p → Bounded bound q
  → read bound p ≡ read bound q → p ≡ q
separates bound p q bp bq e = sym (faithful bound p bp)
  ∙ cong (recover bound) e ∙ faithful bound q bq

-- Both an inverse endpoint and the zero centre are retained explicitly.
lower-endpoint : (bound : ℕ) → offset bound fzero ≡ sym (P.path (J.power bound))
lower-endpoint bound = sym (rUnit (sym (P.path (J.power bound))))

centre : (bound : ℕ) → Slot bound
centre bound = bound , suc-≤-suc ≤SumLeft

centre-is-zero : (bound : ℕ) → offset bound (centre bound) ≡ refl
centre-is-zero bound = lCancel (P.path (J.power bound))
