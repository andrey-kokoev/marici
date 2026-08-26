import Mathlib.Tactic.Abel
import Mathlib.Tactic.FinCases

/-!
Abstract algebraic core of Grothendieck's moving-seam projection cocycle.
The defect of transporting a fixed cut is coherent by a one-cocycle law, not
by pretending the transported cuts are strictly identical.
-/

namespace MariciFormal

structure MovingSeamSystem (G V : Type*) [Add G] [AddCommGroup V] where
  cut : V
  transport : G → V → V
  transport_add : ∀ g h x, transport (g + h) x = transport g (transport h x)
  transport_sub : ∀ g x y, transport g (x - y) = transport g x - transport g y

namespace MovingSeamSystem

variable {G V : Type*} [Add G] [AddCommGroup V]

def defect (system : MovingSeamSystem G V) (g : G) : V :=
  system.cut - system.transport g system.cut

/-- The moving cut carries an exact transported one-cocycle. -/
theorem defect_add (system : MovingSeamSystem G V) (g h : G) :
    system.defect (g + h) =
      system.defect g + system.transport g (system.defect h) := by
  simp only [defect, system.transport_add, system.transport_sub]
  abel

/-- A zero seam defect is exactly strict invariance of the cut under the
declared transport. -/
theorem defect_eq_zero_iff (system : MovingSeamSystem G V) (g : G) :
    system.defect g = 0 ↔ system.transport g system.cut = system.cut := by
  simp [defect, sub_eq_zero, eq_comm]

/-- Nonzero defect is therefore an explicit witness that strict transport
equality is unavailable, even though coherent composition still holds. -/
theorem nonzero_defect_rejects_strict_transport
    (system : MovingSeamSystem G V) (g : G)
    (hdefect : system.defect g ≠ 0) :
    system.transport g system.cut ≠ system.cut := by
  exact fun hstrict => hdefect ((system.defect_eq_zero_iff g).2 hstrict)

end MovingSeamSystem

section FiniteMovingSeamHostile

def parityReflectionSeam : MovingSeamSystem (Fin 2) ℤ where
  cut := 1
  transport g x := if g = 0 then x else -x
  transport_add g h x := by
    fin_cases g <;> fin_cases h <;> simp
  transport_sub g x y := by
    fin_cases g <;> simp

theorem parityReflectionSeam_unit_defect :
    parityReflectionSeam.defect 1 = 2 := by
  norm_num [MovingSeamSystem.defect, parityReflectionSeam]

theorem parityReflectionSeam_coherent_but_not_strict :
    parityReflectionSeam.defect (1 + 1) =
        parityReflectionSeam.defect 1 +
          parityReflectionSeam.transport 1
            (parityReflectionSeam.defect 1) ∧
      parityReflectionSeam.transport 1 parityReflectionSeam.cut ≠
        parityReflectionSeam.cut := by
  constructor
  · exact parityReflectionSeam.defect_add 1 1
  · norm_num [parityReflectionSeam]

end FiniteMovingSeamHostile

end MariciFormal
