import MariciFormal.FiniteCharacterCompleteness
import Mathlib.LinearAlgebra.Matrix.Basis

/-!
Invertible square synthesis matrix attached to the complete finite-abelian
character basis. Orthogonal normalization and the convolution matrix identity
remain separate theorems.
-/

namespace MariciFormal

variable {G : Type*} [Fintype G] [AddCommGroup G]

/-- A noncanonical index equivalence supplied only by the equality between the
number of complex characters and the group cardinality. -/
noncomputable def characterIndexEquiv : G ≃ AddChar G ℂ :=
  Fintype.equivOfCardEq AddChar.card_eq.symm

/-- The point-mass coordinate basis, reindexed by characters so that it and
the character basis have the same square matrix index. -/
noncomputable def coordinateBasisByCharacter :
    Basis (AddChar G ℂ) ℂ (G → ℂ) :=
  (Pi.basisFun ℂ G).reindex characterIndexEquiv

/-- Change-of-basis matrix whose columns are the complete complex character
basis written in reindexed point-mass coordinates. -/
noncomputable def finiteCharacterSynthesisMatrix :
    Matrix (AddChar G ℂ) (AddChar G ℂ) ℂ :=
  coordinateBasisByCharacter.toMatrix (AddChar.complexBasis G)

/-- Completeness of the character family makes its square synthesis matrix
invertible. No orthogonal normalization or arithmetic kernel is used. -/
theorem finiteCharacterSynthesisMatrix_isUnit :
    IsUnit (finiteCharacterSynthesisMatrix (G := G)) := by
  classical
  letI : Invertible (finiteCharacterSynthesisMatrix (G := G)) :=
    Module.Basis.invertibleToMatrix (coordinateBasisByCharacter (G := G))
      (AddChar.complexBasis G)
  exact isUnit_of_invertible _

/-- The inverse is the reverse change-of-basis matrix. -/
theorem finiteCharacterSynthesisMatrix_mul_reverse :
    finiteCharacterSynthesisMatrix (G := G) *
        (AddChar.complexBasis G).toMatrix
          (coordinateBasisByCharacter (G := G)) = 1 := by
  classical
  exact Module.Basis.toMatrix_mul_toMatrix_flip _ _

end MariciFormal
