import MariciFormal.ProfileSeparationLocus

/-!
The rational separation locus of the fixture is typed as the pointwise
vanishing locus of its nonprincipal first determinantal ideal.
-/

namespace MariciFormal

/-- Every polynomial in an ideal evaluates to zero at the given rational
point. This is a pointwise predicate, not a scheme-theoretic support object. -/
def idealVanishesAt (ideal : Ideal TwoVariablePolynomial)
    (point : Fin 2 → Rat) : Prop :=
  ideal ≤ RingHom.ker (MvPolynomial.eval point)

theorem axisIdeal_vanishesAt_iff_origin (point : Fin 2 → Rat) :
    idealVanishesAt axisIdeal point ↔ point = origin := by
  constructor
  · intro hvanishes
    have hu := hvanishes (Ideal.subset_span
      (show variableU ∈ ({variableU, variableV} : Set TwoVariablePolynomial)
        by simp))
    have hv := hvanishes (Ideal.subset_span
      (show variableV ∈ ({variableU, variableV} : Set TwoVariablePolynomial)
        by simp))
    change MvPolynomial.eval point variableU = 0 at hu
    change MvPolynomial.eval point variableV = 0 at hv
    have h0 : point 0 = 0 := by simpa [variableU] using hu
    have h1 : point 1 = 0 := by simpa [variableV] using hv
    funext i
    fin_cases i <;> simp [origin, h0, h1]
  · rintro rfl
    rw [idealVanishesAt, axisIdeal, Ideal.span_le]
    intro polynomial hpolynomial
    simp only [Set.mem_insert_iff, Set.mem_singleton_iff] at hpolynomial
    rcases hpolynomial with rfl | rfl <;>
      change MvPolynomial.eval origin _ = 0 <;>
      simp [variableU, variableV, origin]

/-- For the frozen fixture, profile separation is exactly vanishing of the
first determinantal ideal of `diag(u,v)`. -/
theorem specialized_profiles_differ_iff_axisIdeal_vanishes
    (point : Fin 2 → Rat) :
    specializedProfile point separateAxisMatrix ≠
        specializedProfile point productAxisMatrix ↔
      idealVanishesAt axisIdeal point := by
  rw [specialized_profiles_differ_iff_origin,
    axisIdeal_vanishesAt_iff_origin]

end MariciFormal
