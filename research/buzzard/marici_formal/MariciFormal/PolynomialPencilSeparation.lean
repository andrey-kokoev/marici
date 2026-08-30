import Mathlib

/-!
Equal characteristic polynomials do not classify rational holonomy. The
polynomial pencil's lower determinantal data separates identity from a
nontrivial unipotent.
-/

namespace MariciFormal

open Polynomial

abbrev RationalHolonomy₂ := Matrix (Fin 2) (Fin 2) Rat
abbrev PolynomialPencil₂ := Matrix (Fin 2) (Fin 2) Rat[X]

def identityRationalHolonomy : RationalHolonomy₂ := 1

def unipotentRationalHolonomy : RationalHolonomy₂ := !![1, 1; 0, 1]

noncomputable def pencilOf (holonomy : RationalHolonomy₂) : PolynomialPencil₂ :=
  fun i j => if i = j then X - C (holonomy i j) else -C (holonomy i j)

noncomputable def eigenvalueOneFactor : Rat[X] := X - 1

theorem holonomyMatrices_distinct :
    identityRationalHolonomy ≠ unipotentRationalHolonomy := by
  intro h
  have h01 := congrArg (fun matrix : RationalHolonomy₂ => matrix 0 1) h
  norm_num [identityRationalHolonomy, unipotentRationalHolonomy] at h01

theorem pencilDeterminants_agree :
    (pencilOf identityRationalHolonomy).det = eigenvalueOneFactor ^ 2 ∧
      (pencilOf unipotentRationalHolonomy).det = eigenvalueOneFactor ^ 2 := by
  constructor <;>
    rw [Matrix.det_fin_two] <;>
    simp [pencilOf, identityRationalHolonomy, unipotentRationalHolonomy,
      eigenvalueOneFactor] <;>
    ring

theorem eigenvalueOneFactor_nonunit : ¬ IsUnit eigenvalueOneFactor := by
  simpa [eigenvalueOneFactor, sub_eq_add_neg] using
    (Polynomial.not_isUnit_X_add_C (-1 : Rat))

/-- Every first minor of the identity pencil has the common nonunit divisor. -/
theorem identityPencil_entries_divisible (i j : Fin 2) :
    eigenvalueOneFactor ∣ pencilOf identityRationalHolonomy i j := by
  fin_cases i <;> fin_cases j <;>
    simp [pencilOf, identityRationalHolonomy, eigenvalueOneFactor]

/-- The unipotent pencil contains the unit first minor `-1`. -/
theorem unipotentPencil_hasUnitMinor :
    IsUnit (pencilOf unipotentRationalHolonomy 0 1) := by
  norm_num [pencilOf, unipotentRationalHolonomy]

/-- The top determinant port collides while the first-minor ideals differ. -/
theorem characteristicPolynomial_not_complete :
    identityRationalHolonomy ≠ unipotentRationalHolonomy ∧
      (pencilOf identityRationalHolonomy).det =
        (pencilOf unipotentRationalHolonomy).det ∧
      (∀ i j, eigenvalueOneFactor ∣
        pencilOf identityRationalHolonomy i j) ∧
      ¬ IsUnit eigenvalueOneFactor ∧
      IsUnit (pencilOf unipotentRationalHolonomy 0 1) := by
  exact ⟨holonomyMatrices_distinct,
    pencilDeterminants_agree.1.trans pencilDeterminants_agree.2.symm,
    identityPencil_entries_divisible, eigenvalueOneFactor_nonunit,
    unipotentPencil_hasUnitMinor⟩

end MariciFormal
