import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic

/-!
Finite algebraic core of Grothendieck's Adams-doubling shell-channel packet.
Complex prime powers, analytic continuation, and mapping cones are not
constructed here.
-/

namespace MariciFormal

open scoped BigOperators

variable {K ι S : Type*} [Field K] [Fintype ι]

/-- Finite linear channel before any completion or continuation. -/
def finiteLinearChannel (amplitude : ι → S → K) (parameter : S) : K :=
  ∑ label, amplitude label parameter

/-- Quadratic determinant-log channel with its forced orbit factor. -/
def finiteQuadraticChannel (amplitude : ι → S → K) (parameter : S) : K :=
  (2 : K)⁻¹ * ∑ label, (amplitude label parameter) ^ 2

/-- A parameter map realizes the second Adams operation on the finite source
when every labelled amplitude is squared after pullback. -/
def RealizesSecondAdams
    (double : S → S) (amplitude : ι → S → K) : Prop :=
  ∀ parameter label,
    amplitude label (double parameter) = (amplitude label parameter) ^ 2

/-- Exact finite identity `C₂(s) = (1/2) C₁(2s)` under the explicitly
typed second-Adams amplitude law. -/
theorem finiteQuadraticChannel_eq_half_linearChannel_double
    (double : S → S) (amplitude : ι → S → K)
    (hadams : RealizesSecondAdams double amplitude) (parameter : S) :
    finiteQuadraticChannel amplitude parameter =
      (2 : K)⁻¹ * finiteLinearChannel amplitude (double parameter) := by
  unfold finiteQuadraticChannel finiteLinearChannel
  apply congrArg ((2 : K)⁻¹ * ·)
  apply Finset.sum_congr rfl
  intro label _
  exact (hadams parameter label).symm

/-- Coordinate-free finite vector form of the same identity. -/
theorem finiteQuadraticChannel_eq_half_linear_squares
    (source : ι → K) :
    (2 : K)⁻¹ * ∑ label, (source label) ^ 2 =
      (2 : K)⁻¹ * ∑ label, (fun i ⇒ (source i) ^ 2) label := by
  rfl

/-- Omitting the determinant-log factor changes even the one-label rational
channel. -/
theorem omitted_half_factor_hostile :
    let source : Fin 1 → ℚ := fun _ ⇒ 1
    (∑ label, (source label) ^ 2) ≠
      (2 : ℚ)⁻¹ * ∑ label, (source label) ^ 2 := by
  norm_num

/-- Coupling the quadratic channel to the undoubled linear source is also
wrong in general. -/
theorem omitted_secondAdams_map_hostile :
    let source : Fin 1 → ℚ := fun _ ⇒ 2
    (2 : ℚ)⁻¹ * ∑ label, (source label) ^ 2 ≠
      (2 : ℚ)⁻¹ * ∑ label, source label := by
  norm_num

end MariciFormal
