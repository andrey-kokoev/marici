import Mathlib.LinearAlgebra.Matrix.Hermitian
import Mathlib.Tactic.FinCases

/-!
Coefficient comparison for Nima's bordered pencil.  The affine coefficient
forces a constant symmetrizer to preserve the port/carrier splitting; the
constant coefficient then gives the carrier commutant and port-collocation
equations.  The final example records that indefinite selfadjointness does not
force real spectrum.
-/

namespace MariciFormal

open Matrix

section CoefficientComparison

variable {V : Type*} [AddCommGroup V] [Module ℝ V]

/-- Equality of two affine real-parameter families determines their constant
and linear coefficients independently. -/
theorem affine_coefficients_eq {a b c d : V}
    (h : ∀ λ : ℝ, a - λ • b = c - λ • d) : a = c ∧ b = d := by
  have hconstant : a = c := by simpa using h 0
  have hlinear : a - b = c - d := by simpa using h 1
  constructor
  · exact hconstant
  · rw [hconstant] at hlinear
    exact sub_left_inj.mp hlinear

end CoefficientComparison

section BorderedPencil

variable {ι : Type*} [Fintype ι] [DecidableEq ι]

abbrev PortCarrierMatrix := Matrix (Unit ⊕ ι) (Unit ⊕ ι) ℂ

def carrierProjection : PortCarrierMatrix (ι := ι) :=
  Matrix.fromBlocks (0 : Matrix Unit Unit ℂ) 0 0 1

/-- Commutation with the carrier projection is precisely preservation of the
port/carrier splitting. -/
theorem carrierProjection_commutation_forces_blockDiagonal
    (J : PortCarrierMatrix (ι := ι))
    (hJ : carrierProjection (ι := ι) * J = J * carrierProjection (ι := ι)) :
    Matrix.IsTwoBlockDiagonal J := by
  rw [← J.fromBlocks_toBlocks] at hJ
  simp only [carrierProjection, Matrix.fromBlocks_multiply, Matrix.zero_mul,
    Matrix.mul_zero, Matrix.one_mul, Matrix.mul_one, zero_add, add_zero] at hJ
  obtain ⟨_, h₁₂, h₂₁, _⟩ := Matrix.fromBlocks_inj.mp hJ
  exact ⟨h₁₂.symm, h₂₁⟩

def portRow (c : ι → ℂ) : Matrix Unit ι ℂ := fun _ j => star (c j)

def portColumn (b : ι → ℂ) : Matrix ι Unit ℂ := fun i _ => b i

def scalarBlock (α : ℂ) : Matrix Unit Unit ℂ := fun _ _ => α

def borderedConstant (A : Matrix ι ι ℂ) (b c : ι → ℂ) :
    PortCarrierMatrix (ι := ι) :=
  Matrix.fromBlocks 0 (portRow c) (portColumn b) A

def blockMetric (α : ℂ) (K : Matrix ι ι ℂ) :
    PortCarrierMatrix (ι := ι) :=
  Matrix.fromBlocks (scalarBlock α) 0 0 K

def borderedPencil (A : Matrix ι ι ℂ) (b c : ι → ℂ) (λ : ℝ) :
    PortCarrierMatrix (ι := ι) :=
  borderedConstant A b c - (λ : ℂ) • carrierProjection

theorem carrierProjection_isHermitian :
    (carrierProjection (ι := ι))ᴴ = carrierProjection (ι := ι) := by
  simp [carrierProjection, Matrix.fromBlocks_conjTranspose]

theorem blockMetric_commutes_carrierProjection (α : ℂ) (K : Matrix ι ι ℂ) :
    carrierProjection (ι := ι) * blockMetric α K =
      blockMetric α K * carrierProjection (ι := ι) := by
  simp [carrierProjection, blockMetric, Matrix.fromBlocks_multiply]

