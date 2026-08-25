import MariciFormal.Sprint1

namespace MariciFormal.FiniteObservation

open Module

variable {F V : Type*} [Field F] [AddCommGroup V] [Module F V]

/-- The exact observation matrix/map assembled from scalar ports. -/
def observationMap {ι : Type*} (q : ι → V →ₗ[F] F) : V →ₗ[F] (ι → F) :=
  LinearMap.pi q

theorem ker_observationMap_eq_jointKernel {ι : Type*} (q : ι → V →ₗ[F] F) :
    LinearMap.ker (observationMap q) = MariciFormal.jointKernel q := by
  ext v
  simp only [LinearMap.mem_ker, MariciFormal.jointKernel, Submodule.mem_iInf]
  change (observationMap q v = 0) ↔ ∀ i, q i v = 0
  constructor
  · intro h i
    exact congrFun h i
  · intro h
    funext i
    exact h i

noncomputable def ObservationRank {ι : Type*} (q : ι → V →ₗ[F] F) : Nat :=
  finrank F (LinearMap.range (observationMap q))

/-- Strominger's finite observation theorem: full rank is exactly faithfulness. -/
theorem observationRank_eq_finrank_iff {ι : Type*} [FiniteDimensional F V]
    (q : ι → V →ₗ[F] F) :
    ObservationRank q = finrank F V ↔ MariciFormal.JointlyFaithful q := by
  rw [MariciFormal.JointlyFaithful, ← ker_observationMap_eq_jointKernel]
  constructor
  · intro hrank
    unfold ObservationRank at hrank
    have h := (observationMap q).finrank_range_add_finrank_ker
    rw [hrank] at h
    have hk : finrank F (LinearMap.ker (observationMap q)) = 0 := by omega
    exact Submodule.finrank_eq_zero.mp hk
  · intro hker
    exact LinearMap.finrank_range_of_inj (LinearMap.ker_eq_bot.mp hker)

/-- Faithful after no deletion, unfaithful after deleting any one port. -/
def DeletionMinimal {ι : Type*} (q : ι → V →ₗ[F] F) : Prop :=
  MariciFormal.JointlyFaithful q ∧
    ∀ i, ¬ MariciFormal.JointlyFaithful (fun j : {j // j ≠ i} ↦ q j.1)

def coordinateProbes (n : Nat) : Fin n → (Fin n → F) →ₗ[F] F :=
  fun i ↦ LinearMap.proj i

theorem coordinateProbes_jointlyFaithful (n : Nat) :
    MariciFormal.JointlyFaithful (coordinateProbes (F := F) n) := by
  rw [MariciFormal.jointlyFaithful_iff_point_separating]
  intro v hv
  funext i
  exact hv i

theorem coordinateProbes_deletionMinimal (n : Nat) :
    DeletionMinimal (coordinateProbes (F := F) n) := by
  refine ⟨coordinateProbes_jointlyFaithful n, ?_⟩
  intro i hfaithful
  rw [MariciFormal.jointlyFaithful_iff_point_separating] at hfaithful
  let e : Fin n → F := Pi.single i 1
  have he : e = 0 := hfaithful e (by
    intro j
    simp [coordinateProbes, e, j.property])
  have hi := congrFun he i
  simp [e] at hi

/-- Physical execution authority is separate from a port's linear value. -/
structure AuthorizedPort (V F : Type*) [Semiring F] [AddCommMonoid V] [Module F V] where
  execute : Option (V →ₗ[F] F)

def unavailablePort : AuthorizedPort V F := ⟨none⟩

def availableZeroPort : AuthorizedPort V F := ⟨some 0⟩

theorem unavailable_ne_availableZero :
    (unavailablePort : AuthorizedPort V F) ≠ availableZeroPort := by
  intro h
  have := congrArg AuthorizedPort.execute h
  simp [unavailablePort, availableZeroPort] at this

theorem availableZeroPort_value (v : V) :
    (0 : V →ₗ[F] F) v = 0 := by
  simp

/-- Magnetic 21-mode observation family: identity coordinates are minimal. -/
example : DeletionMinimal (coordinateProbes (F := ℚ) 21) :=
  coordinateProbes_deletionMinimal 21

/-- Boolean two-coordinate zeta transform: `(a,b) ↦ (a,a+b)`. -/
def booleanZetaPorts : Fin 2 → (Fin 2 → ℚ) →ₗ[ℚ] ℚ :=
  ![(LinearMap.proj 0 : (Fin 2 → ℚ) →ₗ[ℚ] ℚ),
    (LinearMap.proj 0 : (Fin 2 → ℚ) →ₗ[ℚ] ℚ) + LinearMap.proj 1]

theorem booleanZetaPorts_faithful :
    MariciFormal.JointlyFaithful booleanZetaPorts := by
  rw [MariciFormal.jointlyFaithful_iff_point_separating]
  intro v h
  have h0 := h 0
  have h1 := h 1
  funext i
  fin_cases i <;> simp [booleanZetaPorts] at h0 h1 ⊢ <;> linarith

/-- Magnetic reflection/Hadamard ports: `(a,b) ↦ (a+b,a-b)`. -/
def magneticHadamardPorts : Fin 2 → (Fin 2 → ℚ) →ₗ[ℚ] ℚ :=
  ![(LinearMap.proj 0 : (Fin 2 → ℚ) →ₗ[ℚ] ℚ) + LinearMap.proj 1,
    (LinearMap.proj 0 : (Fin 2 → ℚ) →ₗ[ℚ] ℚ) - LinearMap.proj 1]

theorem magneticHadamardPorts_faithful :
    MariciFormal.JointlyFaithful magneticHadamardPorts := by
  rw [MariciFormal.jointlyFaithful_iff_point_separating]
  intro v h
  have h0 := h 0
  have h1 := h 1
  funext i
  fin_cases i <;> simp [magneticHadamardPorts] at h0 h1 ⊢ <;> linarith

end MariciFormal.FiniteObservation
