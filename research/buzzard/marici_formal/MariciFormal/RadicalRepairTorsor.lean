import Mathlib.Algebra.Group.Hom.End
import Mathlib.Tactic

/-!
Affine solution-space core of Grothendieck's radical-repair torsor theorem.
The chain grading, radical inclusion, and chain-homotopy quotient remain
external typed interfaces.
-/

namespace MariciFormal

section RepairTorsor

variable {Source Target : Type*}
variable [AddCommGroup Source] [AddCommGroup Target]

def IsRepair
    (homDifferential : (Source →+ Target) →+ (Source →+ Target))
    (defect correction : Source →+ Target) : Prop :=
  defect + homDifferential correction = 0

def IsClosedCorrection
    (homDifferential : (Source →+ Target) →+ (Source →+ Target))
    (correction : Source →+ Target) : Prop :=
  homDifferential correction = 0

/-- Once a base repair exists, every other repair differs from it by a
closed correction. -/
theorem isRepair_iff_difference_closed
    (homDifferential : (Source →+ Target) →+ (Source →+ Target))
    (defect base correction : Source →+ Target)
    (hbase : IsRepair homDifferential defect base) :
    IsRepair homDifferential defect correction ↔
      IsClosedCorrection homDifferential (correction - base) := by
  unfold IsRepair IsClosedCorrection at hbase ⊢
  rw [map_sub]
  constructor
  · intro hcorrection
    apply sub_eq_zero.mpr
    exact add_left_cancel (hcorrection.trans hbase.symm)
  · intro hclosed
    have hdifferentials :
        homDifferential correction = homDifferential base :=
      sub_eq_zero.mp hclosed
    simpa [hdifferentials] using hbase

/-- Translating a repair by a closed correction gives another repair. -/
theorem closedCorrection_translates_repair
    (homDifferential : (Source →+ Target) →+ (Source →+ Target))
    (defect base cycle : Source →+ Target)
    (hbase : IsRepair homDifferential defect base)
    (hcycle : IsClosedCorrection homDifferential cycle) :
    IsRepair homDifferential defect (base + cycle) := by
  unfold IsRepair IsClosedCorrection at hbase hcycle ⊢
  rw [map_add, hcycle, add_zero]
  exact hbase

/-- If the closed-correction group is trivial, a repair is unique. -/
theorem repair_unique_of_closed_trivial
    (homDifferential : (Source →+ Target) →+ (Source →+ Target))
    (defect : Source →+ Target)
    (htrivial : ∀ cycle, IsClosedCorrection homDifferential cycle → cycle = 0)
    {left right : Source →+ Target}
    (hleft : IsRepair homDifferential defect left)
    (hright : IsRepair homDifferential defect right) :
    left = right := by
  have hclosed : IsClosedCorrection homDifferential (right - left) :=
    (isRepair_iff_difference_closed homDifferential defect left right hleft).mp hright
  have hzero := htrivial (right - left) hclosed
  exact (sub_eq_zero.mp hzero).symm

end RepairTorsor

/-- With zero differential and zero defect, integer multiplications give
distinct repairs; existence supplies no canonical repair. -/
theorem integer_zero_differential_repairs_nonunique :
    let homDifferential : (ℤ →+ ℤ) →+ (ℤ →+ ℤ) := 0
    let defect : ℤ →+ ℤ := 0
    IsRepair homDifferential defect 0 ∧
      IsRepair homDifferential defect (AddMonoidHom.id ℤ) ∧
      (0 : ℤ →+ ℤ) ≠ AddMonoidHom.id ℤ := by
  dsimp [IsRepair]
  constructor
  · simp
  constructor
  · simp
  · intro heq
    have hpoint := DFunLike.congr_fun heq 1
    norm_num at hpoint

end MariciFormal
