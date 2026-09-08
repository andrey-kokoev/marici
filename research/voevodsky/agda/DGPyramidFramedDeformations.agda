{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidFramedDeformations where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)

record FirstConductorFramedDeformationCertificate {ℓ : Level}
  : Type (ℓ-suc ℓ) where
  field
    ConductorDegree Cycle Endpoint QClass MapClass Coeff : Type ℓ
    firstNegativeDegree : ConductorDegree
    cyclesAt : ConductorDegree → Type ℓ
    NineCycleFrame : Type ℓ
    nineCycleWitness : NineCycleFrame
    endpoint : Cycle → Endpoint
    qProjection : Cycle → QClass
    zeroEndpoint : Endpoint
    zeroQ : QClass
    framedCycle : Cycle
    framedCycleClosed : Type ℓ
    framedEndpointZero : endpoint framedCycle ≡ zeroEndpoint
    framedQZero : qProjection framedCycle ≡ zeroQ

    mapClassOf : Cycle → MapClass
    zeroMapClass : MapClass
    SixFixedGradeClasses : Type ℓ
    sixFixedGradeWitness : SixFixedGradeClasses
    framedMapNonzero : mapClassOf framedCycle ≡ zeroMapClass → ⊥
    Annihilator : MapClass → Type ℓ
    exactExampleAnnihilator : Annihilator (mapClassOf framedCycle)

    NegativeConductorIdeal StableCycleModule : Type ℓ
    stableNegativeModule : StableCycleModule
    stabilityAllNonnegativeWeights : Type ℓ
    stabilityWitness : stabilityAllNonnegativeWeights
    PhysicalConormalSelection : StableCycleModule → Type ℓ

record CoherentEndpointQFrameCertificate {ℓ : Level}
  : Type (ℓ-suc ℓ) where
  field
    CompleteComplex BoundaryObject Kernel HomotopyFibre : Type ℓ
    boundaryMap : CompleteComplex → BoundaryObject
    kernel : Kernel
    fibre : HomotopyFibre
    fibreToKernel : HomotopyFibre → Kernel
    kernelToFibre : Kernel → HomotopyFibre
    fibreKernelSection : (k : Kernel) → fibreToKernel (kernelToFibre k) ≡ k
    fibreKernelRetraction : (f : HomotopyFibre) → kernelToFibre (fibreToKernel f) ≡ f

    BoundaryClass Coeff : Type ℓ
    chi : BoundaryClass
    zeroBoundary : BoundaryClass
    chiNonzero : chi ≡ zeroBoundary → ⊥
    detector : BoundaryClass → Coeff
    one zeroCoeff : Coeff
    detectorChi : detector chi ≡ one
    oneNonzero : one ≡ zeroCoeff → ⊥

    OrdinaryBoundaryClass : Type ℓ
    forgetFrame : BoundaryClass → OrdinaryBoundaryClass
    ordinaryChi : OrdinaryBoundaryClass
    forgetChi : forgetFrame chi ≡ ordinaryChi

    CoherentMapClass PrimaryClass : Type ℓ
    coherentMapToPrimary : CoherentMapClass → PrimaryClass
    TwelveCoherentClasses : Type ℓ
    twelveCoherentWitness : TwelveCoherentClasses
    primaryChangeIsomorphism : Type ℓ
    primaryChangeWitness : primaryChangeIsomorphism

    FixedPrimaryFibre : PrimaryClass → Type ℓ
    Contractible : Type ℓ → Type ℓ
    nonemptyFixedPrimaryContractible : (p : PrimaryClass) →
      FixedPrimaryFibre p → Contractible (FixedPrimaryFibre p)
    attemptedPrimary : PrimaryClass
    attemptedPrimaryFibreEmpty : FixedPrimaryFibre attemptedPrimary → ⊥

coherentFrameRetainsTransgression : {ℓ : Level}
  (C : CoherentEndpointQFrameCertificate {ℓ}) →
  CoherentEndpointQFrameCertificate.chi C ≡
  CoherentEndpointQFrameCertificate.zeroBoundary C → ⊥
coherentFrameRetainsTransgression C =
  CoherentEndpointQFrameCertificate.chiNonzero C
