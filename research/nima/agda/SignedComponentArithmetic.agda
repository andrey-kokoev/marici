{-# OPTIONS --safe --cubical --guardedness #-}
module SignedComponentArithmetic where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma using (_×_)
import Cubical.Data.Nat as N
import Cubical.Data.Int as Z
import Cubical.Data.Int.MoreInts.DiffInt.Base as D
import Cubical.HITs.SetQuotients as Q
open import Cubical.Algebra.CommRing.Base
open import Cubical.Algebra.Ring.Properties using (Ring→Semiring)
open import Cubical.Algebra.CommRing.Instances.Int using (ℤCommRing)
open import Cubical.Tactics.CommRingSolver
import ComponentArithmetic as C
import FaithfulComponentRing as F

Pair : Type
Pair = C.Word × C.Word
zero-pair one-pair : Pair
zero-pair = 0 , 0
one-pair = 1 , 0
add-pair multiply-pair : Pair → Pair → Pair
add-pair (a , b) (c , d) = C.append a c , C.append b d
multiply-pair (a , b) (c , d) =
  C.append (C.multiply a c) (C.multiply b d) , C.append (C.multiply a d) (C.multiply b c)
negate-pair : Pair → Pair
negate-pair (a , b) = b , a
Balance : Pair → Pair → Type
Balance (a , b) (c , d) = C.append a d ≡ C.append c b
Signed : Type
Signed = Pair Q./ Balance

module Readout (R : CommRing ℓ-zero) where
  open CommRingStr (snd R)
  module W = C.Readout (Ring→Semiring (CommRing→Ring R))
  pair : Pair → fst R
  pair (a , b) = W.numeral a - W.numeral b
  add-polynomial : (a b c d : fst R) → (a + c) - (b + d) ≡ (a - b) + (c - d)
  add-polynomial a b c d = solve! R
  multiply-polynomial : (a b c d : fst R) → (a · c + b · d) - (a · d + b · c) ≡ (a - b) · (c - d)
  multiply-polynomial a b c d = solve! R
  pair-add : (p q : Pair) → pair (add-pair p q) ≡ pair p + pair q
  pair-add (a , b) (c , d) = cong₂ _-_ (W.numeral-add a c) (W.numeral-add b d)
    ∙ add-polynomial (W.numeral a) (W.numeral b) (W.numeral c) (W.numeral d)
  pair-multiply : (p q : Pair) → pair (multiply-pair p q) ≡ pair p · pair q
  pair-multiply (a , b) (c , d) = cong₂ _-_
    (W.numeral-add (C.multiply a c) (C.multiply b d) ∙ cong₂ _+_ (W.numeral-multiply a c) (W.numeral-multiply b d))
    (W.numeral-add (C.multiply a d) (C.multiply b c) ∙ cong₂ _+_ (W.numeral-multiply a d) (W.numeral-multiply b c))
    ∙ multiply-polynomial (W.numeral a) (W.numeral b) (W.numeral c) (W.numeral d)
  negate-polynomial : (a b : fst R) → b - a ≡ - (a - b)
  negate-polynomial a b = solve! R
  pair-negate : (p : Pair) → pair (negate-pair p) ≡ - pair p
  pair-negate (a , b) = negate-polynomial (W.numeral a) (W.numeral b)
  cancel : (a b c d : fst R) → a + d ≡ c + b → a - b ≡ c - d
  cancel a b c d p = step₁ ∙ cong (λ x → x - (b + d)) p ∙ step₂
    where
    step₁ : a - b ≡ (a + d) - (b + d)
    step₁ = solve! R
    step₂ : (c + b) - (b + d) ≡ c - d
    step₂ = solve! R
  respects : (p q : Pair) → Balance p q → pair p ≡ pair q
  respects (a , b) (c , d) p = cancel (W.numeral a) (W.numeral b) (W.numeral c) (W.numeral d)
    (sym (W.numeral-add a d) ∙ cong W.numeral p ∙ W.numeral-add c b)
  read : Signed → fst R
  read = Q.rec is-set pair respects

-- Identification with the library's independently checked difference quotient.
append-native : (a b : C.Word) → C.append a b ≡ a N.+ b
append-native N.zero b = refl
append-native (N.suc a) b = cong N.suc (append-native a b)
balance-native : (p q : Pair) → Balance p q → D.rel p q
balance-native (a , b) (c , d) p = sym (append-native a d) ∙ p ∙ append-native c b
balance-component : (p q : Pair) → D.rel p q → Balance p q
balance-component (a , b) (c , d) p = append-native a d ∙ p ∙ sym (append-native c b)
to-difference : Signed → D.ℤ
to-difference = Q.rec Q.squash/ Q.[_] (λ p q r → Q.eq/ p q (balance-native p q r))
from-difference : D.ℤ → Signed
from-difference = Q.rec Q.squash/ Q.[_] (λ p q r → Q.eq/ p q (balance-component p q r))
roundtrip : (x : Signed) → from-difference (to-difference x) ≡ x
roundtrip = Q.elimProp (λ _ → Q.squash/ _ _) (λ _ → refl)
asInt : Signed → Z.ℤ
asInt x = D.ℤ→Int (to-difference x)
fromInt : Z.ℤ → Signed
fromInt z = from-difference (D.Int→ℤ z)
recover : (x : Signed) → fromInt (asInt x) ≡ x
recover x = cong from-difference (D.ℤ→Int→ℤ (to-difference x)) ∙ roundtrip x
faithful : {x y : Signed} → asInt x ≡ asInt y → x ≡ y
faithful {x} {y} p = sym (recover x) ∙ cong fromInt p ∙ recover y

module I = Readout ℤCommRing
numeral-pos : (a : C.Word) → I.W.numeral a ≡ Z.pos a
numeral-pos N.zero = refl
numeral-pos (N.suc a) = cong (Z.pos 1 Z.+_) (numeral-pos a) ∙ sym (Z.pos+ 1 a)
pair-asInt : (p : Pair) → asInt Q.[ p ] ≡ I.pair p
pair-asInt (a , b) = Z.pos- a b ∙ sym (cong₂ Z._-_ (numeral-pos a) (numeral-pos b))
raw-add : (p q : Pair) → asInt Q.[ add-pair p q ] ≡ asInt Q.[ p ] Z.+ asInt Q.[ q ]
raw-add p q = pair-asInt (add-pair p q) ∙ I.pair-add p q ∙ sym (cong₂ Z._+_ (pair-asInt p) (pair-asInt q))
raw-multiply : (p q : Pair) → asInt Q.[ multiply-pair p q ] ≡ asInt Q.[ p ] Z.· asInt Q.[ q ]
raw-multiply p q = pair-asInt (multiply-pair p q) ∙ I.pair-multiply p q ∙ sym (cong₂ Z._·_ (pair-asInt p) (pair-asInt q))

module QuotientOperation (raw : Pair → Pair → Pair) (op : Z.ℤ → Z.ℤ → Z.ℤ)
  (law : (p q : Pair) → asInt Q.[ raw p q ] ≡ op (asInt Q.[ p ]) (asInt Q.[ q ])) where
  operation : Signed → Signed → Signed
  operation = Q.rec2 Q.squash/ (λ p q → Q.[ raw p q ])
    (λ p p' q r → faithful (law p q ∙ cong (λ x → op x (asInt Q.[ q ])) (cong asInt (Q.eq/ p p' r)) ∙ sym (law p' q)))
    (λ p q q' r → faithful (law p q ∙ cong (op (asInt Q.[ p ])) (cong asInt (Q.eq/ q q' r)) ∙ sym (law p q')))
  preserves : (x y : Signed) → asInt (operation x y) ≡ op (asInt x) (asInt y)
  preserves = Q.elimProp2 (λ _ _ → Z.isSetℤ _ _) law
module Add = QuotientOperation add-pair Z._+_ raw-add
module Multiply = QuotientOperation multiply-pair Z._·_ raw-multiply
add multiply : Signed → Signed → Signed
add = Add.operation
multiply = Multiply.operation
zero one : Signed
zero = Q.[ zero-pair ]
one = Q.[ one-pair ]

asInt-fromInt : (z : Z.ℤ) → asInt (fromInt z) ≡ z
asInt-fromInt (Z.pos n) = refl
asInt-fromInt (Z.negsuc n) = refl
raw-negate : (p : Pair) → asInt Q.[ negate-pair p ] ≡ Z.- asInt Q.[ p ]
raw-negate p = pair-asInt (negate-pair p) ∙ I.pair-negate p ∙ cong Z.-_ (sym (pair-asInt p))
negate : Signed → Signed
negate = Q.rec Q.squash/ (λ p → Q.[ negate-pair p ])
  (λ p q r → faithful (raw-negate p ∙ cong Z.-_ (cong asInt (Q.eq/ p q r)) ∙ sym (raw-negate q)))
negate-preserves : (x : Signed) → asInt (negate x) ≡ Z.- asInt x
negate-preserves = Q.elimProp (λ _ → Z.isSetℤ _ _) raw-negate
add-inverse : (x : Signed) → add x (negate x) ≡ zero
add-inverse x = faithful (Add.preserves x (negate x) ∙ cong (asInt x Z.+_) (negate-preserves x) ∙ Z.-Cancel (asInt x))
module Ring = F.Transfer Signed Q.squash/ ℤCommRing asInt faithful zero one add multiply negate
  refl refl Add.preserves Multiply.preserves negate-preserves
signedRing : CommRing ℓ-zero
signedRing = Ring.ring

-- The actual semiring map from the preceding component-word construction.
embed-word : C.Word → Signed
embed-word n = Q.[ n , 0 ]
embed-word-add : (a b : C.Word) → embed-word (C.append a b) ≡ add (embed-word a) (embed-word b)
embed-word-add a b = refl
embed-word-multiply : (a b : C.Word) → embed-word (C.multiply a b) ≡ multiply (embed-word a) (embed-word b)
embed-word-multiply a b i = Q.[ C.append-unit (C.multiply a b) (~ i) , C.zero-left b (~ i) ]
