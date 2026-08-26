import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Tactic.NormNum

/-!
Prime-local logical core of Grothendieck's norm--resonance trichotomy. The
finite-group theorem supplying `rad(d) | rho` is an external interface.
-/

namespace MariciFormal

/-- If every norm prime is a resonance prime, the prime-local state belongs
to exactly one of the three admissible logical cells. -/
theorem norm_resonance_three_regimes
    (prime degree resonance : ℕ)
    (hsupport : prime ∣ degree → prime ∣ resonance) :
    (¬ prime ∣ degree ∧ ¬ prime ∣ resonance) ∨
      (prime ∣ degree ∧ prime ∣ resonance) ∨
      (¬ prime ∣ degree ∧ prime ∣ resonance) := by
  by_cases hdegree : prime ∣ degree
  · exact Or.inr (Or.inl ⟨hdegree, hsupport hdegree⟩)
  · by_cases hresonance : prime ∣ resonance
    · exact Or.inr (Or.inr ⟨hdegree, hresonance⟩)
    · exact Or.inl ⟨hdegree, hresonance⟩

/-- The fourth cell, norm-bad but resonance-good, is impossible. -/
theorem norm_bad_resonance_good_impossible
    (prime degree resonance : ℕ)
    (hsupport : prime ∣ degree → prime ∣ resonance) :
    ¬ (prime ∣ degree ∧ ¬ prime ∣ resonance) := by
  rintro ⟨hdegree, hresonance⟩
  exact hresonance (hsupport hdegree)

/-- In the `(d,rho)=(4,6)` control, three is resonance-only. -/
theorem a4_prime_three_resonance_only :
    ¬ 3 ∣ 4 ∧ 3 ∣ 6 := by
  norm_num

end MariciFormal
