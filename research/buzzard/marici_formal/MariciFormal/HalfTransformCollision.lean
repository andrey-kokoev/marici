import Mathlib.Tactic

/-!
Finite algebraic core of Grothendieck's packet
`theta-collision-is-stationary-half-transform-phase.md`.

For a sampled half-transform write `C` for its cosine coordinate, `S` for
its sine coordinate, and `M` for the position-weighted sine coordinate.  The
analytic integral construction, phase differentiability, and the conjectural
completed-theta transversality statement remain external interfaces.
-/

namespace MariciFormal

/-- The three real coordinates needed at one half-transform sample. -/
structure HalfTransformJet where
  cosine : ℝ
  sine : ℝ
  firstSine : ℝ
  deriving DecidableEq

namespace HalfTransformJet

/-- Value of the even completed truncation at the sample. -/
def evenValue (jet : HalfTransformJet) : ℝ :=
  2 * jet.cosine

/-- Derivative of the even completed truncation at the sample. -/
def evenDerivative (jet : HalfTransformJet) : ℝ :=
  -2 * jet.firstSine

/-- The half-transform lies on the imaginary-axis seam. -/
def OnSeam (jet : HalfTransformJet) : Prop :=
  jet.cosine = 0

/-- The half-transform itself passes through the origin. -/
def OriginCrossing (jet : HalfTransformJet) : Prop :=
  jet.cosine = 0 ∧ jet.sine = 0

/-- The even truncation has a double-zero sample. -/
def DoubleZero (jet : HalfTransformJet) : Prop :=
  jet.evenValue = 0 ∧ jet.evenDerivative = 0

/-- Algebraic phase velocity on the chart where the sine coordinate is nonzero. -/
def phaseVelocity (jet : HalfTransformJet) : ℝ :=
  jet.firstSine / jet.sine

/-- The source-transversality predicate stated in the frozen packet. -/
def SourceTransverse (jet : HalfTransformJet) : Prop :=
  jet.sine * jet.firstSine ≠ 0

/-- A stronger, oriented condition.  The packet does not assert this sign at
all crossings. -/
def PositiveOrientation (jet : HalfTransformJet) : Prop :=
  0 < jet.sine * jet.firstSine

theorem evenValue_eq_zero_iff (jet : HalfTransformJet) :
    jet.evenValue = 0 ↔ jet.cosine = 0 := by
  simp [evenValue]

theorem evenDerivative_eq_zero_iff (jet : HalfTransformJet) :
    jet.evenDerivative = 0 ↔ jet.firstSine = 0 := by
  simp [evenDerivative]

/-- The double-zero collision equations are exactly `C = 0` and `M = 0`. -/
theorem doubleZero_iff_cosine_firstSine_zero (jet : HalfTransformJet) :
    jet.DoubleZero ↔ jet.cosine = 0 ∧ jet.firstSine = 0 := by
  simp [DoubleZero, evenValue_eq_zero_iff, evenDerivative_eq_zero_iff]

/-- On the non-origin seam chart, a double zero is exactly stationary phase. -/
theorem doubleZero_iff_stationary_phase
    (jet : HalfTransformJet)
    (hseam : jet.OnSeam)
    (hnonorigin : jet.sine ≠ 0) :
    jet.DoubleZero ↔ jet.phaseVelocity = 0 := by
  rw [doubleZero_iff_cosine_firstSine_zero]
  simp only [hseam, true_and]
  simp [phaseVelocity, hnonorigin]

theorem sourceTransverse_iff_coordinates_nonzero (jet : HalfTransformJet) :
    jet.SourceTransverse ↔ jet.sine ≠ 0 ∧ jet.firstSine ≠ 0 := by
  simp [SourceTransverse]

/-- The stronger positive-product hypothesis implies the packet's nonzero
transversality condition, but is not identified with it. -/
theorem positiveOrientation_implies_sourceTransverse
    (jet : HalfTransformJet)
    (hpositive : jet.PositiveOrientation) :
    jet.SourceTransverse := by
  exact ne_of_gt hpositive

