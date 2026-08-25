import MariciFormal.Sprint1

/-! Sprint 2: capability quotients, disappearance mechanisms, and accessible operators. -/

namespace MariciFormal

section Capability

variable {R Repair H Residue Probe : Type*} [CommRing R]
  [AddCommGroup Repair] [Module R Repair]
  [AddCommGroup H] [Module R H]
  [AddCommGroup Residue] [Module R Residue]
  [AddCommGroup Probe] [Module R Probe]

/-- A two-step linear complex `Repair → H → Residue`. -/
structure TwoStepComplex where
  repair : Repair →ₗ[R] H
  residue : H →ₗ[R] Residue
  zero_comp : residue.comp repair = 0

namespace TwoStepComplex

variable (C : TwoStepComplex (R := R) (Repair := Repair)
  (H := H) (Residue := Residue))

def cycles : Submodule R H := LinearMap.ker C.residue

def boundaries : Submodule R C.cycles :=
  (LinearMap.range C.repair).comap C.cycles.subtype

abbrev Capability := C.cycles ⧸ C.boundaries

theorem range_repair_le_cycles : LinearMap.range C.repair ≤ C.cycles := by
  rintro _ ⟨x, rfl⟩
  change C.residue (C.repair x) = 0
  have h := LinearMap.congr_fun C.zero_comp x
  simpa using h

def cycleProbe (ell : H →ₗ[R] Probe) : C.cycles →ₗ[R] Probe :=
  ell.comp C.cycles.subtype

def ProbeDescends (ell : H →ₗ[R] Probe) : Prop :=
  DescendsThrough C.boundaries (C.cycleProbe ell)

theorem probeDescends_iff (ell : H →ₗ[R] Probe) :
    C.ProbeDescends ell ↔ LinearMap.range C.repair ≤ LinearMap.ker ell := by
  rw [ProbeDescends, descendsThrough_iff]
  constructor
  · intro h x hx
    let z : C.cycles := ⟨x, C.range_repair_le_cycles hx⟩
    have hz : z ∈ C.boundaries := hx
    exact h hz
  · intro h z hz
    exact h hz

/-- Joint residue/probe faithfulness modulo repairs. -/
def ResidueProbeFaithfulModulo (ell : H →ₗ[R] Probe) : Prop :=
  LinearMap.ker C.residue ⊓ LinearMap.ker ell = LinearMap.range C.repair

theorem residueProbeFaithfulModulo_iff (ell : H →ₗ[R] Probe) :
    C.ResidueProbeFaithfulModulo ell ↔
      LinearMap.ker C.residue ⊓ LinearMap.ker ell = LinearMap.range C.repair :=
  Iff.rfl

end TwoStepComplex

end Capability

section SuccessorQuotients

variable {R V : Type*} [CommRing R] [AddCommGroup V] [Module R V]

/-- Canonical map induced by enlarging legal repair relations `B ≤ B'`. -/
def successorMap (B B' : Submodule R V) (h : B ≤ B') : V ⧸ B →ₗ[R] V ⧸ B' :=
  B.mapQ B' LinearMap.id (by simpa using h)

@[simp] theorem successorMap_mk (B B' : Submodule R V) (h : B ≤ B') (x : V) :
    successorMap B B' h (B.mkQ x) = B'.mkQ x := by
  simp [successorMap]

/-- Exact constitutive-death criterion for a represented class. -/
theorem successorMap_mk_eq_zero_iff (B B' : Submodule R V) (h : B ≤ B') (x : V) :
    successorMap B B' h (B.mkQ x) = 0 ↔ x ∈ B' := by
  simp [successorMap]

