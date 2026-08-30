import MariciFormal.NeutralZeroDynamics
import Mathlib.Analysis.Normed.Ring.Lemmas
import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.NumberTheory.Real.Irrational
import Mathlib.Topology.DenseEmbedding
import Mathlib.Topology.UniformSpace.CompleteSeparated

/-!
Minimal scalar interface for passing the finite neutral-state identity to a
completion.  The convergence of the paired imaginary residual is explicit;
it is not inferred from untyped convergence of raw state residuals.
-/

namespace MariciFormal

open Filter Topology

section DescendedKernel

variable {X Y : Type*} [Zero X] [Zero Y]

/-- A kernel statement descends from an already supplied completed operator
only through an injective, zero-preserving, operator-compatible embedding. -/
theorem descendedKernel_of_compatibleEmbedding
    (embed : X → Y) (sourceOperator : X → X) (completedOperator : Y → Y)
    (hembedZero : embed 0 = 0)
    (hembedInjective : Function.Injective embed)
    (hcompatible : ∀ x, completedOperator (embed x) = embed (sourceOperator x))
    {x : X} (hcompletedKernel : completedOperator (embed x) = 0) :
    sourceOperator x = 0 := by
  apply hembedInjective
  rw [hembedZero, ← hcompletedKernel]
  exact hcompatible x

end DescendedKernel

section DescendedKernelHostile

def hostileEmbedding : Fin 2 → Fin 2 := id

def hostileSourceOperator : Fin 2 → Fin 2 := fun _ => 1

def hostileCompletedOperator : Fin 2 → Fin 2 := fun _ => 0

theorem hostileEmbedding_injective : Function.Injective hostileEmbedding := by
  exact Function.injective_id

theorem hostileCompletedKernel (x : Fin 2) :
    hostileCompletedOperator (hostileEmbedding x) = 0 := by
  rfl

theorem hostileSource_not_kernel (x : Fin 2) :
    hostileSourceOperator x ≠ 0 := by
  decide

/-- Injectivity and zero preservation alone do not descend kernels when the
two supplied operators are incompatible. -/
theorem compatibility_is_independent_for_descendedKernel :
    ¬ ∀ x : Fin 2,
      hostileCompletedOperator (hostileEmbedding x) =
        hostileEmbedding (hostileSourceOperator x) := by
  intro hcompatible
  have hatZero := hcompatible 0
  decide at hatZero

end DescendedKernelHostile

section DescendedKernelEmbeddingHostiles

/-- Collapsing two source points to the unique target point preserves zero and
operator compatibility but loses the source-kernel distinction. -/
def collapsedEmbedding : Fin 2 → Fin 1 := fun _ => 0

def collapsedSourceOperator : Fin 2 → Fin 2 := fun _ => 1

def collapsedCompletedOperator : Fin 1 → Fin 1 := fun _ => 0

theorem collapsedEmbedding_preserves_zero : collapsedEmbedding 0 = 0 := rfl

theorem collapsedEmbedding_compatible (x : Fin 2) :
    collapsedCompletedOperator (collapsedEmbedding x) =
      collapsedEmbedding (collapsedSourceOperator x) := rfl

theorem collapsedEmbedding_not_injective :
    ¬ Function.Injective collapsedEmbedding := by
  intro hinjective
  have heq : (0 : Fin 2) = 1 := hinjective rfl
  decide at heq

theorem injectivity_is_independent_for_descendedKernel :
    collapsedCompletedOperator (collapsedEmbedding 0) = 0 ∧
      collapsedSourceOperator 0 ≠ 0 := by
  decide

/-- Swapping zero and one is injective, and the selected operators commute
with it, but it does not preserve the distinguished zero. -/
def zeroMovingEmbedding : Fin 2 → Fin 2 := Equiv.swap 0 1

def zeroMovingSourceOperator : Fin 2 → Fin 2 := fun _ => 1

def zeroMovingCompletedOperator : Fin 2 → Fin 2 := fun _ => 0

