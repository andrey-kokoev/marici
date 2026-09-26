{-# OPTIONS --safe --cubical --guardedness #-}
module DependentReorderingLawInstance where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (true≢false)
open import Cubical.Data.Empty.Base using (⊥)
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
import WholeHistoryComparisons as Comparisons
import DependentArbitraryIndexRoutes as Routes
import DependentResolutionAlgebra as Algebra
import GeneratedNormalizationBridge as Bridge

module Instance {ℓ : Level}
  (I : Type ℓ) (J : I → Type ℓ)
  (K : (i : I) → J i → Type ℓ)
  (L : (i : I) (j : J i) → K i j → Type ℓ)
  (B : (i : I) (j : J i) (k : K i j) → L i j k → Type ℓ) where
  open Whole.Universe ℓ
  open Resolution.Generators ℓ
  module R = Routes.Routes I J K L B
  module H = R.H
  module A = Algebra.Interpretation ℓ
  module C = Comparisons.Comparisons ℓ A.Seed
  module O = C.Interpreted A.algebra

  finish : H.Route R.terminal H.normal
  finish = H.next {R = H.normal} (H.map-center R.terminal H.normal) H.stop

  outer-route inner-route : H.Route H.original H.normal
  outer-route = A.append R.outer-first finish
  inner-route = A.append R.inner-first finish

  endpoint : R.C.X → Complete
  endpoint x = pack R.Q x

  outer-history inner-history : (x : R.C.X) → Resolve A.Seed (endpoint x)
  outer-history x = seed outer-route
  inner-history x = seed inner-route

  -- One named, typed reordering schema, not an arbitrary semantic path.
  data Law : (q : Complete) → Resolve A.Seed q → Resolve A.Seed q → Type (ℓ-suc ℓ) where
    dependent-reorder : (x : R.C.X) → Law (endpoint x) (outer-history x) (inner-history x)

  interpret-law : (q : Complete) (d e : Resolve A.Seed q) → Law q d e → O.Semantic d e
  interpret-law _ _ _ (dependent-reorder x) =
    cong lift (H.route-comparison outer-route inner-route)

  module G = O.Structural Law interpret-law
  module NB = Bridge.Bridge ℓ A.Seed A.algebra A.carrier-code (λ _ → idEquiv _)
  module NG = NB.Structural Law interpret-law

  generated : (x : R.C.X) → G.Generated (outer-history x) (inner-history x)
  generated x = G.law (dependent-reorder x)

  -- The actual existing E/Pi rule constructors lift the law through an
  -- arbitrary dependent family of full input packages.
  family : (T : Type ℓ) → (T → R.C.X) → T → Complete
  family T xs t = endpoint (xs t)

  pi-left pi-right : (T : Type ℓ) (xs : T → R.C.X)
    → Resolve A.Seed (Pi-package T (family T xs))
  pi-left T xs = apply (Pi-rule T (family T xs)) (λ { (lift t) → outer-history (xs t) })
  pi-right T xs = apply (Pi-rule T (family T xs)) (λ { (lift t) → inner-history (xs t) })

  pi-generated : (T : Type ℓ) (xs : T → R.C.X) → G.Generated (pi-left T xs) (pi-right T xs)
  pi-generated T xs = G.congruence (Pi-rule T (family T xs))
    (λ { (lift t) → outer-history (xs t) })
    (λ { (lift t) → inner-history (xs t) })
    (λ { (lift t) → generated (xs t) })

  sum-left sum-right : (T : Type ℓ) (xs : T → R.C.X) (t : T)
    → Resolve A.Seed (E-package T (family T xs) t)
  sum-left T xs t = apply (E-rule T (family T xs) t) (λ { (lift j) → outer-history (xs j) })
  sum-right T xs t = apply (E-rule T (family T xs) t) (λ { (lift j) → inner-history (xs j) })

  sum-generated : (T : Type ℓ) (xs : T → R.C.X) (t : T)
    → G.Generated (sum-left T xs t) (sum-right T xs t)
  sum-generated T xs t = G.congruence (E-rule T (family T xs) t)
    (λ { (lift j) → outer-history (xs j) })
    (λ { (lift j) → inner-history (xs j) })
    (λ { (lift j) → generated (xs j) })

  is-four : {Q : Code} {P T : A.H.Presentation Q} → A.H.Route Q P T → Bool
  is-four (A.H.next _ (A.H.next _ (A.H.next _ (A.H.next _ A.H.stop)))) = true
  is-four _ = false

  route-records-distinct : outer-route ≡ inner-route → ⊥
  route-records-distinct p = true≢false (cong is-four p)

  history-tag : {q : Complete} → Resolve A.Seed q → Bool
  history-tag (seed r) = is-four r
  history-tag (apply _ _) = false

  history-records-distinct : (x : R.C.X) → outer-history x ≡ inner-history x → ⊥
  history-records-distinct x p = true≢false (cong (history-tag {endpoint x}) p)

  -- Retain the full source, seven-edge value trace, both embedded route
  -- histories, generated derivation and original/normalized witnesses.
  Retained : Type (ℓ-suc ℓ)
  Retained = Σ[ x ∈ R.C.X ] Σ[ trace ∈ R.C.Trace x ] NG.Retained

  retain-all : R.C.X → Retained
  retain-all x = x , R.C.canonicalTrace x , NG.retain-derivation (generated x)

  next-Q : R.C.X → Whole.Universe.Complete (ℓ-suc ℓ)
  next-Q x = Whole.Universe.pack (Whole.Universe.atom Retained) (retain-all x)

  source-retained : (x : R.C.X) → fst (Whole.Universe.value (next-Q x)) ≡ x
  source-retained x = refl
