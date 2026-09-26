{-# OPTIONS --safe --cubical --guardedness #-}
module ObserverRRCDSCBridge where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Sigma.Base using (Σ; _,_; fst; snd)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (true≢false)
open import Cubical.Data.Empty.Base using (⊥)
import WholePackageSigmaPi as W
import WholePackageResolution as RRC
import ResolutionNetDependentSubstitution as DSC

-- Frozen shared fragment: one native E/Pi application with its ENTIRE
-- supplied input family and actual child derivations. No seed synthesis.
module Bridge (ℓ : Level) (Seed : W.Universe.Complete ℓ → Type (ℓ-suc ℓ)) (I : Type ℓ) where
  module U = W.Universe ℓ
  module R = RRC.Generators ℓ
  module D = DSC.Dependent {ℓ-suc ℓ}

  Inputs = Σ (I → U.Complete) (λ F → (i : I) → R.Resolve Seed (F i))
  Choice = Lift {j = ℓ-suc ℓ} I
  RBoundary = Σ (I → U.Complete) (λ F → Σ ((i : I) → R.Resolve Seed (F i)) (λ _ → Choice))
  DBoundary = Σ Inputs (λ _ → Choice)

  toDSC : RBoundary → DBoundary
  toDSC (F , children , i) = (F , children) , i
  toRRC : DBoundary → RBoundary
  toRRC ((F , children) , i) = F , children , i

  boundary-equivalence : RBoundary ≃ DBoundary
  boundary-equivalence = isoToEquiv (iso toDSC toRRC (λ _ → refl) (λ _ → refl))

  nativeE : RBoundary → R.Closure Seed
  nativeE (F , children , i) = R.output (R.E-rule I F (lower i)) ,
    R.apply (R.E-rule I F (lower i)) (λ j → children (lower j))

  -- The DSC continuation is explicitly the above native constructor,
  -- not an unconstrained host evaluator supplied as a primitive.
  continuation : DBoundary → R.Closure Seed
  continuation b = nativeE (toRRC b)

  execute : {Γ : Type (ℓ-suc ℓ)} → (Γ → Inputs) → (Γ → Choice) → Γ → R.Closure Seed
  execute inputs selected = D.execute (λ _ → R.Closure Seed) continuation inputs selected

  execution-agrees : {Γ : Type (ℓ-suc ℓ)} (inputs : Γ → Inputs) (selected : Γ → Choice) (γ : Γ)
    → execute inputs selected γ ≡ nativeE (toRRC (inputs γ , selected γ))
  execution-agrees inputs selected γ = refl

  e-substitution : {Γ Δ : Type (ℓ-suc ℓ)} (inputs : Γ → Inputs) (selected : Γ → Choice) (σ : Δ → Γ)
    → execute (D.compose inputs σ) (D.compose selected σ) ≡ D.compose (execute inputs selected) σ
  e-substitution inputs selected σ = refl

  RApplication = Σ RBoundary (λ b → Σ (R.Closure Seed) (λ out → nativeE b ≡ out))
  DApplication = Σ DBoundary (λ b → Σ (R.Closure Seed) (λ out → continuation b ≡ out))

  encode : RApplication → DApplication
  encode (b , out , witness) = toDSC b , out , witness
  decode : DApplication → RApplication
  decode (b , out , witness) = toRRC b , out , witness

  application-equivalence : RApplication ≃ DApplication
  application-equivalence = isoToEquiv (iso encode decode (λ _ → refl) (λ _ → refl))

  path-roundtrip : (a b : RApplication) (p : a ≡ b) → cong decode (cong encode p) ≡ p
  path-roundtrip a b p = refl

  retain-application : DApplication → W.Universe.Complete (ℓ-suc ℓ)
  retain-application a = W.Universe.pack (W.Universe.atom DApplication) a

  full-recovery : (a : RApplication)
    → decode (W.Universe.value (retain-application (encode a))) ≡ a
  full-recovery a = refl

  -- Π keeps the entire premise family; its DSC interface is already Inputs.
  nativePi : Inputs → R.Closure Seed
  nativePi (F , children) = R.output (R.Pi-rule I F) ,
    R.apply (R.Pi-rule I F) (λ j → children (lower j))

  executePi : {Γ : Type (ℓ-suc ℓ)} → (Γ → Inputs) → Γ → R.Closure Seed
  executePi inputs = D.compose nativePi inputs

  pi-substitution : {Γ Δ : Type (ℓ-suc ℓ)} (inputs : Γ → Inputs) (σ : Δ → Γ)
    → executePi (D.compose inputs σ) ≡ D.compose (executePi inputs) σ
  pi-substitution inputs σ = refl

-- Endpoint-only translation fails even when ONLY an unselected child's
-- raw seed label changes. The new bridge retains that actual distinction.
module Regression where
  module U = W.Universe ℓ-zero
  module R = RRC.Generators ℓ-zero
  Seed : U.Complete → Type₁
  Seed _ = Lift Bool
  module B = Bridge ℓ-zero Seed Bool

  packet : U.Complete
  packet = U.pack (U.atom Unit) tt

  label : {q : U.Complete} → R.Resolve Seed q → Bool
  label (R.seed b) = lower b
  label (R.apply r children) = true

  children₁ children₂ : (i : Bool) → R.Resolve Seed packet
  children₁ _ = R.seed (lift true)
  children₂ true = R.seed (lift true)
  children₂ false = R.seed (lift false)

  first second : B.RBoundary
  first = (λ _ → packet) , children₁ , lift true
  second = (λ _ → packet) , children₂ , lift true

  unselected : B.RBoundary → Bool
  unselected (F , children , i) = label (children false)

  boundaries-distinct : first ≡ second → ⊥
  boundaries-distinct e = true≢false (cong unselected e)

  same-endpoint : fst (B.nativeE first) ≡ fst (B.nativeE second)
  same-endpoint = refl

  encoded-boundaries-distinct : B.toDSC first ≡ B.toDSC second → ⊥
  encoded-boundaries-distinct e = boundaries-distinct (cong B.toRRC e)

  no-endpoint-inverse : (recover : U.Complete → B.RBoundary)
    → ((b : B.RBoundary) → recover (fst (B.nativeE b)) ≡ b) → ⊥
  no-endpoint-inverse recover exact = boundaries-distinct
    (sym (exact first) ∙ cong recover same-endpoint ∙ exact second)
