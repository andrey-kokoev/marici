import MariciFormal.DeterminantalProfilePresentation

/-!
Determinantal ideals commute with coefficient maps. Specialization is thereby
a typed base change of the profile, rather than an unrelated matrix operation.
-/

namespace MariciFormal

variable {R S : Type*} [CommRing R] [CommRing S]
variable {m n : Type*} [Fintype m] [Fintype n]
  [DecidableEq m] [DecidableEq n]

omit [Fintype m] [Fintype n] [DecidableEq m] [DecidableEq n] in
theorem map_matrixEntryIdeal (f : R →+* S) (matrix : Matrix m n R) :
    Ideal.map f (matrixEntryIdeal matrix) =
      matrixEntryIdeal (matrix.map f) := by
  rw [matrixEntryIdeal, matrixEntryIdeal, Ideal.map_span]
  congr 1
  ext polynomial
  constructor
  · rintro ⟨entry, ⟨ij, rfl⟩, rfl⟩
    exact ⟨ij, rfl⟩
  · rintro ⟨ij, rfl⟩
    exact ⟨matrix ij.1 ij.2, ⟨ij, rfl⟩, rfl⟩

theorem map_secondDeterminantalIdeal (f : R →+* S)
    (matrix : Matrix (Fin 2) (Fin 2) R) :
    Ideal.map f (secondDeterminantalIdeal matrix) =
      secondDeterminantalIdeal (f.mapMatrix matrix) := by
  rw [secondDeterminantalIdeal, secondDeterminantalIdeal, Ideal.map_span,
    Set.image_singleton, f.map_det]

noncomputable def mapTwoByTwoDeterminantalProfile (f : R →+* S)
    (profile : TwoByTwoDeterminantalProfile R) :
    TwoByTwoDeterminantalProfile S where
  first := Ideal.map f profile.first
  second := Ideal.map f profile.second

/-- Both stages of the profile commute with a coefficient-ring map. -/
theorem map_twoByTwoDeterminantalProfile (f : R →+* S)
    (matrix : Matrix (Fin 2) (Fin 2) R) :
    mapTwoByTwoDeterminantalProfile f (twoByTwoDeterminantalProfile matrix) =
      twoByTwoDeterminantalProfile (f.mapMatrix matrix) := by
  unfold mapTwoByTwoDeterminantalProfile twoByTwoDeterminantalProfile
  congr 1
  · exact map_matrixEntryIdeal f matrix
  · exact map_secondDeterminantalIdeal f matrix

theorem specializeMatrix_eq_mapMatrix
    (point : Fin 2 → Rat) (matrix : BivariateMatrix₂) :
    specializeMatrix point matrix = (MvPolynomial.eval point).mapMatrix matrix :=
  rfl

/-- Base change to the origin preserves the lower-minor distinction between
the determinant-collision fixtures. -/
theorem origin_baseChanged_entryIdeals_differ :
    Ideal.map (MvPolynomial.eval origin)
        (matrixEntryIdeal separateAxisMatrix) ≠
      Ideal.map (MvPolynomial.eval origin)
        (matrixEntryIdeal productAxisMatrix) := by
  rw [map_matrixEntryIdeal, map_matrixEntryIdeal]
  change matrixEntryIdeal (specializeMatrix origin separateAxisMatrix) ≠
    matrixEntryIdeal (specializeMatrix origin productAxisMatrix)
  rw [specializeAtOrigin_fixtures.1, specializeAtOrigin_fixtures.2]
  intro hideals
  have hone : (1 : Rat) ∈ matrixEntryIdeal (!![1, 0; 0, 0]) :=
    matrixEntry_mem _ 0 0
  rw [← hideals] at hone
  simp [matrixEntryIdeal] at hone

end MariciFormal
