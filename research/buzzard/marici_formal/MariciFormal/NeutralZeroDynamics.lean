import MariciFormal.BorderedPencilSymmetrizer
import Mathlib.Analysis.Matrix.Hermitian

/-!
Finite neutral-state identity for a symmetrized bordered pencil, together with
Nima's exact three-state hostile.  Completion is intentionally absent: its
uniform residual estimates require a separate interface.
-/

namespace MariciFormal

open Matrix Complex

/-- The scalar core of the finite energy argument.  If the carrier energy,
source pairing, and Krein charge are real, then the imaginary part of
`carrierEnergy - z * charge = sourceEnergy` forces neutrality off the real
axis. -/
theorem imaginaryPart_mul_charge_eq_zero
    (carrierEnergy sourceEnergy charge : ℝ) (z : ℂ)
    (henergy : (carrierEnergy : ℂ) - z * (charge : ℂ) = sourceEnergy) :
    z.im * charge = 0 := by
  have him := congrArg Complex.im henergy
  norm_num at him
  linarith

theorem charge_eq_zero_of_offReal
    (carrierEnergy sourceEnergy charge : ℝ) (z : ℂ)
    (hz : z.im ≠ 0)
    (henergy : (carrierEnergy : ℂ) - z * (charge : ℂ) = sourceEnergy) :
    charge = 0 := by
  exact (mul_eq_zero.mp
    (imaginaryPart_mul_charge_eq_zero carrierEnergy sourceEnergy charge z henergy)).resolve_left hz

section MatrixEnergy

variable {ι : Type*} [Fintype ι] [DecidableEq ι]

def kreinPairing (K : Matrix ι ι ℂ) (x y : ι → ℂ) : ℂ :=
  star x ⬝ᵥ (K *ᵥ y)

def kreinCharge (K : Matrix ι ι ℂ) (x : ι → ℂ) : ℂ :=
  kreinPairing K x x

/-- A Hermitian matrix has real quadratic values. -/
theorem kreinCharge_im_eq_zero
    (K : Matrix ι ι ℂ) (x : ι → ℂ) (hK : Kᴴ = K) :
    (kreinCharge K x).im = 0 := by
  exact (show K.IsHermitian from hK).im_star_dotProduct_mulVec_self x

/-- Commuting Hermitian matrices have Hermitian product. -/
theorem hermitian_mul_of_commute
    (A K : Matrix ι ι ℂ) (hA : Aᴴ = A) (hK : Kᴴ = K)
    (hcomm : A * K = K * A) : (K * A)ᴴ = K * A := by
  rw [Matrix.conjTranspose_mul, hA, hK, hcomm]

/-- The finite zero-dynamics assumptions imply the scalar energy equation.
The source invisibility equation is `c* x = 0`, written as a dot product. -/
theorem finiteZeroDynamics_energyEquation
    (A K : Matrix ι ι ℂ) (b c x : ι → ℂ) (z : ℂ) (α : ℝ)
    (hdynamics : A *ᵥ x - z • x = -b)
    (hinvisible : star c ⬝ᵥ x = 0)
    (hcomm : A * K = K * A)
    (hKb : K *ᵥ b = (α : ℂ) • c) :
    kreinPairing (K * A) x x - z * kreinCharge K x = 0 := by
  have hpaired := congrArg (fun y => star x ⬝ᵥ (K *ᵥ y)) hdynamics
  simp only [Matrix.mulVec_sub, Matrix.mulVec_smul, Matrix.mulVec_neg,
    Matrix.dotProduct_sub, Matrix.dotProduct_smul, Matrix.dotProduct_neg,
    Matrix.mulVec_mulVec, hcomm, hKb] at hpaired
  have hsource : star x ⬝ᵥ c = 0 := by
    rw [Matrix.star_dotProduct]
    simp [hinvisible]
  simpa [kreinPairing, kreinCharge, hsource] using hpaired

/-- Finite neutral-state identity.  The conclusion is stated using the real
part of the Krein charge; Hermiticity separately proves its imaginary part is
zero. -/
theorem finiteZeroDynamics_im_mul_kreinCharge
    (A K : Matrix ι ι ℂ) (b c x : ι → ℂ) (z : ℂ) (α : ℝ)
    (hA : Aᴴ = A) (hK : Kᴴ = K)
    (hdynamics : A *ᵥ x - z • x = -b)
    (hinvisible : star c ⬝ᵥ x = 0)
    (hcomm : A * K = K * A)
    (hKb : K *ᵥ b = (α : ℂ) • c) :
    z.im * (kreinCharge K x).re = 0 := by
  have hKA := hermitian_mul_of_commute A K hA hK hcomm
  have hcarrierReal := kreinCharge_im_eq_zero (K * A) x hKA
  have hchargeReal := kreinCharge_im_eq_zero K x hK
  have henergy := finiteZeroDynamics_energyEquation A K b c x z α
    hdynamics hinvisible hcomm hKb
  have him := congrArg Complex.im henergy
  simp [kreinPairing, kreinCharge, hcarrierReal, hchargeReal] at him
  linarith

