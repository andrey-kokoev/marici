import Mathlib.Algebra.Group.Units.Basic
import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Data.ZMod.Basic
import Mathlib.Tactic

/-!
Cyclic-kernel core of Grothendieck's Adams--Mackey exponent gate. General
finite abelian kernels and conjugation monodromy are external interfaces.
-/

namespace MariciFormal

def cyclicPowerMap (index modulus : ℕ) : ZMod modulus → ZMod modulus :=
  fun x => (index : ZMod modulus) * x

/-- Multiplication by the Adams index on a cyclic kernel is bijective exactly
when the index is coprime to the kernel order. -/
theorem cyclicPowerMap_bijective_iff_coprime (index modulus : ℕ) :
    Function.Bijective (cyclicPowerMap index modulus) ↔
      index.Coprime modulus := by
  unfold cyclicPowerMap
  exact IsUnit.isUnit_iff_mulLeft_bijective.symm.trans
    (ZMod.isUnit_iff_coprime index modulus)

/-- Every exponent-two cyclic branch retains exactly the odd Adams indices. -/
theorem exponentTwo_cyclicPowerMap_bijective_iff_odd (index : ℕ) :
    Function.Bijective (cyclicPowerMap index 2) ↔ Odd index := by
  rw [cyclicPowerMap_bijective_iff_coprime, Nat.coprime_two_right]

/-- The first even Adams operation collapses the two exponent-two labels. -/
theorem evenAdams_collision_hostile :
    cyclicPowerMap 2 2 (0 : ZMod 2) = cyclicPowerMap 2 2 1 ∧
      (0 : ZMod 2) ≠ 1 ∧
      ¬ Function.Bijective (cyclicPowerMap 2 2) := by
  constructor
  · norm_num [cyclicPowerMap]
  constructor
  · norm_num
  · rw [cyclicPowerMap_bijective_iff_coprime]
    norm_num

end MariciFormal
