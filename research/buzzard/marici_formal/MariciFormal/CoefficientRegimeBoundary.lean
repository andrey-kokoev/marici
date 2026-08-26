import MariciFormal.NonprincipalAxisIdeal

/-!
Principal-ideal normalization is available over `Q[X]` but unavailable over
the concrete two-variable coefficient ring `Q[u,v]`.
-/

namespace MariciFormal

/-- Mathlib supplies principal generators for every ideal of `Q[X]`. -/
theorem univariateRat_isPrincipalIdealRing :
    IsPrincipalIdealRing (Polynomial Rat) := by
  infer_instance

/-- The nonprincipal coordinate ideal prevents any principal-ideal-ring
structure on `Q[u,v]`. -/
theorem bivariateRat_not_isPrincipalIdealRing :
    ¬ IsPrincipalIdealRing TwoVariablePolynomial := by
  intro hprincipal
  exact axisIdeal_not_isPrincipal (hprincipal.principal axisIdeal)

/-- A principal-ideal interface cannot be transported merely because both
coefficient rings are polynomial rings over the rationals. -/
theorem polynomialVariableCount_changesPrincipalIdealInterface :
    IsPrincipalIdealRing (Polynomial Rat) ∧
      ¬ IsPrincipalIdealRing TwoVariablePolynomial :=
  ⟨univariateRat_isPrincipalIdealRing, bivariateRat_not_isPrincipalIdealRing⟩

end MariciFormal
