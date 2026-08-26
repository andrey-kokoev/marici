import MariciFormal.LocalSmithProfile

/-!
Smith exponents determine a depth-by-depth persistence barcode. The number of
born generators does not determine how long those generators persist.
-/

namespace MariciFormal

def survivingDirectionsAtDepth (profile : SmithProfile₂) (depth : Nat) : Nat :=
  (if depth ≤ profile.1 then 1 else 0) +
    (if depth ≤ profile.2 then 1 else 0)

def defectBarcode (profile : SmithProfile₂) : List Nat :=
  (List.range (max profile.1 profile.2)).map
    (fun offset => survivingDirectionsAtDepth profile (offset + 1))

theorem deepSingleAlias_barcode :
    defectBarcode deepSingleAlias = [1, 1] := by
  decide

theorem twoShallowAliases_barcode :
    defectBarcode twoShallowAliases = [2] := by
  decide

theorem equalTotalLength_distinctBarcodes :
    determinantOrder deepSingleAlias = determinantOrder twoShallowAliases ∧
      defectBarcode deepSingleAlias ≠ defectBarcode twoShallowAliases := by
  decide

def oneShallowAlias : SmithProfile₂ := (0, 1)

/-- First derived specialization sees births, but not their persistence depth. -/
theorem bornGeneratorCount_does_not_determine_depth :
    seamCorank oneShallowAlias = seamCorank deepSingleAlias ∧
      determinantOrder oneShallowAlias ≠ determinantOrder deepSingleAlias ∧
      defectBarcode oneShallowAlias ≠ defectBarcode deepSingleAlias := by
  decide

theorem firstBarcodeLayer_eq_corank
    (profile : SmithProfile₂) :
    survivingDirectionsAtDepth profile 1 = seamCorank profile := by
  rcases profile with ⟨first, second⟩
  simp [survivingDirectionsAtDepth, seamCorank, Nat.one_le_iff_ne_zero]

end MariciFormal
