# Marked dilation patches through the existing source geometry API

## Result and source boundary

An integer-dilated elementary tetrahedron or octahedron can be constructed as a finite patch of the existing source geometry's primitives, with the original vertex labels retained. The implementation replays **actual `LocalPrimitiveGeometry.register/neighbor` calls**, rather than substituting a separately invented neighbor graph. Each octahedron keeps the source's existing four-tetrahedron diagonal subdivision.

Direct and successive refinements produce the same finest geometric primitive set and the same images of the original labelled vertices. Their geometry histories are retained separately; this does not assert that two particle processes or coefficient histories are identical.

Verification level: a written general geometric argument with bounded exact-safe-integer source-API replay and an independent finite certificate check. No native particle/reader packet, phase-compatible PN/NE transfer or uniform Ramsey bound is produced. In particular, the parent `space-admission` and governing Ramsey claims remain open.

## Prior work recovered before construction

- `research/nima/barycentric-witness-packet.md`: existing marked face/type/term retention for a generated tetrahedron and checked barycentric geometry. It is not this lattice-dilation construction.
- `research/nima/barycentric-refinement-coherence.md`: canonical annotation pullback along a supplied geometrically valid carrier and compatibility under composition. It explicitly does **not** synthesize fillers for every newly introduced boundary.
- `research/strominger/eight-sector-interface-v1.md`: an existing read-only, lossless comparison workspace with actual source contexts; changing comparison charts does not admit new native occupied cells.
- `research/strominger/fcc-toroidal-field-v1.md`: the actual source FCC coordinate map and fixed-octahedral-subdivision obstruction. This construction keeps the fixed subdivision; it does not silently rotate it or add octahedral centers as new native vertices.

These records were inspected, not independently recompiled or imported as local proof outcomes. They prevent conflating a geometric refinement, preservation of annotations and creation of native witness-bearing operations.

## Exact coordinate binding to the actual source

The source uses integer four-vectors b with sum one. Its spatial coordinate map is

$$
F(b)=(b_1+b_2,b_1+b_3,b_2+b_3).
$$

With the preceding plane-lattice coordinates, t=e0-b, where e0=(1,0,0,0). Thus an elementary chamber index k has source item:

- q=-sum(k)=1: inverted tetrahedron, origin e0-k;
- q=2: octahedron, origin e0-k-(1,1,1,1);
- q=3: upright tetrahedron, the same origin formula as q=2.

These origins have sums 2,-1,0 respectively, exactly the contracts of `makeLatticeItem`. This identifies the earlier mathematical chambers with actual source items, including the source octahedron's chosen components.

## Finite patch constructor

For a in L and positive integer m, let D(v)=a+mv. If the original chamber has coordinates k_i <= t_i <= k_i+1, the dilated region has bounds

$$
\ell_i\le t_i\le\ell_i+m,
\qquad\ell_i=t_i(a)+mk_i.
$$

Its elementary chambers are exactly those j satisfying

$$
\ell_i\le j_i\le\ell_i+m-1,
\qquad-\sum_i j_i\in\{1,2,3\}.
$$

Each elementary chamber's t_i coordinate ranges over its full closed unit interval, so these inequalities are both necessary and sufficient for containment. Boundaries of the dilated region lie on arrangement planes, hence no open chamber straddles them. The selected chamber closures therefore cover the entire dilated region, including its boundary. The enumeration is finite, with at most m^4 index candidates.

Materialize every selected item with `makeLatticeItem`, retaining its components. The source's octahedral subdivision consists of four tetrahedra around one fixed opposite-vertex diagonal. It fills the octahedron without changing the triangular macro-boundary. The source-primitive patch is therefore a finite tetrahedralization of a convex region.

Its complete-face adjacency graph is connected: interior points in any two primitives can be joined by a perturbed path inside the convex region that avoids the finite codimension-two skeleton and crosses only complete internal triangular faces. A breadth-first traversal can consequently register one seed primitive and recover all the others using the actual source `neighbor` operation. The implementation checks each internal neighbor against the independently enumerated expected primitive and owner. It retains a full-face spanning-tree history, not just an unordered volume total.

## Marks, readout and composition

Every original source vertex has an explicit occurrence label and the recorded image a+mv. The patch retains these labels even though it introduces additional vertices. Reading a homogeneous pattern checks these **marked vertices**, not the whole refined patch.

For D(a,m) after D(b,n),

$$
D_{a,m}D_{b,n}=D_{a+mb,mn}.
$$

Dilated coarse chamber boundaries remain source arrangement planes. Refining each intermediate chamber therefore partitions exactly the same final region into the same finest source chambers as direct refinement. Fixed source octahedral components then give the same finest primitive set. The affine identity also gives equal images for each original labelled vertex.

The direct traversal and the nested collection of traversals are different retained certificates. Equality of their endpoint geometry is not a supplied higher comparison between native PN/NE histories. Nor is a breadth-first selection claimed to be reference-free or symmetry-equivariant.

Under the earlier parity coloring, the scale-two tetrahedron's marked corners all have color zero while its patch contains color-one subdivision vertices. A generated complete-coloring fixture is accepted by the existing independent `ramsey_certificate.verify`. This explicitly checks the intended readout distinction without claiming unavoidable monochromatic patterns.

## Executable scope and evidence

The mathematical enumeration works over arbitrary exact integers. The reused JavaScript source uses `Number`, so the implementation explicitly limits scale to 16 and guards source/target coordinates at 2^20. Its structural coordinate sums and differences remain well within safe integer arithmetic. Floating drawing centers are not used in decisions. A request beyond the execution envelope raises `PatchResourceError`: it is a resource refusal, **not** an invalid mathematical witness or Ramsey counterexample.

- Constructor: `research/voevodsky/ramsey-marked-patch.mjs`.
- Source-API checker: `research/voevodsky/checkers/check_ramsey_marked_patch.mjs`.
- Combined checker: `research/voevodsky/checkers/check_ramsey_marked_patch.py`.
- Frozen scope: `research/voevodsky/contracts/ramsey-marked-patch-attempt.v1.json`.
- Combined receipt: `research/voevodsky/results/ramsey-marked-patch-v1.json`.
- Source geometry receipt and certificate fixture: `research/voevodsky/results/ramsey-marked-patch-geometry-v1.json` and `research/voevodsky/results/ramsey-marked-patch-fixture-v1.json`.

The finite suite tests three source item types, three translations and scales one through three; nine direct/nested comparisons additionally include total scale four. It checks unit primitive determinants, total volume/count, boundary triangles, actual source neighbor replay and label controls. Recursive source-module hashes pin the API dependencies. No production source or viewer is modified.

A stronger native reader/particle interpretation would additionally need its own protocol preserving source roles, coefficient histories and admissible transfers. That stronger binding is not imposed as a prerequisite for a purely geometric Ramsey theorem. Independently, this construction supplies no forcing bound for arbitrary colorings. Neither a packet interpretation nor a forcing theorem follows from a geometric patch or an imported annotation theorem.
