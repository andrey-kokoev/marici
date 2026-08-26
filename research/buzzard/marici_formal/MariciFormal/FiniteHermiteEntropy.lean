import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Nlinarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity

/-!
Finite information-geometric core of Grothendieck's Hermite-normalized
Newman entropy. Hermite extremality and the flow derivative are explicit
source premises, not manufactured by the definitions.
-/

namespace MariciFormal

open scoped BigOperators

section RelativeEntropy

def finiteHermiteRelativeEntropy
    (referenceDiscriminant observedDiscriminant : ℝ) : ℝ :=
  Real.log (referenceDiscriminant / observedDiscriminant)

/-- The Hermite extremal inequality implies nonnegative relative entropy. -/
theorem finiteHermiteRelativeEntropy_nonnegative
    (reference observed : ℝ) (hobserved : 0 < observed)
    (hextremal : observed ≤ reference) :
    0 ≤ finiteHermiteRelativeEntropy reference observed := by
  apply Real.log_nonneg
  exact (le_div_iff₀ hobserved).mpr hextremal

/-- Under positive discriminants, zero entropy is exactly saturation of the
Hermite extremal bound. -/
theorem finiteHermiteRelativeEntropy_eq_zero_iff
    (reference observed : ℝ) (href : 0 < reference)
    (hobserved : 0 < observed) :
    finiteHermiteRelativeEntropy reference observed = 0 ↔
      reference = observed := by
  constructor
  · intro hzero
    have hratioPos : 0 < reference / observed := div_pos href hobserved
    have hratio : reference / observed = 1 :=
      Real.eq_one_of_pos_of_log_eq_zero hratioPos hzero
    exact (div_eq_one_iff_eq hobserved.ne').mp hratio
  · intro h
    simp [finiteHermiteRelativeEntropy, h, hobserved.ne']

end RelativeEntropy

section RepulsionDissipation

variable {ι : Type*} [Fintype ι]

def centeredRepulsionDissipation (defect : ι → ℝ) : ℝ :=
  4 * ∑ i, (defect i) ^ 2

theorem centeredRepulsionDissipation_nonnegative (defect : ι → ℝ) :
    0 ≤ centeredRepulsionDissipation defect := by
  unfold centeredRepulsionDissipation
  positivity

/-- Once the source proves the derivative identity, monotonicity is the
finite sum-of-squares consequence. -/
theorem entropyDerivative_nonpositive
    (defect : ι → ℝ) (entropyDerivative : ℝ)
    (hflow : entropyDerivative = -centeredRepulsionDissipation defect) :
    entropyDerivative ≤ 0 := by
  rw [hflow]
  exact neg_nonpos.mpr (centeredRepulsionDissipation_nonnegative defect)

theorem centeredRepulsionDissipation_eq_zero_iff
    (defect : ι → ℝ) :
    centeredRepulsionDissipation defect = 0 ↔ defect = 0 := by
  classical
  constructor
  · intro hzero
    have hsum : ∑ i, (defect i) ^ 2 = 0 := by
      unfold centeredRepulsionDissipation at hzero
      linarith
    funext i
    have hle : (defect i) ^ 2 ≤ ∑ j, (defect j) ^ 2 := by
      apply Finset.single_le_sum
      · intro j hj
        exact sq_nonneg (defect j)
      · exact Finset.mem_univ i
    rw [hsum] at hle
    nlinarith [sq_nonneg (defect i)]
  · intro hzero
    subst defect
    simp [centeredRepulsionDissipation]

end RepulsionDissipation

section PremiseHostile

/-- Without the Hermite extremal inequality, the same logarithmic definition
can be negative. -/
theorem relativeEntropy_can_be_negative_without_extremality :
    finiteHermiteRelativeEntropy 1 2 < 0 := by
  change Real.log (1 / 2 : ℝ) < 0
  exact Real.log_neg (by norm_num) (by norm_num)

end PremiseHostile

end MariciFormal
