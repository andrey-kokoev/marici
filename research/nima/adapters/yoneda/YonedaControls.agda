{-# OPTIONS --safe --cubical --guardedness #-}
module YonedaControls where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false; true; _and_)
import Cubical.Data.Bool.Properties as B
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Empty.Base using (⊥)
open import OrdinaryYoneda

-- One object, two endomorphisms, including an absorbing noninvertible arrow.
C : Category ℓ-zero ℓ-zero
C = record
  { Ob = Unit ; Hom = λ _ _ → Bool ; hom-set = λ _ _ → B.isSetBool
  ; unit = true ; comp = _and_
  ; unitL = λ f → refl ; unitR = B.and-identityʳ
  ; assoc = B.and-assoc }
module Y = Theorem C
module T = Y.At (Y.representable tt) tt

raw-constant raw-identity : T.Raw
raw-constant _ _ = true
raw-identity _ f = f
same-at-identity : raw-constant tt true ≡ raw-identity tt true
same-at-identity = refl
raws-differ : raw-constant ≡ raw-identity → ⊥
raws-differ p = B.true≢false (cong (λ α → α tt false) p)
constant-not-natural : T.NaturalLaw raw-constant → ⊥
constant-not-natural law = B.false≢true (law tt tt false true)
noninvertible : (g : Bool) → g and false ≡ true → ⊥
noninvertible false p = B.false≢true p
noninvertible true p = B.false≢true p
