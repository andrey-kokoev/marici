import MariciFormal.Sprint2

/-! Sprint 3 generic layer. Exact Ising matrices require the frozen Kitaev source packet. -/

namespace MariciFormal

section Fusion

variable (K Label : Type*) [CommRing K] [Fintype Label] [DecidableEq Label]

/-- Minimal finite fusion data. Coherence is data, not inferred from multiplicities. -/
structure FiniteFusionSystem where
  multiplicity : Label → Label → Label → Nat
  fusionDim : Nat
  associator : (Fin fusionDim → K) ≃ₗ[K] (Fin fusionDim → K)
  braiding : Label → Label → (Fin fusionDim → K) ≃ₗ[K] (Fin fusionDim → K)
  pentagon : Prop
  hexagon : Prop

namespace FiniteFusionSystem

variable {K Label} (F : FiniteFusionSystem K Label)

abbrev FusionSpace := Fin F.fusionDim → K

/-- A physical model must separately supply proofs of the named coherence laws. -/
structure Coherent where
  pentagon_holds : F.pentagon
  hexagon_holds : F.hexagon

end FiniteFusionSystem

end Fusion

section FusionQuotient

variable {R V W : Type*} [CommRing R]
  [AddCommGroup V] [Module R V] [AddCommGroup W] [Module R W]

/-- Fusion-space readout descent is ordinary canonical module-quotient descent. -/
theorem fusionProbe_descends_iff (K : Submodule R V) (q : V →ₗ[R] W) :
    DescendsThrough K q ↔ K ≤ LinearMap.ker q :=
  descendsThrough_iff K q

/-- A family descends precisely componentwise; no basis or complement is chosen. -/
theorem fusionFamily_descends_iff {ι : Type*} (K : Submodule R V)
    (q : ι → V →ₗ[R] W) :
    (∀ i, DescendsThrough K (q i)) ↔ ∀ i, K ≤ LinearMap.ker (q i) :=
  family_descendsThrough_iff K q

/-- The three disappearance mechanisms remain separated on fusion spaces. -/
theorem fusion_disappearance_mechanisms_distinct :
    Nonempty (AccessDenial (Fin 2)) ∧
    Nonempty (ReadoutLoss (Fin 2 → ℚ) ℚ) ∧
    (let B : Submodule ℚ (Fin 2 → ℚ) := ⊥
     let B' := Submodule.span ℚ {![1, 0]}
     let x : Fin 2 → ℚ := ![1, 0]
     B.mkQ x ≠ 0 ∧ successorMap B B' bot_le (B.mkQ x) = 0) := by
  refine ⟨⟨⟨Set.univ⟩⟩, readout_loss_leaves_object_nontrivial.2, ?_⟩
  exact collapse_can_kill_nonzero_class

end FusionQuotient

section AccessInterface

/-- Point separation and operator generation are independent interface conditions. -/
structure AccessInterface (R V W ι : Type*) [CommRing R]
    [AddCommGroup V] [Module R V] [AddCommGroup W] [Module R W] where
  probes : ι → V →ₗ[R] W
  constructors : Set (Module.End R V)
  pointSeparating : Prop
  operatorGenerating : Prop

theorem point_separation_does_not_imply_operator_generation :
    let q : Fin 2 → (Fin 2 → ℚ) →ₗ[ℚ] ℚ := fun i => LinearMap.proj i
    JointlyFaithful q ∧
      coordinateSwap ∉ accessibleImage
        ({coordinateProjector 0, coordinateProjector 1} :
          Set (Module.End ℚ (Fin 2 → ℚ))) := by
  exact ⟨two_coordinates_jointly_faithful,
    commuting_coordinates_omit_coherence.2⟩

end AccessInterface

section Condensation

variable {R V : Type*} [CommRing R] [AddCommGroup V] [Module R V]

/-- A boundary/condensation successor with explicit nested repair relations. -/
structure CondensationSuccessor where
  before : Submodule R V
  after : Submodule R V
  legal_enlargement : before ≤ after

namespace CondensationSuccessor

def map (C : CondensationSuccessor (R := R) (V := V)) :
    V ⧸ C.before →ₗ[R] V ⧸ C.after :=
  successorMap C.before C.after C.legal_enlargement

theorem representative_dies_iff (C : CondensationSuccessor (R := R) (V := V))
    (x : V) : C.map (C.before.mkQ x) = 0 ↔ x ∈ C.after :=
  successorMap_mk_eq_zero_iff _ _ _ _

/-- Composition needs exactly the two nesting witnesses; no extra splitting. -/
theorem map_comp {B B' B'' : Submodule R V} (h₁ : B ≤ B') (h₂ : B' ≤ B'') :
    (successorMap B' B'' h₂).comp (successorMap B B' h₁) =
      successorMap B B'' (h₁.trans h₂) :=
  successorMap_comp B B' B'' h₁ h₂

end CondensationSuccessor

end Condensation

end MariciFormal
