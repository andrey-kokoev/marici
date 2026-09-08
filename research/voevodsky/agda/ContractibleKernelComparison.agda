{-# OPTIONS --safe --cubical --guardedness #-}
module ContractibleKernelComparison where

open import Cubical.Foundations.Prelude
open import BoundaryExtensionFibres

-- P and C are the relevant derived mapping spaces, NOT raw chain modules.
-- Exactness must supply the fibre models below. Kernel contractibility alone
-- does not imply that every fibre is inhabited (surjectivity is not omitted).
record KernelFibreCertificate {ℓ : Level} {P C : Type ℓ}
  (p : P → C) : Type (ℓ-suc ℓ) where
  field
    Kernel : C → Type ℓ
    kernelContractible : (c : C) → isContr (Kernel c)
    encode : (c : C) → Extension p c → Kernel c
    decode : (c : C) → Kernel c → Extension p c
    decodeEncode : (c : C) (x : Extension p c)
      → decode c (encode c x) ≡ x

-- A retract of a contractible type is contractible. No ambient section,
-- scalar-linear inverse, or ambient contracting homotopy is an input.
kernelComparison : {ℓ : Level} {P C : Type ℓ} {p : P → C}
  → KernelFibreCertificate p → UniqueExtensions p
kernelComparison certificate c =
  decode c (fst (kernelContractible c)) , λ x →
    cong (decode c) (snd (kernelContractible c) (encode c x))
      ∙ decodeEncode c x
  where
  open KernelFibreCertificate certificate

-- Admissibility belongs to the forward map. The supplied predicate may
-- express A-linearity in an independently constructed derived mapping model.
-- Merely naming a predicate does not establish such an interpretation.
record AdmissibleKernelComparison {ℓ : Level} {P C : Type ℓ}
  (p : P → C) (Admissible : (P → C) → Type ℓ)
  : Type (ℓ-suc ℓ) where
  field
    forwardAdmissible : Admissible p
    kernelCertificate : KernelFibreCertificate p

certifiedForwardEquivalence : {ℓ : Level} {P C : Type ℓ}
  {p : P → C} {Admissible : (P → C) → Type ℓ}
  → AdmissibleKernelComparison p Admissible
  → Σ (Admissible p) (λ _ → UniqueExtensions p)
certifiedForwardEquivalence certificate =
  forwardAdmissible , kernelComparison kernelCertificate
  where
  open AdmissibleKernelComparison certificate

-- Positive regression: many distinct boundary points, each with an
-- explicitly modeled contractible fibre. No global boundary selection.
unitContractible : isContr UnitReadout
unitContractible = unit , λ { unit → refl }

identityKernelCertificate : KernelFibreCertificate (λ (m : Marking) → m)
KernelFibreCertificate.Kernel identityKernelCertificate _ = UnitReadout
KernelFibreCertificate.kernelContractible identityKernelCertificate _ = unitContractible
KernelFibreCertificate.encode identityKernelCertificate _ _ = unit
KernelFibreCertificate.decode identityKernelCertificate m _ = m , refl
KernelFibreCertificate.decodeEncode identityKernelCertificate m x =
  snd (identityExtensions m) x

identityPositiveComparison : UniqueExtensions (λ (m : Marking) → m)
identityPositiveComparison = kernelComparison identityKernelCertificate

-- A section of a readout still cannot manufacture this positive certificate.
splitReadoutHasNoKernelCertificate : KernelFibreCertificate readout → Impossible
splitReadoutHasNoKernelCertificate certificate =
  normalized-fibre-not-contractible (kernelComparison certificate unit)

-- No field records an ambient splitting. An R-linear splitting can be stored
-- independently by a client, but cannot be substituted for fibre exactness.
-- An A-linear derived inverse is NOT an A-linear chain-level section.
