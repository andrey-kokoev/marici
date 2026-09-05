import Mathlib.AlgebraicTopology.SimplicialSet.StrictSegal
import Mathlib.CategoryTheory.Category.Preorder
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.MonoidAlgebra.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Sigma
import Mathlib.Data.Fintype.Powerset
import Mathlib.Data.Fintype.BigOperators
import Mathlib.Combinatorics.SimpleGraph.Connectivity.Connected
import Mathlib.RingTheory.Ideal.Quotient.Operations

/-! Generic convex polygon chords, noncrossing dissections, and their nerve. -/

open CategoryTheory

namespace Marici.Polygon

set_option checkBinderAnnotations false
set_option linter.style.haveILetI false

/-- A canonical ordered representative of a polygon diagonal. The endpoint
conditions exclude consecutive vertices and the cyclic boundary edge. -/
structure Diagonal (n : ℕ) where
  lo : Fin n
  hi : Fin n
  ordered : lo < hi
  notConsecutive : hi.val ≠ lo.val + 1
  notWrap : ¬ (lo.val = 0 ∧ hi.val + 1 = n)
  deriving DecidableEq

theorem diagonal_eq_of_endpoints {n : ℕ} {a b : Diagonal n}
    (hlo : a.lo = b.lo) (hhi : a.hi = b.hi) : a = b := by
  cases a
  cases b
  cases hlo
  cases hhi
  rfl

/-- Alternation of four endpoints is exactly crossing for straight chords in a
convex polygon. -/
def Crosses {n : ℕ} (a b : Diagonal n) : Prop :=
  (a.lo < b.lo ∧ b.lo < a.hi ∧ a.hi < b.hi) ∨
  (b.lo < a.lo ∧ a.lo < b.hi ∧ b.hi < a.hi)

/-- Strict membership in the linear vertex interval cut out by the canonical
ordered representative of a chord. The complementary interval includes the
cyclic wrap-around. -/
def InChordInterval {n : ℕ} (c : Diagonal n) (v : Fin n) : Prop :=
  c.lo < v ∧ v < c.hi

/-- Two chords have no common endpoint. This hypothesis separates genuine
side-switching from meeting at the boundary of a region. -/
def EndpointDisjoint {n : ℕ} (a b : Diagonal n) : Prop :=
  a.lo ≠ b.lo ∧ a.lo ≠ b.hi ∧ a.hi ≠ b.lo ∧ a.hi ≠ b.hi

theorem endpointDisjoint_symmetric {n : ℕ} {a b : Diagonal n} :
    EndpointDisjoint a b ↔ EndpointDisjoint b a := by
  unfold EndpointDisjoint
  tauto

/-- Exhaustive split between the generic endpoint-disjoint case and the four
possible shared-endpoint incidences. -/
theorem endpointDisjoint_or_sharedEndpoint {n : ℕ} (a b : Diagonal n) :
    EndpointDisjoint a b ∨
      a.lo = b.lo ∨ a.lo = b.hi ∨ a.hi = b.lo ∨ a.hi = b.hi := by
  unfold EndpointDisjoint
  tauto

/-- If an endpoint-disjoint chord switches strict sides of another chord,
the two chords cross. This is the geometric implication needed to construct
regions from consistent side data. -/
theorem crosses_of_interval_separates {n : ℕ} {a b : Diagonal n}
    (hdisj : EndpointDisjoint a b)
    (hsep : (InChordInterval a b.lo ∧ ¬ InChordInterval a b.hi) ∨
      (¬ InChordInterval a b.lo ∧ InChordInterval a b.hi)) :
    Crosses a b := by
  unfold Crosses InChordInterval EndpointDisjoint at *
  rcases hdisj with ⟨hll, hlh, hhl, hhh⟩
  have hllv : a.lo.val ≠ b.lo.val := fun h => hll (Fin.ext h)
  have hlhv : a.lo.val ≠ b.hi.val := fun h => hlh (Fin.ext h)
  have hhlv : a.hi.val ≠ b.lo.val := fun h => hhl (Fin.ext h)
  have hhhv : a.hi.val ≠ b.hi.val := fun h => hhh (Fin.ext h)
  rcases hsep with ⟨hlin, hhout⟩ | ⟨hlout, hhin⟩
  · rcases lt_trichotomy b.hi a.hi with hlt | heq | hgt
    · exact False.elim (hhout ⟨hlin.1.trans b.ordered, hlt⟩)
    · exact False.elim (hhh heq.symm)
    · exact Or.inl ⟨hlin.1, hlin.2, hgt⟩
  · rcases lt_trichotomy b.lo a.lo with hlt | heq | hgt
    · exact Or.inr ⟨hlt, hhin.1, hhin.2⟩
    · exact False.elim (hll heq.symm)
    · exact False.elim (hlout ⟨hgt, b.ordered.trans hhin.2⟩)

/-- Hence a noncrossing endpoint-disjoint chord has both endpoints on the same
strict side of the cut. -/
theorem same_interval_side_of_not_crosses {n : ℕ} {a b : Diagonal n}
    (hdisj : EndpointDisjoint a b) (hnc : ¬ Crosses a b) :
    InChordInterval a b.lo ↔ InChordInterval a b.hi := by
  by_contra h
  apply hnc
  apply crosses_of_interval_separates hdisj
  tauto

/-- The strict side of a chord endpoint, represented computationally. -/
noncomputable def strictSide {n : ℕ} (c : Diagonal n) (v : Fin n) : Bool := by
  classical
  exact decide (InChordInterval c v)

@[simp] theorem strictSide_eq_true_iff {n : ℕ}
    (c : Diagonal n) (v : Fin n) :
    strictSide c v = true ↔ InChordInterval c v := by
  classical
  simp [strictSide]

@[simp] theorem strictSide_eq_false_iff {n : ℕ}
    (c : Diagonal n) (v : Fin n) :
    strictSide c v = false ↔ ¬ InChordInterval c v := by
  classical
  simp [strictSide]

/-- A true-side retained set is the closed linear interval cut out by the
chord endpoints. -/
theorem mem_retained_true_iff {n : ℕ}
    (c : Diagonal n) (v : Fin n) :
    (v = c.lo ∨ v = c.hi ∨ strictSide c v = true) ↔
      c.lo.val ≤ v.val ∧ v.val ≤ c.hi.val := by
  rw [strictSide_eq_true_iff]
  simp only [Fin.ext_iff]
  unfold InChordInterval
  have hc := c.ordered
  omega

/-- A false-side retained set is the complementary closed cyclic interval. -/
theorem mem_retained_false_iff {n : ℕ}
    (c : Diagonal n) (v : Fin n) :
    (v = c.lo ∨ v = c.hi ∨ strictSide c v = false) ↔
      v.val ≤ c.lo.val ∨ c.hi.val ≤ v.val := by
  rw [strictSide_eq_false_iff]
  simp only [Fin.ext_iff]
  unfold InChordInterval
  have hc := c.ordered
  omega

/-- Two overlapping closed intervals whose endpoints do not interleave are
nested. This is the linear-order core of the regional boundary argument. -/
theorem closedIntervals_nested_of_overlap_not_interleaves
    (a b c d w : ℕ) (hab : a < b)
    (hdisj : a ≠ c ∧ a ≠ d ∧ b ≠ c ∧ b ≠ d)
    (hnc : ¬((a < c ∧ c < b ∧ b < d) ∨
      (c < a ∧ a < d ∧ d < b)))
    (hw : a ≤ w ∧ w ≤ b ∧ c ≤ w ∧ w ≤ d) :
    (a ≤ c ∧ d ≤ b) ∨ (c ≤ a ∧ b ≤ d) := by
  by_cases hac : a ≤ c
  · by_cases hdb : d ≤ b
    · exact Or.inl ⟨hac, hdb⟩
    · right
      constructor <;> omega
  · right
    constructor <;> omega

/-- Crossing forces the endpoints of one chord onto opposite strict sides
of the other. -/
theorem strictSide_ne_of_crosses {n : ℕ} {a b : Diagonal n}
    (h : Crosses a b) : strictSide b a.lo ≠ strictSide b a.hi := by
  rcases h with h | h
  · have hlo : ¬ InChordInterval b a.lo := by
      unfold InChordInterval
      omega
    have hhi : InChordInterval b a.hi := by
      unfold InChordInterval
      omega
    simp [strictSide, hlo, hhi]
  · have hlo : InChordInterval b a.lo := by
      unfold InChordInterval
      omega
    have hhi : ¬ InChordInterval b a.hi := by
      unfold InChordInterval
      omega
    simp [strictSide, hlo, hhi]

/-- A noncrossing endpoint-disjoint chord has a well-defined strict side:
either endpoint computes the same value. -/
theorem strictSide_endpoint_independent {n : ℕ} {a b : Diagonal n}
    (hdisj : EndpointDisjoint a b) (hnc : ¬ Crosses a b) :
    strictSide a b.lo = strictSide a b.hi := by
  classical
  have hsame := same_interval_side_of_not_crosses hdisj hnc
  by_cases hlo : InChordInterval a b.lo
  · have hhi := hsame.mp hlo
    simp [strictSide, hlo, hhi]
  · have hhi : ¬ InChordInterval a b.hi := fun h => hlo (hsame.mpr h)
    simp [strictSide, hlo, hhi]

theorem crosses_symmetric {n : ℕ} {a b : Diagonal n} :
    Crosses a b ↔ Crosses b a := by
  constructor <;> intro h <;> rcases h with h | h
  · exact Or.inr h
  · exact Or.inl h
  · exact Or.inr h
  · exact Or.inl h

noncomputable instance {n : ℕ} (a b : Diagonal n) : Decidable (Crosses a b) :=
  Classical.propDecidable _

/-- A dissection is a finite collection of pairwise noncrossing diagonals. -/
def IsDissection {n : ℕ} (s : Finset (Diagonal n)) : Prop :=
  ∀ ⦃a⦄, a ∈ s → ∀ ⦃b⦄, b ∈ s → a ≠ b → ¬ Crosses a b

/-- Noncrossing is inherited by every subfamily. -/
theorem isDissection_subset {n : ℕ} {s t : Finset (Diagonal n)}
    (ht : IsDissection t) (hst : s ⊆ t) : IsDissection s := by
  intro a ha b hb hab
  exact ht (hst ha) (hst hb) hab

