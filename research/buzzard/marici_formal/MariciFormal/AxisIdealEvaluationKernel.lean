import MariciFormal.IdealVanishingSeparation

/-!
The coordinate ideal `(u,v)` is exactly the kernel of evaluation at the
origin. The reverse containment is proved from monomial support.
-/

namespace MariciFormal

open MvPolynomial

theorem axisGenerators_eq_X_image_univ :
    ({variableU, variableV} : Set TwoVariablePolynomial) =
      MvPolynomial.X '' (Set.univ : Set (Fin 2)) := by
  ext polynomial
  constructor
  · intro hpolynomial
    simp only [Set.mem_insert_iff, Set.mem_singleton_iff] at hpolynomial
    rcases hpolynomial with rfl | rfl
    · exact ⟨0, Set.mem_univ _, rfl⟩
    · exact ⟨1, Set.mem_univ _, rfl⟩
  · rintro ⟨i, _, rfl⟩
    fin_cases i <;> simp [variableU, variableV]

theorem eval_origin_eq_constantCoeff (polynomial : TwoVariablePolynomial) :
    MvPolynomial.eval origin polynomial = MvPolynomial.constantCoeff polynomial := by
  exact (MvPolynomial.eval₂Hom_eq_constantCoeff_of_vars (RingHom.id Rat)
    (p := polynomial) (fun _ _ => rfl)).trans (RingHom.id_apply _)

theorem mem_axisIdeal_of_eval_origin_eq_zero
    {polynomial : TwoVariablePolynomial}
    (heval : MvPolynomial.eval origin polynomial = 0) :
    polynomial ∈ axisIdeal := by
  rw [axisIdeal, axisGenerators_eq_X_image_univ,
    MvPolynomial.mem_ideal_span_X_image]
  intro monomial hmonomial
  have hconstant : polynomial.coeff 0 = 0 := by
    rw [← MvPolynomial.constantCoeff_eq, ← eval_origin_eq_constantCoeff]
    exact heval
  have hnonzero : polynomial.coeff monomial ≠ 0 :=
    MvPolynomial.mem_support_iff.mp hmonomial
  have hmonomial_ne_zero : monomial ≠ 0 := by
    intro hzero
    apply hnonzero
    simpa [hzero] using hconstant
  have hcoordinate : ∃ i : Fin 2, monomial i ≠ 0 := by
    by_contra hnone
    push Not at hnone
    apply hmonomial_ne_zero
    ext i
    exact hnone i
  rcases hcoordinate with ⟨i, hi⟩
  exact ⟨i, Set.mem_univ _, hi⟩

theorem axisIdeal_eq_evalOrigin_ker :
    axisIdeal = RingHom.ker (MvPolynomial.eval origin) := by
  apply le_antisymm
  · exact (axisIdeal_vanishesAt_iff_origin origin).2 rfl
  · intro polynomial hpolynomial
    apply mem_axisIdeal_of_eval_origin_eq_zero
    exact hpolynomial

end MariciFormal
