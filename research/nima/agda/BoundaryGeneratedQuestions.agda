{-# OPTIONS --safe --cubical --guardedness #-}
module BoundaryGeneratedQuestions where
open import Cubical.Foundations.Prelude renaming (_∙_ to trans)
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Unit using (Unit; tt; isPropUnit)
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Relation.Nullary.Base using (¬_)
open import Cubical.Relation.Nullary.Properties using (isProp¬)
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
open import QBooleanity using (D; eta; StableTruth; booleanize)

open Whole.Universe ℓ-zero

-- Abstract exactly the missing evidence fields of the existing compare-rule.
Filler : Complete → Complete → Type
Filler a b = Σ (El (retained a) ≃ El (retained b))
  (λ e → equivFun e (value a) ≡ value b)

question : Complete → Complete → StableTruth
question a b = booleanize (Filler a b)

-- Merely asking for a point-preserving map is trivial on complete packages.
pointed-map-always : (a b : Complete)
  → Σ (El (retained a) → El (retained b)) (λ f → f (value a) ≡ value b)
pointed-map-always a b = (λ _ → value b) , refl

identity : (a : Complete) → Filler a a
identity a = idEquiv _ , refl
compose : {a b c : Complete} → Filler a b → Filler b c → Filler a c
compose (e , p) (f , q) = compEquiv e f , trans (cong (equivFun f) p) q
inverse : {a b : Complete} → Filler a b → Filler b a
inverse {a} {b} (e , p) = invEquiv e ,
  trans (cong (Iso.inv (equivToIso e)) (sym p)) (Iso.leftInv (equivToIso e) (value a))

-- An actual supplied boundary transport moves the question and its fillers.
transport-question : {a a' b b' : Complete}
  → Filler a' a → Filler b b' → Filler a b → Filler a' b'
transport-question {a} {a'} {b} {b'} left right middle =
  compose {a = a'} {b = b} {c = b'}
    (compose {a = a'} {b = a} {c = b} left middle) right

map-truth : {A B : Type} → (A → B) → D A → D B
map-truth f d nb = d (λ a → nb (f a))
transported-truth : {a a' b b' : Complete}
  → Filler a' a → Filler b b' → D (Filler a b) ≃ D (Filler a' b')
transported-truth {a} {a'} {b} {b'} left right = isoToEquiv record
  { fun = map-truth (transport-question {a} {a'} {b} {b'} left right)
  ; inv = map-truth (transport-question {a'} {a} {b'} {b}
      (inverse {a = a'} {b = a} left) (inverse {a = b} {b = b'} right))
  ; rightInv = λ d → isProp¬ (¬ (Filler a' b')) _ d
  ; leftInv = λ d → isProp¬ (¬ (Filler a b)) _ d }

module Application (S : Complete → Type₁) where
  open Resolution.Generators ℓ-zero
  rule : {a b : Complete} → Filler a b → Rule
  rule {a} {b} (e , p) = compare-rule a b e p
  perform : {a b : Complete} (f : Filler a b)
    → Resolve S a → Resolve S b → Resolve S (output (rule f))
  perform f da db = apply (rule f) (λ { (lift true) → da ; (lift false) → db })

  -- The general constructor and its applicability question share one boundary.
  Premises : Rule → Type₁
  Premises r = (i : Arity r) → Resolve S (input r i)
  extend-boundary : (r : Rule) → Premises r → Resolve S (output r)
  extend-boundary = apply

-- Boundary, map and compatibility witness can themselves be retained as Q.
retain-filler : (a b : Complete) → Filler a b → Complete
retain-filler a b f = remember a (remember b (pack (atom (Filler a b)) f))
filler-recovered : (a b : Complete) (f : Filler a b)
  → value (retain-filler a b f) ≡ f
filler-recovered a b f = refl

unitQ squareQ choiceQ fourQ : Complete
unitQ = pack (atom Unit) tt
squareQ = E-package Unit (λ _ → unitQ) tt
choiceQ = E-package Bool (λ _ → unitQ) false
fourQ = E-package Bool (λ _ → pack (atom Bool) false) false

unit-square-iso : Iso Unit (Unit × Unit)
Iso.fun unit-square-iso tt = tt , tt
Iso.inv unit-square-iso (tt , tt) = tt
Iso.rightInv unit-square-iso (tt , tt) = refl
Iso.leftInv unit-square-iso tt = refl
unit-square : Filler unitQ squareQ
unit-square = isoToEquiv unit-square-iso , refl
unit-square-true : D (Filler unitQ squareQ)
unit-square-true = eta unit-square

module ActualResolution where
  open Resolution.Generators ℓ-zero
  data Seeds : Complete → Type₁ where
    base : Seeds unitQ
  root : Resolve Seeds unitQ
  root = seed base
  square : Resolve Seeds squareQ
  square = apply (E-rule Unit (λ _ → unitQ) tt) (λ _ → root)
  choice : Resolve Seeds choiceQ
  choice = apply (E-rule Bool (λ _ → unitQ) false) (λ _ → root)
  module App = Application Seeds
  comparison-derived : Resolve Seeds (output (App.rule {a = unitQ} {b = squareQ} unit-square))
  comparison-derived = App.perform {a = unitQ} {b = squareQ} unit-square root square
  nextQ : Whole.Universe.Complete (ℓ-suc ℓ-zero)
  nextQ = reify-history comparison-derived
  retained-derivation : snd (Whole.Universe.value nextQ) ≡ comparison-derived
  retained-derivation = refl

-- Both Qs are complete, yet this signature-generated question is false.
unit-choice-impossible : ¬ (Filler unitQ choiceQ)
unit-choice-impossible (e , p) = false≢true
  (cong fst (trans (sym (Iso.rightInv i (false , tt)))
    (trans (cong (Iso.fun i) (isPropUnit (Iso.inv i (false , tt)) (Iso.inv i (true , tt))))
      (Iso.rightInv i (true , tt)))))
  where i = equivToIso e
unit-choice-false : ¬ D (Filler unitQ choiceQ)
unit-choice-false d = d unit-choice-impossible

-- One true question can retain different actual compatibility witnesses.
swap-iso : Iso (Bool × Bool) (Bool × Bool)
Iso.fun swap-iso (x , y) = y , x
Iso.inv swap-iso (x , y) = y , x
Iso.rightInv swap-iso (x , y) = refl
Iso.leftInv swap-iso (x , y) = refl
swap-filler : Filler fourQ fourQ
swap-filler = isoToEquiv swap-iso , refl
fillers-distinct : ¬ (identity fourQ ≡ swap-filler)
fillers-distinct p = false≢true
  (cong (λ f → fst (equivFun (fst f) (false , true))) p)
truth-identifies-fillers : eta (identity fourQ) ≡ eta swap-filler
truth-identifies-fillers = isProp¬ (¬ (Filler fourQ fourQ)) _ _
