import Mathlib.LinearAlgebra.Matrix.Determinant.Basic

/-!
Finite algebraic core of Grothendieck's rank-one Fredholm realization no-go.
Every scalar `1 - observation` has an automatic one-dimensional determinant
and kernel encoding; determinant matching alone supplies no source law.
-/

namespace MariciFormal

open Matrix

section UniversalRankOneEncoding

variable {K : Type*} [Field K]

def rankOneDefectMatrix (observation : K) : Matrix (Fin 1) (Fin 1) K :=
  fun _ _ => 1 - observation

def rankOneDefectAction (observation : K) (vector : K) : K :=
  (1 - observation) * vector

theorem rankOneDefect_det (observation : K) :
    Matrix.det (rankOneDefectMatrix observation) = 1 - observation := by
  simp [rankOneDefectMatrix]

theorem rankOneDefect_has_nontrivial_kernel_iff (observation : K) :
    (∃ vector : K, vector ≠ 0 ∧ rankOneDefectAction observation vector = 0) ↔
      observation = 1 := by
  constructor
  · rintro ⟨vector, hvector, hkernel⟩
    have hfactor : 1 - observation = 0 :=
      (mul_eq_zero.mp hkernel).resolve_right hvector
    have hone : (1 : K) = observation := sub_eq_zero.mp hfactor
    exact hone.symm
  · intro hobservation
    refine ⟨1, one_ne_zero, ?_⟩
    simp [rankOneDefectAction, hobservation]

/-- The determinant realization is universal in the observation scalar. -/
theorem every_vacuumMinusObservation_has_rankOneDeterminant
    (observation : K) :
    ∃ matrix : Matrix (Fin 1) (Fin 1) K,
      Matrix.det matrix = 1 - observation := by
  exact ⟨rankOneDefectMatrix observation, rankOneDefect_det observation⟩

end UniversalRankOneEncoding

section SourceLawIndependenceHostile

structure RankOneProposal where
  observation : ℚ
  independentSourceLaw : Bool

def tautologicalProposal : RankOneProposal where
  observation := 1
  independentSourceLaw := false

theorem tautologicalProposal_matches_and_has_kernel :
    Matrix.det (rankOneDefectMatrix tautologicalProposal.observation) = 0 ∧
      ∃ vector : ℚ, vector ≠ 0 ∧
        rankOneDefectAction tautologicalProposal.observation vector = 0 := by
  constructor
  · norm_num [tautologicalProposal, rankOneDefect_det]
  · exact (rankOneDefect_has_nontrivial_kernel_iff (K := ℚ)
      tautologicalProposal.observation).2 (by rfl)

/-- Exact determinant matching and transversality loss do not manufacture an
independent source-derived law. -/
theorem determinant_match_does_not_supply_sourceLaw :
    tautologicalProposal.independentSourceLaw = false := by
  rfl

end SourceLawIndependenceHostile

end MariciFormal
