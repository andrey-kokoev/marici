{-# OPTIONS --safe --cubical --guardedness #-}
module QBooleanity where
open import Cubical.Foundations.Prelude renaming (_∙_ to trans)
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.HLevels
open import Cubical.Foundations.Univalence using (ua)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Empty.Properties using (isProp⊥)
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.Sigma.Properties using (Σ≡Prop)
open import Cubical.Data.Sum.Base using (_⊎_; inl; inr)
open import Cubical.Relation.Nullary.Base using (¬_; Stable)
open import Cubical.Relation.Nullary.Properties using (isProp¬; Stable¬)
import WholePackageSigmaPi as Whole
open import BooleanNandEquivalence using (BooleanStructure; module FromWolfram)

D : Type → Type
D A = ¬ ¬ A
eta : {A : Type} → A → D A
eta a na = na a
N : Type → Type → Type
N A B = ¬ (A × B)
W : Type → Type → Type → Type
W A B C = N (N (N A B) C) (N A (N (N A C) A))

-- Exact constructive value of the Wolfram term: double negation, not C.
w-to-double : {A B C : Type} → W A B C → D C
w-to-double w nc = w
  ((λ { (nab , c) → nc c }) ,
   (λ { (a , h) → h ((λ { (a' , c) → nc c }) , a) }))
double-to-w : {A B C : Type} → D C → W A B C
double-to-w dc (x , y) = dc λ c →
  x ((λ { (a , b) → y (a , (λ { (nac , a') → nac (a' , c) })) }) , c)

wolfram-double : (A B C : Type) → W A B C ≃ D C
wolfram-double A B C = isoToEquiv record
  { fun = w-to-double ; inv = double-to-w
  ; rightInv = λ d → isProp¬ (¬ C) _ d
  ; leftInv = λ w → isProp¬ ((N (N A B) C) × (N A (N (N A C) A))) _ w }

stable-equivalence : (A : Type) → isProp A → Stable A → D A ≃ A
stable-equivalence A prop stable = isoToEquiv record
  { fun = stable ; inv = eta
  ; rightInv = λ a → prop _ a
  ; leftInv = λ d → isProp¬ (¬ A) _ d }

-- Stability is exactly the missing implication for propositional C.
wolfram-stable : (A B C : Type) → isProp C → Stable C → W A B C ≃ C
wolfram-stable A B C prop stable =
  compEquiv (wolfram-double A B C) (stable-equivalence C prop stable)
wolfram-implies-stable : (A B C : Type) → (W A B C → C) → Stable C
wolfram-implies-stable A B C back d = back (double-to-w d)

idempotent : (A : Type) → D (D A) ≃ D A
idempotent A = stable-equivalence (D A) (isProp¬ (¬ A)) Stable¬

wolfram-implies-prop : (A B C : Type) → W A B C ≃ C → isProp C
wolfram-implies-prop A B C e c d =
  trans (sym (Iso.rightInv i c))
    (trans (cong (Iso.fun i) (isProp¬ ((N (N A B) C) × (N A (N (N A C) A)))
      (Iso.inv i c) (Iso.inv i d))) (Iso.rightInv i d))
  where i = equivToIso e

extend-stable : {A P : Type} → Stable P → (A → P) → D A → P
extend-stable stable f d = stable (λ np → d (λ a → np (f a)))
reflection : (A P : Type) → isProp P → Stable P → (D A → P) ≃ (A → P)
reflection A P prop stable = isoToEquiv record
  { fun = λ g a → g (eta a)
  ; inv = extend-stable stable
  ; rightInv = λ f → funExt (λ a → prop _ (f a))
  ; leftInv = λ g → funExt (λ d → prop _ (g d)) }

join-reflection : (A B : Type) → N (N A A) (N B B) ≃ D (A ⊎ B)
join-reflection A B = isoToEquiv record
  { fun = λ j ns → j ((λ { (a , a') → ns (inl a) }) , (λ { (b , b') → ns (inr b) }))
  ; inv = λ d → λ { (na , nb) → d (λ { (inl a) → na (a , a) ; (inr b) → nb (b , b) }) }
  ; rightInv = λ d → isProp¬ (¬ (A ⊎ B)) _ d
  ; leftInv = λ j → isProp¬ (N A A × N B B) _ j }

-- Full Boolean algebra of stable propositions, without supplied Bool indices.
StableTruth : Type₁
StableTruth = Σ (hProp ℓ-zero) (λ P → Stable (fst P))
prop-stability : (P : hProp ℓ-zero) → isProp (Stable (fst P))
prop-stability P = isPropΠ (λ _ → snd P)
set-stable-truth : isSet StableTruth
set-stable-truth = isSetΣ isSetHProp (λ P → isProp→isSet (prop-stability P))
carrier : StableTruth → Type
carrier P = fst (fst P)
false-truth : StableTruth
false-truth = (⊥ , isProp⊥) , (λ nn → nn (λ x → x))
_⊼_ : StableTruth → StableTruth → StableTruth
A ⊼ B = (N (carrier A) (carrier B) , isProp¬ (carrier A × carrier B)) , Stable¬

stable-wolfram : (a b c : StableTruth)
  → ((a ⊼ b) ⊼ c) ⊼ (a ⊼ ((a ⊼ c) ⊼ a)) ≡ c
stable-wolfram a b c = Σ≡Prop prop-stability
  (Σ≡Prop (λ _ → isPropIsProp)
    (ua (wolfram-stable (carrier a) (carrier b) (carrier c) (snd (fst c)) (snd c))))
module StableBoolean = FromWolfram StableTruth set-stable-truth false-truth _⊼_ stable-wolfram
boolean-structure : BooleanStructure StableTruth
boolean-structure = StableBoolean.boolean
module TruthAlgebra = BooleanStructure boolean-structure

top-witness : carrier TruthAlgebra.top
top-witness (n , ())
nontrivial : ¬ (TruthAlgebra.bottom ≡ TruthAlgebra.top)
nontrivial p = (subst carrier (sym p) top-witness) (top-witness , top-witness)

booleanize : Type → StableTruth
booleanize A = (D A , isProp¬ (¬ A)) , Stable¬

-- The same double-negation operation inside the existing Q code signature.
open Whole.Universe ℓ-zero
negCode : Code → Code
negCode C = Pi (El C) (λ _ → atom ⊥)
booleanCode : Code → Code
booleanCode C = negCode (negCode C)
booleanize-complete : Complete → Complete
booleanize-complete q = pack (booleanCode (retained q)) (eta (value q))

-- Inhabitation of a complete package is already witnessed: this readout is
-- always true. Nontrivial truth must concern a specified predicate/fibre.
complete-boolean-contractible : (q : Complete)
  → isContr (El (retained (booleanize-complete q)))
complete-boolean-contractible q = eta (value q) , λ d → isProp¬ (¬ (El (retained q))) _ d

-- Retained alternatives are lost by this truth-valued operation.
collapsed-alternatives : eta {A = Bool} false ≡ eta true
collapsed-alternatives = isProp¬ (¬ Bool) _ _
no-equivalence : ¬ (Bool ≃ D Bool)
no-equivalence e = false≢true
  (trans (sym (Iso.leftInv i false))
    (trans (cong (Iso.inv i) (isProp¬ (¬ Bool) (Iso.fun i false) (Iso.fun i true)))
      (Iso.leftInv i true)))
  where i = equivToIso e
