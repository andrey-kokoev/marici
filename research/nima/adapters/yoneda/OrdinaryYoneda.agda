{-# OPTIONS --safe --cubical --guardedness #-}
module OrdinaryYoneda where

open import Cubical.Foundations.Prelude hiding (comp)
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.HLevels using (isPropΠ4)
open import Cubical.Data.Sigma using (Σ≡Prop)

-- No inverses, four-channel assumption, or reconstruction map is supplied.
record Category (o h : Level) : Type (ℓ-suc (ℓ-max o h)) where
  field
    Ob : Type o
    Hom : Ob → Ob → Type h
    hom-set : (a b : Ob) → isSet (Hom a b)
    unit : {a : Ob} → Hom a a
    comp : {a b c : Ob} → Hom b c → Hom a b → Hom a c
    unitL : {a b : Ob} (f : Hom a b) → comp unit f ≡ f
    unitR : {a b : Ob} (f : Hom a b) → comp f unit ≡ f
    assoc : {a b c d : Ob} (k : Hom c d) (g : Hom b c) (f : Hom a b)
      → comp k (comp g f) ≡ comp (comp k g) f

module Theorem {o h : Level} (C : Category o h) where
  open Category C

  record Presheaf (v : Level) : Type (ℓ-max (ℓ-max o h) (ℓ-suc v)) where
    field
      Obj : Ob → Type v
      obj-set : (a : Ob) → isSet (Obj a)
      pull : {a b : Ob} → Hom a b → Obj b → Obj a
      pull-unit : {a : Ob} (x : Obj a) → pull unit x ≡ x
      pull-comp : {a b c : Ob} (g : Hom b c) (f : Hom a b) (x : Obj c)
        → pull f (pull g x) ≡ pull (comp g f) x

  module At {v : Level} (F : Presheaf v) (a : Ob) where
    open Presheaf F
    Raw : Type (ℓ-max (ℓ-max o h) v)
    Raw = (x : Ob) → Hom x a → Obj x
    NaturalLaw : Raw → Type (ℓ-max (ℓ-max o h) v)
    NaturalLaw α = (x y : Ob) (f : Hom x y) (g : Hom y a)
      → pull f (α y g) ≡ α x (comp g f)
    law-prop : (α : Raw) → isProp (NaturalLaw α)
    law-prop α = isPropΠ4 (λ x y f g → obj-set x _ _)
    Natural : Type (ℓ-max (ℓ-max o h) v)
    Natural = Σ Raw NaturalLaw
    evaluate : Natural → Obj a
    evaluate α = fst α a unit
    extend : Obj a → Natural
    extend z = (λ x f → pull f z) , (λ x y f g → pull-comp g f z)
    evaluate-extend : (z : Obj a) → evaluate (extend z) ≡ z
    evaluate-extend = pull-unit
    extend-evaluate : (α : Natural) → extend (evaluate α) ≡ α
    extend-evaluate α = Σ≡Prop law-prop (funExt λ x → funExt λ f →
      snd α x a f unit ∙ cong (fst α x) (unitL f))
    yoneda : Iso Natural (Obj a)
    yoneda = iso evaluate extend evaluate-extend extend-evaluate
    unique-extension : (z : Obj a) → isContr (Σ[ α ∈ Natural ] (evaluate α ≡ z))
    unique-extension z = equiv-proof (snd (isoToEquiv yoneda)) z

  record Transformation {v : Level} (F G : Presheaf v)
    : Type (ℓ-max (ℓ-max o h) v) where
    field
      component : (x : Ob) → Presheaf.Obj F x → Presheaf.Obj G x
      natural : (x y : Ob) (f : Hom x y) (z : Presheaf.Obj F y)
        → Presheaf.pull G f (component y z) ≡ component x (Presheaf.pull F f z)

  postcompose : {v : Level} {F G : Presheaf v} → Transformation F G
    → (a : Ob) → At.Natural F a → At.Natural G a
  postcompose η a α = (λ x f → Transformation.component η x (fst α x f)) ,
    (λ x y f g → Transformation.natural η x y f (fst α y g)
      ∙ cong (Transformation.component η x) (snd α x y f g))
  evaluation-natural-F : {v : Level} {F G : Presheaf v} (η : Transformation F G)
    (a : Ob) (α : At.Natural F a)
    → At.evaluate G a (postcompose η a α) ≡ Transformation.component η a (At.evaluate F a α)
  evaluation-natural-F η a α = refl

  precompose : {v : Level} (F : Presheaf v) {a b : Ob} → Hom a b
    → At.Natural F b → At.Natural F a
  precompose F f α = (λ x g → fst α x (comp f g)) ,
    (λ x y d g → snd α x y d (comp f g) ∙ cong (fst α x) (sym (assoc f g d)))
  evaluation-natural-a : {v : Level} (F : Presheaf v) {a b : Ob} (f : Hom a b)
    (α : At.Natural F b)
    → At.evaluate F a (precompose F f α) ≡ Presheaf.pull F f (At.evaluate F b α)
  evaluation-natural-a F {a} {b} f α = cong (fst α a) (unitR f)
    ∙ sym (cong (fst α a) (unitL f)) ∙ sym (snd α a b f unit)

  representable : Ob → Presheaf h
  representable b = record
    { Obj = λ x → Hom x b
    ; obj-set = λ x → hom-set x b
    ; pull = λ f g → comp g f
    ; pull-unit = unitR
    ; pull-comp = λ g f k → sym (assoc k g f) }

  -- Nat(Hom(-,a), Hom(-,b)) ≃ Hom(a,b), not merely an encoding of Hom.
  fully-faithful : (a b : Ob) → At.Natural (representable b) a ≃ Hom a b
  fully-faithful a b = isoToEquiv (At.yoneda (representable b) a)

  embedding : {a b : Ob} → Hom a b → At.Natural (representable b) a
  embedding {a} {b} = At.extend (representable b) a
  embedding-component : {a b x : Ob} (f : Hom a b) (g : Hom x a)
    → fst (embedding f) x g ≡ comp f g
  embedding-component f g = refl
  embedding-identity : {a x : Ob} (g : Hom x a) → fst (embedding unit) x g ≡ g
  embedding-identity = unitL
  embedding-composition : {a b c x : Ob} (k : Hom b c) (f : Hom a b) (g : Hom x a)
    → fst (embedding (comp k f)) x g ≡ fst (embedding k) x (fst (embedding f) x g)
  embedding-composition k f g = sym (assoc k f g)