theorem zeroMovingEmbedding_injective : Function.Injective zeroMovingEmbedding := by
  exact (Equiv.swap (0 : Fin 2) 1).injective

theorem zeroMovingEmbedding_compatible (x : Fin 2) :
    zeroMovingCompletedOperator (zeroMovingEmbedding x) =
      zeroMovingEmbedding (zeroMovingSourceOperator x) := by
  simp [zeroMovingCompletedOperator, zeroMovingEmbedding,
    zeroMovingSourceOperator]

theorem zeroMovingEmbedding_does_not_preserve_zero :
    zeroMovingEmbedding 0 ≠ 0 := by
  decide

theorem zeroPreservation_is_independent_for_descendedKernel :
    zeroMovingCompletedOperator (zeroMovingEmbedding 0) = 0 ∧
      zeroMovingSourceOperator 0 ≠ 0 := by
  decide

end DescendedKernelEmbeddingHostiles

section CompatibleExtensionUniqueness

variable {X Y : Type*}

/-- Two compatible target operators agree on embedded source points.  Global
agreement needs an additional coverage principle. -/
theorem compatibleOperators_agree_on_image
    (embed : X → Y) (sourceOperator : X → X)
    (firstExtension secondExtension : Y → Y)
    (hfirst : ∀ x, firstExtension (embed x) = embed (sourceOperator x))
    (hsecond : ∀ x, secondExtension (embed x) = embed (sourceOperator x))
    (x : X) :
    firstExtension (embed x) = secondExtension (embed x) := by
  rw [hfirst x, hsecond x]

/-- Surjectivity is a sufficient discrete coverage principle for uniqueness.
Actual completions normally replace it by density plus continuity. -/
theorem compatibleOperators_eq_of_surjective
    (embed : X → Y) (sourceOperator : X → X)
    (firstExtension secondExtension : Y → Y)
    (hsurjective : Function.Surjective embed)
    (hfirst : ∀ x, firstExtension (embed x) = embed (sourceOperator x))
    (hsecond : ∀ x, secondExtension (embed x) = embed (sourceOperator x)) :
    firstExtension = secondExtension := by
  funext y
  obtain ⟨x, rfl⟩ := hsurjective y
  exact compatibleOperators_agree_on_image
    embed sourceOperator firstExtension secondExtension hfirst hsecond x

end CompatibleExtensionUniqueness

section CompatibleExtensionHostile

def properEmbedding : Fin 1 → Fin 2 := fun _ => 0

def properSourceOperator : Fin 1 → Fin 1 := id

def firstCompatibleExtension : Fin 2 → Fin 2 := id

def secondCompatibleExtension : Fin 2 → Fin 2 := fun _ => 0

theorem firstExtension_compatible (x : Fin 1) :
    firstCompatibleExtension (properEmbedding x) =
      properEmbedding (properSourceOperator x) := by
  rfl

theorem secondExtension_compatible (x : Fin 1) :
    secondCompatibleExtension (properEmbedding x) =
      properEmbedding (properSourceOperator x) := by
  rfl

/-- Compatibility on a proper image does not determine target behavior away
from that image. -/
theorem compatibleExtensions_not_unique_without_coverage :
    firstCompatibleExtension ≠ secondCompatibleExtension := by
  intro heq
  have hatOne := congrFun heq (1 : Fin 2)
  decide at hatOne

end CompatibleExtensionHostile

section DenseCompatibleExtensionUniqueness

variable {X Y : Type*} [TopologicalSpace X] [TopologicalSpace Y] [T2Space Y]

/-- Dense coverage plus continuity upgrades compatibility on the embedded
source to global uniqueness of the supplied target operators. -/
theorem compatibleContinuousOperators_eq_of_denseRange
    (embed : X → Y) (sourceOperator : X → X)
    (firstExtension secondExtension : Y → Y)
    (hdense : DenseRange embed)
    (hfirstContinuous : Continuous firstExtension)
    (hsecondContinuous : Continuous secondExtension)
    (hfirst : ∀ x, firstExtension (embed x) = embed (sourceOperator x))
    (hsecond : ∀ x, secondExtension (embed x) = embed (sourceOperator x)) :
    firstExtension = secondExtension := by
  apply hdense.equalizer hfirstContinuous hsecondContinuous
  funext x
  exact compatibleOperators_agree_on_image
    embed sourceOperator firstExtension secondExtension hfirst hsecond x

