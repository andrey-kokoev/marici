import Mathlib

/-!
Conditional half-plane zero-confinement compiler.  The certificate states the
exact pointwise premises that a source-derived control factorization would
need.  It does not construct those premises for completed xi.
-/

namespace MariciFormal.HalfPlaneZeroConfinement

def InRightHalfPlane (z : ℂ) : Prop := 0 < z.re

def StrictPositiveRealOnRight (response : ℂ → ℂ) : Prop :=
  ∀ z, InRightHalfPlane z → 0 < (response z).re

def ZeroFreeOnRight (function : ℂ → ℂ) : Prop :=
  ∀ z, InRightHalfPlane z → function z ≠ 0

def ZerosOnImaginaryAxis (function : ℂ → ℂ) : Prop :=
  ∀ z, function z = 0 → z.re = 0

/-- Pointwise factorization data.  Analyticity and source provenance are not
smuggled into this logical certificate. -/
structure RightHalfPlaneFactorization (completed : ℂ → ℂ) where
  unit : ℂ → ℂ
  response : ℂ → ℂ
  factors : ∀ z, InRightHalfPlane z →
    completed z = unit z * response z
  unitNonzero : ∀ z, InRightHalfPlane z → unit z ≠ 0
  responseStrictPositive : StrictPositiveRealOnRight response

theorem strictPositiveReal_ne_zero
    {response : ℂ → ℂ} (strict : StrictPositiveRealOnRight response)
    {z : ℂ} (right : InRightHalfPlane z) : response z ≠ 0 := by
  intro zero
  have positive := strict z right
  rw [zero] at positive
  norm_num at positive

/-- A certified unit times a strict-positive-real response is zero-free in the
right half-plane. -/
theorem RightHalfPlaneFactorization.zeroFree
    {completed : ℂ → ℂ}
    (certificate : RightHalfPlaneFactorization completed) :
    ZeroFreeOnRight completed := by
  intro z right zero
  rw [certificate.factors z right] at zero
  exact (mul_ne_zero (certificate.unitNonzero z right)
    (strictPositiveReal_ne_zero certificate.responseStrictPositive right)) zero

/-- Reflection symmetry converts right-half-plane zero-freeness into
imaginary-axis zero confinement. -/
theorem zerosOnImaginaryAxis_of_reflection_and_rightZeroFree
    (completed : ℂ → ℂ)
    (reflection : ∀ z, completed (-z) = completed z)
    (rightZeroFree : ZeroFreeOnRight completed) :
    ZerosOnImaginaryAxis completed := by
  intro z zero
  rcases lt_trichotomy z.re 0 with negative | onAxis | positive
  · have negatedRight : InRightHalfPlane (-z) := by
      simp [InRightHalfPlane]
      linarith
    have negatedZero : completed (-z) = 0 := by
      rw [reflection z, zero]
    exact False.elim (rightZeroFree (-z) negatedRight negatedZero)
  · exact onAxis
  · exact False.elim (rightZeroFree z positive zero)

/-- The complete conditional compiler: factorization plus reflection confines
all zeros to the seam. -/
theorem RightHalfPlaneFactorization.zerosOnImaginaryAxis
    {completed : ℂ → ℂ}
    (certificate : RightHalfPlaneFactorization completed)
    (reflection : ∀ z, completed (-z) = completed z) :
    ZerosOnImaginaryAxis completed :=
  zerosOnImaginaryAxis_of_reflection_and_rightZeroFree completed reflection
    certificate.zeroFree

/-- Positive-real impedance fixture. -/
def identityImpedance (z : ℂ) : ℂ := z

noncomputable def cayleyReflection (z : ℂ) : ℂ := (z - 1) / (z + 1)

theorem identityImpedance_strictPositiveReal :
    StrictPositiveRealOnRight identityImpedance := by
  intro z right
  exact right

/-- Hostile adapter: strict positive-realness of an impedance does not make
its Cayley scattering readout zero-free. -/
theorem positiveReal_impedance_does_not_transport_to_cayley_zeroFree :
    StrictPositiveRealOnRight identityImpedance ∧
      InRightHalfPlane 1 ∧ cayleyReflection 1 = 0 := by
  refine ⟨identityImpedance_strictPositiveReal, ?_, ?_⟩
  · norm_num [InRightHalfPlane]
  · norm_num [cayleyReflection]

end MariciFormal.HalfPlaneZeroConfinement
