import Mathlib.Tactic

/-!
Finite labelled-current core of Grothendieck's packet
`theta-collision-lifts-to-signed-labelled-current-coherence.md`.

Coordinate zero is the current value and coordinate one is its tangent.  This
file formalizes codiagonal aggregation and its cancellation kernel.  It does
not assume the conjectural theta-labelled coherence law.
-/

namespace MariciFormal

/-- Value/tangent collision data for one label. -/
abbrev CollisionVector := Fin 2 → ℝ

namespace LabelledCollision

/-- Codiagonal aggregation forgets the individual winding labels. -/
def aggregate {ι : Type*} [Fintype ι]
    (packet : ι → CollisionVector) : CollisionVector :=
  ∑ i, packet i

def ValueCancels {ι : Type*} [Fintype ι]
    (packet : ι → CollisionVector) : Prop :=
  aggregate packet 0 = 0

def TangentCancels {ι : Type*} [Fintype ι]
    (packet : ι → CollisionVector) : Prop :=
  aggregate packet 1 = 0

/-- The scalar double-zero collision after labels are summed. -/
def ScalarCollision {ι : Type*} [Fintype ι]
    (packet : ι → CollisionVector) : Prop :=
  ValueCancels packet ∧ TangentCancels packet

/-- The exact cross-label condition still needed on the value-zero locus. -/
def VerticallyTransverse {ι : Type*} [Fintype ι]
    (packet : ι → CollisionVector) : Prop :=
  ValueCancels packet → ¬ TangentCancels packet

theorem scalarCollision_iff_aggregate_zero
    {ι : Type*} [Fintype ι]
    (packet : ι → CollisionVector) :
    ScalarCollision packet ↔ aggregate packet = 0 := by
  constructor
  · intro h
    funext coordinate
    fin_cases coordinate
    · exact h.1
    · exact h.2
  · intro h
    constructor
    · exact congrFun h 0
    · exact congrFun h 1

theorem verticallyTransverse_iff_no_scalarCollision
    {ι : Type*} [Fintype ι]
    (packet : ι → CollisionVector) :
    VerticallyTransverse packet ↔ ¬ ScalarCollision packet := by
  simp [VerticallyTransverse, ScalarCollision]

/-- Two nonzero labels with the same local orientation and opposite global
sign. -/
def oppositeOrientedPacket : Fin 2 → CollisionVector :=
  ![![1, 1], ![-1, -1]]

theorem oppositeOrientedPacket_each_nonzero :
    ∀ i, oppositeOrientedPacket i ≠ 0 := by
  intro i
  fin_cases i <;> simp [oppositeOrientedPacket]

/-- Every label separately has positive value-times-tangent orientation. -/
theorem oppositeOrientedPacket_each_positive :
    ∀ i, 0 < oppositeOrientedPacket i 0 * oppositeOrientedPacket i 1 := by
  intro i
  fin_cases i <;> norm_num [oppositeOrientedPacket]

theorem oppositeOrientedPacket_aggregate_zero :
    aggregate oppositeOrientedPacket = 0 := by
  funext coordinate
  fin_cases coordinate <;> norm_num [aggregate, oppositeOrientedPacket]

/-- Per-label positive orientation does not descend through codiagonalization:
both aggregate collision channels can vanish. -/
theorem perLabelPositiveOrientation_does_not_imply_transversality :
    (∀ i, 0 < oppositeOrientedPacket i 0 * oppositeOrientedPacket i 1) ∧
      ScalarCollision oppositeOrientedPacket ∧
      ¬ VerticallyTransverse oppositeOrientedPacket := by
  refine ⟨oppositeOrientedPacket_each_positive, ?_, ?_⟩
  · rw [scalarCollision_iff_aggregate_zero]
    exact oppositeOrientedPacket_aggregate_zero
  · rw [verticallyTransverse_iff_no_scalarCollision]
    push_neg
    rw [scalarCollision_iff_aggregate_zero]
    exact oppositeOrientedPacket_aggregate_zero

/-- Codiagonal aggregation is not faithful on labelled collision packets. -/
theorem codiagonal_has_nontrivial_kernel :
    (∃ i, oppositeOrientedPacket i ≠ 0) ∧
      aggregate oppositeOrientedPacket = 0 := by
  exact ⟨⟨0, oppositeOrientedPacket_each_nonzero 0⟩,
    oppositeOrientedPacket_aggregate_zero⟩

end LabelledCollision

end MariciFormal
