import MariciFormal.DeterminantalProfileBaseChange

/-!
Coefficient specialization can preserve the construction of a determinantal
profile without reflecting distinctions between source profiles.
-/

namespace MariciFormal

def unitPoint : Fin 2 → Rat := fun _ => 1

theorem specializeAtUnit_fixtures :
    specializeMatrix unitPoint separateAxisMatrix = 1 ∧
      specializeMatrix unitPoint productAxisMatrix = 1 := by
  constructor <;>
    ext i j <;>
    fin_cases i <;> fin_cases j <;>
    norm_num [specializeMatrix, separateAxisMatrix, productAxisMatrix,
      variableU, variableV, unitPoint]

theorem unitPoint_mapped_profiles_agree :
    mapTwoByTwoDeterminantalProfile (MvPolynomial.eval unitPoint)
        (twoByTwoDeterminantalProfile separateAxisMatrix) =
      mapTwoByTwoDeterminantalProfile (MvPolynomial.eval unitPoint)
        (twoByTwoDeterminantalProfile productAxisMatrix) := by
  rw [map_twoByTwoDeterminantalProfile, map_twoByTwoDeterminantalProfile]
  apply congrArg twoByTwoDeterminantalProfile
  change specializeMatrix unitPoint separateAxisMatrix =
    specializeMatrix unitPoint productAxisMatrix
  rw [specializeAtUnit_fixtures.1, specializeAtUnit_fixtures.2]

/-- Base-change compatibility does not imply that the coefficient map reflects
distinct determinantal profiles. -/
theorem specialization_does_not_reflect_profile_distinctions :
    twoByTwoDeterminantalProfile separateAxisMatrix ≠
        twoByTwoDeterminantalProfile productAxisMatrix ∧
      mapTwoByTwoDeterminantalProfile (MvPolynomial.eval unitPoint)
          (twoByTwoDeterminantalProfile separateAxisMatrix) =
        mapTwoByTwoDeterminantalProfile (MvPolynomial.eval unitPoint)
          (twoByTwoDeterminantalProfile productAxisMatrix) :=
  ⟨fixture_profiles_differ_despite_equal_topStage.2,
    unitPoint_mapped_profiles_agree⟩

end MariciFormal
