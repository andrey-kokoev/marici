import Mathlib

/-! Reusable algebraic statements for Marici Entries 2109--2125. -/

namespace MariciFormal

section Difference

variable (A : Type*) [AddCommGroup A]

def delta : A × A →+ A := AddMonoidHom.snd A A - AddMonoidHom.fst A A

def diagonal : AddSubgroup (A × A) where
  carrier := {a | a.1 = a.2}
  zero_mem' := rfl
  add_mem' := by rintro ⟨a₀, a₁⟩ ⟨b₀, b₁⟩ ha hb; simp_all
  neg_mem' := by rintro ⟨a₀, a₁⟩ ha; simp_all

theorem delta_ker_eq_diagonal : (delta A).ker = diagonal A := by
  ext a
  simp [delta, diagonal, sub_eq_zero, eq_comm]

structure PeriodicPhaseLayer where
  period : AddSubgroup A
  quotientMap : A →+ A ⧸ period
  quotientMap_eq_mk : quotientMap = QuotientAddGroup.mk' period

end Difference

section Probes

variable {R V W Q : Type*} [CommRing R]
  [AddCommGroup V] [Module R V]
  [AddCommGroup W] [Module R W]
  [AddCommGroup Q] [Module R Q]

def jointKernel {ι : Type*} (q : ι → V →ₗ[R] W) : Submodule R V :=
  ⨅ i, LinearMap.ker (q i)

def JointlyFaithful {ι : Type*} (q : ι → V →ₗ[R] W) : Prop :=
  jointKernel q = ⊥

theorem jointlyFaithful_iff_jointKernel_eq_bot {ι : Type*} (q : ι → V →ₗ[R] W) :
    JointlyFaithful q ↔ jointKernel q = ⊥ := Iff.rfl

theorem jointlyFaithful_iff_point_separating {ι : Type*} (q : ι → V →ₗ[R] W) :
    JointlyFaithful q ↔ ∀ v, (∀ i, q i v = 0) → v = 0 := by
  simp [JointlyFaithful, jointKernel, Submodule.eq_bot_iff]

def Erases (r : V →ₗ[R] Q) (v₁ v₂ : V) : Prop := r v₁ = r v₂

theorem erases_iff_sub_mem_ker (r : V →ₗ[R] Q) (v₁ v₂ : V) :
    Erases r v₁ v₂ ↔ v₁ - v₂ ∈ LinearMap.ker r := by
  simp [Erases, sub_eq_zero]

def DescendsThrough (K : Submodule R V) (q : V →ₗ[R] W) : Prop :=
  ∃ qbar : (V ⧸ K) →ₗ[R] W, qbar.comp K.mkQ = q

theorem descendsThrough_iff (K : Submodule R V) (q : V →ₗ[R] W) :
    DescendsThrough K q ↔ K ≤ LinearMap.ker q := by
  constructor
  · rintro ⟨qbar, hqbar⟩ x hx
    change q x = 0
    rw [← hqbar]
    change qbar (K.mkQ x) = 0
    rw [show K.mkQ x = 0 from (Submodule.Quotient.mk_eq_zero K).mpr hx]
    exact map_zero qbar
  · intro h
    refine ⟨K.liftQ q ?_, ?_⟩
    · intro x hx
      exact h hx
    · ext x
      simp

theorem family_descendsThrough_iff {ι : Type*} (K : Submodule R V)
    (q : ι → V →ₗ[R] W) :
    (∀ i, DescendsThrough K (q i)) ↔ ∀ i, K ≤ LinearMap.ker (q i) := by
  simp [descendsThrough_iff]

end Probes

structure Selector (X : Type*) where
  chosen : X

structure Rigidifier (X : Type*) where
  reduce : X → X
  idempotent : ∀ x, reduce (reduce x) = reduce x

def FaithfulReadout {X Y : Type*} (r : X → Y) : Prop := Function.Injective r

theorem rigidifier_does_not_imply_selector :
    Nonempty (Rigidifier Empty) ∧ IsEmpty (Selector Empty) := by
  constructor
  · exact ⟨⟨id, fun _ => rfl⟩⟩
  · constructor
    intro s
    exact s.chosen.elim

