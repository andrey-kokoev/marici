{-# OPTIONS --safe --cubical --guardedness #-}
module SingleSourceRouteCompilerRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv using (idEquiv)
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import Cubical.Data.FinData.Base using () renaming (zero to fzero)
open import Cubical.Data.Maybe.Base using (Maybe; just; nothing)
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (notEquiv; false≢true)
open import Cubical.Data.Empty.Base using (⊥)
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
import NativeAtomicReachability as Atomic
import SingleSourceRouteCompiler as Compiler
import DependentReorderingLawRegression as Example
import IndexIdentityCoherenceRegression as Loop

module R = Example.R.R
module C = Compiler.Compiler ℓ-zero R.Q
module Old = Resolution.Generators ℓ-zero
module A = Atomic.Reachability ℓ-zero
open Whole.Universe ℓ-zero

x = Example.source
initial = C.start R.H.original x
outer = C.run R.outer-first initial
inner = C.run R.inner-first initial

outer-history = C.source-compile R.outer-first x
inner-history = C.source-compile R.inner-first x
outer-one-seed = C.source-one-seed R.outer-first x
inner-one-seed = C.source-one-seed R.inner-first x

-- Count on the unary certificate, not on a potentially infinite native tree.
steps : {S : Complete → Type₁} {q : Complete} {d : C.T.ResolveT S q}
  → C.T.TransportOnly d → ℕ
steps (C.T.one-seed _) = 0
steps (C.T.one-step _ _ _ _ p) = suc (steps p)

outer-three : steps outer-one-seed ≡ 3
outer-three = refl
inner-four : steps inner-one-seed ≡ 4
inner-four = refl

rewind : ℕ → Complete → Maybe Complete
rewind zero q = just q
rewind (suc n) q with C.T.previous q
... | nothing = nothing
... | just p = rewind n p

whole-source-recovered-outer : rewind 3 (C.packet outer) ≡ just (C.packet initial)
whole-source-recovered-outer = refl
whole-source-recovered-inner : rewind 4 (C.packet inner) ≡ just (C.packet initial)
whole-source-recovered-inner = refl

same-effect : C.viewed-value outer ≡ C.viewed-value inner
same-effect = C.run-agrees R.outer-first initial
  ∙ C.N.effects-agree R.outer-first R.inner-first x
  ∙ sym (C.run-agrees R.inner-first initial)

-- The output is still wrapped. We have not manufactured the old forbidden
-- bare atomic endpoint or weakened the old signature's invariant.
outer-still-wrapped : A.atomic (C.packet outer) ≡ false
outer-still-wrapped = refl

old-first-target-still-unreachable :
  Old.Resolve (C.OnlySource (C.packet initial))
    (pack (atom R.C.A1) (fst (R.a1 x))) → ⊥
old-first-target-still-unreachable =
  A.no-new-atom (C.packet initial) refl R.C.A1 (fst (R.a1 x))

empty-route = R.H.stop {P = R.H.original}
empty-history = C.source-compile empty-route x
empty-one-seed = C.source-one-seed empty-route x
empty-zero : steps empty-one-seed ≡ 0
empty-zero = refl

next-input = C.next-Q (C.retain-compilation R.outer-first x)

route-retained : C.Retained.route (Whole.Universe.value next-input) ≡ R.outer-first
route-retained = refl

retained-loop-nontrivial :
  snd (snd ((C.Retained.input-value (Whole.Universe.value next-input)) 0) fzero) ≡ refl → ⊥
retained-loop-nontrivial = Loop.loop-is-not-reflexive

-- The extension admits real equivalences, not just normalization-preserving
-- ones. A future cross-endpoint comparison must retain its coordinate guard.
bool-source = pack (atom Bool) true
negated = C.T.transported bool-source (atom Bool) notEquiv
unchanged = C.T.transported bool-source (atom Bool) (idEquiv Bool)

negated-history : C.T.ResolveT (C.OnlySource bool-source) negated
negated-history = C.T.transportT bool-source (atom Bool) notEquiv (C.T.seedT refl)
unchanged-history : C.T.ResolveT (C.OnlySource bool-source) unchanged
unchanged-history = C.T.transportT bool-source (atom Bool) (idEquiv Bool) (C.T.seedT refl)

arbitrary-transport-effects-not-equal : value negated ≡ value unchanged → ⊥
arbitrary-transport-effects-not-equal = false≢true
