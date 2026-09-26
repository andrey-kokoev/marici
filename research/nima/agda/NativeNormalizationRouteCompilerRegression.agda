{-# OPTIONS --safe --cubical --guardedness #-}
module NativeNormalizationRouteCompilerRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (true≢false)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Nat.Base using (ℕ; suc)
open import Cubical.Data.FinData.Base using () renaming (zero to fzero)
open import Cubical.Data.Sum.Base using (inl; inr)
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
import NativeNormalizationRouteCompiler as Compiler
import DependentReorderingLawRegression as Example
import IndexIdentityCoherenceRegression as Loop

module R = Example.R.R
module C = Compiler.Compiler ℓ-zero R.Q
open Whole.Universe ℓ-zero
open Resolution.Generators ℓ-zero

x = Example.source
outer-native = C.compile R.outer-first x
inner-native = C.compile R.inner-first x

comparison-root : {q : Complete} → Resolve C.B.A.Seed q → Bool
comparison-root (apply (compare-rule _ _ _ _) _) = true
comparison-root _ = false

all-steps-native : {P T : R.H.Presentation} (route : R.H.Route P T)
  (v : El (R.H.Presentation.expression P)) (i : C.Slots route)
  → comparison-root (C.native-steps route v i) ≡ true
all-steps-native R.H.stop v ()
all-steps-native (R.H.next f tail) v (inl _) = refl
all-steps-native (R.H.next f tail) v (inr i) = all-steps-native tail (fst (f v)) i

steps : {P T : R.H.Presentation} → R.H.Route P T → ℕ
steps R.H.stop = 0
steps (R.H.next _ tail) = suc (steps tail)

three-native-steps : steps R.outer-first ≡ 3
three-native-steps = refl
four-native-steps : steps R.inner-first ≡ 4
four-native-steps = refl

outer-boundaries = C.compile-leaves R.outer-first x
inner-boundaries = C.compile-leaves R.inner-first x

-- An opaque four-step seed fails the compiler's canonical-leaf certificate.
opaque-seed-rejected : C.CanonicalLeaves (Example.R.outer-history x) → ⊥
opaque-seed-rejected ()

same-effect : C.execute R.outer-first x ≡ C.execute R.inner-first x
same-effect = C.effects-agree R.outer-first R.inner-first x

empty-route = R.H.stop {P = R.H.original}
empty-compilation = C.compile empty-route x
empty-boundaries = C.compile-leaves empty-route x
empty-effect : C.execute empty-route x ≡ x
empty-effect = refl

compared = C.compare-compilations R.outer-first R.inner-first x
next-input = C.next-comparison-Q compared

outer-record-retained : C.Compared.first (Whole.Universe.value next-input) ≡ R.outer-first
outer-record-retained = refl
inner-record-retained : C.Compared.second (Whole.Universe.value next-input) ≡ R.inner-first
inner-record-retained = refl

retained-loop-nontrivial :
  snd (snd ((C.Compared.input-value (Whole.Universe.value next-input)) 0) fzero) ≡ refl → ⊥
retained-loop-nontrivial = Loop.loop-is-not-reflexive
