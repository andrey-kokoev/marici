import Mathlib.Algebra.Group.Subgroup.Defs
import Mathlib.Tactic

/-!
Minimal additive Hom-complex core of Grothendieck's degenerate-pairing radical
repair obstruction. Grading, chain differentials, and physical pairings remain
external typed interfaces.
-/

namespace MariciFormal

section AbstractRadicalRepair

variable {Source Target : Type*}
variable [AddCommGroup Source] [AddCommGroup Target]

/-- A map is invisible to the admitted pairing when its image lies in the
chosen right radical. -/
def RadicalValued (radical : AddSubgroup Target)
    (map : Source →+ Target) : Prop :=
  ∀ source, map source ∈ radical

/-- The Hom differential preserves the radical-valued subspace. -/
def PreservesRadical (radical : AddSubgroup Target)
    (homDifferential : (Source →+ Target) →+ (Source →+ Target)) : Prop :=
  ∀ map, RadicalValued radical map →
    RadicalValued radical (homDifferential map)

/-- A pairing-invisible correction cancels the original boundary defect. -/
def HasRadicalRepair (radical : AddSubgroup Target)
    (homDifferential : (Source →+ Target) →+ (Source →+ Target))
    (defect : Source →+ Target) : Prop :=
  ∃ correction, RadicalValued radical correction ∧
    defect + homDifferential correction = 0

/-- Exactness of a radical-valued defect in the degree-minus-one Hom channel.
The radical-valuedness condition is intentionally not bundled into this
predicate, so the two obstruction stages remain distinguishable. -/
def RadicalHomExact (radical : AddSubgroup Target)
    (homDifferential : (Source →+ Target) →+ (Source →+ Target))
    (defect : Source →+ Target) : Prop :=
  ∃ correction, RadicalValued radical correction ∧
    defect + homDifferential correction = 0

/-- Repair is equivalent to the two distinct gates: the defect projects to
zero modulo the radical, and its resulting radical-valued Hom class is exact. -/
theorem hasRadicalRepair_iff_projected_zero_and_exact
    (radical : AddSubgroup Target)
    (homDifferential : (Source →+ Target) →+ (Source →+ Target))
    (defect : Source →+ Target)
    (hpreserves : PreservesRadical radical homDifferential) :
    HasRadicalRepair radical homDifferential defect ↔
      RadicalValued radical defect ∧
        RadicalHomExact radical homDifferential defect := by
  constructor
  · rintro ⟨correction, hcorrection, hzero⟩
    constructor
    · intro source
      have hpoint :
          defect source + homDifferential correction source = 0 := by
        have := congrArg (fun map : Source →+ Target ⇒ map source) hzero
        simpa using this
      have hmembership := hpreserves correction hcorrection source
      have heq : defect source = -(homDifferential correction source) := by
        calc
          defect source =
              defect source + homDifferential correction source -
                homDifferential correction source := by simp
          _ = -(homDifferential correction source) := by rw [hpoint]; simp
      rw [heq]
      exact radical.neg_mem hmembership
    · exact ⟨correction, hcorrection, hzero⟩
  · rintro ⟨_, correction, hcorrection, hzero⟩
    exact ⟨correction, hcorrection, hzero⟩

/-- In the perfect-pairing limit the radical is zero, so a repair exists
exactly when the original defect is already zero. -/
theorem hasRadicalRepair_bot_iff
    (homDifferential : (Source →+ Target) →+ (Source →+ Target))
    (defect : Source →+ Target) :
    HasRadicalRepair ⊥ homDifferential defect ↔ defect = 0 := by
  constructor
  · rintro ⟨correction, hcorrection, hzero⟩
    have hcorrectionZero : correction = 0 := by
      ext source
      simpa using hcorrection source
    simpa [hcorrectionZero] using hzero
  · intro hdefect
    refine ⟨0, ?_, ?_⟩
    · intro source
      simp
    · simp [hdefect]

end AbstractRadicalRepair

/-- A defect may lie entirely in a radical yet represent a nonzero Hom class:
with zero Hom differential, the identity defect on `ℤ` cannot be repaired. -/
theorem projected_radical_zero_not_sufficient_hostile :
    let radical : AddSubgroup ℤ := ⊤
    let homDifferential : (ℤ →+ ℤ) →+ (ℤ →+ ℤ) := 0
    let defect : ℤ →+ ℤ := AddMonoidHom.id ℤ
    RadicalValued radical defect ∧
      ¬ HasRadicalRepair radical homDifferential defect := by
  dsimp
  constructor
  · intro source
    simp
  · rintro ⟨correction, _, hzero⟩
    have hpoint := congrArg (fun map : ℤ →+ ℤ ⇒ map 1) hzero
    norm_num at hpoint

end MariciFormal
