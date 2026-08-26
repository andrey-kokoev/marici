import Mathlib

/-!
Exact finite algebra behind the endpoint-reduced Pick target.

No digamma, zeta, analytic continuation, or global Pick assertion occurs in
this file.  The spectral formula is conditional on explicitly supplied finite
weights and squared coordinates.
-/

namespace MariciFormal

section EndpointReduction

variable {K : Type*} [Field K] [CharZero K]

/-- The two completed endpoint poles collapse to the constant four. -/
theorem reducedEndpointPair_eq_four
    (s : K) (hs : s ≠ 0) (hs1 : s - 1 ≠ 0) (hcenter : 2 * s - 1 ≠ 0) :
    4 * s * (s - 1) / (2 * s - 1) * (1 / s + 1 / (s - 1)) = 4 := by
  field_simp
  ring

end EndpointReduction

section FiniteResolvent

variable {K : Type*} [Field K] [CharZero K]
variable {I : Type*} [Fintype I]

/-- Finite conditional endpoint-reduced source built from squared spectral
coordinates. -/
def finiteReducedPickSource (weight coordinate : I → K) (t : K) : K :=
  4 * ∑ i, weight i -
    ∑ i, weight i * (1 + 4 * coordinate i) / (t + coordinate i)

/-- Its divided difference is the expected finite rank-one resolvent kernel. -/
theorem finiteReducedPickSource_dividedDifference
    (weight coordinate : I → K) (x y : K) (hxy : y - x ≠ 0)
    (hx : ∀ i, x + coordinate i ≠ 0)
    (hy : ∀ i, y + coordinate i ≠ 0) :
    (finiteReducedPickSource weight coordinate y -
        finiteReducedPickSource weight coordinate x) / (y - x) =
      ∑ i, weight i * (1 + 4 * coordinate i) /
        ((x + coordinate i) * (y + coordinate i)) := by
  rw [show finiteReducedPickSource weight coordinate y -
      finiteReducedPickSource weight coordinate x =
      ∑ i, (weight i * (1 + 4 * coordinate i) / (x + coordinate i) -
        weight i * (1 + 4 * coordinate i) / (y + coordinate i)) by
    simp only [finiteReducedPickSource, Finset.sum_sub_distrib]
    ring]
  rw [Finset.sum_div]
  apply Finset.sum_congr rfl
  intro i hi
  field_simp [hxy, hx i, hy i]
  ring

end FiniteResolvent

end MariciFormal
