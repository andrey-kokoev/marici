import Mathlib.Data.Matrix.Notation
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.NormNum

/-!
Finite unitary/orthogonal hostile for Grothendieck's incidence-divisor no-go,
together with the algebraic four-channel cancellation core of Poisson sewing.
-/

namespace MariciFormal

open Matrix

section QuarterRotation

def quarterRotation : Matrix (Fin 2) (Fin 2) ℝ :=
  !![0, -1;
     1,  0]

def incidenceSource : Fin 2 → ℝ
  | 0 => 1
  | 1 => 0

def endpointCoordinate (v : Fin 2 → ℝ) : ℝ :=
  v 0

def complementaryCoordinate (v : Fin 2 → ℝ) : ℝ :=
  v 1

def incidenceReadout (T : Matrix (Fin 2) (Fin 2) ℝ) : ℝ :=
  endpointCoordinate (T *ᵥ incidenceSource)

theorem quarterRotation_det : quarterRotation.det = 1 := by
  norm_num [quarterRotation, Matrix.det_fin_two]

theorem quarterRotation_orthogonal :
    quarterRotationᵀ * quarterRotation = 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    norm_num [quarterRotation, Matrix.mul_apply]

theorem quarterRotation_output :
    quarterRotation *ᵥ incidenceSource = fun i => if i = 1 then 1 else 0 := by
  funext i
  fin_cases i <;>
    norm_num [quarterRotation, incidenceSource, Matrix.mulVec]

/-- The selected scalar coordinate vanishes although the full transfer has
determinant one and the complementary port contains the entire source. -/
theorem quarterRotation_incidence_crossing :
    incidenceReadout quarterRotation = 0 ∧
      complementaryCoordinate (quarterRotation *ᵥ incidenceSource) = 1 ∧
      quarterRotation.det = 1 := by
  norm_num [incidenceReadout, endpointCoordinate, complementaryCoordinate,
    quarterRotation, incidenceSource, Matrix.mulVec, Matrix.det_fin_two]

def InIncidenceCell (T : Matrix (Fin 2) (Fin 2) ℝ) : Prop :=
  incidenceReadout T ≠ 0

theorem quarterRotation_outside_incidence_cell :
    ¬ InIncidenceCell quarterRotation := by
  simp [InIncidenceCell, incidenceReadout, endpointCoordinate,
    quarterRotation, incidenceSource, Matrix.mulVec]

end QuarterRotation

section FourChannelSewing

variable {R : Type*} [AddCommGroup R]

def fourChannelIncidence (bulk direct dualPole sourcePole : R) : R :=
  bulk + direct + dualPole + sourcePole

def incidenceDescentDefect (transportedIncidence sourceIncidence : R) : R :=
  transportedIncidence - sourceIncidence

theorem incidenceDescentDefect_eq_zero_iff
    (transportedIncidence sourceIncidence : R) :
    incidenceDescentDefect transportedIncidence sourceIncidence = 0 ↔
      transportedIncidence = sourceIncidence := by
  simp [incidenceDescentDefect]

end FourChannelSewing

section FourChannelHostile

/-- Four individually nonzero channels can cancel exactly after scalar
aggregation. -/
theorem nonzero_four_channels_can_cancel :
    fourChannelIncidence (R := ℤ) 1 1 (-1) (-1) = 0 ∧
      (1 : ℤ) ≠ 0 ∧ (1 : ℤ) ≠ 0 ∧ (-1 : ℤ) ≠ 0 ∧ (-1 : ℤ) ≠ 0 := by
  norm_num [fourChannelIncidence]

end FourChannelHostile

end MariciFormal
