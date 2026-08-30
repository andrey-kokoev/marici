import Mathlib

/-!
The finite boundary-current cokernel fixture: scalar aggregation can vanish
while the forcing residual remains nonexact relative to the authorized image.
-/

namespace MariciFormal

abbrev BoundaryDensity := Fin 3 → Rat

def authorizedCurrentDirection : BoundaryDensity := ![1, -1, 0]

def forcingResidual : BoundaryDensity := ![1, 0, -1]

/-- The authorized derivative image is the line spanned by `(1,-1,0)`. -/
def boundaryDerivative : Rat →ₗ[Rat] BoundaryDensity where
  toFun t := fun i => t * authorizedCurrentDirection i
  map_add' x y := by
    ext i
    simp
    ring
  map_smul' a x := by
    ext i
    simp
    ring

def scalarAggregate : BoundaryDensity →ₗ[Rat] Rat where
  toFun density := ∑ i, density i
  map_add' x y := by
    simp only [Pi.add_apply, Finset.sum_add_distrib]
  map_smul' a x := by
    simp only [Pi.smul_apply, smul_eq_mul, RingHom.id_apply, Finset.mul_sum]

theorem authorizedCurrent_scalarAggregate_zero :
    scalarAggregate authorizedCurrentDirection = 0 := by
  have h2 : authorizedCurrentDirection (2 : Fin 3) = 0 := by native_decide
  change (∑ i, authorizedCurrentDirection i) = 0
  rw [Fin.sum_univ_three, h2]
  norm_num [authorizedCurrentDirection]

theorem forcingResidual_scalarAggregate_zero :
    scalarAggregate forcingResidual = 0 := by
  have h2 : forcingResidual (2 : Fin 3) = -1 := by native_decide
  change (∑ i, forcingResidual i) = 0
  rw [Fin.sum_univ_three, h2]
  norm_num [forcingResidual]

/-- Equal zero scalar bytes do not place the residual in the authorized image. -/
theorem forcingResidual_not_mem_boundaryDerivative_range :
    forcingResidual ∉ LinearMap.range boundaryDerivative := by
  rintro ⟨t, ht⟩
  have h0 := congrFun ht 0
  have h1 := congrFun ht 1
  norm_num [boundaryDerivative, authorizedCurrentDirection, forcingResidual] at h0 h1
  linarith

abbrev BoundaryCokernel :=
  BoundaryDensity ⧸ LinearMap.range boundaryDerivative

def forcingCokernelClass : BoundaryCokernel :=
  Submodule.Quotient.mk forcingResidual

/-- The forcing residual represents a nonzero boundary-current cokernel class. -/
theorem forcingCokernelClass_ne_zero : forcingCokernelClass ≠ 0 := by
  intro hzero
  apply forcingResidual_not_mem_boundaryDerivative_range
  exact (Submodule.Quotient.mk_eq_zero _).mp hzero

/-- Vanishing aggregate is strictly weaker than vanishing cokernel class. -/
theorem scalarVanishing_does_not_imply_boundaryExactness :
    scalarAggregate forcingResidual = 0 ∧ forcingCokernelClass ≠ 0 :=
  ⟨forcingResidual_scalarAggregate_zero, forcingCokernelClass_ne_zero⟩

end MariciFormal