/-- Grothendieck's finite cross-transfer obstruction: on the real spectral
axis, the canonical bordered pencil is Hermitian exactly when forcing and
observation are the same labelled port. -/
theorem borderedPencil_isHermitian_iff_ports_equal
    (A : Matrix ι ι ℂ) (b c : ι → ℂ) (λ : ℝ)
    (hA : Aᴴ = A) :
    (borderedPencil A b c λ)ᴴ = borderedPencil A b c λ ↔ b = c := by
  constructor
  · intro hHermitian
    funext i
    have hentry := congrFun (congrFun hHermitian (Sum.inr i)) (Sum.inl ())
    simpa [borderedPencil, borderedConstant, carrierProjection, portRow,
      portColumn, Matrix.fromBlocks_conjTranspose] using hentry.symm
  · intro hports
    subst c
    simp [borderedPencil, borderedConstant, carrierProjection, portRow,
      portColumn, Matrix.conjTranspose_sub, Matrix.conjTranspose_smul,
      Matrix.fromBlocks_conjTranspose, Complex.conj_ofReal, hA]

/-- The constant block equation for a Hermitian carrier and a real boundary
weight is exactly carrier commutation together with `K b = α c` and its
adjoint row equation. -/
theorem borderedConstant_symmetrizer_coefficients
    (A K : Matrix ι ι ℂ) (b c : ι → ℂ) (α : ℝ)
    (hA : Aᴴ = A)
    (hK : Kᴴ = K)
    (h : (borderedConstant A b c)ᴴ * blockMetric (α : ℂ) K =
      blockMetric (α : ℂ) K * borderedConstant A b c) :
    A * K = K * A ∧
      K * portColumn b = portColumn c * scalarBlock (α : ℂ) ∧
      portRow b * K = scalarBlock (α : ℂ) * portRow c := by
  simp only [borderedConstant, blockMetric, Matrix.fromBlocks_conjTranspose,
    Matrix.fromBlocks_multiply, Matrix.zero_mul, Matrix.mul_zero, zero_add,
    add_zero, hA, hK, map_zero] at h
  obtain ⟨_, hrow, hcolumn, hcarrier⟩ := Matrix.fromBlocks_inj.mp h
  exact ⟨hcarrier, hcolumn.symm, hrow⟩

/-- For Hermitian `K` and real `α`, the column port equation supplies its
adjoint row equation. -/
theorem adjointPortEquation
    (K : Matrix ι ι ℂ) (b c : ι → ℂ) (α : ℝ)
    (hK : Kᴴ = K)
    (hcolumn : K * portColumn b = portColumn c * scalarBlock (α : ℂ)) :
    portRow b * K = scalarBlock (α : ℂ) * portRow c := by
  have hadjoint := congrArg (fun matrix => matrixᴴ) hcolumn
  simpa [portColumn, portRow, scalarBlock, Matrix.conjTranspose_mul, hK]
    using hadjoint

/-- The coefficient conditions are sufficient to assemble the constant
bordered symmetrizer identity. -/
theorem borderedConstant_selfadjoint_of_coefficients
    (A K : Matrix ι ι ℂ) (b c : ι → ℂ) (α : ℝ)
    (hA : Aᴴ = A)
    (hK : Kᴴ = K)
    (hcomm : A * K = K * A)
    (hcolumn : K * portColumn b = portColumn c * scalarBlock (α : ℂ)) :
    (borderedConstant A b c)ᴴ * blockMetric (α : ℂ) K =
      blockMetric (α : ℂ) K * borderedConstant A b c := by
  have hrow := adjointPortEquation K b c α hK hcolumn
  simp [borderedConstant, blockMetric, Matrix.fromBlocks_conjTranspose,
    Matrix.fromBlocks_multiply, hA, hK, hcomm, hcolumn, hrow]

/-- Exact finite criterion for the constant coefficient of the bordered
symmetrizer equation. -/
theorem borderedConstant_symmetrizer_iff
    (A K : Matrix ι ι ℂ) (b c : ι → ℂ) (α : ℝ)
    (hA : Aᴴ = A) (hK : Kᴴ = K) :
    (borderedConstant A b c)ᴴ * blockMetric (α : ℂ) K =
        blockMetric (α : ℂ) K * borderedConstant A b c ↔
      A * K = K * A ∧
        K * portColumn b = portColumn c * scalarBlock (α : ℂ) := by
  constructor
  · intro h
    have hcoefficients :=
      borderedConstant_symmetrizer_coefficients A K b c α hA hK h
    exact ⟨hcoefficients.1, hcoefficients.2.1⟩
  · rintro ⟨hcomm, hcolumn⟩
    exact borderedConstant_selfadjoint_of_coefficients
      A K b c α hA hK hcomm hcolumn

