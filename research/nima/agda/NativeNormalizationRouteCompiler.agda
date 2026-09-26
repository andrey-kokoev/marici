{-# OPTIONS --safe --cubical --guardedness #-}
module NativeNormalizationRouteCompiler where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Unit.Base using (Unit*; tt*)
open import Cubical.Data.Empty.Base using (⊥*)
open import Cubical.Data.Sum.Base using (_⊎_; inl; inr)
open import Cubical.Data.Bool.Base using (true; false)
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
import DependentNormalizationCoherence as Coherence
import NormalizationComparisonBasis as Basis

module Compiler (ℓ : Level) (Q : Whole.Universe.Code ℓ) where
  open Whole.Universe ℓ
  open Resolution.Generators ℓ
  module H = Coherence.Coherence ℓ Q
  module B = Basis.Basis ℓ
  open H.Presentation

  at : (P : H.Presentation) → El (expression P) → Complete
  at P x = pack (expression P) x

  underlying : {P R : H.Presentation} → H.CoherentMap P R
    → El (expression P) → El (expression R)
  underlying f x = fst (f x)

  -- A coordinate-preserving map is an equivalence. Its underlying function
  -- remains the supplied map, not a replacement by its canonical centre.
  map-equiv : {P R : H.Presentation} → H.CoherentMap P R
    → El (expression P) ≃ El (expression R)
  map-equiv {P} {R} f = (λ x → fst (f x)) ,
    subst isEquiv (cong (underlying {P} {R})
      (H.compare-maps {P} {R} (H.map-center P R) f))
      (snd (compEquiv (coordinates P) (invEquiv (coordinates R))))

  edge-package : {P R : H.Presentation} (f : H.CoherentMap P R)
    → El (expression P) → Complete
  edge-package {P} {R} f x = comparison-package (at P x) (at R (fst (f x))) (map-equiv {P} {R} f) refl

  edge-rule : {P R : H.Presentation} (f : H.CoherentMap P R)
    → El (expression P) → Rule
  edge-rule {P} {R} f x = compare-rule (at P x) (at R (fst (f x))) (map-equiv {P} {R} f) refl

  native-edge : {P R : H.Presentation} (f : H.CoherentMap P R) (x : El (expression P))
    → Resolve B.A.Seed (edge-package {P} {R} f x)
  native-edge {P} {R} f x = apply (edge-rule {P} {R} f x)
    (λ { (lift true) → B.canonical (at P x)
       ; (lift false) → B.canonical (at R (fst (f x))) })

  Slots : {P R : H.Presentation} → H.Route P R → Type ℓ
  Slots H.stop = ⊥* {ℓ = ℓ}
  Slots (H.next _ tail) = Unit* {ℓ = ℓ} ⊎ Slots tail

  packages : {P R : H.Presentation} (route : H.Route P R)
    → El (expression P) → Slots route → Complete
  packages H.stop x ()
  packages {P} (H.next {R = R} f tail) x (inl _) = edge-package {P} {R} f x
  packages (H.next f tail) x (inr i) = packages tail (fst (f x)) i

  native-steps : {P R : H.Presentation} (route : H.Route P R) (x : El (expression P))
    → (i : Slots route) → Resolve B.A.Seed (packages route x i)
  native-steps H.stop x ()
  native-steps {P} (H.next {R = R} f tail) x (inl _) = native-edge {P} {R} f x
  native-steps (H.next f tail) x (inr i) = native-steps tail (fst (f x)) i

  batch : {P R : H.Presentation} (route : H.Route P R) → El (expression P) → Complete
  batch route x = Pi-package (Slots route) (packages route x)

  compile : {P R : H.Presentation} (route : H.Route P R) (x : El (expression P))
    → Resolve B.A.Seed (batch route x)
  compile route x = apply (Pi-rule (Slots route) (packages route x))
    (λ { (lift i) → native-steps route x i })

  -- Compilation never leaves an opaque multi-step route as a tree seed.
  data CanonicalLeaves : {q : Complete} → Resolve B.A.Seed q → Type (ℓ-suc ℓ) where
    canonical-leaf : (q : Complete) → CanonicalLeaves (B.canonical q)
    native-node : (r : Rule) (ds : (i : Arity r) → Resolve B.A.Seed (input r i))
      → ((i : Arity r) → CanonicalLeaves (ds i)) → CanonicalLeaves (apply r ds)

  edge-leaves : {P R : H.Presentation} (f : H.CoherentMap P R) (x : El (expression P))
    → CanonicalLeaves (native-edge {P} {R} f x)
  edge-leaves {P} {R} f x = native-node (edge-rule {P} {R} f x) _
    (λ { (lift true) → canonical-leaf (at P x)
       ; (lift false) → canonical-leaf (at R (fst (f x))) })

  steps-leaves : {P R : H.Presentation} (route : H.Route P R) (x : El (expression P))
    → (i : Slots route) → CanonicalLeaves (native-steps route x i)
  steps-leaves H.stop x ()
  steps-leaves {P} (H.next {R = R} f tail) x (inl _) = edge-leaves {P} {R} f x
  steps-leaves (H.next f tail) x (inr i) = steps-leaves tail (fst (f x)) i

  compile-leaves : {P R : H.Presentation} (route : H.Route P R) (x : El (expression P))
    → CanonicalLeaves (compile route x)
  compile-leaves route x = native-node (Pi-rule (Slots route) (packages route x)) _
    (λ { (lift i) → steps-leaves route x i })

  execute : {P R : H.Presentation} → H.Route P R → El (expression P) → El (expression R)
  execute H.stop x = x
  execute (H.next f tail) x = execute tail (fst (f x))

  execution-agrees : {P R : H.Presentation} (route : H.Route P R) (x : El (expression P))
    → execute route x ≡ fst (H.evaluate route x)
  execution-agrees H.stop x = refl
  execution-agrees (H.next f tail) x = execution-agrees tail (fst (f x))

  effects-agree : {P R : H.Presentation} (a b : H.Route P R) (x : El (expression P))
    → execute a x ≡ execute b x
  effects-agree {P} {R} a b x = execution-agrees a x
    ∙ cong (λ g → underlying {P} {R} g x) (H.route-comparison a b)
    ∙ sym (execution-agrees b x)

  record Retained : Type (ℓ-suc ℓ) where
    constructor compiled
    field
      source target : H.Presentation
      route : H.Route source target
      input-value : El (expression source)
      output-value : El (expression target)
      agrees : output-value ≡ fst (H.evaluate route input-value)
      native-history : Resolve B.A.Seed (batch route input-value)
      canonical-boundaries : CanonicalLeaves native-history

  retain-compilation : {P R : H.Presentation} → H.Route P R → El (expression P) → Retained
  retain-compilation {P} {R} route x = compiled P R route x (execute route x)
    (execution-agrees route x) (compile route x) (compile-leaves route x)

  next-Q : Retained → Whole.Universe.Complete (ℓ-suc ℓ)
  next-Q c = Whole.Universe.pack (Whole.Universe.atom Retained) c

  -- The two batch endpoints may differ. Keep both, and compare their
  -- sequential effects; never coerce them to an invented common endpoint.
  record Compared : Type (ℓ-suc ℓ) where
    constructor compared-native
    field
      source target : H.Presentation
      first second : H.Route source target
      input-value : El (expression source)
      first-native : Resolve B.A.Seed (batch first input-value)
      second-native : Resolve B.A.Seed (batch second input-value)
      first-boundaries : CanonicalLeaves first-native
      second-boundaries : CanonicalLeaves second-native
      effect-witness : execute first input-value ≡ execute second input-value

  compare-compilations : {P R : H.Presentation} → H.Route P R → H.Route P R
    → El (expression P) → Compared
  compare-compilations {P} {R} a b x = compared-native P R a b x
    (compile a x) (compile b x) (compile-leaves a x) (compile-leaves b x) (effects-agree a b x)

  next-comparison-Q : Compared → Whole.Universe.Complete (ℓ-suc ℓ)
  next-comparison-Q c = Whole.Universe.pack (Whole.Universe.atom Compared) c
