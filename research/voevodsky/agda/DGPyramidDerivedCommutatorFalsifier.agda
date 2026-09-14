{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidDerivedCommutatorFalsifier where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)

-- Bruce's derived commutator has the form Q(fg), hence is Q-exact.  The
-- relative native anticommutator is independently known to be nonzero in its
-- current operation cohomology.  This record keeps the two classes typed.
record DerivedCommutatorAudit {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    QFunctions NativeOperations QClass NativeClass : Type ℓ
    zeroQFunction : QFunctions
    zeroQClass : QClass
    zeroNativeClass : NativeClass

    homologicalVectorField : QFunctions → QFunctions
    ordinaryProduct : QFunctions → QFunctions → QFunctions
    derivedCommutator : QFunctions → QFunctions → QFunctions
    classOfQFunction : QFunctions → QClass
    classOfNativeOperation : NativeOperations → NativeClass

    eta04 eta35 : QFunctions
    nativeR04-35 : NativeOperations

    derivedCommutatorIsQOfProduct :
      derivedCommutator eta04 eta35 ≡
      homologicalVectorField (ordinaryProduct eta04 eta35)
    QBoundariesHaveZeroClass : (x : QFunctions) →
      classOfQFunction (homologicalVectorField x) ≡ zeroQClass
    nativeRelativeClassIsNonzero :
      classOfNativeOperation nativeR04-35 ≡ zeroNativeClass → ⊥

open DerivedCommutatorAudit public

-- A proposed identification must include a map on cohomology; equality of
-- word formulas or occurrence weights is not enough.
record NativeToDerivedCommutatorIdentification {ℓ : Level}
  (A : DerivedCommutatorAudit {ℓ}) : Type (ℓ-suc ℓ) where
  field
    compareClasses : NativeClass A → QClass A
    compareZero : compareClasses (zeroNativeClass A) ≡ zeroQClass A
    comparisonReflectsZeroOnR04-35 :
      compareClasses (classOfNativeOperation A (nativeR04-35 A)) ≡
        zeroQClass A →
      classOfNativeOperation A (nativeR04-35 A) ≡ zeroNativeClass A
    identifiesRelativeOperationWithDerivedCommutator :
      compareClasses (classOfNativeOperation A (nativeR04-35 A)) ≡
      classOfQFunction A (derivedCommutator A (eta04 A) (eta35 A))

-- In the unchanged cohomology, a zero-reflecting identification is impossible:
-- Bruce's commutator is exact while the native relative operation is not.
noFaithfulCurrentDerivedCommutatorIdentification : {ℓ : Level}
  (A : DerivedCommutatorAudit {ℓ}) →
  NativeToDerivedCommutatorIdentification A → ⊥
noFaithfulCurrentDerivedCommutatorIdentification A I =
  nativeRelativeClassIsNonzero A
    (NativeToDerivedCommutatorIdentification.comparisonReflectsZeroOnR04-35 I
      (NativeToDerivedCommutatorIdentification.identifiesRelativeOperationWithDerivedCommutator I ∙
       cong (classOfQFunction A)
         (derivedCommutatorIsQOfProduct A) ∙
       QBoundariesHaveZeroClass A
         (ordinaryProduct A (eta04 A) (eta35 A))))

-- Viable alternatives are explicit: enlarge the Q-complex, use a nonfaithful
-- comparison, or reject the proposed commutator dictionary.
record DerivedCommutatorResolutionGate {ℓ : Level}
  (A : DerivedCommutatorAudit {ℓ}) : Type (ℓ-suc ℓ) where
  field
    EnlargedQFunctions : Type ℓ
    includeCurrentFunctions : QFunctions A → EnlargedQFunctions
    enlargedQ : EnlargedQFunctions → EnlargedQFunctions
    relativeOperationBecomesBoundaryOnlyAfterEnlargement : Type ℓ
    comparisonMayHaveKernelOnNativeOperationCohomology : Type ℓ
    orderedProductsAndDerivedCommutatorRemainDistinct : Type ℓ
    reflectionMayExchangeDerivedProductAndAntiOpposite : Type ℓ

-- The canonical odd-anchor route is a candidate only after it is realized as
-- an actual Q-morphism, not merely as an algebra map.
record OddAnchorPhysicalGate {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    PhysicalQSpace OddTangentQSpace : Type ℓ
    oddAnchor : PhysicalQSpace → OddTangentQSpace
    pullbackOnDerivedAlgebras : Type ℓ
    oddAnchorIntertwinesHomologicalVectorFields : Type ℓ
    determinantValuedTetrahedralFormHasTypedPullback : Type ℓ
    pulledBackResidueMatchesPhysicalEndpointColumn : Type ℓ
    nativeOperationActionIsCompatibleWithPullback : Type ℓ

record CurrentDerivedCommutatorAudit {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    nativeR04-35IsNonzeroInCurrentOperationCohomology : Type ℓ
    BruceDerivedCommutatorIsAlwaysQExact : Type ℓ
    faithfulUnchangedIdentificationIsExcluded : Type ℓ
    physicalQFunctionsAndOddAnchorRemainUnconstructed : Type ℓ

-- The viable replacement is a vector-field symmetry, not a function
-- commutator.  This audit is stated on a distinguished endpoint witness so it
-- can be instantiated before the full physical function algebra is built.
record InfinitesimalSymmetryAudit {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    QFunctions QClass NativeEndpointClass : Type ℓ
    zeroQClass : QClass
    zeroNativeEndpointClass : NativeEndpointClass

