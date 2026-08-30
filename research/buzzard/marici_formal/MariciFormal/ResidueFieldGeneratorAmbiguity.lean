import MariciFormal.AxisIdealGeneratorArity
import Mathlib.RingTheory.Polynomial.Ideal

/-!
Two ideals can have isomorphic residue fields while requiring different
numbers of generators.  This is a hostile example against recovering local
generator arity from the residue quotient alone.
-/

namespace MariciFormal

open Polynomial

abbrev UnivariatePolynomial := Polynomial Rat

/-- The origin ideal `(X)` in the univariate polynomial ring `Q[X]`. -/
noncomputable def univariateOriginIdeal : Ideal UnivariatePolynomial :=
  Ideal.span ({Polynomial.X} : Set UnivariatePolynomial)

theorem univariateOriginIdeal_eq_constantCoeff_ker :
    univariateOriginIdeal = RingHom.ker Polynomial.constantCoeff := by
  exact Polynomial.ker_constantCoeff.symm

/-- The univariate origin quotient has residue field `Q`. -/
noncomputable def univariateOriginQuotientEquivRat :
    (UnivariatePolynomial ⧸ univariateOriginIdeal) ≃+* Rat :=
  (Ideal.quotEquivOfEq univariateOriginIdeal_eq_constantCoeff_ker).trans
    (RingHom.quotientKerEquivOfSurjective Polynomial.constantCoeff_surjective)

theorem univariateOriginIdeal_isMaximal : univariateOriginIdeal.IsMaximal := by
  apply Ideal.Quotient.maximal_of_isField univariateOriginIdeal
  exact univariateOriginQuotientEquivRat.toMulEquiv.isField (Field.toIsField Rat)

theorem univariateOriginIdeal_isPrincipal :
    Submodule.IsPrincipal
      (univariateOriginIdeal : Submodule UnivariatePolynomial UnivariatePolynomial) := by
  rw [univariateOriginIdeal]
  infer_instance

/-- Equal rational residue fields do not determine generator arity: `(X)` is
principal, whereas `(u,v)` is not, although both ideals are maximal and both
quotients are explicitly equivalent to `Q`. -/
theorem rationalResidueField_does_not_determine_principality :
    univariateOriginIdeal.IsMaximal ∧
      axisIdeal.IsMaximal ∧
      Submodule.IsPrincipal
        (univariateOriginIdeal : Submodule UnivariatePolynomial UnivariatePolynomial) ∧
      ¬ Submodule.IsPrincipal
        (axisIdeal : Submodule TwoVariablePolynomial TwoVariablePolynomial) := by
  exact ⟨univariateOriginIdeal_isMaximal, axisIdeal_isMaximal,
    univariateOriginIdeal_isPrincipal, axisIdeal_not_isPrincipal⟩

end MariciFormal
