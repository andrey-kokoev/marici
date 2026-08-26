import MariciFormal.AxisIdealQuotient

/-!
Prime/maximal locus information and principal-generator information are
independent interfaces, even inside the single ring `Q[u,v]`.
-/

namespace MariciFormal

theorem axisIdeal_maximal_prime_nonprincipal :
    axisIdeal.IsMaximal ∧ axisIdeal.IsPrime ∧
      ¬ Submodule.IsPrincipal (axisIdeal : Submodule TwoVariablePolynomial
        TwoVariablePolynomial) :=
  ⟨axisIdeal_isMaximal, axisIdeal_isPrime, axisIdeal_not_isPrincipal⟩

theorem topIdeal_principal_not_maximal :
    Submodule.IsPrincipal
        ((⊤ : Ideal TwoVariablePolynomial) :
          Submodule TwoVariablePolynomial TwoVariablePolynomial) ∧
      ¬ (⊤ : Ideal TwoVariablePolynomial).IsMaximal := by
  constructor
  · exact ⟨1, by simp⟩
  · intro hmaximal
    exact hmaximal.ne_top rfl

/-- Maximality does not imply principality, and principality does not imply
maximality, over the concrete bivariate coefficient ring. -/
theorem maximality_and_principality_are_independent :
    (∃ ideal : Ideal TwoVariablePolynomial,
        ideal.IsMaximal ∧
          ¬ Submodule.IsPrincipal
            (ideal : Submodule TwoVariablePolynomial TwoVariablePolynomial)) ∧
      (∃ ideal : Ideal TwoVariablePolynomial,
        Submodule.IsPrincipal
            (ideal : Submodule TwoVariablePolynomial TwoVariablePolynomial) ∧
          ¬ ideal.IsMaximal) :=
  ⟨⟨axisIdeal, axisIdeal_isMaximal, axisIdeal_not_isPrincipal⟩,
    ⟨⊤, topIdeal_principal_not_maximal⟩⟩

theorem separateAxis_firstIdeal_maximal_nonprincipal :
    (firstDeterminantalIdeal separateAxisMatrix).IsMaximal ∧
      ¬ Submodule.IsPrincipal
        (firstDeterminantalIdeal separateAxisMatrix :
          Submodule TwoVariablePolynomial TwoVariablePolynomial) := by
  rw [separateAxis_firstDeterminantalIdeal_eq_axisIdeal]
  exact ⟨axisIdeal_isMaximal, axisIdeal_not_isPrincipal⟩

end MariciFormal
