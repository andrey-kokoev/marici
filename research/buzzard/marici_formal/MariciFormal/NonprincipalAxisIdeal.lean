import MariciFormal.EntryIdealPresentation

/-!
The coordinate ideal `(u,v)` in `Q[u,v]` is not principal. This supplies the
coefficient-ring obstruction that prevents a Smith-factor treatment.
-/

namespace MariciFormal

open MvPolynomial

noncomputable def axisIdeal : Ideal TwoVariablePolynomial :=
  Ideal.span ({variableU, variableV} : Set TwoVariablePolynomial)

theorem axisIdeal_ne_top : axisIdeal ≠ ⊤ := by
  let atOrigin : TwoVariablePolynomial →+* Rat := MvPolynomial.eval origin
  have hle : axisIdeal ≤ Ideal.comap atOrigin ⊥ := by
    rw [axisIdeal, Ideal.span_le]
    intro polynomial hpolynomial
    simp only [Set.mem_insert_iff, Set.mem_singleton_iff] at hpolynomial
    rcases hpolynomial with rfl | rfl <;>
      change atOrigin _ = 0 <;>
      norm_num [atOrigin, variableU, variableV, origin]
  intro htop
  have hone : (1 : TwoVariablePolynomial) ∈ Ideal.comap atOrigin ⊥ :=
    hle (by simp [htop])
  simp [atOrigin] at hone

def uZeroVOne : Fin 2 → Rat
  | 0 => 0
  | 1 => 1

theorem variableU_not_dvd_variableV : ¬ variableU ∣ variableV := by
  rintro ⟨factor, hfactor⟩
  have heval := congrArg (MvPolynomial.eval uZeroVOne) hfactor
  norm_num [variableU, variableV, uZeroVOne] at heval

/-- The concrete coordinate ideal `(u,v)` in `Q[u,v]` has no singleton
generator. -/
theorem axisIdeal_not_principal :
    ¬ ∃ generator : TwoVariablePolynomial,
      axisIdeal = Ideal.span ({generator} : Set TwoVariablePolynomial) := by
  rintro ⟨generator, hgenerator⟩
  have hgu : generator ∣ variableU := by
    rw [← Ideal.mem_span_singleton, ← hgenerator]
    exact Ideal.subset_span (by simp)
  have hgv : generator ∣ variableV := by
    rw [← Ideal.mem_span_singleton, ← hgenerator]
    exact Ideal.subset_span (by simp)
  have hnonunit : ¬ IsUnit generator := by
    intro hunit
    apply axisIdeal_ne_top
    rw [hgenerator, Ideal.eq_top_iff_one, Ideal.mem_span_singleton]
    exact hunit.dvd
  have hassociated : Associated variableU generator :=
    ((MvPolynomial.X_prime (R := Rat) (i := (0 : Fin 2))).irreducible.dvd_iff.mp hgu).resolve_left
      hnonunit
  exact variableU_not_dvd_variableV (hassociated.dvd.trans hgv)

theorem axisIdeal_not_isPrincipal :
    ¬ Submodule.IsPrincipal (axisIdeal : Submodule TwoVariablePolynomial
      TwoVariablePolynomial) := by
  intro hprincipal
  rcases hprincipal.principal with ⟨generator, hgenerator⟩
  exact axisIdeal_not_principal ⟨generator, hgenerator⟩

theorem separateAxis_firstDeterminantalIdeal_eq_axisIdeal :
    firstDeterminantalIdeal separateAxisMatrix = axisIdeal := by
  apply le_antisymm
  · rw [firstDeterminantalIdeal, axisIdeal, Ideal.span_le]
    rintro _ ⟨⟨i, j⟩, rfl⟩
    fin_cases i <;> fin_cases j
    · exact Ideal.subset_span (by simp [separateAxisMatrix, variableU])
    · simp [separateAxisMatrix]
    · simp [separateAxisMatrix]
    · exact Ideal.subset_span (by simp [separateAxisMatrix, variableV])
  · rw [axisIdeal, Ideal.span_le]
    intro polynomial hpolynomial
    simp only [Set.mem_insert_iff, Set.mem_singleton_iff] at hpolynomial
    rcases hpolynomial with rfl | rfl
    · apply Ideal.subset_span
      exact ⟨(0, 0), by simp [separateAxisMatrix, variableU]⟩
    · apply Ideal.subset_span
      exact ⟨(1, 1), by simp [separateAxisMatrix, variableV]⟩

end MariciFormal
