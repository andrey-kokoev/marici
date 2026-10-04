{-# OPTIONS --safe --cubical --guardedness #-}
module RetainedActionYoneda where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.HLevels using (isPropΠ4; isSetΣ)
open import Cubical.Data.Sigma using (_×_; Σ≡Prop)
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (isSetBool; false≢true)
open import Cubical.Data.Empty.Base using (⊥)
import RetainedComparisonStructure as R

module Actions {ℓ : Level} (S : R.Structure ℓ) where
  open R.Structure S hiding (transport)

  -- Object labels remain in P. E acts on fibers; it is not identified with
  -- equality of the object labels. All action-law witnesses remain fields.
  record SetAction (ℓD : Level) : Type (ℓ-max ℓ (ℓ-suc ℓD)) where
    field
      Carrier : P → Type ℓD
      carrier-set : (p : P) → isSet (Carrier p)
      act : {p q : P} → E p q → Carrier p → Carrier q
      act-unit : {p : P} (v : Carrier p) → act idE v ≡ v
      act-comp : {p q r : P} (d : E q r) (e : E p q) (v : Carrier p)
        → act d (act e v) ≡ act (compE d e) v

  module At {ℓD : Level} (D : SetAction ℓD) (p : P) where
    open SetAction D

    Raw : Type (ℓ-max ℓ ℓD)
    Raw = (q : P) → E p q → Carrier q

    Equivariant : Raw → Type (ℓ-max ℓ ℓD)
    Equivariant f = (q r : P) (d : E q r) (e : E p q)
      → act d (f q e) ≡ f r (compE d e)

    equivariance-is-prop : (f : Raw) → isProp (Equivariant f)
    equivariance-is-prop f = isPropΠ4 λ q r d e → carrier-set r _ _

    Natural : Type (ℓ-max ℓ ℓD)
    Natural = Σ[ f ∈ Raw ] Equivariant f

    evaluate : Natural → Carrier p
    evaluate f = fst f p idE

    extend : Carrier p → Natural
    extend v = (λ q e → act e v) , λ q r d e → act-comp d e v

    evaluate-extend : (v : Carrier p) → evaluate (extend v) ≡ v
    evaluate-extend = act-unit

    extend-evaluate : (f : Natural) → extend (evaluate f) ≡ f
    extend-evaluate f = Σ≡Prop equivariance-is-prop
      (funExt λ q → funExt λ e → snd f p q e idE ∙ cong (fst f q) (unitRE e))

    universal-iso : Iso Natural (Carrier p)
    universal-iso = record
      { fun = evaluate ; inv = extend
      ; rightInv = evaluate-extend ; leftInv = extend-evaluate }

    Extension : Carrier p → Type (ℓ-max ℓ ℓD)
    Extension v = Σ[ f ∈ Natural ] (evaluate f ≡ v)

    unique-extension : (v : Carrier p) → isContr (Extension v)
    unique-extension v = equiv-proof (snd (isoToEquiv universal-iso)) v

  -- Inverse transport is derived from the two action laws and E inverses;
  -- it is not a third independent field of an action.
  action-iso : {ℓD : Level} (D : SetAction ℓD) {p q : P} (e : E p q)
    → Iso (SetAction.Carrier D p) (SetAction.Carrier D q)
  action-iso D e = record
    { fun = act e ; inv = act (invE e)
    ; rightInv = λ v → act-comp e (invE e) v
        ∙ cong (λ d → act d v) (inverseRE e) ∙ act-unit v
    ; leftInv = λ v → act-comp (invE e) e v
        ∙ cong (λ d → act d v) (inverseLE e) ∙ act-unit v }
    where open SetAction D

  regular : ((p q : P) → isSet (E p q)) → P → SetAction ℓ
  regular setE a = record
    { Carrier = E a ; carrier-set = setE a
    ; act = λ {p} {q} e d → compE {a} {p} {q} e d
    ; act-unit = λ {p} d → unitLE {a} {p} d
    ; act-comp = λ {p} {q} {r} h e d → assocE {a} {p} {q} {r} h e d }

  realized : ((p q : P) → isSet (K p q)) → P → SetAction ℓ
  realized setK a = record
    { Carrier = K a ; carrier-set = setK a
    ; act = λ e k → compK (realize e) k
    ; act-unit = λ k → cong (λ z → compK z k) realize-id ∙ unitLK k
    ; act-comp = λ d e k → assocK (realize d) (realize e) k
        ∙ cong (λ z → compK z k) (sym (realize-comp d e)) }

  -- The supplied realization itself is the equivariant extension of the K
  -- identity for its induced action. This does not choose the action for us.
  realization-extension : (setK : (p q : P) → isSet (K p q)) (p : P)
    → At.Extension (realized setK p) p (idK {p})
  realization-extension setK p =
    ((λ q e → realize e) , λ q r d e → sym (realize-comp d e)) , realize-id

  recover-realization : (setK : (p q : P) → isSet (K p q)) {p q : P} (e : E p q)
    → SetAction.act (realized setK p) e (idK {p}) ≡ realize e
  recover-realization setK e = unitRK (realize e)

  -- Natural transformations between covariant representables recover an
  -- arrow in the reverse functor direction: E(q,-) -> E(p,-) recovers E(p,q).
  representable-universality : (setE : (p q : P) → isSet (E p q)) (p q : P)
    → At.Natural (regular setE p) q ≃ E p q
  representable-universality setE p q = isoToEquiv (At.universal-iso (regular setE p) q)

  regular-detects : (setE : (p q : P) → isSet (E p q)) {p q : P} (e f : E p q)
    → SetAction.act (regular setE p) e idE ≡ SetAction.act (regular setE p) f idE
    → e ≡ f
  regular-detects setE e f w = sym (unitRE e) ∙ w ∙ unitRE f

module Example = Actions R.example

setE : (p q : Bool) → isSet (R.Example.E p q)
setE p q = isSetΣ isSetBool (λ _ → isSetBool)

setK : (p q : Bool) → isSet (R.Example.K p q)
setK p q = isSetBool

regular realized : Example.SetAction ℓ-zero
regular = Example.regular setE false
realized = Example.realized setK false

-- Hom-wise representability does not imply recovery of raw object labels.
-- This example has identical regular actions at two distinct marked objects.
same-regular-actions : Example.regular setE false ≡ Example.regular setE true
same-regular-actions = refl

no-unmarked-object-recovery : (recover : Example.SetAction ℓ-zero → Bool)
  → ((p : Bool) → recover (Example.regular setE p) ≡ p) → ⊥
no-unmarked-object-recovery recover law = false≢true (sym (law false) ∙ law true)

marked-regular : Bool → Σ[ p ∈ Bool ] Example.SetAction ℓ-zero
marked-regular p = p , Example.regular setE p

marked-object-recovery : (p : Bool) → fst (marked-regular p) ≡ p
marked-object-recovery p = refl

regular-value : R.Example.E false true → Bool × Bool
regular-value e = Example.SetAction.act regular {false} {true} e (false , false)

realized-value : R.Example.E false true → Bool
realized-value e = Example.SetAction.act realized {false} {true} e false

regular-distinguishes : regular-value R.change0 ≡ regular-value R.change1 → ⊥
regular-distinguishes p = false≢true (cong snd p)

realized-identifies : realized-value R.change0 ≡ realized-value R.change1
realized-identifies = refl

-- Equal initial values do NOT determine unrestricted functions. The
-- equivariance witness is precisely the extra interface tested by the UP.
module RegularAt = Example.At regular false

raw0 raw1 : RegularAt.Raw
raw0 q e = false , false
raw1 q e = e

same-at-identity : raw0 false (R.Example.idE {false}) ≡ raw1 false (R.Example.idE {false})
same-at-identity = refl

raws-distinct : raw0 ≡ raw1 → ⊥
raws-distinct p = false≢true (cong (λ f → snd (f true R.change1)) p)

constant-not-equivariant : RegularAt.Equivariant raw0 → ⊥
constant-not-equivariant n = false≢true (sym (cong snd (n false true R.change1 (R.Example.idE {false}))))

identity-is-equivariant : RegularAt.Equivariant raw1
identity-is-equivariant q r d e = refl
