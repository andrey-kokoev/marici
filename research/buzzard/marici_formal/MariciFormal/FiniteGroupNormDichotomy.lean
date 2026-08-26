import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.ZMod.Basic
import Mathlib.Tactic

/-!
Regular-fiber linear core of Grothendieck's finite-group norm characteristic
dichotomy. Group-law representation theory and physical pushforward are external.
-/

namespace MariciFormal

open scoped BigOperators

section RegularNorm

variable {G K : Type*} [Fintype G] [Group G] [Field K]

/-- On the regular coefficient fiber, the group norm sends a packet to the
constant packet whose value is its augmentation. -/
def regularFiberNorm (packet : G → K) : G → K :=
  fun _ => ∑ g, packet g

def regularAugmentation (packet : G → K) : K :=
  ∑ g, packet g

theorem regularFiberNorm_apply (packet : G → K) (g : G) :
    regularFiberNorm packet g = regularAugmentation packet := rfl

/-- The universal norm relation is `N² = |G| N`. -/
theorem regularFiberNorm_square (packet : G → K) (g : G) :
    regularFiberNorm (regularFiberNorm packet) g =
      (Fintype.card G : K) * regularFiberNorm packet g := by
  simp [regularFiberNorm, Finset.sum_const, nsmul_eq_mul]

theorem regularFiberNorm_eq_zero_iff (packet : G → K) :
    regularFiberNorm packet = 0 ↔ regularAugmentation packet = 0 := by
  constructor
  · intro hzero
    have hatOne := congrFun hzero 1
    simpa [regularFiberNorm, regularAugmentation] using hatOne
  · intro haugmentation
    funext g
    simp [regularFiberNorm, regularAugmentation, haugmentation]

/-- In bad characteristic, the regular norm differential is square-zero. -/
theorem regularFiberNorm_square_zero
    (hcard : (Fintype.card G : K) = 0) (packet : G → K) :
    regularFiberNorm (regularFiberNorm packet) = 0 := by
  funext g
  rw [regularFiberNorm_square]
  simp [hcard]

/-- Away from group-order torsion, division by `|G|` produces the normalized
invariant projector. -/
def regularFiberAverage (packet : G → K) : G → K :=
  fun _ => regularAugmentation packet / (Fintype.card G : K)

theorem regularFiberAverage_idempotent
    (hcard : (Fintype.card G : K) ≠ 0) (packet : G → K) :
    regularFiberAverage (regularFiberAverage packet) =
      regularFiberAverage packet := by
  funext g
  simp [regularFiberAverage, regularAugmentation, Finset.sum_const,
    nsmul_eq_mul]
  field_simp

end RegularNorm

section BadCharacteristicHostile

def boolRegularPacket (_ : Bool) : ZMod 2 := 1

theorem boolRegularPacket_nonzero : boolRegularPacket ≠ 0 := by
  intro hzero
  have h := congrFun hzero false
  norm_num [boolRegularPacket] at h

/-- The order-two regular fiber in characteristic two has a nonzero packet in
the norm kernel. -/
theorem characteristicTwo_normKernel_hostile :
    boolRegularPacket ≠ 0 ∧
      regularFiberNorm boolRegularPacket = 0 := by
  refine ⟨boolRegularPacket_nonzero, ?_⟩
  funext g
  simp [regularFiberNorm, boolRegularPacket]

end BadCharacteristicHostile

end MariciFormal
