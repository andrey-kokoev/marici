import Mathlib.Algebra.Group.Hom.End
import Mathlib.Tactic.NormNum

/-!
Quotient-independence core of Grothendieck's cohomology-representative
anomaly. Chain degrees and Bianchi data remain explicit external interfaces.
-/

namespace MariciFormal

section AbstractRepresentativeDescent

variable {Parameter Target Source : Type*}
variable [AddCommGroup Parameter] [AddCommGroup Target] [AddCommGroup Source]

def CohomologousBy
    (boundary : Parameter →+ Target) (left right : Target) : Prop :=
  ∃ alpha, right = left + boundary alpha

def RepresentativeIndependent
    (boundary : Parameter →+ Target) (pullback : Target →+ Source) : Prop :=
  ∀ left right, CohomologousBy boundary left right →
    pullback left = pullback right

def representativeAnomaly
    (boundary : Parameter →+ Target) (pullback : Target →+ Source)
    (alpha : Parameter) : Source :=
  pullback (boundary alpha)

theorem representativeIndependent_iff_anomaly_zero
    (boundary : Parameter →+ Target) (pullback : Target →+ Source) :
    RepresentativeIndependent boundary pullback ↔
      ∀ alpha, representativeAnomaly boundary pullback alpha = 0 := by
  constructor
  · intro hindependent alpha
    have hcohom : CohomologousBy boundary 0 (boundary alpha) := by
      exact ⟨alpha, by simp⟩
    have h := hindependent 0 (boundary alpha) hcohom
    simpa [representativeAnomaly] using h.symm
  · intro hanomaly left right hcohom
    obtain ⟨alpha, rfl⟩ := hcohom
    simp [map_add, representativeAnomaly, hanomaly alpha]

theorem exact_target_maps_to_zero_of_representativeIndependent
    (boundary : Parameter →+ Target) (pullback : Target →+ Source)
    (hindependent : RepresentativeIndependent boundary pullback)
    (alpha : Parameter) :
    pullback (boundary alpha) = 0 := by
  exact (representativeIndependent_iff_anomaly_zero boundary pullback).mp
    hindependent alpha

end AbstractRepresentativeDescent

/-- Identity boundary and identity pullback on `ℤ` send an exact target
representative to the nonzero source value `1`. -/
theorem nonzero_representativeAnomaly_hostile :
    let boundary : ℤ →+ ℤ := AddMonoidHom.id ℤ
    let pullback : ℤ →+ ℤ := AddMonoidHom.id ℤ
    CohomologousBy boundary 0 1 ∧
      representativeAnomaly boundary pullback 1 = 1 ∧
      ¬ RepresentativeIndependent boundary pullback := by
  dsimp
  constructor
  · exact ⟨1, by norm_num⟩
  constructor
  · norm_num [representativeAnomaly]
  · intro h
    have hz := (representativeIndependent_iff_anomaly_zero
      (AddMonoidHom.id ℤ) (AddMonoidHom.id ℤ)).mp h 1
    norm_num [representativeAnomaly] at hz

end MariciFormal
