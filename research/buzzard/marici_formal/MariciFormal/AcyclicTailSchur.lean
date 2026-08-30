import Mathlib.Data.Matrix.Notation
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.Tactic

/-!
Finite scalar core of Grothendieck's acyclic-tail Schur self-energy packet.
The infinite determinant-class, domain, and cohomological interfaces are not
assumed here.
-/

namespace MariciFormal

open Matrix

variable {K : Type*} [Field K]

/-- One physical scalar channel coupled to one even auxiliary scalar channel. -/
def scalarCoupledBlock (physical couplingLeft couplingRight auxiliary : K) :
    Matrix (Fin 2) (Fin 2) K :=
  !![physical, couplingLeft; couplingRight, auxiliary]

/-- The finite graded determinant after dividing by the identical odd
auxiliary determinant. -/
def scalarGradedDeterminant
    (physical couplingLeft couplingRight auxiliary : K) : K :=
  (scalarCoupledBlock physical couplingLeft couplingRight auxiliary).det /
    auxiliary

/-- The auxiliary resolvent contribution retained by the physical channel. -/
def scalarSelfEnergy
    (couplingLeft couplingRight auxiliary : K) : K :=
  couplingLeft * auxiliary⁻¹ * couplingRight

theorem scalarCoupledBlock_det
    (physical couplingLeft couplingRight auxiliary : K) :
    (scalarCoupledBlock physical couplingLeft couplingRight auxiliary).det =
      physical * auxiliary - couplingLeft * couplingRight := by
  simp [scalarCoupledBlock, Matrix.det_fin_two]

/-- Exact scalar Schur identity: cancellation of the bare odd auxiliary
determinant leaves the energy-dependent self-energy term. -/
theorem scalarGradedDeterminant_eq_schur
    (physical couplingLeft couplingRight auxiliary : K)
    (hauxiliary : auxiliary ≠ 0) :
    scalarGradedDeterminant physical couplingLeft couplingRight auxiliary =
      physical - scalarSelfEnergy couplingLeft couplingRight auxiliary := by
  rw [scalarGradedDeterminant, scalarCoupledBlock_det]
  field_simp
  ring

/-- With no coupling, identical even and odd auxiliary factors cancel. -/
theorem uncoupled_scalarGradedDeterminant
    (physical auxiliary : K) (hauxiliary : auxiliary ≠ 0) :
    scalarGradedDeterminant physical 0 0 auxiliary = physical := by
  rw [scalarGradedDeterminant_eq_schur physical 0 0 auxiliary hauxiliary]
  simp [scalarSelfEnergy]

/-- Coupling is invisible to the net auxiliary multiplicity but not to the
effective physical scalar. -/
theorem scalarCoupling_defect
    (physical couplingLeft couplingRight auxiliary : K)
    (hauxiliary : auxiliary ≠ 0) :
    scalarGradedDeterminant physical couplingLeft couplingRight auxiliary -
        scalarGradedDeterminant physical 0 0 auxiliary =
      -scalarSelfEnergy couplingLeft couplingRight auxiliary := by
  rw [scalarGradedDeterminant_eq_schur _ _ _ _ hauxiliary,
    uncoupled_scalarGradedDeterminant _ _ hauxiliary]
  ring

/-- Hostile finite model: zero net auxiliary multiplicity does not delete a
nonzero Schur coupling. -/
theorem paired_auxiliary_cancellation_does_not_erase_coupling :
    scalarGradedDeterminant (K := ℚ) 0 1 1 1 = -1 ∧
      scalarGradedDeterminant (K := ℚ) 0 0 0 1 = 0 ∧
      scalarSelfEnergy (K := ℚ) 1 1 1 ≠ 0 := by
  norm_num [scalarGradedDeterminant, scalarCoupledBlock,
    scalarSelfEnergy, Matrix.det_fin_two]

end MariciFormal
