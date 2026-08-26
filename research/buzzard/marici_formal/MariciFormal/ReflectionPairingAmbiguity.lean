import Mathlib

/-!
Reflection invariance plus positive definiteness does not select a unique
two-channel pairing.
-/

namespace MariciFormal

abbrev ReflectionChannel := Fin 2 → Rat

def swapChannels (x : ReflectionChannel) : ReflectionChannel := ![x 1, x 0]

/-- Symmetric reflection-invariant matrix `[[alpha,beta],[beta,alpha]]`. -/
def reflectionPairing (alpha beta : Rat) (x : ReflectionChannel) : Rat :=
  alpha * x 0 ^ 2 + 2 * beta * x 0 * x 1 + alpha * x 1 ^ 2

def PositiveDefiniteChannelForm (form : ReflectionChannel → Rat) : Prop :=
  ∀ x, x ≠ 0 → 0 < form x

theorem reflectionPairing_swap_invariant
    (alpha beta : Rat) (x : ReflectionChannel) :
    reflectionPairing alpha beta (swapChannels x) =
      reflectionPairing alpha beta x := by
  simp [reflectionPairing, swapChannels]
  ring

def identityPairing : ReflectionChannel → Rat :=
  reflectionPairing 1 0

def coupledPairing : ReflectionChannel → Rat :=
  reflectionPairing 2 1

theorem identityPairing_positiveDefinite :
    PositiveDefiniteChannelForm identityPairing := by
  intro x hx
  unfold identityPairing reflectionPairing
  by_cases h0 : x 0 = 0
  · have h1 : x 1 ≠ 0 := by
      intro h1
      apply hx
      funext i
      fin_cases i <;> assumption
    nlinarith [sq_pos_of_ne_zero h1]
  · nlinarith [sq_pos_of_ne_zero h0, sq_nonneg (x 1)]

theorem coupledPairing_positiveDefinite :
    PositiveDefiniteChannelForm coupledPairing := by
  intro x hx
  unfold coupledPairing reflectionPairing
  have decomposition :
      2 * x 0 ^ 2 + 2 * x 0 * x 1 + 2 * x 1 ^ 2 =
        (x 0 + x 1) ^ 2 + x 0 ^ 2 + x 1 ^ 2 := by ring
  norm_num only [mul_one]
  rw [decomposition]
  by_cases h0 : x 0 = 0
  · have h1 : x 1 ≠ 0 := by
      intro h1
      apply hx
      funext i
      fin_cases i <;> assumption
    nlinarith [sq_pos_of_ne_zero h1, sq_nonneg (x 0 + x 1)]
  · nlinarith [sq_pos_of_ne_zero h0, sq_nonneg (x 1), sq_nonneg (x 0 + x 1)]

def firstChannelFeature : ReflectionChannel := ![1, 0]

theorem pairings_differ_on_firstChannelFeature :
    identityPairing firstChannelFeature = 1 ∧
      coupledPairing firstChannelFeature = 2 := by
  norm_num [identityPairing, coupledPairing, reflectionPairing, firstChannelFeature]

/-- Reflection and positivity admit distinct pairings with different energies. -/
theorem reflectionAndPositivity_do_not_select_pairing :
    ∃ form₀ form₁ : ReflectionChannel → Rat,
      (∀ x, form₀ (swapChannels x) = form₀ x) ∧
      (∀ x, form₁ (swapChannels x) = form₁ x) ∧
      PositiveDefiniteChannelForm form₀ ∧
      PositiveDefiniteChannelForm form₁ ∧
      form₀ firstChannelFeature ≠ form₁ firstChannelFeature := by
  refine ⟨identityPairing, coupledPairing,
    reflectionPairing_swap_invariant 1 0,
    reflectionPairing_swap_invariant 2 1,
    identityPairing_positiveDefinite,
    coupledPairing_positiveDefinite, ?_⟩
  rw [pairings_differ_on_firstChannelFeature.1,
    pairings_differ_on_firstChannelFeature.2]
  norm_num

end MariciFormal
