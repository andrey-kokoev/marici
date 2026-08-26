import Mathlib.Data.Real.Basic
import Mathlib.Tactic

/-!
Real scalar parity core of Grothendieck's mixed-prime rectangle theorem.
Complex and operator-valued correlations require separate adjoint interfaces.
-/

namespace MariciFormal

/-- Quadratic form of a real symmetric two-by-two block. -/
def symmetricBlockEnergy (a b t x y : ℝ) : ℝ :=
  a * x ^ 2 + 2 * t * x * y + b * y ^ 2

/-- Quadratic form of the normalized four-vertex mixed-prime rectangle. -/
def mixedPrimeRectangleEnergy
    (r s c d x₀ x₁ x₂ x₃ : ℝ) : ℝ :=
  x₀ ^ 2 + x₁ ^ 2 + x₂ ^ 2 + x₃ ^ 2 +
    2 * r * (x₀ * x₁ + x₂ * x₃) +
    2 * s * (x₀ * x₂ + x₁ * x₃) +
    2 * c * x₀ * x₃ + 2 * d * x₁ * x₂

def evenRectangleEnergy (r s c d x y : ℝ) : ℝ :=
  symmetricBlockEnergy (1 + c) (1 + d) (r + s) x y

def oddRectangleEnergy (r s c d x y : ℝ) : ℝ :=
  symmetricBlockEnergy (1 - c) (1 - d) (r - s) x y

/-- Opposite-vertex sums and differences split twice the rectangle energy
into its even and odd parity blocks. -/
theorem mixedPrimeRectangle_parity_decomposition
    (r s c d x₀ x₁ x₂ x₃ : ℝ) :
    2 * mixedPrimeRectangleEnergy r s c d x₀ x₁ x₂ x₃ =
      evenRectangleEnergy r s c d (x₀ + x₃) (x₁ + x₂) +
      oddRectangleEnergy r s c d (x₀ - x₃) (x₁ - x₂) := by
  ring

/-- Rectangle positivity is exactly positivity of both parity blocks. -/
theorem mixedPrimeRectangle_nonnegative_iff_parity
    (r s c d : ℝ) :
    (∀ x₀ x₁ x₂ x₃ : ℝ,
        0 ≤ mixedPrimeRectangleEnergy r s c d x₀ x₁ x₂ x₃) ↔
      (∀ x y : ℝ, 0 ≤ evenRectangleEnergy r s c d x y) ∧
      (∀ x y : ℝ, 0 ≤ oddRectangleEnergy r s c d x y) := by
  constructor
  · intro hrectangle
    constructor
    · intro x y
      have h := hrectangle (x / 2) (y / 2) (y / 2) (x / 2)
      have hdecomp :=
        mixedPrimeRectangle_parity_decomposition r s c d
          (x / 2) (y / 2) (y / 2) (x / 2)
      simp [oddRectangleEnergy, symmetricBlockEnergy] at hdecomp
      nlinarith
    · intro x y
      have h := hrectangle (x / 2) (y / 2) (-y / 2) (-x / 2)
      have hdecomp :=
        mixedPrimeRectangle_parity_decomposition r s c d
          (x / 2) (y / 2) (-y / 2) (-x / 2)
      simp [evenRectangleEnergy, symmetricBlockEnergy] at hdecomp
      nlinarith
  · rintro ⟨heven, hodd⟩ x₀ x₁ x₂ x₃
    have he := heven (x₀ + x₃) (x₁ + x₂)
    have ho := hodd (x₀ - x₃) (x₁ - x₂)
    have hdecomp :=
      mixedPrimeRectangle_parity_decomposition r s c d x₀ x₁ x₂ x₃
    nlinarith

/-- Under exact tensor interchange `c = d = r*s`, both parity determinants
are the same product of the two individual contraction defects. -/
theorem exactTensor_even_parity_determinant (r s : ℝ) :
    (1 + r * s) * (1 + r * s) - (r + s) ^ 2 =
      (1 - r ^ 2) * (1 - s ^ 2) := by
  ring

theorem exactTensor_odd_parity_determinant (r s : ℝ) :
    (1 - r * s) * (1 - r * s) - (r - s) ^ 2 =
      (1 - r ^ 2) * (1 - s ^ 2) := by
  ring

/-- Individual edge bounds do not imply rectangle positivity. -/
theorem mixedPrimeRectangle_individual_bounds_hostile :
    |(3 / 5 : ℝ)| ≤ 1 ∧ |(3 / 5 : ℝ)| ≤ 1 ∧
      |(0 : ℝ)| ≤ 1 ∧ |(0 : ℝ)| ≤ 1 ∧
      evenRectangleEnergy (3 / 5) (3 / 5) 0 0 1 (-1) < 0 := by
  norm_num [evenRectangleEnergy, symmetricBlockEnergy]

end MariciFormal
