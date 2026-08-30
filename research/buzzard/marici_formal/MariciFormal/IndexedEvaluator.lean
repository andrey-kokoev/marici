import MariciFormal.Sprint1

/-!
A single indexed evaluator schema can present an infinite jointly faithful
family without yielding any faithful finite instantiated port family.
-/

namespace MariciFormal

abbrev IndexedPacket := Nat →₀ Rat

/-- One evaluator program schema with a logical coordinate index. -/
def indexedEvaluator (index : Nat) : IndexedPacket →ₗ[Rat] Rat :=
  Finsupp.lapply index

theorem indexedEvaluator_jointlyFaithful :
    JointlyFaithful indexedEvaluator := by
  rw [jointlyFaithful_iff_point_separating]
  intro packet vanishes
  ext index
  exact vanishes index

private theorem index_outside_finite_set (observed : Finset Nat) :
    ∃ index, index ∉ observed := by
  by_cases h : observed.Nonempty
  · let index := observed.max' h + 1
    refine ⟨index, ?_⟩
    intro hmem
    have hle := Finset.le_max' observed index hmem
    dsimp [index] at hle
    omega
  · rw [Finset.not_nonempty_iff_eq_empty.mp h]
    exact ⟨0, by simp⟩

/-- Every finite instantiation of the indexed evaluator misses a nonzero packet. -/
theorem finiteIndexedEvaluatorFamily_not_jointlyFaithful
    (observed : Finset Nat) :
    ¬ JointlyFaithful
      (fun index : {j : Nat // j ∈ observed} => indexedEvaluator index.1) := by
  obtain ⟨missing, hmissing⟩ := index_outside_finite_set observed
  intro faithful
  rw [jointlyFaithful_iff_point_separating] at faithful
  let hostile : IndexedPacket := Finsupp.single missing 1
  have hostileZero : hostile = 0 := faithful hostile (by
    intro index
    have hne : index.1 ≠ missing := by
      intro heq
      subst heq
      exact hmissing index.2
    simp [indexedEvaluator, hostile, hne])
  have atMissing := DFunLike.congr_fun hostileZero missing
  simp [hostile] at atMissing

/-- Finite schema and infinite static rank coexist in the same exact fixture. -/
theorem indexedSchema_faithful_but_no_finite_instance_is :
    JointlyFaithful indexedEvaluator ∧
      ∀ observed : Finset Nat,
        ¬ JointlyFaithful
          (fun index : {j : Nat // j ∈ observed} => indexedEvaluator index.1) :=
  ⟨indexedEvaluator_jointlyFaithful,
    finiteIndexedEvaluatorFamily_not_jointlyFaithful⟩

end MariciFormal
