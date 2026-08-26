import Mathlib.Tactic

/-!
Finite valuation and exponent core of Grothendieck's square-current and
quarter-density audit. Prime factorization and Hilbert realization are external.
-/

namespace MariciFormal

section ValuationFiltration

/-- Primitive exclusion contributes one exactly at valuation zero. -/
def primitiveBoundaryMultiplicity (valuation : ℕ) : ℕ :=
  if valuation = 0 then 1 else 0

def valuationDegreeMultiplicity (valuation : ℕ) : ℕ := valuation

/-- Remove the universal identity line after adding primitive boundary and
valuation degree. -/
def renormalizedValuationMultiplicity (valuation : ℕ) : ℕ :=
  primitiveBoundaryMultiplicity valuation +
    valuationDegreeMultiplicity valuation - 1

/-- The square-and-higher current counts valuation depth beyond the primitive
layer. -/
def squareCurrentMultiplicity (valuation : ℕ) : ℕ := valuation - 1

theorem boundary_plus_degree_is_gapped (valuation : ℕ) :
    1 ≤ primitiveBoundaryMultiplicity valuation +
      valuationDegreeMultiplicity valuation := by
  cases valuation <;> simp [primitiveBoundaryMultiplicity,
    valuationDegreeMultiplicity]

/-- Primitive boundary plus valuation degree, after subtracting the universal
line, is exactly the square-and-higher multiplicity. -/
theorem renormalized_eq_squareCurrent (valuation : ℕ) :
    renormalizedValuationMultiplicity valuation =
      squareCurrentMultiplicity valuation := by
  cases valuation <;> simp [renormalizedValuationMultiplicity,
    primitiveBoundaryMultiplicity, valuationDegreeMultiplicity,
    squareCurrentMultiplicity]

theorem squareCurrent_kernel_iff_squarefreeLocal (valuation : ℕ) :
    squareCurrentMultiplicity valuation = 0 ↔ valuation ≤ 1 := by
  simp [squareCurrentMultiplicity]

/-- A nonvacuum squarefree label remains in the local square-current kernel. -/
theorem squarefree_nonfaithful_hostile :
    (1 : ℕ) ≠ 0 ∧ squareCurrentMultiplicity 1 = 0 := by
  norm_num [squareCurrentMultiplicity]

end ValuationFiltration

section QuarterDensity

def quadraticTransportExponent (alpha : ℚ) (depth : ℕ) : ℚ :=
  2 * alpha * depth

def halfDensityStaircaseExponent (depth : ℕ) : ℚ :=
  (1 / 2) * depth

/-- Matching the linear half-density staircase at every depth uniquely forces
quarter-density transport before squaring. -/
theorem allDepth_matching_iff_quarterDensity (alpha : ℚ) :
    (∀ depth : ℕ,
      quadraticTransportExponent alpha depth =
        halfDensityStaircaseExponent depth) ↔
      alpha = 1 / 4 := by
  constructor
  · intro hall
    have h := hall 1
    norm_num [quadraticTransportExponent,
      halfDensityStaircaseExponent] at h ⊢
    linarith
  · intro halpha depth
    subst alpha
    change 2 * (1 / 4 : ℚ) * (depth : ℚ) =
      (1 / 2 : ℚ) * (depth : ℚ)
    ring

/-- Putting half-density directly on transport already misses the required
depth-two exponent. -/
theorem naiveHalfDensity_depthTwo_hostile :
    quadraticTransportExponent (1 / 2) 2 ≠
      halfDensityStaircaseExponent 2 := by
  norm_num [quadraticTransportExponent, halfDensityStaircaseExponent]

end QuarterDensity

end MariciFormal
