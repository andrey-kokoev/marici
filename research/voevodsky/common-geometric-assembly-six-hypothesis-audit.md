# Common geometric assembly: six-hypothesis test ledger

## Frozen targets and order

Targets: proton twelve centroid-edge triangles on its tetrahedral boundary;
neutron candidate six-panel belt, with each panel split into three centroid-edge
triangles; electron displayed regular 4-simplex with ABCD retained as attachment
cell. The electron spinor coefficient store is only on ABCD, not the entire
4-simplex. Do not silently substitute the alternative bipyramid for the belt.

Test order: H4 symmetry, H2 links/cones, H5 constraints, H3 gluing,
H6 compatibility refinement, H1 dimensional succession.

| Hypothesis | Status |
|---|---|
| H4 Symmetry-generated multi-orbit assembly | Iteration 1 tested geometrically; partial result below |
| H2 Common coning with source-dependent link | Iteration 2 tested; reproduces constituents up to subdivision, but does not generate the links |
| H5 Minimal-dimensional constraint realization | Iteration 3 tested; naive rule rejected by exact flat/folded counterexamples; symmetry-enriched metric closure survives |
| H3 Oriented interface matching | Iteration 4 tested; exact gluing succeeds with labels and cell inventories, but does not determine those inventories |
| H6 Common refinement of competing descriptions | Iteration 5 tested; ordinary refinement insufficient, higher filling witnesses distinguished explicitly |
| H1 Dimension succession and promotion | Iteration 6 tested; no intrinsic 4D reset, and source-supported completion requires symmetry and protected interfaces |

## Iteration 1: H4 symmetry-orbit test

Fresh source reads are hashed in `results/common_assembly_symmetry.json`.
`checkers/check_common_assembly_symmetry.py` applies one operation to all targets:

1. Recover exact affine coordinates and rank from squared-distance Gram data.
2. Enumerate vertex permutations preserving distances, orientation and cells.
3. Partition barycentrically represented cells into orbits.
4. Regenerate cells from one representative per orbit and compare all shared
   codimension-one interfaces exactly.
5. Repeat with attachment interfaces fixed setwise.

The belt metric correctly uses physical x=sqrt(3)X, not the unweighted stored
coordinate triple. The electron metric is the full four-dimensional metric,
not its projected view. Its ten squared edge lengths are 8, directly from the
retained ABCD coordinates and E=(0,0,0,sqrt(5)) in the source note.

| Target | Proper symmetries | Unmarked cell orbits | Attachment-preserving symmetries | Marked cell orbits |
|---|---:|---|---:|---|
| Proton | 12 | 12 | 3 | 3+3+3+3 |
| Neutron belt | 6 | 6+6+6 | 3 | 3+3+3+3+3+3 |
| Electron pentachoron | 60 | 5 | 12 | 1+4 |

Marks: proton ABC face; neutron upper and lower rims separately; electron ABCD
cell. Whether to impose those marks during construction or only afterward is a
real model choice. They cannot be silently dropped when claiming preservation
of the attachment data.

All three regenerated cell adjacency graphs are connected. Their shared
interface counts are respectively 18, 24 and 10. In the unmarked belt, each pair
of its three symmetry orbits has six shared interfaces. Thus the geometric belt
is connected even though symmetry transport alone does not connect its orbits.

### Disposition

- A common multi-orbit operation reconstructs the supplied targets and seams.
- A common **single-orbit** construction fails for the belt, and for every
  attachment-marked target.
- This is an inverse test using target metrics and cell lists. It is NOT a
  derivation of those targets from the original minimal arrow records.
- Orbit representatives and inter-orbit source relations remain to be derived.
- No coefficient transport between distinct orbits, neutron arrow count or
  five-cell electron spinor calculation was supplied by this test.

### Reproduction

    python research/voevodsky/checkers/check_common_assembly_symmetry.py

Fresh run passed the exact cell/seam reconstruction, group closure, rank and
orbit checks. Receipt includes hashes of all input records and the checker.

## Iteration 2: H2 common coning and center links

Freshly reread the audit, target loader, and belt constituent store. Executed
`checkers/check_common_assembly_cones.py` on the same targets. Receipt:
`results/common_assembly_cones.json`, including source and implementation hashes.

The common operation is K -> O*K. The checker computes rational boundary-matrix
ranks, not merely Euler characteristics, and extracts the apex link directly
from the resulting complex. It verifies the exact boundary formula
boundary(O*K) = K union O*boundary(K) at the exposed-facet level.