end DenseCompatibleExtensionUniqueness

section CanonicalUniformExtension

variable {X Y Z : Type*}
    [UniformSpace X] [UniformSpace Y] [UniformSpace Z]
    [CompleteSpace Z] [T0Space Z]

/-- A uniformly continuous map has a unique uniformly continuous extension
along a uniformly inducing dense embedding into a complete separated target. -/
theorem existsUnique_uniformContinuousExtension
    (embed : X → Y) (sourceMap : X → Z)
    (huniform : IsUniformInducing embed)
    (hdense : DenseRange embed)
    (hsource : UniformContinuous sourceMap) :
    ∃! completedMap : Y → Z,
      UniformContinuous completedMap ∧
        ∀ x, completedMap (embed x) = sourceMap x := by
  let denseInducing := huniform.isDenseInducing hdense
  let completedMap := denseInducing.extend sourceMap
  refine ⟨completedMap, ?_, ?_⟩
  · constructor
    · exact uniformContinuous_uniformly_extend huniform hdense hsource
    · intro x
      exact uniformly_extend_of_ind huniform hdense hsource x
  · intro candidate hcandidate
    exact uniformly_extend_unique huniform hdense
      hcandidate.2 hcandidate.1.continuous

/-- Operator specialization: the transported source action, rather than the
bare source operator, is the map whose uniform continuity authorizes a unique
completed operator. -/
theorem existsUnique_compatibleOperatorExtension
    [CompleteSpace Y] [T0Space Y]
    (embed : X → Y) (sourceOperator : X → X)
    (hembedding : IsUniformEmbedding embed)
    (hdense : DenseRange embed)
    (htransport : UniformContinuous (fun x => embed (sourceOperator x))) :
    ∃! completedOperator : Y → Y,
      UniformContinuous completedOperator ∧
        ∀ x, completedOperator (embed x) = embed (sourceOperator x) := by
  exact existsUnique_uniformContinuousExtension
    embed (fun x => embed (sourceOperator x))
      hembedding.isUniformInducing hdense htransport

end CanonicalUniformExtension

section CompatibleOperatorKernelDescent

variable {X Y : Type*} [Zero X] [Zero Y]
    [UniformSpace X] [UniformSpace Y]

/-- Any supplied compatible completion obtained along a zero-preserving
uniform embedding reflects kernel membership back to the source. -/
theorem kernel_descends_for_compatibleUniformExtension
    (embed : X → Y) (sourceOperator : X → X) (completedOperator : Y → Y)
    (hembedding : IsUniformEmbedding embed)
    (hembedZero : embed 0 = 0)
    (hcompatible : ∀ x,
      completedOperator (embed x) = embed (sourceOperator x))
    {x : X} (hkernel : completedOperator (embed x) = 0) :
    sourceOperator x = 0 := by
  exact descendedKernel_of_compatibleEmbedding
    embed sourceOperator completedOperator hembedZero hembedding.injective
      hcompatible hkernel

end CompatibleOperatorKernelDescent

section CompletionOnlyOrdinaryKernel

variable {X Y : Type*}

def IsRepresentedKernelPoint [Zero Y]
    (embed : X → Y) (completedOperator : Y → Y) (y : Y) : Prop :=
  completedOperator y = 0 ∧ y ∈ Set.range embed

def IsCompletionOnlyKernelPoint [Zero Y]
    (embed : X → Y) (completedOperator : Y → Y) (y : Y) : Prop :=
  completedOperator y = 0 ∧ y ∉ Set.range embed