/-- An off-real finite zero-dynamics state is exactly Krein-neutral. -/
theorem finiteZeroDynamics_kreinNeutral_of_offReal
    (A K : Matrix ι ι ℂ) (b c x : ι → ℂ) (z : ℂ) (α : ℝ)
    (hA : Aᴴ = A) (hK : Kᴴ = K)
    (hdynamics : A *ᵥ x - z • x = -b)
    (hinvisible : star c ⬝ᵥ x = 0)
    (hcomm : A * K = K * A)
    (hKb : K *ᵥ b = (α : ℂ) • c)
    (hoffReal : z.im ≠ 0) :
    kreinCharge K x = 0 := by
  have hproduct := finiteZeroDynamics_im_mul_kreinCharge A K b c x z α
    hA hK hdynamics hinvisible hcomm hKb
  have hreal : (kreinCharge K x).re = 0 :=
    (mul_eq_zero.mp hproduct).resolve_left hoffReal
  have himaginary := kreinCharge_im_eq_zero K x hK
  exact Complex.ext hreal himaginary

/-- Finite exclusion principle: a nonneutral admissible zero-dynamics state
can occur only at a real spectral parameter.  This is pointwise and makes no
uniform completion claim. -/
theorem finiteZeroDynamics_real_of_kreinCharge_ne_zero
    (A K : Matrix ι ι ℂ) (b c x : ι → ℂ) (z : ℂ) (α : ℝ)
    (hA : Aᴴ = A) (hK : Kᴴ = K)
    (hdynamics : A *ᵥ x - z • x = -b)
    (hinvisible : star c ⬝ᵥ x = 0)
    (hcomm : A * K = K * A)
    (hKb : K *ᵥ b = (α : ℂ) • c)
    (hnonneutral : kreinCharge K x ≠ 0) :
    z.im = 0 := by
  by_contra hoffReal
  exact hnonneutral (finiteZeroDynamics_kreinNeutral_of_offReal
    A K b c x z α hA hK hdynamics hinvisible hcomm hKb hoffReal)

end MatrixEnergy

section ThreeStateHostile

def threeStateCarrier : Matrix (Fin 3) (Fin 3) ℂ :=
  !![-1, 0, 0; 0, 0, 0; 0, 0, 1]

def threeStateMetric : Matrix (Fin 3) (Fin 3) ℂ :=
  !![1, 0, 0; 0, -1, 0; 0, 0, 1]

def threeStateActuator : Fin 3 → ℂ := ![1, 1, 1]

def threeStateSensor : Fin 3 → ℂ := ![1, -1, 1]

theorem threeStateCarrier_isHermitian : threeStateCarrierᴴ = threeStateCarrier := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    norm_num [threeStateCarrier]

theorem threeStateMetric_isHermitian : threeStateMetricᴴ = threeStateMetric := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    norm_num [threeStateMetric]

theorem threeState_carrier_metric_commute :
    threeStateCarrier * threeStateMetric = threeStateMetric * threeStateCarrier := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    norm_num [threeStateCarrier, threeStateMetric, Matrix.mul_apply]

theorem threeState_metric_maps_actuator_to_sensor :
    threeStateMetric *ᵥ threeStateActuator = threeStateSensor := by
  funext i
  fin_cases i <;>
    norm_num [threeStateMetric, threeStateActuator, threeStateSensor,
      Matrix.mulVec, dotProduct]

/-- The common-denominator numerator of the three-state transfer. -/
def threeStateTransferNumerator (z : ℂ) : ℂ :=
  (-z) * (1 - z) - (-1 - z) * (1 - z) + (-1 - z) * (-z)

theorem threeStateTransferNumerator_eq (z : ℂ) :
    threeStateTransferNumerator z = z ^ 2 + 1 := by
  ring

theorem threeStateTransferNumerator_at_I :
    threeStateTransferNumerator Complex.I = 0 := by
  rw [threeStateTransferNumerator_eq]
  norm_num [Complex.I_mul_I, pow_two]

theorem threeStateTransferNumerator_at_neg_I :
    threeStateTransferNumerator (-Complex.I) = 0 := by
  rw [threeStateTransferNumerator_eq]
  norm_num [Complex.I_mul_I, pow_two]

/-- Explicit zero-dynamics state at `z = i`. -/
def threeStatePositiveImaginaryState : Fin 3 → ℂ :=
  ![(1 - Complex.I) / 2, -Complex.I, -(1 + Complex.I) / 2]

theorem threeStatePositiveImaginaryState_dynamics :
    threeStateCarrier *ᵥ threeStatePositiveImaginaryState -
      Complex.I • threeStatePositiveImaginaryState = -threeStateActuator := by
  funext i
  fin_cases i <;>
    norm_num [threeStateCarrier, threeStatePositiveImaginaryState,
      threeStateActuator, Matrix.mulVec, dotProduct, Complex.I_mul_I]