    homologicalVectorField : QFunctions → QFunctions
    classOfQFunction : QFunctions → QClass
    endpointWitness : QFunctions

    X04 X35 relativeSymmetryBracket : QFunctions → QFunctions
    shiftedBracket :
      (QFunctions → QFunctions) →
      (QFunctions → QFunctions) →
      QFunctions → QFunctions

    -- These are the concrete equations [X_i,Q] = 0 and
    -- X_r = [X_04,X_35] that a physical realization must discharge.
    X04CommutesWithQ : (x : QFunctions) →
      X04 (homologicalVectorField x) ≡ homologicalVectorField (X04 x)
    X35CommutesWithQ : (x : QFunctions) →
      X35 (homologicalVectorField x) ≡ homologicalVectorField (X35 x)
    relativeIsShiftedSymmetryBracket : (x : QFunctions) →
      relativeSymmetryBracket x ≡ shiftedBracket X04 X35 x

    nativeRelativeEndpointAction : NativeEndpointClass
    nativeRelativeEndpointActionIsNonzero :
      nativeRelativeEndpointAction ≡ zeroNativeEndpointClass → ⊥
    compareEndpointClasses : NativeEndpointClass → QClass
    comparisonReflectsZeroOnRelativeAction :
      compareEndpointClasses nativeRelativeEndpointAction ≡ zeroQClass →
      nativeRelativeEndpointAction ≡ zeroNativeEndpointClass
    identifiesRelativeEndpointAction :
      compareEndpointClasses nativeRelativeEndpointAction ≡
      classOfQFunction (relativeSymmetryBracket endpointWitness)

    -- Bruce's formula D_f(g) = [f,g]_star = Q(fg), packaged without
    -- prematurely choosing a particular candidate f.
    InnerParameters : Type ℓ
    innerDerivedAction : InnerParameters → QFunctions → QFunctions
    innerActionIsQBoundary : (f : InnerParameters) (x : QFunctions) →
      classOfQFunction (innerDerivedAction f x) ≡ zeroQClass

open InfinitesimalSymmetryAudit public

-- A symmetry bracket realizing the nonzero native endpoint action cannot be
-- inner.  Thus any successful X_r determines a genuinely outer class at the
-- tested endpoint.
relativeSymmetryIsNotInnerAtEndpoint : {ℓ : Level}
  (A : InfinitesimalSymmetryAudit {ℓ}) →
  (f : InnerParameters A) →
  relativeSymmetryBracket A (endpointWitness A) ≡
    innerDerivedAction A f (endpointWitness A) → ⊥
relativeSymmetryIsNotInnerAtEndpoint A f isInner =
  nativeRelativeEndpointActionIsNonzero A
    (comparisonReflectsZeroOnRelativeAction A
      (identifiesRelativeEndpointAction A ∙
       cong (classOfQFunction A) isInner ∙
       innerActionIsQBoundary A f (endpointWitness A)))

-- This is the next construction interface.  Merely giving derivations does
-- not fill it: the X_i must geometrize as vector fields on the same Q-space.
record PhysicalOuterSymmetryGate {ℓ : Level}
  (A : InfinitesimalSymmetryAudit {ℓ}) : Type (ℓ-suc ℓ) where
  field
    PhysicalQSpace : Type ℓ
    realizeX04AsVectorField : Type ℓ
    realizeX35AsVectorField : Type ℓ
    realizedFieldsCommuteWithPhysicalQ : Type ℓ
    realizedBracketMatchesRelativeOperation : Type ℓ
    operationIntertwinerToControlHom : Type ℓ
    operationIntertwinerToCyclicCochains : Type ℓ
    reflectionExchangesOrderedSymmetryData : Type ℓ