/-- Every ordinary completed-kernel point is either represented by source
data or is completion-only.  This is a set-theoretic partition, not a derived
or Tor classification. -/
theorem completedKernelPoint_partition [Zero Y]
    (embed : X → Y) (completedOperator : Y → Y) (y : Y)
    (hkernel : completedOperator y = 0) :
    IsRepresentedKernelPoint embed completedOperator y ∨
      IsCompletionOnlyKernelPoint embed completedOperator y := by
  classical
  by_cases himage : y ∈ Set.range embed
  · exact Or.inl ⟨hkernel, himage⟩
  · exact Or.inr ⟨hkernel, himage⟩

theorem represented_and_completionOnly_disjoint [Zero Y]
    (embed : X → Y) (completedOperator : Y → Y) (y : Y) :
    ¬ (IsRepresentedKernelPoint embed completedOperator y ∧
      IsCompletionOnlyKernelPoint embed completedOperator y) := by
  rintro ⟨⟨_, himage⟩, _, hnotImage⟩
  exact hnotImage himage

end CompletionOnlyOrdinaryKernel

section CompletionOnlyOrdinaryKernelHostile

theorem properEmbedding_has_completionOnlyKernelPoint :
    IsCompletionOnlyKernelPoint properEmbedding secondCompatibleExtension
      (1 : Fin 2) := by
  constructor
  · rfl
  · rintro ⟨x, hx⟩
    fin_cases x
    decide at hx

end CompletionOnlyOrdinaryKernelHostile

section DenseDiscontinuousExtensionHostile

def rationalEmbedding : ℚ → ℝ := fun q => (q : ℝ)

def rationalZeroOperator : ℚ → ℚ := fun _ => 0

def continuousZeroExtension : ℝ → ℝ := fun _ => 0

def rationalImageIndicator : ℝ → ℝ := fun x =>
  if x ∈ Set.range ((↑) : ℚ → ℝ) then 0 else 1

theorem rationalEmbedding_dense : DenseRange rationalEmbedding := by
  exact Rat.denseRange_cast

theorem continuousZeroExtension_compatible (q : ℚ) :
    continuousZeroExtension (rationalEmbedding q) =
      rationalEmbedding (rationalZeroOperator q) := by
  simp [continuousZeroExtension, rationalEmbedding, rationalZeroOperator]

theorem rationalImageIndicator_compatible (q : ℚ) :
    rationalImageIndicator (rationalEmbedding q) =
      rationalEmbedding (rationalZeroOperator q) := by
  simp [rationalImageIndicator, rationalEmbedding, rationalZeroOperator]

/-- Dense agreement does not determine a discontinuous target operator. -/
theorem denseCompatibility_not_unique_without_continuity :
    continuousZeroExtension ≠ rationalImageIndicator := by
  intro heq
  have hatSqrtTwo := congrFun heq (Real.sqrt 2)
  have hirrational : Irrational (Real.sqrt 2) := irrational_sqrt_two
  simp [continuousZeroExtension, rationalImageIndicator, Irrational,
    hirrational] at hatSqrtTwo

theorem rationalImageIndicator_not_continuous :
    ¬ Continuous rationalImageIndicator := by
  intro hindicatorContinuous
  have heq : rationalImageIndicator = continuousZeroExtension := by
    apply Rat.denseRange_cast.equalizer hindicatorContinuous continuous_const
    funext q
    simp [rationalImageIndicator, continuousZeroExtension]
  exact denseCompatibility_not_unique_without_continuity heq.symm

/-- Even a dense identity embedding does not manufacture a continuous
extension of an incompatible source operator. -/
theorem denseEmbedding_does_not_manufacture_continuousExtension :
    DenseRange (id : ℝ → ℝ) ∧
      ¬ ∃ completedOperator : ℝ → ℝ,
        Continuous completedOperator ∧
          ∀ x, completedOperator (id x) = rationalImageIndicator x := by
  constructor
  · exact denseRange_id
  · rintro ⟨completedOperator, hcontinuous, hcompatible⟩
    have heq : completedOperator = rationalImageIndicator := by
      funext x
      exact hcompatible x
    rw [heq] at hcontinuous
    exact rationalImageIndicator_not_continuous hcontinuous

end DenseDiscontinuousExtensionHostile

