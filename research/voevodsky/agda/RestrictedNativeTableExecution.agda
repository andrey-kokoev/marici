{-# OPTIONS --safe --cubical --guardedness #-}
module RestrictedNativeTableExecution where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import RestrictedSeedArityProfile
import NativeTableRules
import NativeTableResolution
import WholePackageSigmaPi

module N = NativeTableRules.Native ℓ-zero
module C = NativeTableResolution.ForOldSeeds ℓ-zero Seed

native-family : N.G.Package → N.G.Package → Bool → N.G.Package
native-family a b false = a
native-family a b true = b

family-agreement : (a b : WholePackageSigmaPi.Universe.Complete ℓ-zero)
  → native-family (N.G.encode-package a) (N.G.encode-package b)
    ≡ (λ i → N.G.encode-package (family a b i))
family-agreement a b = funExt (λ { false → refl ; true → refl })

-- Native operations perform the work; no old-code decoder occurs here.
native : Term → N.G.Package
native (literal false-seed) = N.pack (N.G.atom-node Bool) false
native (identity t) = N.identity-comparison (native t)
native (pair t u) = N.Pi-package Bool (native-family (native t) (native u))
native (select b t u) = N.E-package Bool (native-family (native t) (native u)) b

agreement : (t : Term) → native t ≡ N.G.encode-package (eval t)
agreement (literal false-seed) = refl
agreement (identity t) = cong N.identity-comparison (agreement t)
  ∙ sym (N.output-commutes (G.identity-rule (eval t)))
agreement (pair t u) = cong₂ (λ a b → N.Pi-package Bool (native-family a b))
  (agreement t) (agreement u)
  ∙ cong (N.Pi-package Bool) (family-agreement (eval t) (eval u))
  ∙ sym (N.output-commutes (G.Pi-rule Bool (family (eval t) (eval u))))
agreement (select b t u) = cong₂ (λ a c → N.E-package Bool (native-family a c) b)
  (agreement t) (agreement u)
  ∙ cong (λ f → N.E-package Bool f b) (family-agreement (eval t) (eval u))
  ∙ sym (N.output-commutes (G.E-rule Bool (family (eval t) (eval u)) b))

old-closed : (t : Term) → G.Closure Seed
old-closed t = eval t , compile t

native-closed : Term → C.F.Closed
native-closed t = equivFun C.closure-equivalence (old-closed t)

native-history-endpoint : (t : Term) → fst (native-closed t) ≡ native t
native-history-endpoint t = C.endpoint-commutes (old-closed t) ∙ sym (agreement t)

original-derivation-recovered : (t : Term)
  → invEq C.closure-equivalence (native-closed t) ≡ old-closed t
original-derivation-recovered t = retEq C.closure-equivalence (old-closed t)

-- Syntax is retained separately: endpoint equality is not syntax identity.
RetainedNative : Type₁
RetainedNative = Σ[ t ∈ Term ] (Σ[ d ∈ C.F.Closed ] (fst d ≡ native t))

run-native : Term → RetainedNative
run-native t = t , native-closed t , native-history-endpoint t

syntax-recovered : (t : Term) → fst (run-native t) ≡ t
syntax-recovered t = refl
