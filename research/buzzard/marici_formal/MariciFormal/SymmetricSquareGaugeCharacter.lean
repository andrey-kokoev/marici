import Mathlib

/-!
The observability determinant is a relative invariant under parity-sector
chart changes: its zero locus is intrinsic, while its scalar value and sign
need not be.
-/

namespace MariciFormal

/-- Symmetric-square action in the basis `(x², y², 2xy)`. -/
def symmetricSquareRepresentation (a b c d : Rat) : Matrix (Fin 3) (Fin 3) Rat :=
  ![![a ^ 2, b ^ 2, 2 * a * b],
    ![c ^ 2, d ^ 2, 2 * c * d],
    ![a * c, b * d, a * d + b * c]]

theorem det_symmetricSquareRepresentation (a b c d : Rat) :
    (symmetricSquareRepresentation a b c d).det = (a * d - b * c) ^ 3 := by
  rw [Matrix.det_fin_three]
  simp [symmetricSquareRepresentation]
  ring

def twoByTwoDeterminant (a b c d : Rat) : Rat := a * d - b * c

def pairedGaugeCharacter
    (aPlus bPlus cPlus dPlus aMinus bMinus cMinus dMinus : Rat) : Rat :=
  twoByTwoDeterminant aPlus bPlus cPlus dPlus ^ 3 *
    twoByTwoDeterminant aMinus bMinus cMinus dMinus ^ 3

def transportDesignDeterminant (character determinant : Rat) : Rat :=
  character * determinant

theorem gaugeTransport_preserves_nonvanishing
    {character determinant : Rat}
    (hCharacter : character ≠ 0) (hDeterminant : determinant ≠ 0) :
    transportDesignDeterminant character determinant ≠ 0 := by
  simp [transportDesignDeterminant, hCharacter, hDeterminant]

theorem positiveDeterminantFixture :
    pairedGaugeCharacter 6 0 0 1 35 0 0 1 = 9261000 ∧
      transportDesignDeterminant 9261000 4 = 37044000 := by
  norm_num [pairedGaugeCharacter, twoByTwoDeterminant,
    transportDesignDeterminant]

/-- An orientation-reversing chart preserves nonvanishing but reverses sign. -/
theorem orientationReversalFixture :
    pairedGaugeCharacter (-1) 0 0 1 1 0 0 1 = -1 ∧
      transportDesignDeterminant (-1) 4 = -4 ∧
      transportDesignDeterminant (-1) 4 ≠ 0 := by
  norm_num [pairedGaugeCharacter, twoByTwoDeterminant,
    transportDesignDeterminant]

/-- Nonvanishing is transportable without promoting coordinate positivity. -/
theorem nonvanishing_does_not_imply_chartIndependentPositivity :
    ∃ character determinant : Rat,
      character ≠ 0 ∧ determinant > 0 ∧
      transportDesignDeterminant character determinant ≠ 0 ∧
      transportDesignDeterminant character determinant < 0 := by
  exact ⟨-1, 4, by norm_num, by norm_num, by norm_num [transportDesignDeterminant],
    by norm_num [transportDesignDeterminant]⟩

end MariciFormal