/-- At a fixed off-real spectral parameter, a vanishing paired residual forces
the real Krein charges to converge to zero. -/
theorem asymptoticChargeNeutrality
    (z : ℂ) (charge imaginaryResidual : ℕ → ℝ)
    (hoffReal : z.im ≠ 0)
    (hbalance : ∀ n, z.im * charge n = imaginaryResidual n)
    (hresidual : Tendsto imaginaryResidual atTop (𝓝 0)) :
    Tendsto charge atTop (𝓝 0) := by
  have hcharge : charge = fun n => imaginaryResidual n / z.im := by
    funext n
    apply (eq_div_iff hoffReal).2
    simpa [mul_comm] using hbalance n
  rw [hcharge]
  simpa using hresidual.div_const z.im

/-- Convergence of an explicitly constructed complex paired residual supplies
the scalar imaginary-residual premise. -/
theorem pairedResidual_im_tendsto_zero
    (pairedResidual : ℕ → ℂ)
    (hresidual : Tendsto pairedResidual atTop (𝓝 0)) :
    Tendsto (fun n => (pairedResidual n).im) atTop (𝓝 0) := by
  simpa using (Complex.continuous_im.tendsto 0).comp hresidual

/-- Complex-residual form of asymptotic neutrality.  The residual has already
been paired with the state and metric; no boundedness transport is hidden in
this theorem. -/
theorem asymptoticChargeNeutrality_of_pairedResidual
    (z : ℂ) (charge : ℕ → ℝ) (pairedResidual : ℕ → ℂ)
    (hoffReal : z.im ≠ 0)
    (hbalance : ∀ n, z.im * charge n = (pairedResidual n).im)
    (hresidual : Tendsto pairedResidual atTop (𝓝 0)) :
    Tendsto charge atTop (𝓝 0) := by
  exact asymptoticChargeNeutrality z charge
    (fun n => (pairedResidual n).im) hoffReal hbalance
    (pairedResidual_im_tendsto_zero pairedResidual hresidual)

/-- A uniform nonneutrality gap contradicts asymptotic neutrality.  The gap is
stated only on the supplied sequence and does not assert global definiteness. -/
theorem noUniformChargeGap_of_asymptoticNeutrality
    (charge : ℕ → ℝ)
    (hcharge : Tendsto charge atTop (𝓝 0))
    (κ : ℝ) (hκ : 0 < κ) :
    ¬ ∀ᶠ n in atTop, κ ≤ |charge n| := by
  intro hgap
  have hsmall : ∀ᶠ n in atTop, |charge n| < κ :=
    by
      have hball : Metric.ball (0 : ℝ) κ ∈ 𝓝 0 := Metric.ball_mem_nhds 0 hκ
      simpa [Metric.mem_ball, Real.dist_eq] using hcharge.eventually hball
  filter_upwards [hgap, hsmall] with n hlower hupper
  exact (not_lt_of_ge hlower) hupper

/-- Hostile omission: without residual convergence, a constant nonzero charge
can satisfy the balance law at `z = i`. -/
def uncontrolledCharge : ℕ → ℝ := fun _ => 1

def uncontrolledImaginaryResidual : ℕ → ℝ := fun _ => 1

theorem uncontrolled_balance (n : ℕ) :
    Complex.I.im * uncontrolledCharge n = uncontrolledImaginaryResidual n := by
  norm_num [uncontrolledCharge, uncontrolledImaginaryResidual]

theorem uncontrolled_residual_does_not_vanish :
    ¬ Tendsto uncontrolledImaginaryResidual atTop (𝓝 0) := by
  simpa [uncontrolledImaginaryResidual, tendsto_const_nhds_iff]

/-- Raw residuals can vanish while an unbounded pairing amplification keeps
the paired residual nonzero. -/
def vanishingRawResidual (n : ℕ) : ℝ := 1 / ((n : ℝ) + 1)

def unboundedPairingAmplifier (n : ℕ) : ℝ := (n : ℝ) + 1

def amplifiedResidual (n : ℕ) : ℝ :=
  unboundedPairingAmplifier n * vanishingRawResidual n

