import Mathlib.Analysis.InnerProductSpace.Basic

/-!
Finite pullback-metric core of Grothendieck's divisor-incidence construction.

An incidence pushforward is an isometry for the metric pulled back through a
specified left inverse.  No infinite Euler tensor product, prime-shell limit,
or physical relative-chain identification is assumed.
-/

namespace MariciFormal

open scoped RealInnerProductSpace

variable {V : Type*} [SeminormedAddCommGroup V] [InnerProductSpace ℝ V]

/-- The target bilinear form obtained by measuring potentials after applying
the declared inverse incidence map. -/
def incidencePullbackInner (inverse : V →ₗ[ℝ] V) (x y : V) : ℝ :=
  ⟪inverse x, inverse y⟫_ℝ

theorem incidencePullbackInner_nonnegative
    (inverse : V →ₗ[ℝ] V) (x : V) :
    0 ≤ incidencePullbackInner inverse x x := by
  exact real_inner_self_nonneg

/-- A declared left inverse makes the forward incidence map exactly isometric
from the original inner product to the pullback target metric. -/
theorem incidence_pushforward_isometry
    (forward inverse : V →ₗ[ℝ] V)
    (hleft : inverse.comp forward = LinearMap.id)
    (x y : V) :
    incidencePullbackInner inverse (forward x) (forward y) = ⟪x, y⟫_ℝ := by
  have hx := LinearMap.congr_fun hleft x
  have hy := LinearMap.congr_fun hleft y
  simp only [LinearMap.comp_apply, LinearMap.id_apply] at hx hy
  simp [incidencePullbackInner, hx, hy]

/-- Positivity of a pullback form alone does not make the forward map
information-preserving: the zero candidate inverse collapses nonzero energy. -/
theorem missing_leftInverse_collapses_metric_hostile :
    incidencePullbackInner (0 : ℝ →ₗ[ℝ] ℝ) 1 1 = 0 ∧
      ⟪(1 : ℝ), (1 : ℝ)⟫_ℝ = 1 := by
  norm_num [incidencePullbackInner]

end MariciFormal
