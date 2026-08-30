import MariciFormal.MultiplicityPairingReconstruction

/-!
Port cardinality is not observability rank on the reflection-invariant
symmetric-square parameter space.
-/

namespace MariciFormal

/-- Six nominal ports, with the final odd mixed port replaced by a duplicate. -/
def duplicatedSixPortObservation (j : MultiplicityPairing) :
    (Rat × Rat × Rat) × (Rat × Rat × Rat) :=
  (polarizedObservation j.1,
    (blockEnergy j.2 basisProbe₁, blockEnergy j.2 basisProbe₂,
      blockEnergy j.2 basisProbe₂))

def diagonalOddMultiplicityPairing : MultiplicityPairing :=
  (fixedOddBlock, diagonalEvenBlock)

def coupledOddMultiplicityPairing : MultiplicityPairing :=
  (fixedOddBlock, coupledEvenBlock)

/-- Six outputs do not imply faithfulness when their induced rows are dependent. -/
theorem sixDuplicatedPorts_are_not_faithful :
    diagonalOddMultiplicityPairing ≠ coupledOddMultiplicityPairing ∧
      PositiveDefiniteBlock diagonalOddMultiplicityPairing.2 ∧
      PositiveDefiniteBlock coupledOddMultiplicityPairing.2 ∧
      duplicatedSixPortObservation diagonalOddMultiplicityPairing =
        duplicatedSixPortObservation coupledOddMultiplicityPairing := by
  refine ⟨?_, diagonalEvenBlock_positiveDefinite,
    coupledEvenBlock_positiveDefinite, ?_⟩
  · norm_num [diagonalOddMultiplicityPairing, coupledOddMultiplicityPairing,
      diagonalEvenBlock, coupledEvenBlock]
  · norm_num [duplicatedSixPortObservation, diagonalOddMultiplicityPairing,
      coupledOddMultiplicityPairing, diagonalEvenBlock, coupledEvenBlock,
      fixedOddBlock, polarizedObservation, blockEnergy, basisProbe₁,
      basisProbe₂, mixedProbe]

abbrev ParityMultiplicityChannel := Fin 4 → Rat

/-- Reflection fixes the even coordinates and negates the odd coordinates. -/
def parityReflection (v : ParityMultiplicityChannel) :
    ParityMultiplicityChannel :=
  ![v 0, v 1, -v 2, -v 3]

/-- Restricted symmetric-square row in the two parity multiplicity blocks. -/
def invariantSymmetricSquareRow (v : ParityMultiplicityChannel) : Fin 6 → Rat :=
  ![v 0 ^ 2, v 1 ^ 2, 2 * v 0 * v 1,
    v 2 ^ 2, v 3 ^ 2, 2 * v 2 * v 3]

/-- Closing a probe under reflection creates no new invariant observation row. -/
theorem reflectionOrbit_has_same_invariantRow
    (v : ParityMultiplicityChannel) :
    invariantSymmetricSquareRow (parityReflection v) =
      invariantSymmetricSquareRow v := by
  funext i
  fin_cases i <;>
    simp [invariantSymmetricSquareRow, parityReflection]

def reflectionOrbitFixture : ParityMultiplicityChannel := ![1, 2, 3, 4]

theorem reflectionOrbitFixture_row :
    invariantSymmetricSquareRow reflectionOrbitFixture = ![1, 4, 4, 9, 16, 24] ∧
      invariantSymmetricSquareRow (parityReflection reflectionOrbitFixture) =
        ![1, 4, 4, 9, 16, 24] := by
  native_decide

end MariciFormal