| Target | Link at center | Rational Betti numbers of link | Coarse -> refined cone cells |
|---|---|---|---|
| Proton | 2-sphere | (1,0,1) | 4 -> 12 tetrahedra |
| Neutron belt | Annulus | (1,1,0) | 6 -> 18 tetrahedra |
| Electron pentachoron | 3-sphere | (1,0,0,1) | 5 -> 5 four-dimensional simplices |

The two-dimensional links have connected vertex links explicitly checked as
circles or intervals. The belt boundary has two circle components, Betti
numbers (2,2). The electron link is the full boundary of the source 4-simplex.

The recovered coarse proton and belt cones match every constituent vertex set
in `four_six_center_cones.json`. Positive exact cone determinants show that the
centroid subdivisions preserve each parent's volume. The electron construction
adds a barycenter and is a stellar subdivision of its 4-simplex, NOT literally
the original five-vertex cell list.

### Discriminating findings

1. **The belt center is not a manifold point.** Its local rational homology has
   H2=Q and H3=0, rather than the H3=Q of an interior point in a 3-ball. The two
   omitted cap cones share this apex. Filling them changes the center link from
   annulus to 2-sphere; the checker verifies that control exactly.
2. **All three cones collapse to a dot.** Explicit elementary simplicial
   collapses to the apex are checked and retained in the receipt: 38, 60, and
   30 pairs respectively in these triangulations. These are not proposed
   physical periods or primitive operation counts. This establishes that
   contractibility/point reduction alone cannot select one particle or a
   special dimensional reset. Their differing links and retained structure
   must not be discarded in such a promotion.
3. The belt cone's exposed boundary has Betti numbers (1,1,1), not those of a
   sphere. A common rule that always returns a filled simplex or ball therefore
   fails for the stored six-cone belt.

### Disposition

Common coning survives as an exact geometric construction, up to the explicitly
checked subdivisions. It does not explain why the three source links differ:
the complete target links were inputs. No source-arrow minimality or coefficient
count follows. The operation is more general than simplex completion, and its
non-manifold belt output is essential, not a numerical discrepancy to erase.

### Reproduction

    python research/voevodsky/checkers/check_common_assembly_cones.py

## Iteration 3: H5 metric constraints and minimal dimension

Freshly read the audit, metric implementation, six-arrow input, and electron
attachment definition. Executed `checkers/check_common_assembly_constraints.py`.
The common operation forms a rational Gram matrix from squared distances,
tests all principal minors for positive semidefiniteness, and computes exact
rank. Incomplete constraints are tested with explicit alternative completions;
the missing entries are not silently copied from the target.

### Proton: five seed-edge lengths do not fix the sixth

The six directed source arrows supply only five undirected edges, missing CD.
Even granting squared length 8 to every seed edge, t=CD^2 is unconstrained by
those five lengths. The anchored Gram determinant is 2*t*(24-t).

Fresh exact examples:

| CD^2 | Euclidean? | Affine dimension |
|---:|---|---:|
| 4 | yes | 3 |
| 8 (target) | yes | 3 |
| 12 | yes | 3 |
| 24 | yes, four distinct vertices | 2 |
| 25 | no | — |

Thus a bare minimum-dimension rule admits a flat competitor rather than forcing
the regular tetrahedron. This does not contradict the original constructor,
which additionally interprets its cycle permutations as rigid symmetries.

**Positive control:** derive the two three-cycles from the source arrows,
declare their vertex permutations to preserve distances, and propagate the five
edge constraints. This derives CD^2=8 and the full regular tetrahedral metric,
without reading the missing length. The symmetry interpretation is the crucial
extra rule, not a consequence of directed incidence alone.

### Electron: equal lengths force 4D; incidence/equidistance alone do not

Keep the regular ABCD base of squared edge length 8. Let s be the common squared
distance from E to the four base vertices. Its height satisfies h^2=s-3, and the
four-dimensional Gram determinant is 256*(s-3).

Checked s=2 (not Euclidean), s=3 (distinct fifth vertex at the center, rank 3),
s=4,8,12 (rank 4). Requiring all ten edges to have squared length 8 forces
h^2=5 and rank 4, exactly recovering the stored pentachoron metric up to isometry.
Merely requiring E to be equidistant, or joining E to all base vertices, does not.

### Neutron: local rigidity does not give global selection

Within the stored two-parallel-rim family, rim edge squares are 3 and side edge
squares are 1+g^2. Exact trials at gap g=1/2,7/10,1 preserve incidence and rim
lengths but change the side lengths. The stored gap 7/10 is therefore not fixed
by incidence and rim lengths alone.

