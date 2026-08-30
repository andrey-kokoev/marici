import Mathlib

/-!
Multiplicity-two parity sectors require three polarized probes per symmetric
pairing block.
-/

namespace MariciFormal

abbrev MultiplicityVector := Fin 2 → Rat

/-- Coefficients `(j11, j22, j12)` of a symmetric two-dimensional block. -/
abbrev SymmetricBlock := Rat × Rat × Rat

def blockEnergy (j : SymmetricBlock) (x : MultiplicityVector) : Rat :=
  j.1 * x 0 ^ 2 + j.2.1 * x 1 ^ 2 + 2 * j.2.2 * x 0 * x 1

def basisProbe₁ : MultiplicityVector := ![1, 0]

def basisProbe₂ : MultiplicityVector := ![0, 1]

def mixedProbe : MultiplicityVector := ![1, 1]

def polarizedObservation (j : SymmetricBlock) : Rat × Rat × Rat :=
  (blockEnergy j basisProbe₁, blockEnergy j basisProbe₂,
    blockEnergy j mixedProbe)

theorem polarizedObservation_formula (j : SymmetricBlock) :
    polarizedObservation j = (j.1, j.2.1, j.1 + j.2.1 + 2 * j.2.2) := by
  simp [polarizedObservation, blockEnergy, basisProbe₁, basisProbe₂, mixedProbe]

def reconstructBlock (energies : Rat × Rat × Rat) : SymmetricBlock :=
  (energies.1, energies.2.1,
    (energies.2.2 - energies.1 - energies.2.1) / 2)

theorem reconstructBlock_polarizedObservation (j : SymmetricBlock) :
    reconstructBlock (polarizedObservation j) = j := by
  rcases j with ⟨j11, j22, j12⟩
  rw [polarizedObservation_formula]
  simp [reconstructBlock]
  ring

theorem polarizedObservation_injective :
    Function.Injective polarizedObservation := by
  intro j k h
  rw [← reconstructBlock_polarizedObservation j,
    ← reconstructBlock_polarizedObservation k, h]

/-- The invariant four-channel parameters are one symmetric block per parity. -/
abbrev MultiplicityPairing := SymmetricBlock × SymmetricBlock

def sixPolarizedObservations (j : MultiplicityPairing) :
    (Rat × Rat × Rat) × (Rat × Rat × Rat) :=
  (polarizedObservation j.1, polarizedObservation j.2)

theorem sixPolarizedObservations_injective :
    Function.Injective sixPolarizedObservations := by
  intro j k h
  apply Prod.ext
  · apply polarizedObservation_injective
    exact congrArg Prod.fst h
  · apply polarizedObservation_injective
    exact congrArg Prod.snd h

/-- Five retained probes omit the mixed probe in the even block. -/
def fiveProbeObservation (j : MultiplicityPairing) :
    (Rat × Rat) × (Rat × Rat × Rat) :=
  ((blockEnergy j.1 basisProbe₁, blockEnergy j.1 basisProbe₂),
    polarizedObservation j.2)

def diagonalEvenBlock : SymmetricBlock := (2, 3, 0)

def coupledEvenBlock : SymmetricBlock := (2, 3, 1)

def fixedOddBlock : SymmetricBlock := (4, 2, -1)

def diagonalMultiplicityPairing : MultiplicityPairing :=
  (diagonalEvenBlock, fixedOddBlock)

def coupledMultiplicityPairing : MultiplicityPairing :=
  (coupledEvenBlock, fixedOddBlock)

def PositiveDefiniteBlock (j : SymmetricBlock) : Prop :=
  ∀ x, x ≠ 0 → 0 < blockEnergy j x

theorem diagonalEvenBlock_positiveDefinite :
    PositiveDefiniteBlock diagonalEvenBlock := by
  intro x hx
  unfold diagonalEvenBlock blockEnergy
  by_cases h0 : x 0 = 0
  · have h1 : x 1 ≠ 0 := by
      intro h1
      apply hx
      funext i
      fin_cases i <;> assumption
    nlinarith [sq_pos_of_ne_zero h1]
  · nlinarith [sq_pos_of_ne_zero h0, sq_nonneg (x 1)]

theorem coupledEvenBlock_positiveDefinite :
    PositiveDefiniteBlock coupledEvenBlock := by
  intro x hx
  unfold coupledEvenBlock blockEnergy
  norm_num only [Prod.fst, Prod.snd]
  have decomposition :
      2 * x 0 ^ 2 + 3 * x 1 ^ 2 + 2 * x 0 * x 1 =
        x 0 ^ 2 + (x 0 + x 1) ^ 2 + 2 * x 1 ^ 2 := by ring
  rw [decomposition]
  by_cases h0 : x 0 = 0
  · have h1 : x 1 ≠ 0 := by
      intro h1
      apply hx
      funext i
      fin_cases i <;> assumption
    nlinarith [sq_pos_of_ne_zero h1, sq_nonneg (x 0 + x 1)]
  · nlinarith [sq_pos_of_ne_zero h0, sq_nonneg (x 1),
      sq_nonneg (x 0 + x 1)]

/-- Positive alternatives agree on five probes but differ on the omitted one. -/
theorem fiveProbes_are_not_faithful :
    PositiveDefiniteBlock diagonalEvenBlock ∧
      PositiveDefiniteBlock coupledEvenBlock ∧
      diagonalMultiplicityPairing ≠ coupledMultiplicityPairing ∧
      fiveProbeObservation diagonalMultiplicityPairing =
        fiveProbeObservation coupledMultiplicityPairing ∧
      blockEnergy diagonalEvenBlock mixedProbe ≠
        blockEnergy coupledEvenBlock mixedProbe := by
  refine ⟨diagonalEvenBlock_positiveDefinite,
    coupledEvenBlock_positiveDefinite, ?_, ?_, ?_⟩
  · norm_num [diagonalMultiplicityPairing, coupledMultiplicityPairing,
      diagonalEvenBlock, coupledEvenBlock]
  · norm_num [fiveProbeObservation, diagonalMultiplicityPairing,
      coupledMultiplicityPairing, diagonalEvenBlock, coupledEvenBlock,
      fixedOddBlock, polarizedObservation, blockEnergy, basisProbe₁,
      basisProbe₂, mixedProbe]
  · norm_num [diagonalEvenBlock, coupledEvenBlock, blockEnergy, mixedProbe]

theorem finitePolarizationFixtures :
    reconstructBlock (2, 3, 7) = (2, 3, 1) ∧
      reconstructBlock (4, 2, 4) = (4, 2, -1) := by
  norm_num [reconstructBlock]

end MariciFormal
