{-# OPTIONS --safe --cubical --guardedness #-}
module UniversalSubstitution where
open import Cubical.Foundations.Prelude renaming (_∙_ to trans)
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.HLevels
open import Cubical.Data.Unit using (Unit; tt)
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Relation.Nullary.Base using (¬_)
import WholePackageSigmaPi as Whole
import BoundaryGeneratedQuestions as Boundary

-- Reversibility of substitution is a property of an actual map, not merely
-- a comparison of endpoint truth values.
module Substitution (A B : Type) (f : A → B) where
  pre : (X : Type) → (B → X) → (A → X)
  pre X h a = h (f a)
  Universal : Type₁
  Universal = (X : Type) → isEquiv (pre X)
  TwoTests : Type
  TwoTests = isEquiv (pre A) × isEquiv (pre B)

  two-to-iso : TwoTests → Iso A B
  two-to-iso (testA , testB) = result where
    ia = equivToIso (pre A , testA)
    ib = equivToIso (pre B , testB)
    g : B → A
    g = Iso.inv ia (λ a → a)
    section-proof : (a : A) → g (f a) ≡ a
    section-proof a = cong (λ h → h a) (Iso.rightInv ia (λ a → a))
    injective : (u v : B → B) → pre B u ≡ pre B v → u ≡ v
    injective u v p = trans (sym (Iso.leftInv ib u))
      (trans (cong (Iso.inv ib) p) (Iso.leftInv ib v))
    retraction-proof : (b : B) → f (g b) ≡ b
    retraction-proof b = cong (λ h → h b)
      (injective (λ b → f (g b)) (λ b → b) (funExt (λ a → cong f (section-proof a))))
    result : Iso A B
    Iso.fun result = f
    Iso.inv result = g
    Iso.rightInv result = retraction-proof
    Iso.leftInv result = section-proof

  two-to-equiv : TwoTests → isEquiv f
  two-to-equiv t = isoToIsEquiv (two-to-iso t)
  universal-to-equiv : Universal → isEquiv f
  universal-to-equiv all = two-to-equiv (all A , all B)

  equiv-to-universal : isEquiv f → Universal
  equiv-to-universal e X = isoToIsEquiv result where
    i = equivToIso (f , e)
    result : Iso (B → X) (A → X)
    Iso.fun result = pre X
    Iso.inv result k b = k (Iso.inv i b)
    Iso.rightInv result k = funExt (λ a → cong k (Iso.leftInv i a))
    Iso.leftInv result h = funExt (λ b → cong h (Iso.rightInv i b))

  universal-characterization : Universal ≃ isEquiv f
  universal-characterization = isoToEquiv record
    { fun = universal-to-equiv ; inv = equiv-to-universal
    ; rightInv = λ e → isPropIsEquiv f _ e
    ; leftInv = λ all → isPropΠ (λ X → isPropIsEquiv (pre X)) _ all }

  post : (X : Type) → (X → A) → (X → B)
  post X h x = f (h x)
  post-unit-to-equiv : isEquiv (post Unit) → isEquiv f
  post-unit-to-equiv test = isoToIsEquiv result where
    i = equivToIso (post Unit , test)
    result : Iso A B
    Iso.fun result = f
    Iso.inv result b = Iso.inv i (λ _ → b) tt
    Iso.rightInv result b = cong (λ h → h tt) (Iso.rightInv i (λ _ → b))
    Iso.leftInv result a = cong (λ h → h tt) (Iso.leftInv i (λ _ → a))

-- Sigma and Pi are the two context-extension adjunctions. These are
-- equivalences of entire map types, with explicit inverse operations.
sigma-adjunction : (I : Type) (A : I → Type)
  (B : (i : I) → A i → Type) (C : I → Type)
  → ((i : I) → (Σ (A i) (B i)) → C i)
      ≃ ((i : I) (a : A i) → B i a → C i)
sigma-adjunction I A B C = isoToEquiv record
  { fun = λ h i a b → h i (a , b)
  ; inv = λ k i → λ { (a , b) → k i a b }
  ; rightInv = λ k → refl ; leftInv = λ h → refl }

pi-adjunction : (I : Type) (A : I → Type)
  (B : (i : I) → A i → Type) (C : I → Type)
  → ((i : I) (a : A i) → C i → B i a)
      ≃ ((i : I) → C i → (a : A i) → B i a)
pi-adjunction I A B C = isoToEquiv record
  { fun = λ k i c a → k i a c ; inv = λ h i a c → h i c a
  ; rightInv = λ h → refl ; leftInv = λ k → refl }

-- A candidate E or P is forced up to value equivalence by its universal
-- extension property. Existence and the chosen index family are not inferred.
module SumSelection (I : Type) (A : I → Type) (S : Type)
  (inject : (i : I) → A i → S) where
  assemble : Σ I A → S
  assemble (i , a) = inject i a
  restrict : (X : Type) → (S → X) → ((i : I) → A i → X)
  restrict X h i a = h (inject i a)
  curry-iso : (X : Type) → Iso ((Σ I A) → X) ((i : I) → A i → X)
  Iso.fun (curry-iso X) h i a = h (i , a)
  Iso.inv (curry-iso X) k (i , a) = k i a
  Iso.rightInv (curry-iso X) k = refl
  Iso.leftInv (curry-iso X) h = refl
  universal-selects-sum : ((X : Type) → isEquiv (restrict X)) → isEquiv assemble
  universal-selects-sum tests = Substitution.universal-to-equiv (Σ I A) S assemble
    (λ X → snd (compEquiv (restrict X , tests X) (invEquiv (isoToEquiv (curry-iso X)))))

module ProductSelection (I : Type) (A : I → Type) (P : Type)
  (project : P → (i : I) → A i) where
  restrict : (X : Type) → (X → P) → ((i : I) → X → A i)
  restrict X h i x = project (h x) i
  curry-iso : (X : Type) → Iso (X → (i : I) → A i) ((i : I) → X → A i)
  Iso.fun (curry-iso X) h i x = h x i
  Iso.inv (curry-iso X) k x i = k i x
  Iso.rightInv (curry-iso X) k = refl
  Iso.leftInv (curry-iso X) h = refl
  universal-selects-product : ((X : Type) → isEquiv (restrict X)) → isEquiv project
  universal-selects-product tests = Substitution.post-unit-to-equiv P ((i : I) → A i) project
    (snd (compEquiv (restrict Unit , tests Unit) (invEquiv (isoToEquiv (curry-iso Unit)))))

-- The comparison evidence is recovered from substitution tests and the
-- selected-value boundary. No equivalence witness is assumed here.
module Q = Whole.Universe ℓ-zero
select-comparison : (a b : Q.Complete)
  (f : Q.El (Q.retained a) → Q.El (Q.retained b))
  → f (Q.value a) ≡ Q.value b
  → Substitution.Universal (Q.El (Q.retained a)) (Q.El (Q.retained b)) f
  → Boundary.Filler a b
select-comparison a b f p tests =
  (f , Substitution.universal-to-equiv _ _ f tests) , p

-- Testing only proposition-valued functions is strictly weaker.
collapse : Bool → Unit
collapse b = tt
collapse-passes-props : (P : Type) → isProp P
  → isEquiv (Substitution.pre Bool Unit collapse P)
collapse-passes-props P prop = isoToIsEquiv record
  { fun = Substitution.pre Bool Unit collapse P
  ; inv = λ h _ → h false
  ; rightInv = λ h → funExt (λ b → prop _ (h b))
  ; leftInv = λ k → funExt (λ { tt → refl }) }
collapse-not-equiv : ¬ (isEquiv collapse)
collapse-not-equiv e = false≢true
  (trans (sym (Iso.leftInv i false)) (Iso.leftInv i true))
  where i = equivToIso (collapse , e)

-- Bool-valued tests retain two distinguishable outputs and DO detect loss.
collapse-fails-bool-test : ¬ (isEquiv (Substitution.pre Bool Unit collapse Bool))
collapse-fails-bool-test test = false≢true
  (trans (sym (cong (λ h → h false) p)) (cong (λ h → h true) p))
  where
  i = equivToIso (Substitution.pre Bool Unit collapse Bool , test)
  p = Iso.rightInv i (λ b → b)

-- Retaining an input makes EVERY map reversible onto its graph. Thus
-- recoverability of an enlarged package alone cannot select allowed maps.
module GraphRetention {ℓ ℓ' : Level} (A : Type ℓ) (B : Type ℓ') (f : A → B) where
  Graph : Type (ℓ-max ℓ ℓ')
  Graph = Σ A (λ a → Σ B (λ b → f a ≡ b))
  enter : A → Graph
  enter a = a , f a , refl
  graph-iso : Iso A Graph
  Iso.fun graph-iso = enter
  Iso.inv graph-iso = fst
  Iso.leftInv graph-iso a = refl
  Iso.rightInv graph-iso (a , b , p) i = a , p i , (λ j → p (i ∧ j))
  input-recovered : (a : A) → fst (enter a) ≡ a
  input-recovered a = refl
  output-realized : (a : A) → fst (snd (enter a)) ≡ f a
  output-realized a = refl

-- Changing from value contexts to full retained contexts changes what
-- must be preserved. This result is an implication, not an identification
-- of arbitrary families of transport witnesses with paths.
FullTransport : Q.Complete → Q.Complete → Type₂
FullTransport a b = (P : Q.Complete → Type₁) → P a → P b
full-transport-to-path : (a b : Q.Complete) → FullTransport a b → a ≡ b
full-transport-to-path a b t = t (λ q → a ≡ q) refl
path-to-full-transport : (a b : Q.Complete) → a ≡ b → FullTransport a b
path-to-full-transport a b p P = subst P p

is-E : Q.Code → Bool
is-E (Q.E _ _) = true
is-E _ = false
unit-square-not-equal : ¬ (Boundary.unitQ ≡ Boundary.squareQ)
unit-square-not-equal p = false≢true (cong (λ q → is-E (Q.expression q)) p)
unit-square-no-full-transport : ¬ (FullTransport Boundary.unitQ Boundary.squareQ)
unit-square-no-full-transport t = unit-square-not-equal
  (full-transport-to-path Boundary.unitQ Boundary.squareQ t)
unit-square-value-tests : Substitution.Universal
  (Q.El (Q.retained Boundary.unitQ)) (Q.El (Q.retained Boundary.squareQ))
  (equivFun (fst Boundary.unit-square))
unit-square-value-tests = Substitution.equiv-to-universal _ _ _ (snd (fst Boundary.unit-square))
