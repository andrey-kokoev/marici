{-# OPTIONS --safe --cubical --guardedness #-}
module ObserverRRCSourceAdmission where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma.Base using (_×_; _,_)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Empty.Base using (⊥)
import WholePackageSigmaPi as W
import WholePackageResolution as RRC

-- A mathematical predicate over explicit rule values, NOT an external
-- permission grant. Source evidence and all rule witnesses remain supplied.
module Admission (ℓ : Level) (Allowed : RRC.Generators.Rule ℓ → Type (ℓ-suc ℓ)) where
  module U = W.Universe ℓ
  module R = RRC.Generators ℓ
  Source = U.Complete → Type (ℓ-suc ℓ)

  Admitted : {S : Source} {q : U.Complete} → R.Resolve S q → Type (ℓ-suc ℓ)
  Admitted (R.seed s) = Lift Unit
  Admitted (R.apply r ds) = Allowed r × ((i : R.Arity r) → Admitted (ds i))

  rename-admitted : {S T : Source} (f : (q : U.Complete) → S q → T q)
    {q : U.Complete} (d : R.Resolve S q) → Admitted d → Admitted (R.mapSeeds f d)
  rename-admitted f (R.seed s) a = lift tt
  rename-admitted f (R.apply r ds) (a , children) =
    a , (λ i → rename-admitted f (ds i) (children i))

  -- Outer permission alone says nothing about the histories stored in its
  -- seeds: every replacement must independently satisfy the SAME policy.
  substitute-admitted : {S T : Source} (f : (q : U.Complete) → S q → R.Resolve T q)
    → ((q : U.Complete) (s : S q) → Admitted (f q s))
    → {q : U.Complete} (d : R.Resolve S q) → Admitted d
    → Admitted (R.flatten (R.mapSeeds f d))
  substitute-admitted f replacements (R.seed s) a = replacements _ s
  substitute-admitted f replacements (R.apply r ds) (a , children) =
    a , (λ i → substitute-admitted f replacements (ds i) (children i))

  -- Counter-boundary in general form: a seed can hide any disallowed inner
  -- history; admitting the outer seed never certifies its flattening.
  outer-seed-admitted : {S : Source} {q : U.Complete} (d : R.Resolve S q)
    → Admitted (R.seed {S = R.Resolve S} {q = q} d)
  outer-seed-admitted d = lift tt

  flatten-seed : {S : Source} {q : U.Complete} (d : R.Resolve S q)
    → Admitted (R.flatten (R.seed d)) ≡ Admitted d
  flatten-seed d = refl

module Regression where
  module U = W.Universe ℓ-zero
  module R = RRC.Generators ℓ-zero
  module A = Admission ℓ-zero (λ _ → Lift ⊥)
  S : U.Complete → Type₁
  S _ = Lift Unit
  packet = U.pack (U.atom Unit) tt
  bad : R.Resolve S (R.output (R.identity-rule packet))
  bad = R.apply (R.identity-rule packet) (λ _ → R.seed (lift tt))
  rejected : A.Admitted bad → ⊥
  rejected (permission , _) = lower permission
  no-unchecked-flatten :
    ((q : U.Complete) (d : R.Resolve (R.Resolve S) q) → A.Admitted d → A.Admitted (R.flatten d)) → ⊥
  no-unchecked-flatten claimed = rejected (claimed _ (R.seed bad) (lift tt))
