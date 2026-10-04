{-# OPTIONS --safe --cubical --guardedness #-}
module RetainedNandPhases where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.HLevels using (isSetΣ; isPropΠ4)
open import Cubical.Data.Sigma using (_×_; Σ≡Prop)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Empty.Properties using (isProp⊥)
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (isSetBool; false≢true)
open import Cubical.Relation.Nullary.Base using (¬_; Stable)
open import Cubical.Relation.Nullary.Properties using (isProp¬)
import RetainedComparisonStructure as R
import RetainedActionYoneda as Y
import QBooleanity as Q
import NandConstructions as Old
import WholePackageSigmaPi as Whole

-- P and E are the CURRENT object/change fields, not the earlier sum/product
-- constructor names. Small set-valued actions are the question types here.
module Questions {ℓ : Level} (S : R.Structure ℓ) where
  open R.Structure S using (P; E; invE)
  module A = Y.Actions S
  open A.SetAction

  Question : Type (ℓ-max ℓ (ℓ-suc ℓ-zero))
  Question = A.SetAction ℓ-zero

  Natural : (X Z : Question) → ((p : P) → Carrier X p → Carrier Z p) → Type ℓ
  Natural X Z f = (p q : P) (e : E p q) (x : Carrier X p)
    → act Z e (f p x) ≡ f q (act X e x)

  natural-prop : (X Z : Question) (f : (p : P) → Carrier X p → Carrier Z p)
    → isProp (Natural X Z f)
  natural-prop X Z f = isPropΠ4 λ p q e x → carrier-set Z q _ _

  Map : Question → Question → Type ℓ
  Map X Z = Σ[ f ∈ ((p : P) → Carrier X p → Carrier Z p) ] Natural X Z f

  map-path : (X Z : Question) {f g : Map X Z}
    → ((p : P) (x : Carrier X p) → fst f p x ≡ fst g p x) → f ≡ g
  map-path X Z h = Σ≡Prop (natural-prop X Z) (funExt λ p → funExt (h p))

  compose : {X Z T : Question} → Map Z T → Map X Z → Map X T
  compose {X} {Z} {T} g f = (λ p x → fst g p (fst f p x)) ,
    λ p q e x → snd g p q e (fst f p x) ∙ cong (fst g q) (snd f p q e x)

  -- PHASE 1. Empty, joint answers, and empty-target function space.
  -- Empty elimination, Sigma pairs and Pi functions are ambient constructors.
  Zero : Question
  Zero = record
    { Carrier = λ _ → ⊥ ; carrier-set = λ _ → isProp→isSet isProp⊥
    ; act = λ e () ; act-unit = λ () ; act-comp = λ d e () }

  zero-initial : (Z : Question) → isContr (Map Zero Z)
  zero-initial Z = ((λ p ()) , (λ p q e ())) , λ f → map-path Zero Z (λ p ())

  Joint : Question → Question → Question
  Joint X Z = record
    { Carrier = λ p → Carrier X p × Carrier Z p
    ; carrier-set = λ p → isSetΣ (carrier-set X p) (λ _ → carrier-set Z p)
    ; act = λ e v → act X e (fst v) , act Z e (snd v)
    ; act-unit = λ v i → act-unit X (fst v) i , act-unit Z (snd v) i
    ; act-comp = λ d e v i → act-comp X d e (fst v) i , act-comp Z d e (snd v) i }

  pair-maps : {X Z T : Question} → Map X Z → Map X T → Map X (Joint Z T)
  pair-maps f g = (λ p x → fst f p x , fst g p x) ,
    λ p q e x i → snd f p q e x i , snd g p q e x i

  left-map : {X Z T : Question} → Map X (Joint Z T) → Map X Z
  left-map f = (λ p x → fst (fst f p x)) , λ p q e x → cong fst (snd f p q e x)

  right-map : {X Z T : Question} → Map X (Joint Z T) → Map X T
  right-map f = (λ p x → snd (fst f p x)) , λ p q e x → cong snd (snd f p q e x)

  joint-universal : (X Z T : Question) → Map X (Joint Z T) ≃ (Map X Z × Map X T)
  joint-universal X Z T = isoToEquiv record
    { fun = λ f → left-map {X} {Z} {T} f , right-map {X} {Z} {T} f
    ; inv = λ { (f , g) → pair-maps {X} {Z} {T} f g }
    ; rightInv = λ { (f , g) i →
        map-path X Z {f = left-map {X} {Z} {T} (pair-maps {X} {Z} {T} f g)} {g = f} (λ p x → refl) i ,
        map-path X T {f = right-map {X} {Z} {T} (pair-maps {X} {Z} {T} f g)} {g = g} (λ p x → refl) i }
    ; leftInv = λ f → map-path X (Joint Z T)
        {f = pair-maps {X} {Z} {T} (left-map {X} {Z} {T} f) (right-map {X} {Z} {T} f)} {g = f}
        (λ p x → refl) }

  Nand : Question → Question → Question
  Nand X Z = record
    { Carrier = λ p → ¬ (Carrier X p × Carrier Z p)
    ; carrier-set = λ p → isProp→isSet (isProp¬ (Carrier X p × Carrier Z p))
    ; act = λ e n v → n (act X (invE e) (fst v) , act Z (invE e) (snd v))
    ; act-unit = λ {p} n → isProp¬ (Carrier X p × Carrier Z p) _ _
    ; act-comp = λ {p} {q} {r} d e n → isProp¬ (Carrier X r × Carrier Z r) _ _ }

  -- Retaining the inputs is a separate operation from taking their truth
  -- result. The input action records, including their laws, remain fields.
  record RetainedNand : Type (ℓ-max ℓ (ℓ-suc ℓ-zero)) where
    field
      left-input right-input : Question
    result : Question
    result = Nand left-input right-input

  retain-nand : Question → Question → RetainedNand
  retain-nand X Z = record { left-input = X ; right-input = Z }

  recover-left : (X Z : Question) → RetainedNand.left-input (retain-nand X Z) ≡ X
  recover-left X Z = refl

  recover-right : (X Z : Question) → RetainedNand.right-input (retain-nand X Z) ≡ Z
  recover-right X Z = refl

  -- This is a comparison of VALUE types at a retained object p. It does not
  -- erase old constructor annotations or assert equivalence of whole Q codes.
  old-constructor-comparison : (X Z : Question) (p : P)
    → Carrier (Nand X Z) p ≃ Whole.Universe.El ℓ-zero (Old.nandCode (Carrier X p) (Carrier Z p))
  old-constructor-comparison X Z p = idEquiv _

  nand-prop : (X Z : Question) (p : P) → isProp (Carrier (Nand X Z) p)
  nand-prop X Z p = isProp¬ (Carrier X p × Carrier Z p)

  curry-refutation : (X Z T : Question) → Map (Joint X (Joint Z T)) Zero → Map X (Nand Z T)
  curry-refutation X Z T f = (λ p x zt → fst f p (x , zt)) ,
    λ p q e x → nand-prop Z T q _ _

  uncurry-refutation : (X Z T : Question) → Map X (Nand Z T) → Map (Joint X (Joint Z T)) Zero
  uncurry-refutation X Z T f = (λ p v → fst f p (fst v) (snd v)) ,
    λ p q e v → isProp⊥ _ _

  nand-universal : (X Z T : Question)
    → Map X (Nand Z T) ≃ Map (Joint X (Joint Z T)) Zero
  nand-universal X Z T = isoToEquiv record
    { fun = uncurry-refutation X Z T ; inv = curry-refutation X Z T
    ; rightInv = λ f → map-path (Joint X (Joint Z T)) Zero (λ p v → refl)
    ; leftInv = λ f → map-path X (Nand Z T) (λ p x → refl) }

  on-first : {X Y Z T : Question} → Map Y X → Map (Joint Y (Joint Z T)) (Joint X (Joint Z T))
  on-first {Z = Z} {T = T} h = (λ p v → fst h p (fst v) , snd v) ,
    λ p q e v i → snd h p q e (fst v) i , act (Joint Z T) e (snd v)

  -- Naturality in the test question: the two evaluation routes agree as maps,
  -- including their equivariance proofs, not just as unstructured functions.
  universal-natural : (X Y Z T : Question) (h : Map Y X) (f : Map X (Nand Z T))
    → uncurry-refutation Y Z T (compose {Y} {X} {Nand Z T} f h)
      ≡ compose {Joint Y (Joint Z T)} {Joint X (Joint Z T)} {Zero}
          (uncurry-refutation X Z T f) (on-first {X} {Y} {Z} {T} h)
  universal-natural X Y Z T h f = map-path (Joint Y (Joint Z T)) Zero (λ p v → refl)

  -- PHASE 2. Exact value of the Wolfram expression, before any Boolean claim.
  Double : Question → Question
  Double X = record
    { Carrier = λ p → Q.D (Carrier X p)
    ; carrier-set = λ p → isProp→isSet (isProp¬ (¬ (Carrier X p)))
    ; act = λ e nn n → nn (λ x → n (act X e x))
    ; act-unit = λ {p} nn → isProp¬ (¬ (Carrier X p)) _ _
    ; act-comp = λ {p} {q} {r} d e nn → isProp¬ (¬ (Carrier X r)) _ _ }

  W : Question → Question → Question → Question
  W X Z T = Nand (Nand (Nand X Z) T) (Nand X (Nand (Nand X T) X))

  record ActionIso (X Z : Question) : Type ℓ where
    field
      forward : Map X Z
      backward : Map Z X
      recover-source : (p : P) (x : Carrier X p) → fst backward p (fst forward p x) ≡ x
      recover-target : (p : P) (z : Carrier Z p) → fst forward p (fst backward p z) ≡ z

  at-point : {X Z : Question} → ActionIso X Z → (p : P) → Carrier X p ≃ Carrier Z p
  at-point i p = isoToEquiv record
    { fun = fst (ActionIso.forward i) p ; inv = fst (ActionIso.backward i) p
    ; leftInv = ActionIso.recover-source i p ; rightInv = ActionIso.recover-target i p }

  prop-action-iso : (X Z : Question)
    → ((p : P) → isProp (Carrier X p)) → ((p : P) → isProp (Carrier Z p))
    → ((p : P) → Carrier X p ≃ Carrier Z p) → ActionIso X Z
  prop-action-iso X Z propX propZ eq = record
    { forward = (λ p → equivFun (eq p)) , λ p q e x → propZ q _ _
    ; backward = (λ p → invEq (eq p)) , λ p q e z → propX q _ _
    ; recover-source = λ p → retEq (eq p)
    ; recover-target = λ p → secEq (eq p) }

  wolfram-double : (X Z T : Question) → ActionIso (W X Z T) (Double T)
  wolfram-double X Z T = prop-action-iso (W X Z T) (Double T)
    (λ p → isProp¬ _) (λ p → isProp¬ _)
    (λ p → Q.wolfram-double (Carrier X p) (Carrier Z p) (Carrier T p))

  wolfram-stable : (X Z T : Question)
    → ((p : P) → isProp (Carrier T p)) → ((p : P) → Stable (Carrier T p))
    → ActionIso (W X Z T) T
  wolfram-stable X Z T prop stable = prop-action-iso (W X Z T) T
    (λ p → isProp¬ _) prop
    (λ p → Q.wolfram-stable (Carrier X p) (Carrier Z p) (Carrier T p) (prop p) (stable p))

  wolfram-necessary : (X Z T : Question) → ActionIso (W X Z T) T
    → (p : P) → isProp (Carrier T p) × Stable (Carrier T p)
  wolfram-necessary X Z T i p =
    Q.wolfram-implies-prop (Carrier X p) (Carrier Z p) (Carrier T p) (at-point i p) ,
    Q.wolfram-implies-stable (Carrier X p) (Carrier Z p) (Carrier T p) (fst (ActionIso.forward i) p)

  -- The previous truth reflection also respects retained changes.
  reflection-universal : (X T : Question)
    → ((p : P) → isProp (Carrier T p)) → ((p : P) → Stable (Carrier T p))
    → Map (Double X) T ≃ Map X T
  reflection-universal X T prop stable = isoToEquiv record
    { fun = λ f → (λ p x → fst f p (Q.eta x)) , λ p q e x → prop q _ _
    ; inv = λ f → (λ p → Q.extend-stable (stable p) (fst f p)) , λ p q e x → prop q _ _
    ; rightInv = λ f → map-path X T (λ p x → prop p _ _)
    ; leftInv = λ f → map-path (Double X) T (λ p x → prop p _ _) }

  -- A set-valued question can still have two different answers.
  ConstantBool : Question
  ConstantBool = record
    { Carrier = λ _ → Bool ; carrier-set = λ _ → isSetBool
    ; act = λ e b → b ; act-unit = λ b → refl ; act-comp = λ d e b → refl }

  no-boolean-recovery : (recover : Q.D Bool → Bool)
    → ((b : Bool) → recover (Q.eta b) ≡ b) → ⊥
  no-boolean-recovery recover law = false≢true
    (sym (law false) ∙ cong recover Q.collapsed-alternatives ∙ law true)

  no-wolfram-on-all-sets : (p : P) → ActionIso (W ConstantBool ConstantBool ConstantBool) ConstantBool → ⊥
  no-wolfram-on-all-sets p i = false≢true (fst (wolfram-necessary ConstantBool ConstantBool ConstantBool i p) false true)

module Model = Questions R.example

concrete-nonboolean-question :
  Model.ActionIso (Model.W Model.ConstantBool Model.ConstantBool Model.ConstantBool) Model.ConstantBool → ⊥
concrete-nonboolean-question = Model.no-wolfram-on-all-sets false