theorem selector_does_not_imply_faithful_readout :
    Nonempty (Selector Bool) ∧ ¬ FaithfulReadout (fun _ : Bool => ()) := by
  constructor
  · exact ⟨⟨true⟩⟩
  · intro h
    have hfalse := h (a₁ := false) (a₂ := true) rfl
    simp at hfalse

theorem faithful_readout_does_not_supply_selector :
    FaithfulReadout (fun x : Empty => x) ∧ IsEmpty (Selector Empty) := by
  constructor
  · intro x
    exact x.elim
  · constructor
    intro s
    exact s.chosen.elim

section Transport

variable {G : Type*} [Group G]

def gaugeOpen (g₀ g₁ t : G) : G := g₁ * t * g₀⁻¹

structure FramePair where
  source : G
  target : G

def framedValue (f : FramePair (G := G)) (t : G) : G :=
  f.target⁻¹ * t * f.source

def gaugeFrame (g₀ g₁ : G) (f : FramePair (G := G)) : FramePair (G := G) where
  source := g₀ * f.source
  target := g₁ * f.target

theorem open_transport_not_invariant {g : G} (hg : g ≠ 1) :
    gaugeOpen 1 g 1 ≠ 1 := by
  simpa [gaugeOpen] using hg

theorem framedValue_gauge_invariant (g₀ g₁ t : G) (f : FramePair (G := G)) :
    framedValue (gaugeFrame g₀ g₁ f) (gaugeOpen g₀ g₁ t) = framedValue f t := by
  simp [framedValue, gaugeFrame, gaugeOpen, mul_assoc]

theorem closed_holonomy_invariant {G : Type*} [CommGroup G] (g h : G) :
    g * h * g⁻¹ = h := by
  simp

end Transport

section Detection

variable {R V W : Type*} [CommRing R]
  [AddCommGroup V] [Module R V]
  [AddCommGroup W] [Module R W]

def DetectsNonzeroOn (q : V →ₗ[R] W) (S : Set V) : Prop :=
  ∀ v ∈ S, q v ≠ 0 → v ≠ 0

theorem linear_response_detects_nonzero (q : V →ₗ[R] W) (S : Set V) :
    DetectsNonzeroOn q S := by
  intro v _ hq hv
  subst v
  exact hq (map_zero q)

theorem one_probe_detects_without_reconstructing :
    let q : (Fin 2 → ℚ) →ₗ[ℚ] ℚ := LinearMap.proj 0
    let S : Set (Fin 2 → ℚ) := {v | v 0 = 1}
    DetectsNonzeroOn q S ∧ ¬ Set.InjOn q S := by
  dsimp
  constructor
  · exact linear_response_detects_nonzero _ _
  · intro h
    let v : Fin 2 → ℚ := ![1, 0]
    let w : Fin 2 → ℚ := ![1, 1]
    have hv : v ∈ ({x | x 0 = 1} : Set (Fin 2 → ℚ)) := by decide
    have hw : w ∈ ({x | x 0 = 1} : Set (Fin 2 → ℚ)) := by decide
    have heq : (LinearMap.proj 0 : (Fin 2 → ℚ) →ₗ[ℚ] ℚ) v =
        (LinearMap.proj 0 : (Fin 2 → ℚ) →ₗ[ℚ] ℚ) w := by decide
    have hs := h hv hw heq
    have hcoord := congrFun hs 1
    norm_num [v, w] at hcoord

theorem jointlyFaithful_reconstructs_equality {ι : Type*}
    (q : ι → V →ₗ[R] W) (hq : JointlyFaithful q)
    {v₁ v₂ : V} (hread : ∀ i, q i v₁ = q i v₂) : v₁ = v₂ := by
  rw [jointlyFaithful_iff_point_separating] at hq
  have hz : v₁ - v₂ = 0 := hq (v₁ - v₂) (by
    intro i
    simp [hread i])
  exact sub_eq_zero.mp hz

theorem detection_does_not_imply_reconstruction :
    ∃ (q : (Fin 2 → ℚ) →ₗ[ℚ] ℚ) (S : Set (Fin 2 → ℚ)),
      DetectsNonzeroOn q S ∧ ¬ Set.InjOn q S := by
  refine ⟨LinearMap.proj 0, {v | v 0 = 1}, ?_⟩
  exact one_probe_detects_without_reconstructing

end Detection

end MariciFormal
