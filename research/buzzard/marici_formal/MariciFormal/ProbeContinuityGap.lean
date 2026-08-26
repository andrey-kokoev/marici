import Mathlib

/-!
Coordinate probes jointly separate finite-support packets, but no fixed finite
subfamily determines the total-sum endpoint.
-/

namespace MariciFormal

abbrev FinitePacket := Nat →₀ Rat

def coordinateProbe (j : Nat) (packet : FinitePacket) : Rat :=
  packet j

def totalEndpoint (packet : FinitePacket) : Rat :=
  packet.sum fun _ value => value

/-- The full coordinate family is jointly faithful on finite packets. -/
theorem coordinateProbes_jointly_faithful
    (packet : FinitePacket)
    (vanishes : ∀ j, coordinateProbe j packet = 0) :
    packet = 0 := by
  ext j
  exact vanishes j

/-- A finite probe family determines the endpoint only if common probe-zero
packets also have zero endpoint. -/
def FiniteProbeFamilyControlsEndpoint (observed : Finset Nat) : Prop :=
  ∀ packet : FinitePacket,
    (∀ j ∈ observed, coordinateProbe j packet = 0) →
      totalEndpoint packet = 0

private theorem exists_index_outside (observed : Finset Nat) :
    ∃ m : Nat, m ∉ observed := by
  by_cases h : observed.Nonempty
  · let m := observed.max' h + 1
    refine ⟨m, ?_⟩
    intro hm
    have hle : m ≤ observed.max' h := Finset.le_max' observed m hm
    dsimp [m] at hle
    omega
  · have hempty : observed = ∅ := Finset.not_nonempty_iff_eq_empty.mp h
    exact ⟨0, by simp [hempty]⟩

/-- Every finite observation set misses a unit packet with nonzero endpoint. -/
theorem finiteCoordinateFamily_has_endpoint_hostile
    (observed : Finset Nat) :
    ∃ packet : FinitePacket,
      (∀ j ∈ observed, coordinateProbe j packet = 0) ∧
      totalEndpoint packet = 1 := by
  obtain ⟨m, hm⟩ := exists_index_outside observed
  refine ⟨Finsupp.single m 1, ?_, ?_⟩
  · intro j hj
    have hjm : j ≠ m := by
      intro heq
      subst heq
      exact hm hj
    simp [coordinateProbe, hjm]
  · simp [totalEndpoint]

/-- Joint faithfulness does not collapse to endpoint control by a finite subfamily. -/
theorem noFiniteCoordinateFamilyControlsEndpoint :
    ∀ observed : Finset Nat,
      ¬ FiniteProbeFamilyControlsEndpoint observed := by
  intro observed controls
  obtain ⟨packet, probeZero, endpointOne⟩ :=
    finiteCoordinateFamily_has_endpoint_hostile observed
  have endpointZero := controls packet probeZero
  linarith

end MariciFormal
