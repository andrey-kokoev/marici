import Mathlib.LinearAlgebra.Basic
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.PushNeg
import Mathlib.Tactic.Ring

/-!
Finite rank-one incidence transport and its unavoidable detector kernel from
Grothendieck's theta anomaly-line/projective-incidence packets.
-/

namespace MariciFormal

section RankOneTransport

variable {R CS CT LS LT : Type*}
variable [Semiring R]
variable [AddCommMonoid CS] [Module R CS]
variable [AddCommMonoid CT] [Module R CT]
variable [AddCommMonoid LS] [Module R LS]
variable [AddCommMonoid LT] [Module R LT]

def rankOneIncidence
    (vacuum : LT) (trace : CT →ₗ[R] R) (c : CT) : LT :=
  trace c • vacuum

/-- Compatible trace transport and vacuum transport make the rank-one
incidence square commute exactly. -/
theorem rankOneIncidence_transport
    (vacuumS : LS) (vacuumT : LT)
    (traceS : CS →ₗ[R] R) (traceT : CT →ₗ[R] R)
    (sourceMap : CS →ₗ[R] CT) (lineMap : LS →ₗ[R] LT)
    (htrace : ∀ c, traceT (sourceMap c) = traceS c)
    (hvacuum : lineMap vacuumS = vacuumT) (c : CS) :
    rankOneIncidence vacuumT traceT (sourceMap c) =
      lineMap (rankOneIncidence vacuumS traceS c) := by
  simp [rankOneIncidence, htrace c, ← hvacuum]

end RankOneTransport

section ScalarQuotient

variable {K C : Type*} [Field K] [AddCommGroup C] [Module K C]

/-- A nonzero scalar trace is onto its one-dimensional endpoint quotient. -/
theorem nonzero_scalar_trace_surjective
    (trace : C →ₗ[K] K) (htrace : trace ≠ 0) :
    Function.Surjective trace := by
  have hex : ∃ c, trace c ≠ 0 := by
    by_contra hall
    push_neg at hall
    apply htrace
    ext c
    simpa using hall c
  obtain ⟨c, hc⟩ := hex
  intro value
  refine ⟨((trace c)⁻¹ * value) • c, ?_⟩
  simp [hc, mul_assoc, mul_comm, mul_left_comm]

/-- Trace compatibility makes the transported trace onto whenever the source
trace is nonzero. This is the scalar form of quotient surjectivity. -/
theorem compatible_trace_composite_surjective
    {CT : Type*} [AddCommGroup CT] [Module K CT]
    (traceS : C →ₗ[K] K) (traceT : CT →ₗ[K] K)
    (sourceMap : C →ₗ[K] CT) (htraceS : traceS ≠ 0)
    (hcompat : ∀ c, traceT (sourceMap c) = traceS c) :
    Function.Surjective (fun c => traceT (sourceMap c)) := by
  intro value
  obtain ⟨c, hc⟩ := nonzero_scalar_trace_surjective traceS htraceS value
  exact ⟨c, by rw [hcompat c, hc]⟩

end ScalarQuotient

section TwoLabelKernel

variable {K L : Type*} [Field K]
variable [AddCommGroup L] [Module K L]

def twoLabelTrace (weight : Fin 2 → K) : (Fin 2 → K) →ₗ[K] K :=
  { toFun := fun c => weight 0 * c 0 + weight 1 * c 1
    map_add' := by
      intro x y
      simp
      ring
    map_smul' := by
      intro scalar x
      simp
      ring }

def twoLabelKernelWitness (weight : Fin 2 → K) : Fin 2 → K
  | 0 => weight 1
  | 1 => -weight 0

theorem twoLabelKernelWitness_trace_zero (weight : Fin 2 → K) :
    twoLabelTrace weight (twoLabelKernelWitness weight) = 0 := by
  simp [twoLabelTrace, twoLabelKernelWitness]
  ring

theorem twoLabelKernelWitness_ne_zero
    (weight : Fin 2 → K) (hvisible : weight 1 ≠ 0) :
    twoLabelKernelWitness weight ≠ 0 := by
  intro hzero
  have hfirst := congrFun hzero (0 : Fin 2)
  simp [twoLabelKernelWitness] at hfirst
  exact hvisible hfirst

/-- Two visible labels already make the scalar detector nonfaithful. -/
theorem twoLabelTrace_not_injective
    (weight : Fin 2 → K) (hvisible : weight 1 ≠ 0) :
    ¬ Function.Injective (twoLabelTrace weight) := by
  intro hinjective
  have hwitnessZero : twoLabelKernelWitness weight = 0 :=
    hinjective (by simpa using twoLabelKernelWitness_trace_zero weight)
  exact twoLabelKernelWitness_ne_zero weight hvisible hwitnessZero

/-- With a nonzero vacuum, rank-one incidence vanishes exactly when its
scalar trace vanishes: this is projective hyperplane incidence, not a
self-adjoint spectral equation. -/
theorem rankOneIncidence_eq_zero_iff
    (vacuum : L) (hvacuum : vacuum ≠ 0)
    (trace : (Fin 2 → K) →ₗ[K] K) (c : Fin 2 → K) :
    rankOneIncidence vacuum trace c = 0 ↔ trace c = 0 := by
  simp [rankOneIncidence, hvacuum]

end TwoLabelKernel

end MariciFormal
