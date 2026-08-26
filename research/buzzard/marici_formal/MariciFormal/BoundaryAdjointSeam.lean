import Mathlib.Data.Complex.Basic
import Mathlib.Tactic.NormNum

/-!
Infinitesimal algebraic core of Grothendieck's boundary-cocycle adjointness
criterion.  The continuous boundary family and its differentiability are not
constructed here.
-/

namespace MariciFormal

open Complex

def reciprocalBoundaryGenerator (z : ℂ) : ℂ :=
  -I * z

def adjointBoundaryGenerator (z : ℂ) : ℂ :=
  -I * conj z

def InfinitesimallyStarCompatible (z : ℂ) : Prop :=
  reciprocalBoundaryGenerator z = adjointBoundaryGenerator z

/-- Equality of the reciprocal and adjoint infinitesimal boundary phases is
equivalent to lying on the real spectral seam. -/
theorem infinitesimal_starCompatible_iff_im_eq_zero (z : ℂ) :
    InfinitesimallyStarCompatible z ↔ z.im = 0 := by
  constructor
  · intro h
    have hre := congrArg Complex.re h
    simp [InfinitesimallyStarCompatible, reciprocalBoundaryGenerator,
      adjointBoundaryGenerator] at hre
    linarith
  · intro him
    simp [InfinitesimallyStarCompatible, reciprocalBoundaryGenerator,
      adjointBoundaryGenerator, Complex.ext_iff, him]

theorem infinitesimal_starCompatible_of_real (x : ℝ) :
    InfinitesimallyStarCompatible (x : ℂ) := by
  rw [infinitesimal_starCompatible_iff_im_eq_zero]
  simp

/-- Convergence or existence of a boundary record carries no star-compatible
generator field by itself. -/
structure SummableBoundaryRecord where
  value : ℂ

def offSeamSummableRecord : SummableBoundaryRecord :=
  ⟨I⟩

theorem summable_record_does_not_force_starCompatibility :
    ¬ InfinitesimallyStarCompatible offSeamSummableRecord.value := by
  rw [infinitesimal_starCompatible_iff_im_eq_zero]
  norm_num [offSeamSummableRecord]

end MariciFormal
