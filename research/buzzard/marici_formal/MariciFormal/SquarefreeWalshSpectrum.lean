import MariciFormal.AdditivePrimeEdgeBudget
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Tactic

/-!
Finite character and tensor-factorization core of Grothendieck's squarefree
prime-cube Walsh packet. Fourier completeness and source descent are explicit
external interfaces.
-/

namespace MariciFormal

open scoped BigOperators

section FiniteConvolution

variable {G : Type*} [Fintype G] [AddCommGroup G]

/-- Minimal real character interface needed by the finite convolution proof. -/
structure RealAddCharacter (G : Type*) [AddCommGroup G] where
  toFun : G → ℝ
  map_zero : toFun 0 = 1
  map_add : ∀ x y, toFun (x + y) = toFun x * toFun y
  map_neg : ∀ x, toFun (-x) = toFun x

instance : CoeFun (RealAddCharacter G) (fun _ => G → ℝ) :=
  ⟨RealAddCharacter.toFun⟩

theorem RealAddCharacter.map_sub (character : RealAddCharacter G) (x y : G) :
    character (x - y) = character x * character y := by
  rw [sub_eq_add_neg, character.map_add, character.map_neg]

def finiteConvolution (kernel vector : G → ℝ) (x : G) : ℝ :=
  ∑ y, kernel y * vector (x - y)

def characterEigenvalue
    (kernel : G → ℝ) (character : RealAddCharacter G) : ℝ :=
  ∑ y, kernel y * character y

/-- Every exponent-two real character is an eigenvector of finite convolution. -/
theorem finiteConvolution_apply_character
    (kernel : G → ℝ) (character : RealAddCharacter G) (x : G) :
    finiteConvolution kernel character x =
      characterEigenvalue kernel character * character x := by
  unfold finiteConvolution characterEigenvalue
  calc
    (∑ y, kernel y * character (x - y)) =
        ∑ y, character x * (kernel y * character y) := by
      apply Finset.sum_congr rfl
      intro y hy
      rw [character.map_sub]
      ring
    _ = character x * ∑ y, kernel y * character y := by
      rw [Finset.mul_sum]
    _ = (∑ y, kernel y * character y) * character x := by ring

end FiniteConvolution

section TensorWalsh

variable {ι : Type*} [Fintype ι]

/-- Walsh coefficient of the tensor kernel, represented as a sum over all
squarefree subsets. -/
def tensorWalshCoefficient
    (coefficient : ι → ℝ) (polarity : ι → Bool) : ℝ :=
  ∑ subset ∈ (Finset.univ : Finset ι).powerset,
    ∏ i ∈ subset, signedEdge (coefficient i) (polarity i)

/-- Exact Mackey tensor interchange factors every Walsh coefficient. -/
theorem tensorWalshCoefficient_factorization
    (coefficient : ι → ℝ) (polarity : ι → Bool) :
    tensorWalshCoefficient coefficient polarity =
      ∏ i, (1 + signedEdge (coefficient i) (polarity i)) := by
  unfold tensorWalshCoefficient
  rw [Finset.prod_one_add]

theorem one_add_signedEdge_nonnegative
    (coefficient : ℝ) (polarity : Bool) (hbound : |coefficient| ≤ 1) :
    0 ≤ 1 + signedEdge coefficient polarity := by
  cases polarity
  · change 0 ≤ 1 + coefficient
    linarith [neg_abs_le coefficient]
  · change 0 ≤ 1 + -coefficient
    linarith [le_abs_self coefficient]

/-- Individual contraction bounds suffice in the exact tensor branch because
every factored Walsh eigenvalue is a product of nonnegative factors. -/
theorem tensorWalshCoefficient_nonnegative
    (coefficient : ι → ℝ) (polarity : ι → Bool)
    (hbound : ∀ i, |coefficient i| ≤ 1) :
    0 ≤ tensorWalshCoefficient coefficient polarity := by
  rw [tensorWalshCoefficient_factorization]
  exact Finset.prod_nonneg fun i hi =>
    one_add_signedEdge_nonnegative (coefficient i) (polarity i) (hbound i)

end TensorWalsh

end MariciFormal