Fix all twelve surface-edge lengths at the target values. The rigidity matrix
has rank 12=3*6-6: there are no infinitesimal flexes beyond rigid motions.
Nevertheless an exact distinct folded realization exists. Reflect U0 across
its four-neighbor plane y+g*z=0. At g=7/10, in the stored scaled coordinates:

    U0=(0,7/20,1) -> (0,-3157/2980,2/149).

Every one of the twelve edge lengths is unchanged; the missing opposite-pair
squared distance U0-L0 changes from 449/100 to 22801/14900. All vertices remain
distinct, rank stays three, and all six side triangles are nondegenerate.

The first test incorrectly predicted that an unoriented supporting-plane check
would reject this fold; execution disproved that assertion. All six side planes
remain supporting. What fails is **retained outward orientation**: only three
of the six retain it, and neither rim plane is supporting anymore. This makes
orientation and interface data substantive constraints, not display decoration.

The target's convex hull has eight facets, whereas the stored belt retains six.
Even after geometry is selected, the two rims must remain protected/unfilled;
convex-hull completion alone would produce the wrong complex.

### Disposition

- Full supplied metrics recover dimensions 3,3,4, as expected but not explanatory.
- Incidence/edge-length constraints plus minimum dimension are insufficient.
- Metric closure enriched by the source's symmetries recovers the proton metric.
- Full equal-edge constraints force the electron's fourth dimension.
- The belt needs a global orientation/interface selection beyond local rigidity.
- These are exact witnesses, not an exhaustive classification of all belt
  realizations. No coefficient or return-arrow counts were inferred.

### Reproduction

    python research/voevodsky/checkers/check_common_assembly_constraints.py

Receipt: `results/common_assembly_constraints.json`, including inputs and
implementation hashes. Fresh rerun passed all metric and counterexample checks.

## Iteration 4: H3 labelled oriented interface gluing

Freshly read the audit and belt face/constituent records. Executed
`checkers/check_common_assembly_gluing.py`. Receipt:
`results/common_assembly_gluing.json`, with source and implementation hashes.

The same gluer starts with disjoint local vertex occurrences in oriented cells.
For each codimension-one face it compares retained vertex labels and induced
boundary signs. Opposite signs admit identification of matching vertex
occurrences; equal signs are rejected. A union-find quotient is actually formed
before comparison with the target. Geometry is used to orient the test fixtures,
not to choose identifications inside the gluer. No particle label is an argument.

| Target | Cells supplied | Matched interfaces | Exposed interfaces | Exact quotient |
|---|---:|---:|---:|---|
| Proton | 12 triangles | 18 edges | 0 | recovered |
| Neutron belt | 18 triangles | 24 edges | 6 rim edges | recovered |
| Electron pentachoron boundary | 5 tetrahedra | 10 triangles | 0 | recovered |

All dual graphs are connected. For each fixed inventory the compatible cell
orientations are determined up to one global reversal. Flipping one cell alone
is rejected, producing respectively 3, 2 and 4 interface orientation conflicts.
This tests orientation as an admission condition, not a visualization choice.

### What is and is not uniquely selected

With labels and the cell inventory fixed, gluing recovers the targets exactly.
Without labels, metric compatibility permits many more local interface pairs:

| Target | Metric-compatible facet-occurrence pairs | Actual labelled matches |
|---|---:|---:|
| Proton | 330 | 18 |
| Neutron belt | 417 | 24 |
| Electron | 160 | 10 |

These are local pair counts, not counts of globally valid alternative quotients.
They show why dropping source correspondence does not leave a unique local rule.

More importantly, even complete labels and orientations do not determine which
higher cells should be present:

- Three faces of a tetrahedron have the same vertices and edges as all four.
  The gluer accepts both inventories: disk versus sphere.
- Four tetrahedral facets of a 4-simplex have the same complete 2-skeleton as
  all five. The gluer accepts both: a 3-ball versus the full 3-sphere boundary.
- The neutron's six panels, either singly capped variant, and the doubly capped
  variant all have exactly the same vertices and edges. All four inventories
  admit consistent oriented gluing. Their surface homology distinguishes
  annulus, disk, disk and sphere.

### Protected-rim test

Mark the six neutron rim edges as exposed interfaces that cannot be consumed by
internal gluing. The exact same gluer then accepts only the uncapped inventory
among those four candidates. Each single cap violates three protected interface
conditions; both caps violate six. No orientation inconsistency would reject
these caps without the protection rule.

This is a concrete source-data distinction that works: **an interface intended
for external attachment is not an internal hole to be automatically filled.**
It is still additional marked data. The test does not derive that marking from
an untyped arrow list or prove uniqueness among every conceivable complex.

### Disposition

