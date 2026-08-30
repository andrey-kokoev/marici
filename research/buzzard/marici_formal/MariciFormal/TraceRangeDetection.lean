import Mathlib.Data.Fin.VecNotation
import Mathlib.Data.ZMod.Basic
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
Abstract algebraic core of Grothendieck's norm detection theorem for
fiber-invariant boundary defects. Physical trace and pushforward maps are not
constructed here.
-/

namespace MariciFormal

section Detection

variable {X Y : Type*} [AddCommGroup X] [AddCommGroup Y]

/-- If `S T = d id` and multiplication by `d` is injective on the target,
then `S` detects every vector in the trace range. -/
theorem trace_range_detected_away_from_torsion
    (S : X →+ Y) (T : Y →+ X) (degree : ℕ)
    (hnorm : ∀ y, S (T y) = degree • y)
    (hdegree : Function.Injective (fun y : Y ↦ degree • y))
    (y : Y) (hvanish : S (T y) = 0) :
    T y = 0 := by
  have hdegreeZero : degree • y = 0 := by
    rw [← hnorm y]
    exact hvanish
  have hy : y = 0 := by
    apply hdegree
    simpa using hdegreeZero
  simp [hy]

end Detection

section BadPrimeHostile

def modTwoFiberTrace : ZMod 2 →+ (Fin 2 → ZMod 2) where
  toFun y := ![y, y]
  map_zero' := by ext i; fin_cases i <;> rfl
  map_add' left right := by ext i; fin_cases i <;> rfl

def modTwoFiberSum : (Fin 2 → ZMod 2) →+ ZMod 2 where
  toFun x := x 0 + x 1
  map_zero' := by simp
  map_add' left right := by simp; ring

/-- At the degree prime, the nonzero invariant trace vector is killed by the
fiber sum. -/
theorem degree_two_trace_detection_fails_mod_two :
    modTwoFiberTrace 1 ≠ 0 ∧
      modTwoFiberSum (modTwoFiberTrace 1) = 0 := by
  constructor
  · intro hzero
    have hpoint := congrFun hzero 0
    norm_num [modTwoFiberTrace] at hpoint
  · norm_num [modTwoFiberTrace, modTwoFiberSum]

end BadPrimeHostile

end MariciFormal
