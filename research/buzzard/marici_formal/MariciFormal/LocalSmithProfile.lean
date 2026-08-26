import Mathlib

/-!
Determinant order records only total defect depth; the local Smith profile
also records how that depth is distributed among lost directions.
-/

namespace MariciFormal

/-- Ordered local Smith exponents of a diagonal two-direction fixture. -/
abbrev SmithProfile₂ := Nat × Nat

def OrderedSmithProfile (profile : SmithProfile₂) : Prop :=
  profile.1 ≤ profile.2

def determinantOrder (profile : SmithProfile₂) : Nat :=
  profile.1 + profile.2

def seamCorank (profile : SmithProfile₂) : Nat :=
  (if profile.1 = 0 then 0 else 1) +
    (if profile.2 = 0 then 0 else 1)

/-- Valuations of the first and second determinantal ideals. -/
def determinantalValuations (profile : SmithProfile₂) : Nat × Nat :=
  (min profile.1 profile.2, determinantOrder profile)

/-- Successive differences recover Smith exponents from minor-ideal orders. -/
def recoverSmithProfile (valuations : Nat × Nat) : SmithProfile₂ :=
  (valuations.1, valuations.2 - valuations.1)

theorem determinantalValuations_recover
    (profile : SmithProfile₂) (hOrdered : OrderedSmithProfile profile) :
    recoverSmithProfile (determinantalValuations profile) = profile := by
  rcases profile with ⟨first, second⟩
  simp [determinantalValuations, determinantOrder,
    recoverSmithProfile, Nat.min_eq_left hOrdered]

def deepSingleAlias : SmithProfile₂ := (0, 2)

def twoShallowAliases : SmithProfile₂ := (1, 1)

theorem equalDeterminantOrder_distinctFailureType :
    determinantOrder deepSingleAlias = 2 ∧
      determinantOrder twoShallowAliases = 2 ∧
      seamCorank deepSingleAlias = 1 ∧
      seamCorank twoShallowAliases = 2 ∧
      deepSingleAlias ≠ twoShallowAliases := by
  decide

theorem determinantalFixtures :
    determinantalValuations deepSingleAlias = (0, 2) ∧
      determinantalValuations twoShallowAliases = (1, 2) ∧
      recoverSmithProfile (0, 2) = deepSingleAlias ∧
      recoverSmithProfile (1, 2) = twoShallowAliases := by
  decide

/-- Aggregate determinant depth cannot classify the failure module. -/
theorem determinantOrder_not_completeInvariant :
    ∃ profileA profileB : SmithProfile₂,
      determinantOrder profileA = determinantOrder profileB ∧
      profileA ≠ profileB ∧
      seamCorank profileA ≠ seamCorank profileB := by
  exact ⟨deepSingleAlias, twoShallowAliases, by decide, by decide, by decide⟩

end MariciFormal
