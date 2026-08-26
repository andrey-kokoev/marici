import Mathlib.Algebra.GroupPower.Lemmas
import Mathlib.Data.Equiv.Basic
import Mathlib.Tactic

/-!
Finite permutation core of Grothendieck's inertia ghost-Frobenius system.
Arithmetic prime attachment and dynamical determinants are separate gates.
-/

namespace MariciFormal

section PowerSystem

variable {X : Type*}

def inertiaPower (permutation : Equiv.Perm X) (index : ℕ) : Equiv.Perm X :=
  permutation ^ index

theorem inertiaPower_comp
    (permutation : Equiv.Perm X) (first second : ℕ) :
    inertiaPower (inertiaPower permutation first) second =
      inertiaPower permutation (first * second) := by
  simp [inertiaPower, pow_mul]

theorem inertiaPower_one (permutation : Equiv.Perm X) :
    inertiaPower permutation 1 = permutation := by
  simp [inertiaPower]

end PowerSystem

section GhostCoordinates

variable {X : Type*} [Fintype X] [DecidableEq X]

def fixedPointCount (permutation : Equiv.Perm X) (index : ℕ) : ℕ :=
  (Finset.univ.filter fun x => (permutation ^ index) x = x).card

theorem fixedPointCount_inertiaPower_shift
    (permutation : Equiv.Perm X) (powerIndex ghostIndex : ℕ) :
    fixedPointCount (inertiaPower permutation powerIndex) ghostIndex =
      fixedPointCount permutation (powerIndex * ghostIndex) := by
  simp [fixedPointCount, inertiaPower, pow_mul]

end GhostCoordinates

def boolTransposition : Equiv.Perm Bool :=
  Equiv.swap false true

theorem boolTransposition_nontrivial :
    boolTransposition ≠ 1 := by
  intro h
  have := congrArg (fun permutation : Equiv.Perm Bool => permutation false) h
  simpa [boolTransposition] using this

theorem boolTransposition_square_identity :
    inertiaPower boolTransposition 2 = 1 := by
  ext x
  simpa [inertiaPower, boolTransposition] using
    Equiv.swap_apply_self false true x

/-- The second power operation turns a nonidentity two-cycle into the
identity, so inertia power is not the identity operation. -/
theorem inertiaPower_two_nontrivial_hostile :
    boolTransposition ≠ 1 ∧ inertiaPower boolTransposition 2 = 1 :=
  ⟨boolTransposition_nontrivial, boolTransposition_square_identity⟩

end MariciFormal
