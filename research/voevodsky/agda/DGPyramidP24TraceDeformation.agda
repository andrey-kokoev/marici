{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidP24TraceDeformation where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)

-- Exact interface extracted from P24, Section 3.7.  P24 uses the Hochschild
-- coboundary of the nonunital derived algebra; it does not supply a Connes
-- mixed-complex differential b+B.
record P24TraceDeformationProblem {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    Functions TraceValue ZeroCochain OneCochain TwoCochain CyclicClass : Type ℓ
    zeroFunction : Functions
    zeroTraceValue : TraceValue
    zeroOne : OneCochain
    zeroTwo : TwoCochain
    zeroClass : CyclicClass
    addFunctions : Functions → Functions → Functions
    negateOne : OneCochain → OneCochain

    ordinaryProduct : Functions → Functions → Functions
    signedByOriginalParity : Functions → Functions
    homologicalVectorField infinitesimalSymmetry : Functions → Functions
    trace : Functions → TraceValue
    traceCochain : ZeroCochain
    evaluateOne : OneCochain → Functions → Functions → TraceValue
    hochschildB0 : ZeroCochain → OneCochain
    hochschildB1 : OneCochain → TwoCochain
    classOfOneCocycle : OneCochain → CyclicClass

    traceIsQClosed : (f : Functions) →
      trace (homologicalVectorField f) ≡ zeroTraceValue
    traceCochainIsClosed : hochschildB0 traceCochain ≡ zeroOne
    -- Q and X are odd, so [Q,X]=QX+XQ=0.
    symmetryCommutesWithQ : (f : Functions) →
      addFunctions (homologicalVectorField (infinitesimalSymmetry f))
        (infinitesimalSymmetry (homologicalVectorField f)) ≡ zeroFunction

