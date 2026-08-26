import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic

/-!
Typed partial logarithmic-chart boundary extracted from Grothendieck's Euler
staircase audit. Analytic logarithms and Hurwitz convergence are external.
-/

namespace MariciFormal

section PartialChart

variable {K : Type*} [Field K]

/-- The logarithmic derivative is a chart only where the scalar section is
nonzero. `Option` records this domain instead of silently totalizing division. -/
def logarithmicDerivativeChart (value derivative : K) : Option K :=
  if value = 0 then none else some (derivative / value)

def LogarithmicChartAvailable (value derivative : K) : Prop :=
  ∃ coordinate, logarithmicDerivativeChart value derivative = some coordinate

theorem logarithmicChart_available_iff
    (value derivative : K) :
    LogarithmicChartAvailable value derivative ↔ value ≠ 0 := by
  by_cases hvalue : value = 0
  · simp [LogarithmicChartAvailable, logarithmicDerivativeChart, hvalue]
  · simp [LogarithmicChartAvailable, logarithmicDerivativeChart, hvalue]

theorem logarithmicChart_unavailable_at_zero (derivative : K) :
    ¬ LogarithmicChartAvailable 0 derivative := by
  simp [logarithmicChart_available_iff]

/-- Lean's totalized field division at zero is not evidence that the
logarithmic chart extends through a zero. -/
theorem totalizedDivision_is_not_chart_hostile :
    (1 : ℚ) / 0 = 0 ∧
      logarithmicDerivativeChart (0 : ℚ) 1 = none := by
  norm_num [logarithmicDerivativeChart]

end PartialChart

section FiniteEulerPacket

variable {Index K : Type*} [DecidableEq Index] [Field K]

/-- A finite packet of nonzero local factors gives a nonzero multiplicative
Euler object. -/
theorem finiteEulerProduct_ne_zero
    (packet : Finset Index) (factor : Index → K)
    (hlocallyNonzero : ∀ i ∈ packet, factor i ≠ 0) :
    ∏ i ∈ packet, factor i ≠ 0 := by
  exact Finset.prod_ne_zero_iff.mpr hlocallyNonzero

theorem finiteEuler_logarithmicChart_available
    (packet : Finset Index) (factor : Index → K) (derivative : K)
    (hlocallyNonzero : ∀ i ∈ packet, factor i ≠ 0) :
    LogarithmicChartAvailable (∏ i ∈ packet, factor i) derivative := by
  apply (logarithmicChart_available_iff _ _).2
  exact finiteEulerProduct_ne_zero packet factor hlocallyNonzero

/-- Nonvanishing multiplicative data can have a vanishing additive coordinate;
the two aggregation constructors are not interchangeable. -/
theorem multiplicative_nonzero_additive_cancel_hostile :
    (1 : ℚ) * (-1) ≠ 0 ∧ (1 : ℚ) + (-1) = 0 := by
  norm_num

end FiniteEulerPacket

end MariciFormal
