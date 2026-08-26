import Mathlib.LinearAlgebra.Basic

/-!
Linear-algebra core of Grothendieck's separated-support boundary-defect
detection theorem. Recovery of untransported defects still requires separate
surjectivity and relative-injectivity premises.
-/

namespace MariciFormal

section SeparatedImages

variable {R X Y : Type*} [CommRing R]
variable [AddCommGroup X] [AddCommGroup Y] [Module R X] [Module R Y]

/-- Two transported defect terms with disjoint ranges cannot cancel except
by vanishing separately. -/
theorem separated_ranges_prevent_cancellation
    (left right : X →ₗ[R] Y)
    (hseparated : LinearMap.range left ⊓ LinearMap.range right = ⊥)
    (x : X) (hzero : left x + right x = 0) :
    left x = 0 ∧ right x = 0 := by
  have heq : left x = -(right x) := by
    calc
      left x = left x + right x - right x := by simp
      _ = -(right x) := by rw [hzero]; simp
  have hleftRange : left x ∈ LinearMap.range left := ⟨x, rfl⟩
  have hrightRange : left x ∈ LinearMap.range right := by
    refine ⟨-x, ?_⟩
    simp [heq]
  have hintersection : left x ∈ LinearMap.range left ⊓ LinearMap.range right :=
    ⟨hleftRange, hrightRange⟩
  have hleftZero : left x = 0 := by
    rw [hseparated] at hintersection
    exact hintersection
  constructor
  · exact hleftZero
  · simpa [hleftZero] using hzero

/-- Separation alone says nothing about a nonzero defect already annihilated
by its transport. -/
theorem separation_does_not_prevent_annihilation_hostile :
    let transport : (Fin 2 → ℚ) →ₗ[ℚ] ℚ := LinearMap.proj 0
    let defect : Fin 2 → ℚ := fun i ↦ if i = 1 then 1 else 0
    defect ≠ 0 ∧ transport defect = 0 := by
  dsimp
  constructor
  · intro hzero
    have hpoint := congrFun hzero 1
    norm_num at hpoint
  · rfl

end SeparatedImages

end MariciFormal
