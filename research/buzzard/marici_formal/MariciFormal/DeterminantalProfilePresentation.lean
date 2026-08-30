import MariciFormal.TwoByTwoDeterminantalProfile

/-!
The complete two-stage determinantal profile of a two-by-two matrix is
invariant under explicitly reversible row and column changes.
-/

namespace MariciFormal

variable {R : Type*} [CommRing R]

theorem secondDeterminantalIdeal_left_mul_le
    (left matrix : Matrix (Fin 2) (Fin 2) R) :
    secondDeterminantalIdeal (left * matrix) ≤
      secondDeterminantalIdeal matrix := by
  rw [secondDeterminantalIdeal, Ideal.span_le]
  intro polynomial hpolynomial
  simp only [Set.mem_singleton_iff] at hpolynomial
  subst polynomial
  change (left * matrix).det ∈ Ideal.span ({matrix.det} : Set R)
  rw [Ideal.mem_span_singleton, Matrix.det_mul]
  exact dvd_mul_left _ _

theorem secondDeterminantalIdeal_right_mul_le
    (matrix right : Matrix (Fin 2) (Fin 2) R) :
    secondDeterminantalIdeal (matrix * right) ≤
      secondDeterminantalIdeal matrix := by
  rw [secondDeterminantalIdeal, Ideal.span_le]
  intro polynomial hpolynomial
  simp only [Set.mem_singleton_iff] at hpolynomial
  subst polynomial
  change (matrix * right).det ∈ Ideal.span ({matrix.det} : Set R)
  rw [Ideal.mem_span_singleton, Matrix.det_mul]
  exact dvd_mul_right _ _

theorem secondDeterminantalIdeal_left_equivalence
    (left leftInv matrix : Matrix (Fin 2) (Fin 2) R)
    (hInv : leftInv * left = 1) :
    secondDeterminantalIdeal (left * matrix) =
      secondDeterminantalIdeal matrix := by
  apply le_antisymm
  · exact secondDeterminantalIdeal_left_mul_le left matrix
  · have hmatrix : leftInv * (left * matrix) = matrix := by
      rw [← Matrix.mul_assoc, hInv, Matrix.one_mul]
    calc
      secondDeterminantalIdeal matrix =
          secondDeterminantalIdeal (leftInv * (left * matrix)) :=
        congrArg _ hmatrix.symm
      _ ≤ secondDeterminantalIdeal (left * matrix) :=
        secondDeterminantalIdeal_left_mul_le leftInv (left * matrix)

theorem secondDeterminantalIdeal_right_equivalence
    (right rightInv matrix : Matrix (Fin 2) (Fin 2) R)
    (hInv : right * rightInv = 1) :
    secondDeterminantalIdeal (matrix * right) =
      secondDeterminantalIdeal matrix := by
  apply le_antisymm
  · exact secondDeterminantalIdeal_right_mul_le matrix right
  · have hmatrix : (matrix * right) * rightInv = matrix := by
      rw [Matrix.mul_assoc, hInv, Matrix.mul_one]
    calc
      secondDeterminantalIdeal matrix =
          secondDeterminantalIdeal ((matrix * right) * rightInv) :=
        congrArg _ hmatrix.symm
      _ ≤ secondDeterminantalIdeal (matrix * right) :=
        secondDeterminantalIdeal_right_mul_le (matrix * right) rightInv

theorem secondDeterminantalIdeal_two_sided_equivalence
    (left leftInv right rightInv matrix : Matrix (Fin 2) (Fin 2) R)
    (hLeft : leftInv * left = 1) (hRight : right * rightInv = 1) :
    secondDeterminantalIdeal (left * matrix * right) =
      secondDeterminantalIdeal matrix := by
  rw [secondDeterminantalIdeal_right_equivalence right rightInv
    (left * matrix) hRight]
  exact secondDeterminantalIdeal_left_equivalence left leftInv matrix hLeft

/-- Both stages of the determinantal profile survive an explicitly reversible
two-sided presentation change. -/
theorem twoByTwoDeterminantalProfile_two_sided_equivalence
    (left leftInv right rightInv matrix : Matrix (Fin 2) (Fin 2) R)
    (hLeft : leftInv * left = 1) (hRight : right * rightInv = 1) :
    twoByTwoDeterminantalProfile (left * matrix * right) =
      twoByTwoDeterminantalProfile matrix := by
  unfold twoByTwoDeterminantalProfile
  congr 1
  · exact matrixEntryIdeal_two_sided_equivalence left leftInv right rightInv
      matrix hLeft hRight
  · exact secondDeterminantalIdeal_two_sided_equivalence left leftInv right
      rightInv matrix hLeft hRight

end MariciFormal
