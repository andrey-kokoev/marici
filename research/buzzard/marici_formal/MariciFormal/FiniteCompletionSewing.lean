import MariciFormal.FiniteInstrumentReadout

/-!
Finite sewing laws shared by Grothendieck's boundary-bearing cuts and
Aspect's retained-plus-tail decompositions.

The results here are deliberately finite.  They do not assert convergence in
a completion, continuity of a trace map, or effective descent for an infinite
cover.
-/

namespace MariciFormal.FiniteCompletionSewing

open MariciFormal.FiniteInstrumentReadout

/-- Energy accumulated by a finite ordered list of adjacent cut lengths. -/
def segmentedPrefixEnergy (source : ℕ → ℚ) : List ℕ → ℚ
  | [] => 0
  | length :: rest =>
      finitePrefixEnergy source length +
        segmentedPrefixEnergy (shiftedEnergySource source length) rest

/-- Translating by two adjacent cuts is translating by their total length. -/
theorem shiftedEnergySource_add
    (source : ℕ → ℚ) (first second : ℕ) :
    shiftedEnergySource
        (shiftedEnergySource source first) second =
      shiftedEnergySource source (first + second) := by
  funext index
  simp [shiftedEnergySource, Nat.add_assoc]

/-- Strong finite theorem: sewing any finite ordered cut family recovers the
energy of the single prefix whose length is the sum of the cuts. -/
theorem segmentedPrefixEnergy_eq_total
    (source : ℕ → ℚ) (lengths : List ℕ) :
    segmentedPrefixEnergy source lengths =
      finitePrefixEnergy source lengths.sum := by
  induction lengths generalizing source with
  | nil => simp [segmentedPrefixEnergy, finitePrefixEnergy]
  | cons length rest ih =>
      rw [segmentedPrefixEnergy, ih]
      simpa using
        (finitePrefixEnergy_add source length rest.sum).symm

/-- The local record retains each segment's contribution instead of summing
it away. -/
def segmentEnergyRecord (source : ℕ → ℚ) : List ℕ → List ℚ
  | [] => []
  | length :: rest =>
      finitePrefixEnergy source length ::
        segmentEnergyRecord (shiftedEnergySource source length) rest

/-- Forgetting the local allocation by summing the record recovers the sewn
energy. -/
theorem segmentEnergyRecord_sum
    (source : ℕ → ℚ) (lengths : List ℕ) :
    (segmentEnergyRecord source lengths).sum =
      segmentedPrefixEnergy source lengths := by
  induction lengths generalizing source with
  | nil => rfl
  | cons length rest ih =>
      simp [segmentEnergyRecord, segmentedPrefixEnergy, ih]

/-- Finite refinement coherence: splitting one leading cut into two adjacent
cuts preserves the total sewn energy. -/
theorem split_leading_cut_preserves_total
    (source : ℕ → ℚ) (first second : ℕ) (rest : List ℕ) :
    segmentedPrefixEnergy source ((first + second) :: rest) =
      segmentedPrefixEnergy source (first :: second :: rest) := by
  rw [segmentedPrefixEnergy_eq_total, segmentedPrefixEnergy_eq_total]
  simp [Nat.add_assoc]

/-- A finite fixture with all energy concentrated at the second sample. -/
def secondSampleUnitSource : ℕ → ℚ
  | 1 => 1
  | _ => 0

/-- Hostile distinction: moving the cut changes the local allocation even
when both segmentations have the same sewn total.  Effective total sewing is
therefore weaker than equality of local records. -/
theorem moving_cut_changes_local_record_not_total :
    segmentEnergyRecord secondSampleUnitSource [1, 2] = [0, 1] ∧
      segmentEnergyRecord secondSampleUnitSource [2, 1] = [1, 0] ∧
      segmentedPrefixEnergy secondSampleUnitSource [1, 2] =
        segmentedPrefixEnergy secondSampleUnitSource [2, 1] := by
  norm_num [segmentEnergyRecord, segmentedPrefixEnergy,
    finitePrefixEnergy, shiftedEnergySource, secondSampleUnitSource,
    Finset.sum_range_succ]

/-- Coarsen a refined local record by merging its first two adjacent entries.
The map is explicit because equality of coarse and refined records is false. -/
def mergeLeadingRecord : List ℚ → List ℚ
  | first :: second :: rest => (first + second) :: rest
  | record => record

/-- Strong finite coherence theorem: the record of a split leading cut
coarsens exactly to the record of the unsplit cut. -/
theorem merge_split_leading_record
    (source : ℕ → ℚ) (first second : ℕ) (rest : List ℕ) :
    mergeLeadingRecord
        (segmentEnergyRecord source (first :: second :: rest)) =
      segmentEnergyRecord source ((first + second) :: rest) := by
  simp only [segmentEnergyRecord, mergeLeadingRecord]
  rw [finitePrefixEnergy_add]
  congr 1
  rw [shiftedEnergySource_add]

/-- Hostile countermodel: record coarsening is not injective.  Consequently a
coarse sewn record cannot reconstruct how its leading contribution was split.
-/
theorem mergeLeadingRecord_not_injective :
    ¬ Function.Injective mergeLeadingRecord := by
  intro h
  have equality := h (show mergeLeadingRecord [0, 1] =
    mergeLeadingRecord [1, 0] by norm_num [mergeLeadingRecord])
  norm_num at equality

/-- Hostile finite countermodel: a zero-valued translated tail does not imply
that the sewn record has zero energy, because the seam-bearing prefix remains.
-/
theorem zero_tail_does_not_determine_sewn_energy :
    finitePrefixEnergy
        (shiftedEnergySource seamOnlyUnitSource 1) 2 = 0 ∧
      segmentedPrefixEnergy seamOnlyUnitSource [1, 2] = 1 := by
  constructor
  · exact vanishingTail_does_not_erase_seamEnergy.2.1
  · norm_num [segmentedPrefixEnergy, finitePrefixEnergy,
      shiftedEnergySource, seamOnlyUnitSource]

end MariciFormal.FiniteCompletionSewing
