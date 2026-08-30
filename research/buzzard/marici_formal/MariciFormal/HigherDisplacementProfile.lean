import Mathlib

/-!
The first displacement rank does not classify four-dimensional unipotent
holonomy. Higher powers distinguish Jordan types `(3,1)` and `(2,2)`.
-/

namespace MariciFormal

abbrev HolonomyVector₄ := Fin 4 → Rat

/-- Nilpotent displacement with Jordan type `(3,1)`. -/
def displacement₃₁ (x : HolonomyVector₄) : HolonomyVector₄ :=
  ![x 1, x 2, 0, 0]

/-- Nilpotent displacement with Jordan type `(2,2)`. -/
def displacement₂₂ (x : HolonomyVector₄) : HolonomyVector₄ :=
  ![x 1, 0, x 3, 0]

def secondDisplacement
    (displacement : HolonomyVector₄ → HolonomyVector₄) (x : HolonomyVector₄) :
    HolonomyVector₄ :=
  displacement (displacement x)

def thirdDisplacement
    (displacement : HolonomyVector₄ → HolonomyVector₄) (x : HolonomyVector₄) :
    HolonomyVector₄ :=
  displacement (secondDisplacement displacement x)

theorem displacement₃₁_range_iff (output : HolonomyVector₄) :
    (∃ input, displacement₃₁ input = output) ↔
      ∃ a b : Rat, output = ![a, b, 0, 0] := by
  constructor
  · rintro ⟨input, rfl⟩
    exact ⟨input 1, input 2, rfl⟩
  · rintro ⟨a, b, rfl⟩
    exact ⟨![0, a, b, 0], rfl⟩

theorem displacement₂₂_range_iff (output : HolonomyVector₄) :
    (∃ input, displacement₂₂ input = output) ↔
      ∃ a b : Rat, output = ![a, 0, b, 0] := by
  constructor
  · rintro ⟨input, rfl⟩
    exact ⟨input 1, input 3, rfl⟩
  · rintro ⟨a, b, rfl⟩
    exact ⟨![0, a, 0, b], rfl⟩

theorem displacement₃₁_square_formula (x : HolonomyVector₄) :
    secondDisplacement displacement₃₁ x = ![x 2, 0, 0, 0] := by
  rfl

theorem displacement₂₂_square_zero (x : HolonomyVector₄) :
    secondDisplacement displacement₂₂ x = 0 := by
  funext i
  fin_cases i <;> rfl

theorem displacement₃₁_cube_zero (x : HolonomyVector₄) :
    thirdDisplacement displacement₃₁ x = 0 := by
  funext i
  fin_cases i <;> rfl

theorem displacement₂₂_cube_zero (x : HolonomyVector₄) :
    thirdDisplacement displacement₂₂ x = 0 := by
  rw [thirdDisplacement, displacement₂₂_square_zero]
  funext i
  fin_cases i <;> rfl

def squareDisplacementWitness : HolonomyVector₄ := ![0, 0, 1, 0]

theorem equalFirstRank_differentHigherProfile :
    (∃ first second : HolonomyVector₄,
      displacement₃₁ first ≠ 0 ∧ displacement₃₁ second ≠ 0 ∧
      displacement₂₂ first ≠ 0 ∧ displacement₂₂ second ≠ 0) ∧
      secondDisplacement displacement₃₁ squareDisplacementWitness ≠ 0 ∧
      secondDisplacement displacement₂₂ squareDisplacementWitness = 0 ∧
      (∀ x, thirdDisplacement displacement₃₁ x = 0) ∧
      (∀ x, thirdDisplacement displacement₂₂ x = 0) := by
  refine ⟨?_, ?_, displacement₂₂_square_zero _,
    displacement₃₁_cube_zero, displacement₂₂_cube_zero⟩
  · refine ⟨![0, 1, 0, 0], ![0, 0, 1, 1], ?_, ?_, ?_, ?_⟩
    · intro h
      have h0 := congrFun h 0
      norm_num [displacement₃₁] at h0
    · intro h
      have h1 := congrFun h 1
      change (1 : Rat) = 0 at h1
      norm_num at h1
    · intro h
      have h0 := congrFun h 0
      norm_num [displacement₂₂] at h0
    · intro h
      have h2 := congrFun h 2
      change (1 : Rat) = 0 at h2
      norm_num at h2
  · rw [displacement₃₁_square_formula]
    intro h
    have h0 := congrFun h 0
    change (1 : Rat) = 0 at h0
    norm_num at h0

end MariciFormal
