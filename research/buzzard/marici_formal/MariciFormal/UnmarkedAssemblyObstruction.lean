import Mathlib.Data.ZMod.Basic

/-!
The finite source-symmetry obstruction in Grothendieck's Phase-I unmarked
assembly packet. Independent cyclic relabellings act transitively on the
sixteen edge pairs, and no edge pair is invariant under every relabelling.
-/

namespace MariciFormal

abbrev QuadrilateralEdge := ZMod 4

abbrev QuadrilateralSewingChoice :=
  QuadrilateralEdge × QuadrilateralEdge

/-- Independent rotations of the two quadrilateral boundary-edge sets. -/
def rotateSewingChoice
    (leftShift rightShift : QuadrilateralEdge)
    (choice : QuadrilateralSewingChoice) : QuadrilateralSewingChoice :=
  (choice.1 + leftShift, choice.2 + rightShift)

/-- Independent rotations act transitively on all sixteen sewing choices. -/
theorem rotateSewingChoice_transitive
    (source target : QuadrilateralSewingChoice) :
    ∃ leftShift rightShift,
      rotateSewingChoice leftShift rightShift source = target := by
  refine ⟨target.1 - source.1, target.2 - source.2, ?_⟩
  ext <;> simp [rotateSewingChoice, add_comm]

/-- Rotating just the left boundary by one edge moves every sewing choice. -/
theorem left_quarter_rotation_has_no_fixed_choice
    (choice : QuadrilateralSewingChoice) :
    rotateSewingChoice 1 0 choice ≠ choice := by
  intro hfixed
  have hleft := congrArg Prod.fst hfixed
  have hone : (1 : QuadrilateralEdge) = 0 := by
    apply add_left_cancel (a := choice.1)
    simpa [rotateSewingChoice]
      using hleft
  exact one_ne_zero hone

/-- Hence no unmarked sewing choice is natural under all independent source
rotations; invariance under the larger independent dihedral action is
therefore impossible as well. -/
theorem no_unmarked_rotation_invariant_sewing_choice :
    ¬ ∃ choice : QuadrilateralSewingChoice,
      ∀ leftShift rightShift,
        rotateSewingChoice leftShift rightShift choice = choice := by
  rintro ⟨choice, hinvariant⟩
  exact left_quarter_rotation_has_no_fixed_choice choice
    (hinvariant 1 0)

/-- Once a sewing choice is marked, the identity relabellings lie in its
stabilizer. This records the typed marked operation without claiming a
canonical choice before marking. -/
theorem marked_choice_has_identity_stabilizer
    (choice : QuadrilateralSewingChoice) :
    rotateSewingChoice 0 0 choice = choice := by
  simp [rotateSewingChoice]

end MariciFormal
