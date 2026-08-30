import Mathlib

/-!
Residue-flag comparison cells are nonunique, and pairwise-valid comparisons
can carry nonidentity stabilizer holonomy around a triangle.
-/

namespace MariciFormal

abbrev FlagVector := Fin 2 → Rat
abbrev FlagComparison := Matrix (Fin 2) (Fin 2) Rat

def carriesFlag (comparison : FlagComparison) (source target : FlagVector) : Prop :=
  comparison.mulVec source = target

def InvertibleComparison (comparison : FlagComparison) : Prop := comparison.det ≠ 0

def flag₀ : FlagVector := ![1, 0]
def flag₁ : FlagVector := ![0, 1]
def flag₂ : FlagVector := ![1, 1]

def comparison₀₁ : FlagComparison := !![0, 1; 1, 0]
def comparison₁₂ : FlagComparison := !![1, 1; 0, 1]
def comparison₂₀ : FlagComparison := !![1, 0; -1, 1]

def triangleHolonomy : FlagComparison :=
  comparison₂₀ * comparison₁₂ * comparison₀₁

def expectedTriangleHolonomy : FlagComparison := !![1, 1; 0, -1]

theorem pairwiseComparisons_valid :
    InvertibleComparison comparison₀₁ ∧
      InvertibleComparison comparison₁₂ ∧
      InvertibleComparison comparison₂₀ ∧
      carriesFlag comparison₀₁ flag₀ flag₁ ∧
      carriesFlag comparison₁₂ flag₁ flag₂ ∧
      carriesFlag comparison₂₀ flag₂ flag₀ := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_⟩
  · norm_num [InvertibleComparison, comparison₀₁, Matrix.det_fin_two]
  · norm_num [InvertibleComparison, comparison₁₂, Matrix.det_fin_two]
  · norm_num [InvertibleComparison, comparison₂₀, Matrix.det_fin_two]
  all_goals
    funext i
    fin_cases i <;>
      norm_num [carriesFlag, comparison₀₁, comparison₁₂, comparison₂₀,
        flag₀, flag₁, flag₂, Matrix.mulVec, dotProduct]

theorem triangleHolonomy_fixture :
    triangleHolonomy = expectedTriangleHolonomy ∧
      triangleHolonomy ≠ 1 ∧
      carriesFlag triangleHolonomy flag₀ flag₀ := by
  constructor
  · ext i j
    fin_cases i <;> fin_cases j <;>
      norm_num [triangleHolonomy, expectedTriangleHolonomy, comparison₀₁,
        comparison₁₂, comparison₂₀, Matrix.mul_apply]
  · constructor
    · intro h
      have h01 := congrArg (fun matrix : FlagComparison => matrix 0 1) h
      norm_num [triangleHolonomy, comparison₀₁, comparison₁₂, comparison₂₀,
        Matrix.mul_apply] at h01
    · funext i
      fin_cases i <;>
        norm_num [carriesFlag, triangleHolonomy, comparison₀₁, comparison₁₂,
          comparison₂₀, flag₀, Matrix.mulVec, Matrix.mul_apply, dotProduct]

/-- Pairwise-valid comparison cells do not imply coherent triple descent. -/
theorem pairwiseFlagComparison_does_not_imply_triangleCoherence :
    (InvertibleComparison comparison₀₁ ∧ carriesFlag comparison₀₁ flag₀ flag₁) ∧
      (InvertibleComparison comparison₁₂ ∧ carriesFlag comparison₁₂ flag₁ flag₂) ∧
      (InvertibleComparison comparison₂₀ ∧ carriesFlag comparison₂₀ flag₂ flag₀) ∧
      triangleHolonomy ≠ 1 := by
  exact ⟨⟨pairwiseComparisons_valid.1, pairwiseComparisons_valid.2.2.2.1⟩,
    ⟨pairwiseComparisons_valid.2.1, pairwiseComparisons_valid.2.2.2.2.1⟩,
    ⟨pairwiseComparisons_valid.2.2.1, pairwiseComparisons_valid.2.2.2.2.2⟩,
    triangleHolonomy_fixture.2.1⟩

def alternateComparison₀₁ : FlagComparison := !![0, 1; 1, 1]

/-- Existence of a flag comparison does not select a unique comparison cell. -/
theorem flagComparison_is_nonunique :
    comparison₀₁ ≠ alternateComparison₀₁ ∧
      InvertibleComparison comparison₀₁ ∧
      InvertibleComparison alternateComparison₀₁ ∧
      carriesFlag comparison₀₁ flag₀ flag₁ ∧
      carriesFlag alternateComparison₀₁ flag₀ flag₁ := by
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · intro h
    have h11 := congrArg (fun matrix : FlagComparison => matrix 1 1) h
    norm_num [comparison₀₁, alternateComparison₀₁] at h11
  · norm_num [InvertibleComparison, comparison₀₁, Matrix.det_fin_two]
  · norm_num [InvertibleComparison, alternateComparison₀₁, Matrix.det_fin_two]
  all_goals
    funext i
    fin_cases i <;>
      norm_num [carriesFlag, comparison₀₁, alternateComparison₀₁,
        flag₀, flag₁, Matrix.mulVec, dotProduct]

end MariciFormal