Common oriented gluing survives as a shared assembler for already admitted
cells. It explains retained seams and protected openings, but does not generate
the cell inventory. Full automatic closure would destroy the stored neutron
belt; refusing all closure would leave proton/electron completion unexplained.
A common law therefore needs typed completion/admission data as well as matching.

### Reproduction

    python research/voevodsky/checkers/check_common_assembly_gluing.py

Fresh run passed exact quotient, orientation-flip, metric-label-erasure and all
four protected/unprotected cap-inventory controls. No coefficient count inferred.

## Iteration 5: H6 refinement versus higher witnesses

Freshly read the audit and the historical `three_tetrahedron_belt.json` source.
Executed `checkers/check_common_assembly_refinement.py`. Receipt:
`results/common_assembly_refinement.json`, including inputs and implementation
hashes. No particle-specific alternate renderer or coefficient formula is used.

### A shared refinement operation really works at the surface level

For an oriented triangle (a,b,c), insert its centroid F and replace it by
(F,a,b)+(F,b,c)+(F,c,a). The checker verifies the exact oriented boundary identity
for each face and for the full chain.

- Proton: the four coarse faces generate exactly its twelve stored triangles.
- Actual neutron belt: the six coarse panels generate exactly its eighteen
  centroid-edge triangles.

The two results use the same rule. But the different coarse surfaces remain
inputs; subdivision does not explain how those surfaces were selected.

### The six-cell bipyramid is not the neutron target

Recomputed the historical common refinement of two face-sharing tetrahedra and
three tetrahedra around their opposite-apex edge. Each of its six tetrahedra is
contained in both recorded parents, checked by nonnegative exact barycentric
coordinates. Parent volumes add correctly, total volume is 16/3, and all three
arrangements have the same exact oriented outer boundary.

This verifies a genuine common refinement, but its center F has a 2-sphere
link with Betti numbers (1,0,1). The actual neutron six-cone package has an annular
center link with Betti numbers (1,1,0). Both bodies are contractible; that does
not identify their local topology. No center-preserving subdivision can turn
one into the other. Six pieces alone had hidden this distinction.

### Actual belt: alternate diagonals change the geometry

Tested all six internal seams of the six-panel belt. Each joins a noncoplanar
pair of triangles: the four-vertex determinant is +21/20 or -21/20 in the source's
scaled coordinates. Replacing the common edge with the other diagonal preserves
the patch's four-edge boundary but changes its spatial support.

Thus these alternative patches do not possess a common geometric refinement at
the fixed coordinates. A tetrahedral filling between them is possible as a
**higher witness**, but is not a subdivision of either surface. The determinant
is used only for nondegeneracy, not as a physical-volume or mass readout.

### Electron: a 4D witness, not a refinement

Partition the five oriented tetrahedral facets of the electron pentachoron into
two and three. Their boundary chains are exactly opposite and have the same six
triangular faces. The sum of all five facets is exactly the oriented boundary
of one 4-simplex, up to the single global orientation convention.

Nevertheless the two sides have different supports in four dimensions. For
each facet on the two-cell side, its interior barycenter has positive coordinate
at the vertex omitted by every three-cell-side facet; hence it is outside every
one of those facets. A geometric common refinement cannot cover both supports.
The full metric has Gram determinant 1280, so this is not a collapsed 3D case.

The pentachoron fills their difference as a four-dimensional cell. It is not a
common subdivision. Likewise its boundary has Betti numbers (1,0,0,1), unlike
the attachment tetrahedron's (1,0,0,0); refining the latter cannot create the
former.

### Disposition

Ordinary common refinement alone fails as the proposed full assembly law. It
correctly reproduces proton/belt subdivisions when the coarse surfaces exist,
but cannot select the belt topology or produce the electron's higher cell.

The broader compatibility idea survives only if it explicitly admits **higher
fillers between different constructions**, rather than conflating those fillers
with refinements. That is an additional mathematical operation whose admission
and source data remain to be specified. This distinction feeds the final
iteration on dimensional succession.

### Reproduction

    python research/voevodsky/checkers/check_common_assembly_refinement.py

Fresh run passed the exact boundary, containment, volume, link, diagonal-flip and
four-dimensional witness checks. No coefficient or return-arrow count inferred.

## Iteration 6: H1 dimensional succession and retained promotion

Freshly read the audit and common coning implementation. Executed
`checkers/check_common_assembly_dimension_cycle.py`. Receipt:
`results/common_assembly_dimension_cycle.json`.

### No intrinsic reset at dimension four

Starting with a vertex, repeatedly apply the same cone operation with a fresh
apex. Exact tests through dimension six produce the full simplex at every level.
The regular unit-edge Gram determinant is (n+1)/2^n, strictly positive; there is
no geometric obstruction after dimension four.

