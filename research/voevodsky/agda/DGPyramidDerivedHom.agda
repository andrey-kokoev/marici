{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidDerivedHom where

open import Cubical.Foundations.Prelude

-- Certificate boundary for Stacks Project, More on Algebra: a bounded-above
-- projective source lets the ordinary Hom complex represent derived Hom.
record DerivedHomComputationCertificate {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    SourceComplex TargetComplex OrdinaryHomComplex DerivedHomObject : Type ℓ
    BoundedAboveProjective : SourceComplex → Type ℓ
    source : SourceComplex
    target : TargetComplex
    sourceIsBoundedAboveProjective : BoundedAboveProjective source

    ordinaryToDerived : OrdinaryHomComplex → DerivedHomObject
    derivedToOrdinary : DerivedHomObject → OrdinaryHomComplex
    ordinaryDerivedSection : (x : OrdinaryHomComplex) →
      derivedToOrdinary (ordinaryToDerived x) ≡ x
    ordinaryDerivedRetraction : (x : DerivedHomObject) →
      ordinaryToDerived (derivedToOrdinary x) ≡ x

    -- Hom-complex convention d(f)=d_M f-(-1)^n f d_L and its interpretation.
    HomDegree : Type ℓ
    HomCochain : HomDegree → Type ℓ
    homDifferential : HomDegree → HomDegree
    Closed : {n : HomDegree} → HomCochain n → Type ℓ
    Boundary : {n : HomDegree} → HomCochain n → Type ℓ
    ShiftedHomotopyClass : HomDegree → Type ℓ
    classOfClosed : {n : HomDegree} →
      (f : HomCochain n) → Closed f → ShiftedHomotopyClass n
    boundaryClassIsTrivial : {n : HomDegree} (f : HomCochain n) →
      Boundary f → Type ℓ

open DerivedHomComputationCertificate public

-- This record does not infer projectivity from finite matrix size. A concrete
-- importer must supply the bounded-free/projective witness.