    deformationCocycle : OneCochain
    -- P24 (3.18): phi(f0,f1)=tau((-1)^|f0| X(f0 f1)).
    deformationCocycleHasP24Formula : (f0 f1 : Functions) →
      evaluateOne deformationCocycle f0 f1 ≡
      trace (signedByOriginalParity
        (infinitesimalSymmetry (ordinaryProduct f0 f1)))
    deformationCocycleIsShiftedCyclic : Type ℓ
    deformationCocycleIsClosed :
      hochschildB1 deformationCocycle ≡ zeroTwo
    boundariesHaveZeroClass : (sigma : ZeroCochain) →
      classOfOneCocycle (negateOne (hochschildB0 sigma)) ≡ zeroClass
    -- Quotient exactness, specialized to the class used in Theorem 3.3.
    zeroClassProducesNegativeBoundary :
      classOfOneCocycle deformationCocycle ≡ zeroClass →
      Σ[ sigma ∈ ZeroCochain ]
        deformationCocycle ≡ negateOne (hochschildB0 sigma)

open P24TraceDeformationProblem public

-- P24 Section 3.2 topology: C^n consists of continuous linear functionals on
-- the completed projective (n+1)-fold tensor power of C-infinity(M).  Nuclearity
-- makes the usual reasonable completed tensor products coincide.  The paper
-- works in practice with compact supermanifolds; compact support on a
-- noncompact M leads instead to a nuclear LF-space and is left unresolved.
record P24CochainTopology {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    SmoothFunctions NuclearFrechetSpace RealScalars : Type ℓ
    CompletedTensorPower ContinuousLinearMap : Type ℓ
    smoothFunctionsCarryNuclearFrechetTopology : Type ℓ
    cochainsAreContinuousMapsFromCompletedProjectiveTensorPowers : Type ℓ
    projectiveAndInjectiveCompletionsCoincideByNuclearity : Type ℓ
    compactSupermanifoldConvention : Type ℓ
    noncompactCompactSupportWouldRequireLFAnalysis : Type ℓ

-- P24 Theorem 3.3: extending tau to tau+t sigma is equivalent to making the
-- deformation cocycle phi a Hochschild boundary.
record InfinitesimalTraceExtension {ℓ : Level}
  (P : P24TraceDeformationProblem {ℓ}) : Type (ℓ-suc ℓ) where
  field
    traceVariation : ZeroCochain P
    firstOrderTraceEquation :
      deformationCocycle P ≡ negateOne P (hochschildB0 P traceVariation)

open InfinitesimalTraceExtension public

traceExtensionForcesZeroDeformationClass : {ℓ : Level}
  (P : P24TraceDeformationProblem {ℓ}) →
  InfinitesimalTraceExtension P →
  classOfOneCocycle P (deformationCocycle P) ≡ zeroClass P
traceExtensionForcesZeroDeformationClass P E =
  cong (classOfOneCocycle P) (firstOrderTraceEquation E) ∙
  boundariesHaveZeroClass P (traceVariation E)

zeroDeformationClassProducesTraceExtension : {ℓ : Level}
  (P : P24TraceDeformationProblem {ℓ}) →
  classOfOneCocycle P (deformationCocycle P) ≡ zeroClass P →
  InfinitesimalTraceExtension P
zeroDeformationClassProducesTraceExtension P classZero =
  record
    { traceVariation = fst witness
    ; firstOrderTraceEquation = snd witness
    }
  where
  witness = zeroClassProducesNegativeBoundary P classZero

record NonzeroP24DeformationClass {ℓ : Level}
  (P : P24TraceDeformationProblem {ℓ}) : Type (ℓ-suc ℓ) where
  field
    deformationClassIsNonzero :
      classOfOneCocycle P (deformationCocycle P) ≡ zeroClass P → ⊥

nonzeroP24ClassObstructsTraceExtension : {ℓ : Level}
  (P : P24TraceDeformationProblem {ℓ}) →
  NonzeroP24DeformationClass P →
  InfinitesimalTraceExtension P → ⊥
nonzeroP24ClassObstructsTraceExtension P N E =
  NonzeroP24DeformationClass.deformationClassIsNonzero N
    (traceExtensionForcesZeroDeformationClass P E)

-- This is the actual proposed third-row comparison: the control obstruction
-- maps covariantly to P24's degree-one deformation class.
record ControlToP24DeformationBridge {ℓ : Level}
  (P : P24TraceDeformationProblem {ℓ}) : Type (ℓ-suc ℓ) where
  field
    ControlObstruction : Type ℓ
    controlObstruction : ControlObstruction
    controlToCyclicClass : ControlObstruction → CyclicClass P
    hitsP24DeformationClass :
      controlToCyclicClass controlObstruction ≡
      classOfOneCocycle P (deformationCocycle P)
    mapIsCovariantInQManifoldMorphisms : Type ℓ
    determinantAndConormalLinesSurviveRealCompletion : Type ℓ
    nativeOuterSymmetryMapsToP24InfinitesimalSymmetry : Type ℓ
    antipodeVarianceIsResolvedBeforeThisCovariantMap : Type ℓ

-- P24 Proposition 3.6 gives coefficientwise closure conditions for a double-Q
-- pencil.  In degree one there are exactly three equations.
record P24DoubleQDegreeOneClosure {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    Functions TraceValue : Type ℓ
    firstQ secondQ : Functions → Functions
    cyclicOneCochain : Functions → Functions → TraceValue
    zeroTrace : TraceValue
    addTrace : TraceValue → TraceValue → TraceValue
    firstPureClosure : (f g : Functions) →
      cyclicOneCochain (firstQ f) (firstQ g) ≡ zeroTrace
    secondPureClosure : (f g : Functions) →
      cyclicOneCochain (secondQ f) (secondQ g) ≡ zeroTrace
    mixedClosureEquation : (f g : Functions) →
      addTrace (cyclicOneCochain (firstQ f) (secondQ g))
        (cyclicOneCochain (secondQ f) (firstQ g)) ≡ zeroTrace

record CurrentP24ConstructiveBoundary {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    localP24SourceHasBeenRecovered : Type ℓ
    P24DeformationCocycleFormulaIsKnown : Type ℓ
    physicalQFunctionsRemainUnconstructed : Type ℓ
    physicalTraceTauRemainsUnconstructed : Type ℓ
    nativeOuterSymmetryXRemainsUngeometrized : Type ℓ
    thereforeNoConcreteP24CochainMatrixYet : Type ℓ
    ConnesMixedComplexMustNotBeImportedFromP24 : Type ℓ
