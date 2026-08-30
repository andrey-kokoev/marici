import MariciFormal.BaseChangeNonreflection

/-!
For the determinant-collision fixtures, rational specialization separates the
two determinantal profiles exactly at the origin.
-/

namespace MariciFormal

noncomputable def specializedProfile (point : Fin 2 → Rat)
    (matrix : BivariateMatrix₂) : TwoByTwoDeterminantalProfile Rat :=
  twoByTwoDeterminantalProfile (specializeMatrix point matrix)

theorem specializeMatrix_fixtures (point : Fin 2 → Rat) :
    specializeMatrix point separateAxisMatrix = !![point 0, 0; 0, point 1] ∧
      specializeMatrix point productAxisMatrix =
        !![1, 0; 0, point 0 * point 1] := by
  constructor <;>
    ext i j <;>
    fin_cases i <;> fin_cases j <;>
    simp [specializeMatrix, separateAxisMatrix, productAxisMatrix,
      variableU, variableV]

theorem matrixEntryIdeal_eq_top_of_entry_ne_zero
    {matrix : Matrix (Fin 2) (Fin 2) Rat} {i j : Fin 2}
    (hentry : matrix i j ≠ 0) :
    matrixEntryIdeal matrix = ⊤ := by
  rw [Ideal.eq_top_iff_one]
  have hmem := (matrixEntryIdeal matrix).mul_mem_left (matrix i j)⁻¹
    (matrixEntry_mem matrix i j)
  simpa [inv_mul_cancel₀ hentry] using hmem

theorem separate_specialized_entryIdeal_eq_top_of_ne_origin
    {point : Fin 2 → Rat} (hpoint : point ≠ origin) :
    matrixEntryIdeal (specializeMatrix point separateAxisMatrix) = ⊤ := by
  have hcoordinate : point 0 ≠ 0 ∨ point 1 ≠ 0 := by
    by_contra hzero
    push Not at hzero
    apply hpoint
    funext i
    fin_cases i <;> simp [origin, hzero.1, hzero.2]
  rw [specializeMatrix_fixtures point |>.1]
  rcases hcoordinate with h0 | h1
  · exact matrixEntryIdeal_eq_top_of_entry_ne_zero (i := 0) (j := 0)
      (by simpa using h0)
  · exact matrixEntryIdeal_eq_top_of_entry_ne_zero (i := 1) (j := 1)
      (by simpa using h1)

theorem product_specialized_entryIdeal_eq_top (point : Fin 2 → Rat) :
    matrixEntryIdeal (specializeMatrix point productAxisMatrix) = ⊤ := by
  rw [specializeMatrix_fixtures point |>.2]
  exact matrixEntryIdeal_eq_top_of_entry_ne_zero (i := 0) (j := 0)
    (by norm_num)

theorem specialized_secondIdeals_agree (point : Fin 2 → Rat) :
    secondDeterminantalIdeal (specializeMatrix point separateAxisMatrix) =
      secondDeterminantalIdeal (specializeMatrix point productAxisMatrix) := by
  rw [specializeMatrix_eq_mapMatrix, specializeMatrix_eq_mapMatrix,
    ← map_secondDeterminantalIdeal, ← map_secondDeterminantalIdeal,
    fixture_secondDeterminantalIdeals_agree]

theorem specialized_profiles_agree_of_ne_origin
    {point : Fin 2 → Rat} (hpoint : point ≠ origin) :
    specializedProfile point separateAxisMatrix =
      specializedProfile point productAxisMatrix := by
  unfold specializedProfile twoByTwoDeterminantalProfile
  congr 1
  · rw [separate_specialized_entryIdeal_eq_top_of_ne_origin hpoint,
      product_specialized_entryIdeal_eq_top]
  · exact specialized_secondIdeals_agree point

theorem specialized_profiles_differ_at_origin :
    specializedProfile origin separateAxisMatrix ≠
      specializedProfile origin productAxisMatrix := by
  intro hprofile
  have hfirst := congrArg TwoByTwoDeterminantalProfile.first hprofile
  change matrixEntryIdeal (specializeMatrix origin separateAxisMatrix) =
    matrixEntryIdeal (specializeMatrix origin productAxisMatrix) at hfirst
  change matrixEntryIdeal (separateAxisMatrix.map (MvPolynomial.eval origin)) =
    matrixEntryIdeal (productAxisMatrix.map (MvPolynomial.eval origin)) at hfirst
  rw [← map_matrixEntryIdeal, ← map_matrixEntryIdeal] at hfirst
  exact origin_baseChanged_entryIdeals_differ hfirst

/-- The exact rational-point separation locus for the fixture is the origin. -/
theorem specialized_profiles_differ_iff_origin (point : Fin 2 → Rat) :
    specializedProfile point separateAxisMatrix ≠
        specializedProfile point productAxisMatrix ↔
      point = origin := by
  constructor
  · intro hdiffer
    by_contra hpoint
    exact hdiffer (specialized_profiles_agree_of_ne_origin hpoint)
  · rintro rfl
    exact specialized_profiles_differ_at_origin

end MariciFormal
