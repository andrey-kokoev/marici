{-# OPTIONS --safe --cubical --guardedness #-}
module ObserverRRCComparisonBridge where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Sigma.Base using (Σ; _,_)
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (true≢false)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Relation.Nullary.Base using (Dec; yes; no)
import ObserverRRCWitnessSynthesis as S
import ObserverRRCRecursiveBridge as Recursive
module B = Recursive.Bridge ℓ-zero
module R = S.R
module U = S.U

-- The endpoint depends on the actual comparison witness, not only x,y.
DSolution : S.Mode → Bool → Bool → Type₁
DSolution m x y = Σ (S.Boundary m x y) (λ p →
  B.Term S.Source (U.comparison-package (S.packet x) (S.packet y) (S.equivalence m) p))

encode : {m : S.Mode} {x y : Bool} → S.Solution m x y → DSolution m x y
encode (S.solved p h) = p , B.encode h

decode : {m : S.Mode} {x y : Bool} → DSolution m x y → S.Solution m x y
decode (p , t) = S.solved p (B.decode t)

roundtrip-RRC : {m : S.Mode} {x y : Bool} (s : S.Solution m x y) → decode {m} {x} {y} (encode s) ≡ s
roundtrip-RRC (S.solved p h) i = S.solved p (B.decode-encode h i)

roundtrip-DSC : {m : S.Mode} {x y : Bool} (s : DSolution m x y) → encode (decode {m} {x} {y} s) ≡ s
roundtrip-DSC (p , t) i = p , B.encode-decode t i

solutions-equivalent : (m : S.Mode) (x y : Bool) → S.Solution m x y ≃ DSolution m x y
solutions-equivalent m x y = isoToEquiv
  (iso (encode {m} {x} {y}) (decode {m} {x} {y}) (roundtrip-DSC {m} {x} {y}) (roundtrip-RRC {m} {x} {y}))

-- Both successful witnesses AND certified impossibility cross the bridge.
synthesize : (m : S.Mode) (x y : Bool) → Dec (DSolution m x y)
synthesize m x y with S.synthesize m x y
... | yes s = yes (encode s)
... | no impossible = no (λ s → impossible (decode {m} {x} {y} s))

-- Same exact Complete endpoint, different retained rule constructors.
endpoint : U.Complete
endpoint = U.identity-comparison (S.packet true)

by-comparison by-identity : R.Resolve S.Source endpoint
by-comparison = S.history (S.construct S.identity true true refl)
by-identity = R.apply (R.identity-rule (S.packet true)) (λ _ → S.source true)

comparison-tag : R.Rule → Bool
comparison-tag (R.compare-rule a b e p) = true
comparison-tag _ = false

head-tag : {q : U.Complete} → R.Resolve S.Source q → Bool
head-tag (R.seed s) = false
head-tag (R.apply r ds) = comparison-tag r

raw-histories-distinct : by-comparison ≡ by-identity → ⊥
raw-histories-distinct p = true≢false (cong head-tag p)

translated-histories-distinct : B.encode by-comparison ≡ B.encode by-identity → ⊥
translated-histories-distinct p = raw-histories-distinct
  (sym (B.decode-encode by-comparison) ∙ cong B.decode p ∙ B.decode-encode by-identity)

-- Neither endpoint agreement nor the existence of a semantic comparison
-- licenses replacing these two raw derivations by one identical history.