/-- Positive product gives positive phase velocity whenever the phase chart is
defined. -/
theorem positiveOrientation_implies_positive_phaseVelocity
    (jet : HalfTransformJet)
    (hpositive : jet.PositiveOrientation) :
    0 < jet.phaseVelocity := by
  rcases (mul_pos_iff.mp hpositive) with h | h
  · exact div_pos h.2 h.1
  · exact div_pos_of_neg_of_neg h.2 h.1

/-- On a seam sample, positive orientation excludes both a double zero and an
origin crossing. -/
theorem positiveOrientation_excludes_collisions
    (jet : HalfTransformJet)
    (hseam : jet.OnSeam)
    (hpositive : jet.PositiveOrientation) :
    ¬ jet.DoubleZero ∧ ¬ jet.OriginCrossing := by
  have htransverse := jet.positiveOrientation_implies_sourceTransverse hpositive
  rw [sourceTransverse_iff_coordinates_nonzero] at htransverse
  constructor
  · rw [doubleZero_iff_cosine_firstSine_zero]
    exact fun hdouble => htransverse.2 hdouble.2
  · exact fun horigin => htransverse.1 horigin.2

/-- Once source monotonicity supplies a strictly positive sine coordinate, an
imaginary-axis seam point cannot be an origin crossing. -/
theorem positiveSine_excludes_originCrossing
    (jet : HalfTransformJet)
    (hpositiveSine : 0 < jet.sine) :
    ¬ jet.OriginCrossing := by
  intro horigin
  linarith [horigin.2]

/-- Under the positive-sine theorem, the remaining transversality gate is
exactly nonvanishing of the position-weighted sine coordinate. -/
theorem sourceTransverse_iff_firstSine_nonzero_of_positiveSine
    (jet : HalfTransformJet)
    (hpositiveSine : 0 < jet.sine) :
    jet.SourceTransverse ↔ jet.firstSine ≠ 0 := by
  rw [sourceTransverse_iff_coordinates_nonzero]
  simp [ne_of_gt hpositiveSine]

/-- Positive sine does not orient the remaining coordinate: the phase
velocity may be negative at a transverse seam crossing. -/
def negativeOrientationSeam : HalfTransformJet :=
  ⟨0, 1, -1⟩

theorem positiveSine_does_not_force_positiveOrientation :
    negativeOrientationSeam.OnSeam ∧
      0 < negativeOrientationSeam.sine ∧
      negativeOrientationSeam.SourceTransverse ∧
      ¬ negativeOrientationSeam.PositiveOrientation := by
  norm_num [negativeOrientationSeam, OnSeam, SourceTransverse,
    PositiveOrientation]

/-- Jet of the exact monotone step-source hostile: the half-transform is
nonzero and has positive sine coordinate, but the cosine crossing is tangent. -/
def monotoneTangentHostile : HalfTransformJet :=
  ⟨0, 2, 0⟩

theorem monotoneTangentHostile_properties :
    monotoneTangentHostile.OnSeam ∧
      0 < monotoneTangentHostile.sine ∧
      ¬ monotoneTangentHostile.OriginCrossing ∧
      monotoneTangentHostile.DoubleZero ∧
      monotoneTangentHostile.phaseVelocity = 0 ∧
      ¬ monotoneTangentHostile.SourceTransverse := by
  norm_num [monotoneTangentHostile, OnSeam, OriginCrossing, DoubleZero,
    evenValue, evenDerivative, phaseVelocity, SourceTransverse]

end HalfTransformJet

/-! The positive two-atom origin-crossing hostile. -/

/-- Endpoint data for `w₀ δ₀ + wL δL` at one character value. -/
structure TwoAtomPhaseSample where
  wZero : ℝ
  wEnd : ℝ
  length : ℝ
  endpointCosine : ℝ
  endpointSine : ℝ

namespace TwoAtomPhaseSample

def PositiveWeights (sample : TwoAtomPhaseSample) : Prop :=
  0 < sample.wZero ∧ 0 < sample.wEnd

/-- The atom at zero contributes `(wZero, 0, 0)`; the endpoint atom supplies
the displayed character coordinates. -/
def jet (sample : TwoAtomPhaseSample) : HalfTransformJet where
  cosine := sample.wZero + sample.wEnd * sample.endpointCosine
  sine := sample.wEnd * sample.endpointSine
  firstSine := sample.length * sample.wEnd * sample.endpointSine

