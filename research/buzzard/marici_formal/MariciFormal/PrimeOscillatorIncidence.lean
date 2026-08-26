import Mathlib.LinearAlgebra.Vandermonde

/-!
Finite-cutoff algebraic core of Grothendieck's prime--oscillator semigroup
incidence kernel.  Analytic Schatten estimates and the Schur-complement
identification are deliberately outside this module.
-/

namespace MariciFormal

open Matrix
open scoped BigOperators

section CutoffKernel

variable {K : Type*} [Field K]
variable {n : ℕ}

/-- Rows are oscillator modes and columns are source labels. `node` is the
semigroup node (for primes, `1/p`) and `amplitude` is the nonzero column
weight. -/
def semigroupIncidence
    (node amplitude : Fin n → K) : Matrix (Fin n) (Fin n) K :=
  (Matrix.diagonal amplitude * Matrix.vandermonde node)ᵀ

theorem semigroupIncidence_apply
    (node amplitude : Fin n → K) (mode label : Fin n) :
    semigroupIncidence node amplitude mode label =
      amplitude label * node label ^ mode.val := by
  simp [semigroupIncidence, Matrix.mul_apply, Matrix.vandermonde]

/-- The finite cutoff determinant is the product of the source amplitudes
and the Vandermonde differences, up to the fixed row/column orientation built
into `semigroupIncidence`. -/
theorem det_semigroupIncidence (node amplitude : Fin n → K) :
    (semigroupIncidence node amplitude).det =
      (∏ i, amplitude i) *
        ∏ i : Fin n, ∏ j ∈ Finset.Ioi i, (node j - node i) := by
  rw [semigroupIncidence, Matrix.det_transpose, Matrix.det_mul,
    Matrix.det_diagonal, Matrix.det_vandermonde]

/-- Distinct semigroup nodes and nonzero source amplitudes give full-rank
finite cutoffs at every parameter value satisfying those two premises. -/
theorem det_semigroupIncidence_ne_zero
    (node amplitude : Fin n → K)
    (hnode : Function.Injective node)
    (hamplitude : ∀ i, amplitude i ≠ 0) :
    (semigroupIncidence node amplitude).det ≠ 0 := by
  rw [det_semigroupIncidence]
  apply mul_ne_zero
  · exact Finset.prod_ne_zero_iff.mpr (fun i hi => hamplitude i)
  · exact (Matrix.det_vandermonde_ne_zero_iff.mpr hnode)

/-- Consequently this bare incidence determinant cannot itself encode an
isolated zero while its source amplitudes remain nonzero and its nodes remain
distinct. -/
theorem bare_incidence_has_no_parameter_zero
    {T : Type*} (node : Fin n → K) (amplitude : T → Fin n → K)
    (hnode : Function.Injective node)
    (hamplitude : ∀ t i, amplitude t i ≠ 0) (t : T) :
    (semigroupIncidence node (amplitude t)).det ≠ 0 :=
  det_semigroupIncidence_ne_zero node (amplitude t) hnode (hamplitude t)

end CutoffKernel

end MariciFormal