/-- The exact coefficient conditions make the complete bordered pencil
`J`-selfadjoint for every real spectral parameter. -/
theorem borderedPencil_selfadjoint_of_coefficients
    (A K : Matrix ι ι ℂ) (b c : ι → ℂ) (α : ℝ)
    (hA : Aᴴ = A)
    (hK : Kᴴ = K)
    (hcomm : A * K = K * A)
    (hcolumn : K * portColumn b = portColumn c * scalarBlock (α : ℂ))
    (λ : ℝ) :
    (borderedPencil A b c λ)ᴴ * blockMetric (α : ℂ) K =
      blockMetric (α : ℂ) K * borderedPencil A b c λ := by
  have hconstant := borderedConstant_selfadjoint_of_coefficients
    A K b c α hA hK hcomm hcolumn
  have hprojection := blockMetric_commutes_carrierProjection
    (ι := ι) (α : ℂ) K
  simp only [borderedPencil, Matrix.conjTranspose_sub,
    Matrix.conjTranspose_smul, Complex.conj_ofReal,
    carrierProjection_isHermitian, sub_mul, mul_sub, smul_mul, mul_smul]
  rw [hconstant, hprojection]

/-- The affine pencil equation supplies the two coefficient equations.  The
input is the expanded polynomial identity, avoiding any appeal to evaluation
at unspecified complex parameters. -/
theorem borderedPencil_coefficientComparison
    (L₀ P J : PortCarrierMatrix (ι := ι))
    (h : ∀ λ : ℝ,
      L₀ᴴ * J - λ • (Pᴴ * J) = J * L₀ - λ • (J * P)) :
    L₀ᴴ * J = J * L₀ ∧ Pᴴ * J = J * P :=
  affine_coefficients_eq h

/-- An arbitrary constant metric symmetrizing the full real bordered pencil
must preserve the port/carrier splitting.  The constant equation is recovered
at the same time. -/
theorem borderedPencil_symmetrizer_forces_blockDiagonal
    (A : Matrix ι ι ℂ) (b c : ι → ℂ)
    (J : PortCarrierMatrix (ι := ι))
    (h : ∀ λ : ℝ,
      (borderedPencil A b c λ)ᴴ * J = J * borderedPencil A b c λ) :
    Matrix.IsTwoBlockDiagonal J ∧
      (borderedConstant A b c)ᴴ * J = J * borderedConstant A b c := by
  have hexpanded : ∀ λ : ℝ,
      (borderedConstant A b c)ᴴ * J -
          λ • ((carrierProjection (ι := ι))ᴴ * J) =
        J * borderedConstant A b c -
          λ • (J * carrierProjection (ι := ι)) := by
    intro λ
    simpa [borderedPencil, Matrix.conjTranspose_sub,
      Matrix.conjTranspose_smul, Complex.conj_ofReal, sub_mul, mul_sub,
      smul_mul, mul_smul, Algebra.smul_def] using h λ
  have hcoefficients := borderedPencil_coefficientComparison
    (borderedConstant A b c) (carrierProjection (ι := ι)) J hexpanded
  have hprojection :
      carrierProjection (ι := ι) * J = J * carrierProjection (ι := ι) := by
    calc
      carrierProjection (ι := ι) * J =
          (carrierProjection (ι := ι))ᴴ * J := by
            rw [carrierProjection_isHermitian]
      _ = J * carrierProjection (ι := ι) := hcoefficients.2
  exact ⟨carrierProjection_commutation_forces_blockDiagonal J hprojection,
    hcoefficients.1⟩

end BorderedPencil

section BlockMetricNondegeneracy

variable {ι : Type*} [Fintype ι] [DecidableEq ι]

def portLift (z : ℂ) : Unit ⊕ ι → ℂ
  | Sum.inl _ => z
  | Sum.inr _ => 0

def carrierLift (v : ι → ℂ) : Unit ⊕ ι → ℂ
  | Sum.inl _ => 0
  | Sum.inr i => v i

theorem blockMetric_mulVec_portLift (α : ℂ) (K : Matrix ι ι ℂ) (z : ℂ) :
    blockMetric α K *ᵥ portLift z = portLift (α * z) := by
  funext index
  rcases index with port | carrier
  · simp [blockMetric, portLift, scalarBlock, Matrix.mulVec, dotProduct]
  · simp [blockMetric, portLift, Matrix.mulVec, dotProduct]