/-- Algebraic sample of `δ₀ + δL` at an odd multiple of `π/L`: the endpoint
character has cosine `-1` and sine `0`. -/
def positiveOddSample (L : ℝ) : TwoAtomPhaseSample where
  wZero := 1
  wEnd := 1
  length := L
  endpointCosine := -1
  endpointSine := 0

theorem positiveOddSample_weights (L : ℝ) :
    (positiveOddSample L).PositiveWeights := by
  norm_num [PositiveWeights, positiveOddSample]

theorem positiveOddSample_jet (L : ℝ) :
    (positiveOddSample L).jet = ⟨0, 0, 0⟩ := by
  simp [positiveOddSample, jet]

/-- Positive atom weights do not exclude an origin crossing or a double zero. -/
theorem positive_two_atom_origin_double_zero_hostile (L : ℝ) :
    (positiveOddSample L).PositiveWeights ∧
      (positiveOddSample L).jet.OriginCrossing ∧
      (positiveOddSample L).jet.DoubleZero := by
  refine ⟨positiveOddSample_weights L, ?_, ?_⟩
  · simp [HalfTransformJet.OriginCrossing, positiveOddSample, jet]
  · simp [HalfTransformJet.DoubleZero, HalfTransformJet.evenValue,
      HalfTransformJet.evenDerivative, positiveOddSample, jet]

/-- In particular, source positivity plus the cosine-zero constraint cannot
imply the stronger positive-product target. -/
theorem positive_weights_and_seam_do_not_force_positive_orientation :
    ∃ sample : TwoAtomPhaseSample,
      sample.PositiveWeights ∧ sample.jet.OnSeam ∧
        ¬ sample.jet.PositiveOrientation := by
  refine ⟨positiveOddSample 1, positiveOddSample_weights 1, ?_, ?_⟩
  · simp [HalfTransformJet.OnSeam, positiveOddSample, jet]
  · simp [HalfTransformJet.PositiveOrientation, positiveOddSample, jet]

end TwoAtomPhaseSample

/-! Finite current geometry behind the monotone tangent hostile. -/

/-- Values of two positive current atoms at one character.  The cosine
velocity coordinates already include the position factors needed for the
derivative of the sine transform. -/
structure TwoAtomCurrentSample where
  weightLeft : ℝ
  weightRight : ℝ
  sineLeft : ℝ
  sineRight : ℝ
  cosineVelocityLeft : ℝ
  cosineVelocityRight : ℝ

namespace TwoAtomCurrentSample

def PositiveWeights (sample : TwoAtomCurrentSample) : Prop :=
  0 < sample.weightLeft ∧ 0 < sample.weightRight

def currentValue (sample : TwoAtomCurrentSample) : ℝ :=
  sample.weightLeft * sample.sineLeft +
    sample.weightRight * sample.sineRight

def currentDerivative (sample : TwoAtomCurrentSample) : ℝ :=
  sample.weightLeft * sample.cosineVelocityLeft +
    sample.weightRight * sample.cosineVelocityRight

/-- Two equal positive atoms at opposite sine extrema. -/
def balancedOppositeExtrema : TwoAtomCurrentSample where
  weightLeft := 1
  weightRight := 1
  sineLeft := 1
  sineRight := -1
  cosineVelocityLeft := 0
  cosineVelocityRight := 0

/-- Positive current mass can have a multiple real zero of its sine transform:
both its value and its first velocity vanish at the balanced extrema sample. -/
theorem positive_current_multiple_zero_hostile :
    balancedOppositeExtrema.PositiveWeights ∧
      balancedOppositeExtrema.currentValue = 0 ∧
      balancedOppositeExtrema.currentDerivative = 0 := by
  norm_num [balancedOppositeExtrema, PositiveWeights, currentValue,
    currentDerivative]

end TwoAtomCurrentSample

/-! Algebraic core of the smooth strictly log-concave hostile continuation. -/

namespace ExponentialCollisionHostile