theorem vanishingRawResidual_tendsto_zero :
    Tendsto vanishingRawResidual atTop (𝓝 0) := by
  simpa [vanishingRawResidual] using
    (tendsto_one_div_add_atTop_nhds_zero_nat (𝕜 := ℝ))

theorem amplifiedResidual_eq_one (n : ℕ) : amplifiedResidual n = 1 := by
  simp only [amplifiedResidual, unboundedPairingAmplifier, vanishingRawResidual]
  field_simp

theorem amplifiedResidual_does_not_vanish :
    ¬ Tendsto amplifiedResidual atTop (𝓝 0) := by
  have heq : amplifiedResidual = fun _ : ℕ => (1 : ℝ) := by
    funext n
    exact amplifiedResidual_eq_one n
  rw [heq]
  simpa [tendsto_const_nhds_iff]

/-- The minimal scalar repair: a norm-bounded pairing amplifier transports a
vanishing raw residual to a vanishing paired residual. -/
theorem pairedResidual_tendsto_zero_of_boundedAmplifier
    (amplifier rawResidual : ℕ → ℂ)
    (hamplifier : IsBoundedUnder (· ≤ ·) atTop (norm ∘ amplifier))
    (hraw : Tendsto rawResidual atTop (𝓝 0)) :
    Tendsto (fun n => amplifier n * rawResidual n) atTop (𝓝 0) := by
  exact Filter.isBoundedUnder_le_mul_tendsto_zero hamplifier hraw

/-- Completion neutrality under the minimal scalar bounded-amplification
premise. -/
theorem asymptoticChargeNeutrality_of_boundedAmplifier
    (z : ℂ) (charge : ℕ → ℝ)
    (amplifier rawResidual : ℕ → ℂ)
    (hoffReal : z.im ≠ 0)
    (hbalance : ∀ n,
      z.im * charge n = (amplifier n * rawResidual n).im)
    (hamplifier : IsBoundedUnder (· ≤ ·) atTop (norm ∘ amplifier))
    (hraw : Tendsto rawResidual atTop (𝓝 0)) :
    Tendsto charge atTop (𝓝 0) := by
  apply asymptoticChargeNeutrality_of_pairedResidual z charge
    (fun n => amplifier n * rawResidual n) hoffReal hbalance
  exact pairedResidual_tendsto_zero_of_boundedAmplifier
    amplifier rawResidual hamplifier hraw

/-- A convergent pairing amplifier transports a vanishing raw residual to a
vanishing paired residual.  Convergence is a sufficient but stronger-than-
necessary control premise. -/
theorem pairedResidual_tendsto_zero_of_convergentAmplifier
    (amplifier rawResidual : ℕ → ℂ) (amplifierLimit : ℂ)
    (hamplifier : Tendsto amplifier atTop (𝓝 amplifierLimit))
    (hraw : Tendsto rawResidual atTop (𝓝 0)) :
    Tendsto (fun n => amplifier n * rawResidual n) atTop (𝓝 0) := by
  simpa using hamplifier.mul hraw

/-- Completion neutrality obtained from an explicitly convergent pairing
amplifier and a vanishing raw residual. -/
theorem asymptoticChargeNeutrality_of_convergentAmplifier
    (z : ℂ) (charge : ℕ → ℝ)
    (amplifier rawResidual : ℕ → ℂ) (amplifierLimit : ℂ)
    (hoffReal : z.im ≠ 0)
    (hbalance : ∀ n,
      z.im * charge n = (amplifier n * rawResidual n).im)
    (hamplifier : Tendsto amplifier atTop (𝓝 amplifierLimit))
    (hraw : Tendsto rawResidual atTop (𝓝 0)) :
    Tendsto charge atTop (𝓝 0) := by
  apply asymptoticChargeNeutrality_of_pairedResidual z charge
    (fun n => amplifier n * rawResidual n) hoffReal hbalance
  exact pairedResidual_tendsto_zero_of_convergentAmplifier
    amplifier rawResidual amplifierLimit hamplifier hraw

end MariciFormal
