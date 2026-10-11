{-# OPTIONS --safe --cubical --guardedness #-}
module TickSpectralLocalContinuity where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ; max)
import Cubical.Data.Nat.Order as O
open import Cubical.Data.Bool.Base using (false; true)
open import Cubical.Data.Sigma using (Σ; _×_)
open import Cubical.HITs.PropositionalTruncation as PT
open import CauchyMetricEquivalence using (MetricCompletionCandidate)
open import CauchyAdditionCongruence using (_+completion_)
open import CauchyNegation using (-completion_)
open import CauchyCompletionMultiplication using (preferredCompletionMultiplication)
open import ConstructiveComplexCompletion
open import TickCompletionMetric
open import TickCompletionRingContinuity
open import TickPhaseMetricContinuity
open import TickCompletionPhase using (phase)
open import TickMachinPiEndpointContract using (machinPi)
import TickSpectralLocalOperators as L

Control : MetricCompletionCandidate → (MetricCompletionCandidate → Type) → Type
Control a P = ∥ Σ ℕ (λ l → (b : MetricCompletionCandidate) → CompletionWithin a b l → P b) ∥₁

combine : {a : MetricCompletionCandidate} {P Q : MetricCompletionCandidate → Type} →
  Control a P → Control a Q → Control a (λ b → P b × Q b)
combine {a} pc qc = PT.rec isPropPropTrunc
  (λ { (l , hl) → PT.map (λ { (m , hm) → max l m , λ b h →
    hl b (within-weaken a b l (max l m) O.left-≤-max h) ,
    hm b (within-weaken a b m (max l m) O.right-≤-max h) }) qc }) pc

complex-components : {f : MetricCompletionCandidate → ComplexCompletion} →
  MetricContinuous (λ t → realPart (f t)) → MetricContinuous (λ t → imaginaryPart (f t)) → ComplexMetricContinuous f
complex-components rc ic a k = combine (rc a k) (ic a k)

real-continuous : {f : MetricCompletionCandidate → ComplexCompletion} →
  ComplexMetricContinuous f → MetricContinuous (λ t → realPart (f t))
real-continuous fc a k = PT.map (λ { (l , h) → l , λ b hb → fst (h b hb) }) (fc a k)
imaginary-continuous : {f : MetricCompletionCandidate → ComplexCompletion} →
  ComplexMetricContinuous f → MetricContinuous (λ t → imaginaryPart (f t))
imaginary-continuous fc a k = PT.map (λ { (l , h) → l , λ b hb → snd (h b hb) }) (fc a k)

sum-continuous : {f g : MetricCompletionCandidate → MetricCompletionCandidate} →
  MetricContinuous f → MetricContinuous g → MetricContinuous (λ t → f t +completion g t)
sum-continuous {f} {g} = joint-compose-continuous _+completion_ f g addition-joint-continuous
product-continuous : {f g : MetricCompletionCandidate → MetricCompletionCandidate} →
  MetricContinuous f → MetricContinuous g → MetricContinuous (λ t → preferredCompletionMultiplication (f t) (g t))
product-continuous {f} {g} = joint-compose-continuous preferredCompletionMultiplication f g multiplication-joint-continuous

complex-constant-continuous : (z : ComplexCompletion) → ComplexMetricContinuous (λ _ → z)
complex-constant-continuous z = complex-components
  (constant-metric-continuous (realPart z)) (constant-metric-continuous (imaginaryPart z))

complex-add-continuous : {f g : MetricCompletionCandidate → ComplexCompletion} →
  ComplexMetricContinuous f → ComplexMetricContinuous g → ComplexMetricContinuous (λ t → f t +complex g t)
complex-add-continuous fc gc = complex-components
  (sum-continuous (real-continuous fc) (real-continuous gc))
  (sum-continuous (imaginary-continuous fc) (imaginary-continuous gc))

complex-product-continuous : {f g : MetricCompletionCandidate → ComplexCompletion} →
  ComplexMetricContinuous f → ComplexMetricContinuous g → ComplexMetricContinuous (λ t → f t ·complex g t)
complex-product-continuous fc gc = complex-components
  (sum-continuous (product-continuous (real-continuous fc) (real-continuous gc))
    (compose-metric-continuous negation-metric-continuous
      (product-continuous (imaginary-continuous fc) (imaginary-continuous gc))))
  (sum-continuous (product-continuous (real-continuous fc) (imaginary-continuous gc))
    (product-continuous (imaginary-continuous fc) (real-continuous gc)))

affine-complex-continuous : (a b : ComplexCompletion) {f : MetricCompletionCandidate → ComplexCompletion} →
  ComplexMetricContinuous f → ComplexMetricContinuous (λ t → a +complex (f t ·complex b))
affine-complex-continuous a b fc = complex-add-continuous (complex-constant-continuous a)
  (complex-product-continuous fc (complex-constant-continuous b))

module V = L.V
VectorWithin : V.Vector → V.Vector → ℕ → Type
VectorWithin v w k = (j : V.Label) → ComplexWithin (v j) (w j) k
VectorMetricContinuous : (MetricCompletionCandidate → V.Vector) → Type
VectorMetricContinuous f = (a : MetricCompletionCandidate) (k : ℕ) → Control a (λ b → VectorWithin (f a) (f b) k)

-- A single modulus controls all four coordinates, not four unrelated limits.
vector-from-coordinates : {f : MetricCompletionCandidate → V.Vector} →
  ((j : V.Label) → ComplexMetricContinuous (λ t → f t j)) → VectorMetricContinuous f
vector-from-coordinates fc a k = PT.map
  (λ { (l , hl) → l , λ b h → λ
    { (false , false) → fst (fst (hl b h))
    ; (false , true) → snd (fst (hl b h))
    ; (true , false) → fst (snd (hl b h))
    ; (true , true) → snd (snd (hl b h)) } })
  (combine (combine (fc (false , false) a k) (fc (false , true) a k))
    (combine (fc (true , false) a k) (fc (true , true) a k)))

abstract
  local-metric-continuous : (P : V.Vector → V.Vector) (v : V.Vector) → VectorMetricContinuous (λ t → L.local P t v)
  local-metric-continuous P v = vector-from-coordinates λ j →
    affine-complex-continuous (L.positiveProjector P v j) (L.negativeProjector P v j)
      (operational-phase-metric-continuous machinPi)

  left-local-metric-continuous : (v : V.Vector) → VectorMetricContinuous (λ t → L.leftLocal t v)
  left-local-metric-continuous = local-metric-continuous V.left
  right-local-metric-continuous : (v : V.Vector) → VectorMetricContinuous (λ t → L.rightLocal t v)
  right-local-metric-continuous = local-metric-continuous V.right
