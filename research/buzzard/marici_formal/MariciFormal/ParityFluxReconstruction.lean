import MariciFormal.ReflectionPairingAmbiguity

/-!
Two parity-sector fluxes are necessary and sufficient to reconstruct a
two-channel reflection-invariant pairing.
-/

namespace MariciFormal

def evenParityChannel : ReflectionChannel := ![1, 1]

def oddParityChannel : ReflectionChannel := ![1, -1]

def evenSectorEnergy (alpha beta : Rat) : Rat :=
  reflectionPairing alpha beta evenParityChannel

def oddSectorEnergy (alpha beta : Rat) : Rat :=
  reflectionPairing alpha beta oddParityChannel

theorem paritySectorEnergy_formula (alpha beta : Rat) :
    evenSectorEnergy alpha beta = 2 * (alpha + beta) ∧
      oddSectorEnergy alpha beta = 2 * (alpha - beta) := by
  constructor <;>
    norm_num [evenSectorEnergy, oddSectorEnergy, reflectionPairing,
      evenParityChannel, oddParityChannel] <;>
    ring

/-- One authorized even-sector flux leaves the odd-sector weight undetermined. -/
theorem oneParityFlux_is_not_faithful :
    evenSectorEnergy 2 0 = evenSectorEnergy 3 (-1) ∧
      oddSectorEnergy 2 0 ≠ oddSectorEnergy 3 (-1) := by
  norm_num [evenSectorEnergy, oddSectorEnergy, reflectionPairing,
    evenParityChannel, oddParityChannel]

def alphaFromParityEnergies (evenEnergy oddEnergy : Rat) : Rat :=
  (evenEnergy + oddEnergy) / 4

def betaFromParityEnergies (evenEnergy oddEnergy : Rat) : Rat :=
  (evenEnergy - oddEnergy) / 4

/-- The two parity-sector energies reconstruct both invariant coefficients. -/
theorem reconstruct_from_parity_energies (alpha beta : Rat) :
    alphaFromParityEnergies (evenSectorEnergy alpha beta)
        (oddSectorEnergy alpha beta) = alpha ∧
      betaFromParityEnergies (evenSectorEnergy alpha beta)
        (oddSectorEnergy alpha beta) = beta := by
  rw [paritySectorEnergy_formula alpha beta |>.1,
    paritySectorEnergy_formula alpha beta |>.2]
  constructor <;>
    norm_num [alphaFromParityEnergies, betaFromParityEnergies] <;>
    ring

theorem parityEnergyObservation_injective :
    Function.Injective (fun p : Rat × Rat =>
      (evenSectorEnergy p.1 p.2, oddSectorEnergy p.1 p.2)) := by
  intro p q h
  have hEven : evenSectorEnergy p.1 p.2 = evenSectorEnergy q.1 q.2 := by
    exact congrArg Prod.fst h
  have hOdd : oddSectorEnergy p.1 p.2 = oddSectorEnergy q.1 q.2 := by
    exact congrArg Prod.snd h
  apply Prod.ext
  · rw [← reconstruct_from_parity_energies p.1 p.2 |>.1,
      ← reconstruct_from_parity_energies q.1 q.2 |>.1, hEven, hOdd]
  · rw [← reconstruct_from_parity_energies p.1 p.2 |>.2,
      ← reconstruct_from_parity_energies q.1 q.2 |>.2, hEven, hOdd]

theorem finiteParityFluxFixture :
    alphaFromParityEnergies 10 6 = 4 ∧
      betaFromParityEnergies 10 6 = 1 ∧
      evenSectorEnergy 4 1 = 10 ∧
      oddSectorEnergy 4 1 = 6 := by
  norm_num [alphaFromParityEnergies, betaFromParityEnergies,
    evenSectorEnergy, oddSectorEnergy, reflectionPairing,
    evenParityChannel, oddParityChannel]

end MariciFormal