/-- At a collision, the lower-right Jacobian entry vanishes, so the determinant
is the negative product of the two off-diagonal derivatives. -/
def collisionJacobianDet (dyFirst dASecond : ℝ) : ℝ :=
  -(dyFirst * dASecond)

theorem collisionJacobianDet_negative
    (dyFirst dASecond : ℝ)
    (hdy : 0 < dyFirst)
    (hdA : 0 < dASecond) :
    collisionJacobianDet dyFirst dASecond < 0 := by
  unfold collisionJacobianDet
  nlinarith [mul_pos hdy hdA]

/-- Logarithmic curvature of `exp (-A*u - epsilon*u^2)`.  Deriving this from
the analytic source function is a separate interface. -/
def quadraticLogCurvature (epsilon : ℝ) : ℝ :=
  -2 * epsilon

theorem quadraticLogCurvature_negative
    (epsilon : ℝ)
    (hepsilon : 0 < epsilon) :
    quadraticLogCurvature epsilon < 0 := by
  unfold quadraticLogCurvature
  linarith

/-- Negative log curvature and a transverse parameter Jacobian are compatible
with the hostile collision data; neither condition proves theta-source
transversality. -/
theorem strictLogConcavity_and_transverseJacobian_compatible
    (epsilon dyFirst dASecond : ℝ)
    (hepsilon : 0 < epsilon)
    (hdy : 0 < dyFirst)
    (hdA : 0 < dASecond) :
    quadraticLogCurvature epsilon < 0 ∧
      collisionJacobianDet dyFirst dASecond < 0 := by
  exact ⟨quadraticLogCurvature_negative epsilon hepsilon,
    collisionJacobianDet_negative dyFirst dASecond hdy hdA⟩

end ExponentialCollisionHostile

/-! Phase-aligned Gaussian value--tangent port dependence. -/

namespace GaussianBoundaryCollision

/-- Integration-by-parts normal form for one truncated Gaussian sample. -/
def boundaryIdentityRhs
    (A endpointValue boundarySine frequency cosineValue : ℝ) : ℝ :=
  -(endpointValue * boundarySine) / (2 * A) +
    frequency / (2 * A) * cosineValue

/-- When the endpoint sine vanishes, the Gaussian tangent port is a scalar
multiple of the value port.  The integration-by-parts identity is an explicit
premise rather than an assumed collision conclusion. -/
theorem tangent_eq_scalar_value_of_phase_aligned
    (A endpointValue frequency cosineValue tangentValue : ℝ)
    (hidentity :
      tangentValue =
        boundaryIdentityRhs A endpointValue 0 frequency cosineValue) :
    tangentValue = frequency / (2 * A) * cosineValue := by
  simpa [boundaryIdentityRhs] using hidentity

/-- At a phase-aligned endpoint, any zero of the Gaussian value port forces
the tangent port to vanish as well. -/
theorem value_zero_forces_tangent_zero
    (A endpointValue frequency cosineValue tangentValue : ℝ)
    (hidentity :
      tangentValue =
        boundaryIdentityRhs A endpointValue 0 frequency cosineValue)
    (hcosine : cosineValue = 0) :
    tangentValue = 0 := by
  rw [tangent_eq_scalar_value_of_phase_aligned A endpointValue frequency
    cosineValue tangentValue hidentity, hcosine]
  simp

/-- The resulting collision jet has dependent value and tangent ports. -/
theorem phase_aligned_gaussian_collision_jet
    (A endpointValue frequency sineValue cosineValue tangentValue : ℝ)
    (hidentity :
      tangentValue =
        boundaryIdentityRhs A endpointValue 0 frequency cosineValue)
    (hcosine : cosineValue = 0) :
    (HalfTransformJet.mk cosineValue sineValue tangentValue).DoubleZero := by
  rw [HalfTransformJet.doubleZero_iff_cosine_firstSine_zero]
  exact ⟨hcosine,
    value_zero_forces_tangent_zero A endpointValue frequency cosineValue
      tangentValue hidentity hcosine⟩

end GaussianBoundaryCollision

/-! Seam-matched Gaussian score residual. -/

