{-# OPTIONS --safe --cubical --guardedness #-}
module ObserverRRCCompletenessBoundary where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma.Base using (_,_)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Bool.Properties using (true≢false)
open import Cubical.Data.Empty.Base using (⊥)
import WholePackageUniversalProperty as Universal
import WholeHistoryComparisons as Comparisons
import ObserverRRCWitnessSynthesis as S
import ObserverRRCComparisonBridge as Fixture
import ObserverRRCGeneratedBridge as Transfer

module R = S.R
module U = S.U
module V = Universal.Universal ℓ-zero S.Source
module C = Comparisons.Comparisons ℓ-zero S.Source

-- A legitimate but information-forgetting algebra, not claimed to be
-- the intended physical/operational semantics of resolution.
algebra : V.Algebra
algebra = record
  { Carrier = λ _ → Lift Unit
  ; on-seed = λ _ → lift tt
  ; on-rule = λ _ _ → lift tt
  }

collapse : {q : U.Complete} (d : R.Resolve S.Source q)
  → V.evaluate algebra d ≡ lift tt
collapse (R.seed s) = refl
collapse (R.apply r ds) = refl

module Sem = C.Interpreted algebra

-- A nonempty source law family: ALL laws preserving the outer rule tag.
-- This admits reflexivity and many pairs, not just an empty law theory.
Law : (q : U.Complete) → R.Resolve S.Source q → R.Resolve S.Source q → Type₁
Law q d e = Lift (Fixture.head-tag d ≡ Fixture.head-tag e)

interpret-law : (q : U.Complete) (d e : R.Resolve S.Source q) → Law q d e → Sem.Semantic d e
interpret-law q d e w = collapse d ∙ sym (collapse e)

module G = Sem.Structural Law interpret-law

-- Every constructor preserves the tag invariant. Congruence may change
-- all child histories but cannot change its supplied outer rule.
preserves-head : {q : U.Complete} {d e : R.Resolve S.Source q}
  → G.Generated d e → Fixture.head-tag d ≡ Fixture.head-tag e
preserves-head (G.reflexive d) = refl
preserves-head (G.invert c) = sym (preserves-head c)
preserves-head (G.concatenate c c') = preserves-head c ∙ preserves-head c'
preserves-head (G.law w) = lower w
preserves-head (G.congruence r ds es cs) = refl

same-semantics : Sem.Semantic Fixture.by-comparison Fixture.by-identity
same-semantics = refl

no-generated-route : G.Generated Fixture.by-comparison Fixture.by-identity → ⊥
no-generated-route c = true≢false (preserves-head c)

not-complete : G.Completeness → ⊥
not-complete complete with complete Fixture.endpoint Fixture.by-comparison Fixture.by-identity same-semantics
... | c , witness-agreement = no-generated-route c

module Bridge = Transfer.Bridge ℓ-zero S.Source
module Target = Bridge.Interpreted algebra Law interpret-law
module B = Bridge.B

same-translated-semantics : Target.Semantic
  (B.encode Fixture.by-comparison) (B.encode Fixture.by-identity)
same-translated-semantics = refl

no-translated-route : Target.Generated
  (B.encode Fixture.by-comparison) (B.encode Fixture.by-identity) → ⊥
no-translated-route c = no-generated-route (subst2 (λ d e → G.Generated d e)
  (B.decode-encode Fixture.by-comparison) (B.decode-encode Fixture.by-identity) (Target.reflect c))