/-- All dissections of the canonical convex `n`-gon. -/
def Dissection (n : ℕ) := {s : Finset (Diagonal n) // IsDissection s}

instance (n : ℕ) : LE (Dissection n) :=
  ⟨fun D E => D.val ⊆ E.val⟩

instance (n : ℕ) : PartialOrder (Dissection n) where
  le_refl _ := Finset.Subset.rfl
  le_trans _ _ _ := Finset.Subset.trans
  le_antisymm D E hDE hED := Subtype.ext (Finset.Subset.antisymm hDE hED)

noncomputable instance diagonalFintype (n : ℕ) : Fintype (Diagonal n) := by
  let endpoint : Diagonal n → Fin n × Fin n := fun d => (d.lo, d.hi)
  exact Fintype.ofInjective endpoint (by
    rintro ⟨alo, ahi, ha, hc, hw⟩ ⟨blo, bhi, hb, hd, hx⟩ h
    change (alo, ahi) = (blo, bhi) at h
    have hlo : alo = blo := congrArg Prod.fst h
    have hhi : ahi = bhi := congrArg Prod.snd h
    cases hlo
    cases hhi
    rfl)

noncomputable instance dissectionFintype (n : ℕ) : Fintype (Dissection n) :=
  Fintype.ofInjective Subtype.val Subtype.val_injective

/-- The empty dissection. -/
def empty (n : ℕ) : Dissection n := ⟨∅, by simp [IsDissection]⟩

/-- The dissection consisting of one diagonal. -/
def singletonDissection {n : ℕ} (d : Diagonal n) : Dissection n := by
  refine ⟨{d}, ?_⟩
  intro a ha b hb hab
  simp only [Finset.mem_singleton] at ha hb
  subst a
  subst b
  exact False.elim (hab rfl)

/-- Refinement is literal inclusion of diagonal sets. -/
theorem refinement_iff_subset {n : ℕ} (D E : Dissection n) :
    D ≤ E ↔ D.val ⊆ E.val := Iff.rfl

/-- A diagonal is admissible above `D` when it is new and crosses none of the
already selected cuts. These, rather than all diagonals outside `D`, form the
correct domain for regional addressing. -/
def CompatibleWith {n : ℕ} (D : Dissection n) (d : Diagonal n) : Prop :=
  ∀ c ∈ D.1, ¬ Crosses d c

/-- Candidate refinement diagonals above `D`. -/
def OptionalDiagonal {n : ℕ} (D : Dissection n) :=
  {d : Diagonal n // d ∉ D.1 ∧ CompatibleWith D d}

/-- Canonical endpoint used to locate a chord relative to a cut. If its lower
endpoint lies on the cut boundary, use its upper endpoint; otherwise use its
lower endpoint. For a new canonical diagonal, this resolves the shared-endpoint
case without choosing extra geometric data. -/
noncomputable def sideWitness {n : ℕ} (c d : Diagonal n) : Fin n := by
  classical
  exact if d.lo = c.lo ∨ d.lo = c.hi then d.hi else d.lo

/-- Side of a whole chord relative to a cut, including chords incident to that
cut. -/
noncomputable def chordSide {n : ℕ} (c d : Diagonal n) : Bool :=
  strictSide c (sideWitness c d)

@[simp] theorem chordSide_eq_lower_of_lower_not_endpoint {n : ℕ}
    (c d : Diagonal n) (h : d.lo ≠ c.lo ∧ d.lo ≠ c.hi) :
    chordSide c d = strictSide c d.lo := by
  classical
  simp [chordSide, sideWitness, h.1, h.2]

@[simp] theorem chordSide_eq_upper_of_lower_endpoint {n : ℕ}
    (c d : Diagonal n) (h : d.lo = c.lo ∨ d.lo = c.hi) :
    chordSide c d = strictSide c d.hi := by
  classical
  simp [chordSide, sideWitness, h]

/-- Two crossing chords that are each compatible with a third cut occupy the
same side of that cut. Thus a crossing pair cannot acquire different regional
signatures. -/
theorem chordSide_eq_of_crosses_of_compatible {n : ℕ}
    (c a b : Diagonal n) (hac : ¬ Crosses a c) (hbc : ¬ Crosses b c)
    (hab : Crosses a b) : chordSide c a = chordSide c b := by
  classical
  unfold chordSide sideWitness strictSide
  split <;> split <;> rename_i ha hb
  all_goals
    congr 1
    apply propext
    unfold InChordInterval Crosses at *
    rcases hab with hab | hab
    all_goals
      simp only [not_or, not_and_or, not_lt] at hac hbc
      rcases hac with ⟨hac₁, hac₂⟩
      rcases hbc with ⟨hbc₁, hbc₂⟩
      omega

/-- Full side data of a candidate diagonal relative to every selected cut. -/
noncomputable def canonicalCutSideSignature {n : ℕ} (D : Dissection n)
    (d : Diagonal n) : {c // c ∈ D.1} → Bool :=
  fun c => chordSide c.1 d

/-- Side data using the lower endpoint; retained as the endpoint-disjoint
specialization of the full signature. -/
noncomputable def cutSideSignature {n : ℕ} (D : Dissection n)
    (d : Diagonal n) : {c // c ∈ D.1} → Bool :=
  fun c => strictSide c.1 d.lo

/-- On cuts disjoint from both endpoints, the full signature reduces to the
previous lower-endpoint signature. -/
theorem canonicalCutSideSignature_eq_cutSideSignature {n : ℕ}
    (D : Dissection n) (d : Diagonal n)
    (hdisj : ∀ c : {c // c ∈ D.1}, EndpointDisjoint c.1 d) :
    canonicalCutSideSignature D d = cutSideSignature D d := by
  funext c
  apply chordSide_eq_lower_of_lower_not_endpoint
  exact ⟨Ne.symm (hdisj c).1, Ne.symm (hdisj c).2.2.1⟩

/-- Cyclic successor of a vertex. The existence of the input vertex supplies
the required positivity of `n`. -/
def cyclicSucc {n : ℕ} (i : Fin n) : Fin n :=
  ⟨(i.val + 1) % n, Nat.mod_lt _ (Nat.zero_lt_of_lt i.isLt)⟩

/-- Side occupied by the boundary edge beginning at `i`. If `i` is an endpoint
of the cut, its cyclic successor is used; the diagonal axioms ensure this
selects the incident face rather than the cut itself. -/
noncomputable def boundaryEdgeSide {n : ℕ} (c : Diagonal n) (i : Fin n) : Bool := by
  classical
  exact if i = c.lo ∨ i = c.hi then strictSide c (cyclicSucc i)
    else strictSide c i

/-- Complete side signature of a cyclic boundary edge relative to `D`. -/
noncomputable def boundaryEdgeSignature {n : ℕ} (D : Dissection n)
    (i : Fin n) : {c // c ∈ D.1} → Bool :=
  fun c => boundaryEdgeSide c.1 i

/-- Canonical candidate regions are exactly side signatures realized by cyclic
boundary edges. This includes triangular regions with no internal diagonal. -/
def CanonicalRegion {n : ℕ} (D : Dissection n) :=
  {s : {c // c ∈ D.1} → Bool // ∃ i : Fin n, boundaryEdgeSignature D i = s}

/-- Every boundary edge has its canonical region. -/
noncomputable def boundaryEdgeRegion {n : ℕ} (D : Dissection n) (i : Fin n) :
    CanonicalRegion D :=
  ⟨boundaryEdgeSignature D i, ⟨i, rfl⟩⟩

noncomputable instance canonicalRegionFintype {n : ℕ} (D : Dissection n) :
    Fintype (CanonicalRegion D) := by
  classical
  exact Fintype.ofSurjective (boundaryEdgeRegion D) (by
    rintro ⟨s, i, hi⟩
    use i
    apply Subtype.ext
    exact hi)

/-- Consecutive boundary vertices not lying on a cut occupy the same strict
side of that cut. -/
theorem strictSide_cyclicSucc_eq {n : ℕ} (c : Diagonal n) (i : Fin n)
    (hiLo : i ≠ c.lo) (hiHi : i ≠ c.hi)
    (hsLo : cyclicSucc i ≠ c.lo) (hsHi : cyclicSucc i ≠ c.hi) :
    strictSide c i = strictSide c (cyclicSucc i) := by
  classical
  unfold strictSide
  congr 1
  apply propext
  unfold InChordInterval
  have hiLoVal : i.val ≠ c.lo.val := fun h => hiLo (Fin.ext h)
  have hiHiVal : i.val ≠ c.hi.val := fun h => hiHi (Fin.ext h)
  have hsLoVal : (cyclicSucc i).val ≠ c.lo.val :=
    fun h => hsLo (Fin.ext h)
  have hsHiVal : (cyclicSucc i).val ≠ c.hi.val :=
    fun h => hsHi (Fin.ext h)
  by_cases hnext : i.val + 1 < n
  · have hval : (cyclicSucc i).val = i.val + 1 := by
      simp [cyclicSucc, Nat.mod_eq_of_lt hnext]
    omega
  · have hiLast : i.val + 1 = n := by omega
    have hval : (cyclicSucc i).val = 0 := by
      simp [cyclicSucc, hiLast]
    omega

/-- A polygon vertex belongs to the closure of a canonical region when it is
on each cut bounding that region or occupies the region's recorded strict
side. -/
def VertexInCanonicalRegion {n : ℕ} {D : Dissection n}
    (r : CanonicalRegion D) (v : Fin n) : Prop :=
  ∀ c : {c // c ∈ D.1},
    v = c.1.lo ∨ v = c.1.hi ∨ strictSide c.1 v = r.1 c

/-- Canonical vertex set of a region. -/
noncomputable def canonicalRegionVertices {n : ℕ} {D : Dissection n}
    (r : CanonicalRegion D) : Finset (Fin n) := by
  classical
  exact Finset.univ.filter (VertexInCanonicalRegion r)

/-- Region arity is derived from its canonical vertex set. -/
noncomputable def canonicalRegionArity {n : ℕ} {D : Dissection n}
    (r : CanonicalRegion D) : ℕ :=
  (canonicalRegionVertices r).card

/-- The initial vertex of every boundary edge belongs to the closure of the
region represented by that edge. -/
theorem vertex_mem_boundaryEdgeRegion {n : ℕ} (D : Dissection n) (i : Fin n) :
    i ∈ canonicalRegionVertices (boundaryEdgeRegion D i) := by
  classical
  rw [canonicalRegionVertices, Finset.mem_filter]
  refine ⟨Finset.mem_univ i, ?_⟩
  intro c
  by_cases hlo : i = c.1.lo
  · exact Or.inl hlo
  by_cases hhi : i = c.1.hi
  · exact Or.inr (Or.inl hhi)
  · exact Or.inr (Or.inr (by
      simp [boundaryEdgeRegion, boundaryEdgeSignature, boundaryEdgeSide,
        hlo, hhi]))

/-- The terminal vertex of every boundary edge belongs to the same canonical
region as its initial vertex. -/
theorem cyclicSucc_mem_boundaryEdgeRegion {n : ℕ}
    (D : Dissection n) (i : Fin n) :
    cyclicSucc i ∈ canonicalRegionVertices (boundaryEdgeRegion D i) := by
  classical
  rw [canonicalRegionVertices, Finset.mem_filter]
  refine ⟨Finset.mem_univ _, ?_⟩
  intro c
  by_cases hsLo : cyclicSucc i = c.1.lo
  · exact Or.inl hsLo
  by_cases hsHi : cyclicSucc i = c.1.hi
  · exact Or.inr (Or.inl hsHi)
  refine Or.inr (Or.inr ?_)
  by_cases hiLo : i = c.1.lo
  · simp [boundaryEdgeRegion, boundaryEdgeSignature, boundaryEdgeSide, hiLo]
  by_cases hiHi : i = c.1.hi
  · simp [boundaryEdgeRegion, boundaryEdgeSignature, boundaryEdgeSide, hiHi]
  · rw [← strictSide_cyclicSucc_eq c.1 i hiLo hiHi hsLo hsHi]
    simp [boundaryEdgeRegion, boundaryEdgeSignature, boundaryEdgeSide,
      hiLo, hiHi]

/-- Every canonical region has at least one derived vertex. -/
theorem canonicalRegionVertices_nonempty {n : ℕ} {D : Dissection n}
    (r : CanonicalRegion D) : (canonicalRegionVertices r).Nonempty := by
  rcases r.2 with ⟨i, hi⟩
  have hm := vertex_mem_boundaryEdgeRegion D i
  have hr : boundaryEdgeRegion D i = r := by
    apply Subtype.ext
    exact hi
  rw [hr] at hm
  exact ⟨i, hm⟩

/-- The derived arity is positive for every realized region signature. -/
theorem canonicalRegionArity_pos {n : ℕ} {D : Dissection n}
    (r : CanonicalRegion D) : 0 < canonicalRegionArity r := by
  rw [canonicalRegionArity, Finset.card_pos]
  exact canonicalRegionVertices_nonempty r

/-- Vertices of one canonical region, retaining their embedding into the
ambient cyclically labelled polygon. -/
def CanonicalRegionVertex {n : ℕ} {D : Dissection n}
    (r : CanonicalRegion D) :=
  {v : Fin n // v ∈ canonicalRegionVertices r}

noncomputable instance canonicalRegionVertexFintype {n : ℕ}
    {D : Dissection n} (r : CanonicalRegion D) :
    Fintype (CanonicalRegionVertex r) :=
  Finset.Subtype.fintype (canonicalRegionVertices r)

/- The regional vertex subtype inherits the ambient total order; its cyclic
interpretation uses the ambient polygon's wrap edge. -/

/-- Canonical local labels for the vertices of a region. -/
noncomputable def canonicalRegionVertexLabels {n : ℕ} {D : Dissection n}
    (r : CanonicalRegion D) :
    CanonicalRegionVertex r ≃ Fin (canonicalRegionArity r) := by
  classical
  exact (Finset.orderIsoOfFin (canonicalRegionVertices r) rfl).symm.toEquiv

/-- If a distinct ordered diagonal starts on an endpoint of a cut, its other
endpoint is not on that cut. -/
theorem upper_not_endpoint_of_lower_endpoint {n : ℕ} {c d : Diagonal n}
    (hne : d ≠ c) (hlo : d.lo = c.lo ∨ d.lo = c.hi) :
    d.hi ≠ c.lo ∧ d.hi ≠ c.hi := by
  constructor
  · intro hhi
    rcases hlo with hlo | hlo
    · exact d.ordered.ne (hlo.trans hhi.symm)
    · have : c.hi < c.lo := by rw [← hlo, ← hhi]; exact d.ordered
      exact (not_lt_of_ge c.ordered.le) this
  · intro hhi
    rcases hlo with hlo | hlo
    · apply hne
      cases d
      cases c
      simp_all
    · exact d.ordered.ne (hlo.trans hhi.symm)

/-- A local diagonal candidate is an admissible global diagonal whose two
endpoints lie in the derived closure of the region. -/
def CanonicalRegionalDiagonal {n : ℕ} {D : Dissection n}
    (r : CanonicalRegion D) :=
  {d : OptionalDiagonal D //
    d.1.lo ∈ canonicalRegionVertices r ∧
    d.1.hi ∈ canonicalRegionVertices r}

noncomputable instance canonicalRegionalDiagonalFintype {n : ℕ}
    {D : Dissection n} (r : CanonicalRegion D) :
    Fintype (CanonicalRegionalDiagonal r) :=
  Fintype.ofInjective (fun d : CanonicalRegionalDiagonal r => d.1.1) (by
    intro a b h
    apply Subtype.ext
    apply Subtype.ext
    exact h)

/-- Membership in a regional diagonal fiber determines its complete cut-side
signature. This is the uniqueness half of canonical regional addressing. -/
theorem CanonicalRegionalDiagonal.signature_eq_region {n : ℕ}
    {D : Dissection n} {r : CanonicalRegion D}
    (d : CanonicalRegionalDiagonal r) :
    canonicalCutSideSignature D d.1.1 = r.1 := by
  classical
  funext c
  have hloMem := (Finset.mem_filter.mp d.2.1).2 c
  have hhiMem := (Finset.mem_filter.mp d.2.2).2 c
  by_cases hlo : d.1.1.lo = c.1.lo ∨ d.1.1.lo = c.1.hi
  · have hne : d.1.1 ≠ c.1 := by
      intro h
      exact d.1.2.1 (h ▸ c.2)
    have hu := upper_not_endpoint_of_lower_endpoint hne hlo
    have hside : strictSide c.1 d.1.1.hi = r.1 c := by
      rcases hhiMem with h | h | h
      · exact False.elim (hu.1 h)
      · exact False.elim (hu.2 h)
      · exact h
    simpa [canonicalCutSideSignature,
      chordSide_eq_upper_of_lower_endpoint c.1 d.1.1 hlo] using hside
  · have hlo' : d.1.1.lo ≠ c.1.lo ∧ d.1.1.lo ≠ c.1.hi := by
      tauto
    have hside : strictSide c.1 d.1.1.lo = r.1 c := by
      rcases hloMem with h | h | h
      · exact False.elim (hlo'.1 h)
      · exact False.elim (hlo'.2 h)
      · exact h
    simpa [canonicalCutSideSignature,
      chordSide_eq_lower_of_lower_not_endpoint c.1 d.1.1 hlo'] using hside

/-- An admissible diagonal cannot belong to two distinct canonical regional
fibers. -/
theorem canonicalRegionalDiagonal_region_unique {n : ℕ}
    {D : Dissection n} (d : OptionalDiagonal D)
    (r s : CanonicalRegion D)
    (hr : d.1.lo ∈ canonicalRegionVertices r ∧
      d.1.hi ∈ canonicalRegionVertices r)
    (hs : d.1.lo ∈ canonicalRegionVertices s ∧
      d.1.hi ∈ canonicalRegionVertices s) : r = s := by
  have er := CanonicalRegionalDiagonal.signature_eq_region
    (⟨d, hr⟩ : CanonicalRegionalDiagonal r)
  have es := CanonicalRegionalDiagonal.signature_eq_region
    (⟨d, hs⟩ : CanonicalRegionalDiagonal s)
  apply Subtype.ext
  rw [← er, ← es]

/-- Forgetting the regional witness is injective: local diagonals retain their
source global channel. -/
theorem CanonicalRegionalDiagonal.forget_injective {n : ℕ}
    {D : Dissection n} {r : CanonicalRegion D} :
    Function.Injective (fun d : CanonicalRegionalDiagonal r => d.1) :=
  Subtype.val_injective

/-- Compatibility makes the side signature independent of which endpoint of
the optional diagonal is used, whenever the selected cut shares no endpoint
with it. -/
theorem OptionalDiagonal.cutSideSignature_endpoint_independent {n : ℕ}
    {D : Dissection n} (d : OptionalDiagonal D) (c : {c // c ∈ D.1})
    (hdisj : EndpointDisjoint c.1 d.1) :
    strictSide c.1 d.1.lo = strictSide c.1 d.1.hi := by
  apply strictSide_endpoint_independent hdisj
  intro hcross
  exact d.2.2 c.1 c.2 ((crosses_symmetric.mp hcross))

noncomputable instance optionalDiagonalFintype {n : ℕ} (D : Dissection n) :
    Fintype (OptionalDiagonal D) :=
  Fintype.ofInjective Subtype.val Subtype.val_injective

/-- Canonical side-signature regions actually occupied by optional diagonals.
Unlike `CanonicalRegion`, this type omits regions with no internal diagonal but
provides an unconditional address for every optional diagonal. -/
def OptionalSignatureRegion {n : ℕ} (D : Dissection n) :=
  {s : {c // c ∈ D.1} → Bool //
    ∃ d : OptionalDiagonal D, canonicalCutSideSignature D d.1 = s}

/-- Closure-membership of a vertex in an arbitrary cut-side signature. -/
def VertexInCutSignature {n : ℕ} (D : Dissection n)
    (s : {c // c ∈ D.1} → Bool) (v : Fin n) : Prop :=
  ∀ c : {c // c ∈ D.1},
    v = c.1.lo ∨ v = c.1.hi ∨ strictSide c.1 v = s c

/-- Exact witness for failure of cut-side-closure membership. The selected
cut supplied here is the active constraint that removes the vertex. -/
theorem not_vertexInCutSignature_iff
    {n : ℕ} (D : Dissection n)
    (s : {c // c ∈ D.1} → Bool) (v : Fin n) :
    ¬ VertexInCutSignature D s v ↔
      ∃ c : {c // c ∈ D.1},
        v ≠ c.1.lo ∧ v ≠ c.1.hi ∧ strictSide c.1 v ≠ s c := by
  simp only [VertexInCutSignature, not_forall, not_or]

/-- Selected cuts whose constraint excludes a specified ambient vertex. -/
noncomputable def excludingSignatureCuts
    {n : ℕ} (D : Dissection n)
    (s : {c // c ∈ D.1} → Bool) (v : Fin n) :
    Finset {c // c ∈ D.1} := by
  classical
  exact Finset.univ.filter fun c =>
    v ≠ c.1.lo ∧ v ≠ c.1.hi ∧ strictSide c.1 v ≠ s c

@[simp] theorem mem_excludingSignatureCuts_iff
    {n : ℕ} (D : Dissection n)
    (s : {c // c ∈ D.1} → Bool) (v : Fin n)
    (c : {c // c ∈ D.1}) :
    c ∈ excludingSignatureCuts D s v ↔
      v ≠ c.1.lo ∧ v ≠ c.1.hi ∧ strictSide c.1 v ≠ s c := by
  classical
  simp [excludingSignatureCuts]

/-- A vertex is excluded from the closure exactly when its finite family of
excluding selected cuts is nonempty. -/
theorem excludingSignatureCuts_nonempty_iff
    {n : ℕ} (D : Dissection n)
    (s : {c // c ∈ D.1} → Bool) (v : Fin n) :
    (excludingSignatureCuts D s v).Nonempty ↔
      ¬ VertexInCutSignature D s v := by
  rw [not_vertexInCutSignature_iff]
  constructor
  · rintro ⟨c, hc⟩
    exact ⟨c, (mem_excludingSignatureCuts_iff D s v c).1 hc⟩
  · rintro ⟨c, hc⟩
    exact ⟨c, (mem_excludingSignatureCuts_iff D s v c).2 hc⟩

/-- Vertices retained by one selected-cut constraint, including its boundary
endpoints. -/
noncomputable def retainedVertices
    {n : ℕ} {D : Dissection n} (s : {c // c ∈ D.1} → Bool)
    (c : {c // c ∈ D.1}) : Finset (Fin n) := by
  classical
  exact Finset.univ.filter fun w =>
    w = c.1.lo ∨ w = c.1.hi ∨ strictSide c.1 w = s c

@[simp] theorem mem_retainedVertices_iff
    {n : ℕ} {D : Dissection n} (s : {c // c ∈ D.1} → Bool)
    (c : {c // c ∈ D.1}) (w : Fin n) :
    w ∈ retainedVertices s c ↔
      w = c.1.lo ∨ w = c.1.hi ∨ strictSide c.1 w = s c := by
  classical
  simp [retainedVertices]

theorem mem_retainedVertices_true_iff
    {n : ℕ} {D : Dissection n} (s : {c // c ∈ D.1} → Bool)
    (c : {c // c ∈ D.1}) (hc : s c = true) (w : Fin n) :
    w ∈ retainedVertices s c ↔
      c.1.lo.val ≤ w.val ∧ w.val ≤ c.1.hi.val := by
  rw [mem_retainedVertices_iff, hc]
  exact mem_retained_true_iff c.1 w

theorem mem_retainedVertices_false_iff
    {n : ℕ} {D : Dissection n} (s : {c // c ∈ D.1} → Bool)
    (c : {c // c ∈ D.1}) (hc : s c = false) (w : Fin n) :
    w ∈ retainedVertices s c ↔
      w.val ≤ c.1.lo.val ∨ c.1.hi.val ≤ w.val := by
  rw [mem_retainedVertices_iff, hc]
  exact mem_retained_false_iff c.1 w

/-- True-oriented retained sides of endpoint-disjoint noncrossing cuts are
nested whenever they retain a common vertex. -/
theorem retainedVertices_comparable_of_true_true
    {n : ℕ} {D : Dissection n}
    (s : {c // c ∈ D.1} → Bool) (c e : {c // c ∈ D.1})
    (hc : s c = true) (he : s e = true)
    (hdisj : EndpointDisjoint c.1 e.1) (hnc : ¬ Crosses c.1 e.1)
    (w : Fin n) (hwc : w ∈ retainedVertices s c)
    (hwe : w ∈ retainedVertices s e) :
    retainedVertices s c ⊆ retainedVertices s e ∨
      retainedVertices s e ⊆ retainedVertices s c := by
  have hll : c.1.lo.val ≠ e.1.lo.val := fun h => hdisj.1 (Fin.ext h)
  have hlh : c.1.lo.val ≠ e.1.hi.val := fun h => hdisj.2.1 (Fin.ext h)
  have hhl : c.1.hi.val ≠ e.1.lo.val := fun h => hdisj.2.2.1 (Fin.ext h)
  have hhh : c.1.hi.val ≠ e.1.hi.val := fun h => hdisj.2.2.2 (Fin.ext h)
  have hwc' := (mem_retainedVertices_true_iff s c hc w).1 hwc
  have hwe' := (mem_retainedVertices_true_iff s e he w).1 hwe
  have hnested := closedIntervals_nested_of_overlap_not_interleaves
    c.1.lo.val c.1.hi.val e.1.lo.val e.1.hi.val w.val c.1.ordered
    ⟨hll, hlh, hhl, hhh⟩ hnc
    ⟨hwc'.1, hwc'.2, hwe'.1, hwe'.2⟩
  rcases hnested with hEc | hCe
  · right
    intro x hx
    apply (mem_retainedVertices_true_iff s c hc x).2
    have hx' := (mem_retainedVertices_true_iff s e he x).1 hx
    omega
  · left
    intro x hx
    apply (mem_retainedVertices_true_iff s e he x).2
    have hx' := (mem_retainedVertices_true_iff s c hc x).1 hx
    omega

/-- False-oriented retained sides of endpoint-disjoint noncrossing cuts are
nested whenever they reject a common vertex. -/
theorem retainedVertices_comparable_of_false_false
    {n : ℕ} {D : Dissection n}
    (s : {c // c ∈ D.1} → Bool) (c e : {c // c ∈ D.1})
    (hc : s c = false) (he : s e = false)
    (hdisj : EndpointDisjoint c.1 e.1) (hnc : ¬ Crosses c.1 e.1)
    (v : Fin n) (hvc : v ∉ retainedVertices s c)
    (hve : v ∉ retainedVertices s e) :
    retainedVertices s c ⊆ retainedVertices s e ∨
      retainedVertices s e ⊆ retainedVertices s c := by
  have hll : c.1.lo.val ≠ e.1.lo.val := fun h => hdisj.1 (Fin.ext h)
  have hlh : c.1.lo.val ≠ e.1.hi.val := fun h => hdisj.2.1 (Fin.ext h)
  have hhl : c.1.hi.val ≠ e.1.lo.val := fun h => hdisj.2.2.1 (Fin.ext h)
  have hhh : c.1.hi.val ≠ e.1.hi.val := fun h => hdisj.2.2.2 (Fin.ext h)
  have hvc' : ¬(v.val ≤ c.1.lo.val ∨ c.1.hi.val ≤ v.val) := by
    intro hv
    exact hvc ((mem_retainedVertices_false_iff s c hc v).2 hv)
  have hve' : ¬(v.val ≤ e.1.lo.val ∨ e.1.hi.val ≤ v.val) := by
    intro hv
    exact hve ((mem_retainedVertices_false_iff s e he v).2 hv)
  have hnested := closedIntervals_nested_of_overlap_not_interleaves
    c.1.lo.val c.1.hi.val e.1.lo.val e.1.hi.val v.val c.1.ordered
    ⟨hll, hlh, hhl, hhh⟩ hnc (by omega)
  rcases hnested with hEc | hCe
  · left
    intro x hx
    apply (mem_retainedVertices_false_iff s e he x).2
    have hx' := (mem_retainedVertices_false_iff s c hc x).1 hx
    omega
  · right
    intro x hx
    apply (mem_retainedVertices_false_iff s c hc x).2
    have hx' := (mem_retainedVertices_false_iff s e he x).1 hx
    omega

/-- If a true-oriented and a false-oriented endpoint-disjoint noncrossing
constraint retain one common vertex and reject another, the linear retained
interval lies in the cyclic-complement retained side. -/
theorem retainedVertices_subset_of_true_false
    {n : ℕ} {D : Dissection n}
    (s : {c // c ∈ D.1} → Bool) (c e : {c // c ∈ D.1})
    (hc : s c = true) (he : s e = false)
    (hdisj : EndpointDisjoint c.1 e.1) (hnc : ¬ Crosses c.1 e.1)
    (v w : Fin n) (hvc : v ∉ retainedVertices s c)
    (hve : v ∉ retainedVertices s e)
    (hwc : w ∈ retainedVertices s c) (hwe : w ∈ retainedVertices s e) :
    retainedVertices s c ⊆ retainedVertices s e := by
  have hll : c.1.lo.val ≠ e.1.lo.val := fun h => hdisj.1 (Fin.ext h)
  have hlh : c.1.lo.val ≠ e.1.hi.val := fun h => hdisj.2.1 (Fin.ext h)
  have hhl : c.1.hi.val ≠ e.1.lo.val := fun h => hdisj.2.2.1 (Fin.ext h)
  have hhh : c.1.hi.val ≠ e.1.hi.val := fun h => hdisj.2.2.2 (Fin.ext h)
  have hvc' : ¬(c.1.lo.val ≤ v.val ∧ v.val ≤ c.1.hi.val) := by
    intro hv
    exact hvc ((mem_retainedVertices_true_iff s c hc v).2 hv)
  have hve' : ¬(v.val ≤ e.1.lo.val ∨ e.1.hi.val ≤ v.val) := by
    intro hv
    exact hve ((mem_retainedVertices_false_iff s e he v).2 hv)
  have hwc' := (mem_retainedVertices_true_iff s c hc w).1 hwc
  have hwe' := (mem_retainedVertices_false_iff s e he w).1 hwe
  unfold Crosses at hnc
  intro x hx
  apply (mem_retainedVertices_false_iff s e he x).2
  have hx' := (mem_retainedVertices_true_iff s c hc x).1 hx
  rcases lt_or_gt_of_ne hll with hlo | hlo <;> omega

/-- Uniform nesting for endpoint-disjoint selected-cut constraints with common
retained and rejected witnesses. -/
theorem retainedVertices_comparable_of_endpointDisjoint
    {n : ℕ} {D : Dissection n}
    (s : {c // c ∈ D.1} → Bool) (c e : {c // c ∈ D.1})
    (hdisj : EndpointDisjoint c.1 e.1) (hnc : ¬ Crosses c.1 e.1)
    (v w : Fin n) (hvc : v ∉ retainedVertices s c)
    (hve : v ∉ retainedVertices s e)
    (hwc : w ∈ retainedVertices s c) (hwe : w ∈ retainedVertices s e) :
    retainedVertices s c ⊆ retainedVertices s e ∨
      retainedVertices s e ⊆ retainedVertices s c := by
  cases hc : s c <;> cases he : s e
  · exact retainedVertices_comparable_of_false_false
      s c e hc he hdisj hnc v hvc hve
  · right
    have hdisj' : EndpointDisjoint e.1 c.1 :=
      endpointDisjoint_symmetric.mp hdisj
    have hnc' : ¬ Crosses e.1 c.1 := by
      intro hcross
      exact hnc ((crosses_symmetric (a := c.1) (b := e.1)).mpr hcross)
    exact retainedVertices_subset_of_true_false
      s e c he hc hdisj' hnc' v w hve hvc hwe hwc
  · left
    exact retainedVertices_subset_of_true_false
      s c e hc he hdisj hnc v w hvc hve hwc hwe
  · exact retainedVertices_comparable_of_true_true
      s c e hc he hdisj hnc w hwc hwe

/-- True-oriented constraints sharing their upper endpoint have comparable
retained intervals. -/
theorem retainedVertices_comparable_of_sameUpper_true
    {n : ℕ} {D : Dissection n}
    (s : {c // c ∈ D.1} → Bool) (c e : {c // c ∈ D.1})
    (hhi : c.1.hi = e.1.hi)
    (hc : s c = true) (he : s e = true) :
    retainedVertices s c ⊆ retainedVertices s e ∨
      retainedVertices s e ⊆ retainedVertices s c := by
  have hhiVal := congrArg Fin.val hhi
  rcases le_total c.1.lo.val e.1.lo.val with hlo | hlo
  · right
    intro x hx
    apply (mem_retainedVertices_true_iff s c hc x).2
    have hx' := (mem_retainedVertices_true_iff s e he x).1 hx
    omega
  · left
    intro x hx
    apply (mem_retainedVertices_true_iff s e he x).2
    have hx' := (mem_retainedVertices_true_iff s c hc x).1 hx
    omega

/-- False-oriented constraints sharing their upper endpoint have comparable
retained cyclic complements. -/
theorem retainedVertices_comparable_of_sameUpper_false
    {n : ℕ} {D : Dissection n}
    (s : {c // c ∈ D.1} → Bool) (c e : {c // c ∈ D.1})
    (hhi : c.1.hi = e.1.hi)
    (hc : s c = false) (he : s e = false) :
    retainedVertices s c ⊆ retainedVertices s e ∨
      retainedVertices s e ⊆ retainedVertices s c := by
  have hhiVal := congrArg Fin.val hhi
  rcases le_total c.1.lo.val e.1.lo.val with hlo | hlo
  · left
    intro x hx
    apply (mem_retainedVertices_false_iff s e he x).2
    rcases (mem_retainedVertices_false_iff s c hc x).1 hx with hx | hx
    · exact Or.inl (hx.trans hlo)
    · exact Or.inr (by omega)
  · right
    intro x hx
    apply (mem_retainedVertices_false_iff s c hc x).2
    rcases (mem_retainedVertices_false_iff s e he x).1 hx with hx | hx
    · exact Or.inl (hx.trans hlo)
    · exact Or.inr (by omega)

/-- Equal-oriented constraints sharing their upper endpoint are uniformly
comparable. -/
theorem retainedVertices_comparable_of_sameUpper_sameOrientation
    {n : ℕ} {D : Dissection n}
    (s : {c // c ∈ D.1} → Bool) (c e : {c // c ∈ D.1})
    (hhi : c.1.hi = e.1.hi) (hs : s c = s e) :
    retainedVertices s c ⊆ retainedVertices s e ∨
      retainedVertices s e ⊆ retainedVertices s c := by
  cases hc : s c <;> cases he : s e
  · exact retainedVertices_comparable_of_sameUpper_false s c e hhi hc he
  · simp [hc, he] at hs
  · simp [hc, he] at hs
  · exact retainedVertices_comparable_of_sameUpper_true s c e hhi hc he

/-- Equal-oriented constraints sharing their lower endpoint are uniformly
comparable. -/
theorem retainedVertices_comparable_of_sameLower_sameOrientation
    {n : ℕ} {D : Dissection n}
    (s : {c // c ∈ D.1} → Bool) (c e : {c // c ∈ D.1})
    (hlo : c.1.lo = e.1.lo) (hs : s c = s e) :
    retainedVertices s c ⊆ retainedVertices s e ∨
      retainedVertices s e ⊆ retainedVertices s c := by
  have hloVal := congrArg Fin.val hlo
  cases hc : s c <;> cases he : s e
  · rcases le_total c.1.hi.val e.1.hi.val with hhi | hhi
    · right
      intro x hx
      apply (mem_retainedVertices_false_iff s c hc x).2
      rcases (mem_retainedVertices_false_iff s e he x).1 hx with hx | hx
      · exact Or.inl (by omega)
      · exact Or.inr (hhi.trans hx)
    · left
      intro x hx
      apply (mem_retainedVertices_false_iff s e he x).2
      rcases (mem_retainedVertices_false_iff s c hc x).1 hx with hx | hx
      · exact Or.inl (by omega)
      · exact Or.inr (hhi.trans hx)
  · simp [hc, he] at hs
  · simp [hc, he] at hs
  · rcases le_total c.1.hi.val e.1.hi.val with hhi | hhi
    · left
      intro x hx
      apply (mem_retainedVertices_true_iff s e he x).2
      have hx' := (mem_retainedVertices_true_iff s c hc x).1 hx
      omega
    · right
      intro x hx
      apply (mem_retainedVertices_true_iff s c hc x).2
      have hx' := (mem_retainedVertices_true_iff s e he x).1 hx
      omega

/-- Oppositely oriented constraints sharing their upper endpoint cannot both
reject one vertex while retaining two distinct common vertices. -/
theorem sameUpper_oppositeOrientation_impossible
    {n : ℕ} {D : Dissection n}
    (s : {c // c ∈ D.1} → Bool) (c e : {c // c ∈ D.1})
    (hhi : c.1.hi = e.1.hi) (hc : s c = true) (he : s e = false)
    (v w z : Fin n) (hwz : w ≠ z)
    (hvc : v ∉ retainedVertices s c) (hve : v ∉ retainedVertices s e)
    (hwc : w ∈ retainedVertices s c) (hwe : w ∈ retainedVertices s e)
    (hzc : z ∈ retainedVertices s c) (hze : z ∈ retainedVertices s e) :
    False := by
  have hhiVal := congrArg Fin.val hhi
  have hwzVal : w.val ≠ z.val := fun h => hwz (Fin.ext h)
  have hvc' : ¬(c.1.lo.val ≤ v.val ∧ v.val ≤ c.1.hi.val) := by
    intro hv
    exact hvc ((mem_retainedVertices_true_iff s c hc v).2 hv)
  have hve' : ¬(v.val ≤ e.1.lo.val ∨ e.1.hi.val ≤ v.val) := by
    intro hv
    exact hve ((mem_retainedVertices_false_iff s e he v).2 hv)
  have hwc' := (mem_retainedVertices_true_iff s c hc w).1 hwc
  have hwe' := (mem_retainedVertices_false_iff s e he w).1 hwe
  have hzc' := (mem_retainedVertices_true_iff s c hc z).1 hzc
  have hze' := (mem_retainedVertices_false_iff s e he z).1 hze
  rcases hwe' with hwe' | hwe' <;> rcases hze' with hze' | hze' <;> omega

/-- Oppositely oriented constraints sharing their lower endpoint cannot both
reject one vertex while retaining two distinct common vertices. -/
theorem sameLower_oppositeOrientation_impossible
    {n : ℕ} {D : Dissection n}
    (s : {c // c ∈ D.1} → Bool) (c e : {c // c ∈ D.1})
    (hlo : c.1.lo = e.1.lo) (hc : s c = true) (he : s e = false)
    (v w z : Fin n) (hwz : w ≠ z)
    (hvc : v ∉ retainedVertices s c) (hve : v ∉ retainedVertices s e)
    (hwc : w ∈ retainedVertices s c) (hwe : w ∈ retainedVertices s e)
    (hzc : z ∈ retainedVertices s c) (hze : z ∈ retainedVertices s e) :
    False := by
  have hloVal := congrArg Fin.val hlo
  have hwzVal : w.val ≠ z.val := fun h => hwz (Fin.ext h)
  have hvc' : ¬(c.1.lo.val ≤ v.val ∧ v.val ≤ c.1.hi.val) := by
    intro hv
    exact hvc ((mem_retainedVertices_true_iff s c hc v).2 hv)
  have hve' : ¬(v.val ≤ e.1.lo.val ∨ e.1.hi.val ≤ v.val) := by
    intro hv
    exact hve ((mem_retainedVertices_false_iff s e he v).2 hv)
  have hwc' := (mem_retainedVertices_true_iff s c hc w).1 hwc
  have hwe' := (mem_retainedVertices_false_iff s e he w).1 hwe
  have hzc' := (mem_retainedVertices_true_iff s c hc z).1 hzc
  have hze' := (mem_retainedVertices_false_iff s e he z).1 hze
  rcases hwe' with hwe' | hwe' <;> rcases hze' with hze' | hze' <;> omega

/-- Constraints meeting upper-to-lower are comparable whenever they reject a
common vertex and retain two distinct common vertices. Equal orientations make
one of those witness conditions impossible; mixed orientations give direct
containment. -/
theorem retainedVertices_comparable_of_upper_eq_lower
    {n : ℕ} {D : Dissection n}
    (s : {c // c ∈ D.1} → Bool) (c e : {c // c ∈ D.1})
    (htouch : c.1.hi = e.1.lo)
    (v w z : Fin n) (hwz : w ≠ z)
    (hvc : v ∉ retainedVertices s c) (hve : v ∉ retainedVertices s e)
    (hwc : w ∈ retainedVertices s c) (hwe : w ∈ retainedVertices s e)
    (hzc : z ∈ retainedVertices s c) (hze : z ∈ retainedVertices s e) :
    retainedVertices s c ⊆ retainedVertices s e ∨
      retainedVertices s e ⊆ retainedVertices s c := by
  have htouchVal := congrArg Fin.val htouch
  have hwzVal : w.val ≠ z.val := fun h => hwz (Fin.ext h)
  cases hc : s c <;> cases he : s e
  · have hvc' : ¬(v.val ≤ c.1.lo.val ∨ c.1.hi.val ≤ v.val) := by
      intro hv
      exact hvc ((mem_retainedVertices_false_iff s c hc v).2 hv)
    have hve' : ¬(v.val ≤ e.1.lo.val ∨ e.1.hi.val ≤ v.val) := by
      intro hv
      exact hve ((mem_retainedVertices_false_iff s e he v).2 hv)
    omega
  · right
    intro x hx
    apply (mem_retainedVertices_false_iff s c hc x).2
    have hx' := (mem_retainedVertices_true_iff s e he x).1 hx
    exact Or.inr (by omega)
  · left
    intro x hx
    apply (mem_retainedVertices_false_iff s e he x).2
    have hx' := (mem_retainedVertices_true_iff s c hc x).1 hx
    exact Or.inl (by omega)
  · have hwc' := (mem_retainedVertices_true_iff s c hc w).1 hwc
    have hwe' := (mem_retainedVertices_true_iff s e he w).1 hwe
    have hzc' := (mem_retainedVertices_true_iff s c hc z).1 hzc
    have hze' := (mem_retainedVertices_true_iff s e he z).1 hze
    omega

/-- Uniform comparability for distinct constraints sharing any endpoint, under
the common retained and rejected witnesses supplied by an occupied region. -/
theorem retainedVertices_comparable_of_sharedEndpoint
    {n : ℕ} {D : Dissection n}
    (s : {c // c ∈ D.1} → Bool) (c e : {c // c ∈ D.1})
    (hshare : c.1.lo = e.1.lo ∨ c.1.lo = e.1.hi ∨
      c.1.hi = e.1.lo ∨ c.1.hi = e.1.hi)
    (v w z : Fin n) (hwz : w ≠ z)
    (hvc : v ∉ retainedVertices s c) (hve : v ∉ retainedVertices s e)
    (hwc : w ∈ retainedVertices s c) (hwe : w ∈ retainedVertices s e)
    (hzc : z ∈ retainedVertices s c) (hze : z ∈ retainedVertices s e) :
    retainedVertices s c ⊆ retainedVertices s e ∨
      retainedVertices s e ⊆ retainedVertices s c := by
  rcases hshare with hll | hlh | hhl | hhh
  · cases hc : s c <;> cases he : s e
    · exact retainedVertices_comparable_of_sameLower_sameOrientation
        s c e hll (hc.trans he.symm)
    · exact False.elim (sameLower_oppositeOrientation_impossible
        s e c hll.symm he hc v w z hwz hve hvc hwe hwc hze hzc)
    · exact False.elim (sameLower_oppositeOrientation_impossible
        s c e hll hc he v w z hwz hvc hve hwc hwe hzc hze)
    · exact retainedVertices_comparable_of_sameLower_sameOrientation
        s c e hll (hc.trans he.symm)
  · have h := retainedVertices_comparable_of_upper_eq_lower
      s e c hlh.symm v w z hwz hve hvc hwe hwc hze hzc
    exact h.symm
  · exact retainedVertices_comparable_of_upper_eq_lower
      s c e hhl v w z hwz hvc hve hwc hwe hzc hze
  · cases hc : s c <;> cases he : s e
    · exact retainedVertices_comparable_of_sameUpper_sameOrientation
        s c e hhh (hc.trans he.symm)
    · exact False.elim (sameUpper_oppositeOrientation_impossible
        s e c hhh.symm he hc v w z hwz hve hvc hwe hwc hze hzc)
    · exact False.elim (sameUpper_oppositeOrientation_impossible
        s c e hhh hc he v w z hwz hvc hve hwc hwe hzc hze)
    · exact retainedVertices_comparable_of_sameUpper_sameOrientation
        s c e hhh (hc.trans he.symm)

/-- Closure membership is simultaneous membership in every retained side. -/
theorem vertexInCutSignature_iff_forall_mem_retainedVertices
    {n : ℕ} (D : Dissection n)
    (s : {c // c ∈ D.1} → Bool) (v : Fin n) :
    VertexInCutSignature D s v ↔
      ∀ c : {c // c ∈ D.1}, v ∈ retainedVertices s c := by
  simp [VertexInCutSignature, mem_retainedVertices_iff]

theorem mem_excludingSignatureCuts_iff_not_mem_retainedVertices
    {n : ℕ} (D : Dissection n)
    (s : {c // c ∈ D.1} → Bool) (v : Fin n)
    (c : {c // c ∈ D.1}) :
    c ∈ excludingSignatureCuts D s v ↔ v ∉ retainedVertices s c := by
  rw [mem_excludingSignatureCuts_iff, mem_retainedVertices_iff]
  tauto

/-- Smallest retained-side cardinality among constraints excluding a vertex.
Unlike raw chord span, this criterion handles interval and complementary-side
signatures uniformly. -/
noncomputable def minimalExcludingRetainedCard
    {n : ℕ} (D : Dissection n)
    (s : {c // c ∈ D.1} → Bool) (v : Fin n)
    (h : (excludingSignatureCuts D s v).Nonempty) : ℕ := by
  classical
  exact ((excludingSignatureCuts D s v).image
    (fun c => (retainedVertices s c).card)).min'
    ((Finset.image_nonempty).2 h)

/-- The smallest retained-side cardinality is attained by an excluding cut. -/
theorem exists_excludingCut_with_minimalRetainedCard
    {n : ℕ} (D : Dissection n)
    (s : {c // c ∈ D.1} → Bool) (v : Fin n)
    (h : (excludingSignatureCuts D s v).Nonempty) :
    ∃ c ∈ excludingSignatureCuts D s v,
      (retainedVertices s c).card =
        minimalExcludingRetainedCard D s v h := by
  classical
  have hm := Finset.min'_mem
    ((excludingSignatureCuts D s v).image
      (fun c => (retainedVertices s c).card))
    ((Finset.image_nonempty).2 h)
  rcases Finset.mem_image.mp hm with ⟨c, hc, heq⟩
  exact ⟨c, hc, heq⟩

/-- Canonical choice of an excluding cut attaining minimum retained-side
cardinality. -/
noncomputable def minimalExcludingCut
    {n : ℕ} (D : Dissection n)
    (s : {c // c ∈ D.1} → Bool) (v : Fin n)
    (h : (excludingSignatureCuts D s v).Nonempty) : {c // c ∈ D.1} :=
  Classical.choose (exists_excludingCut_with_minimalRetainedCard D s v h)

@[simp] theorem minimalExcludingCut_mem
    {n : ℕ} (D : Dissection n)
    (s : {c // c ∈ D.1} → Bool) (v : Fin n)
    (h : (excludingSignatureCuts D s v).Nonempty) :
    minimalExcludingCut D s v h ∈ excludingSignatureCuts D s v :=
  (Classical.choose_spec
    (exists_excludingCut_with_minimalRetainedCard D s v h)).1

@[simp] theorem minimalExcludingCut_card
    {n : ℕ} (D : Dissection n)
    (s : {c // c ∈ D.1} → Bool) (v : Fin n)
    (h : (excludingSignatureCuts D s v).Nonempty) :
    (retainedVertices s (minimalExcludingCut D s v h)).card =
      minimalExcludingRetainedCard D s v h :=
  (Classical.choose_spec
    (exists_excludingCut_with_minimalRetainedCard D s v h)).2

/-- The minimum retained cardinality bounds every excluding constraint. -/
theorem minimalExcludingRetainedCard_le
    {n : ℕ} (D : Dissection n)
    (s : {c // c ∈ D.1} → Bool) (v : Fin n)
    (h : (excludingSignatureCuts D s v).Nonempty)
    (c : {c // c ∈ D.1}) (hc : c ∈ excludingSignatureCuts D s v) :
    minimalExcludingRetainedCard D s v h ≤ (retainedVertices s c).card := by
  classical
  exact Finset.min'_le
    ((excludingSignatureCuts D s v).image
      (fun e => (retainedVertices s e).card))
    (retainedVertices s c).card (Finset.mem_image.mpr ⟨c, hc, rfl⟩)

/-- A selected cut is active on a signature closure when both of its
endpoints survive every other cut-side constraint. -/
def ActiveSignatureCut {n : ℕ} (D : Dissection n)
    (s : {c // c ∈ D.1} → Bool) :=
  {c : {c // c ∈ D.1} //
    VertexInCutSignature D s c.1.lo ∧
      VertexInCutSignature D s c.1.hi}

noncomputable instance activeSignatureCutFintype
    {n : ℕ} (D : Dissection n) (s : {c // c ∈ D.1} → Bool) :
    Fintype (ActiveSignatureCut D s) :=
  Fintype.ofInjective Subtype.val Subtype.val_injective

/-- The lower endpoint of an active cut is canonically a closure vertex. -/
def ActiveSignatureCut.lowerVertex
    {n : ℕ} {D : Dissection n} {s : {c // c ∈ D.1} → Bool}
    (c : ActiveSignatureCut D s) :
    {v : Fin n // VertexInCutSignature D s v} := ⟨c.1.1.lo, c.2.1⟩

/-- The upper endpoint of an active cut is canonically a closure vertex. -/
def ActiveSignatureCut.upperVertex
    {n : ℕ} {D : Dissection n} {s : {c // c ∈ D.1} → Bool}
    (c : ActiveSignatureCut D s) :
    {v : Fin n // VertexInCutSignature D s v} := ⟨c.1.1.hi, c.2.2⟩

@[simp] theorem ActiveSignatureCut.lowerVertex_val
    {n : ℕ} {D : Dissection n} {s : {c // c ∈ D.1} → Bool}
    (c : ActiveSignatureCut D s) : c.lowerVertex.1 = c.1.1.lo := rfl

@[simp] theorem ActiveSignatureCut.upperVertex_val
    {n : ℕ} {D : Dissection n} {s : {c // c ∈ D.1} → Bool}
    (c : ActiveSignatureCut D s) : c.upperVertex.1 = c.1.1.hi := rfl

/-- A chord joining two vertices in one cut-side closure crosses no selected
cut. -/
theorem compatibleWith_of_endpoints_in_cutSignature
    {n : ℕ} (D : Dissection n) (s : {c // c ∈ D.1} → Bool)
    (d : Diagonal n)
    (hlo : VertexInCutSignature D s d.lo)
    (hhi : VertexInCutSignature D s d.hi) :
    CompatibleWith D d := by
  intro c hc hcross
  let cD : {c // c ∈ D.1} := ⟨c, hc⟩
  have hl := hlo cD
  have hh := hhi cD
  have hsideNe := strictSide_ne_of_crosses hcross
  have hcross' := hcross
  unfold Crosses at hcross'
  have hlSide : strictSide c d.lo = s cD := by
    rcases hl with hl | hl | hl
    · simp [cD] at hl
      rcases hcross' with hcross' | hcross' <;> omega
    · simp [cD] at hl
      rcases hcross' with hcross' | hcross' <;> omega
    · exact hl
  have hhSide : strictSide c d.hi = s cD := by
    rcases hh with hh | hh | hh
    · simp [cD] at hh
      rcases hcross' with hcross' | hcross' <;> omega
    · simp [cD] at hh
      rcases hcross' with hcross' | hcross' <;> omega
    · exact hh
  exact hsideNe (hlSide.trans hhSide.symm)

/-- A new chord with both endpoints in one signature closure has exactly that
canonical cut-side signature. -/
theorem canonicalCutSideSignature_eq_of_endpoints_in_signature
    {n : ℕ} (D : Dissection n) (s : {c // c ∈ D.1} → Bool)
    (d : Diagonal n) (hnew : d ∉ D.1)
    (hlo : VertexInCutSignature D s d.lo)
    (hhi : VertexInCutSignature D s d.hi) :
    canonicalCutSideSignature D d = s := by
  funext c
  have hcNe : d ≠ c.1 := by
    intro h
    apply hnew
    rw [h]
    exact c.2
  by_cases hstart : d.lo = c.1.lo ∨ d.lo = c.1.hi
  · rw [canonicalCutSideSignature,
      chordSide_eq_upper_of_lower_endpoint c.1 d hstart]
    have hupper := hhi c
    have hnot := upper_not_endpoint_of_lower_endpoint hcNe hstart
    rcases hupper with hupper | hupper | hupper
    · exact False.elim (hnot.1 hupper)
    · exact False.elim (hnot.2 hupper)
    · exact hupper
  · rw [canonicalCutSideSignature,
      chordSide_eq_lower_of_lower_not_endpoint c.1 d (not_or.mp hstart)]
    have hlower := hlo c
    rcases hlower with hlower | hlower | hlower
    · exact False.elim (hstart (Or.inl hlower))
    · exact False.elim (hstart (Or.inr hlower))
    · exact hlower

/-- Vertex set and arity derived for an occupied optional-diagonal region. -/
noncomputable def optionalSignatureRegionVertices {n : ℕ} {D : Dissection n}
    (r : OptionalSignatureRegion D) : Finset (Fin n) := by
  classical
  exact Finset.univ.filter (VertexInCutSignature D r.1)

noncomputable def optionalSignatureRegionArity {n : ℕ} {D : Dissection n}
    (r : OptionalSignatureRegion D) : ℕ :=
  (optionalSignatureRegionVertices r).card

/-- Local diagonal fiber over an occupied side-signature region. -/
def OptionalSignatureRegionalDiagonal {n : ℕ} {D : Dissection n}
    (r : OptionalSignatureRegion D) :=
  {d : OptionalDiagonal D // canonicalCutSideSignature D d.1 = r.1}

/-- Both endpoints of a signature-fiber diagonal lie in the vertex closure of
that occupied region. -/
theorem OptionalSignatureRegionalDiagonal.lower_mem_vertices {n : ℕ}
    {D : Dissection n} {r : OptionalSignatureRegion D}
    (d : OptionalSignatureRegionalDiagonal r) :
    d.1.1.lo ∈ optionalSignatureRegionVertices r := by
  classical
  rw [optionalSignatureRegionVertices, Finset.mem_filter]
  refine ⟨Finset.mem_univ _, ?_⟩
  intro c
  by_cases hlo : d.1.1.lo = c.1.lo
  · exact Or.inl hlo
  by_cases hhi : d.1.1.lo = c.1.hi
  · exact Or.inr (Or.inl hhi)
  · refine Or.inr (Or.inr ?_)
    have hc := congrFun d.2 c
    simpa [canonicalCutSideSignature,
      chordSide_eq_lower_of_lower_not_endpoint c.1 d.1.1 ⟨hlo, hhi⟩] using hc

theorem OptionalSignatureRegionalDiagonal.upper_mem_vertices {n : ℕ}
    {D : Dissection n} {r : OptionalSignatureRegion D}
    (d : OptionalSignatureRegionalDiagonal r) :
    d.1.1.hi ∈ optionalSignatureRegionVertices r := by
  classical
  rw [optionalSignatureRegionVertices, Finset.mem_filter]
  refine ⟨Finset.mem_univ _, ?_⟩
  intro c
  by_cases hlo : d.1.1.hi = c.1.lo
  · exact Or.inl hlo
  by_cases hhi : d.1.1.hi = c.1.hi
  · exact Or.inr (Or.inl hhi)
  · refine Or.inr (Or.inr ?_)
    have hc := congrFun d.2 c
    by_cases hstart : d.1.1.lo = c.1.lo ∨ d.1.1.lo = c.1.hi
    · simpa [canonicalCutSideSignature,
        chordSide_eq_upper_of_lower_endpoint c.1 d.1.1 hstart] using hc
    · have hdisj : EndpointDisjoint c.1 d.1.1 := by
        rcases not_or.mp hstart with ⟨ha, hb⟩
        exact ⟨Ne.symm ha, Ne.symm hlo, Ne.symm hb, Ne.symm hhi⟩
      have hnc : ¬ Crosses c.1 d.1.1 := by
        intro h
        exact d.1.2.2 c.1 c.2 (crosses_symmetric.mpr h)
      rw [← strictSide_endpoint_independent hdisj hnc]
      simpa [canonicalCutSideSignature,
        chordSide_eq_lower_of_lower_not_endpoint c.1 d.1.1
          (not_or.mp hstart)] using hc

/-- Canonical choice of the optional diagonal witnessing occupation of a
signature region. -/
noncomputable def OptionalSignatureRegion.witness
    {n : ℕ} {D : Dissection n} (r : OptionalSignatureRegion D) :
    OptionalDiagonal D := Classical.choose r.2

@[simp] theorem OptionalSignatureRegion.witness_signature
    {n : ℕ} {D : Dissection n} (r : OptionalSignatureRegion D) :
    canonicalCutSideSignature D r.witness.1 = r.1 :=
  Classical.choose_spec r.2

/-- The occupation witness as a member of the regional diagonal fiber. -/
noncomputable def OptionalSignatureRegion.witnessRegionalDiagonal
    {n : ℕ} {D : Dissection n} (r : OptionalSignatureRegion D) :
    OptionalSignatureRegionalDiagonal r :=
  ⟨r.witness, r.witness_signature⟩

/-- The witness supplies two distinct closure vertices retained by every
selected-cut constraint. -/
theorem OptionalSignatureRegion.witness_endpoints_mem
    {n : ℕ} {D : Dissection n} (r : OptionalSignatureRegion D) :
    r.witness.1.lo ∈ optionalSignatureRegionVertices r ∧
      r.witness.1.hi ∈ optionalSignatureRegionVertices r :=
  ⟨r.witnessRegionalDiagonal.lower_mem_vertices,
    r.witnessRegionalDiagonal.upper_mem_vertices⟩

/-- Any two distinct selected-cut constraints excluding the same vertex in an
occupied signature have comparable retained sides. -/
theorem OptionalSignatureRegion.retainedVertices_comparable
    {n : ℕ} {D : Dissection n} (r : OptionalSignatureRegion D)
    (c e : {c // c ∈ D.1}) (hne : c.1 ≠ e.1) (v : Fin n)
    (hvc : v ∉ retainedVertices r.1 c)
    (hve : v ∉ retainedVertices r.1 e) :
    retainedVertices r.1 c ⊆ retainedVertices r.1 e ∨
      retainedVertices r.1 e ⊆ retainedVertices r.1 c := by
  let q := r.witnessRegionalDiagonal
  have hloVertex : VertexInCutSignature D r.1 q.1.1.lo := by
    simpa [optionalSignatureRegionVertices] using q.lower_mem_vertices
  have hhiVertex : VertexInCutSignature D r.1 q.1.1.hi := by
    simpa [optionalSignatureRegionVertices] using q.upper_mem_vertices
  have hqloc := (vertexInCutSignature_iff_forall_mem_retainedVertices
    D r.1 q.1.1.lo).1 hloVertex c
  have hqloe := (vertexInCutSignature_iff_forall_mem_retainedVertices
    D r.1 q.1.1.lo).1 hloVertex e
  have hqhic := (vertexInCutSignature_iff_forall_mem_retainedVertices
    D r.1 q.1.1.hi).1 hhiVertex c
  have hqhie := (vertexInCutSignature_iff_forall_mem_retainedVertices
    D r.1 q.1.1.hi).1 hhiVertex e
  rcases endpointDisjoint_or_sharedEndpoint c.1 e.1 with hdisj | hshare
  · have hnc : ¬ Crosses c.1 e.1 := D.2 c.2 e.2 hne
    exact retainedVertices_comparable_of_endpointDisjoint
      r.1 c e hdisj hnc v q.1.1.lo hvc hve hqloc hqloe
  · exact retainedVertices_comparable_of_sharedEndpoint
      r.1 c e hshare v q.1.1.lo q.1.1.hi
      (ne_of_lt q.1.1.ordered) hvc hve hqloc hqloe hqhic hqhie

/-- An excluding cut attaining the minimum retained cardinality is contained
in every other excluding retained side. -/
theorem OptionalSignatureRegion.minimalExcludingCut_subset
    {n : ℕ} {D : Dissection n} (r : OptionalSignatureRegion D)
    (v : Fin n) (h : (excludingSignatureCuts D r.1 v).Nonempty)
    (c : {c // c ∈ D.1}) (hc : c ∈ excludingSignatureCuts D r.1 v)
    (hcmin : (retainedVertices r.1 c).card =
      minimalExcludingRetainedCard D r.1 v h)
    (e : {c // c ∈ D.1}) (he : e ∈ excludingSignatureCuts D r.1 v) :
    retainedVertices r.1 c ⊆ retainedVertices r.1 e := by
  by_cases hce : c.1 = e.1
  · have hce' : c = e := Subtype.ext hce
    subst e
    exact Finset.Subset.rfl
  · rcases r.retainedVertices_comparable c e hce v
      ((mem_excludingSignatureCuts_iff_not_mem_retainedVertices
        D r.1 v c).1 hc)
      ((mem_excludingSignatureCuts_iff_not_mem_retainedVertices
        D r.1 v e).1 he) with hsub | hsub
    · exact hsub
    · have hcard : (retainedVertices r.1 c).card ≤
          (retainedVertices r.1 e).card := by
        rw [hcmin]
        exact minimalExcludingRetainedCard_le D r.1 v h e he
      have heq := Finset.eq_of_subset_of_card_le hsub hcard
      rw [heq]

/-- The canonical minimum excluding cut has retained side contained in every
other constraint excluding the same vertex. -/
theorem OptionalSignatureRegion.minimalExcludingCut_subset_all
    {n : ℕ} {D : Dissection n} (r : OptionalSignatureRegion D)
    (v : Fin n) (h : (excludingSignatureCuts D r.1 v).Nonempty)
    (e : {c // c ∈ D.1}) (he : e ∈ excludingSignatureCuts D r.1 v) :
    retainedVertices r.1 (minimalExcludingCut D r.1 v h) ⊆
      retainedVertices r.1 e :=
  r.minimalExcludingCut_subset v h (minimalExcludingCut D r.1 v h)
    (minimalExcludingCut_mem D r.1 v h)
    (minimalExcludingCut_card D r.1 v h) e he

/-- Both endpoints of the canonical least rejecting cut satisfy every
constraint that also rejects the chosen vertex. -/
theorem OptionalSignatureRegion.minimalExcludingCut_endpoints_mem_rejecting
    {n : ℕ} {D : Dissection n} (r : OptionalSignatureRegion D)
    (v : Fin n) (h : (excludingSignatureCuts D r.1 v).Nonempty)
    (e : {c // c ∈ D.1}) (he : e ∈ excludingSignatureCuts D r.1 v) :
    (minimalExcludingCut D r.1 v h).1.lo ∈ retainedVertices r.1 e ∧
      (minimalExcludingCut D r.1 v h).1.hi ∈ retainedVertices r.1 e := by
  let c := minimalExcludingCut D r.1 v h
  have hsubset := r.minimalExcludingCut_subset_all v h e he
  constructor
  · apply hsubset
    apply (mem_retainedVertices_iff r.1 c c.1.lo).2
    exact Or.inl rfl
  · apply hsubset
    apply (mem_retainedVertices_iff r.1 c c.1.hi).2
    exact Or.inr (Or.inl rfl)

/-- Any failure of full activity for the least rejecting cut must therefore
come from a constraint that retains the originally excluded vertex. -/
theorem OptionalSignatureRegion.nonactive_minimalExcludingCut_witness_retains
    {n : ℕ} {D : Dissection n} (r : OptionalSignatureRegion D)
    (v : Fin n) (h : (excludingSignatureCuts D r.1 v).Nonempty)
    (x : Fin n)
    (hxEndpoint : x = (minimalExcludingCut D r.1 v h).1.lo ∨
      x = (minimalExcludingCut D r.1 v h).1.hi)
    (hx : ¬ VertexInCutSignature D r.1 x) :
    ∃ e : {c // c ∈ D.1},
      v ∈ retainedVertices r.1 e ∧ x ∉ retainedVertices r.1 e := by
  rw [vertexInCutSignature_iff_forall_mem_retainedVertices] at hx
  push Not at hx
  rcases hx with ⟨e, hxe⟩
  refine ⟨e, ?_, hxe⟩
  by_contra hve
  have he : e ∈ excludingSignatureCuts D r.1 v :=
    (mem_excludingSignatureCuts_iff_not_mem_retainedVertices
      D r.1 v e).2 hve
  have hendpoints := r.minimalExcludingCut_endpoints_mem_rejecting v h e he
  rcases hxEndpoint with rfl | rfl
  · exact hxe hendpoints.1
  · exact hxe hendpoints.2

/-- A noncrossing constraint retaining two distinct common witnesses but
rejecting an endpoint of `c` has retained side nested inside that of `c`. -/
theorem retainedVertices_subset_of_endpoint_rejected
    {n : ℕ} {D : Dissection n}
    (s : {c // c ∈ D.1} → Bool) (c e : {c // c ∈ D.1})
    (hnc : ¬ Crosses c.1 e.1) (w z : Fin n) (hwz : w ≠ z)
    (hwc : w ∈ retainedVertices s c) (hwe : w ∈ retainedVertices s e)
    (hzc : z ∈ retainedVertices s c) (hze : z ∈ retainedVertices s e)
    (hend : c.1.lo ∉ retainedVertices s e ∨
      c.1.hi ∉ retainedVertices s e) :
    retainedVertices s e ⊆ retainedVertices s c := by
  have hwzVal : w.val ≠ z.val := fun h => hwz (Fin.ext h)
  unfold Crosses at hnc
  cases hc : s c <;> cases he : s e
  · have hwc' := (mem_retainedVertices_false_iff s c hc w).1 hwc
    have hwe' := (mem_retainedVertices_false_iff s e he w).1 hwe
    have hzc' := (mem_retainedVertices_false_iff s c hc z).1 hzc
    have hze' := (mem_retainedVertices_false_iff s e he z).1 hze
    intro x hx
    have hx' := (mem_retainedVertices_false_iff s e he x).1 hx
    apply (mem_retainedVertices_false_iff s c hc x).2
    rcases hend with hend | hend
    · have hend' : ¬(c.1.lo.val ≤ e.1.lo.val ∨
          e.1.hi.val ≤ c.1.lo.val) := by
        intro h
        exact hend ((mem_retainedVertices_false_iff s e he c.1.lo).2 h)
      rcases hwc' with hwc' | hwc' <;>
        rcases hwe' with hwe' | hwe' <;>
        rcases hzc' with hzc' | hzc' <;>
        rcases hze' with hze' | hze' <;>
        rcases hx' with hx' | hx' <;> omega
    · have hend' : ¬(c.1.hi.val ≤ e.1.lo.val ∨
          e.1.hi.val ≤ c.1.hi.val) := by
        intro h
        exact hend ((mem_retainedVertices_false_iff s e he c.1.hi).2 h)
      rcases hwc' with hwc' | hwc' <;>
        rcases hwe' with hwe' | hwe' <;>
        rcases hzc' with hzc' | hzc' <;>
        rcases hze' with hze' | hze' <;>
        rcases hx' with hx' | hx' <;> omega
  · have hwc' := (mem_retainedVertices_false_iff s c hc w).1 hwc
    have hwe' := (mem_retainedVertices_true_iff s e he w).1 hwe
    have hzc' := (mem_retainedVertices_false_iff s c hc z).1 hzc
    have hze' := (mem_retainedVertices_true_iff s e he z).1 hze
    intro x hx
    have hx' := (mem_retainedVertices_true_iff s e he x).1 hx
    apply (mem_retainedVertices_false_iff s c hc x).2
    rcases hend with hend | hend
    · have hend' : ¬(e.1.lo.val ≤ c.1.lo.val ∧
          c.1.lo.val ≤ e.1.hi.val) := by
        intro h
        exact hend ((mem_retainedVertices_true_iff s e he c.1.lo).2 h)
      rcases hwc' with hwc' | hwc' <;>
        rcases hzc' with hzc' | hzc' <;> omega
    · have hend' : ¬(e.1.lo.val ≤ c.1.hi.val ∧
          c.1.hi.val ≤ e.1.hi.val) := by
        intro h
        exact hend ((mem_retainedVertices_true_iff s e he c.1.hi).2 h)
      rcases hwc' with hwc' | hwc' <;>
        rcases hzc' with hzc' | hzc' <;> omega
  · have hwc' := (mem_retainedVertices_true_iff s c hc w).1 hwc
    have hwe' := (mem_retainedVertices_false_iff s e he w).1 hwe
    have hzc' := (mem_retainedVertices_true_iff s c hc z).1 hzc
    have hze' := (mem_retainedVertices_false_iff s e he z).1 hze
    intro x hx
    have hx' := (mem_retainedVertices_false_iff s e he x).1 hx
    apply (mem_retainedVertices_true_iff s c hc x).2
    rcases hend with hend | hend
    · have hend' : ¬(c.1.lo.val ≤ e.1.lo.val ∨
          e.1.hi.val ≤ c.1.lo.val) := by
        intro h
        exact hend ((mem_retainedVertices_false_iff s e he c.1.lo).2 h)
      rcases hwe' with hwe' | hwe' <;>
        rcases hze' with hze' | hze' <;>
        rcases hx' with hx' | hx' <;> omega
    · have hend' : ¬(c.1.hi.val ≤ e.1.lo.val ∨
          e.1.hi.val ≤ c.1.hi.val) := by
        intro h
        exact hend ((mem_retainedVertices_false_iff s e he c.1.hi).2 h)
      rcases hwe' with hwe' | hwe' <;>
        rcases hze' with hze' | hze' <;>
        rcases hx' with hx' | hx' <;> omega
  · have hwc' := (mem_retainedVertices_true_iff s c hc w).1 hwc
    have hwe' := (mem_retainedVertices_true_iff s e he w).1 hwe
    have hzc' := (mem_retainedVertices_true_iff s c hc z).1 hzc
    have hze' := (mem_retainedVertices_true_iff s e he z).1 hze
    intro x hx
    have hx' := (mem_retainedVertices_true_iff s e he x).1 hx
    apply (mem_retainedVertices_true_iff s c hc x).2
    rcases hend with hend | hend
    · have hend' : ¬(e.1.lo.val ≤ c.1.lo.val ∧
          c.1.lo.val ≤ e.1.hi.val) := by
        intro h
        exact hend ((mem_retainedVertices_true_iff s e he c.1.lo).2 h)
      omega
    · have hend' : ¬(e.1.lo.val ≤ c.1.hi.val ∧
          c.1.hi.val ≤ e.1.hi.val) := by
        intro h
        exact hend ((mem_retainedVertices_true_iff s e he c.1.hi).2 h)
      omega

/-- The remaining geometric core: every selected-cut side rejecting an
endpoint of `c` is nested inside the side retained by `c`. -/
def EndpointSeparatorNesting
    {n : ℕ} {D : Dissection n} (r : OptionalSignatureRegion D)
    (c : {c // c ∈ D.1}) : Prop :=
  ∀ e : {e // e ∈ D.1},
    (c.1.lo ∉ retainedVertices r.1 e ∨
      c.1.hi ∉ retainedVertices r.1 e) →
    retainedVertices r.1 e ⊆ retainedVertices r.1 c

/-- Endpoint-separator nesting is forced by dissection noncrossing and the two
distinct endpoints of the occupied-region witness diagonal. -/
theorem OptionalSignatureRegion.endpointSeparatorNesting
    {n : ℕ} {D : Dissection n} (r : OptionalSignatureRegion D)
    (c : {c // c ∈ D.1}) : EndpointSeparatorNesting r c := by
  intro e hend
  by_cases hce : c.1 = e.1
  · have hce' : c = e := Subtype.ext hce
    subst e
    rcases hend with hend | hend
    · exact False.elim (hend ((mem_retainedVertices_iff r.1 c c.1.lo).2
        (Or.inl rfl)))
    · exact False.elim (hend ((mem_retainedVertices_iff r.1 c c.1.hi).2
        (Or.inr (Or.inl rfl))))
  · let q := r.witnessRegionalDiagonal
    have hloVertex : VertexInCutSignature D r.1 q.1.1.lo := by
      simpa [optionalSignatureRegionVertices] using q.lower_mem_vertices
    have hhiVertex : VertexInCutSignature D r.1 q.1.1.hi := by
      simpa [optionalSignatureRegionVertices] using q.upper_mem_vertices
    exact retainedVertices_subset_of_endpoint_rejected r.1 c e
      (D.2 c.2 e.2 hce) q.1.1.lo q.1.1.hi (ne_of_lt q.1.1.ordered)
      ((vertexInCutSignature_iff_forall_mem_retainedVertices
        D r.1 q.1.1.lo).1 hloVertex c)
      ((vertexInCutSignature_iff_forall_mem_retainedVertices
        D r.1 q.1.1.lo).1 hloVertex e)
      ((vertexInCutSignature_iff_forall_mem_retainedVertices
        D r.1 q.1.1.hi).1 hhiVertex c)
      ((vertexInCutSignature_iff_forall_mem_retainedVertices
        D r.1 q.1.1.hi).1 hhiVertex e) hend

/-- Endpoint-separator nesting upgrades the canonical least rejecting cut to
an active cut. This isolates the sole remaining geometric lemma from the
finite-choice and minimum-cardinality argument. -/
theorem OptionalSignatureRegion.minimalExcludingCut_active_of_separatorNesting
    {n : ℕ} {D : Dissection n} (r : OptionalSignatureRegion D)
    (v : Fin n) (h : (excludingSignatureCuts D r.1 v).Nonempty)
    (hnest : EndpointSeparatorNesting r
      (minimalExcludingCut D r.1 v h)) :
    VertexInCutSignature D r.1
        (minimalExcludingCut D r.1 v h).1.lo ∧
      VertexInCutSignature D r.1
        (minimalExcludingCut D r.1 v h).1.hi := by
  let c := minimalExcludingCut D r.1 v h
  have hvc : v ∉ retainedVertices r.1 c :=
    (mem_excludingSignatureCuts_iff_not_mem_retainedVertices
      D r.1 v c).1 (minimalExcludingCut_mem D r.1 v h)
  constructor
  · apply (vertexInCutSignature_iff_forall_mem_retainedVertices
      D r.1 c.1.lo).2
    intro e
    by_contra hlo
    have hsub : retainedVertices r.1 e ⊆ retainedVertices r.1 c :=
      hnest e (Or.inl hlo)
    have hve : v ∈ retainedVertices r.1 e := by
      by_contra hv
      have he : e ∈ excludingSignatureCuts D r.1 v :=
        (mem_excludingSignatureCuts_iff_not_mem_retainedVertices
          D r.1 v e).2 hv
      exact hlo (r.minimalExcludingCut_endpoints_mem_rejecting v h e he).1
    exact hvc (hsub hve)
  · apply (vertexInCutSignature_iff_forall_mem_retainedVertices
      D r.1 c.1.hi).2
    intro e
    by_contra hhi
    have hsub : retainedVertices r.1 e ⊆ retainedVertices r.1 c :=
      hnest e (Or.inr hhi)
    have hve : v ∈ retainedVertices r.1 e := by
      by_contra hv
      have he : e ∈ excludingSignatureCuts D r.1 v :=
        (mem_excludingSignatureCuts_iff_not_mem_retainedVertices
          D r.1 v e).2 hv
      exact hhi (r.minimalExcludingCut_endpoints_mem_rejecting v h e he).2
    exact hvc (hsub hve)

/-- The canonical least cut excluding a vertex is active, with no supplied
geometric interface. -/
theorem OptionalSignatureRegion.minimalExcludingCut_active
    {n : ℕ} {D : Dissection n} (r : OptionalSignatureRegion D)
    (v : Fin n) (h : (excludingSignatureCuts D r.1 v).Nonempty) :
    VertexInCutSignature D r.1
        (minimalExcludingCut D r.1 v h).1.lo ∧
      VertexInCutSignature D r.1
        (minimalExcludingCut D r.1 v h).1.hi :=
  r.minimalExcludingCut_active_of_separatorNesting v h
    (r.endpointSeparatorNesting (minimalExcludingCut D r.1 v h))

/-- Canonically labelled vertices of an occupied signature region. -/
def OptionalSignatureRegionVertex {n : ℕ} {D : Dissection n}
    (r : OptionalSignatureRegion D) :=
  {v : Fin n // v ∈ optionalSignatureRegionVertices r}

theorem OptionalSignatureRegionVertex.inCutSignature
    {n : ℕ} {D : Dissection n} {r : OptionalSignatureRegion D}
    (v : OptionalSignatureRegionVertex r) :
    VertexInCutSignature D r.1 v.1 := by
  simpa [optionalSignatureRegionVertices] using v.2

noncomputable instance optionalSignatureRegionVertexFintype {n : ℕ}
    {D : Dissection n} (r : OptionalSignatureRegion D) :
    Fintype (OptionalSignatureRegionVertex r) :=
  Finset.Subtype.fintype (optionalSignatureRegionVertices r)

instance optionalSignatureRegionVertexLinearOrder {n : ℕ}
    {D : Dissection n} (r : OptionalSignatureRegion D) :
    LinearOrder (OptionalSignatureRegionVertex r) := by
  unfold OptionalSignatureRegionVertex
  infer_instance

noncomputable def optionalSignatureRegionVertexOrderLabels {n : ℕ}
    {D : Dissection n} (r : OptionalSignatureRegion D) :
    OptionalSignatureRegionVertex r ≃o Fin (optionalSignatureRegionArity r) := by
  classical
  exact (Finset.orderIsoOfFin (optionalSignatureRegionVertices r) rfl).symm

noncomputable def optionalSignatureRegionVertexLabels {n : ℕ}
    {D : Dissection n} (r : OptionalSignatureRegion D) :
    OptionalSignatureRegionVertex r ≃ Fin (optionalSignatureRegionArity r) :=
  (optionalSignatureRegionVertexOrderLabels r).toEquiv

/-- An order embedding of finite linear orders cannot insert a target point
between consecutive source images. -/
theorem fin_orderEmbedding_reflects_consecutive {m n : ℕ}
    (f : Fin m ↪o Fin n) {a b : Fin m} (hab : a < b)
    (himages : (f b).val = (f a).val + 1) :
    b.val = a.val + 1 := by
  by_contra h
  have hgap : a.val + 1 < b.val := by omega
  let k : Fin m := ⟨a.val + 1, by omega⟩
  have hak : a < k := by
    change a.val < k.val
    simp [k]
  have hkb : k < b := by
    change k.val < b.val
    simpa [k] using hgap
  have hafk : f a < f k := f.lt_iff_lt.mpr hak
  have hkfb : f k < f b := f.lt_iff_lt.mpr hkb
  omega

/-- If an ordered finite set has no point strictly between two elements,
their canonical finite labels are consecutive. -/
theorem orderIso_labels_consecutive_of_no_between
    {α : Type*} [LinearOrder α] {m : ℕ} (e : α ≃o Fin m)
    (a b : α) (hab : a < b)
    (hno : ∀ x : α, ¬(a < x ∧ x < b)) :
    (e b).val = (e a).val + 1 := by
  by_contra h
  have hgap : (e a).val + 1 < (e b).val := by
    have := e.lt_iff_lt.mpr hab
    omega
  let k : Fin m := ⟨(e a).val + 1, by omega⟩
  apply hno (e.symm k)
  have hak : e a < k := by
    change (e a).val < k.val
    simp [k]
  have hkb : k < e b := by
    change k.val < (e b).val
    simpa [k] using hgap
  constructor
  · apply e.lt_iff_lt.mp
    simpa using hak
  · apply e.lt_iff_lt.mp
    simpa using hkb

/-- A least element of a finite ordered set receives label zero. -/
theorem orderIso_label_zero_of_no_lt
    {α : Type*} [LinearOrder α] {m : ℕ} (e : α ≃o Fin m)
    (a : α) (hmin : ∀ x : α, ¬ x < a) : (e a).val = 0 := by
  by_contra h
  have hpos : 0 < (e a).val := by omega
  let z : Fin m := ⟨0, Nat.zero_lt_of_lt (e a).isLt⟩
  have hza : z < e a := by
    change z.val < (e a).val
    simpa [z] using hpos
  apply hmin (e.symm z)
  apply e.lt_iff_lt.mp
  simpa using hza

/-- A greatest element of a finite ordered set receives the final label. -/
theorem orderIso_label_last_of_no_lt
    {α : Type*} [LinearOrder α] {m : ℕ} (e : α ≃o Fin m)
    (a : α) (hmax : ∀ x : α, ¬ a < x) : (e a).val + 1 = m := by
  by_contra h
  have hnext : (e a).val + 1 < m := by omega
  let k : Fin m := ⟨(e a).val + 1, hnext⟩
  have hak : e a < k := by
    change (e a).val < k.val
    simp [k]
  apply hmax (e.symm k)
  apply e.lt_iff_lt.mp
  simpa using hak

/-- An embedded source point mapping to ambient zero is source zero. -/
theorem fin_orderEmbedding_reflects_zero {m n : ℕ}
    (f : Fin m ↪o Fin n) (a : Fin m) (ha : (f a).val = 0) :
    a.val = 0 := by
  by_contra h
  have haPos : 0 < a.val := by omega
  let z : Fin m := ⟨0, Nat.zero_lt_of_lt a.isLt⟩
  have hza : z < a := by
    change z.val < a.val
    simpa [z] using haPos
  have := f.lt_iff_lt.mpr hza
  omega

/-- An embedded source point mapping to the final ambient point is the final
source point. -/
theorem fin_orderEmbedding_reflects_last {m n : ℕ}
    (f : Fin m ↪o Fin n) (a : Fin m) (ha : (f a).val + 1 = n) :
    a.val + 1 = m := by
  by_contra h
  have hnext : a.val + 1 < m := by omega
  let k : Fin m := ⟨a.val + 1, hnext⟩
  have hak : a < k := by
    change a.val < k.val
    simp [k]
  have hafk := f.lt_iff_lt.mpr hak
  have hkBound := (f k).isLt
  omega

/-- Therefore ambient consecutive regional vertices receive consecutive local
labels. -/
theorem optionalSignatureRegionLabels_consecutive
    {n : ℕ} {D : Dissection n} (r : OptionalSignatureRegion D)
    (a b : OptionalSignatureRegionVertex r) (hab : a < b)
    (hsource : b.1.val = a.1.val + 1) :
    (optionalSignatureRegionVertexOrderLabels r b).val =
      (optionalSignatureRegionVertexOrderLabels r a).val + 1 := by
  let f : Fin (optionalSignatureRegionArity r) ↪o Fin n :=
    (optionalSignatureRegionVertexOrderLabels r).symm.toOrderEmbedding.trans
      ⟨Function.Embedding.subtype _, by intro a b; rfl⟩
  apply fin_orderEmbedding_reflects_consecutive f
  · exact (optionalSignatureRegionVertexOrderLabels r).lt_iff_lt.mpr hab
  · dsimp [f]
    rw [OrderIso.symm_apply_apply, OrderIso.symm_apply_apply]
    exact hsource

/-- Ambient wrap endpoints receive the first and final local labels. -/
theorem optionalSignatureRegionLabels_wrap
    {n : ℕ} {D : Dissection n} (r : OptionalSignatureRegion D)
    (a b : OptionalSignatureRegionVertex r)
    (ha : a.1.val = 0) (hb : b.1.val + 1 = n) :
    (optionalSignatureRegionVertexOrderLabels r a).val = 0 ∧
      (optionalSignatureRegionVertexOrderLabels r b).val + 1 =
        optionalSignatureRegionArity r := by
  let f : Fin (optionalSignatureRegionArity r) ↪o Fin n :=
    (optionalSignatureRegionVertexOrderLabels r).symm.toOrderEmbedding.trans
      ⟨Function.Embedding.subtype _, by intro x y; rfl⟩
  constructor
  · apply fin_orderEmbedding_reflects_zero f
    dsimp [f]
    rw [OrderIso.symm_apply_apply]
    exact ha
  · apply fin_orderEmbedding_reflects_last f
    dsimp [f]
    rw [OrderIso.symm_apply_apply]
    exact hb

/-- Ordered local chord before proving that its endpoints are nonadjacent in
the regional cyclic order. -/
structure LocalOrderedChord (m : ℕ) where
  lo : Fin m
  hi : Fin m
  ordered : lo < hi

theorem localOrderedChord_eq_of_endpoints {m : ℕ}
    {a b : LocalOrderedChord m} (hlo : a.lo = b.lo) (hhi : a.hi = b.hi) :
    a = b := by
  cases a
  cases b
  cases hlo
  cases hhi
  rfl

/-- Exact additional conditions promoting an ordered local chord to a
standard polygon diagonal. -/
def LocalOrderedChord.IsPolygonDiagonal {m : ℕ}
    (d : LocalOrderedChord m) : Prop :=
  d.hi.val ≠ d.lo.val + 1 ∧
    ¬(d.lo.val = 0 ∧ d.hi.val + 1 = m)

/-- A standard local chord canonically determines an ambient polygon
diagonal by inverse regional vertex labeling. -/
noncomputable def LocalOrderedChord.toAmbientDiagonal
    {n : ℕ} {D : Dissection n} (r : OptionalSignatureRegion D)
    (d : LocalOrderedChord (optionalSignatureRegionArity r))
    (h : d.IsPolygonDiagonal) : Diagonal n := by
  classical
  let a := (optionalSignatureRegionVertexOrderLabels r).symm d.lo
  let b := (optionalSignatureRegionVertexOrderLabels r).symm d.hi
  have hab : a < b := by
    apply (optionalSignatureRegionVertexOrderLabels r).lt_iff_lt.mp
    simpa [a, b] using d.ordered
  refine ⟨a.1, b.1, hab, ?_, ?_⟩
  · intro hsource
    apply h.1
    simpa [a, b] using
      optionalSignatureRegionLabels_consecutive r a b hab hsource
  · intro hsource
    apply h.2
    have hw := optionalSignatureRegionLabels_wrap r a b hsource.1 hsource.2
    simpa [a, b] using hw

@[simp] theorem LocalOrderedChord.toAmbientDiagonal_lo
    {n : ℕ} {D : Dissection n} (r : OptionalSignatureRegion D)
    (d : LocalOrderedChord (optionalSignatureRegionArity r))
    (h : d.IsPolygonDiagonal) :
    (d.toAmbientDiagonal r h).lo =
      ((optionalSignatureRegionVertexOrderLabels r).symm d.lo).1 := rfl

@[simp] theorem LocalOrderedChord.toAmbientDiagonal_hi
    {n : ℕ} {D : Dissection n} (r : OptionalSignatureRegion D)
    (d : LocalOrderedChord (optionalSignatureRegionArity r))
    (h : d.IsPolygonDiagonal) :
    (d.toAmbientDiagonal r h).hi =
      ((optionalSignatureRegionVertexOrderLabels r).symm d.hi).1 := rfl

/-- The ambient lift of every standard local chord is compatible with the
entire dissection. -/
theorem LocalOrderedChord.toAmbientDiagonal_compatible
    {n : ℕ} {D : Dissection n} (r : OptionalSignatureRegion D)
    (d : LocalOrderedChord (optionalSignatureRegionArity r))
    (h : d.IsPolygonDiagonal) :
    CompatibleWith D (d.toAmbientDiagonal r h) := by
  apply compatibleWith_of_endpoints_in_cutSignature D r.1
  · change VertexInCutSignature D r.1
      ((optionalSignatureRegionVertexOrderLabels r).symm d.lo).1
    have hm := ((optionalSignatureRegionVertexOrderLabels r).symm d.lo).2
    simpa [optionalSignatureRegionVertices] using hm
  · change VertexInCutSignature D r.1
      ((optionalSignatureRegionVertexOrderLabels r).symm d.hi).1
    have hm := ((optionalSignatureRegionVertexOrderLabels r).symm d.hi).2
    simpa [optionalSignatureRegionVertices] using hm

/-- A standard local chord cannot lift to an already selected cut: each cut
is either a consecutive edge or the wrap edge of either incident signature
closure. -/
theorem LocalOrderedChord.toAmbientDiagonal_not_mem
    {n : ℕ} {D : Dissection n} (r : OptionalSignatureRegion D)
    (d : LocalOrderedChord (optionalSignatureRegionArity r))
    (h : d.IsPolygonDiagonal) :
    d.toAmbientDiagonal r h ∉ D.1 := by
  intro hmem
  let a := (optionalSignatureRegionVertexOrderLabels r).symm d.lo
  let b := (optionalSignatureRegionVertexOrderLabels r).symm d.hi
  let cD : {c // c ∈ D.1} := ⟨d.toAmbientDiagonal r h, hmem⟩
  have hab : a < b := by
    apply (optionalSignatureRegionVertexOrderLabels r).lt_iff_lt.mp
    simpa [a, b] using d.ordered
  have closure (x : OptionalSignatureRegionVertex r) :=
    x.inCutSignature cD
  cases hs : r.1 cD
  · apply h.1
    have hcon := orderIso_labels_consecutive_of_no_between
      (optionalSignatureRegionVertexOrderLabels r) a b hab (by
        intro x hx
        have hxC := closure x
        rcases hxC with hxC | hxC | hxC
        · simp [cD] at hxC
          exact hx.1.ne (Subtype.ext hxC.symm)
        · simp [cD] at hxC
          exact hx.2.ne (Subtype.ext hxC)
        · have hinside : InChordInterval (d.toAmbientDiagonal r h) x.1 := by
            exact hx
          have : strictSide (d.toAmbientDiagonal r h) x.1 = true := by
            simp [strictSide, hinside]
          rw [this, hs] at hxC
          contradiction)
    simpa [a, b] using hcon
  · apply h.2
    constructor
    · have hz := orderIso_label_zero_of_no_lt
        (optionalSignatureRegionVertexOrderLabels r) a (by
          intro x hx
          have hxC := closure x
          rcases hxC with hxC | hxC | hxC
          · simp [cD] at hxC
            exact hx.ne (Subtype.ext hxC)
          · simp [cD] at hxC
            exact (hx.trans hab).ne (Subtype.ext hxC)
          · have hout : ¬ InChordInterval (d.toAmbientDiagonal r h) x.1 := by
              intro hin
              have hxv : x.1 ≤ a.1 := hx.le
              exact (not_lt_of_ge hxv) (by simpa [a] using hin.1)
            have : strictSide (d.toAmbientDiagonal r h) x.1 = false := by
              simp [strictSide, hout]
            rw [this, hs] at hxC
            contradiction)
      simpa [a] using hz
    · have hz := orderIso_label_last_of_no_lt
        (optionalSignatureRegionVertexOrderLabels r) b (by
          intro x hx
          have hxC := closure x
          rcases hxC with hxC | hxC | hxC
          · simp [cD] at hxC
            exact (hab.trans hx).ne' (Subtype.ext hxC)
          · simp [cD] at hxC
            exact hx.ne' (Subtype.ext hxC)
          · have hout : ¬ InChordInterval (d.toAmbientDiagonal r h) x.1 := by
              intro hin
              have hxv : b.1 ≤ x.1 := hx.le
              exact (not_lt_of_ge hxv) (by simpa [b] using hin.2)
            have : strictSide (d.toAmbientDiagonal r h) x.1 = false := by
              simp [strictSide, hout]
            rw [this, hs] at hxC
            contradiction)
      simpa [b] using hz

/-- Every standard local chord now has a canonical admissible global
optional diagonal. -/
noncomputable def LocalOrderedChord.toOptionalDiagonal
    {n : ℕ} {D : Dissection n} (r : OptionalSignatureRegion D)
    (d : LocalOrderedChord (optionalSignatureRegionArity r))
    (h : d.IsPolygonDiagonal) : OptionalDiagonal D :=
  ⟨d.toAmbientDiagonal r h,
    d.toAmbientDiagonal_not_mem r h,
    d.toAmbientDiagonal_compatible r h⟩

/-- The optional lift lies in the specified occupied signature fiber. -/
theorem LocalOrderedChord.toOptionalDiagonal_signature
    {n : ℕ} {D : Dissection n} (r : OptionalSignatureRegion D)
    (d : LocalOrderedChord (optionalSignatureRegionArity r))
    (h : d.IsPolygonDiagonal) :
    canonicalCutSideSignature D (d.toOptionalDiagonal r h).1 = r.1 := by
  apply canonicalCutSideSignature_eq_of_endpoints_in_signature D r.1
  · exact d.toAmbientDiagonal_not_mem r h
  · change VertexInCutSignature D r.1
      ((optionalSignatureRegionVertexOrderLabels r).symm d.lo).1
    exact ((optionalSignatureRegionVertexOrderLabels r).symm d.lo).inCutSignature
  · change VertexInCutSignature D r.1
      ((optionalSignatureRegionVertexOrderLabels r).symm d.hi).1
    exact ((optionalSignatureRegionVertexOrderLabels r).symm d.hi).inCutSignature

/-- Forget only the boundary-exclusion proofs of a standard diagonal. -/
def Diagonal.toLocalOrderedChord {m : ℕ} (d : Diagonal m) :
    LocalOrderedChord m := ⟨d.lo, d.hi, d.ordered⟩

@[simp] theorem Diagonal.toLocalOrderedChord_isPolygonDiagonal
    {m : ℕ} (d : Diagonal m) :
    d.toLocalOrderedChord.IsPolygonDiagonal :=
  ⟨d.notConsecutive, d.notWrap⟩

/-- Canonical inverse candidate from every standard lower-point diagonal into
the regional global-channel fiber. -/
noncomputable def standardDiagonalToRegional
    {n : ℕ} {D : Dissection n} (r : OptionalSignatureRegion D)
    (d : Diagonal (optionalSignatureRegionArity r)) :
    OptionalSignatureRegionalDiagonal r :=
  ⟨d.toLocalOrderedChord.toOptionalDiagonal r
      d.toLocalOrderedChord_isPolygonDiagonal,
    d.toLocalOrderedChord.toOptionalDiagonal_signature r
      d.toLocalOrderedChord_isPolygonDiagonal⟩

/-- Promote a local ordered chord once regional adjacency and wrap exclusion
have been proved. -/
def LocalOrderedChord.toDiagonal {m : ℕ} (d : LocalOrderedChord m)
    (h : d.IsPolygonDiagonal) : Diagonal m :=
  ⟨d.lo, d.hi, d.ordered, h.1, h.2⟩

/-- Promotion retains both local endpoints. -/
@[simp] theorem LocalOrderedChord.toDiagonal_lo {m : ℕ}
    (d : LocalOrderedChord m) (h : d.IsPolygonDiagonal) :
    (d.toDiagonal h).lo = d.lo := rfl

@[simp] theorem LocalOrderedChord.toDiagonal_hi {m : ℕ}
    (d : LocalOrderedChord m) (h : d.IsPolygonDiagonal) :
    (d.toDiagonal h).hi = d.hi := rfl

/-- Explicit order-preserving relabeling of a regional global diagonal to a
local ordered chord. -/
noncomputable def OptionalSignatureRegionalDiagonal.toLocalOrderedChord
    {n : ℕ} {D : Dissection n} {r : OptionalSignatureRegion D}
    (d : OptionalSignatureRegionalDiagonal r) :
    LocalOrderedChord (optionalSignatureRegionArity r) := by
  let lo : OptionalSignatureRegionVertex r := ⟨d.1.1.lo, d.lower_mem_vertices⟩
  let hi : OptionalSignatureRegionVertex r := ⟨d.1.1.hi, d.upper_mem_vertices⟩
  exact ⟨optionalSignatureRegionVertexOrderLabels r lo,
    optionalSignatureRegionVertexOrderLabels r hi,
    (optionalSignatureRegionVertexOrderLabels r).lt_iff_lt.mpr d.1.1.ordered⟩

/-- Consecutive local labels leave no closure vertex strictly between the
corresponding ambient endpoints. -/
theorem OptionalSignatureRegionalDiagonal.no_vertex_between_of_local_consecutive
    {n : ℕ} {D : Dissection n} {r : OptionalSignatureRegion D}
    (d : OptionalSignatureRegionalDiagonal r)
    (hcon : d.toLocalOrderedChord.hi.val =
      d.toLocalOrderedChord.lo.val + 1) :
    ∀ x : OptionalSignatureRegionVertex r,
      ¬(d.1.1.lo < x.1 ∧ x.1 < d.1.1.hi) := by
  let a : OptionalSignatureRegionVertex r :=
    ⟨d.1.1.lo, d.lower_mem_vertices⟩
  let b : OptionalSignatureRegionVertex r :=
    ⟨d.1.1.hi, d.upper_mem_vertices⟩
  intro x hx
  have hax : a < x := hx.1
  have hxb : x < b := hx.2
  have hlax := (optionalSignatureRegionVertexOrderLabels r).lt_iff_lt.mpr hax
  have hlxb := (optionalSignatureRegionVertexOrderLabels r).lt_iff_lt.mpr hxb
  change (optionalSignatureRegionVertexOrderLabels r b).val =
    (optionalSignatureRegionVertexOrderLabels r a).val + 1 at hcon
  omega

/-- Local wrap labels make the two ambient endpoints respectively least and
greatest among all vertices in the cut-side closure. -/
theorem OptionalSignatureRegionalDiagonal.no_vertex_outside_of_local_wrap
    {n : ℕ} {D : Dissection n} {r : OptionalSignatureRegion D}
    (d : OptionalSignatureRegionalDiagonal r)
    (hwrap : d.toLocalOrderedChord.lo.val = 0 ∧
      d.toLocalOrderedChord.hi.val + 1 = optionalSignatureRegionArity r) :
    (∀ x : OptionalSignatureRegionVertex r, ¬ x.1 < d.1.1.lo) ∧
      (∀ x : OptionalSignatureRegionVertex r, ¬ d.1.1.hi < x.1) := by
  let a : OptionalSignatureRegionVertex r :=
    ⟨d.1.1.lo, d.lower_mem_vertices⟩
  let b : OptionalSignatureRegionVertex r :=
    ⟨d.1.1.hi, d.upper_mem_vertices⟩
  change (optionalSignatureRegionVertexOrderLabels r a).val = 0 ∧
    (optionalSignatureRegionVertexOrderLabels r b).val + 1 =
      optionalSignatureRegionArity r at hwrap
  constructor
  · intro x hx
    have hxa : x < a := hx
    have hl := (optionalSignatureRegionVertexOrderLabels r).lt_iff_lt.mpr hxa
    omega
  · intro x hx
    have hbx : b < x := hx
    have hl := (optionalSignatureRegionVertexOrderLabels r).lt_iff_lt.mpr hbx
    have hbound := (optionalSignatureRegionVertexOrderLabels r x).isLt
    omega

/-- A locally consecutive regional pair is either already an ambient boundary
edge or is a selected cut. This is the linear, non-wrap boundary branch. -/
theorem OptionalSignatureRegionalDiagonal.selected_or_ambientConsecutive
    {n : ℕ} {D : Dissection n} {r : OptionalSignatureRegion D}
    (d : OptionalSignatureRegionalDiagonal r)
    (hcon : d.toLocalOrderedChord.hi.val =
      d.toLocalOrderedChord.lo.val + 1) :
    d.1.1 ∈ D.1 ∨ d.1.1.hi.val = d.1.1.lo.val + 1 := by
  by_cases hamb : d.1.1.hi.val = d.1.1.lo.val + 1
  · exact Or.inr hamb
  · have hgap : d.1.1.lo.val + 1 < d.1.1.hi.val := by
      have := d.1.1.ordered
      omega
    let v : Fin n := ⟨d.1.1.lo.val + 1, by
      have := d.1.1.hi.isLt
      omega⟩
    have hlo_v : d.1.1.lo < v := by
      change d.1.1.lo.val < v.val
      simp [v]
    have hv_hi : v < d.1.1.hi := by
      change v.val < d.1.1.hi.val
      simpa [v] using hgap
    have hvNot : ¬ VertexInCutSignature D r.1 v := by
      intro hv
      let x : OptionalSignatureRegionVertex r := ⟨v, by
        simpa [optionalSignatureRegionVertices] using hv⟩
      exact d.no_vertex_between_of_local_consecutive hcon x ⟨hlo_v, hv_hi⟩
    have hex : (excludingSignatureCuts D r.1 v).Nonempty :=
      (excludingSignatureCuts_nonempty_iff D r.1 v).2 hvNot
    let c := minimalExcludingCut D r.1 v hex
    have hcActive := r.minimalExcludingCut_active v hex
    have hvc : v ∉ retainedVertices r.1 c :=
      (mem_excludingSignatureCuts_iff_not_mem_retainedVertices
        D r.1 v c).1 (minimalExcludingCut_mem D r.1 v hex)
    have hloMem : d.1.1.lo ∈ retainedVertices r.1 c :=
      (vertexInCutSignature_iff_forall_mem_retainedVertices
        D r.1 d.1.1.lo).1 (by
          simpa [optionalSignatureRegionVertices] using d.lower_mem_vertices) c
    have hhiMem : d.1.1.hi ∈ retainedVertices r.1 c :=
      (vertexInCutSignature_iff_forall_mem_retainedVertices
        D r.1 d.1.1.hi).1 (by
          simpa [optionalSignatureRegionVertices] using d.upper_mem_vertices) c
    cases hc : r.1 c
    · have hvInside : c.1.lo.val < v.val ∧ v.val < c.1.hi.val := by
        have hv' : ¬(v.val ≤ c.1.lo.val ∨ c.1.hi.val ≤ v.val) := by
          intro h
          exact hvc ((mem_retainedVertices_false_iff r.1 c hc v).2 h)
        omega
      have hloOutside := (mem_retainedVertices_false_iff r.1 c hc d.1.1.lo).1 hloMem
      have hhiOutside := (mem_retainedVertices_false_iff r.1 c hc d.1.1.hi).1 hhiMem
      have hcLoBounds : d.1.1.lo.val ≤ c.1.lo.val := by
        rcases hloOutside with hloOutside | hloOutside <;> omega
      have hcHiBounds : c.1.hi.val ≤ d.1.1.hi.val := by
        rcases hhiOutside with hhiOutside | hhiOutside <;> omega
      have hcLoEq : c.1.lo = d.1.1.lo := by
        apply Fin.ext
        by_contra hne
        have hstrict : d.1.1.lo < c.1.lo := by
          change d.1.1.lo.val < c.1.lo.val
          omega
        let x : OptionalSignatureRegionVertex r := ⟨c.1.lo, by
          simpa [optionalSignatureRegionVertices] using hcActive.1⟩
        exact d.no_vertex_between_of_local_consecutive hcon x
          ⟨hstrict, by change c.1.lo.val < d.1.1.hi.val; omega⟩
      have hcHiEq : c.1.hi = d.1.1.hi := by
        apply Fin.ext
        by_contra hne
        have hstrict : c.1.hi < d.1.1.hi := by
          change c.1.hi.val < d.1.1.hi.val
          omega
        let x : OptionalSignatureRegionVertex r := ⟨c.1.hi, by
          simpa [optionalSignatureRegionVertices] using hcActive.2⟩
        exact d.no_vertex_between_of_local_consecutive hcon x
          ⟨by change d.1.1.lo.val < c.1.hi.val; omega, hstrict⟩
      left
      have hdiag : c.1 = d.1.1 :=
        diagonal_eq_of_endpoints hcLoEq hcHiEq
      rw [← hdiag]
      exact c.2
    · have hloInside := (mem_retainedVertices_true_iff r.1 c hc d.1.1.lo).1 hloMem
      have hhiInside := (mem_retainedVertices_true_iff r.1 c hc d.1.1.hi).1 hhiMem
      have hvOutside : ¬(c.1.lo.val ≤ v.val ∧ v.val ≤ c.1.hi.val) := by
        intro h
        exact hvc ((mem_retainedVertices_true_iff r.1 c hc v).2 h)
      omega

/-- A local wrap regional pair is either the ambient wrap edge or a selected
cut. -/
theorem OptionalSignatureRegionalDiagonal.selected_or_ambientWrap
    {n : ℕ} {D : Dissection n} {r : OptionalSignatureRegion D}
    (d : OptionalSignatureRegionalDiagonal r)
    (hwrap : d.toLocalOrderedChord.lo.val = 0 ∧
      d.toLocalOrderedChord.hi.val + 1 = optionalSignatureRegionArity r) :
    d.1.1 ∈ D.1 ∨
      (d.1.1.lo.val = 0 ∧ d.1.1.hi.val + 1 = n) := by
  by_cases hamb : d.1.1.lo.val = 0 ∧ d.1.1.hi.val + 1 = n
  · exact Or.inr hamb
  · have houtside := d.no_vertex_outside_of_local_wrap hwrap
    obtain ⟨v, hvOutside⟩ : ∃ v : Fin n,
        v < d.1.1.lo ∨ d.1.1.hi < v := by
      by_cases hlo : d.1.1.lo.val = 0
      · have hhi : d.1.1.hi.val + 1 < n := by
          have := d.1.1.hi.isLt
          omega
        exact ⟨⟨d.1.1.hi.val + 1, hhi⟩, Or.inr (by
          change d.1.1.hi.val < d.1.1.hi.val + 1
          omega)⟩
      · exact ⟨⟨0, Nat.zero_lt_of_lt d.1.1.lo.isLt⟩, Or.inl (by
          change 0 < d.1.1.lo.val
          omega)⟩
    have hvNot : ¬ VertexInCutSignature D r.1 v := by
      intro hv
      let x : OptionalSignatureRegionVertex r := ⟨v, by
        simpa [optionalSignatureRegionVertices] using hv⟩
      rcases hvOutside with hv | hv
      · exact houtside.1 x hv
      · exact houtside.2 x hv
    have hex : (excludingSignatureCuts D r.1 v).Nonempty :=
      (excludingSignatureCuts_nonempty_iff D r.1 v).2 hvNot
    let c := minimalExcludingCut D r.1 v hex
    have hcActive := r.minimalExcludingCut_active v hex
    have hvc : v ∉ retainedVertices r.1 c :=
      (mem_excludingSignatureCuts_iff_not_mem_retainedVertices
        D r.1 v c).1 (minimalExcludingCut_mem D r.1 v hex)
    have hloMem : d.1.1.lo ∈ retainedVertices r.1 c :=
      (vertexInCutSignature_iff_forall_mem_retainedVertices
        D r.1 d.1.1.lo).1 (by
          simpa [optionalSignatureRegionVertices] using d.lower_mem_vertices) c
    have hhiMem : d.1.1.hi ∈ retainedVertices r.1 c :=
      (vertexInCutSignature_iff_forall_mem_retainedVertices
        D r.1 d.1.1.hi).1 (by
          simpa [optionalSignatureRegionVertices] using d.upper_mem_vertices) c
    have hcLoLower : d.1.1.lo.val ≤ c.1.lo.val := by
      by_contra h
      let x : OptionalSignatureRegionVertex r := ⟨c.1.lo, by
        simpa [optionalSignatureRegionVertices] using hcActive.1⟩
      exact houtside.1 x (by change c.1.lo.val < d.1.1.lo.val; omega)
    have hcHiUpper : c.1.hi.val ≤ d.1.1.hi.val := by
      by_contra h
      let x : OptionalSignatureRegionVertex r := ⟨c.1.hi, by
        simpa [optionalSignatureRegionVertices] using hcActive.2⟩
      exact houtside.2 x (by change d.1.1.hi.val < c.1.hi.val; omega)
    cases hc : r.1 c
    · apply False.elim
      apply hvc
      apply (mem_retainedVertices_false_iff r.1 c hc v).2
      rcases hvOutside with hv | hv
      · exact Or.inl (by omega)
      · exact Or.inr (by omega)
    · have hloInside :=
        (mem_retainedVertices_true_iff r.1 c hc d.1.1.lo).1 hloMem
      have hhiInside :=
        (mem_retainedVertices_true_iff r.1 c hc d.1.1.hi).1 hhiMem
      have hcLoEq : c.1.lo = d.1.1.lo := Fin.ext (by omega)
      have hcHiEq : c.1.hi = d.1.1.hi := Fin.ext (by omega)
      left
      have hdiag : c.1 = d.1.1 :=
        diagonal_eq_of_endpoints hcLoEq hcHiEq
      rw [← hdiag]
      exact c.2

/-- Combinatorial boundary classification for a cut-side closure: a pair
consecutive in the regional order is either a selected cut or an ambient
polygon boundary pair. This is the exact geometry lemma needed below. -/
def RegionalBoundaryPairClassification {n : ℕ} {D : Dissection n}
    (r : OptionalSignatureRegion D) : Prop :=
  ∀ d : OptionalSignatureRegionalDiagonal r,
    ((d.toLocalOrderedChord.hi.val = d.toLocalOrderedChord.lo.val + 1) →
      d.1.1 ∈ D.1 ∨ d.1.1.hi.val = d.1.1.lo.val + 1) ∧
    ((d.toLocalOrderedChord.lo.val = 0 ∧
        d.toLocalOrderedChord.hi.val + 1 = optionalSignatureRegionArity r) →
      d.1.1 ∈ D.1 ∨
        (d.1.1.lo.val = 0 ∧ d.1.1.hi.val + 1 = n))

/-- Every occupied cut-side closure has the canonical boundary-pair
classification, with no supplied geometric interface. -/
theorem OptionalSignatureRegion.regionalBoundaryPairClassification
    {n : ℕ} {D : Dissection n} (r : OptionalSignatureRegion D) :
    RegionalBoundaryPairClassification r := by
  intro d
  exact ⟨d.selected_or_ambientConsecutive,
    d.selected_or_ambientWrap⟩

/-- Regional adjacency exclusion is canonical for every occupied cut-side
closure: optionality excludes selected cuts, while the ambient diagonal type
excludes polygon boundary pairs. -/
theorem OptionalSignatureRegion.regionalAdjacencyExclusion
    {n : ℕ} {D : Dissection n} (r : OptionalSignatureRegion D)
    (d : OptionalSignatureRegionalDiagonal r) :
    d.toLocalOrderedChord.IsPolygonDiagonal := by
  have h := r.regionalBoundaryPairClassification
  constructor
  · intro hconsecutive
    rcases (h d).1 hconsecutive with hselected | hambient
    · exact d.1.2.1 hselected
    · exact d.1.1.notConsecutive hambient
  · intro hwrap
    rcases (h d).2 hwrap with hselected | hambient
    · exact d.1.2.1 hselected
    · exact d.1.1.notWrap hambient

/-- Every regional global channel has a canonical standard local polygon
diagonal. -/
noncomputable def regionalDiagonalToStandard
    {n : ℕ} {D : Dissection n} {r : OptionalSignatureRegion D}
    (d : OptionalSignatureRegionalDiagonal r) :
    Diagonal (optionalSignatureRegionArity r) :=
  d.toLocalOrderedChord.toDiagonal (r.regionalAdjacencyExclusion d)

/-- Order-preserving regional relabeling is injective. -/
theorem OptionalSignatureRegionalDiagonal.toLocalOrderedChord_injective
    {n : ℕ} {D : Dissection n} {r : OptionalSignatureRegion D} :
    Function.Injective
      (@OptionalSignatureRegionalDiagonal.toLocalOrderedChord n D r) := by
  intro a b h
  have hloLab := congrArg LocalOrderedChord.lo h
  have hhiLab := congrArg LocalOrderedChord.hi h
  have hloVertex :
      (⟨a.1.1.lo, a.lower_mem_vertices⟩ : OptionalSignatureRegionVertex r) =
      ⟨b.1.1.lo, b.lower_mem_vertices⟩ := by
    apply (optionalSignatureRegionVertexOrderLabels r).injective
    simpa [OptionalSignatureRegionalDiagonal.toLocalOrderedChord] using hloLab
  have hhiVertex :
      (⟨a.1.1.hi, a.upper_mem_vertices⟩ : OptionalSignatureRegionVertex r) =
      ⟨b.1.1.hi, b.upper_mem_vertices⟩ := by
    apply (optionalSignatureRegionVertexOrderLabels r).injective
    simpa [OptionalSignatureRegionalDiagonal.toLocalOrderedChord] using hhiLab
  have hlo := congrArg Subtype.val hloVertex
  have hhi := congrArg Subtype.val hhiVertex
  have hdiag : a.1.1 = b.1.1 := diagonal_eq_of_endpoints hlo hhi
  exact Subtype.ext (Subtype.ext hdiag)

/-- Lifting a standard diagonal and relabeling its endpoints back to the
region recovers the original ordered chord. -/
theorem standardDiagonalToRegional_toLocalOrderedChord
    {n : ℕ} {D : Dissection n} (r : OptionalSignatureRegion D)
    (d : Diagonal (optionalSignatureRegionArity r)) :
    (standardDiagonalToRegional r d).toLocalOrderedChord =
      d.toLocalOrderedChord := by
  apply localOrderedChord_eq_of_endpoints
  · change (optionalSignatureRegionVertexOrderLabels r)
      ⟨((optionalSignatureRegionVertexOrderLabels r).symm d.lo).1, _⟩ = d.lo
    calc
      _ = (optionalSignatureRegionVertexOrderLabels r)
          ((optionalSignatureRegionVertexOrderLabels r).symm d.lo) := by
            congr 1
      _ = d.lo := (optionalSignatureRegionVertexOrderLabels r).apply_symm_apply d.lo
  · change (optionalSignatureRegionVertexOrderLabels r)
      ⟨((optionalSignatureRegionVertexOrderLabels r).symm d.hi).1, _⟩ = d.hi
    calc
      _ = (optionalSignatureRegionVertexOrderLabels r)
          ((optionalSignatureRegionVertexOrderLabels r).symm d.hi) := by
            congr 1
      _ = d.hi := (optionalSignatureRegionVertexOrderLabels r).apply_symm_apply d.hi

/-- Hence the canonical lift from standard lower-point diagonals is injective. -/
theorem standardDiagonalToRegional_injective
    {n : ℕ} {D : Dissection n} (r : OptionalSignatureRegion D) :
    Function.Injective (standardDiagonalToRegional r) := by
  intro a b hab
  have hlocal := congrArg
    OptionalSignatureRegionalDiagonal.toLocalOrderedChord hab
  rw [standardDiagonalToRegional_toLocalOrderedChord,
    standardDiagonalToRegional_toLocalOrderedChord] at hlocal
  exact diagonal_eq_of_endpoints
    (congrArg LocalOrderedChord.lo hlocal)
    (congrArg LocalOrderedChord.hi hlocal)

/-- Standard local-diagonal relabeling is injective. -/
theorem regionalDiagonalToStandard_injective
    {n : ℕ} {D : Dissection n} {r : OptionalSignatureRegion D} :
    Function.Injective (@regionalDiagonalToStandard n D r) := by
  intro a b hab
  apply OptionalSignatureRegionalDiagonal.toLocalOrderedChord_injective
  apply localOrderedChord_eq_of_endpoints
  · exact congrArg Diagonal.lo hab
  · exact congrArg Diagonal.hi hab

/-- Standardization followed by canonical lifting recovers the original
regional channel. -/
theorem standardDiagonalToRegional_regionalDiagonalToStandard
    {n : ℕ} {D : Dissection n} {r : OptionalSignatureRegion D}
    (d : OptionalSignatureRegionalDiagonal r) :
    standardDiagonalToRegional r (regionalDiagonalToStandard d) = d := by
  apply OptionalSignatureRegionalDiagonal.toLocalOrderedChord_injective
  rw [standardDiagonalToRegional_toLocalOrderedChord]
  apply localOrderedChord_eq_of_endpoints <;> rfl

/-- Canonical regional relabeling preserves and reflects chord crossing. -/
theorem regionalDiagonalToStandard_crosses_iff
    {n : ℕ} {D : Dissection n} {r : OptionalSignatureRegion D}
    (a b : OptionalSignatureRegionalDiagonal r) :
    Crosses (regionalDiagonalToStandard a)
        (regionalDiagonalToStandard b) ↔
      Crosses a.1.1 b.1.1 := by
  have ll : a.toLocalOrderedChord.lo < b.toLocalOrderedChord.lo ↔
      a.1.1.lo < b.1.1.lo := by
    unfold OptionalSignatureRegionalDiagonal.toLocalOrderedChord
    exact (optionalSignatureRegionVertexOrderLabels r).lt_iff_lt
  have lh : a.toLocalOrderedChord.lo < b.toLocalOrderedChord.hi ↔
      a.1.1.lo < b.1.1.hi := by
    unfold OptionalSignatureRegionalDiagonal.toLocalOrderedChord
    exact (optionalSignatureRegionVertexOrderLabels r).lt_iff_lt
  have hh : a.toLocalOrderedChord.hi < b.toLocalOrderedChord.hi ↔
      a.1.1.hi < b.1.1.hi := by
    unfold OptionalSignatureRegionalDiagonal.toLocalOrderedChord
    exact (optionalSignatureRegionVertexOrderLabels r).lt_iff_lt
  have ll' : b.toLocalOrderedChord.lo < a.toLocalOrderedChord.lo ↔
      b.1.1.lo < a.1.1.lo := by
    unfold OptionalSignatureRegionalDiagonal.toLocalOrderedChord
    exact (optionalSignatureRegionVertexOrderLabels r).lt_iff_lt
  have lh' : b.toLocalOrderedChord.lo < a.toLocalOrderedChord.hi ↔
      b.1.1.lo < a.1.1.hi := by
    unfold OptionalSignatureRegionalDiagonal.toLocalOrderedChord
    exact (optionalSignatureRegionVertexOrderLabels r).lt_iff_lt
  have hh' : b.toLocalOrderedChord.hi < a.toLocalOrderedChord.hi ↔
      b.1.1.hi < a.1.1.hi := by
    unfold OptionalSignatureRegionalDiagonal.toLocalOrderedChord
    exact (optionalSignatureRegionVertexOrderLabels r).lt_iff_lt
  unfold Crosses regionalDiagonalToStandard LocalOrderedChord.toDiagonal
  simp only [ll, lh, hh, ll', lh', hh']

/-- Regional channels are canonically equivalent to all standard diagonals of
the lower-point polygon. -/
noncomputable def regionalDiagonalStandardEquiv
    {n : ℕ} {D : Dissection n} {r : OptionalSignatureRegion D} :
    OptionalSignatureRegionalDiagonal r ≃
      Diagonal (optionalSignatureRegionArity r) where
  toFun := regionalDiagonalToStandard
  invFun := standardDiagonalToRegional r
  left_inv := standardDiagonalToRegional_regionalDiagonalToStandard
  right_inv := by
    intro d
    apply diagonal_eq_of_endpoints
    · exact congrArg LocalOrderedChord.lo
        (standardDiagonalToRegional_toLocalOrderedChord r d)
    · exact congrArg LocalOrderedChord.hi
        (standardDiagonalToRegional_toLocalOrderedChord r d)

/-- Local ordered channels actually realized by regional global diagonals. -/
def RealizedLocalOrderedChord {n : ℕ} {D : Dissection n}
    (r : OptionalSignatureRegion D) :=
  Set.range (@OptionalSignatureRegionalDiagonal.toLocalOrderedChord n D r)

/-- Exact channel-relabeling equivalence onto the realized local channels. -/
noncomputable def optionalSignatureRegionalChordEquiv {n : ℕ}
    {D : Dissection n} (r : OptionalSignatureRegion D) :
    OptionalSignatureRegionalDiagonal r ≃ RealizedLocalOrderedChord r :=
  Equiv.ofInjective
    (@OptionalSignatureRegionalDiagonal.toLocalOrderedChord n D r)
    OptionalSignatureRegionalDiagonal.toLocalOrderedChord_injective

noncomputable instance optionalSignatureRegionFintype {n : ℕ}
    (D : Dissection n) : Fintype (OptionalSignatureRegion D) := by
  classical
  exact Fintype.ofSurjective
    (fun d : OptionalDiagonal D =>
      (⟨canonicalCutSideSignature D d.1, ⟨d, rfl⟩⟩ :
        OptionalSignatureRegion D)) (by
      rintro ⟨s, d, hd⟩
      use d
      apply Subtype.ext
      exact hd)

noncomputable instance optionalSignatureRegionalDiagonalFintype {n : ℕ}
    {D : Dissection n} (r : OptionalSignatureRegion D) :
    Fintype (OptionalSignatureRegionalDiagonal r) :=
  Fintype.ofInjective
    (fun d : OptionalSignatureRegionalDiagonal r => d.1)
    Subtype.val_injective

/-- Canonical equivalence between optional diagonals and the disjoint union of
their occupied side-signature fibers. -/
noncomputable def optionalSignatureAddress {n : ℕ} (D : Dissection n) :
    OptionalDiagonal D ≃ Sigma (@OptionalSignatureRegionalDiagonal n D) where
  toFun d := ⟨⟨canonicalCutSideSignature D d.1, ⟨d, rfl⟩⟩, ⟨d, rfl⟩⟩
  invFun d := d.2.1
  left_inv _ := rfl
  right_inv := by
    rintro ⟨⟨s, hs⟩, ⟨d, hd⟩⟩
    cases hd
    rfl

/-- Crossing optional diagonals have the same complete side signature. -/
theorem optionalDiagonal_signature_eq_of_crosses {n : ℕ}
    {D : Dissection n} (a b : OptionalDiagonal D) (hab : Crosses a.1 b.1) :
    canonicalCutSideSignature D a.1 = canonicalCutSideSignature D b.1 := by
  funext c
  exact chordSide_eq_of_crosses_of_compatible c.1 a.1 b.1
    (a.2.2 c.1 c.2) (b.2.2 c.1 c.2) hab

/-- Diagonals in distinct occupied signature regions cannot cross. -/
theorem optionalSignature_crossRegionNoncrossing {n : ℕ}
    {D : Dissection n} (a b : OptionalDiagonal D) :
    (optionalSignatureAddress D a).1 ≠ (optionalSignatureAddress D b).1 →
      ¬ Crosses a.1 b.1 := by
  intro hregions hab
  apply hregions
  apply Subtype.ext
  exact optionalDiagonal_signature_eq_of_crosses a b hab

/-- Exact interface supplied by cutting a convex polygon along `D`. It records
regions, their internal diagonal types, the unique regional address of every
admissible diagonal, and the fact that diagonals in distinct regions cannot
cross. -/
structure RegionDecomposition {n : ℕ} (D : Dissection n) where
  Region : Type
  regionFintype : Fintype Region
  RegionalDiagonal : Region → Type
  regionalDiagonalFintype : ∀ r, Fintype (RegionalDiagonal r)
  address : OptionalDiagonal D ≃ Sigma RegionalDiagonal
  crossRegionNoncrossing : ∀ a b : OptionalDiagonal D,
    (address a).1 ≠ (address b).1 → ¬ Crosses a.1 b.1

/-- Canonical region decomposition obtained from occupied side signatures.
Regions with no optional diagonal are omitted; their triangulation factor is
the empty product, hence the multiplicative unit. -/
noncomputable abbrev canonicalRegionDecomposition {n : ℕ} (D : Dissection n) :
    RegionDecomposition D where
  Region := OptionalSignatureRegion D
  regionFintype := optionalSignatureRegionFintype D
  RegionalDiagonal := @OptionalSignatureRegionalDiagonal n D
  regionalDiagonalFintype := fun r =>
    optionalSignatureRegionalDiagonalFintype r
  address := optionalSignatureAddress D
  crossRegionNoncrossing := fun a b h =>
    optionalSignature_crossRegionNoncrossing a b h

@[simp] theorem canonicalRegionDecomposition_region {n : ℕ}
    (D : Dissection n) :
    (canonicalRegionDecomposition D).Region = OptionalSignatureRegion D := rfl

@[simp] theorem canonicalRegionDecomposition_regionalDiagonal {n : ℕ}
    (D : Dissection n) (r : OptionalSignatureRegion D) :
    (canonicalRegionDecomposition D).RegionalDiagonal r =
      OptionalSignatureRegionalDiagonal r := rfl

@[simp] theorem canonicalRegionDecomposition_address {n : ℕ}
    (D : Dissection n) :
    (canonicalRegionDecomposition D).address = optionalSignatureAddress D := rfl

noncomputable instance canonicalRegionDecompositionRegionalDiagonalFintype
    {n : ℕ} (D : Dissection n) (r : OptionalSignatureRegion D) :
    Fintype ((canonicalRegionDecomposition D).RegionalDiagonal r) :=
  optionalSignatureRegionalDiagonalFintype r

attribute [instance] RegionDecomposition.regionFintype
attribute [instance] RegionDecomposition.regionalDiagonalFintype

/-- Region containing an admissible diagonal. -/
def RegionDecomposition.regionOf {n : ℕ} {D : Dissection n}
    (regions : RegionDecomposition D) (d : OptionalDiagonal D) : regions.Region :=
  (regions.address d).1

/-- The regional address is unique because it is the image under an
 equivalence. -/
theorem RegionDecomposition.region_unique {n : ℕ} {D : Dissection n}
    (regions : RegionDecomposition D) (d : OptionalDiagonal D)
    (r : regions.Region) (h : r = regions.regionOf d) :
    r = (regions.address d).1 := h

/-- Diagonals assigned to different regions are automatically compatible. -/
theorem RegionDecomposition.not_crosses_of_region_ne {n : ℕ}
    {D : Dissection n} (regions : RegionDecomposition D)
    (a b : OptionalDiagonal D)
    (h : regions.regionOf a ≠ regions.regionOf b) : ¬ Crosses a.1 b.1 :=
  regions.crossRegionNoncrossing a b h

/-- Pairwise noncrossing for a set of admissible optional diagonals. Requiring
all pairs is equivalent to the usual distinct-pair formulation because crossing
is irreflexive. -/
def OptionalFamilyNoncrossing {n : ℕ} {D : Dissection n}
    (S : Set (OptionalDiagonal D)) : Prop :=
  ∀ a ∈ S, ∀ b ∈ S, ¬ Crosses a.1 b.1

/-- Componentwise noncrossing: only pairs carrying the same region label need
to be tested. -/
def ComponentwiseNoncrossing {n : ℕ} {D : Dissection n}
    (regions : RegionDecomposition D) (S : Set (OptionalDiagonal D)) : Prop :=
  ∀ a ∈ S, ∀ b ∈ S, regions.regionOf a = regions.regionOf b →
    ¬ Crosses a.1 b.1

/-- Global noncrossing is exactly componentwise noncrossing, because the region
decomposition already excludes crossings between distinct regions. -/
theorem optionalFamilyNoncrossing_iff_componentwise {n : ℕ}
    {D : Dissection n} (regions : RegionDecomposition D)
    (S : Set (OptionalDiagonal D)) :
    OptionalFamilyNoncrossing S ↔ ComponentwiseNoncrossing regions S := by
  constructor
  · intro h a ha b hb _
    exact h a ha b hb
  · intro h a ha b hb
    by_cases hab : regions.regionOf a = regions.regionOf b
    · exact h a ha b hb hab
    · exact regions.not_crosses_of_region_ne a b hab

/-- Restrict a global optional-diagonal set to every regional fiber. -/
def regionSetsEquiv {n : ℕ} {D : Dissection n}
    (regions : RegionDecomposition D) :
    Set (OptionalDiagonal D) ≃
      ((r : regions.Region) → Set (regions.RegionalDiagonal r)) where
  toFun S r := {x | regions.address.symm ⟨r, x⟩ ∈ S}
  invFun A := {d | (regions.address d).2 ∈ A (regions.address d).1}
  left_inv S := by
    ext d
    change regions.address.symm (regions.address d) ∈ S ↔ d ∈ S
    simp
  right_inv A := by
    funext r
    ext x
    change (regions.address (regions.address.symm ⟨r, x⟩)).2 ∈
      A (regions.address (regions.address.symm ⟨r, x⟩)).1 ↔ x ∈ A r
    rw [regions.address.apply_symm_apply]

/-- Regional restriction preserves and reflects inclusion, so it is an order
isomorphism before imposing noncrossing and maximality. -/
def regionSetsOrderIso {n : ℕ} {D : Dissection n}
    (regions : RegionDecomposition D) :
    Set (OptionalDiagonal D) ≃o
      ((r : regions.Region) → Set (regions.RegionalDiagonal r)) where
  toEquiv := regionSetsEquiv regions
  map_rel_iff' := by
    intro S T
    constructor
    · intro h d hd
      have hs : regions.address.symm (regions.address d) ∈ S := by
        simpa using hd
      have ht := h (regions.address d).1 hs
      change regions.address.symm (regions.address d) ∈ T at ht
      simpa using ht
    · intro h r x hx
      change regions.address.symm ⟨r, x⟩ ∈ T
      apply h
      exact hx

/-- Noncrossing imposed independently in every regional fiber. -/
def RegionalFamiliesNoncrossing {n : ℕ} {D : Dissection n}
    (regions : RegionDecomposition D)
    (A : (r : regions.Region) → Set (regions.RegionalDiagonal r)) : Prop :=
  ∀ r, ∀ x ∈ A r, ∀ y ∈ A r,
    ¬ Crosses (regions.address.symm ⟨r, x⟩).1
      (regions.address.symm ⟨r, y⟩).1

/-- Regional restriction preserves and reflects noncrossing. -/
theorem regionSetsEquiv_noncrossing {n : ℕ} {D : Dissection n}
    (regions : RegionDecomposition D) (S : Set (OptionalDiagonal D)) :
    OptionalFamilyNoncrossing S ↔
      RegionalFamiliesNoncrossing regions (regionSetsEquiv regions S) := by
  constructor
  · intro h r x hx y hy
    exact h (regions.address.symm ⟨r, x⟩) hx
      (regions.address.symm ⟨r, y⟩) hy
  · intro h
    apply (optionalFamilyNoncrossing_iff_componentwise regions S).mpr
    intro a ha b hb hab
    rcases ha' : regions.address a with ⟨ra, xa⟩
    rcases hb' : regions.address b with ⟨rb, xb⟩
    have hr : ra = rb := by
      simpa [RegionDecomposition.regionOf, ha', hb'] using hab
    subst rb
    have hxa : regions.address.symm ⟨ra, xa⟩ ∈ S := by
      rw [← ha']
      simpa using ha
    have hxb : regions.address.symm ⟨ra, xb⟩ ∈ S := by
      rw [← hb']
      simpa using hb
    have haa : regions.address.symm ⟨ra, xa⟩ = a := by
      rw [← ha']
      simp
    have hbb : regions.address.symm ⟨ra, xb⟩ = b := by
      rw [← hb']
      simp
    simpa [haa, hbb] using h ra xa hxa xb hxb

/-- Global noncrossing families of admissible refinement diagonals. -/
def OptionalDissectionFamily {n : ℕ} {D : Dissection n} :=
  {S : Set (OptionalDiagonal D) // OptionalFamilyNoncrossing S}

/-- The refinement face above a fixed dissection. -/
def RefinementFace {n : ℕ} (D : Dissection n) :=
  {E : Dissection n // D ≤ E}

/-- Every refinement determines the family of its added admissible diagonals. -/
def faceToOptionalFamily {n : ℕ} (D : Dissection n) :
    RefinementFace D → OptionalDissectionFamily (D := D) := fun E =>
  ⟨{d | d.1 ∈ E.1.1}, by
    intro a ha b hb
    by_cases hab : a.1 = b.1
    · intro hcross
      rw [hab] at hcross
      rcases hcross with h | h
      · exact lt_irrefl _ h.1
      · exact lt_irrefl _ h.1
    · exact E.1.2 ha hb hab⟩

/-- The finite underlying diagonal set of an optional family. -/
noncomputable def optionalFamilyFinset {n : ℕ} {D : Dissection n}
    (S : OptionalDissectionFamily (D := D))
    [DecidablePred (fun d => d ∈ S.1)] : Finset (Diagonal n) :=
  (Finset.univ.filter (fun d => d ∈ S.1)).map
    ⟨Subtype.val, Subtype.val_injective⟩

@[simp] theorem mem_optionalFamilyFinset {n : ℕ} {D : Dissection n}
    (S : OptionalDissectionFamily (D := D))
    [decS : DecidablePred (fun d => d ∈ S.1)] (d : Diagonal n) :
    d ∈ optionalFamilyFinset S ↔ ∃ x : OptionalDiagonal D, x ∈ S.1 ∧ x.1 = d := by
  constructor
  · intro hd
    rw [optionalFamilyFinset] at hd
    rcases Finset.mem_map.mp hd with ⟨x, hx, hxd⟩
    exact ⟨x, (Finset.mem_filter (p := fun d => d ∈ S.1)).mp hx |>.2, hxd⟩
  · rintro ⟨x, hx, hxd⟩
    rw [optionalFamilyFinset]
    apply Finset.mem_map.mpr
    exact ⟨x, (Finset.mem_filter (p := fun d => d ∈ S.1)).mpr
      ⟨Finset.mem_univ x, hx⟩, hxd⟩

/-- Adjoin a noncrossing optional family to the fixed cuts. -/
noncomputable def optionalFamilyToFace {n : ℕ} (D : Dissection n) :
    OptionalDissectionFamily (D := D) → RefinementFace D := by
  classical
  exact fun S =>
  ⟨⟨D.1 ∪ optionalFamilyFinset S, by
      intro a ha b hb hab
      rw [Finset.mem_union] at ha hb
      rcases ha with haD | haS <;> rcases hb with hbD | hbS
      · exact D.2 haD hbD hab
      · rcases (mem_optionalFamilyFinset S b).mp hbS with ⟨bo, hbo, rfl⟩
        intro hcross
        exact bo.2.2 a haD ((crosses_symmetric).mp hcross)
      · rcases (mem_optionalFamilyFinset S a).mp haS with ⟨ao, hao, rfl⟩
        exact ao.2.2 b hbD
      · rcases (mem_optionalFamilyFinset S a).mp haS with ⟨ao, hao, rfl⟩
        rcases (mem_optionalFamilyFinset S b).mp hbS with ⟨bo, hbo, rfl⟩
        exact S.2 ao hao bo hbo⟩,
    by
      intro d hd
      exact Finset.mem_union_left _ hd⟩

/-- Refinements above `D` are exactly the noncrossing families of admissible
new diagonals. -/
noncomputable def refinementFaceEquivOptionalFamilies {n : ℕ} (D : Dissection n) :
    RefinementFace D ≃ OptionalDissectionFamily (D := D) where
  toFun := faceToOptionalFamily D
  invFun := optionalFamilyToFace D
  left_inv E := by
    classical
    apply Subtype.ext
    apply Subtype.ext
    ext d
    change d ∈ D.1 ∪ optionalFamilyFinset (faceToOptionalFamily D E) ↔ d ∈ E.1.1
    constructor
    · intro hd
      rcases Finset.mem_union.mp hd with hdD | hdS
      · exact E.2 hdD
      · rcases (mem_optionalFamilyFinset (faceToOptionalFamily D E) d).mp hdS with
          ⟨x, hx, hxd⟩
        change x.1 ∈ E.1.1 at hx
        rw [← hxd]
        exact hx
    · intro hd
      by_cases hdD : d ∈ D.1
      · exact Finset.mem_union_left _ hdD
      · apply Finset.mem_union_right
        apply (mem_optionalFamilyFinset (faceToOptionalFamily D E) d).mpr
        let x : OptionalDiagonal D := ⟨d, hdD, by
          intro c hc
          by_cases hcd : c = d
          · subst c
            intro hcross
            rcases hcross with h | h
            · exact lt_irrefl _ h.1
            · exact lt_irrefl _ h.1
          · intro hcross
            exact E.1.2 (E.2 hc) hd hcd ((crosses_symmetric).mp hcross)⟩
        exact ⟨x, hd, rfl⟩
  right_inv S := by
    classical
    apply Subtype.ext
    ext x
    change x.1 ∈ (optionalFamilyToFace D S).1.1 ↔ x ∈ S.1
    rw [show (optionalFamilyToFace D S).1.1 = D.1 ∪ optionalFamilyFinset S from rfl,
      Finset.mem_union]
    constructor
    · rintro (hxD | hxS)
      · exact False.elim (x.2.1 hxD)
      · rcases (mem_optionalFamilyFinset S x.1).mp hxS with ⟨y, hy, hyx⟩
        simpa [Subtype.ext hyx] using hy
    · intro hx
      right
      exact (mem_optionalFamilyFinset S x.1).mpr ⟨x, hx, rfl⟩

/-- Tuples of noncrossing families, one in each regional fiber. -/
def RegionalDissectionFamilies {n : ℕ} {D : Dissection n}
    (regions : RegionDecomposition D) :=
  {A : (r : regions.Region) → Set (regions.RegionalDiagonal r) //
    RegionalFamiliesNoncrossing regions A}

/-- The regional set equivalence restricts to an equivalence of actual
noncrossing families. -/
def regionDissectionFamiliesEquiv {n : ℕ} {D : Dissection n}
    (regions : RegionDecomposition D) :
    OptionalDissectionFamily (D := D) ≃ RegionalDissectionFamilies regions where
  toFun S := ⟨regionSetsEquiv regions S.1,
    (regionSetsEquiv_noncrossing regions S.1).mp S.2⟩
  invFun A := ⟨(regionSetsEquiv regions).symm A.1,
    (regionSetsEquiv_noncrossing regions ((regionSetsEquiv regions).symm A.1)).mpr
      (by simpa using A.2)⟩
  left_inv S := by
    apply Subtype.ext
    exact (regionSetsEquiv regions).symm_apply_apply S.1
  right_inv A := by
    apply Subtype.ext
    exact (regionSetsEquiv regions).apply_symm_apply A.1

instance optionalDissectionFamilyLE {n : ℕ} {D : Dissection n} :
    LE (OptionalDissectionFamily (D := D)) :=
  ⟨fun S T => S.1 ⊆ T.1⟩

instance regionalDissectionFamiliesLE {n : ℕ} {D : Dissection n}
    (regions : RegionDecomposition D) : LE (RegionalDissectionFamilies regions) :=
  ⟨fun A B => ∀ r, A.1 r ⊆ B.1 r⟩

/-- Maximality in an arbitrary refinement relation. -/
def IsOrderMaximal {α : Type*} [LE α] (x : α) : Prop :=
  ∀ y, x ≤ y → y ≤ x

/-- An order-compatible equivalence restricts to maximal elements. -/
def maximalElementsEquiv {α β : Type*} [LE α] [LE β]
    (e : α ≃ β) (map_rel_iff : ∀ x y, x ≤ y ↔ e x ≤ e y) :
    {x : α // IsOrderMaximal x} ≃ {y : β // IsOrderMaximal y} where
  toFun x := ⟨e x.1, by
    intro y hy
    let z := e.symm y
    have hxz : x.1 ≤ z := (map_rel_iff x.1 z).mpr (by simpa [z] using hy)
    have hzx := x.2 z hxz
    calc
      y = e z := (e.apply_symm_apply y).symm
      _ ≤ e x.1 := (map_rel_iff z x.1).mp hzx⟩
  invFun y := ⟨e.symm y.1, by
    intro x hx
    have hyex : y.1 ≤ e x := by
      simpa using (map_rel_iff (e.symm y.1) x).mp hx
    have hexy : e x ≤ y.1 := y.2 (e x) hyex
    exact (map_rel_iff x (e.symm y.1)).mpr (by simpa using hexy)⟩
  left_inv x := by
    apply Subtype.ext
    simp
  right_inv y := by
    apply Subtype.ext
    simp

/-- Regional restriction identifies maximal global noncrossing families with
maximal tuples of regional noncrossing families. -/
def maximalRegionDissectionFamiliesEquiv {n : ℕ} {D : Dissection n}
    (regions : RegionDecomposition D) :
    {S : OptionalDissectionFamily (D := D) // IsOrderMaximal S} ≃
      {A : RegionalDissectionFamilies regions // IsOrderMaximal A} :=
  maximalElementsEquiv (regionDissectionFamiliesEquiv regions) (by
    intro S T
    change S.1 ⊆ T.1 ↔
      regionSetsEquiv regions S.1 ≤ regionSetsEquiv regions T.1
    exact ((regionSetsOrderIso regions).le_iff_le).symm)

instance refinementFaceLE {n : ℕ} {D : Dissection n} : LE (RefinementFace D) :=
  ⟨fun E F => E.1 ≤ F.1⟩

/-- The refinement/optional-family equivalence preserves and reflects the
refinement order. -/
theorem refinementFaceEquivOptionalFamilies_le_iff {n : ℕ} (D : Dissection n)
    (E F : RefinementFace D) :
    E ≤ F ↔ refinementFaceEquivOptionalFamilies D E ≤
      refinementFaceEquivOptionalFamilies D F := by
  constructor
  · intro h x hx
    exact h hx
  · intro h d hd
    by_cases hdD : d ∈ D.1
    · exact F.2 hdD
    · let x : OptionalDiagonal D := ⟨d, hdD, by
        intro c hc
        by_cases hcd : c = d
        · subst c
          intro hcross
          rcases hcross with hcross | hcross
          · exact lt_irrefl _ hcross.1
          · exact lt_irrefl _ hcross.1
        · intro hcross
          exact E.1.2 (E.2 hc) hd hcd ((crosses_symmetric).mp hcross)⟩
      have hx : x ∈ (refinementFaceEquivOptionalFamilies D E).1 := hd
      exact h hx

/-- Maximal refinements correspond to maximal admissible optional families. -/
noncomputable def maximalRefinementOptionalFamiliesEquiv {n : ℕ} (D : Dissection n) :
    {E : RefinementFace D // IsOrderMaximal E} ≃
      {S : OptionalDissectionFamily (D := D) // IsOrderMaximal S} :=
  maximalElementsEquiv (refinementFaceEquivOptionalFamilies D)
    (refinementFaceEquivOptionalFamilies_le_iff D)

/-- Any finite region-label function produces the unique-address part of a
region decomposition. The sole geometric obligation is that differently
labelled admissible diagonals do not cross. -/
noncomputable def RegionDecomposition.ofLabel {n : ℕ} {D : Dissection n}
    (Region : Type) [Fintype Region]
    (label : OptionalDiagonal D → Region)
    (separated : ∀ a b : OptionalDiagonal D,
      label a ≠ label b → ¬ Crosses a.1 b.1) : RegionDecomposition D where
  Region := Region
  regionFintype := inferInstance
  RegionalDiagonal := fun r => {d : OptionalDiagonal D // label d = r}
  regionalDiagonalFintype := fun _ => Fintype.ofInjective Subtype.val Subtype.val_injective
  address :=
    { toFun := fun d => ⟨label d, ⟨d, rfl⟩⟩
      invFun := fun z => z.2.1
      left_inv := fun _ => rfl
      right_inv := by
        rintro ⟨r, d, hd⟩
        cases hd
        rfl }
  crossRegionNoncrossing := by
    intro a b h
    exact separated a b h

/-- No diagonal crosses itself. -/
theorem crosses_irrefl {n : ℕ} (a : Diagonal n) : ¬ Crosses a a := by
  intro h
  rcases h with h | h
  · exact (lt_irrefl _ h.1)
  · exact (lt_irrefl _ h.1)

/-- The crossing graph of admissible diagonals above `D`. Its connected
components are the nontrivial interaction regions; triangular polygon cells
carry no diagonal and therefore contribute unit factors. -/
def crossingGraph {n : ℕ} (D : Dissection n) :
    SimpleGraph (OptionalDiagonal D) where
  Adj a b := Crosses a.1 b.1
  symm := ⟨fun ⦃a b : OptionalDiagonal D⦄ h =>
    (crosses_symmetric (a := a.1) (b := b.1)).mp h⟩
  loopless := ⟨fun ⦃a : OptionalDiagonal D⦄ => crosses_irrefl a.1⟩

/-- Canonical region decomposition by connected components of the crossing
graph. Any crossing edge lies inside one component, so distinct components are
independent automatically. -/
noncomputable def interactionRegionDecomposition {n : ℕ} (D : Dissection n) :
    RegionDecomposition D := by
  let G := crossingGraph D
  letI : Fintype G.ConnectedComponent := Fintype.ofFinite G.ConnectedComponent
  exact RegionDecomposition.ofLabel G.ConnectedComponent
    G.connectedComponentMk (by
      intro a b hne hab
      apply hne
      exact SimpleGraph.ConnectedComponent.connectedComponentMk_eq_of_adj hab)

/-- Before any cut there is one region, and every polygon diagonal is assigned
to it. This is the base case for recursive cutting. -/
noncomputable def emptyRegionDecomposition (n : ℕ) :
    RegionDecomposition (empty n) where
  Region := PUnit
  regionFintype := inferInstance
  RegionalDiagonal := fun _ => OptionalDiagonal (empty n)
  regionalDiagonalFintype := fun _ => inferInstance
  address :=
    { toFun := fun d => ⟨PUnit.unit, d⟩
      invFun := fun z => z.2
      left_inv := fun _ => rfl
      right_inv := by
        rintro ⟨r, d⟩
        cases r
        rfl }
  crossRegionNoncrossing := by
    intro a b h
    exact False.elim (h rfl)

/-- Every genuinely added diagonal in a refinement is admissible above the
selected cuts. -/
theorem refinement_new_diagonal_compatible {n : ℕ} {D E : Dissection n}
    (hDE : D ≤ E) {d : Diagonal n} (hdE : d ∈ E.1) (hdD : d ∉ D.1) :
    CompatibleWith D d := by
  intro c hcD
  apply E.2 hdE (hDE hcD)
  intro hdc
  apply hdD
  simpa [hdc] using hcD

/-- Inserting a new diagonal preserves noncrossing exactly when that diagonal
crosses none of the existing cuts. -/
theorem insert_isDissection_iff {n : ℕ} (D : Dissection n)
    (d : Diagonal n) (hd : d ∉ D.1) :
    IsDissection (insert d D.1) ↔ CompatibleWith D d := by
  constructor
  · intro h c hc
    apply h (Finset.mem_insert_self d D.1) (Finset.mem_insert_of_mem hc)
    intro hdc
    apply hd
    simpa [hdc] using hc
  · intro h a ha b hb hab
    rw [Finset.mem_insert] at ha hb
    rcases ha with rfl | ha <;> rcases hb with rfl | hb
    · exact False.elim (hab rfl)
    · exact h b hb
    · intro hcross
      exact h a ha ((crosses_symmetric).mpr hcross)
    · exact D.2 ha hb hab

/-- A triangulation is a maximal dissection in the refinement order. This
order-theoretic definition avoids choosing a cardinality theorem prematurely. -/
def IsTriangulation {n : ℕ} (T : Dissection n) : Prop :=
  ∀ E : Dissection n, T ≤ E → E ≤ T

/-- Maximality is equivalent to saturation: every missing diagonal crosses an
existing diagonal and therefore cannot be inserted. -/
theorem isTriangulation_iff_no_compatible_missing {n : ℕ} (T : Dissection n) :
    IsTriangulation T ↔
      ∀ d : Diagonal n, d ∉ T.1 → ¬ CompatibleWith T d := by
  constructor
  · intro hmax d hdT hcompat
    let E : Dissection n :=
      ⟨insert d T.1, (insert_isDissection_iff T d hdT).mpr hcompat⟩
    have hTE : T ≤ E := by
      intro c hc
      exact Finset.mem_insert_of_mem hc
    have hET : E ≤ T := hmax E hTE
    exact hdT (hET (Finset.mem_insert_self d T.1))
  · intro hsaturated E hTE d hdE
    by_contra hdT
    exact hsaturated d hdT
      (refinement_new_diagonal_compatible hTE hdE hdT)

/-- Generic triangulations of the convex `n`-gon. -/
def Triangulation (n : ℕ) := {T : Dissection n // IsTriangulation T}

/-- Terms that remain after taking a residue along `D`: maximal dissections
that refine all cuts in `D`. -/
def RefiningTriangulation {n : ℕ} (D : Dissection n) :=
  {T : Triangulation n // D ≤ T.1}

noncomputable instance triangulationFintype (n : ℕ) : Fintype (Triangulation n) :=
  Fintype.ofInjective Subtype.val Subtype.val_injective

noncomputable instance refiningTriangulationFintype {n : ℕ} (D : Dissection n) :
    Fintype (RefiningTriangulation D) :=
  Fintype.ofInjective Subtype.val Subtype.val_injective

/-- A triangulation refining `D` is equivalently a maximal element of the face
above `D`. -/
theorem refiningTriangulation_maximal_in_face {n : ℕ} (D : Dissection n)
    (T : RefiningTriangulation D) (E : Dissection n)
    (hTE : T.1.1 ≤ E) : E = T.1.1 := by
  exact le_antisymm (T.1.2 E hTE) hTE

/-- Maximal elements of the refinement face are precisely triangulations
containing `D`. -/
def maximalRefinementFaceEquivRefiningTriangulation {n : ℕ} (D : Dissection n) :
    {E : RefinementFace D // IsOrderMaximal E} ≃ RefiningTriangulation D where
  toFun E := ⟨⟨E.1.1, by
    intro F hEF
    exact E.2 ⟨F, le_trans E.1.2 hEF⟩ hEF⟩, E.1.2⟩
  invFun T := ⟨⟨T.1.1, T.2⟩, by
    intro E hTE
    exact T.1.2 E.1 hTE⟩
  left_inv E := by
    apply Subtype.ext
    apply Subtype.ext
    rfl
  right_inv T := by
    apply Subtype.ext
    apply Subtype.ext
    rfl

/-- The canonical indexing equivalence used by regional amplitude
factorization: a refining triangulation is a tuple of maximal regional
noncrossing families. -/
noncomputable def refiningTriangulationsEquivMaximalRegionalFamilies {n : ℕ}
    (D : Dissection n) (regions : RegionDecomposition D) :
    RefiningTriangulation D ≃
      {A : RegionalDissectionFamilies regions // IsOrderMaximal A} :=
  (maximalRefinementFaceEquivRefiningTriangulation D).symm |>.trans
    ((maximalRefinementOptionalFamiliesEquiv D).trans
      (maximalRegionDissectionFamiliesEquiv regions))

open scoped BigOperators

/-- Product of supplied inverse-channel weights over a dissection. -/
def monomialWeight {n : ℕ} {R : Type*} [CommMonoid R]
    (inverseChannelWeight : Diagonal n → R) (T : Dissection n) : R :=
  ∏ d ∈ T.1, inverseChannelWeight d

/-- Removing the selected cuts from a refining triangulation leaves another
noncrossing dissection. -/
def residualDissection {n : ℕ} (D : Dissection n)
    (T : RefiningTriangulation D) : Dissection n :=
  ⟨T.1.1.1 \ D.1,
    isDissection_subset T.1.1.2 (by
      intro d hd
      exact (Finset.mem_sdiff.mp hd).1)⟩

/-- Residual monomial after extracting all channel weights belonging to `D`. -/
def residualWeight {n : ℕ} {R : Type*} [CommMonoid R]
    (inverseChannelWeight : Diagonal n → R) (D : Dissection n)
    (T : RefiningTriangulation D) : R :=
  ∏ d ∈ T.1.1.1 \ D.1, inverseChannelWeight d

/-- Removing `D` from a refining triangulation gives exactly the finite
support of its associated optional family. -/
theorem residualFinset_eq_optionalFamilyFinset {n : ℕ} (D : Dissection n)
    (T : RefiningTriangulation D)
    [DecidablePred (fun d => d ∈
      (faceToOptionalFamily D ⟨T.1.1, T.2⟩).1)] :
    T.1.1.1 \ D.1 = optionalFamilyFinset
      (faceToOptionalFamily D ⟨T.1.1, T.2⟩) := by
  classical
  ext d
  rw [Finset.mem_sdiff, mem_optionalFamilyFinset]
  constructor
  · rintro ⟨hdT, hdD⟩
    let x : OptionalDiagonal D := ⟨d, hdD, by
      intro c hc
      by_cases hcd : c = d
      · subst c
        intro hcross
        rcases hcross with hcross | hcross
        · exact lt_irrefl _ hcross.1
        · exact lt_irrefl _ hcross.1
      · intro hcross
        exact T.1.1.2 (T.2 hc) hdT hcd ((crosses_symmetric).mp hcross)⟩
    exact ⟨x, hdT, rfl⟩
  · rintro ⟨x, hx, hxd⟩
    change x.1 ∈ T.1.1.1 at hx
    rw [← hxd]
    exact ⟨hx, x.2.1⟩

/-- Residual weight is the product over the optional family obtained by
removing the selected dissection. -/
theorem residualWeight_eq_optionalFamilyWeight {n : ℕ} {R : Type*}
    [CommMonoid R] (inverseChannelWeight : Diagonal n → R) (D : Dissection n)
    (T : RefiningTriangulation D)
    [DecidablePred (fun d => d ∈
      (faceToOptionalFamily D ⟨T.1.1, T.2⟩).1)] :
    residualWeight inverseChannelWeight D T =
      ∏ d ∈ optionalFamilyFinset
        (faceToOptionalFamily D ⟨T.1.1, T.2⟩), inverseChannelWeight d := by
  unfold residualWeight
  rw [residualFinset_eq_optionalFamilyFinset D T]

/-- Residual weight is the ordinary monomial weight of the residual
noncrossing dissection. -/
theorem residualWeight_eq_monomialWeight {n : ℕ} {R : Type*} [CommMonoid R]
    (inverseChannelWeight : Diagonal n → R) (D : Dissection n)
    (T : RefiningTriangulation D) :
    residualWeight inverseChannelWeight D T =
      monomialWeight inverseChannelWeight (residualDissection D T) := rfl

/-- A term refining `D` splits exactly into the cut monomial and its residual
monomial. This is coefficient extraction at the level of one planar term. -/
theorem monomialWeight_split {n : ℕ} {R : Type*} [CommMonoid R]
    (inverseChannelWeight : Diagonal n → R) (D : Dissection n)
    (T : RefiningTriangulation D) :
    monomialWeight inverseChannelWeight T.1.1 =
      monomialWeight inverseChannelWeight D * residualWeight inverseChannelWeight D T := by
  simpa [monomialWeight, residualWeight, mul_comm] using
    (Finset.prod_sdiff T.2 (f := inverseChannelWeight)).symm

/-- Full planar amplitude: the finite sum over all maximal dissections. -/
noncomputable def planarAmplitude {n : ℕ} {R : Type*} [CommSemiring R]
    (inverseChannelWeight : Diagonal n → R) : R :=
  ∑ T : Triangulation n, monomialWeight inverseChannelWeight T.1

/-- Coefficient residue along `D`, after removing the channel weights in `D`. -/
noncomputable def residueAmplitude {n : ℕ} {R : Type*} [CommSemiring R]
    (inverseChannelWeight : Diagonal n → R) (D : Dissection n) : R :=
  ∑ T : RefiningTriangulation D, residualWeight inverseChannelWeight D T

/-- The portion of the amplitude supported on triangulations containing `D`. -/
noncomputable def supportedAmplitude {n : ℕ} {R : Type*} [CommSemiring R]
    (inverseChannelWeight : Diagonal n → R) (D : Dissection n) : R :=
  ∑ T : RefiningTriangulation D, monomialWeight inverseChannelWeight T.1.1

/-- Extracting the common cut-channel weights from every supported planar term
leaves exactly the coefficient residue. -/
theorem supportedAmplitude_factor {n : ℕ} {R : Type*} [CommSemiring R]
    (inverseChannelWeight : Diagonal n → R) (D : Dissection n) :
    supportedAmplitude inverseChannelWeight D =
      monomialWeight inverseChannelWeight D * residueAmplitude inverseChannelWeight D := by
  unfold supportedAmplitude residueAmplitude
  simp_rw [monomialWeight_split inverseChannelWeight D]
  exact (Finset.mul_sum _ _ _).symm

/-- A noncrossing family internal to one regional fiber. -/
def RegionalFamily {n : ℕ} {D : Dissection n}
    (regions : RegionDecomposition D) (r : regions.Region) :=
  {S : Set (regions.RegionalDiagonal r) //
    ∀ x ∈ S, ∀ y ∈ S,
      ¬ Crosses (regions.address.symm ⟨r, x⟩).1
        (regions.address.symm ⟨r, y⟩).1}

/-- Relabel a regional noncrossing family as a standard lower-point
dissection. -/
noncomputable def regionalFamilyToStandardDissection
    {n : ℕ} {D : Dissection n} {r : OptionalSignatureRegion D}
    (S : RegionalFamily (canonicalRegionDecomposition D) r) :
    Dissection (optionalSignatureRegionArity r) := by
  classical
  let e := regionalDiagonalStandardEquiv (r := r)
  refine ⟨Finset.univ.filter (fun d => e.symm d ∈ S.1), ?_⟩
  intro a ha b hb hab
  simp only [Finset.mem_filter, Finset.mem_univ, true_and] at ha hb
  have hnc := S.2 (e.symm a) ha (e.symm b) hb
  intro hcross
  apply hnc
  apply (regionalDiagonalToStandard_crosses_iff (e.symm a) (e.symm b)).mp
  have haeq : regionalDiagonalToStandard (e.symm a) = a :=
    e.apply_symm_apply a
  have hbeq : regionalDiagonalToStandard (e.symm b) = b :=
    e.apply_symm_apply b
  rw [haeq, hbeq]
  exact hcross

/-- Pull a standard lower-point dissection back to a regional noncrossing
family. -/
noncomputable def standardDissectionToRegionalFamily
    {n : ℕ} {D : Dissection n} {r : OptionalSignatureRegion D}
    (T : Dissection (optionalSignatureRegionArity r)) :
    RegionalFamily (canonicalRegionDecomposition D) r := by
  let e := regionalDiagonalStandardEquiv (r := r)
  refine ⟨{x | e x ∈ T.1}, ?_⟩
  intro x hx y hy
  by_cases hxy : x = y
  · subst y
    unfold Crosses
    omega
  · have hnc := T.2 hx hy (fun he => hxy (e.injective he))
    intro hcross
    apply hnc
    exact (regionalDiagonalToStandard_crosses_iff x y).mpr hcross

instance regionalFamilyLE {n : ℕ} {D : Dissection n}
    (regions : RegionDecomposition D) (r : regions.Region) :
    LE (RegionalFamily regions r) :=
  ⟨fun S T => S.1 ⊆ T.1⟩

/-- Regional noncrossing families are equivalent to standard lower-point
dissections. -/
noncomputable def regionalFamilyStandardDissectionEquiv
    {n : ℕ} {D : Dissection n} {r : OptionalSignatureRegion D} :
    RegionalFamily (canonicalRegionDecomposition D) r ≃
      Dissection (optionalSignatureRegionArity r) where
  toFun := regionalFamilyToStandardDissection
  invFun := standardDissectionToRegionalFamily
  left_inv := by
    intro S
    apply Subtype.ext
    ext x
    simp [regionalFamilyToStandardDissection,
      standardDissectionToRegionalFamily]
  right_inv := by
    intro T
    apply Subtype.ext
    ext d
    simp [regionalFamilyToStandardDissection,
      standardDissectionToRegionalFamily]

/-- The family equivalence preserves and reflects inclusion. -/
noncomputable def regionalFamilyStandardDissectionOrderIso
    {n : ℕ} {D : Dissection n} {r : OptionalSignatureRegion D} :
    RegionalFamily (canonicalRegionDecomposition D) r ≃o
      Dissection (optionalSignatureRegionArity r) where
  toEquiv := regionalFamilyStandardDissectionEquiv
  map_rel_iff' := by
    intro S T
    change (regionalFamilyToStandardDissection S).1 ⊆
        (regionalFamilyToStandardDissection T).1 ↔ S.1 ⊆ T.1
    constructor
    · intro hST x hx
      have hm : (regionalDiagonalStandardEquiv x) ∈
          (regionalFamilyToStandardDissection S).1 := by
        simp [regionalFamilyToStandardDissection, hx]
      have hm' := hST hm
      simpa [regionalFamilyToStandardDissection] using hm'
    · intro hST d hd
      simp only [regionalFamilyToStandardDissection, Finset.mem_filter,
        Finset.mem_univ, true_and] at hd ⊢
      exact hST hd

/-- Any order isomorphism transports order-maximal elements. -/
noncomputable def orderIsoMaximalEquiv
    {α β : Type*} [LE α] [LE β] (e : α ≃o β) :
    {a : α // IsOrderMaximal a} ≃ {b : β // IsOrderMaximal b} where
  toFun a := ⟨e a.1, by
    intro y hey
    have hsource : a.1 ≤ e.symm y := by
      apply e.le_iff_le.mp
      simpa using hey
    have hback := a.2 (e.symm y) hsource
    have himage := e.le_iff_le.mpr hback
    simpa using himage⟩
  invFun b := ⟨e.symm b.1, by
    intro x hex
    have himage : b.1 ≤ e x := by
      have := e.le_iff_le.mpr hex
      simpa using this
    have hback := b.2 (e x) himage
    apply e.le_iff_le.mp
    simpa using hback⟩
  left_inv a := by
    apply Subtype.ext
    exact e.symm_apply_apply a.1
  right_inv b := by
    apply Subtype.ext
    exact e.apply_symm_apply b.1

noncomputable instance regionalFamilyFintype {n : ℕ} {D : Dissection n}
    (regions : RegionDecomposition D) (r : regions.Region) :
    Fintype (RegionalFamily regions r) := by
  classical
  apply Fintype.ofInjective
    (fun S : RegionalFamily regions r =>
      Finset.univ.filter (fun x => x ∈ S.1))
  intro S T h
  apply Subtype.ext
  ext x
  have hx := Finset.ext_iff.mp h x
  simpa using hx

/-- A regional triangulation is a maximal noncrossing family in that fiber. -/
def RegionalTriangulation {n : ℕ} {D : Dissection n}
    (regions : RegionDecomposition D) (r : regions.Region) :=
  {S : RegionalFamily regions r // IsOrderMaximal S}

/-- Maximal regional noncrossing families are exactly standard lower-point
triangulations. -/
noncomputable def regionalTriangulationStandardEquiv
    {n : ℕ} {D : Dissection n} {r : OptionalSignatureRegion D} :
    RegionalTriangulation (canonicalRegionDecomposition D) r ≃
      Triangulation (optionalSignatureRegionArity r) :=
  orderIsoMaximalEquiv regionalFamilyStandardDissectionOrderIso

/-- Membership in a transported triangulation is exactly membership of the
inverse-relabeled regional channel. -/
theorem mem_regionalTriangulationStandardEquiv
    {n : ℕ} {D : Dissection n} {r : OptionalSignatureRegion D}
    (T : RegionalTriangulation (canonicalRegionDecomposition D) r)
    (d : Diagonal (optionalSignatureRegionArity r)) :
    d ∈ (regionalTriangulationStandardEquiv T).1.1 ↔
      (regionalDiagonalStandardEquiv).symm d ∈ T.1.1 := by
  change d ∈ (regionalFamilyToStandardDissection T.1).1 ↔
    (regionalDiagonalStandardEquiv).symm d ∈ T.1.1
  simp [regionalFamilyToStandardDissection]

/-- Finite support of a regional triangulation. -/
noncomputable def regionalTriangulationSupport
    {n : ℕ} {D : Dissection n} {r : OptionalSignatureRegion D}
    (T : RegionalTriangulation (canonicalRegionDecomposition D) r) :
    Finset (OptionalSignatureRegionalDiagonal r) := by
  classical
  exact Finset.univ.filter (fun x => x ∈ T.1.1)

/-- The transported standard triangulation has exactly the image of the
regional channel support. -/
theorem regionalTriangulationStandard_support
    {n : ℕ} {D : Dissection n} {r : OptionalSignatureRegion D}
    (T : RegionalTriangulation (canonicalRegionDecomposition D) r) :
    (regionalTriangulationSupport T).map
        (regionalDiagonalStandardEquiv).toEmbedding =
      (regionalTriangulationStandardEquiv T).1.1 := by
  ext d
  rw [Finset.mem_map]
  constructor
  · rintro ⟨x, hx, rfl⟩
    rw [mem_regionalTriangulationStandardEquiv]
    simpa [regionalTriangulationSupport] using hx
  · intro hd
    refine ⟨(regionalDiagonalStandardEquiv).symm d, ?_,
      (regionalDiagonalStandardEquiv).apply_symm_apply d⟩
    simp only [regionalTriangulationSupport, Finset.mem_filter,
      Finset.mem_univ, true_and]
    exact (mem_regionalTriangulationStandardEquiv T d).mp hd

noncomputable instance regionalTriangulationFintype {n : ℕ} {D : Dissection n}
    (regions : RegionDecomposition D) (r : regions.Region) :
    Fintype (RegionalTriangulation regions r) :=
  Fintype.ofInjective Subtype.val Subtype.val_injective

noncomputable instance canonicalRegionDecompositionRegionalTriangulationFintype
    {n : ℕ} (D : Dissection n) (r : OptionalSignatureRegion D) :
    Fintype (RegionalTriangulation (canonicalRegionDecomposition D) r) :=
  regionalTriangulationFintype (canonicalRegionDecomposition D) r

/-- A regional noncrossing-family tuple is equivalently a tuple of regional
families. -/
def regionalDissectionFamiliesEquivPiRegionalFamily {n : ℕ}
    {D : Dissection n} (regions : RegionDecomposition D) :
    RegionalDissectionFamilies regions ≃
      ((r : regions.Region) → RegionalFamily regions r) where
  toFun A r := ⟨A.1 r, A.2 r⟩
  invFun A := ⟨fun r => (A r).1, fun r => (A r).2⟩
  left_inv A := by
    apply Subtype.ext
    rfl
  right_inv A := by
    funext r
    apply Subtype.ext
    rfl

/-- Maximality for a dependent product with pointwise order is exactly
coordinatewise maximality. -/
noncomputable def maximalPiEquivPiMaximal {ι : Type*} {β : ι → Type*}
    [∀ i, LE (β i)] (le_refl' : ∀ i (x : β i), x ≤ x) :
    {x : (∀ i, β i) // IsOrderMaximal x} ≃
      ((i : ι) → {y : β i // IsOrderMaximal y}) where
  toFun x i := ⟨x.1 i, by
    classical
    intro y hxy
    let z : ∀ j, β j := Function.update x.1 i y
    have hxz : x.1 ≤ z := by
      intro j
      by_cases hji : j = i
      · subst j
        simpa [z] using hxy
      · simpa [z, hji] using le_refl' j (x.1 j)
    have hzx := x.2 z hxz
    simpa [z] using hzx i⟩
  invFun x := ⟨fun i => (x i).1, by
    intro y hxy i
    exact (x i).2 (y i) (hxy i)⟩
  left_inv x := by
    apply Subtype.ext
    rfl
  right_inv x := by
    funext i
    apply Subtype.ext
    rfl

/-- Maximal global regional-family tuples are exactly tuples of regional
triangulations. -/
noncomputable def maximalRegionalFamiliesEquivPiRegionalTriangulation
    {n : ℕ} {D : Dissection n} (regions : RegionDecomposition D) :
    {A : RegionalDissectionFamilies regions // IsOrderMaximal A} ≃
      ((r : regions.Region) → RegionalTriangulation regions r) :=
  (maximalElementsEquiv
    (regionalDissectionFamiliesEquivPiRegionalFamily regions) (by
      intro A B
      rfl)).trans (maximalPiEquivPiMaximal (fun _ S _ hx => hx))

/-- Refining triangulations are canonically tuples of regional
triangulations. -/
noncomputable def refiningTriangulationsEquivRegionalTriangulations
    {n : ℕ} (D : Dissection n) (regions : RegionDecomposition D) :
    RefiningTriangulation D ≃
      ((r : regions.Region) → RegionalTriangulation regions r) :=
  (refiningTriangulationsEquivMaximalRegionalFamilies D regions).trans
    (maximalRegionalFamiliesEquivPiRegionalTriangulation regions)

/-- A filtered product over a finite type splits into filtered products over
the fibers of any dependent-sum presentation of that type. -/
theorem filtered_prod_equiv_sigma {A ι : Type*} {β : ι → Type*}
    [Fintype A] [Fintype ι] [∀ i, Fintype (β i)]
    {R : Type*} [CommMonoid R] (e : A ≃ Sigma β)
    (p : A → Prop) [DecidablePred p] (f : A → R) :
    (∏ a ∈ Finset.univ.filter p, f a) =
      ∏ i, ∏ b ∈ Finset.univ.filter (fun b => p (e.symm ⟨i, b⟩)),
        f (e.symm ⟨i, b⟩) := by
  classical
  calc
    (∏ a ∈ Finset.univ.filter p, f a) = ∏ a : A, if p a then f a else 1 := by
      rw [Finset.prod_filter]
    _ = ∏ z : Sigma β, if p (e.symm z) then f (e.symm z) else 1 := by
      exact Fintype.prod_equiv e _ _ (fun _ => by simp)
    _ = ∏ i, ∏ b : β i,
        if p (e.symm ⟨i, b⟩) then f (e.symm ⟨i, b⟩) else 1 := by
      rw [Fintype.prod_sigma]
    _ = ∏ i, ∏ b ∈ Finset.univ.filter (fun b => p (e.symm ⟨i, b⟩)),
        f (e.symm ⟨i, b⟩) := by
      apply Finset.prod_congr rfl
      intro i _
      rw [Finset.prod_filter]

/-- The product over a global optional family is the product of the products
in its regional restrictions. -/
theorem optionalFamilyWeight_partition {n : ℕ} {R : Type*} [CommMonoid R]
    {D : Dissection n} (regions : RegionDecomposition D)
    (inverseChannelWeight : Diagonal n → R) (S : OptionalDissectionFamily (D := D))
    [DecidablePred (fun x => x ∈ S.1)]
    [∀ r : regions.Region, DecidablePred
      (fun x => x ∈ (regionSetsEquiv regions S.1) r)] :
    (∏ d ∈ optionalFamilyFinset S, inverseChannelWeight d) =
      ∏ r, ∏ x ∈ Finset.univ.filter
          (fun x => x ∈ (regionSetsEquiv regions S.1) r),
        inverseChannelWeight (regions.address.symm ⟨r, x⟩).1 := by
  classical
  calc
    (∏ d ∈ optionalFamilyFinset S, inverseChannelWeight d) =
        ∏ x ∈ Finset.univ.filter (fun x => x ∈ S.1), inverseChannelWeight x.1 := by
      unfold optionalFamilyFinset
      exact Finset.prod_map _ _ inverseChannelWeight
    _ = ∏ r, ∏ x ∈ Finset.univ.filter
          (fun x => regions.address.symm ⟨r, x⟩ ∈ S.1),
        inverseChannelWeight (regions.address.symm ⟨r, x⟩).1 :=
      filtered_prod_equiv_sigma regions.address
        (fun x => x ∈ S.1) (fun x => inverseChannelWeight x.1)
    _ = _ := by
      apply Finset.prod_congr rfl
      intro r _
      congr 1
      ext x
      simp only [Finset.mem_filter, Finset.mem_univ, true_and]
      change (regions.address.symm ⟨r, x⟩ ∈ S.1 ↔
        regions.address.symm ⟨r, x⟩ ∈ S.1)
      exact Iff.rfl

/-- Product of inverse-channel weights represented by one regional triangulation. -/
noncomputable def regionalWeight {n : ℕ} {R : Type*} [CommMonoid R]
    (inverseChannelWeight : Diagonal n → R) {D : Dissection n}
    (regions : RegionDecomposition D) (r : regions.Region)
    (T : RegionalTriangulation regions r) : R := by
  classical
  exact ∏ x ∈ Finset.univ.filter (fun x => x ∈ T.1.1),
    inverseChannelWeight (regions.address.symm ⟨r, x⟩).1

/-- Residual channel weights factor into the weights of the regional
triangulations selected by the canonical indexing equivalence. -/
theorem residualWeight_product_regions {n : ℕ} {R : Type*} [CommMonoid R]
    (inverseChannelWeight : Diagonal n → R) (D : Dissection n)
    (regions : RegionDecomposition D) (T : RefiningTriangulation D) :
    residualWeight inverseChannelWeight D T =
      ∏ r, regionalWeight inverseChannelWeight regions r
        (refiningTriangulationsEquivRegionalTriangulations D regions T r) := by
  classical
  rw [residualWeight_eq_optionalFamilyWeight inverseChannelWeight D T]
  rw [optionalFamilyWeight_partition regions inverseChannelWeight
    (faceToOptionalFamily D ⟨T.1.1, T.2⟩)]
  apply Finset.prod_congr rfl
  intro r _
  unfold regionalWeight
  congr 1

/-- The amplitude of one region is the sum over its maximal noncrossing
families. -/
noncomputable def regionalAmplitude {n : ℕ} {R : Type*} [CommSemiring R]
    (inverseChannelWeight : Diagonal n → R) {D : Dissection n}
    (regions : RegionDecomposition D) (r : regions.Region) : R :=
  ∑ T : RegionalTriangulation regions r,
    regionalWeight inverseChannelWeight regions r T

/-- A complete regional factorization certificate for a selected dissection.
It identifies every global residue term with one triangulation per region and
states that residual channel weights multiply under that identification. -/
structure RegionalFactorization {n : ℕ} {R : Type*} [CommSemiring R]
    (inverseChannelWeight : Diagonal n → R) (D : Dissection n) where
  decomposition : RegionDecomposition D
  RegionalTriangulation : decomposition.Region → Type
  regionalFintype : ∀ r, Fintype (RegionalTriangulation r)
  terms : RefiningTriangulation D ≃
    ((r : decomposition.Region) → RegionalTriangulation r)
  regionalWeight : (r : decomposition.Region) → RegionalTriangulation r → R
  residualWeight_product : ∀ T,
    residualWeight inverseChannelWeight D T =
      ∏ r, regionalWeight r (terms T r)

attribute [instance] RegionalFactorization.regionalFintype

/-- The combinatorial regional decomposition canonically supplies every field
of the factorization certificate. -/
noncomputable def canonicalRegionalFactorization {n : ℕ} {R : Type*}
    [CommSemiring R] (inverseChannelWeight : Diagonal n → R) (D : Dissection n)
    (regions : RegionDecomposition D) :
    RegionalFactorization inverseChannelWeight D where
  decomposition := regions
  RegionalTriangulation := RegionalTriangulation regions
  regionalFintype := regionalTriangulationFintype regions
  terms := refiningTriangulationsEquivRegionalTriangulations D regions
  regionalWeight := regionalWeight inverseChannelWeight regions
  residualWeight_product := residualWeight_product_regions
    inverseChannelWeight D regions

/-- Once the geometric regional certificate is supplied, the coefficient
residue of the polygon amplitude is exactly the product of regional
amplitudes. This is the integrated factorization theorem. -/
theorem residueAmplitude_factorization {n : ℕ} {R : Type*}
    [CommSemiring R] (inverseChannelWeight : Diagonal n → R) (D : Dissection n)
    (F : RegionalFactorization inverseChannelWeight D) :
    residueAmplitude inverseChannelWeight D =
      ∏ r, ∑ u : F.RegionalTriangulation r, F.regionalWeight r u := by
  classical
  unfold residueAmplitude
  calc
    (∑ T : RefiningTriangulation D, residualWeight inverseChannelWeight D T) =
        ∑ a : ((r : F.decomposition.Region) → F.RegionalTriangulation r),
          ∏ r, F.regionalWeight r (a r) := by
      exact Fintype.sum_equiv F.terms
        (fun T => residualWeight inverseChannelWeight D T)
        (fun a => ∏ r, F.regionalWeight r (a r))
        F.residualWeight_product
    _ = ∏ r, ∑ u : F.RegionalTriangulation r, F.regionalWeight r u :=
      (Fintype.prod_sum F.regionalWeight).symm

/-- Certificate-free factorization for an arbitrary convex polygon and any
chosen regional decomposition of `D`. -/
theorem residueAmplitude_factorization_canonical {n : ℕ} {R : Type*}
    [CommSemiring R] (inverseChannelWeight : Diagonal n → R) (D : Dissection n)
    (regions : RegionDecomposition D) :
    residueAmplitude inverseChannelWeight D =
      ∏ r, regionalAmplitude inverseChannelWeight regions r := by
  classical
  let F := canonicalRegionalFactorization inverseChannelWeight D regions
  rw [residueAmplitude_factorization inverseChannelWeight D F]
  apply Finset.prod_congr rfl
  intro r _
  unfold regionalAmplitude
  exact Fintype.sum_equiv (Equiv.refl _) _ _ (fun _ => rfl)

/-- Laurent exponent vectors for planar channel variables. Negative entries
represent channel denominators. -/
abbrev ChannelExponent (n : ℕ) := Finsupp (Diagonal n) ℤ

/-- Laurent exponent vectors and algebras indexed by an arbitrary channel
type. -/
abbrev LaurentExponentOn (ι : Type*) := Finsupp ι ℤ

abbrev LaurentAlgebraOn (R : Type*) [Semiring R] (ι : Type*) :=
  AddMonoidAlgebra R (LaurentExponentOn ι)

/-- A channel equivalence induces an additive equivalence of Laurent exponent
vectors. -/
noncomputable def laurentExponentCongr {ι κ : Type*} (e : ι ≃ κ) :
    LaurentExponentOn ι ≃+ LaurentExponentOn κ :=
  Finsupp.domCongr e

/-- Regional global-channel exponents are canonically relabeled as exponents
on realized local ordered chords. -/
noncomputable def optionalSignatureRegionalExponentEquiv {n : ℕ}
    {D : Dissection n} (r : OptionalSignatureRegion D) :
    LaurentExponentOn (OptionalSignatureRegionalDiagonal r) ≃+
      LaurentExponentOn (RealizedLocalOrderedChord r) :=
  laurentExponentCongr (optionalSignatureRegionalChordEquiv r)

/-- Native convolution-preserving lift of a channel equivalence to Laurent
algebras. -/
noncomputable def laurentAlgebraRingCongr {R : Type*} [Semiring R]
    {ι κ : Type*} (e : ι ≃ κ) :
    LaurentAlgebraOn R ι ≃+* LaurentAlgebraOn R κ :=
  AddMonoidAlgebra.mapDomainRingEquiv R (laurentExponentCongr e)

/-- Regional exponents relabeled onto every standard lower-point channel. -/
noncomputable def regionalStandardExponentEquiv
    {n : ℕ} {D : Dissection n} {r : OptionalSignatureRegion D} :
    LaurentExponentOn (OptionalSignatureRegionalDiagonal r) ≃+
      LaurentExponentOn (Diagonal (optionalSignatureRegionArity r)) :=
  laurentExponentCongr regionalDiagonalStandardEquiv

/-- Explicit regional-to-standard lower-point Laurent-algebra relabeling. -/
noncomputable def regionalStandardLaurentEquiv
    {n : ℕ} {R : Type*} [Semiring R]
    {D : Dissection n} {r : OptionalSignatureRegion D} :
    LaurentAlgebraOn R (OptionalSignatureRegionalDiagonal r) ≃+*
      LaurentAlgebraOn R (Diagonal (optionalSignatureRegionArity r)) :=
  laurentAlgebraRingCongr regionalDiagonalStandardEquiv

/-- The regional channel relabeling lifted to a ring equivalence of Laurent
algebras on global regional channels and realized local channels. -/
noncomputable def optionalSignatureRegionalLaurentEquiv
    {n : ℕ} {R : Type*} [Semiring R]
    {D : Dissection n} (r : OptionalSignatureRegion D) :
    LaurentAlgebraOn R (OptionalSignatureRegionalDiagonal r) ≃+*
      LaurentAlgebraOn R (RealizedLocalOrderedChord r) :=
  laurentAlgebraRingCongr (optionalSignatureRegionalChordEquiv r)

/-- Inverse Laurent monomial on an arbitrary channel type. -/
noncomputable def laurentInverseOn {R : Type*} [Semiring R] {ι : Type*}
    (x : ι) : LaurentAlgebraOn R ι :=
  AddMonoidAlgebra.single (-Finsupp.single x 1) 1

/-- Channel relabeling carries each formal channel inverse to the inverse on
the relabeled channel. -/
theorem laurentAlgebraRingCongr_laurentInverse
    {R : Type*} [Semiring R] {ι κ : Type*} (e : ι ≃ κ) (x : ι) :
    laurentAlgebraRingCongr (R := R) e (laurentInverseOn x) =
      laurentInverseOn (e x) := by
  classical
  simp [laurentAlgebraRingCongr, laurentExponentCongr, laurentInverseOn]
  congr 1
  ext y
  by_cases hy : y = e x
  · subst y
    simp
  · have hsymm : e.symm y ≠ x := by
      intro h
      apply hy
      rw [← h, e.apply_symm_apply]
    simp [hy, hsymm]

/-- The explicit regional-to-standard Laurent relabeling preserves inverse
channel inverses channel by channel. -/
theorem regionalStandardLaurentEquiv_laurentInverse
    {n : ℕ} {R : Type*} [Semiring R]
    {D : Dissection n} {r : OptionalSignatureRegion D}
    (d : OptionalSignatureRegionalDiagonal r) :
    regionalStandardLaurentEquiv (R := R) (laurentInverseOn d) =
      laurentInverseOn (regionalDiagonalToStandard d) :=
  laurentAlgebraRingCongr_laurentInverse
    regionalDiagonalStandardEquiv d

/-- Relabeling carries each regional triangulation monomial to the monomial
of its transported standard triangulation. -/
theorem regionalStandardLaurentEquiv_triangulationProduct
    {n : ℕ} {R : Type*} [CommSemiring R]
    {D : Dissection n} {r : OptionalSignatureRegion D}
    (T : RegionalTriangulation (canonicalRegionDecomposition D) r) :
    regionalStandardLaurentEquiv (R := R)
        (∏ x ∈ regionalTriangulationSupport T, laurentInverseOn x) =
      ∏ d ∈ (regionalTriangulationStandardEquiv T).1.1,
        laurentInverseOn d := by
  rw [← regionalTriangulationStandard_support T]
  simp [regionalStandardLaurentEquiv_laurentInverse,
    regionalDiagonalStandardEquiv]

/-- Regional amplitude internal to its own canonical channel Laurent algebra. -/
noncomputable def canonicalRegionalFiberAmplitude
    {n : ℕ} {R : Type*} [CommSemiring R]
    {D : Dissection n} (r : OptionalSignatureRegion D) :
    LaurentAlgebraOn R (OptionalSignatureRegionalDiagonal r) := by
  classical
  let regions := canonicalRegionDecomposition D
  letI : Fintype (regions.RegionalDiagonal r) :=
    regions.regionalDiagonalFintype r
  letI : Fintype (RegionalTriangulation regions r) :=
    regionalTriangulationFintype regions r
  change LaurentAlgebraOn R (regions.RegionalDiagonal r)
  exact ∑ T : RegionalTriangulation regions r,
    ∏ x ∈ Finset.univ.filter (fun x => x ∈ T.1.1), laurentInverseOn x

/-- The canonical regional amplitude expressed directly in the full standard
lower-point channel Laurent algebra. -/
noncomputable def canonicalRegionalStandardAmplitude
    {n : ℕ} {R : Type*} [CommSemiring R]
    {D : Dissection n} {r : OptionalSignatureRegion D} :
    LaurentAlgebraOn R (Diagonal (optionalSignatureRegionArity r)) :=
  regionalStandardLaurentEquiv (R := R)
    (canonicalRegionalFiberAmplitude (R := R) r)

/-- Its definition is the explicit channel-by-channel Laurent transport. -/
theorem canonicalRegionalFiberAmplitude_standard_relabel
    {n : ℕ} {R : Type*} [CommSemiring R]
    {D : Dissection n} {r : OptionalSignatureRegion D} :
    regionalStandardLaurentEquiv (R := R)
        (canonicalRegionalFiberAmplitude (R := R) r) =
      canonicalRegionalStandardAmplitude (R := R) := rfl

/-- The same regional amplitude expressed in realized local channel
coordinates. -/
noncomputable def realizedLocalRegionalAmplitude
    {n : ℕ} {R : Type*} [CommSemiring R]
    {D : Dissection n} (r : OptionalSignatureRegion D) :
    LaurentAlgebraOn R (RealizedLocalOrderedChord r) :=
  optionalSignatureRegionalLaurentEquiv (R := R) r
    (canonicalRegionalFiberAmplitude (R := R) r)

/-- Regional amplitude transport along the explicit channel relabeling. -/
theorem canonicalRegionalFiberAmplitude_relabel
    {n : ℕ} {R : Type*} [CommSemiring R]
    {D : Dissection n} (r : OptionalSignatureRegion D) :
    optionalSignatureRegionalLaurentEquiv (R := R) r
        (canonicalRegionalFiberAmplitude (R := R) r) =
      realizedLocalRegionalAmplitude r := rfl

/-- Embed regional exponent vectors into the ambient global channel lattice. -/
noncomputable def optionalSignatureRegionalExponentEmbedding
    {n : ℕ} {D : Dissection n} (r : OptionalSignatureRegion D) :
    LaurentExponentOn (OptionalSignatureRegionalDiagonal r) →+
      ChannelExponent n :=
  Finsupp.mapDomain.addMonoidHom (fun d => d.1.1)

/-- Embed a regional Laurent algebra into the ambient global Laurent algebra. -/
noncomputable def optionalSignatureRegionalLaurentEmbedding
    {n : ℕ} {R : Type*} [Semiring R]
    {D : Dissection n} (r : OptionalSignatureRegion D) :
    LaurentAlgebraOn R (OptionalSignatureRegionalDiagonal r) →+*
      AddMonoidAlgebra R (ChannelExponent n) :=
  AddMonoidAlgebra.mapDomainRingHom R
    (optionalSignatureRegionalExponentEmbedding r)

/-- The finite-support Laurent algebra in independent planar channel
variables. -/
abbrev ChannelLaurentAlgebra (R : Type*) [Semiring R] (n : ℕ) :=
  AddMonoidAlgebra R (ChannelExponent n)

/-- Source momentum data with an explicit conservation law. The polygon
label is a particle label; no time interpretation is attached. -/
structure MomentumConfiguration (V : Type*) [AddCommGroup V] (n : ℕ) where
  momentum : Fin n → V
  total_zero : ∑ i, momentum i = 0

/-- Momentum carried by the consecutive planar channel represented by `d`. -/
def channelMomentum {V : Type*} [AddCommGroup V] {n : ℕ}
    (P : MomentumConfiguration V n) (d : Diagonal n) : V :=
  ∑ i ∈ Finset.univ.filter (fun i : Fin n => d.lo ≤ i ∧ i < d.hi),
    P.momentum i

/-- Momentum carried by the complementary particle labels. -/
noncomputable def complementaryChannelMomentum
    {V : Type*} [AddCommGroup V] {n : ℕ}
    (P : MomentumConfiguration V n) (d : Diagonal n) : V := by
  classical
  exact ∑ i ∈ Finset.univ.filter
    (fun i : Fin n => ¬(d.lo ≤ i ∧ i < d.hi)), P.momentum i

/-- The channel labels and their complement partition all particle labels. -/
theorem channelMomentum_add_complementary
    {V : Type*} [AddCommGroup V] {n : ℕ}
    (P : MomentumConfiguration V n) (d : Diagonal n) :
    channelMomentum P d + complementaryChannelMomentum P d =
      ∑ i, P.momentum i := by
  classical
  unfold channelMomentum complementaryChannelMomentum
  simpa using (Finset.sum_filter_add_sum_filter_not
    (s := Finset.univ)
    (p := fun i : Fin n => d.lo ≤ i ∧ i < d.hi)
    (f := P.momentum))

/-- Conservation identifies complementary channel momentum with the negative
of channel momentum. -/
theorem complementaryChannelMomentum_eq_neg
    {V : Type*} [AddCommGroup V] {n : ℕ}
    (P : MomentumConfiguration V n) (d : Diagonal n) :
    complementaryChannelMomentum P d = -channelMomentum P d := by
  have h := channelMomentum_add_complementary P d
  rw [P.total_zero] at h
  rw [add_comm] at h
  exact eq_neg_of_add_eq_zero_left h

/-- An even momentum readout. No quadratic law or bilinear polarization is
asserted; evenness is exactly the property used for complementary channels. -/
structure EvenMomentumReadout (V K : Type*) [Neg V] where
  value : V → K
  even : ∀ v, value (-v) = value v

/-- Conserved momenta whose individual entries are massless for the declared
quadratic map. This structure is not an assumption of the evaluated residue or
factorization theorems below; those results use only `MomentumConfiguration`,
quadratic evenness, and explicit channel units. -/
structure MasslessMomentumConfiguration (V K : Type*) [AddCommGroup V]
    (Q : EvenMomentumReadout V K) (n : ℕ)
    extends MomentumConfiguration V n where
  massless : ∀ i, Q.value (momentum i) = Q.value 0

/-- Planar channel value derived from source momentum and an even readout. -/
def planarChannelReadout {V K : Type*} [AddCommGroup V] {n : ℕ}
    (Q : EvenMomentumReadout V K) (P : MomentumConfiguration V n)
    (d : Diagonal n) : K :=
  Q.value (channelMomentum P d)

/-- Conservation and evenness identify the complementary-channel readout with
the planar channel value. No masslessness or bilinearity
assumption is used. -/
theorem complementaryChannelReadout_eq_planarChannelReadout
    {V K : Type*} [AddCommGroup V] {n : ℕ}
    (Q : EvenMomentumReadout V K) (P : MomentumConfiguration V n)
    (d : Diagonal n) :
    Q.value (complementaryChannelMomentum P d) =
      planarChannelReadout Q P d := by
  rw [complementaryChannelMomentum_eq_neg]
  exact Q.even (channelMomentum P d)

/-- Data required to evaluate the Laurent presentation: every planar channel
readout is represented by a unit in the target ring. This makes
the localization requirement explicit. -/
structure InvertiblePlanarChannelReadout
    (V K : Type*) [AddCommGroup V] [CommRing K] {n : ℕ}
    (Q : EvenMomentumReadout V K) (P : MomentumConfiguration V n) where
  channelUnit : Diagonal n → Kˣ
  coe_channelUnit : ∀ d, (channelUnit d : K) = planarChannelReadout Q P d

/-- The supplied channel-unit structure is exactly the localization
hypothesis that every planar channel-readout value is a unit. Momentum
conservation and evenness alone do not supply this condition. -/
theorem nonempty_invertiblePlanarChannelReadout_iff
    {V K : Type*} [AddCommGroup V] [CommRing K] {n : ℕ}
    (Q : EvenMomentumReadout V K) (P : MomentumConfiguration V n) :
    Nonempty (InvertiblePlanarChannelReadout V K Q P) ↔
      ∀ d : Diagonal n, IsUnit (planarChannelReadout Q P d) := by
  constructor
  · rintro ⟨U⟩ d
    exact ⟨U.channelUnit d, U.coe_channelUnit d⟩
  · intro h
    classical
    choose u hu using h
    exact ⟨{
      channelUnit := u
      coe_channelUnit := hu
    }⟩

/-- Integer powers of a unit form an additive homomorphism into the additive
presentation of its multiplicative group. -/
def unitZPowAddHom {K : Type*} [CommRing K] (u : Kˣ) :
    ℤ →+ Additive Kˣ where
  toFun z := Additive.ofMul (u ^ z)
  map_zero' := by simp
  map_add' x y := by simp [zpow_add]

/-- Evaluate a Laurent exponent vector as a product of its assigned channel
units. -/
noncomputable def channelExponentUnitAddHom
    {K : Type*} [CommRing K] {n : ℕ} (u : Diagonal n → Kˣ) :
    ChannelExponent n →+ Additive Kˣ :=
  Finsupp.liftAddHom (fun d => unitZPowAddHom (u d))

/-- Multiplicative form of channel-exponent evaluation. -/
noncomputable def channelExponentUnitMonoidHom
    {K : Type*} [CommRing K] {n : ℕ} (u : Diagonal n → Kˣ) :
    Multiplicative (ChannelExponent n) →* Kˣ where
  toFun a := (channelExponentUnitAddHom u a.toAdd).toMul
  map_one' := by simp
  map_mul' a b := by
    change (channelExponentUnitAddHom u (a.toAdd + b.toAdd)).toMul =
      (channelExponentUnitAddHom u a.toAdd).toMul *
        (channelExponentUnitAddHom u b.toAdd).toMul
    rw [map_add]
    rfl

noncomputable def channelExponentMonoidHom
    {K : Type*} [CommRing K] {n : ℕ} (u : Diagonal n → Kˣ) :
    Multiplicative (ChannelExponent n) →* K :=
  (Units.coeHom K).comp (channelExponentUnitMonoidHom u)

/-- Laurent evaluation determined by invertible planar channel-readout values. -/
noncomputable def planarChannelReadoutEvaluation
    {V K : Type*} [AddCommGroup V] [CommRing K] {n : ℕ}
    {Q : EvenMomentumReadout V K} {P : MomentumConfiguration V n}
    (U : InvertiblePlanarChannelReadout V K Q P) :
    ChannelLaurentAlgebra K n →+* K :=
  ((AddMonoidAlgebra.lift K K (ChannelExponent n))
    (channelExponentMonoidHom U.channelUnit)).toRingHom

/-- The Laurent channel inverse evaluates to its assigned readout unit's
inverse. -/
theorem planarChannelReadoutEvaluation_channelInverse
    {V K : Type*} [AddCommGroup V] [CommRing K] {n : ℕ}
    {Q : EvenMomentumReadout V K} {P : MomentumConfiguration V n}
    (U : InvertiblePlanarChannelReadout V K Q P) (d : Diagonal n) :
    planarChannelReadoutEvaluation U (laurentInverseOn d) =
      (↑((U.channelUnit d)⁻¹) : K) := by
  classical
  simp [planarChannelReadoutEvaluation, laurentInverseOn,
    channelExponentMonoidHom, channelExponentUnitMonoidHom,
    channelExponentUnitAddHom, unitZPowAddHom]
  rw [Finset.prod_eq_single d]
  · simp
  · intro b _ hbd
    simp [hbd]
  · intro hd
    exact False.elim (hd (Finset.mem_univ d))

/-- Evaluated channel inverses are genuine inverses of the planar channel
readout values. -/
theorem planarChannelReadoutEvaluation_inverse_mul_value
    {V K : Type*} [AddCommGroup V] [CommRing K] {n : ℕ}
    {Q : EvenMomentumReadout V K} {P : MomentumConfiguration V n}
    (U : InvertiblePlanarChannelReadout V K Q P) (d : Diagonal n) :
    planarChannelReadoutEvaluation U (laurentInverseOn d) *
      planarChannelReadout Q P d = 1 := by
  rw [planarChannelReadoutEvaluation_channelInverse,
    ← U.coe_channelUnit]
  exact Units.inv_mul (U.channelUnit d)

/-- Inverse of the explicit channel-readout unit. -/
def inverseChannelReadout
    {V K : Type*} [AddCommGroup V] [CommRing K] {n : ℕ}
    {Q : EvenMomentumReadout V K} {P : MomentumConfiguration V n}
    (U : InvertiblePlanarChannelReadout V K Q P) (d : Diagonal n) : K :=
  ↑((U.channelUnit d)⁻¹)

/-- Laurent evaluation agrees pointwise with the inverse channel readout. -/
theorem planarChannelReadoutEvaluation_eq_inverseChannelReadout
    {V K : Type*} [AddCommGroup V] [CommRing K] {n : ℕ}
    {Q : EvenMomentumReadout V K} {P : MomentumConfiguration V n}
    (U : InvertiblePlanarChannelReadout V K Q P) (d : Diagonal n) :
    planarChannelReadoutEvaluation U (laurentInverseOn d) =
      inverseChannelReadout U d :=
  planarChannelReadoutEvaluation_channelInverse U d


/-- Evaluated residue factorization using the canonical side-signature region
decomposition; no regional decomposition is supplied to the theorem. -/
theorem evaluatedResidueAmplitude_factorization
    {V K : Type*} [AddCommGroup V] [CommRing K] {n : ℕ}
    {Q : EvenMomentumReadout V K} {P : MomentumConfiguration V n}
    (U : InvertiblePlanarChannelReadout V K Q P) (D : Dissection n) :
    residueAmplitude (inverseChannelReadout U) D =
      ∏ r, regionalAmplitude (inverseChannelReadout U)
        (canonicalRegionDecomposition D) r :=
  residueAmplitude_factorization_canonical
    (inverseChannelReadout U) D (canonicalRegionDecomposition D)

/-- The complementary channel has the same invariant; this relation follows
from conservation and quadratic evenness. -/
theorem planarChannelReadout_complementary
    {V K : Type*} [AddCommGroup V] {n : ℕ}
    (Q : EvenMomentumReadout V K) (P : MomentumConfiguration V n)
    (d : Diagonal n) :
    Q.value (complementaryChannelMomentum P d) = planarChannelReadout Q P d := by
  rw [complementaryChannelMomentum_eq_neg, Q.even]
  rfl


/-- Relations derived from a specified algebraic evaluation are its kernel;
no relation is inserted independently of that source map. -/
noncomputable def sourceDerivedKinematicIdeal {n : ℕ} {R K : Type*}
    [CommRing R] [CommRing K]
    (φ : ChannelLaurentAlgebra R n →+* K) :
    Ideal (ChannelLaurentAlgebra R n) := RingHom.ker φ

/-- Kinematic quotient presented by the kernel of a source evaluation. -/
abbrev SourceKinematicRing {n : ℕ} {R K : Type*}
    [CommRing R] [CommRing K]
    (φ : ChannelLaurentAlgebra R n →+* K) :=
  ChannelLaurentAlgebra R n ⧸ sourceDerivedKinematicIdeal φ

/-- Canonical projection to the source-derived kinematic quotient. -/
noncomputable abbrev sourceKinematicProjection {n : ℕ} {R K : Type*}
    [CommRing R] [CommRing K]
    (φ : ChannelLaurentAlgebra R n →+* K) :
    ChannelLaurentAlgebra R n →+* SourceKinematicRing φ :=
  Ideal.Quotient.mk (sourceDerivedKinematicIdeal φ)

/-- Equality in a source-derived kinematic quotient is exactly equality under
the source evaluation. -/
theorem sourceKinematicProjection_eq_iff
    {n : ℕ} {R K : Type*} [CommRing R] [CommRing K]
    (φ : ChannelLaurentAlgebra R n →+* K)
    (f g : ChannelLaurentAlgebra R n) :
    sourceKinematicProjection φ f = sourceKinematicProjection φ g ↔
      φ f = φ g := by
  constructor
  · intro h
    change (Ideal.Quotient.mk (RingHom.ker φ)) f =
      (Ideal.Quotient.mk (RingHom.ker φ)) g at h
    apply sub_eq_zero.mp
    rw [← map_sub]
    apply (RingHom.mem_ker).mp
    apply (Ideal.Quotient.eq_zero_iff_mem).mp
    rw [map_sub, h, sub_self]
  · intro h
    apply sub_eq_zero.mp
    rw [← map_sub]
    apply (Ideal.Quotient.eq_zero_iff_mem).mpr
    apply (RingHom.mem_ker).mpr
    rw [map_sub, h, sub_self]

/-- Evaluated planar kinematic ring derived from conserved momenta,
the even channel readout, and the declared channel localizations. -/
abbrev EvaluatedPlanarKinematicRing
    {V K : Type*} [AddCommGroup V] [CommRing K] {n : ℕ}
    {Q : EvenMomentumReadout V K} {P : MomentumConfiguration V n}
    (U : InvertiblePlanarChannelReadout V K Q P) :=
  SourceKinematicRing (planarChannelReadoutEvaluation U)

/-- Canonical projection from independent channels to evaluated planar
kinematics. -/
noncomputable abbrev evaluatedPlanarKinematicProjection
    {V K : Type*} [AddCommGroup V] [CommRing K] {n : ℕ}
    {Q : EvenMomentumReadout V K} {P : MomentumConfiguration V n}
    (U : InvertiblePlanarChannelReadout V K Q P) :
    ChannelLaurentAlgebra K n →+* EvaluatedPlanarKinematicRing U :=
  sourceKinematicProjection (planarChannelReadoutEvaluation U)

/-- The positive Laurent monomial representing the planar channel variable
`X_d`. -/
noncomputable def channelVariable {n : ℕ} {R : Type*} [Semiring R]
    (d : Diagonal n) : ChannelLaurentAlgebra R n :=
  AddMonoidAlgebra.single (Finsupp.single d 1) 1

/-- The formal channel inverse associated with a polygon diagonal. -/
noncomputable def channelInverse {n : ℕ} {R : Type*} [Semiring R] (d : Diagonal n) :
    ChannelLaurentAlgebra R n :=
  AddMonoidAlgebra.single (-Finsupp.single d 1) 1

/-- Regional-to-global Laurent embedding preserves formal channel inverses. -/
theorem optionalSignatureRegionalLaurentEmbedding_laurentInverse
    {n : ℕ} {R : Type*} [Semiring R]
    {D : Dissection n} (r : OptionalSignatureRegion D)
    (x : OptionalSignatureRegionalDiagonal r) :
    optionalSignatureRegionalLaurentEmbedding (R := R) r
        (laurentInverseOn x) = channelInverse x.1.1 := by
  classical
  simp [optionalSignatureRegionalLaurentEmbedding,
    optionalSignatureRegionalExponentEmbedding,
    laurentInverseOn, channelInverse]
  congr 1
  change (Finsupp.mapDomain.addMonoidHom (fun d => d.1.1))
      (-Finsupp.single x 1) = -Finsupp.single x.1.1 1
  rw [map_neg]
  simp

/-- Embedding the intrinsic regional amplitude recovers the corresponding
ambient regional amplitude exactly. -/
theorem optionalSignatureRegionalLaurentEmbedding_fiberAmplitude
    {n : ℕ} {R : Type*} [CommSemiring R]
    {D : Dissection n} (r : OptionalSignatureRegion D) :
    optionalSignatureRegionalLaurentEmbedding (R := R) r
        (canonicalRegionalFiberAmplitude (R := R) r) =
      regionalAmplitude (channelInverse (R := R))
        (canonicalRegionDecomposition D) r := by
  classical
  let regions := canonicalRegionDecomposition D
  letI : Fintype (regions.RegionalDiagonal r) :=
    regions.regionalDiagonalFintype r
  letI : Fintype (RegionalTriangulation regions r) :=
    regionalTriangulationFintype regions r
  change optionalSignatureRegionalLaurentEmbedding (R := R) r
      (∑ T : RegionalTriangulation regions r,
        ∏ x ∈ Finset.univ.filter (fun x => x ∈ T.1.1), laurentInverseOn x) =
    ∑ T : RegionalTriangulation regions r,
      ∏ x ∈ Finset.univ.filter (fun x => x ∈ T.1.1), channelInverse x.1.1
  simp_rw [map_sum, map_prod]
  apply Finset.sum_congr rfl
  intro T _
  apply Finset.prod_congr rfl
  intro x _
  exact optionalSignatureRegionalLaurentEmbedding_laurentInverse r x

/-- Integer Laurent exponents make the channel-inverse monomial a genuine
multiplicative inverse of its channel variable. -/
theorem channelVariable_mul_channelInverse {n : ℕ} {R : Type*}
    [CommSemiring R] (d : Diagonal n) :
    channelVariable (R := R) d * channelInverse (R := R) d = 1 := by
  classical
  simp [channelVariable, channelInverse,
    AddMonoidAlgebra.single_mul_single, AddMonoidAlgebra.one_def]

/-- The inverse also multiplies to one in the opposite order. -/
theorem channelInverse_mul_channelVariable {n : ℕ} {R : Type*}
    [CommSemiring R] (d : Diagonal n) :
    channelInverse (R := R) d * channelVariable (R := R) d = 1 := by
  rw [mul_comm]
  exact channelVariable_mul_channelInverse d

/-- The combinatorial planar biadjoint amplitude in independent channel
variables. This is the formal target of the declared evaluation, not by itself
a claim about a physical amplitude. -/
noncomputable def combinatorialBiadjointAmplitude {n : ℕ} {R : Type*}
    [CommSemiring R] : ChannelLaurentAlgebra R n :=
  planarAmplitude (channelInverse (R := R))

/-- Projected quotient class of a planar channel variable. -/
noncomputable def projectedPlanarChannel
    {V K : Type*} [AddCommGroup V] [CommRing K] {n : ℕ}
    {Q : EvenMomentumReadout V K} {P : MomentumConfiguration V n}
    (U : InvertiblePlanarChannelReadout V K Q P) (d : Diagonal n) :
    EvaluatedPlanarKinematicRing U :=
  evaluatedPlanarKinematicProjection U (channelVariable d)

/-- Projected quotient class of the inverse planar channel variable. -/
noncomputable def projectedPlanarInverseChannel
    {V K : Type*} [AddCommGroup V] [CommRing K] {n : ℕ}
    {Q : EvenMomentumReadout V K} {P : MomentumConfiguration V n}
    (U : InvertiblePlanarChannelReadout V K Q P) (d : Diagonal n) :
    EvaluatedPlanarKinematicRing U :=
  evaluatedPlanarKinematicProjection U (channelInverse d)

/-- Every projected planar channel remains a unit with the projected formal
inverse. -/
theorem projectedPlanarChannel_mul_inverse
    {V K : Type*} [AddCommGroup V] [CommRing K] {n : ℕ}
    {Q : EvenMomentumReadout V K} {P : MomentumConfiguration V n}
    (U : InvertiblePlanarChannelReadout V K Q P) (d : Diagonal n) :
    projectedPlanarChannel U d * projectedPlanarInverseChannel U d = 1 := by
  unfold projectedPlanarChannel projectedPlanarInverseChannel
  rw [← map_mul, channelVariable_mul_channelInverse, map_one]

/-- The inverse relation also holds in the opposite order. -/
theorem projectedPlanarInverseChannel_mul_channel
    {V K : Type*} [AddCommGroup V] [CommRing K] {n : ℕ}
    {Q : EvenMomentumReadout V K} {P : MomentumConfiguration V n}
    (U : InvertiblePlanarChannelReadout V K Q P) (d : Diagonal n) :
    projectedPlanarInverseChannel U d * projectedPlanarChannel U d = 1 := by
  rw [mul_comm]
  exact projectedPlanarChannel_mul_inverse U d

/-- Projected quotient class of the global combinatorial amplitude. -/
noncomputable def projectedPlanarAmplitudeClass
    {V K : Type*} [AddCommGroup V] [CommRing K] {n : ℕ}
    {Q : EvenMomentumReadout V K} {P : MomentumConfiguration V n}
    (U : InvertiblePlanarChannelReadout V K Q P) :
    EvaluatedPlanarKinematicRing U :=
  evaluatedPlanarKinematicProjection U
    (combinatorialBiadjointAmplitude (n := n) (R := K))

/-- Canonical regional Laurent transport is exactly the standard lower-point
combinatorial biadjoint amplitude. -/
theorem canonicalRegionalStandardAmplitude_eq_combinatorialBiadjointAmplitude
    {n : ℕ} {R : Type*} [CommSemiring R]
    {D : Dissection n} {r : OptionalSignatureRegion D} :
    canonicalRegionalStandardAmplitude (R := R) =
      combinatorialBiadjointAmplitude
        (n := optionalSignatureRegionArity r) (R := R) := by
  change regionalStandardLaurentEquiv (R := R)
      (∑ T : RegionalTriangulation (canonicalRegionDecomposition D) r,
        ∏ x ∈ regionalTriangulationSupport T, laurentInverseOn x) =
    ∑ T : Triangulation (optionalSignatureRegionArity r),
      ∏ d ∈ T.1.1, laurentInverseOn d
  rw [map_sum]
  exact Fintype.sum_equiv regionalTriangulationStandardEquiv
    (fun T => regionalStandardLaurentEquiv (R := R)
      (∏ x ∈ regionalTriangulationSupport T, laurentInverseOn x))
    (fun T => ∏ d ∈ T.1.1, laurentInverseOn d)
    regionalStandardLaurentEquiv_triangulationProduct

/-- Canonical residue factorization into explicitly relabeled standard
lower-point amplitudes; no regional presentation certificate is supplied. -/
theorem residueAmplitude_factorization_standardLowerPoint
    {n : ℕ} {R : Type*} [CommSemiring R] (D : Dissection n) :
    residueAmplitude (channelInverse (R := R)) D =
      ∏ r : OptionalSignatureRegion D,
        optionalSignatureRegionalLaurentEmbedding (R := R) r
          ((regionalStandardLaurentEquiv (R := R) (r := r)).symm
            (combinatorialBiadjointAmplitude
              (n := optionalSignatureRegionArity r) (R := R))) := by
  rw [residueAmplitude_factorization_canonical
    (channelInverse (R := R)) D (canonicalRegionDecomposition D)]
  apply Finset.prod_congr rfl
  intro r _
  rw [← optionalSignatureRegionalLaurentEmbedding_fiberAmplitude]
  congr 1
  apply (regionalStandardLaurentEquiv (R := R) (r := r)).injective
  rw [(regionalStandardLaurentEquiv (R := R) (r := r)).apply_symm_apply]
  exact canonicalRegionalStandardAmplitude_eq_combinatorialBiadjointAmplitude
    (R := R)

/-- The defining triangulation expansion of the combinatorial amplitude. -/
theorem combinatorialBiadjointAmplitude_eq_triangulation_sum {n : ℕ}
    {R : Type*} [CommSemiring R] :
    combinatorialBiadjointAmplitude (n := n) (R := R) =
      ∑ T : Triangulation n,
        ∏ d ∈ T.1.1, channelInverse (R := R) d := rfl

/-- Source-facing contract identifying an amplitude with the checked
triangulation presentation. Lean inhabitation enforces the equality but does
not encode external provenance or certify that the value was separately
supplied. -/
structure BiadjointAmplitudePresentation (n : ℕ) (R : Type*)
    [CommSemiring R] where
  presentedAmplitude : ChannelLaurentAlgebra R n
  triangulation_expansion :
    presentedAmplitude = combinatorialBiadjointAmplitude (n := n) (R := R)

/-- The combinatorial amplitude itself canonically inhabits the presentation
contract. This inhabitant supplies no external physical provenance. -/
noncomputable def combinatorialBiadjointAmplitudePresentation
    (n : ℕ) (R : Type*) [CommSemiring R] :
    BiadjointAmplitudePresentation n R where
  presentedAmplitude := combinatorialBiadjointAmplitude
  triangulation_expansion := rfl

/-- The equality field determines the entire presentation. Thus the structure
contains no independent formal amplitude datum beyond the checked
triangulation expression. -/
instance biadjointAmplitudePresentationSubsingleton
    (n : ℕ) (R : Type*) [CommSemiring R] :
    Subsingleton (BiadjointAmplitudePresentation n R) where
  allEq a b := by
    cases a with
    | mk av ah =>
      cases b with
      | mk bv bh =>
        simp_all

/-- Exponent vector of the channel-inverse monomial belonging to a finite
diagonal family. -/
noncomputable def diagonalFamilyExponent {n : ℕ} (s : Finset (Diagonal n)) :
    ChannelExponent n :=
  -(∑ d ∈ s, Finsupp.single d 1)

/-- A product of formal channel inverses is the Laurent monomial with
exponent `-1` precisely on its diagonal family. -/
theorem channelInverse_prod {n : ℕ} {R : Type*} [CommSemiring R]
    (s : Finset (Diagonal n)) :
    (∏ d ∈ s, channelInverse (R := R) d) =
      AddMonoidAlgebra.single (diagonalFamilyExponent s) 1 := by
  classical
  induction s using Finset.induction_on with
  | empty => simp [diagonalFamilyExponent, AddMonoidAlgebra.one_def]
  | @insert d s hd ih =>
      simp [diagonalFamilyExponent, hd, channelInverse,
        AddMonoidAlgebra.single_mul_single, add_comm]

/-- The exponent shift that removes one formal channel inverse for every cut in
`D`. -/
noncomputable def cutExponent {n : ℕ} (D : Dissection n) : ChannelExponent n :=
  ∑ d ∈ D.1, Finsupp.single d 1

/-- A Laurent monomial has the prescribed simultaneous simple pole along `D`
when every selected channel occurs with exponent exactly `-1`. -/
def HasSimplePolesAlong {n : ℕ} (D : Dissection n)
    (a : ChannelExponent n) : Prop :=
  ∀ d ∈ D.1, a d = -1

/-- The selected simple-pole test on a dissection monomial is exactly finite-set
containment of all selected cuts. -/
theorem hasSimplePolesAlong_diagonalFamilyExponent {n : ℕ}
    (D : Dissection n) (s : Finset (Diagonal n)) :
    HasSimplePolesAlong D (diagonalFamilyExponent s) ↔ D.1 ⊆ s := by
  classical
  constructor
  · intro h d hdD
    by_contra hds
    have hd := h d hdD
    simp [diagonalFamilyExponent, Finsupp.single_apply, hds] at hd
  · intro h d hdD
    have hds : d ∈ s := h hdD
    simp [diagonalFamilyExponent, Finsupp.single_apply, hds]

/-- For a family containing `D`, the residue exponent shift removes exactly
the selected diagonals. -/
theorem diagonalFamilyExponent_add_cutExponent {n : ℕ}
    (D : Dissection n) (s : Finset (Diagonal n)) (hDs : D.1 ⊆ s) :
    diagonalFamilyExponent s + cutExponent D =
      diagonalFamilyExponent (s \ D.1) := by
  classical
  ext d
  by_cases hdD : d ∈ D.1
  · have hds : d ∈ s := hDs hdD
    simp [diagonalFamilyExponent, cutExponent, Finsupp.single_apply, hdD, hds]
  · by_cases hds : d ∈ s
    · simp [diagonalFamilyExponent, cutExponent, Finsupp.single_apply, hdD, hds]
    · simp [diagonalFamilyExponent, cutExponent, Finsupp.single_apply, hdD, hds]

/-- The cuts newly introduced by a refinement `D ≤ E`, retained as a
noncrossing dissection. -/
def dissectionDifference {n : ℕ} (E D : Dissection n) : Dissection n :=
  ⟨E.1 \ D.1, isDissection_subset E.2 (by
    intro d hd
    exact (Finset.mem_sdiff.mp hd).1)⟩

/-- Exponent shifts compose for nested dissections. -/
theorem cutExponent_add_difference {n : ℕ} (D E : Dissection n)
    (hDE : D ≤ E) :
    cutExponent D + cutExponent (dissectionDifference E D) = cutExponent E := by
  classical
  ext d
  by_cases hdD : d ∈ D.1
  · have hdE : d ∈ E.1 := hDE hdD
    simp [cutExponent, dissectionDifference, Finsupp.single_apply, hdD, hdE]
  · by_cases hdE : d ∈ E.1
    · simp [cutExponent, dissectionDifference, Finsupp.single_apply, hdD, hdE]
    · simp [cutExponent, dissectionDifference, Finsupp.single_apply, hdD, hdE]

/-- For nested cuts, passing the first simple-pole test and then testing the
new cuts after the first exponent shift is equivalent to the direct test. -/
theorem hasSimplePolesAlong_nested {n : ℕ} (D E : Dissection n)
    (hDE : D ≤ E) (a : ChannelExponent n) :
    (HasSimplePolesAlong D a ∧
      HasSimplePolesAlong (dissectionDifference E D) (a + cutExponent D)) ↔
      HasSimplePolesAlong E a := by
  classical
  constructor
  · rintro ⟨hD, hnew⟩ d hdE
    by_cases hdD : d ∈ D.1
    · exact hD d hdD
    · have hdnew : d ∈ (dissectionDifference E D).1 :=
        Finset.mem_sdiff.mpr ⟨hdE, hdD⟩
      have h := hnew d hdnew
      simpa [cutExponent, Finsupp.single_apply, hdD] using h
  · intro hE
    constructor
    · intro d hdD
      exact hE d (hDE hdD)
    · intro d hdnew
      have hd := Finset.mem_sdiff.mp hdnew
      have h := hE d hd.1
      simpa [cutExponent, Finsupp.single_apply, hd.2] using h

/-- Simultaneous Laurent-coefficient residue convention. It discards monomials
without exponent `-1` in every selected channel and shifts each retained
exponent by `+1`, thereby removing the selected channel inverses. -/
noncomputable def simultaneousChannelResidue {n : ℕ} {R : Type*} [Semiring R]
    (D : Dissection n) (f : ChannelLaurentAlgebra R n) :
    ChannelLaurentAlgebra R n := by
  classical
  exact f.coeff.sum fun a c =>
    if HasSimplePolesAlong D a then
      AddMonoidAlgebra.single (a + cutExponent D) c
    else 0

/-- The residue convention acts on one Laurent monomial by the declared pole
test and exponent shift. -/
theorem simultaneousChannelResidue_single {n : ℕ} {R : Type*} [Semiring R]
    (D : Dissection n) (a : ChannelExponent n) (c : R)
    [Decidable (HasSimplePolesAlong D a)] :
    simultaneousChannelResidue D (AddMonoidAlgebra.single a c) =
      if HasSimplePolesAlong D a then
        AddMonoidAlgebra.single (a + cutExponent D) c
      else 0 := by
  classical
  simp [simultaneousChannelResidue]

/-- The residue of one formal channel inverse along its singleton cut is one. -/
theorem simultaneousChannelResidue_singleton_channelInverse
    {n : ℕ} {R : Type*} [CommRing R] (d : Diagonal n) :
    simultaneousChannelResidue (singletonDissection d)
      (channelInverse (R := R) d) = 1 := by
  classical
  unfold channelInverse
  rw [simultaneousChannelResidue_single]
  simp [HasSimplePolesAlong, singletonDissection,
    cutExponent, AddMonoidAlgebra.one_def]

/-- A constant has no pole and hence zero residue along a nonempty singleton
cut. -/
theorem simultaneousChannelResidue_singleton_constant
    {n : ℕ} {R : Type*} [CommRing R] (d : Diagonal n) (c : R) :
    simultaneousChannelResidue (singletonDissection d)
      (AddMonoidAlgebra.single 0 c) = 0 := by
  classical
  rw [simultaneousChannelResidue_single]
  simp [HasSimplePolesAlong, singletonDissection]

/-- Nested residues agree with the direct residue on each Laurent monomial. -/
theorem simultaneousChannelResidue_nested_single {n : ℕ} {R : Type*}
    [Semiring R] (D E : Dissection n) (hDE : D ≤ E)
    (a : ChannelExponent n) (c : R) :
    simultaneousChannelResidue (dissectionDifference E D)
        (simultaneousChannelResidue D (AddMonoidAlgebra.single a c)) =
      simultaneousChannelResidue E (AddMonoidAlgebra.single a c) := by
  classical
  by_cases hE : HasSimplePolesAlong E a
  · have hnested := (hasSimplePolesAlong_nested D E hDE a).mpr hE
    calc
      _ = simultaneousChannelResidue (dissectionDifference E D)
          (AddMonoidAlgebra.single (a + cutExponent D) c) := by
        rw [simultaneousChannelResidue_single, if_pos hnested.1]
      _ = AddMonoidAlgebra.single
          ((a + cutExponent D) + cutExponent (dissectionDifference E D)) c := by
        rw [simultaneousChannelResidue_single, if_pos hnested.2]
      _ = AddMonoidAlgebra.single (a + cutExponent E) c := by
        apply congrArg (fun z => AddMonoidAlgebra.single z c)
        rw [add_assoc, cutExponent_add_difference D E hDE]
      _ = _ := by
        rw [simultaneousChannelResidue_single, if_pos hE]
  · have hnotnested : ¬(HasSimplePolesAlong D a ∧
        HasSimplePolesAlong (dissectionDifference E D)
          (a + cutExponent D)) := by
      intro h
      exact hE ((hasSimplePolesAlong_nested D E hDE a).mp h)
    by_cases hD : HasSimplePolesAlong D a
    · have hnew : ¬HasSimplePolesAlong (dissectionDifference E D)
          (a + cutExponent D) := fun h => hnotnested ⟨hD, h⟩
      simp [hE, hD, hnew, simultaneousChannelResidue]
    · simp [hE, hD, simultaneousChannelResidue]

/-- Simultaneous coefficient residue is additive in the Laurent
presentation. -/
theorem simultaneousChannelResidue_add {n : ℕ} {R : Type*} [Semiring R]
    (D : Dissection n) (f g : ChannelLaurentAlgebra R n) :
    simultaneousChannelResidue D (f + g) =
      simultaneousChannelResidue D f + simultaneousChannelResidue D g := by
  classical
  unfold simultaneousChannelResidue
  apply Finsupp.sum_add_index
  · intro a
    split_ifs <;> simp
  · intro a x y
    split_ifs <;> simp [AddMonoidAlgebra.single_add]

/-- Simultaneous residue as an additive homomorphism. -/
noncomputable def simultaneousChannelResidueAddHom {n : ℕ} {R : Type*}
    [Semiring R] (D : Dissection n) :
    ChannelLaurentAlgebra R n →+ ChannelLaurentAlgebra R n where
  toFun := simultaneousChannelResidue D
  map_zero' := by
    simp [simultaneousChannelResidue]
  map_add' := simultaneousChannelResidue_add D

/-- Nested-cut naturality holds on every finite Laurent expression, not only
on triangulation monomials. -/
theorem simultaneousChannelResidue_nested {n : ℕ} {R : Type*} [Semiring R]
    (D E : Dissection n) (hDE : D ≤ E)
    (f : ChannelLaurentAlgebra R n) :
    simultaneousChannelResidue (dissectionDifference E D)
        (simultaneousChannelResidue D f) =
      simultaneousChannelResidue E f := by
  let lhs := (simultaneousChannelResidueAddHom (R := R)
    (dissectionDifference E D)).comp (simultaneousChannelResidueAddHom D)
  let rhs := simultaneousChannelResidueAddHom (R := R) E
  have hhom : lhs = rhs := by
    apply AddMonoidAlgebra.addMonoidHom_ext
    intro a c
    exact simultaneousChannelResidue_nested_single D E hDE a c
  exact DFunLike.congr_fun hhom f

/-- Canonical quotient class of the Laurent residue of the global amplitude.
This is well-defined because the representative is fixed before projection; it
does not assert a residue operator on arbitrary quotient classes. -/
noncomputable def projectedPlanarResidueClass
    {V K : Type*} [AddCommGroup V] [CommRing K] {n : ℕ}
    {Q : EvenMomentumReadout V K} {P : MomentumConfiguration V n}
    (U : InvertiblePlanarChannelReadout V K Q P) (D : Dissection n) :
    EvaluatedPlanarKinematicRing U :=
  evaluatedPlanarKinematicProjection U
    (simultaneousChannelResidue D
      (combinatorialBiadjointAmplitude (n := n) (R := K)))

/-- Nested-cut naturality holds for the canonical projected residue classes,
although no residue operation exists on arbitrary evaluated quotient classes. -/
theorem projectedPlanarResidueClass_nested
    {V K : Type*} [AddCommGroup V] [CommRing K] {n : ℕ}
    {Q : EvenMomentumReadout V K} {P : MomentumConfiguration V n}
    (U : InvertiblePlanarChannelReadout V K Q P)
    (D E : Dissection n) (hDE : D ≤ E) :
    evaluatedPlanarKinematicProjection U
      (simultaneousChannelResidue (dissectionDifference E D)
        (simultaneousChannelResidue D
          (combinatorialBiadjointAmplitude (n := n) (R := K)))) =
      projectedPlanarResidueClass U E := by
  unfold projectedPlanarResidueClass
  rw [simultaneousChannelResidue_nested D E hDE]

/-- The channel-readout-evaluation kernel is not stable under coefficient residue:
a formal channel inverse and its evaluated constant represent the same evaluated
class but have different singleton residues. -/
theorem planarChannelReadoutEvaluation_kernel_not_residue_stable
    {V K : Type*} [AddCommGroup V] [CommRing K] [Nontrivial K] {n : ℕ}
    {Q : EvenMomentumReadout V K} {P : MomentumConfiguration V n}
    (U : InvertiblePlanarChannelReadout V K Q P) (d : Diagonal n) :
    ∃ f : ChannelLaurentAlgebra K n,
      planarChannelReadoutEvaluation U f = 0 ∧
      planarChannelReadoutEvaluation U
        (simultaneousChannelResidue (singletonDissection d) f) ≠ 0 := by
  let c := inverseChannelReadout U d
  let k : ChannelLaurentAlgebra K n := AddMonoidAlgebra.single 0 c
  refine ⟨channelInverse d - k, ?_, ?_⟩
  · rw [map_sub]
    change planarChannelReadoutEvaluation U (laurentInverseOn d) -
      planarChannelReadoutEvaluation U k = 0
    rw [planarChannelReadoutEvaluation_channelInverse]
    simp [k, c, inverseChannelReadout, planarChannelReadoutEvaluation,
      planarChannelReadoutEvaluation]
  · change planarChannelReadoutEvaluation U
      ((simultaneousChannelResidueAddHom (R := K) (singletonDissection d))
        (channelInverse d - k)) ≠ 0
    rw [map_sub]
    change planarChannelReadoutEvaluation U
      (simultaneousChannelResidue (singletonDissection d) (channelInverse d) -
        simultaneousChannelResidue (singletonDissection d) k) ≠ 0
    rw [simultaneousChannelResidue_singleton_channelInverse,
      simultaneousChannelResidue_singleton_constant]
    simp

/-- Exact criterion for a residue operator to descend to a source-derived
kinematic quotient. -/
def ResidueRespectsSourceKinematics {n : ℕ} {R K : Type*}
    [CommRing R] [CommRing K]
    (φ : ChannelLaurentAlgebra R n →+* K) (D : Dissection n) : Prop :=
  ∀ f g, sourceKinematicProjection φ f = sourceKinematicProjection φ g →
    sourceKinematicProjection φ (simultaneousChannelResidue D f) =
      sourceKinematicProjection φ (simultaneousChannelResidue D g)

/-- Consequently singleton coefficient residue does not descend to the
evaluated channel-readout quotient. -/
theorem not_residueRespectsEvaluatedPlanarKinematics
    {V K : Type*} [AddCommGroup V] [CommRing K] [Nontrivial K] {n : ℕ}
    {Q : EvenMomentumReadout V K} {P : MomentumConfiguration V n}
    (U : InvertiblePlanarChannelReadout V K Q P) (d : Diagonal n) :
    ¬ ResidueRespectsSourceKinematics
      (planarChannelReadoutEvaluation U) (singletonDissection d) := by
  intro hdesc
  rcases planarChannelReadoutEvaluation_kernel_not_residue_stable U d with
    ⟨f, hf, hres⟩
  have hfq : sourceKinematicProjection (planarChannelReadoutEvaluation U) f =
      sourceKinematicProjection (planarChannelReadoutEvaluation U) 0 := by
    rw [map_zero]
    apply (Ideal.Quotient.eq_zero_iff_mem).mpr
    exact (RingHom.mem_ker).mpr hf
  have hq := hdesc f 0 hfq
  have hz : simultaneousChannelResidue (singletonDissection d)
      (0 : ChannelLaurentAlgebra K n) = 0 :=
    (simultaneousChannelResidueAddHom (R := K)
      (singletonDissection d)).map_zero
  rw [hz, map_zero] at hq
  have hmem : simultaneousChannelResidue (singletonDissection d) f ∈
      RingHom.ker (planarChannelReadoutEvaluation U) :=
    (Ideal.Quotient.eq_zero_iff_mem).mp hq
  exact hres ((RingHom.mem_ker).mp hmem)

/-- Residue induced on a source-derived quotient once representative
independence has been proved. -/
noncomputable def descendedChannelResidue
    {n : ℕ} {R K : Type*} [CommRing R] [CommRing K]
    (φ : ChannelLaurentAlgebra R n →+* K) (D : Dissection n)
    (h : ResidueRespectsSourceKinematics φ D) :
    SourceKinematicRing φ → SourceKinematicRing φ :=
  Quotient.lift
    (fun f => sourceKinematicProjection φ (simultaneousChannelResidue D f))
    (by
      intro f g hfg
      exact h f g (Quotient.sound hfg))

@[simp] theorem descendedChannelResidue_projection
    {n : ℕ} {R K : Type*} [CommRing R] [CommRing K]
    (φ : ChannelLaurentAlgebra R n →+* K) (D : Dissection n)
    (h : ResidueRespectsSourceKinematics φ D)
    (f : ChannelLaurentAlgebra R n) :
    descendedChannelResidue φ D h (sourceKinematicProjection φ f) =
      sourceKinematicProjection φ (simultaneousChannelResidue D f) := rfl

/-- Nested-cut naturality remains equal after projection to every
source-derived kinematic quotient. This does not assert that either residue
operator descends without `ResidueRespectsSourceKinematics`. -/
theorem sourceKinematicProjection_residue_nested
    {n : ℕ} {R K : Type*} [CommRing R] [CommRing K]
    (φ : ChannelLaurentAlgebra R n →+* K)
    (D E : Dissection n) (hDE : D ≤ E)
    (f : ChannelLaurentAlgebra R n) :
    sourceKinematicProjection φ
        (simultaneousChannelResidue (dissectionDifference E D)
          (simultaneousChannelResidue D f)) =
      sourceKinematicProjection φ (simultaneousChannelResidue E f) := by
  rw [simultaneousChannelResidue_nested D E hDE f]

/-- When all three residue maps respect the source relations, nested-cut
naturality holds as equality of induced quotient operations. -/
theorem descendedChannelResidue_nested
    {n : ℕ} {R K : Type*} [CommRing R] [CommRing K]
    (φ : ChannelLaurentAlgebra R n →+* K)
    (D E : Dissection n) (hDE : D ≤ E)
    (hD : ResidueRespectsSourceKinematics φ D)
    (hDiff : ResidueRespectsSourceKinematics φ (dissectionDifference E D))
    (hE : ResidueRespectsSourceKinematics φ E)
    (x : SourceKinematicRing φ) :
    descendedChannelResidue φ (dissectionDifference E D) hDiff
        (descendedChannelResidue φ D hD x) =
      descendedChannelResidue φ E hE x := by
  refine Quotient.inductionOn x ?_
  intro f
  change descendedChannelResidue φ (dissectionDifference E D) hDiff
      (descendedChannelResidue φ D hD (sourceKinematicProjection φ f)) =
    descendedChannelResidue φ E hE (sourceKinematicProjection φ f)
  rw [descendedChannelResidue_projection φ D hD f]
  rw [descendedChannelResidue_projection φ
    (dissectionDifference E D) hDiff (simultaneousChannelResidue D f)]
  rw [descendedChannelResidue_projection φ E hE f]
  rw [simultaneousChannelResidue_nested D E hDE f]

/-- Additivity extends the residue operation over any finite sum. -/
theorem simultaneousChannelResidue_finset_sum {n : ℕ} {R : Type*} [Semiring R]
    {ι : Type*} (D : Dissection n) (s : Finset ι)
    (f : ι → ChannelLaurentAlgebra R n) :
    simultaneousChannelResidue D (∑ i ∈ s, f i) =
      ∑ i ∈ s, simultaneousChannelResidue D (f i) := by
  classical
  induction s using Finset.induction_on with
  | empty => simp [simultaneousChannelResidue]
  | @insert i s hi ih =>
      simp [hi, simultaneousChannelResidue_add, ih]

/-- On a dissection monomial, simultaneous residue selects exactly the
families containing `D` and removes precisely those selected channel inverses. -/
theorem simultaneousChannelResidue_monomialWeight {n : ℕ} {R : Type*}
    [CommSemiring R] (D T : Dissection n) :
    simultaneousChannelResidue D
        (monomialWeight (channelInverse (R := R)) T) =
      if D.1 ⊆ T.1 then
        AddMonoidAlgebra.single
          (diagonalFamilyExponent (T.1 \ D.1)) 1
      else 0 := by
  classical
  rw [show monomialWeight (channelInverse (R := R)) T =
    AddMonoidAlgebra.single (diagonalFamilyExponent T.1) 1 by
      exact channelInverse_prod T.1]
  rw [simultaneousChannelResidue_single]
  rw [hasSimplePolesAlong_diagonalFamilyExponent]
  split_ifs with h
  · rw [diagonalFamilyExponent_add_cutExponent D T.1 h]
  · rfl

/-- The simultaneous Laurent residue of the combinatorial amplitude is the
previously defined sum of residual triangulation weights. -/
theorem simultaneousChannelResidue_combinatorialBiadjointAmplitude
    {n : ℕ} {R : Type*} [CommSemiring R] (D : Dissection n) :
    simultaneousChannelResidue D
        (combinatorialBiadjointAmplitude (n := n) (R := R)) =
      residueAmplitude (channelInverse (R := R)) D := by
  classical
  rw [combinatorialBiadjointAmplitude_eq_triangulation_sum]
  rw [show (∑ T : Triangulation n,
      ∏ d ∈ T.1.1, channelInverse (R := R) d) =
      ∑ T ∈ (Finset.univ : Finset (Triangulation n)),
        monomialWeight (channelInverse (R := R)) T.1 by rfl]
  rw [simultaneousChannelResidue_finset_sum]
  simp_rw [simultaneousChannelResidue_monomialWeight]
  change (∑ T ∈ (Finset.univ : Finset (Triangulation n)),
    if D.1 ⊆ T.1.1 then
      AddMonoidAlgebra.single (diagonalFamilyExponent (T.1.1 \ D.1)) 1
    else 0) = _
  rw [← Finset.sum_filter]
  rw [Finset.sum_subtype
    (p := fun T : Triangulation n => D.1 ⊆ T.1.1)
    (Finset.univ.filter (fun T : Triangulation n => D.1 ⊆ T.1.1))
    (by intro T; simp)]
  unfold residueAmplitude residualWeight
  apply Finset.sum_congr rfl
  intro T _
  exact (channelInverse_prod (R := R) (T.1.1.1 \ D.1)).symm

/-- The canonical projected residue class factors into explicitly relabelled
standard lower-point amplitudes. -/
theorem projectedPlanarResidueClass_factorization_standardLowerPoint
    {V K : Type*} [AddCommGroup V] [CommRing K] {n : ℕ}
    {Q : EvenMomentumReadout V K} {P : MomentumConfiguration V n}
    (U : InvertiblePlanarChannelReadout V K Q P) (D : Dissection n) :
    projectedPlanarResidueClass U D =
      evaluatedPlanarKinematicProjection U
        (∏ r : OptionalSignatureRegion D,
          optionalSignatureRegionalLaurentEmbedding (R := K) r
            ((regionalStandardLaurentEquiv (R := K) (r := r)).symm
              (combinatorialBiadjointAmplitude
                (n := optionalSignatureRegionArity r) (R := K)))) := by
  unfold projectedPlanarResidueClass
  rw [simultaneousChannelResidue_combinatorialBiadjointAmplitude]
  exact congrArg (evaluatedPlanarKinematicProjection U)
    (residueAmplitude_factorization_standardLowerPoint D)

/-- Channel-readout evaluation transports the combinatorial residual sum to the
evaluated inverse-channel-weight residual sum. -/
theorem planarChannelReadoutEvaluation_residueAmplitude
    {V K : Type*} [AddCommGroup V] [CommRing K] {n : ℕ}
    {Q : EvenMomentumReadout V K} {P : MomentumConfiguration V n}
    (U : InvertiblePlanarChannelReadout V K Q P) (D : Dissection n) :
    planarChannelReadoutEvaluation U
        (residueAmplitude (channelInverse (R := K)) D) =
      residueAmplitude (inverseChannelReadout U) D := by
  classical
  unfold residueAmplitude residualWeight
  simp_rw [map_sum, map_prod]
  apply Finset.sum_congr rfl
  intro T _
  apply Finset.prod_congr rfl
  intro d hd
  exact planarChannelReadoutEvaluation_eq_inverseChannelReadout U d

/-- Evaluated residue factorization into canonical standard lower-point
amplitudes, obtained solely by channel-readout evaluation of the explicit
relabeling diagram. -/
theorem evaluatedResidueAmplitude_factorization_standardLowerPoint
    {V K : Type*} [AddCommGroup V] [CommRing K] {n : ℕ}
    {Q : EvenMomentumReadout V K} {P : MomentumConfiguration V n}
    (U : InvertiblePlanarChannelReadout V K Q P) (D : Dissection n) :
    residueAmplitude (inverseChannelReadout U) D =
      planarChannelReadoutEvaluation U
        (∏ r : OptionalSignatureRegion D,
          optionalSignatureRegionalLaurentEmbedding (R := K) r
            ((regionalStandardLaurentEquiv (R := K) (r := r)).symm
              (combinatorialBiadjointAmplitude
                (n := optionalSignatureRegionArity r) (R := K)))) := by
  rw [← planarChannelReadoutEvaluation_residueAmplitude U D]
  exact congrArg (planarChannelReadoutEvaluation U)
    (residueAmplitude_factorization_standardLowerPoint D)

/-- The evaluated Laurent residue factors over the canonical regions. -/
theorem planarChannelReadoutEvaluation_residue_factorization
    {V K : Type*} [AddCommGroup V] [CommRing K] {n : ℕ}
    {Q : EvenMomentumReadout V K} {P : MomentumConfiguration V n}
    (U : InvertiblePlanarChannelReadout V K Q P) (D : Dissection n) :
    planarChannelReadoutEvaluation U
      (simultaneousChannelResidue D
        (combinatorialBiadjointAmplitude (n := n) (R := K))) =
      ∏ r, regionalAmplitude (inverseChannelReadout U)
        (canonicalRegionDecomposition D) r := by
  rw [simultaneousChannelResidue_combinatorialBiadjointAmplitude]
  rw [planarChannelReadoutEvaluation_residueAmplitude]
  exact evaluatedResidueAmplitude_factorization U D

/-- Nested-cut naturality survives channel-readout evaluation. -/
theorem planarChannelReadoutEvaluation_nested_residue
    {V K : Type*} [AddCommGroup V] [CommRing K] {n : ℕ}
    {Q : EvenMomentumReadout V K} {P : MomentumConfiguration V n}
    (U : InvertiblePlanarChannelReadout V K Q P)
    (D E : Dissection n) (hDE : D ≤ E) :
    planarChannelReadoutEvaluation U
      (simultaneousChannelResidue (dissectionDifference E D)
        (simultaneousChannelResidue D
          (combinatorialBiadjointAmplitude (n := n) (R := K)))) =
    planarChannelReadoutEvaluation U
      (simultaneousChannelResidue E
        (combinatorialBiadjointAmplitude (n := n) (R := K))) := by
  rw [simultaneousChannelResidue_nested D E hDE]

/-- The evaluated iterated residue therefore equals the evaluated product over
the canonical regions of the refined dissection. -/
theorem planarChannelReadoutEvaluation_nested_residue_factorization
    {V K : Type*} [AddCommGroup V] [CommRing K] {n : ℕ}
    {Q : EvenMomentumReadout V K} {P : MomentumConfiguration V n}
    (U : InvertiblePlanarChannelReadout V K Q P)
    (D E : Dissection n) (hDE : D ≤ E) :
    planarChannelReadoutEvaluation U
      (simultaneousChannelResidue (dissectionDifference E D)
        (simultaneousChannelResidue D
          (combinatorialBiadjointAmplitude (n := n) (R := K)))) =
      ∏ r, regionalAmplitude (inverseChannelReadout U)
        (canonicalRegionDecomposition E) r := by
  rw [simultaneousChannelResidue_nested D E hDE]
  exact planarChannelReadoutEvaluation_residue_factorization U E

/-- Forgetting part of a nested dissection sends an optional diagonal for
`E` to the same diagonal viewed as optional for `D`. -/
def OptionalDiagonal.forgetNested {n : ℕ} {D E : Dissection n}
    (hDE : D ≤ E) (x : OptionalDiagonal E) : OptionalDiagonal D :=
  ⟨x.1, fun hxD => x.2.1 (hDE hxD), by
    intro c hc
    exact x.2.2 c (hDE hc)⟩

/-- Every newly introduced cut has a canonical address in the decomposition of
`D`; this names the affected old region without adding a choice. -/
def newCutAsOptional {n : ℕ} {D E : Dissection n} (hDE : D ≤ E)
    (d : ↥(dissectionDifference E D).1) : OptionalDiagonal D :=
  ⟨d.1, (Finset.mem_sdiff.mp d.2).2, by
    intro c hc
    have hdE : d.1 ∈ E.1 := (Finset.mem_sdiff.mp d.2).1
    by_cases hcd : c = d.1
    · subst c
      intro hcross
      rcases hcross with hcross | hcross
      · exact lt_irrefl _ hcross.1
      · exact lt_irrefl _ hcross.1
    · intro hcross
      exact E.2 (hDE hc) hdE hcd ((crosses_symmetric).mp hcross)⟩

/-- Compatibility data making an `E`-decomposition a refinement of a
`D`-decomposition. It records the parent old region of every refined region and
requires regional addresses of surviving optional diagonals to commute. -/
structure NestedRegionDecomposition {n : ℕ} {D E : Dissection n}
    (hDE : D ≤ E) (regionsD : RegionDecomposition D)
    (regionsE : RegionDecomposition E) where
  parentRegion : regionsE.Region → regionsD.Region
  address_natural : ∀ x : OptionalDiagonal E,
    parentRegion (regionsE.regionOf x) =
      regionsD.regionOf (OptionalDiagonal.forgetNested hDE x)

/-- The old region affected by one newly introduced cut. -/
def NestedRegionDecomposition.affectedRegion {n : ℕ} {D E : Dissection n}
    {hDE : D ≤ E} {regionsD : RegionDecomposition D}
    {regionsE : RegionDecomposition E}
    (_nested : NestedRegionDecomposition hDE regionsD regionsE)
    (d : ↥(dissectionDifference E D).1) : regionsD.Region :=
  regionsD.regionOf (newCutAsOptional hDE d)

/-- The new cuts localized in one old region. -/
noncomputable def NestedRegionDecomposition.affectedCuts {n : ℕ}
    {D E : Dissection n} {hDE : D ≤ E}
    {regionsD : RegionDecomposition D} {regionsE : RegionDecomposition E}
    (nested : NestedRegionDecomposition hDE regionsD regionsE)
    (r : regionsD.Region) : Dissection n := by
  classical
  exact ⟨(dissectionDifference E D).1.filter (fun d =>
      ∃ hd : d ∈ (dissectionDifference E D).1,
        nested.affectedRegion ⟨d, hd⟩ = r),
    isDissection_subset (dissectionDifference E D).2 (by
      intro d hd
      exact (Finset.mem_filter.mp hd).1)⟩

/-- Membership in an affected-region cut family has the expected two
components: it is a new cut and its canonical old-region address is `r`. -/
theorem NestedRegionDecomposition.mem_affectedCuts {n : ℕ}
    {D E : Dissection n} {hDE : D ≤ E}
    {regionsD : RegionDecomposition D} {regionsE : RegionDecomposition E}
    (nested : NestedRegionDecomposition hDE regionsD regionsE)
    (r : regionsD.Region) (d : Diagonal n) :
    d ∈ (nested.affectedCuts r).1 ↔
      ∃ hd : d ∈ (dissectionDifference E D).1,
        nested.affectedRegion ⟨d, hd⟩ = r := by
  classical
  simp [NestedRegionDecomposition.affectedCuts]

/-- New cuts whose affected old region belongs to a selected finite family of
old regions. This supplies cumulative stages for an iterated regional residue. -/
noncomputable def NestedRegionDecomposition.affectedCutsForRegions {n : ℕ}
    {D E : Dissection n} {hDE : D ≤ E}
    {regionsD : RegionDecomposition D} {regionsE : RegionDecomposition E}
    (nested : NestedRegionDecomposition hDE regionsD regionsE)
    (q : Finset regionsD.Region) : Dissection n := by
  classical
  exact ⟨(dissectionDifference E D).1.filter (fun d =>
      ∃ hd : d ∈ (dissectionDifference E D).1,
        nested.affectedRegion ⟨d, hd⟩ ∈ q),
    isDissection_subset (dissectionDifference E D).2 (by
      intro d hd
      exact (Finset.mem_filter.mp hd).1)⟩

/-- Enlarging the selected old-region family enlarges the cumulative induced
cut dissection. -/
theorem NestedRegionDecomposition.affectedCutsForRegions_mono {n : ℕ}
    {D E : Dissection n} {hDE : D ≤ E}
    {regionsD : RegionDecomposition D} {regionsE : RegionDecomposition E}
    (nested : NestedRegionDecomposition hDE regionsD regionsE)
    {q q' : Finset regionsD.Region} (hqq' : q ⊆ q') :
    nested.affectedCutsForRegions q ≤ nested.affectedCutsForRegions q' := by
  classical
  intro d hd
  change d ∈ (dissectionDifference E D).1.filter _ at hd ⊢
  rw [Finset.mem_filter] at hd ⊢
  exact ⟨hd.1, hd.2.imp fun hcut hr => hqq' hr⟩

/-- Selecting all old regions recovers the complete new-cut dissection. -/
theorem NestedRegionDecomposition.affectedCutsForRegions_univ {n : ℕ}
    {D E : Dissection n} {hDE : D ≤ E}
    {regionsD : RegionDecomposition D} {regionsE : RegionDecomposition E}
    (nested : NestedRegionDecomposition hDE regionsD regionsE) :
    nested.affectedCutsForRegions Finset.univ = dissectionDifference E D := by
  classical
  apply Subtype.ext
  ext d
  simp [NestedRegionDecomposition.affectedCutsForRegions]

/-- A singleton cumulative stage is the cut family of that affected region. -/
theorem NestedRegionDecomposition.affectedCutsForRegions_singleton {n : ℕ}
    {D E : Dissection n} {hDE : D ≤ E}
    {regionsD : RegionDecomposition D} {regionsE : RegionDecomposition E}
    (nested : NestedRegionDecomposition hDE regionsD regionsE)
    (r : regionsD.Region) :
    nested.affectedCutsForRegions {r} = nested.affectedCuts r := by
  classical
  apply Subtype.ext
  ext d
  simp [NestedRegionDecomposition.affectedCutsForRegions,
    NestedRegionDecomposition.affectedCuts]

/-- The new cuts added between two cumulative regional stages are exactly
those assigned to the set difference of their region indices. -/
theorem NestedRegionDecomposition.difference_affectedCutsForRegions {n : ℕ}
    {D E : Dissection n} {hDE : D ≤ E}
    {regionsD : RegionDecomposition D} {regionsE : RegionDecomposition E}
    [DecidableEq regionsD.Region]
    (nested : NestedRegionDecomposition hDE regionsD regionsE)
    (q q' : Finset regionsD.Region) :
    dissectionDifference (nested.affectedCutsForRegions q')
        (nested.affectedCutsForRegions q) =
      nested.affectedCutsForRegions (q' \ q) := by
  classical
  apply Subtype.ext
  ext d
  simp only [dissectionDifference, Finset.mem_sdiff]
  simp only [NestedRegionDecomposition.affectedCutsForRegions,
    Finset.mem_filter]
  constructor
  · rintro ⟨⟨hd, ⟨hd', hrq'⟩⟩, hnq⟩
    refine ⟨hd, ⟨hd, ?_⟩⟩
    rw [Finset.mem_sdiff]
    exact ⟨hrq', fun hrq => hnq ⟨hd, ⟨hd, hrq⟩⟩⟩
  · rintro ⟨hd, ⟨hd', hr⟩⟩
    rw [Finset.mem_sdiff] at hr
    exact ⟨⟨hd, ⟨hd, hr.1⟩⟩,
      fun hq => hr.2 hq.2.choose_spec⟩

/-- Residues compose between arbitrary cumulative affected-region stages. -/
theorem NestedRegionDecomposition.residue_affectedCutsForRegions {n : ℕ}
    {R : Type*} [Semiring R]
    {D E : Dissection n} {hDE : D ≤ E}
    {regionsD : RegionDecomposition D} {regionsE : RegionDecomposition E}
    [DecidableEq regionsD.Region]
    (nested : NestedRegionDecomposition hDE regionsD regionsE)
    {q q' : Finset regionsD.Region} (hqq' : q ⊆ q')
    (f : ChannelLaurentAlgebra R n) :
    simultaneousChannelResidue (nested.affectedCutsForRegions (q' \ q))
        (simultaneousChannelResidue (nested.affectedCutsForRegions q) f) =
      simultaneousChannelResidue (nested.affectedCutsForRegions q') f := by
  rw [← nested.difference_affectedCutsForRegions q q']
  exact simultaneousChannelResidue_nested
    (nested.affectedCutsForRegions q)
    (nested.affectedCutsForRegions q')
    (nested.affectedCutsForRegions_mono hqq') f

/-- Processing one previously unprocessed old region is one exact step of the
cumulative residue. -/
theorem NestedRegionDecomposition.residue_insert_region {n : ℕ}
    {R : Type*} [Semiring R]
    {D E : Dissection n} {hDE : D ≤ E}
    {regionsD : RegionDecomposition D} {regionsE : RegionDecomposition E}
    [DecidableEq regionsD.Region]
    (nested : NestedRegionDecomposition hDE regionsD regionsE)
    (q : Finset regionsD.Region) (r : regionsD.Region) (hr : r ∉ q)
    (f : ChannelLaurentAlgebra R n) :
    simultaneousChannelResidue (nested.affectedCuts r)
        (simultaneousChannelResidue (nested.affectedCutsForRegions q) f) =
      simultaneousChannelResidue
        (nested.affectedCutsForRegions (insert r q)) f := by
  have hq : q ⊆ insert r q := Finset.subset_insert r q
  have h := nested.residue_affectedCutsForRegions hq f
  rw [show insert r q \ q = {r} by ext x; simp [hr]] at h
  rw [nested.affectedCutsForRegions_singleton r] at h
  exact h

/-- Processing every old region recovers the residue in all new channels. -/
theorem NestedRegionDecomposition.residue_all_affected_regions {n : ℕ}
    {R : Type*} [Semiring R]
    {D E : Dissection n} {hDE : D ≤ E}
    {regionsD : RegionDecomposition D} {regionsE : RegionDecomposition E}
    (nested : NestedRegionDecomposition hDE regionsD regionsE)
    (f : ChannelLaurentAlgebra R n) :
    simultaneousChannelResidue
        (nested.affectedCutsForRegions Finset.univ) f =
      simultaneousChannelResidue (dissectionDifference E D) f := by
  rw [nested.affectedCutsForRegions_univ]

/-- Nested-cut naturality expressed through the exhaustive family of cuts
localized in the affected old regions. -/
theorem NestedRegionDecomposition.residue_after_all_affected_regions {n : ℕ}
    {R : Type*} [Semiring R]
    {D E : Dissection n} {hDE : D ≤ E}
    {regionsD : RegionDecomposition D} {regionsE : RegionDecomposition E}
    (nested : NestedRegionDecomposition hDE regionsD regionsE)
    (f : ChannelLaurentAlgebra R n) :
    simultaneousChannelResidue
        (nested.affectedCutsForRegions Finset.univ)
        (simultaneousChannelResidue D f) =
      simultaneousChannelResidue E f := by
  rw [nested.affectedCutsForRegions_univ]
  exact simultaneousChannelResidue_nested D E hDE f

/-- Distinct old regions receive disjoint families of new cuts. -/
theorem NestedRegionDecomposition.affectedCuts_disjoint {n : ℕ}
    {D E : Dissection n} {hDE : D ≤ E}
    {regionsD : RegionDecomposition D} {regionsE : RegionDecomposition E}
    (nested : NestedRegionDecomposition hDE regionsD regionsE)
    {r s : regionsD.Region} (hrs : r ≠ s) :
    Disjoint (nested.affectedCuts r).1 (nested.affectedCuts s).1 := by
  classical
  apply Finset.disjoint_left.mpr
  intro d hdr hds
  rcases (nested.mem_affectedCuts r d).mp hdr with ⟨hd, hr⟩
  rcases (nested.mem_affectedCuts s d).mp hds with ⟨hd', hs⟩
  apply hrs
  rw [← hr, ← hs]

/-- The union of all affected-region cut families is exactly `E \ D`. -/
theorem NestedRegionDecomposition.biUnion_affectedCuts {n : ℕ}
    {D E : Dissection n} {hDE : D ≤ E}
    {regionsD : RegionDecomposition D} {regionsE : RegionDecomposition E}
    (nested : NestedRegionDecomposition hDE regionsD regionsE) :
    Finset.univ.biUnion (fun r => (nested.affectedCuts r).1) =
      (dissectionDifference E D).1 := by
  classical
  ext d
  constructor
  · intro hd
    rcases Finset.mem_biUnion.mp hd with ⟨r, _, hdr⟩
    exact (nested.mem_affectedCuts r d).mp hdr |>.choose
  · intro hd
    apply Finset.mem_biUnion.mpr
    let r := nested.affectedRegion ⟨d, hd⟩
    exact ⟨r, Finset.mem_univ r,
      (nested.mem_affectedCuts r d).mpr ⟨hd, rfl⟩⟩

/-- The induced cut families partition the total exponent shift for
`E \ D`. -/
theorem NestedRegionDecomposition.cutExponent_difference_eq_sum_affected
    {n : ℕ} {D E : Dissection n} {hDE : D ≤ E}
    {regionsD : RegionDecomposition D} {regionsE : RegionDecomposition E}
    (nested : NestedRegionDecomposition hDE regionsD regionsE) :
    cutExponent (dissectionDifference E D) =
      ∑ r, cutExponent (nested.affectedCuts r) := by
  classical
  ext d
  by_cases hd : d ∈ (dissectionDifference E D).1
  · let r := nested.affectedRegion ⟨d, hd⟩
    simp [cutExponent, NestedRegionDecomposition.affectedCuts,
      Finsupp.single_apply, hd]
  · simp [cutExponent, NestedRegionDecomposition.affectedCuts,
      Finsupp.single_apply, hd]

/-- Regional factorization is coherent under nested cuts at the embedded
Laurent-expression level: factor first over `D` and then take the residue in
the new channels, or factor directly over `E`. -/
theorem regionalAmplitude_nested_coherence {n : ℕ} {R : Type*}
    [CommSemiring R] (D E : Dissection n) (hDE : D ≤ E)
    (regionsD : RegionDecomposition D) (regionsE : RegionDecomposition E) :
    simultaneousChannelResidue (dissectionDifference E D)
        (∏ r, regionalAmplitude (channelInverse (R := R)) regionsD r) =
      ∏ s, regionalAmplitude (channelInverse (R := R)) regionsE s := by
  rw [← residueAmplitude_factorization_canonical
    (channelInverse (R := R)) D regionsD]
  rw [← simultaneousChannelResidue_combinatorialBiadjointAmplitude D]
  rw [simultaneousChannelResidue_nested D E hDE]
  rw [simultaneousChannelResidue_combinatorialBiadjointAmplitude E]
  exact residueAmplitude_factorization_canonical
    (channelInverse (R := R)) E regionsE

/-- Componentwise regional coherence: first factor over `D`, then process
all cut families localized in affected `D`-regions, or factor directly over
`E`. -/
theorem affectedRegionalAmplitude_nested_coherence {n : ℕ} {R : Type*}
    [CommSemiring R] {D E : Dissection n} {hDE : D ≤ E}
    {regionsD : RegionDecomposition D} {regionsE : RegionDecomposition E}
    (nested : NestedRegionDecomposition hDE regionsD regionsE) :
    simultaneousChannelResidue
        (nested.affectedCutsForRegions Finset.univ)
        (∏ r, regionalAmplitude (channelInverse (R := R)) regionsD r) =
      ∏ s, regionalAmplitude (channelInverse (R := R)) regionsE s := by
  rw [nested.affectedCutsForRegions_univ]
  exact regionalAmplitude_nested_coherence D E hDE regionsD regionsE

/-- A presented amplitude factors through canonical regions and explicit
standard lower-point amplitudes. No physical provenance or regional
identification interface is supplied. -/
theorem biadjointPresentationResidue_factorization {n : ℕ} {R : Type*}
    [CommSemiring R] (D : Dissection n)
    (global : BiadjointAmplitudePresentation n R) :
    simultaneousChannelResidue D global.presentedAmplitude =
      ∏ r : OptionalSignatureRegion D,
        optionalSignatureRegionalLaurentEmbedding (R := R) r
          ((regionalStandardLaurentEquiv (R := R) (r := r)).symm
            (combinatorialBiadjointAmplitude
              (n := optionalSignatureRegionArity r) (R := R))) := by
  rw [global.triangulation_expansion]
  rw [simultaneousChannelResidue_combinatorialBiadjointAmplitude D]
  exact residueAmplitude_factorization_standardLowerPoint D

/-- Channel-readout evaluation of the presented factorization. This asserts only
the algebraic evaluation supplied by `U`, not a physical interpretation. -/
theorem biadjointPresentationChannelReadoutResidue_factorization
    {V K : Type*} [AddCommGroup V] [CommRing K] {n : ℕ}
    {Q : EvenMomentumReadout V K} {P : MomentumConfiguration V n}
    (U : InvertiblePlanarChannelReadout V K Q P) (D : Dissection n)
    (global : BiadjointAmplitudePresentation n K) :
    planarChannelReadoutEvaluation U
      (simultaneousChannelResidue D global.presentedAmplitude) =
    planarChannelReadoutEvaluation U
      (∏ r : OptionalSignatureRegion D,
        optionalSignatureRegionalLaurentEmbedding (R := K) r
          ((regionalStandardLaurentEquiv (R := K) (r := r)).symm
            (combinatorialBiadjointAmplitude
              (n := optionalSignatureRegionArity r) (R := K)))) := by
  exact congrArg (planarChannelReadoutEvaluation U)
    (biadjointPresentationResidue_factorization D global)

/-- The genuine simplicial-set nerve of the generic polygon-dissection order.
Faces and degeneracies are inherited from the simplex-category functor. -/
def nerve (n : ℕ) : SSet := CategoryTheory.nerve (Dissection n)

/-- Polygon-dissection nerves satisfy strict Segal composition. -/
instance nerveIsStrictSegal (n : ℕ) : SSet.IsStrictSegal (nerve n) :=
  CategoryTheory.Nerve.isStrictSegal (Dissection n)

/-- Rezk completeness for the refinement order: invertible refinements force
literal equality by antisymmetry. -/
theorem iso_nonempty_iff_eq {n : ℕ} (D E : Dissection n) :
    Nonempty (D ≅ E) ↔ D = E := by
  constructor
  · rintro ⟨i⟩
    exact le_antisymm i.hom.le i.inv.le
  · rintro rfl
    exact ⟨Iso.refl D⟩

end Marici.Polygon
