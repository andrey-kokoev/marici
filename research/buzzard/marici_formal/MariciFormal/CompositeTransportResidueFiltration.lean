import Mathlib

/-!
Successive codomain transport defects form a filtration. The final excess
kernel is intrinsic to the composite, while its intermediate flag depends on
the chosen factorization.
-/

namespace MariciFormal

abbrev ResidueSpace₃ := Fin 3 → Rat

def killFirstCoordinate (x : ResidueSpace₃) : ResidueSpace₃ := ![0, x 1, x 2]

def killSecondCoordinate (x : ResidueSpace₃) : ResidueSpace₃ := ![x 0, 0, x 2]

def firstThenSecond (x : ResidueSpace₃) : ResidueSpace₃ :=
  killSecondCoordinate (killFirstCoordinate x)

def secondThenFirst (x : ResidueSpace₃) : ResidueSpace₃ :=
  killFirstCoordinate (killSecondCoordinate x)

theorem factorizations_have_same_composite : firstThenSecond = secondThenFirst := by
  funext x i
  fin_cases i <;>
    simp [firstThenSecond, secondThenFirst, killFirstCoordinate,
      killSecondCoordinate]

theorem killFirstCoordinate_kernel_iff (x : ResidueSpace₃) :
    killFirstCoordinate x = 0 ↔ x 1 = 0 ∧ x 2 = 0 := by
  constructor
  · intro h
    exact ⟨by simpa [killFirstCoordinate] using congrFun h 1,
      by simpa [killFirstCoordinate] using congrFun h 2⟩
  · rintro ⟨h1, h2⟩
    funext i
    fin_cases i <;> simp [killFirstCoordinate, h1, h2]

theorem killSecondCoordinate_kernel_iff (x : ResidueSpace₃) :
    killSecondCoordinate x = 0 ↔ x 0 = 0 ∧ x 2 = 0 := by
  constructor
  · intro h
    exact ⟨by simpa [killSecondCoordinate] using congrFun h 0,
      by simpa [killSecondCoordinate] using congrFun h 2⟩
  · rintro ⟨h0, h2⟩
    funext i
    fin_cases i <;> simp [killSecondCoordinate, h0, h2]

theorem composite_kernel_iff (x : ResidueSpace₃) :
    firstThenSecond x = 0 ↔ x 2 = 0 := by
  constructor
  · intro h
    simpa [firstThenSecond, killFirstCoordinate, killSecondCoordinate] using
      congrFun h 2
  · intro h2
    funext i
    fin_cases i <;>
      simp [firstThenSecond, killFirstCoordinate, killSecondCoordinate, h2]

def firstResidueDirection : ResidueSpace₃ := ![1, 0, 0]

def secondResidueDirection : ResidueSpace₃ := ![0, 1, 0]

theorem successiveResidueLayers :
    killFirstCoordinate firstResidueDirection = 0 ∧
      killSecondCoordinate firstResidueDirection ≠ 0 ∧
      killFirstCoordinate secondResidueDirection ≠ 0 ∧
      killSecondCoordinate secondResidueDirection = 0 ∧
      firstThenSecond firstResidueDirection = 0 ∧
      firstThenSecond secondResidueDirection = 0 := by
  native_decide

/-- Equal endpoint kernels do not canonically identify intermediate flags. -/
theorem residueFlag_depends_on_factorization :
    firstThenSecond = secondThenFirst ∧
      (∃ x, killFirstCoordinate x = 0 ∧ killSecondCoordinate x ≠ 0) ∧
      (∃ x, killSecondCoordinate x = 0 ∧ killFirstCoordinate x ≠ 0) := by
  exact ⟨factorizations_have_same_composite,
    ⟨firstResidueDirection, successiveResidueLayers.1,
      successiveResidueLayers.2.1⟩,
    ⟨secondResidueDirection, successiveResidueLayers.2.2.2.1,
      successiveResidueLayers.2.2.1⟩⟩

end MariciFormal
