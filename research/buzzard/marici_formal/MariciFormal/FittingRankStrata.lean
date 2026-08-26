import Mathlib

/-!
Over a multivariable coefficient ring, equal determinant ideals can hide
different deeper rank strata. Lower determinantal data remains necessary.
-/

namespace MariciFormal

open MvPolynomial

abbrev TwoVariablePolynomial := MvPolynomial (Fin 2) Rat
abbrev BivariateMatrix₂ := Matrix (Fin 2) (Fin 2) TwoVariablePolynomial
abbrev SpecializedMatrix₂ := Matrix (Fin 2) (Fin 2) Rat

noncomputable def variableU : TwoVariablePolynomial := X 0
noncomputable def variableV : TwoVariablePolynomial := X 1

noncomputable def separateAxisMatrix : BivariateMatrix₂ :=
  !![variableU, 0; 0, variableV]

noncomputable def productAxisMatrix : BivariateMatrix₂ :=
  !![1, 0; 0, variableU * variableV]

noncomputable def specializeMatrix
    (point : Fin 2 → Rat) (matrix : BivariateMatrix₂) : SpecializedMatrix₂ :=
  fun i j => MvPolynomial.eval point (matrix i j)

theorem determinantPolynomials_agree :
    separateAxisMatrix.det = variableU * variableV ∧
      productAxisMatrix.det = variableU * variableV := by
  constructor <;>
    rw [Matrix.det_fin_two] <;>
    simp [separateAxisMatrix, productAxisMatrix]

def origin : Fin 2 → Rat := fun _ => 0

theorem specializeAtOrigin_fixtures :
    specializeMatrix origin separateAxisMatrix = 0 ∧
      specializeMatrix origin productAxisMatrix = !![1, 0; 0, 0] := by
  constructor <;>
    ext i j <;>
    fin_cases i <;> fin_cases j <;>
    norm_num [specializeMatrix, separateAxisMatrix, productAxisMatrix,
      variableU, variableV, origin]

theorem separateAxis_origin_annihilates_everyVector (x : Fin 2 → Rat) :
    (specializeMatrix origin separateAxisMatrix).mulVec x = 0 := by
  rw [specializeAtOrigin_fixtures.1]
  simp

theorem productAxis_origin_action (x : Fin 2 → Rat) :
    (specializeMatrix origin productAxisMatrix).mulVec x = ![x 0, 0] := by
  rw [specializeAtOrigin_fixtures.2]
  funext i
  fin_cases i <;> simp [Matrix.mulVec, dotProduct]

theorem productAxis_origin_has_nonzeroImage :
    (specializeMatrix origin productAxisMatrix).mulVec ![1, 0] ≠ 0 := by
  rw [productAxis_origin_action]
  intro h
  have h0 := congrFun h 0
  norm_num at h0

/-- Equal top determinant data does not determine the deepest rank stratum. -/
theorem determinantLocus_does_not_determine_originRank :
    separateAxisMatrix.det = productAxisMatrix.det ∧
      (∀ x, (specializeMatrix origin separateAxisMatrix).mulVec x = 0) ∧
      ∃ x, (specializeMatrix origin productAxisMatrix).mulVec x ≠ 0 := by
  exact ⟨determinantPolynomials_agree.1.trans
      determinantPolynomials_agree.2.symm,
    separateAxis_origin_annihilates_everyVector,
    ⟨![1, 0], productAxis_origin_has_nonzeroImage⟩⟩

end MariciFormal
