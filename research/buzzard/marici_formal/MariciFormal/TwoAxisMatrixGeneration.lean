import Mathlib

/-!
Finite two-axis reciprocal matrix generation.  This is the algebraic core of
Grothendieck's two-nonresonant-prime theorem and a finite observability fixture
for polarization/control matrix sectors.
-/

namespace MariciFormal.TwoAxisMatrixGeneration

abbrev MatrixTwo := Matrix (Fin 2) (Fin 2) ℂ

def sigmaOne : MatrixTwo := !![0, 1; 1, 0]
def sigmaTwo : MatrixTwo := !![0, -Complex.I; Complex.I, 0]

def reciprocalAxis (cosine sine : ℂ) : MatrixTwo :=
  cosine • sigmaOne + sine • sigmaTwo

/-- Nonresonance (`sine ≠ 0`) makes the four displayed generated matrices a
spanning family for every complex two-by-two matrix. -/
theorem two_nonresonant_axes_span
    (cosine sine : ℂ) (sineNonzero : sine ≠ 0) (target : MatrixTwo) :
    ∃ identityCoefficient firstCoefficient secondCoefficient
        productCoefficient : ℂ,
      target = identityCoefficient • (1 : MatrixTwo) +
        firstCoefficient • sigmaOne +
        secondCoefficient • reciprocalAxis cosine sine +
        productCoefficient • (sigmaOne * reciprocalAxis cosine sine) := by
  let productCoefficient : ℂ :=
    (target 0 0 - target 1 1) / (2 * Complex.I * sine)
  let identityCoefficient : ℂ :=
    target 0 0 - productCoefficient * (cosine + Complex.I * sine)
  let secondCoefficient : ℂ :=
    (target 1 0 - target 0 1) / (2 * Complex.I * sine)
  let firstCoefficient : ℂ :=
    target 0 1 - secondCoefficient * (cosine - Complex.I * sine)
  refine ⟨identityCoefficient, firstCoefficient, secondCoefficient,
    productCoefficient, ?_⟩
  ext row column
  fin_cases row <;> fin_cases column <;>
    simp [identityCoefficient, firstCoefficient, secondCoefficient,
      productCoefficient, reciprocalAxis, sigmaOne, sigmaTwo,
      ] <;>
    field_simp [sineNonzero, Complex.I_ne_zero] <;> ring

/-- Hostile resonant locus: when the second axis is parallel to the first,
the same four expressions cannot generate the missing `sigmaTwo` direction.
-/
theorem resonant_axes_do_not_span_sigmaTwo :
    ¬ ∃ identityCoefficient firstCoefficient secondCoefficient
        productCoefficient : ℂ,
      sigmaTwo = identityCoefficient • (1 : MatrixTwo) +
        firstCoefficient • sigmaOne +
        secondCoefficient • reciprocalAxis 1 0 +
        productCoefficient • (sigmaOne * reciprocalAxis 1 0) := by
  rintro ⟨identityCoefficient, firstCoefficient, secondCoefficient,
    productCoefficient, equality⟩
  have upper := congrFun (congrFun equality 0) 1
  have lower := congrFun (congrFun equality 1) 0
  simp [reciprocalAxis, sigmaOne, sigmaTwo] at upper lower
  have impossible : (2 : ℂ) * Complex.I = 0 := by
    linear_combination lower - upper
  norm_num [Complex.I_ne_zero] at impossible

end MariciFormal.TwoAxisMatrixGeneration
