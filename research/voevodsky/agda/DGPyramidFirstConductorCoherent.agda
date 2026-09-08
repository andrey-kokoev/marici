{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidFirstConductorCoherent where

open import Cubical.Foundations.Prelude

record FirstConductorCoherentPrimaryCertificate {ℓ : Level}
  : Type (ℓ-suc ℓ) where
  field
    CompleteComplex BoundaryObject Kernel Fibre : Type ℓ
    boundaryMap : CompleteComplex → BoundaryObject
    fibreToKernel : Fibre → Kernel
    kernelToFibre : Kernel → Fibre
    fibreKernelSection : (k : Kernel) → fibreToKernel (kernelToFibre k) ≡ k
    fibreKernelRetraction : (f : Fibre) → kernelToFibre (fibreToKernel f) ≡ f

    PrimaryFramedCochain TopChain : Type ℓ
    differential : PrimaryFramedCochain → PrimaryFramedCochain
    projectionToTop : PrimaryFramedCochain → TopChain
    inclusionFromTop : TopChain → PrimaryFramedCochain
    projectionSection : (z : TopChain) →
      projectionToTop (inclusionFromTop z) ≡ z
    PrimaryFibreRetraction : Type ℓ
    primaryFibreRetractionWitness : PrimaryFibreRetraction

    OccurrenceWeight Component : Type ℓ
    weight02 weight04 weight13 weight15 weight24 weight35 : OccurrenceWeight
    componentsAt : OccurrenceWeight → Type ℓ
    ComponentRanks9977919 : Type ℓ
    componentRanksWitness : ComponentRanks9977919
    TotalComponentLattice : Type ℓ
    sixtyComponentWitness : TotalComponentLattice
    Contractible : Type ℓ → Type ℓ
    eachComponentContractible : (c : Component) → Contractible Component

    OrdinaryMapLattice PrimaryChangeLattice ForgetfulKernel : Type ℓ
    forgetPrimaryHomotopy : TotalComponentLattice → OrdinaryMapLattice
    primaryChange : OrdinaryMapLattice → PrimaryChangeLattice
    TwentyFourKernel : Type ℓ
    twentyFourKernelWitness : TwentyFourKernel
    SeventyTwoOrdinary : Type ℓ
    seventyTwoWitness : SeventyTwoOrdinary
    ThirtySixPrimaryChanges : Type ℓ
    thirtySixWitness : ThirtySixPrimaryChanges
    forgetfulExactSequence : Type ℓ
    forgetfulExactWitness : forgetfulExactSequence

    NativeExample OccurrencePartnerExample : Type ℓ
    nativeExample : NativeExample
    occurrencePartnerExample : OccurrencePartnerExample
    ordinaryOccurrenceBoundary : Type ℓ
    framedOccurrenceNontrivial : Type ℓ

    SourcePrimaryHomotopySelection :
      OccurrenceWeight → TotalComponentLattice → Type ℓ