/-- The kernel is precisely the image of the enlarged repair submodule. -/
theorem ker_successorMap (B B' : Submodule R V) (h : B ≤ B') :
    LinearMap.ker (successorMap B B' h) = B'.map B.mkQ := by
  simpa [successorMap] using Submodule.ker_mapQ (p := B) (q := B') LinearMap.id
    (by simpa using h)

/-- Functorial recomputation under two successive enlargements. -/
theorem successorMap_comp (B B' B'' : Submodule R V)
    (h₁ : B ≤ B') (h₂ : B' ≤ B'') :
    (successorMap B' B'' h₂).comp (successorMap B B' h₁) =
      successorMap B B'' (h₁.trans h₂) := by
  ext x
  change successorMap B' B'' h₂ (successorMap B B' h₁ (B.mkQ x)) =
    successorMap B B'' (h₁.trans h₂) (B.mkQ x)
  rw [successorMap_mk, successorMap_mk, successorMap_mk]

end SuccessorQuotients

section Mechanisms

/-- Access denial changes only the admitted probe index set. -/
structure AccessDenial (ι : Type*) where
  admitted : Set ι

/-- Readout loss is a noninjective map on an unchanged capability object. -/
structure ReadoutLoss (X Y : Type*) where
  readout : X → Y
  noninjective : ¬ Function.Injective readout

/-- Constitutive collapse enlarges the repair relation. -/
structure ConstitutiveCollapse {R V : Type*} [CommRing R]
    [AddCommGroup V] [Module R V] where
  before : Submodule R V
  after : Submodule R V
  enlarged : before ≤ after

theorem access_denial_leaves_class_nonzero :
    let v : Fin 2 → ℚ := ![1, 0]
    v ≠ 0 ∧ ∃ d : AccessDenial (Fin 2), d.admitted = {0} := by
  dsimp
  constructor
  · intro h
    have := congrFun h 0
    norm_num at this
  · exact ⟨⟨{0}⟩, rfl⟩

theorem readout_loss_leaves_object_nontrivial :
    Nontrivial (Fin 2 → ℚ) ∧
      Nonempty (ReadoutLoss (Fin 2 → ℚ) ℚ) := by
  constructor
  · infer_instance
  · let q : (Fin 2 → ℚ) → ℚ := fun v => v 0
    refine ⟨⟨q, ?_⟩⟩
    intro h
    have heq := h (a₁ := ![0, 0]) (a₂ := ![0, 1]) rfl
    have := congrFun heq 1
    norm_num at this

theorem collapse_can_kill_nonzero_class :
    let B : Submodule ℚ (Fin 2 → ℚ) := ⊥
    let B' : Submodule ℚ (Fin 2 → ℚ) := Submodule.span ℚ {![1, 0]}
    let x : Fin 2 → ℚ := ![1, 0]
    B.mkQ x ≠ 0 ∧ successorMap B B' bot_le (B.mkQ x) = 0 := by
  dsimp
  constructor
  · simp
  · apply (successorMap_mk_eq_zero_iff _ _ _ _).2
    exact Submodule.subset_span (Set.mem_singleton _)

/-- Removing a probe never changes the underlying vector or makes it zero. -/
theorem removing_probe_does_not_kill_capability :
    let x : Fin 2 → ℚ := ![1, 0]
    let all : Fin 2 → (Fin 2 → ℚ) →ₗ[ℚ] ℚ := fun i => LinearMap.proj i
    let admitted : Set (Fin 2) := {1}
    x ≠ 0 ∧ (∀ i ∈ admitted, all i x = 0) := by
  dsimp
  constructor
  · intro h
    have := congrFun h 0
    norm_num at this
  · intro i hi
    simp at hi
    subst i
    norm_num

end Mechanisms

section AccessibleOperators

variable {R V : Type*} [CommRing R] [AddCommGroup V] [Module R V]

/-- Endomorphisms generated by the declared constructor family. -/
def accessibleImage (constructors : Set (Module.End R V)) : Submonoid (Module.End R V) :=
  Submonoid.closure constructors

theorem accessibleImage_mono {C D : Set (Module.End R V)} (h : C ⊆ D) :
    accessibleImage C ≤ accessibleImage D :=
  Submonoid.closure_mono h

theorem outside_accessibleImage_not_generated (C : Set (Module.End R V))
    (p : Module.End R V) (hp : p ∉ accessibleImage C) : p ∉ accessibleImage C := hp

/-- Even a commuting constructor family need not generate every endomorphism. -/
theorem commuting_generators_need_not_generate_all :
    let C : Set (Module.End ℚ ℚ) := {1}
    (∀ a ∈ C, ∀ b ∈ C, a * b = b * a) ∧
      (0 : Module.End ℚ ℚ) ∉ accessibleImage C := by
  dsimp
  constructor
  · simp
  · rw [accessibleImage, Submonoid.closure_singleton_one]
    simp

/-- Full reconstruction is an additional spanning condition, not a consequence of membership. -/
def OperatorSpanning (C : Set (Module.End R V)) : Prop := accessibleImage C = ⊤

theorem operatorSpanning_iff (C : Set (Module.End R V)) :
    OperatorSpanning C ↔ ∀ p, p ∈ accessibleImage C := by
  constructor
  · intro h p
    rw [OperatorSpanning] at h
    rw [h]
    trivial
  · intro h
    rw [OperatorSpanning]
    exact top_unique (fun p _ => h p)

end AccessibleOperators

section FiniteModel

/-- Two coordinate probes jointly reconstruct the two-dimensional rational model. -/
theorem two_coordinates_jointly_faithful :
    let q : Fin 2 → (Fin 2 → ℚ) →ₗ[ℚ] ℚ := fun i => LinearMap.proj i
    JointlyFaithful q := by
  dsimp
  rw [jointlyFaithful_iff_point_separating]
  intro v hv
  funext i
  exact hv i

def coordinateProjector (i : Fin 2) : Module.End ℚ (Fin 2 → ℚ) :=
  (LinearMap.single ℚ (fun _ : Fin 2 => ℚ) i).comp (LinearMap.proj i)

def coordinateSwap : Module.End ℚ (Fin 2 → ℚ) :=
  (LinearMap.single ℚ (fun _ : Fin 2 => ℚ) 0).comp (LinearMap.proj 1) +
  (LinearMap.single ℚ (fun _ : Fin 2 => ℚ) 1).comp (LinearMap.proj 0)

def PreservesFirstAxis (f : Module.End ℚ (Fin 2 → ℚ)) : Prop :=
  ∀ v, v 1 = 0 → f v 1 = 0

theorem generated_coordinates_preserve_first_axis
    {f : Module.End ℚ (Fin 2 → ℚ)}
    (hf : f ∈ accessibleImage ({coordinateProjector 0, coordinateProjector 1} :
      Set (Module.End ℚ (Fin 2 → ℚ)))) : PreservesFirstAxis f := by
  change f ∈ Submonoid.closure _ at hf
  induction hf using Submonoid.closure_induction with
  | mem f hf =>
      simp only [Set.mem_insert_iff, Set.mem_singleton_iff] at hf
      rcases hf with rfl | rfl <;> intro v hv <;>
        simp [coordinateProjector, hv]
  | one => simp [PreservesFirstAxis]
  | mul f g _ _ hf hg =>
      intro v hv
      exact hf (g v) (hg v hv)

/-- The commuting coordinate projectors omit the off-diagonal coordinate swap. -/
theorem commuting_coordinates_omit_coherence :
    coordinateProjector 0 * coordinateProjector 1 =
      coordinateProjector 1 * coordinateProjector 0 ∧
    coordinateSwap ∉ accessibleImage
      ({coordinateProjector 0, coordinateProjector 1} :
        Set (Module.End ℚ (Fin 2 → ℚ))) := by
  constructor
  · ext v i
    fin_cases i <;> simp [coordinateProjector]
  · intro hswap
    have hpres := generated_coordinates_preserve_first_axis hswap
    have hz := hpres ![1, 0] (by norm_num)
    norm_num [coordinateSwap] at hz

end FiniteModel

end MariciFormal