theorem threeStatePositiveImaginaryState_invisible :
    star threeStateSensor ⬝ᵥ threeStatePositiveImaginaryState = 0 := by
  norm_num [threeStateSensor, threeStatePositiveImaginaryState, dotProduct]

theorem threeStatePositiveImaginaryState_neutral :
    kreinCharge threeStateMetric threeStatePositiveImaginaryState = 0 := by
  norm_num [kreinCharge, kreinPairing, threeStateMetric,
    threeStatePositiveImaginaryState, Matrix.mulVec, dotProduct,
    Complex.normSq_apply]

/-- The conjugate zero-dynamics state at `z = -i`. -/
def threeStateNegativeImaginaryState : Fin 3 → ℂ :=
  ![(1 + Complex.I) / 2, Complex.I, -(1 - Complex.I) / 2]

theorem threeStateNegativeImaginaryState_dynamics :
    threeStateCarrier *ᵥ threeStateNegativeImaginaryState -
      (-Complex.I) • threeStateNegativeImaginaryState = -threeStateActuator := by
  funext i
  fin_cases i <;>
    norm_num [threeStateCarrier, threeStateNegativeImaginaryState,
      threeStateActuator, Matrix.mulVec, dotProduct, Complex.I_mul_I]

theorem threeStateNegativeImaginaryState_invisible :
    star threeStateSensor ⬝ᵥ threeStateNegativeImaginaryState = 0 := by
  norm_num [threeStateSensor, threeStateNegativeImaginaryState, dotProduct]

theorem threeStateNegativeImaginaryState_neutral :
    kreinCharge threeStateMetric threeStateNegativeImaginaryState = 0 := by
  norm_num [kreinCharge, kreinPairing, threeStateMetric,
    threeStateNegativeImaginaryState, Matrix.mulVec, dotProduct,
    Complex.normSq_apply]

/-- The reusable finite theorem forces neutrality of the positive-imaginary
hostile witness from the structural certificates. -/
theorem threeStatePositiveImaginaryState_neutral_by_general_theorem :
    kreinCharge threeStateMetric threeStatePositiveImaginaryState = 0 := by
  apply finiteZeroDynamics_kreinNeutral_of_offReal
    threeStateCarrier threeStateMetric threeStateActuator threeStateSensor
    threeStatePositiveImaginaryState Complex.I 1
  · exact threeStateCarrier_isHermitian
  · exact threeStateMetric_isHermitian
  · exact threeStatePositiveImaginaryState_dynamics
  · exact threeStatePositiveImaginaryState_invisible
  · exact threeState_carrier_metric_commute
  · simpa using threeState_metric_maps_actuator_to_sensor
  · norm_num

/-- The reusable finite theorem likewise forces neutrality of the conjugate
negative-imaginary witness. -/
theorem threeStateNegativeImaginaryState_neutral_by_general_theorem :
    kreinCharge threeStateMetric threeStateNegativeImaginaryState = 0 := by
  apply finiteZeroDynamics_kreinNeutral_of_offReal
    threeStateCarrier threeStateMetric threeStateActuator threeStateSensor
    threeStateNegativeImaginaryState (-Complex.I) 1
  · exact threeStateCarrier_isHermitian
  · exact threeStateMetric_isHermitian
  · exact threeStateNegativeImaginaryState_dynamics
  · exact threeStateNegativeImaginaryState_invisible
  · exact threeState_carrier_metric_commute
  · simpa using threeState_metric_maps_actuator_to_sensor
  · norm_num

/-- Both members of the hostile conjugate pair have explicit invisible,
Krein-neutral zero-dynamics witnesses. -/
theorem threeStateHostile_has_conjugate_neutral_pair :
    (threeStateCarrier *ᵥ threeStatePositiveImaginaryState -
        Complex.I • threeStatePositiveImaginaryState = -threeStateActuator ∧
      star threeStateSensor ⬝ᵥ threeStatePositiveImaginaryState = 0 ∧
      kreinCharge threeStateMetric threeStatePositiveImaginaryState = 0) ∧
    (threeStateCarrier *ᵥ threeStateNegativeImaginaryState -
        (-Complex.I) • threeStateNegativeImaginaryState = -threeStateActuator ∧
      star threeStateSensor ⬝ᵥ threeStateNegativeImaginaryState = 0 ∧
      kreinCharge threeStateMetric threeStateNegativeImaginaryState = 0) := by
  exact ⟨⟨threeStatePositiveImaginaryState_dynamics,
      threeStatePositiveImaginaryState_invisible,
      threeStatePositiveImaginaryState_neutral⟩,
    ⟨threeStateNegativeImaginaryState_dynamics,
      threeStateNegativeImaginaryState_invisible,
      threeStateNegativeImaginaryState_neutral⟩⟩

end ThreeStateHostile

end MariciFormal