theorem blockMetric_mulVec_carrierLift
    (α : ℂ) (K : Matrix ι ι ℂ) (v : ι → ℂ) :
    blockMetric α K *ᵥ carrierLift v = carrierLift (K *ᵥ v) := by
  funext index
  rcases index with port | carrier
  · simp [blockMetric, carrierLift, scalarBlock, Matrix.mulVec, dotProduct]
  · simp [blockMetric, carrierLift, Matrix.mulVec, dotProduct]

/-- The kernel equation for a block metric splits exactly into its boundary
and carrier equations. -/
theorem blockMetric_mulVec_eq_zero_iff
    (α : ℂ) (K : Matrix ι ι ℂ) (vector : Unit ⊕ ι → ℂ) :
    blockMetric α K *ᵥ vector = 0 ↔
      α * vector (Sum.inl ()) = 0 ∧
        K *ᵥ (fun i => vector (Sum.inr i)) = 0 := by
  constructor
  · intro hzero
    constructor
    · have hatPort := congrFun hzero (Sum.inl ())
      simpa [blockMetric, scalarBlock, Matrix.mulVec, dotProduct] using hatPort
    · funext i
      have hatCarrier := congrFun hzero (Sum.inr i)
      simpa [blockMetric, Matrix.mulVec, dotProduct] using hatCarrier
  · rintro ⟨hboundary, hcarrier⟩
    funext index
    rcases index with port | carrier
    · simpa [blockMetric, scalarBlock, Matrix.mulVec, dotProduct] using hboundary
    · have hatCarrier := congrFun hcarrier carrier
      simpa [blockMetric, Matrix.mulVec, dotProduct] using hatCarrier

/-- A block metric is nondegenerate exactly when its boundary scalar and
carrier block are independently nondegenerate. -/
theorem blockMetric_mulVec_injective_iff (α : ℂ) (K : Matrix ι ι ℂ) :
    Function.Injective (fun vector => blockMetric α K *ᵥ vector) ↔
      α ≠ 0 ∧ Function.Injective (fun vector => K *ᵥ vector) := by
  constructor
  · intro hmetric
    constructor
    · intro hα
      have hlifts : portLift (ι := ι) 1 = portLift 0 := by
        apply hmetric
        rw [blockMetric_mulVec_portLift, blockMetric_mulVec_portLift, hα]
        simp
      have hatPort := congrFun hlifts (Sum.inl ())
      norm_num [portLift] at hatPort
    · intro v w hvw
      have hlifts : carrierLift v = carrierLift w := by
        apply hmetric
        rw [blockMetric_mulVec_carrierLift, blockMetric_mulVec_carrierLift, hvw]
      funext i
      exact congrFun hlifts (Sum.inr i)
  · rintro ⟨hα, hK⟩ x y hxy
    have hport : x (Sum.inl ()) = y (Sum.inl ()) := by
      have hcoordinate := congrFun hxy (Sum.inl ())
      simp [blockMetric, scalarBlock, Matrix.mulVec, dotProduct] at hcoordinate
      exact mul_left_cancel₀ hα hcoordinate
    have hcarrier :
        (fun i => x (Sum.inr i)) = fun i => y (Sum.inr i) := by
      apply hK
      funext i
      have hcoordinate := congrFun hxy (Sum.inr i)
      simpa [blockMetric, Matrix.mulVec, dotProduct] using hcoordinate
    funext index
    rcases index with port | carrier
    · exact hport
    · exact congrFun hcarrier carrier

/-- A zero boundary weight destroys nondegeneracy even when the carrier block
is otherwise well behaved. -/
theorem zeroBoundaryWeight_blockMetric_not_injective
    (K : Matrix ι ι ℂ) :
    ¬ Function.Injective (fun vector => blockMetric 0 K *ᵥ vector) := by
  intro hmetric
  have hboundary := ((blockMetric_mulVec_injective_iff 0 K).mp hmetric).1
  exact hboundary rfl

