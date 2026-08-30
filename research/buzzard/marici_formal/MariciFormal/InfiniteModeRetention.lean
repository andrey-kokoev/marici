import Mathlib.Data.Set.Finite.Basic

/-!
Information-level precursor to Grothendieck's continuum moving-seam
noncompactness theorem.  Retaining infinitely many distinct fixed modes cannot
be inferred from, or reduced to, a finite scalar readout.
-/

namespace MariciFormal

variable {I X S : Type*} [Infinite I]

/-- An operator fixing an injectively indexed infinite family has infinite
set-theoretic range. -/
theorem infinite_range_of_fixed_injective_family
    (operator : X → X) (mode : I → X)
    (hmodeInjective : Function.Injective mode)
    (hfixed : ∀ i, operator (mode i) = mode i) :
    Set.Infinite (Set.range operator) := by
  apply (Set.infinite_range_of_injective hmodeInjective).mono
  rintro _ ⟨i, rfl⟩
  exact ⟨mode i, hfixed i⟩

section ScalarCompressionHostile

def retainedModeOperator : ℕ → ℕ := id

def singletonScalarReadout : ℕ → Fin 1 := fun _ => 0

theorem retainedModeOperator_has_infinite_range :
    Set.Infinite (Set.range retainedModeOperator) := by
  exact infinite_range_of_fixed_injective_family
    retainedModeOperator id Function.injective_id (fun _ => rfl)

theorem singletonScalarReadout_has_finite_range :
    (Set.range singletonScalarReadout).Finite := by
  exact Set.toFinite _

/-- A finite scalar image can coexist with an infinite retained carrier. -/
theorem finite_scalar_readout_does_not_bound_carrier_range :
    (Set.range singletonScalarReadout).Finite ∧
      Set.Infinite (Set.range retainedModeOperator) :=
  ⟨singletonScalarReadout_has_finite_range,
    retainedModeOperator_has_infinite_range⟩

end ScalarCompressionHostile

end MariciFormal
