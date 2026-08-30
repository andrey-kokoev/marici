import MariciFormal.FactorizationDescent

/-!
Sequential zero-control is an additional completion premise beyond algebraic
factorization.  Size functions are explicit so no norm or topology is silently
selected.
-/

namespace MariciFormal

open Filter Topology

/-- Every sequence invisible to the source size becomes invisible to the repair size. -/
def SequentialZeroControl {V : Type*} (sourceSize repairSize : V → ℝ) : Prop :=
  ∀ sequence : ℕ → V,
    Tendsto (fun n => sourceSize (sequence n)) atTop (𝓝 0) →
      Tendsto (fun n => repairSize (sequence n)) atTop (𝓝 0)

/-- A uniform size domination is a sufficient continuous-descent certificate. -/
theorem sequentialZeroControl_of_uniform_domination
    {V : Type*} {sourceSize repairSize : V → ℝ} {C : ℝ}
    (repair_nonnegative : ∀ v, 0 ≤ repairSize v)
    (domination : ∀ v, repairSize v ≤ C * sourceSize v) :
    SequentialZeroControl sourceSize repairSize := by
  intro sequence source_tends
  apply squeeze_zero (fun n => repair_nonnegative (sequence n))
    (fun n => domination (sequence n))
  have scaled :
      Tendsto (fun n => C * sourceSize (sequence n)) atTop (𝓝 (C * 0)) :=
    (tendsto_const_nhds : Tendsto (fun _ : ℕ => C) atTop (𝓝 C)).mul source_tends
  simpa using scaled

section Hostile

def zeroSize : ℚ → ℝ := fun _ => 0
def rationalAbsSize : ℚ → ℝ := fun x => |(x : ℝ)|

/-- The algebraic identity factors through itself, independently of size data. -/
theorem identity_algebraically_factors :
    FactorsThrough (LinearMap.id : ℚ →ₗ[ℚ] ℚ)
      (LinearMap.id : ℚ →ₗ[ℚ] ℚ) := by
  exact ⟨LinearMap.id, rfl⟩

/-- Hostile topology: the zero source seminorm cannot control absolute value. -/
theorem algebraic_factorization_does_not_supply_sequential_control :
    FactorsThrough (LinearMap.id : ℚ →ₗ[ℚ] ℚ)
        (LinearMap.id : ℚ →ₗ[ℚ] ℚ) ∧
      ¬ SequentialZeroControl zeroSize rationalAbsSize := by
  refine ⟨identity_algebraically_factors, ?_⟩
  intro control
  have bad := control (fun _ => (1 : ℚ)) (by simp [zeroSize])
  norm_num [rationalAbsSize] at bad

/-- Positive finite fixture: ordinary absolute value controls itself with constant one. -/
theorem absolute_value_controls_itself :
    SequentialZeroControl rationalAbsSize rationalAbsSize := by
  apply sequentialZeroControl_of_uniform_domination
    (sourceSize := rationalAbsSize) (repairSize := rationalAbsSize) (C := 1)
  · intro x
    exact abs_nonneg (x : ℝ)
  · intro x
    simp

end Hostile
end MariciFormal