/-- Every nonzero carrier-kernel witness lifts to a failure of block-metric
nondegeneracy, independently of the boundary scalar. -/
theorem carrierKernelWitness_blockMetric_not_injective
    (α : ℂ) (K : Matrix ι ι ℂ) (v : ι → ℂ)
    (hv : v ≠ 0) (hkernel : K *ᵥ v = 0) :
    ¬ Function.Injective (fun vector => blockMetric α K *ᵥ vector) := by
  intro hmetric
  have hcarrier := ((blockMetric_mulVec_injective_iff α K).mp hmetric).2
  apply hv
  apply hcarrier
  rw [hkernel]
  simp

end BlockMetricNondegeneracy

section SingularSymmetrizerHostile

abbrev SingletonCarrier := Fin 1

def singularCarrierMatrix : Matrix SingletonCarrier SingletonCarrier ℂ := 0

def singularPort : SingletonCarrier → ℂ := 0

def singularBlockMetric :
    Matrix (Unit ⊕ SingletonCarrier) (Unit ⊕ SingletonCarrier) ℂ :=
  blockMetric (ι := SingletonCarrier) 1 0

def singularMetricKernelVector : Unit ⊕ SingletonCarrier → ℂ
  | Sum.inl _ => 0
  | Sum.inr _ => 1

/-- The coefficient equations can hold and symmetrize the full pencil even
when the carrier metric block is singular. -/
theorem singularSymmetrizerHostile_selfadjoint (λ : ℝ) :
    (borderedPencil singularCarrierMatrix singularPort singularPort λ)ᴴ *
        singularBlockMetric =
      singularBlockMetric *
        borderedPencil singularCarrierMatrix singularPort singularPort λ := by
  apply borderedPencil_selfadjoint_of_coefficients
    singularCarrierMatrix 0 singularPort singularPort 1
  · simp [singularCarrierMatrix]
  · simp
  · simp
  · simp [singularPort, portColumn, scalarBlock]

theorem singularMetricKernelVector_ne_zero : singularMetricKernelVector ≠ 0 := by
  intro hzero
  have hatCarrier := congrFun hzero (Sum.inr (0 : SingletonCarrier))
  norm_num [singularMetricKernelVector] at hatCarrier

theorem singularBlockMetric_kills_kernelVector :
    singularBlockMetric *ᵥ singularMetricKernelVector = 0 := by
  apply (blockMetric_mulVec_eq_zero_iff
    (ι := SingletonCarrier) 1 0 singularMetricKernelVector).2
  constructor
  · simp [singularMetricKernelVector]
  · simp [singularMetricKernelVector, Matrix.mulVec]

/-- Algebraic symmetrization does not imply metric nondegeneracy. -/
theorem singularBlockMetric_mulVec_not_injective :
    ¬ Function.Injective (fun vector => singularBlockMetric *ᵥ vector) := by
  intro hinjective
  apply singularMetricKernelVector_ne_zero
  apply hinjective
  rw [singularBlockMetric_kills_kernelVector]
  simp

end SingularSymmetrizerHostile

section SimpleSpectrumCoordinate

/-- A diagonal simple-spectrum coordinate of `K b = α c` forces the port
ratio to be real.  This is the coordinate consequence; diagonalization of a
commuting Hermitian matrix is a separate spectral theorem. -/
theorem real_ratio_of_real_weights
    (k α : ℝ) (b c : ℂ) (hα : α ≠ 0)
    (h : (k : ℂ) * b = (α : ℂ) * c) :
    ∃ r : ℝ, c = (r : ℂ) * b := by
  refine ⟨k / α, ?_⟩
  apply (mul_left_cancel₀ (show (α : ℂ) ≠ 0 by exact_mod_cast hα))
  rw [← h]
  push_cast
  field_simp

/-- Nonzero diagonal metric and boundary weights force exact support matching
between the two port coordinates. -/
theorem support_matches_of_nonzero_real_weights
    (k α : ℝ) (b c : ℂ) (hk : k ≠ 0) (hα : α ≠ 0)
    (h : (k : ℂ) * b = (α : ℂ) * c) :
    b = 0 ↔ c = 0 := by
  constructor
  · intro hb
    have hzero : (α : ℂ) * c = 0 := by simpa [hb] using h.symm
    exact (mul_eq_zero.mp hzero).resolve_left (by exact_mod_cast hα)
  · intro hc
    have hzero : (k : ℂ) * b = 0 := by simpa [hc] using h
    exact (mul_eq_zero.mp hzero).resolve_left (by exact_mod_cast hk)

