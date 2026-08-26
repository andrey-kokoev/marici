import Mathlib

/-!
The exact two-dimensional local residue/Krein hostile for a hypothetical
double zero.  It is a model of `K[t]/(t^2)`, not an assertion that Xi has a
multiple zero.
-/

namespace MariciFormal

def doubleZeroResidueMetric : Matrix (Fin 2) (Fin 2) Rat :=
  !![0, 1; 1, 0]

def doubleZeroJordanCoordinate (lambda : Rat) : Matrix (Fin 2) (Fin 2) Rat :=
  !![lambda, 0; 1, lambda]

def residueQuadratic (v : Fin 2 → Rat) : Rat :=
  dotProduct v (doubleZeroResidueMetric *ᵥ v)

def socleVector : Fin 2 → Rat := ![0, 1]
def positiveResidueVector : Fin 2 → Rat := ![1, 1]
def negativeResidueVector : Fin 2 → Rat := ![1, -1]

theorem doubleZeroResidue_socle_nonzero_isotropic :
    socleVector ≠ 0 ∧ residueQuadratic socleVector = 0 := by
  constructor
  · intro h
    have h1 := congrFun h 1
    norm_num [socleVector] at h1
  · norm_num [residueQuadratic, socleVector, doubleZeroResidueMetric,
      Matrix.mulVec, dotProduct, Fin.sum_univ_two]

theorem doubleZeroResidue_indefinite :
    0 < residueQuadratic positiveResidueVector ∧
      residueQuadratic negativeResidueVector < 0 := by
  norm_num [residueQuadratic, positiveResidueVector, negativeResidueVector,
    doubleZeroResidueMetric, Matrix.mulVec, dotProduct, Fin.sum_univ_two]

/-- Jordan multiplication is self-adjoint for the residue metric even though
it is not diagonalized by that local algebra. -/
theorem doubleZeroJordan_metric_selfadjoint (lambda : Rat) :
    (doubleZeroJordanCoordinate lambda)ᵀ * doubleZeroResidueMetric =
      doubleZeroResidueMetric * doubleZeroJordanCoordinate lambda := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    norm_num [doubleZeroJordanCoordinate, doubleZeroResidueMetric,
      Matrix.mul_apply, Fin.sum_univ_two]

end MariciFormal
