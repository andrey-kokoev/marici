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

/-- Merge the second and third entries of a local record. -/
def mergeSecondRecord : List ℚ → List ℚ
  | first :: second :: third :: rest =>
      first :: (second + third) :: rest
  | record => record

/-- Finite folded-square coherence: the two binary coarsening paths from a
three-piece record agree.  The proof uses associativity explicitly. -/
theorem merge_three_record_coherent
    (first second third : ℚ) (rest : List ℚ) :
    mergeLeadingRecord
        (mergeLeadingRecord (first :: second :: third :: rest)) =
      mergeLeadingRecord
        (mergeSecondRecord (first :: second :: third :: rest)) := by
  simp [mergeLeadingRecord, mergeSecondRecord, add_assoc]

/-- A binary gluing law together with the coherence datum needed for three
local pieces. -/
structure CoherentBinarySewing (Value : Type*) where
  sew : Value → Value → Value
  associator : ∀ first second third,
    sew (sew first second) third = sew first (sew second third)

/-- Any witness-bearing sewing law yields a coherent three-piece fold. -/
theorem CoherentBinarySewing.fold_three
    {Value : Type*} (sewing : CoherentBinarySewing Value)
    (first second third : Value) :
    sewing.sew (sewing.sew first second) third =
      sewing.sew first (sewing.sew second third) :=
  sewing.associator first second third

/-- Hostile binary law: pairwise sewing can be total while three-piece
coherence fails. -/
def subtractiveSew (first second : ℤ) : ℤ := first - second

theorem pairwise_sewing_does_not_supply_triple_coherence :
    subtractiveSew (subtractiveSew 1 1) 1 ≠
      subtractiveSew 1 (subtractiveSew 1 1) := by
  norm_num [subtractiveSew]

/-- A finite refinement certificate carries the actual comparison map and its
total-preservation law.  Equality of totals is a consequence, not a substitute
for this data. -/
structure RecordCoarseningCertificate where
  fine : List ℚ
  coarse : List ℚ
  coarsen : List ℚ → List ℚ
  mapsRecord : coarsen fine = coarse
  preservesTotal : ∀ record, (coarsen record).sum = record.sum

/-- Every typed coarsening certificate transports the total. -/
theorem RecordCoarseningCertificate.equal_total
    (certificate : RecordCoarseningCertificate) :
    certificate.coarse.sum = certificate.fine.sum := by
  rw [← certificate.mapsRecord]
  exact certificate.preservesTotal certificate.fine

/-- Identity refinement certificate on a finite local record. -/
def RecordCoarseningCertificate.identity (record : List ℚ) :
    RecordCoarseningCertificate where
  fine := record
  coarse := record
  coarsen := id
  mapsRecord := rfl
  preservesTotal := fun _ => rfl

/-- Partial composition: the first coarse record must be exactly the second
fine record.  Aggregate equality is intentionally insufficient. -/
def RecordCoarseningCertificate.compose
    (first second : RecordCoarseningCertificate)
    (intermediate : first.coarse = second.fine) :
    RecordCoarseningCertificate where
  fine := first.fine
  coarse := second.coarse
  coarsen := second.coarsen ∘ first.coarsen
  mapsRecord := by
    simp only [Function.comp_apply, first.mapsRecord]
    rw [intermediate, second.mapsRecord]
  preservesTotal := by
    intro record
    rw [Function.comp_apply, second.preservesTotal, first.preservesTotal]

/-- Composition retains the expected composite comparison map. -/
theorem RecordCoarseningCertificate.compose_coarsen
    (first second : RecordCoarseningCertificate)
    (intermediate : first.coarse = second.fine) :
    (first.compose second intermediate).coarsen =
      second.coarsen ∘ first.coarsen := rfl

/-- Certificates are determined by their typed endpoints and comparison map;
the law fields are propositions. -/
@[ext] theorem RecordCoarseningCertificate.ext
    {first second : RecordCoarseningCertificate}
    (fine : first.fine = second.fine)
    (coarse : first.coarse = second.coarse)
    (coarsen : first.coarsen = second.coarsen) :
    first = second := by
  cases first
  cases second
  simp_all

/-- Left identity for typed finite refinement composition. -/
theorem RecordCoarseningCertificate.identity_comp
    (certificate : RecordCoarseningCertificate) :
    (RecordCoarseningCertificate.identity certificate.fine).compose
        certificate rfl = certificate := by
  apply RecordCoarseningCertificate.ext <;> rfl

/-- Right identity for typed finite refinement composition. -/
theorem RecordCoarseningCertificate.comp_identity
    (certificate : RecordCoarseningCertificate) :
    certificate.compose
        (RecordCoarseningCertificate.identity certificate.coarse) rfl =
      certificate := by
  apply RecordCoarseningCertificate.ext <;> rfl

/-- Associativity for three admitted certificate compositions.  Both
intermediate equalities remain explicit inputs. -/
theorem RecordCoarseningCertificate.compose_assoc
    (first second third : RecordCoarseningCertificate)
    (firstSecond : first.coarse = second.fine)
    (secondThird : second.coarse = third.fine) :
    (first.compose second firstSecond).compose third secondThird =
      first.compose (second.compose third secondThird) firstSecond := by
  apply RecordCoarseningCertificate.ext <;> rfl

/-- Hostile intermediate boundary: these records have equal totals but are
not the same labelled/local record, so aggregate equality cannot provide the
equality witness required by `compose`. -/
theorem equal_intermediate_totals_do_not_type_composition :
    ([0, 1] : List ℚ).sum = ([1, 0] : List ℚ).sum ∧
      ([0, 1] : List ℚ) ≠ [1, 0] := by
  norm_num

/-- `mergeLeadingRecord` preserves the sum of every record. -/
theorem mergeLeadingRecord_sum (record : List ℚ) :
    (mergeLeadingRecord record).sum = record.sum := by
  cases record with
  | nil => rfl
  | cons first rest =>
      cases rest with
      | nil => rfl
      | cons second tail =>
          simp [mergeLeadingRecord, add_assoc]

/-- The split leading segment record has a source-typed coarsening
certificate, not merely an equal-total coincidence. -/
def splitLeadingRecordCertificate
    (source : ℕ → ℚ) (first second : ℕ) (rest : List ℕ) :
    RecordCoarseningCertificate where
  fine := segmentEnergyRecord source (first :: second :: rest)
  coarse := segmentEnergyRecord source ((first + second) :: rest)
  coarsen := mergeLeadingRecord
  mapsRecord := merge_split_leading_record source first second rest
  preservesTotal := mergeLeadingRecord_sum

/-- Compatibility with a named label transport is pointwise data. -/
def CompatibleIndexedRecord
    {Label : Type*} (transport : Label → Label)
    (source target : Label → ℚ) : Prop :=
  ∀ label, target (transport label) = source label

/-- Hostile labelled fixture: equal aggregate totals do not imply
compatibility with the declared identity transport. -/
theorem equal_total_does_not_supply_indexed_transport :
    let source : Bool → ℚ := fun label => if label then 1 else 0
    let target : Bool → ℚ := fun label => if label then 0 else 1
    source false + source true = target false + target true ∧
      ¬ CompatibleIndexedRecord id source target := by
  dsimp [CompatibleIndexedRecord]
  constructor
  · norm_num
  · intro h
    have := h false
    norm_num at this

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