/-- At a nonzero port coordinate, the ratio is exactly the real diagonal
weight ratio. -/
theorem port_ratio_eq_real_weight_ratio
    (k α : ℝ) (b c : ℂ) (hα : α ≠ 0) (hb : b ≠ 0)
    (h : (k : ℂ) * b = (α : ℂ) * c) :
    c / b = ((k / α : ℝ) : ℂ) := by
  apply (div_eq_iff hb).2
  apply (mul_left_cancel₀ (show (α : ℂ) ≠ 0 by exact_mod_cast hα))
  rw [← h]
  push_cast
  field_simp

/-- A support mismatch is a finite falsifier for every pair of nonzero real
weights satisfying the coordinate port equation. -/
theorem support_mismatch_forbids_nonzero_real_weights
    (b c : ℂ) (hb : b = 0) (hc : c ≠ 0) :
    ¬ ∃ k α : ℝ, k ≠ 0 ∧ α ≠ 0 ∧
      (k : ℂ) * b = (α : ℂ) * c := by
  rintro ⟨k, α, hk, hα, h⟩
  exact hc ((support_matches_of_nonzero_real_weights
    k α b c hk hα h).mp hb)

/-- A single nonreal port ratio rules out every real diagonal weight with
nonzero boundary scale. -/
theorem nonreal_port_ratio_forbids_real_weights
    (b c : ℂ) (hb : b ≠ 0) (hnonreal : (c / b).im ≠ 0) :
    ¬ ∃ k α : ℝ, α ≠ 0 ∧
      (k : ℂ) * b = (α : ℂ) * c := by
  rintro ⟨k, α, hα, h⟩
  have hratio := port_ratio_eq_real_weight_ratio k α b c hα hb h
  apply hnonreal
  simpa using congrArg Complex.im hratio

/-- Minimal support-mismatch fixture. -/
theorem zero_one_support_mismatch_fixture :
    ¬ ∃ k α : ℝ, k ≠ 0 ∧ α ≠ 0 ∧
      (k : ℂ) * 0 = (α : ℂ) * 1 := by
  exact support_mismatch_forbids_nonzero_real_weights 0 1 rfl one_ne_zero

/-- Minimal nonreal-ratio fixture. -/
theorem one_I_nonreal_ratio_fixture :
    ¬ ∃ k α : ℝ, α ≠ 0 ∧
      (k : ℂ) * 1 = (α : ℂ) * Complex.I := by
  apply nonreal_port_ratio_forbids_real_weights 1 Complex.I
  · norm_num
  · norm_num

end SimpleSpectrumCoordinate

section IndefiniteHostile

def hostileKreinOperator : Matrix (Fin 2) (Fin 2) ℂ :=
  !![0, 1; -1, 0]

def hostileKreinMetric : Matrix (Fin 2) (Fin 2) ℂ :=
  !![1, 0; 0, -1]

def positiveImaginaryEigenvector : Fin 2 → ℂ := ![1, Complex.I]

def negativeImaginaryEigenvector : Fin 2 → ℂ := ![1, -Complex.I]

theorem hostileKreinOperator_is_metric_selfadjoint :
    hostileKreinOperatorᴴ * hostileKreinMetric =
      hostileKreinMetric * hostileKreinOperator := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    norm_num [hostileKreinOperator, hostileKreinMetric, Matrix.mul_apply]

theorem hostileKreinOperator_has_positive_imaginary_eigenvector :
    hostileKreinOperator *ᵥ positiveImaginaryEigenvector =
      Complex.I • positiveImaginaryEigenvector := by
  funext i
  fin_cases i <;>
    norm_num [hostileKreinOperator, positiveImaginaryEigenvector, Matrix.mulVec,
      dotProduct, Complex.I_mul_I]

theorem hostileKreinOperator_has_negative_imaginary_eigenvector :
    hostileKreinOperator *ᵥ negativeImaginaryEigenvector =
      (-Complex.I) • negativeImaginaryEigenvector := by
  funext i
  fin_cases i <;>
    norm_num [hostileKreinOperator, negativeImaginaryEigenvector, Matrix.mulVec,
      dotProduct, Complex.I_mul_I]

end IndefiniteHostile

end MariciFormal
