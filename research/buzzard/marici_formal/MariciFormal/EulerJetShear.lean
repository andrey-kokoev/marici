import Mathlib

/-!
Exact finite matrix core of Grothendieck's normalized Euler value-flux jet
transport, shared with unipotent optical transfer shears.
-/

namespace MariciFormal.EulerJetShear

def lowerShear (slope : ℚ) : Matrix (Fin 2) (Fin 2) ℚ :=
  !![1, 0; slope, 1]

theorem lowerShear_mul (first second : ℚ) :
    lowerShear first * lowerShear second =
      lowerShear (first + second) := by
  ext row column
  fin_cases row <;> fin_cases column <;>
    simp [lowerShear, Matrix.mul_apply, Fin.sum_univ_two]

theorem lowerShear_commute (first second : ℚ) :
    lowerShear first * lowerShear second =
      lowerShear second * lowerShear first := by
  rw [lowerShear_mul, lowerShear_mul, add_comm]

theorem lowerShear_det (slope : ℚ) :
    (lowerShear slope).det = 1 := by
  norm_num [lowerShear, Matrix.det_fin_two]

/-- Comparison between two charts derived from one slope potential. -/
def shearTransition (potential : ι → ℚ) (source target : ι) :
    Matrix (Fin 2) (Fin 2) ℚ :=
  lowerShear (potential target - potential source)

theorem shearTransition_comp
    (potential : ι → ℚ) (first second third : ι) :
    shearTransition potential first second *
        shearTransition potential second third =
      shearTransition potential first third := by
  rw [shearTransition, shearTransition, shearTransition, lowerShear_mul]
  congr 1
  ring

theorem shearTransition_triangle
    (potential : ι → ℚ) (first second third : ι) :
    shearTransition potential first second *
        shearTransition potential second third *
        shearTransition potential third first = 1 := by
  rw [shearTransition_comp]
  simp only [shearTransition]
  rw [lowerShear_mul]
  have slopeZero :
      potential third - potential first +
        (potential first - potential third) = 0 := by ring
  rw [slopeZero]
  ext row column
  fin_cases row <;> fin_cases column <;> simp [lowerShear]

/-- A genuinely different nilpotent direction. -/
def upperShear (slope : ℚ) : Matrix (Fin 2) (Fin 2) ℚ :=
  !![1, slope; 0, 1]

/-- Hostile omitted premise: a second shear generator need not commute with
the Euler lower-shear channel. -/
theorem second_generator_breaks_commutativity :
    lowerShear 1 * upperShear 1 ≠ upperShear 1 * lowerShear 1 := by
  intro equality
  have atZeroZero := congrFun (congrFun equality 0) 0
  norm_num [lowerShear, upperShear, Matrix.mul_apply,
    Fin.sum_univ_two] at atZeroZero

end MariciFormal.EulerJetShear
