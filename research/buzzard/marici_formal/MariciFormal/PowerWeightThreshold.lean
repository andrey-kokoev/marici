import Mathlib

/-!
The exact integer-power fixtures for a linear-growth trace: quadratic and
cubic weights fail, while quartic weight succeeds.
-/

namespace MariciFormal

/-- Weighted-dual term for coefficient `c_n = n+1` and weight `(n+1)^beta`. -/
noncomputable def linearPowerDualTerm (beta n : Nat) : Real :=
  ((n + 1 : Nat) : Real) ^ 2 / ((n + 1 : Nat) : Real) ^ beta

private theorem successorCast_ne_zero (n : Nat) : ((n + 1 : Nat) : Real) ≠ 0 := by
  positivity

theorem quadraticWeight_dual_not_summable :
    ¬ Summable (linearPowerDualTerm 2) := by
  have hterm : linearPowerDualTerm 2 = fun _ : Nat => (1 : Real) := by
    funext n
    unfold linearPowerDualTerm
    field_simp [successorCast_ne_zero n]
  rw [hterm]
  simpa only [summable_const_iff] using (one_ne_zero : (1 : Real) ≠ 0)

theorem cubicWeight_dual_not_summable :
    ¬ Summable (linearPowerDualTerm 3) := by
  have hterm : linearPowerDualTerm 3 =
      fun n : Nat => 1 / ((n + 1 : Nat) : Real) := by
    funext n
    unfold linearPowerDualTerm
    field_simp [successorCast_ne_zero n]
  rw [hterm]
  exact mt
    (summable_nat_add_iff (f := fun n : Nat => 1 / (n : Real)) 1).mp
    Real.not_summable_one_div_natCast

theorem quarticWeight_dual_summable :
    Summable (linearPowerDualTerm 4) := by
  have hterm : linearPowerDualTerm 4 =
      fun n : Nat => 1 / ((n + 1 : Nat) : Real) ^ 2 := by
    funext n
    unfold linearPowerDualTerm
    field_simp [successorCast_ne_zero n]
  rw [hterm]
  exact
    (summable_nat_add_iff (f := fun n : Nat => 1 / (n : Real) ^ 2) 1).mpr
      ((Real.summable_one_div_nat_pow (p := 2)).mpr (by omega))

end MariciFormal