At every tested level:

- boundary-of-boundary is zero;
- the filled simplex collapses to a vertex by checked elementary collapses;
- it can be packaged as an external object retaining its complete internal
  simplex record, verified by exact recovery from the package;
- the filled top chain itself has nonzero boundary whenever dimension > 0.

Thus the proposed gates either apply at every level or at none of the positive
levels. They do not distinguish a tetrahedral stop from a pentachoron stop or
force a reset after four dimensions. Three and five are exactly the facet
counts of a 2-simplex and a 4-simplex, not independently derived periods.

### A finite source can bound dimension without a clock

The same flag-completion rule admits a vertex set iff all its edges exist and
it contains no source-forbidden face. It records every dimensional stage and
never supplies extra vertices to reach a desired answer.

| Source | Admitted cell counts by dimension | Result |
|---|---|---|
| Proton six directed seed arrows, forgetting directions for the skeleton | 4,5,2 | Two triangles, not a tetrahedron |
| Same seed after its declared cycle-symmetry closure | 4,6,4,1 | Filled tetrahedron |
| Supplied electron K5 skeleton | 5,10,10,5,1 | Filled 4-simplex |
| Neutron coarse edge skeleton, unprotected | 6,12,8 | Capped 2-sphere; wrong belt |
| Same neutron skeleton, two rim faces forbidden as internal fillers | 6,12,6 | Exact stored six-panel annulus |

Coning the last two alternatives gives eight versus six tetrahedral pieces.
The six-piece result is exact only because the external rims remain protected.
This is a source-based stopping distinction, not a fixed dimensional period.
The supplied electron K5 still is not a recovered minimal electron arrow seed.

### Relative closure is shared, but not a dimensional selector

On the three actual target supports, absolute boundary closure holds for the
proton and electron, but not the neutron belt. Declare the supplied attachment
marks and test closure relative to the exposed faces supported on those marks:
all three pass. All three coned targets also pass explicit point-collapse tests.

This makes relative closure a useful common admission condition, but not a rule
selecting a unique particle dimension or promotion period. No dimension-specific
reset instruction has been justified by these tests.

### Disposition

The bare cyclic-dimension hypothesis does not select the targets. Its more
restricted form—raise dimension only when source relations admit the requisite
boundary—remains viable with additional typed source data. The tests identify
which data are doing work: source symmetries, complete incidence and protected
attachment interfaces. Packaging must retain these distinctions.

## Six-test conclusion and fresh suite verification

All six bounded test batches are complete. They are not six successful
particle derivations; several simple versions have explicit counterexamples.

| Hypothesis | Final disposition |
|---|---|
| H4 Symmetry orbits | Multi-orbit reconstruction works; one orbit fails for belt/marked targets; source representatives and transports still needed |
| H2 Center/link coning | Reproduces stored constituents up to subdivision; different links remain source inputs |
| H5 Constraint realization | Bare lengths/minimum dimension fail; symmetry-enriched and oriented constraints are substantive |
| H3 Interface gluing | Exact once cells/labels are admitted; protected interfaces preserve the belt, but inventory is not generated |
| H6 Compatibility refinement | Ordinary refinement insufficient; higher filling witnesses are a distinct operation |
| H1 Dimension succession | No intrinsic 4D reset or 3/5 period; source-restricted completion remains a candidate |

The strongest surviving direction combines source-supported boundary admission,
protected external interfaces, and explicit higher fillers. Coning, symmetry,
gluing and subdivision are available operations within it, not interchangeable
explanations. A complete common minimal-source constructor and shared coefficient
transport still have to be derived; no neutron/electron count was fabricated.

Freshly reran all six checkers and the source-driven proton input-sensitivity
regression in one suite:

    python research/voevodsky/checkers/check_common_assembly_hypotheses.py

All seven executions passed. The proton still matches every historical typed
arrow and exact coefficient in the 1836 manifest; single-arrow deletions still
change its result. Suite receipt: `results/common_assembly_hypotheses.json`, with
hashes of each regenerated receipt and implementation. This verifies the current
code and freezes the evidence for the completed six-hypothesis investigation.

## Follow-up: compact source-driven geometric construction

`relative-geometric-source-constructor.md` now records an executable shared
orbit/supporting-facet/relative-boundary/cone constructor. Three proposed source
records supply seeds, affine isometries, metrics and interface roles, but no
finished face or cell lists. An independent checker reproduces all three stored
geometries and attachment marks exactly and tests source deletions. This closes
the target-list dependency for geometric construction, not the remaining
minimal-arrow derivation or coefficient-transport obligations.
