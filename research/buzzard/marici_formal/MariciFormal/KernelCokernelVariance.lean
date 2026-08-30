import Mathlib

/-!
Equal-dimensional kernel and adjoint-kernel defects retain opposite variance;
a nonzero Green residual records rather than repairs the mismatch.
-/

namespace MariciFormal

abbrev VarianceChannel := Fin 2 → Rat

/-- The observation matrix `[[1,1],[0,0]]`. -/
def observationMap (x : VarianceChannel) : VarianceChannel :=
  ![x 0 + x 1, 0]

/-- The transpose/adjoint matrix `[[1,0],[1,0]]`. -/
def adjointObservationMap (x : VarianceChannel) : VarianceChannel :=
  ![x 0, x 0]

theorem observationMap_kernel_iff (x : VarianceChannel) :
    observationMap x = 0 ↔ x 0 + x 1 = 0 := by
  constructor
  · intro h
    have h0 := congrFun h 0
    simpa [observationMap] using h0
  · intro h
    funext i
    fin_cases i <;> simp [observationMap, h]

theorem adjointObservationMap_kernel_iff (x : VarianceChannel) :
    adjointObservationMap x = 0 ↔ x 0 = 0 := by
  constructor
  · intro h
    have h0 := congrFun h 0
    simpa [adjointObservationMap] using h0
  · intro h
    funext i
    fin_cases i <;> simp [adjointObservationMap, h]

def ordinaryKernelWitness : VarianceChannel := ![-1, 1]

def adjointKernelWitness : VarianceChannel := ![0, 1]

theorem kernelLines_are_distinct :
    ordinaryKernelWitness ≠ 0 ∧
      adjointKernelWitness ≠ 0 ∧
      observationMap ordinaryKernelWitness = 0 ∧
      adjointObservationMap adjointKernelWitness = 0 ∧
      observationMap adjointKernelWitness ≠ 0 ∧
      adjointObservationMap ordinaryKernelWitness ≠ 0 := by
  native_decide

/-- Every ordinary-kernel vector has the form `(-t,t)`. -/
theorem observationKernel_parameterized (x : VarianceChannel) :
    observationMap x = 0 ↔ ∃ t : Rat, x = ![-t, t] := by
  rw [observationMap_kernel_iff]
  constructor
  · intro h
    refine ⟨x 1, ?_⟩
    funext i
    fin_cases i
    · dsimp
      linarith
    · rfl
  · rintro ⟨t, rfl⟩
    norm_num

/-- Every adjoint-kernel vector has the form `(0,t)`. -/
theorem adjointKernel_parameterized (x : VarianceChannel) :
    adjointObservationMap x = 0 ↔ ∃ t : Rat, x = ![0, t] := by
  rw [adjointObservationMap_kernel_iff]
  constructor
  · intro h
    refine ⟨x 1, ?_⟩
    funext i
    fin_cases i
    · exact h
    · rfl
  · rintro ⟨t, rfl⟩
    rfl

/-- With identity pairings, `M - Mᵀ` is the Green residual. -/
def greenResidual (x : VarianceChannel) : VarianceChannel :=
  observationMap x - adjointObservationMap x

theorem greenResidual_formula (x : VarianceChannel) :
    greenResidual x = ![x 1, -x 0] := by
  funext i
  fin_cases i <;> simp [greenResidual, observationMap, adjointObservationMap]

theorem retainedResidual_does_not_restoreAdjointness :
    greenResidual ordinaryKernelWitness ≠ 0 ∧
      observationMap ≠ adjointObservationMap := by
  constructor
  · native_decide
  · intro h
    have hAt := congrFun h ordinaryKernelWitness
    have hResidual : greenResidual ordinaryKernelWitness = 0 := by
      simp [greenResidual, hAt]
    exact (by native_decide : greenResidual ordinaryKernelWitness ≠ 0) hResidual

end MariciFormal