namespace SeamMatchedScore

/-- Integration-by-parts normal form for the sine readout of the matched score
residual. -/
def residualIdentityRhs
    (boundaryTerm frequency cosineValue curvature tangentValue : ℝ) : ℝ :=
  boundaryTerm - frequency * cosineValue +
    2 * curvature * tangentValue

theorem residual_eq_phase_aligned_normal_form
    (frequency cosineValue curvature tangentValue residualValue : ℝ)
    (hidentity :
      residualValue = residualIdentityRhs 0 frequency cosineValue curvature
        tangentValue) :
    residualValue =
      -frequency * cosineValue + 2 * curvature * tangentValue := by
  simpa [residualIdentityRhs] using hidentity

/-- On the phase-aligned cosine-zero locus, nonzero matched curvature lets the
score residual reconstruct the tangent port. -/
theorem tangent_eq_residual_div_of_cosine_zero
    (frequency cosineValue curvature tangentValue residualValue : ℝ)
    (hcurvature : curvature ≠ 0)
    (hcosine : cosineValue = 0)
    (hidentity :
      residualValue = residualIdentityRhs 0 frequency cosineValue curvature
        tangentValue) :
    tangentValue = residualValue / (2 * curvature) := by
  have hform := residual_eq_phase_aligned_normal_form frequency cosineValue
    curvature tangentValue residualValue hidentity
  rw [hcosine] at hform
  have hden : 2 * curvature ≠ 0 := mul_ne_zero (by norm_num) hcurvature
  apply (eq_div_iff hden).2
  rw [hform]
  ring

/-- With nonzero matched curvature, the original value/tangent collision is
equivalent to simultaneous vanishing of the value and score-residual ports. -/
theorem doubleZero_iff_cosine_residual_zero
    (frequency cosineValue sineValue curvature tangentValue residualValue : ℝ)
    (hcurvature : curvature ≠ 0)
    (hidentity :
      residualValue = residualIdentityRhs 0 frequency cosineValue curvature
        tangentValue) :
    (HalfTransformJet.mk cosineValue sineValue tangentValue).DoubleZero ↔
      cosineValue = 0 ∧ residualValue = 0 := by
  rw [HalfTransformJet.doubleZero_iff_cosine_firstSine_zero]
  constructor
  · rintro ⟨hcosine, htangent⟩
    refine ⟨hcosine, ?_⟩
    rw [residual_eq_phase_aligned_normal_form frequency cosineValue curvature
      tangentValue residualValue hidentity, hcosine, htangent]
    ring
  · rintro ⟨hcosine, hresidual⟩
    refine ⟨hcosine, ?_⟩
    have hreconstruct := tangent_eq_residual_div_of_cosine_zero frequency
      cosineValue curvature tangentValue residualValue hcurvature hcosine
      hidentity
    rw [hresidual] at hreconstruct
    simpa using hreconstruct

/-- Translating the seam-matched score produces a primitive-score term and a
logarithmic shear term.  Here `logLabel` is an abstract translated coordinate;
identifying it with `log n` is an analytic/source interface. -/
theorem translated_score_shear_identity
    (curvature u logLabel phiValue phiDerivative : ℝ) :
    phiDerivative + 2 * curvature * u * phiValue =
      (phiDerivative + 2 * curvature * (u + logLabel) * phiValue) -
        2 * curvature * logLabel * phiValue := by
  ring

/-- A pure matched Gaussian has zero score residual, so the residual port adds
no information beyond the value port. -/
theorem zero_residual_collapses_transverse_port
    (frequency cosineValue sineValue curvature tangentValue : ℝ)
    (hcurvature : curvature ≠ 0)
    (hidentity :
      0 = residualIdentityRhs 0 frequency cosineValue curvature tangentValue)
    (hcosine : cosineValue = 0) :
    (HalfTransformJet.mk cosineValue sineValue tangentValue).DoubleZero := by
  rw [doubleZero_iff_cosine_residual_zero frequency cosineValue sineValue
    curvature tangentValue 0 hcurvature hidentity]
  exact ⟨hcosine, rfl⟩

end SeamMatchedScore

end MariciFormal
