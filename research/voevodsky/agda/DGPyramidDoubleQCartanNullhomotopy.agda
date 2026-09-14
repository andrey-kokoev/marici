{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidDoubleQCartanNullhomotopy where

open import Cubical.Foundations.Prelude

-- Cartan calculus packages the useful part of the canonical double Q-manifold
-- (Pi T M, d, L_Q).  Signs are carried by homotopyBoundary rather than hidden
-- in an ungraded equation.
record CartanQCalculus {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    Forms : Type ℓ
    zeroForm : Forms
    negateForm : Forms → Forms
    deRhamD physicalLieDerivative contractionByQ : Forms → Forms
    homotopyBoundary : (Forms → Forms) → Forms → Forms

    deRhamSquared : (x : Forms) → deRhamD (deRhamD x) ≡ zeroForm
    physicalLieDerivativeSquared : (x : Forms) →
      physicalLieDerivative (physicalLieDerivative x) ≡ zeroForm
    -- Both fields are odd: [d,L_Q]=0 means d L_Q = - L_Q d.
    deRhamAndLieDerivativeAnticommute : (x : Forms) →
      deRhamD (physicalLieDerivative x) ≡
      negateForm (physicalLieDerivative (deRhamD x))
    cartanFormula : (x : Forms) →
      physicalLieDerivative x ≡ homotopyBoundary contractionByQ x

open CartanQCalculus public

-- If the composite of the two vertical comparison maps is the lifted Lie
-- derivative, contraction by Q supplies the required nullhomotopy immediately.
record CartanThreeLayerFactorization {ℓ : Level}
  (C : CartanQCalculus {ℓ}) : Type (ℓ-suc ℓ) where
  field
    PhysicalHom ControlHom : Type ℓ
    physicalToControl : PhysicalHom → ControlHom
    controlToForms : ControlHom → Forms C
    realizePhysicalAsForm : PhysicalHom → Forms C
    compositeIsPhysicalLieDerivative : (x : PhysicalHom) →
      controlToForms (physicalToControl x) ≡
      physicalLieDerivative C (realizePhysicalAsForm x)

open CartanThreeLayerFactorization public

cartanCompositeNullhomotopy : {ℓ : Level}
  (C : CartanQCalculus {ℓ})
  (F : CartanThreeLayerFactorization C) →
  (x : PhysicalHom F) →
  controlToForms F (physicalToControl F x) ≡
  homotopyBoundary C (contractionByQ C) (realizePhysicalAsForm F x)
cartanCompositeNullhomotopy C F x =
  compositeIsPhysicalLieDerivative F x ∙
  cartanFormula C (realizePhysicalAsForm F x)

-- Optional external route only.  P24 does not construct this cyclic Cartan
-- calculus: its derived cyclic complex uses Hochschild b, and its nonunitality
-- means the standard Connes SBI/mixed-complex machinery does not directly
-- apply.  Thus no P24 claim may discharge any field below.
record CyclicCartanCalculus {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    CyclicCochains : Type ℓ
    zeroCyclic : CyclicCochains
    cyclicDifferential : CyclicCochains → CyclicCochains
    cyclicLieDerivative cyclicContraction :
      CyclicCochains → CyclicCochains
    cyclicHomotopyBoundary :
      (CyclicCochains → CyclicCochains) →
      CyclicCochains → CyclicCochains
    cyclicDifferentialSquared : (x : CyclicCochains) →
      cyclicDifferential (cyclicDifferential x) ≡ zeroCyclic
    cyclicCartanFormula : (x : CyclicCochains) →
      cyclicLieDerivative x ≡
      cyclicHomotopyBoundary cyclicContraction x

record DeRhamToCyclicCartanBridge {ℓ : Level}
  (D : CartanQCalculus {ℓ})
  (C : CyclicCartanCalculus {ℓ}) : Type (ℓ-suc ℓ) where
  field
    formsToCyclic : Forms D → CyclicCartanCalculus.CyclicCochains C
    preservesDifferential : (x : Forms D) →
      formsToCyclic (deRhamD D x) ≡
      CyclicCartanCalculus.cyclicDifferential C (formsToCyclic x)
    preservesLieDerivative : (x : Forms D) →
      formsToCyclic (physicalLieDerivative D x) ≡
      CyclicCartanCalculus.cyclicLieDerivative C (formsToCyclic x)
    preservesContraction : (x : Forms D) →
      formsToCyclic (contractionByQ D x) ≡
      CyclicCartanCalculus.cyclicContraction C (formsToCyclic x)
    nuclearCompletionAndContinuityAreRetained : Type ℓ
    determinantLineIsRetained : Type ℓ
    nativeRelativeOperationActionIntertwinesOuterSymmetries : Type ℓ

-- A compatible Q-pencil is the plausible geometric home of a Rees parameter;
-- this remains a gate until both fields and their weights are constructed.
record ReesDoubleQGate {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    QSpace Parameter : Type ℓ
    firstQ secondQ : QSpace → QSpace
    parameterizedQ : Parameter → QSpace → QSpace
    bothQFieldsSquareToZero : Type ℓ
    signedMixedBracketVanishes : Type ℓ
    parameterizedQIsTheLinearPencil : Type ℓ
    parameterizedQSquaresToZero : Type ℓ
    ReesWeightsMatchPhysicalNormalWeights : Type ℓ
    originalAndSpecialFibresMatchExistingModels : Type ℓ
