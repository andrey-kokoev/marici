import Mathlib

/-!
Trace and determinant are not jointly faithful holonomy probes. A nontrivial
unipotent has the same scalar characters as identity but nonzero rank-one
displacement.
-/

namespace MariciFormal

abbrev HolonomyMatrix₂ := Matrix (Fin 2) (Fin 2) Rat
abbrev HolonomyVector₂ := Fin 2 → Rat

def matrixTrace₂ (matrix : HolonomyMatrix₂) : Rat := matrix 0 0 + matrix 1 1

def identityHolonomy : HolonomyMatrix₂ := 1

def unipotentHolonomy : HolonomyMatrix₂ := !![1, 1; 0, 1]

def scalarHolonomyPorts (matrix : HolonomyMatrix₂) : Rat × Rat :=
  (matrixTrace₂ matrix, matrix.det)

theorem scalarHolonomyPorts_blindFixture :
    identityHolonomy ≠ unipotentHolonomy ∧
      scalarHolonomyPorts identityHolonomy = (2, 1) ∧
      scalarHolonomyPorts unipotentHolonomy = (2, 1) := by
  refine ⟨?_, ?_, ?_⟩
  · intro h
    have h01 := congrArg (fun matrix : HolonomyMatrix₂ => matrix 0 1) h
    norm_num [identityHolonomy, unipotentHolonomy] at h01
  · norm_num [scalarHolonomyPorts, matrixTrace₂, identityHolonomy,
      Matrix.det_fin_two]
  · norm_num [scalarHolonomyPorts, matrixTrace₂, unipotentHolonomy,
      Matrix.det_fin_two]

def holonomyDisplacement
    (matrix : HolonomyMatrix₂) (vector : HolonomyVector₂) : HolonomyVector₂ :=
  matrix.mulVec vector - vector

theorem identityDisplacement_zero (vector : HolonomyVector₂) :
    holonomyDisplacement identityHolonomy vector = 0 := by
  funext i
  fin_cases i <;>
    simp [holonomyDisplacement, identityHolonomy]

theorem unipotentDisplacement_formula (vector : HolonomyVector₂) :
    holonomyDisplacement unipotentHolonomy vector = ![vector 1, 0] := by
  funext i
  fin_cases i <;>
    simp [holonomyDisplacement, unipotentHolonomy, dotProduct]

def FirstCoordinateLine (vector : HolonomyVector₂) : Prop :=
  ∃ scalar : Rat, vector = ![scalar, 0]

/-- The unipotent displacement image is exactly one nonzero coordinate line. -/
theorem unipotentDisplacement_range_iff (output : HolonomyVector₂) :
    (∃ input, holonomyDisplacement unipotentHolonomy input = output) ↔
      FirstCoordinateLine output := by
  constructor
  · rintro ⟨input, rfl⟩
    exact ⟨input 1, unipotentDisplacement_formula input⟩
  · rintro ⟨scalar, rfl⟩
    refine ⟨![0, scalar], ?_⟩
    rw [unipotentDisplacement_formula]
    rfl

theorem unipotentDisplacement_nonzero :
    holonomyDisplacement unipotentHolonomy ![0, 1] ≠ 0 := by
  rw [unipotentDisplacement_formula]
  intro h
  have h0 := congrFun h 0
  norm_num at h0

/-- Central scalar ports fail faithfulness on the two-element fixture. -/
theorem traceAndDeterminant_are_not_jointlyFaithful :
    ∃ first second : HolonomyMatrix₂,
      first ≠ second ∧ scalarHolonomyPorts first = scalarHolonomyPorts second := by
  exact ⟨identityHolonomy, unipotentHolonomy,
    scalarHolonomyPorts_blindFixture.1,
    scalarHolonomyPorts_blindFixture.2.1.trans
      scalarHolonomyPorts_blindFixture.2.2.symm⟩

end MariciFormal
