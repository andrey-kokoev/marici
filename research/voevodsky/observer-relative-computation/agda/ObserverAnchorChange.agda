{-# OPTIONS --safe --cubical --guardedness #-}
module ObserverAnchorChange where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.Transport using (substEquiv; substComposite)
open import Cubical.Data.Sigma.Base using (Σ; _,_)
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (true≢false)
open import Cubical.Data.Empty.Base using (⊥)
import ObserverInternalComparison as C
import ObserverAnchoredRecords as A

RecordAt : C.Reply → Type
RecordAt a = Σ C.Reply (λ y → Σ (a ≡ y) (λ _ → A.Fibre y))

embed : (a : C.Reply) → A.Fibre a → RecordAt a
embed a v = a , refl , v

normalize : (a : C.Reply) → RecordAt a → A.Fibre a
normalize a (y , p , v) = subst A.Fibre (sym p) v

normalize-embed : (a : C.Reply) (v : A.Fibre a) → normalize a (embed a v) ≡ v
normalize-embed a v = substRefl {B = A.Fibre} {x = a} v

embed-normalize : (a : C.Reply) (r : RecordAt a) → embed a (normalize a r) ≡ r
embed-normalize a (y , p , v) = J
  (λ y p → (v : A.Fibre y) → embed a (subst A.Fibre (sym p) v) ≡ (y , p , v))
  (λ v → cong (embed a) (substRefl {B = A.Fibre} {x = a} v)) p v

normalization : (a : C.Reply) → RecordAt a ≃ A.Fibre a
normalization a = isoToEquiv (iso (normalize a) (embed a) (normalize-embed a) (embed-normalize a))

reanchor : {a b : C.Reply} → a ≡ b → RecordAt a → RecordAt b
reanchor = subst RecordAt

reanchor-equivalence : {a b : C.Reply} → a ≡ b → RecordAt a ≃ RecordAt b
reanchor-equivalence = substEquiv RecordAt

identity-law : {a : C.Reply} (r : RecordAt a) → reanchor refl r ≡ r
identity-law = substRefl {B = RecordAt}

composition-law : {a b c : C.Reply} (p : a ≡ b) (q : b ≡ c) (r : RecordAt a)
  → reanchor (p ∙ q) r ≡ reanchor q (reanchor p r)
composition-law = substComposite RecordAt

equivariant : {a b : C.Reply} (p : a ≡ b) (r : RecordAt a)
  → normalize b (reanchor p r) ≡ subst A.Fibre p (normalize a r)
equivariant {a} p r = J
  (λ b p → normalize b (reanchor p r) ≡ subst A.Fibre p (normalize a r))
  (cong (normalize a) (substRefl {B = RecordAt} {x = a} r)
    ∙ sym (substRefl {B = A.Fibre} {x = a} (normalize a r))) p

Unanchored = Σ C.Reply A.Fibre
forget : {a : C.Reply} → RecordAt a → Unanchored
forget (y , p , v) = y , v

forget-reanchor : {a b : C.Reply} (p : a ≡ b) (r : RecordAt a)
  → forget (reanchor p r) ≡ forget r
forget-reanchor {a} p r = J (λ b p → forget (reanchor p r) ≡ forget r)
  (cong (forget {a}) (substRefl {B = RecordAt} {x = a} r)) p

loop-flips-normalization : normalize C.base
  (reanchor (C.interpret C.turn) (embed C.base true)) ≡ false
loop-flips-normalization = equivariant (C.interpret C.turn) (embed C.base true)
  ∙ cong (subst A.Fibre (C.interpret C.turn)) (normalize-embed C.base true)
  ∙ C.turn-read

-- Same reply and displayed value, but distinct normalized anchor values.
same-forgotten : forget (A.embed true) ≡ forget A.held-true
same-forgotten = refl

held-normalization : normalize C.base A.held-true ≡ false
held-normalization = sym (cong A.anchor A.other-anchor) ∙ A.anchor-embed false

no-normalization-descent : (read : Unanchored → Bool)
  → ((r : RecordAt C.base) → read (forget r) ≡ normalize C.base r) → ⊥
no-normalization-descent read exact = true≢false
  (sym (normalize-embed C.base true) ∙ sym (exact (A.embed true))
    ∙ cong read same-forgotten ∙ exact A.held-true ∙ held-normalization)
