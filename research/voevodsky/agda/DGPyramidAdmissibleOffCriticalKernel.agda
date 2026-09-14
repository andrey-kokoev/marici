{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidAdmissibleOffCriticalKernel where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)
open import Cubical.Data.Sigma

-- Abstract data of a parameterized, source-derived, multi-observer kernel
-- problem.  Positivity and completion stability are independent fields:
-- observer conformance alone is not allowed to imply either one.
record MultiObserverKernelProblem {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    Parameter Probe : Type ℓ
    RoutePair : Probe → Type ℓ
    Source Carrier Target ResidualValue : Parameter → Type ℓ

    zeroCarrier : (s : Parameter) → Carrier s
    zeroTarget : (s : Parameter) → Target s
    zeroResidual : (s : Parameter) → ResidualValue s

    realize : (s : Parameter) → Source s → Carrier s
    kernelFamily : (s : Parameter) → Carrier s → Target s
    residual : (s : Parameter) →
      (p : Probe) → RoutePair p → Source s → ResidualValue s

    OffCritical : Parameter → Type ℓ
    Positive : (s : Parameter) → Source s → Type ℓ
    CompletionStable : (s : Parameter) → Source s → Type ℓ

open MultiObserverKernelProblem public

-- This record is the homotopy intersection of the admitted source image,
-- the derived zero fibre of the kernel family, all conformance equalizers,
-- the positivity locus, and the completion-stable locus.
record AdmissibleKernelState {ℓ : Level}
  (P : MultiObserverKernelProblem {ℓ})
  (s : Parameter P) : Type ℓ where
  field
    source : Source P s
    kernelPath :
      kernelFamily P s (realize P s source) ≡ zeroTarget P s
    conformance : (p : Probe P) (α : RoutePair P p) →
      residual P s p α source ≡ zeroResidual P s
    positivity : Positive P s source
    completion : CompletionStable P s source

open AdmissibleKernelState public

OffCriticalKernelState : {ℓ : Level} →
  (P : MultiObserverKernelProblem {ℓ}) → Type ℓ
OffCriticalKernelState P =
  Σ[ s ∈ Parameter P ]
    OffCritical P s × AdmissibleKernelState P s

-- A detector theorem has two genuinely different halves.  Kernel/conformance
-- forces the detector into its zero fibre, while source admissibility on the
-- off-critical locus says that the same value cannot be zero.
record JointOffCriticalDetector {ℓ : Level}
  (P : MultiObserverKernelProblem {ℓ}) : Type (ℓ-suc ℓ) where
  field
    DetectorValue : Type ℓ
    zeroDetector : DetectorValue
    detect : (s : Parameter P) → AdmissibleKernelState P s → DetectorValue

    kernelConformanceForcesZero :
      (s : Parameter P) → (x : AdmissibleKernelState P s) →
      detect s x ≡ zeroDetector

    offCriticalAdmissibilityDetects :
      (s : Parameter P) → OffCritical P s →
      (x : AdmissibleKernelState P s) →
      detect s x ≡ zeroDetector → ⊥

open JointOffCriticalDetector public

-- The categorical non-constructability theorem.  Its proof is independent
-- of zero-by-zero arithmetic estimates once the two detector halves exist.
noAdmissibleOffCriticalKernelStates : {ℓ : Level}
  (P : MultiObserverKernelProblem {ℓ}) →
  JointOffCriticalDetector P →
  OffCriticalKernelState P → ⊥
noAdmissibleOffCriticalKernelStates P D (s , off , x) =
  offCriticalAdmissibilityDetects D s off x
    (kernelConformanceForcesZero D s x)

-- A realization interface is kept separate: the emptiness theorem becomes
-- RH only after actual Xi-zero data are mapped into admissible kernel states.
record ArithmeticZeroRealization {ℓ : Level}
  (P : MultiObserverKernelProblem {ℓ}) : Type (ℓ-suc ℓ) where
  field
    ArithmeticZero : Type ℓ
    zeroParameter : ArithmeticZero → Parameter P
    zeroIsOffCritical : ArithmeticZero → Type ℓ
    realizeZero : (z : ArithmeticZero) →
      zeroIsOffCritical z → AdmissibleKernelState P (zeroParameter z)
    offCriticalWitness : (z : ArithmeticZero) →
      zeroIsOffCritical z → OffCritical P (zeroParameter z)

open ArithmeticZeroRealization public

noOffCriticalArithmeticZeros : {ℓ : Level}
  (P : MultiObserverKernelProblem {ℓ}) →
  (D : JointOffCriticalDetector P) →
  (R : ArithmeticZeroRealization P) →
  (z : ArithmeticZero R) → zeroIsOffCritical R z → ⊥
noOffCriticalArithmeticZeros P D R z off =
  noAdmissibleOffCriticalKernelStates P D
    (zeroParameter R z , offCriticalWitness R z off , realizeZero R z off)
