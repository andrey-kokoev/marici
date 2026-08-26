import MariciFormal.AxisIdealEvaluationKernel

/-!
Evaluation at the origin identifies `Q[u,v]/(u,v)` with `Q`. Maximality of
the coordinate ideal is derived from this quotient equivalence.
-/

namespace MariciFormal

theorem evalOrigin_surjective :
    Function.Surjective (MvPolynomial.eval origin :
      TwoVariablePolynomial → Rat) := by
  intro coefficient
  exact ⟨MvPolynomial.C coefficient, by simp⟩

/-- Evaluation at the origin descended directly to the coordinate quotient. -/
noncomputable def axisEvalLift : (TwoVariablePolynomial ⧸ axisIdeal) →+* Rat :=
  Ideal.Quotient.lift axisIdeal (MvPolynomial.eval origin) fun polynomial hpolynomial => by
    rw [← RingHom.mem_ker, ← axisIdeal_eq_evalOrigin_ker]
    exact hpolynomial

theorem axisEvalLift_injective : Function.Injective axisEvalLift := by
  apply RingHom.lift_injective_of_ker_le_ideal axisIdeal
  rw [← axisIdeal_eq_evalOrigin_ker]

theorem axisEvalLift_surjective : Function.Surjective axisEvalLift := by
  intro coefficient
  exact ⟨Ideal.Quotient.mk axisIdeal (MvPolynomial.C coefficient), by
    simp [axisEvalLift]⟩

/-- The first-isomorphism equivalence implemented directly on the axis-ideal
quotient, so it computes on representatives without equality transport. -/
noncomputable def axisIdealQuotientEquivRat :
    (TwoVariablePolynomial ⧸ axisIdeal) ≃+* Rat :=
  RingEquiv.ofBijective axisEvalLift
    ⟨axisEvalLift_injective, axisEvalLift_surjective⟩

@[simp]
theorem axisIdealQuotientEquivRat_apply_mk
    (polynomial : TwoVariablePolynomial) :
    axisIdealQuotientEquivRat (Ideal.Quotient.mk axisIdeal polynomial) =
      MvPolynomial.eval origin polynomial := by
  rfl

theorem axisIdeal_isMaximal : axisIdeal.IsMaximal := by
  apply Ideal.Quotient.maximal_of_isField axisIdeal
  exact axisIdealQuotientEquivRat.toMulEquiv.isField (Field.toIsField Rat)

theorem axisIdeal_isPrime : axisIdeal.IsPrime :=
  axisIdeal_isMaximal.isPrime

end MariciFormal
