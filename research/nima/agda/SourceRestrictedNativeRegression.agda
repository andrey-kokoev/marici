{-# OPTIONS --safe --cubical --guardedness #-}
module SourceRestrictedNativeRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Bool.Base using (false)
open import Cubical.Data.Empty.Base using (⊥)
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
import DependentArbitraryIndexRoutes as Routes
import NativeAtomicReachability as Atomic
import NativeNormalizationRouteCompiler as Compiler

module Obstruction {ℓ : Level}
  (I : Type ℓ) (J : I → Type ℓ)
  (K : (i : I) → J i → Type ℓ)
  (L : (i : I) (j : J i) → K i j → Type ℓ)
  (B : (i : I) (j : J i) (k : K i j) → L i j k → Type ℓ) where
  open Whole.Universe ℓ
  open Resolution.Generators ℓ
  module R = Routes.Routes I J K L B
  module A = Atomic.Reachability ℓ
  module C = Compiler.Compiler ℓ R.Q

  source : R.C.X → Complete
  source x = pack R.Q x

  first-outer : R.C.X → Complete
  first-outer x = pack (atom R.C.A1) (Iso.fun R.C.edgeA1 x)

  first-inner : R.C.X → Complete
  first-inner x = pack (atom R.C.B1) (Iso.fun R.C.edgeB1 x)

  terminal : R.C.X → Complete
  terminal x = pack (atom R.C.N) (Iso.fun R.C.routeA x)

  source-reachable : (x : R.C.X) → Resolve (A.OnlySource (source x)) (source x)
  source-reachable x = A.source-available (source x)

  outer-unreachable : (x : R.C.X)
    → Resolve (A.OnlySource (source x)) (first-outer x) → ⊥
  outer-unreachable x = A.no-new-atom (source x) refl R.C.A1 (Iso.fun R.C.edgeA1 x)

  inner-unreachable : (x : R.C.X)
    → Resolve (A.OnlySource (source x)) (first-inner x) → ⊥
  inner-unreachable x = A.no-new-atom (source x) refl R.C.B1 (Iso.fun R.C.edgeB1 x)

  terminal-unreachable : (x : R.C.X)
    → Resolve (A.OnlySource (source x)) (terminal x) → ⊥
  terminal-unreachable x = A.no-new-atom (source x) refl R.C.N (Iso.fun R.C.routeA x)

  -- These are the EXACT native compiler nodes, not substitute counterexamples.
  first-outer-rule : R.C.X → Rule
  first-outer-rule x = C.edge-rule {R.H.original} {R.A1} R.a1 x

  first-inner-rule : R.C.X → Rule
  first-inner-rule x = C.edge-rule {R.H.original} {R.B1} R.b1 x

  cannot-discharge-outer-premises : (x : R.C.X)
    → ((i : Arity (first-outer-rule x))
       → Resolve (A.OnlySource (source x)) (input (first-outer-rule x) i)) → ⊥
  cannot-discharge-outer-premises x ds = outer-unreachable x (ds (lift false))

  cannot-discharge-inner-premises : (x : R.C.X)
    → ((i : Arity (first-inner-rule x))
       → Resolve (A.OnlySource (source x)) (input (first-inner-rule x) i)) → ⊥
  cannot-discharge-inner-premises x ds = inner-unreachable x (ds (lift false))

  -- Providing precisely the intermediate seed discharges atomic reachability.
  seeded-intermediate : (x : R.C.X)
    → Resolve (A.OnlySource (first-outer x)) (first-outer x)
  seeded-intermediate x = A.source-available (first-outer x)
