import MariciFormal.PrimePrincipalIndependence

/-!
The coordinate ideal `(u,v)` has an explicit two-element generating family and
no one-element indexed generating family.
-/

namespace MariciFormal

noncomputable def axisGeneratorFamily : Fin 2 → TwoVariablePolynomial :=
  ![variableU, variableV]

theorem range_axisGeneratorFamily :
    Set.range axisGeneratorFamily =
      ({variableU, variableV} : Set TwoVariablePolynomial) := by
  ext polynomial
  constructor
  · rintro ⟨i, rfl⟩
    fin_cases i <;> simp [axisGeneratorFamily]
  · intro hpolynomial
    simp only [Set.mem_insert_iff, Set.mem_singleton_iff] at hpolynomial
    rcases hpolynomial with rfl | rfl
    · exact ⟨0, by simp [axisGeneratorFamily]⟩
    · exact ⟨1, by simp [axisGeneratorFamily]⟩

theorem axisIdeal_generated_by_two :
    axisIdeal = Ideal.span (Set.range axisGeneratorFamily) := by
  rw [axisIdeal, range_axisGeneratorFamily]

theorem range_fin_one_eq_singleton
    (family : Fin 1 → TwoVariablePolynomial) :
    Set.range family = ({family 0} : Set TwoVariablePolynomial) := by
  ext polynomial
  constructor
  · rintro ⟨i, rfl⟩
    fin_cases i
    simp
  · intro hpolynomial
    simp only [Set.mem_singleton_iff] at hpolynomial
    exact ⟨0, hpolynomial.symm⟩

theorem axisIdeal_not_generated_by_one :
    ¬ ∃ family : Fin 1 → TwoVariablePolynomial,
      axisIdeal = Ideal.span (Set.range family) := by
  rintro ⟨family, hfamily⟩
  apply axisIdeal_not_principal
  rw [range_fin_one_eq_singleton family] at hfamily
  exact ⟨family 0, hfamily⟩

/-- The concrete coordinate ideal needs two displayed generators in the exact
sense that two suffice and one cannot suffice. -/
theorem axisIdeal_exact_generator_arity_two :
    axisIdeal = Ideal.span (Set.range axisGeneratorFamily) ∧
      ¬ ∃ family : Fin 1 → TwoVariablePolynomial,
        axisIdeal = Ideal.span (Set.range family) :=
  ⟨axisIdeal_generated_by_two, axisIdeal_not_generated_by_one⟩

end MariciFormal
