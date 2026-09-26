{-# OPTIONS --safe --cubical --guardedness #-}
module GuardedUnaryHistoryRecognitionRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (notEquiv; false≢true)
open import Cubical.Data.Unit.Base using (Unit; tt; tt*)
open import Cubical.Data.Empty.Base using (⊥)
import WholePackageSigmaPi as Whole
import GuardedUnaryHistoryRecognition as Recognition
import SigmaPiComparisonDecomposition as Decomposition

open Whole.Universe ℓ-zero
module G = Recognition.Recognition ℓ-zero (atom Bool) true
module D = Decomposition.Decomposition ℓ-zero

root-chart = G.H.N.normalize-equiv (atom Bool)
root : G.T.ResolveT G.Source G.source
root = G.T.seedT G.origin

first = G.T.transported G.source (atom Bool) (idEquiv Bool)
first-history : G.T.ResolveT G.Source first
first-history = G.T.transportT G.source (atom Bool) (idEquiv Bool) root
first-guard : G.Guarded first-history root-chart
first-guard = G.move G.source (atom Bool) (idEquiv Bool) root root-chart root-chart G.base (λ _ → refl)

second = G.T.transported first (atom Bool) (idEquiv Bool)
second-history : G.T.ResolveT G.Source second
second-history = G.T.transportT first (atom Bool) (idEquiv Bool) first-history
second-guard : G.Guarded second-history root-chart
second-guard = G.move first (atom Bool) (idEquiv Bool) first-history root-chart root-chart first-guard (λ _ → refl)

-- Histories above were written directly with transportT, not compiled.
module P = G.Pair first-guard second-guard

abstract
  requested-witness : P.Semantic
  requested-witness = G.H.compare-maps {G.H.original} {G.H.normal}
    (G.observed first-guard) (G.observed second-guard)

reconstructed : Σ[ p ∈ P.Derivation ] (P.sound p ≡ requested-witness)
reconstructed = P.completeness requested-witness

next-input : Whole.Universe.Complete (ℓ-suc ℓ-zero)
next-input = G.next-Q (G.retain-recognition first-guard second-guard requested-witness)

first-raw-history-retained : G.Retained.first-history (Whole.Universe.value next-input) ≡ first-history
first-raw-history-retained = refl
second-raw-history-retained : G.Retained.second-history (Whole.Universe.value next-input) ≡ second-history
second-raw-history-retained = refl

actual-first : G.actual first-guard true ≡ value first
actual-first = G.actual-at-source first-guard
actual-second : G.actual second-guard true ≡ value second
actual-second = G.actual-at-source second-guard

-- Negation fails the FIXED identity target chart's pointwise guard.
negation-guard-impossible :
  ((b : Bool) → equivFun root-chart (equivFun notEquiv b) ≡ equivFun root-chart b) → ⊥
negation-guard-impossible guard = false≢true (cong (λ v → snd v tt*) (guard true))

-- A real native history even has a faithful endpoint chart, but remains
-- outside this unary recognizer. No native coverage is inferred silently.
identity-rule = G.Old.identity-rule G.source
native-history = G.T.nativeT identity-rule (λ _ → root)
native-chart : G.Chart (G.Old.output identity-rule)
native-chart = compEquiv
  (D.comparison-projection (retained G.source) (retained G.source) (idEquiv Bool)) root-chart

native-case-excluded : G.Guarded native-history native-chart → ⊥
native-case-excluded = G.native-not-recognized identity-rule (λ _ → root) native-chart

-- Stronger coverage obstruction: a genuinely indexed native E-node is
-- reachable from one source, but has NO faithful chart to that source's
-- fixed normal type. Adding a syntactic native case alone cannot repair it.
module U = Recognition.Recognition ℓ-zero (atom Unit) tt
branch-rule = U.Old.E-rule Bool (λ _ → U.source) true
branch-history : U.T.ResolveT U.Source (U.Old.output branch-rule)
branch-history = U.T.nativeT branch-rule (λ _ → U.T.seedT U.origin)

source-normal-contractible : isContr U.Normal
source-normal-contractible = U.H.N.normalize (atom Unit) tt , (λ _ → refl)

branch-chart-impossible : U.Chart (U.Old.output branch-rule) → ⊥
branch-chart-impossible c = false≢true (cong fst
  (sym (retEq c (false , tt))
   ∙ cong (invEq c)
       (isContr→isProp source-normal-contractible (equivFun c (false , tt)) (equivFun c (true , tt)))
   ∙ retEq c (true , tt)))
