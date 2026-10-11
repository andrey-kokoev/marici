# Testing a tetrahedral parent for the signed belt

## Question and claim boundary

Operator stimulus: “i think positron is a tetrahedron. so, can signed-belt construction be a tetrahedron in higher dimension?” The requested test concerns the geometric and coefficient construction, not an identification with a physical antiparticle.

Active obligations: **forward realization**, **signed attachment transport**, and compatibility of midpoint subdivision with projection.

- **Problem:** Can a four-vertex source reproduce the actual belt panels and signed spinor return?
- **Conjecture:** A regular tetrahedron embedded in R4 admits a medial subdivision whose six selected panels project onto the retained belt, with its signs arising from inherited versus reversed face orientation.
- **Rivals:** An entire tetrahedron projects directly onto the belt; only the silhouette matches; or a change of spinor phase alone supplies the comparison.
- **Risky consequences:** All six vertices, six panels, six signs and 312 retained coefficients must agree exactly. A whole-image comparison must respect extreme-point count, and unchanged unitary/antiunitary face transport must preserve projector overlaps.
- **Falsification test:** Construct the source with gap 7/10, test the full coefficients, perturb the hidden metric, erase the orientation signs and compare regular versus projected face overlaps.
- **Disposition:** The signed medial-subassembly construction passes exactly. The entire-tetrahedron projection and unchanged-phase/unitary-view interpretations fail. This is a geometric construction and coefficient reconstruction, not an antiparticle identification.

## Explicit regular parent in four-dimensional Euclidean space

With the retained gap g=7/10, take

\[
\begin{aligned}
A&=(0,21/20,0,3\sqrt{151}/20),\\
B&=(0,-7/20,2,-\sqrt{151}/20),\\
C&=(-\sqrt3,-7/20,-1,-\sqrt{151}/20),\\
D&=(\sqrt3,-7/20,-1,-\sqrt{151}/20).
\end{aligned}
\]

Every squared edge length is 12. These four vertices define an ordinary three-dimensional tetrahedron embedded in R4, not a four-simplex or a proposed physical extra dimension.

Orthogonally project by dropping the last coordinate. The resulting tetrahedron is flattened: its three base edges have squared length 12 and its three apex edges have squared length 149/25. Thus a tetrahedral parent also exists entirely in three dimensions, but it is not regular in the displayed metric. The additional coordinate restores regularity.

## Midpoint subdivision, rather than whole-object projection

The six edge midpoints are exactly the retained belt vertices:

| Parent edge | Belt vertex |
|---|---|
| AB | U0 |
| AC | U1 |
| AD | U2 |
| BC | L1 |
| BD | L2 |
| CD | L0 |

Midpoint subdivision cuts off four corner tetrahedra and leaves a central octahedron. Retain its six side triangles, omitting the U0–U1–U2 and L0–L1–L2 caps. Projection gives precisely the current six-panel belt. Midpoint formation and projection commute as linear maps on every labelled coordinate packet; the checker stores both independently computed matrices.

This is a subassembly of a volume subdivision. Three retained panels are interior cuts of the parent tetrahedron, so it is not a subdivision of the original tetrahedral boundary alone.

The stronger whole-object claim fails independently of ambient dimension: all six belt vertices are exposed extreme points of their convex hull, whereas an affine image of a four-vertex simplex has at most four extreme points. Its six-panel surface also has two boundary loops and Euler characteristic zero, unlike the closed tetrahedral boundary.

## The existing signs arise from face orientation

For a central triangle lying in a parent face, its outward normal agrees with the parent's. For a corner-cut triangle, its outward normal is opposite to the normal of the parallel opposite parent face. This gives chi=+1 and chi=−1 respectively.

| Belt panel | Subdivision role | Inherited parent face | chi |
|---|---|---|---|
| U0 L1 L2 | Cut at B | ACD | −1 |
| U1 L0 L1 | Cut at C | ABD | −1 |
| U2 L2 L0 | Cut at D | ABC | −1 |
| L0 U1 U2 | Central face | ACD | +1 |
| L1 U0 U1 | Central face | ABC | +1 |
| L2 U2 U0 | Central face | ABD | +1 |

These are exactly the recorded signs, without adjusting the old coefficients. If n_i is the belt's outward normal and m_a the inherited projected parent-face normal, then

\[
\chi_i n_i=m_a,
\qquad
P_i=\frac{I-\chi_i n_i\cdot\sigma}{2}
   =\frac{I-m_a\cdot\sigma}{2}.
\]

There are three distinct inherited projectors, each appearing twice on opposite panels. BCD is the omitted parent-face direction. These opposite-panel copies do not identify the original neutron candidate's selected triangle-mode states with spinor states.

The frame sum and inverse are recomputed from these newly derived projectors. The resulting L, G and N matrices reproduce **every one of the 312 retained nonzero coefficients**, with the same zero entries and labelled ports. N is again Hermitian, idempotent and rank two: omitting the face direction does not prevent the normalized frame from retaining both input components.

## Why this is not merely a phase-shifted regular tetrahedron

In intrinsic orthonormal coordinates, the geometric projection restricts to

\[
M=\operatorname{diag}(1,g/\sqrt2,1).
\]

Normals transport by the normalized inverse transpose of M, not by a rotation. The checker verifies its cofactor form on all four parent faces.

For distinct regular tetrahedral face projectors,

\[
\operatorname{tr}(P_aP_b)=\frac13.
\]

For distinct retained projected side directions,

\[
\operatorname{tr}(P_iP_j)=\frac{149}{296}.
\]

A common unitary or antiunitary change of spinor basis preserves these overlaps; a scalar phase does not change a projector at all. Consequently the new route must transport the geometry's normals and rebuild and normalize the projected frame. It does not carry the unmodified regular tetrahedral face states across by a phase or rotation.

Two additional controls fail as expected: changing the hidden squared scale by −1/100 changes the apex squared edges from 12 to 299/25; discarding the orientation signs gives the different 264-transfer return instead of the retained 312-transfer return.

## Surviving scope and verification

The parent depends on the supplied belt gap, distinguished axis, cap omission and spinor projection rule. The construction proves existence, not uniqueness or a source-derived physical interpretation. The charge-conjugation map and mass/charge readouts needed for positron identification remain absent.

```text
python research/aspect/scc/scc.py check voevodsky-signed-belt-tetrahedral-parent
python research/aspect/scc/scc.py categorical research/voevodsky/contracts/signed-belt-tetrahedral-parent.json
python research/aspect/scc/scc.py inverse research/voevodsky/contracts/signed-belt-tetrahedral-parent.json positron_identification
```

Sixteen exact checker conditions cover geometry, inherited signs, full coefficients, normal transport, route compatibility and negative controls. No floating-point comparison is used. Outputs:

- `results/signed_belt_tetrahedral_parent.json`
- `results/signed_belt_tetrahedral_parent_maps.json`
- `contracts/signed-belt-tetrahedral-parent.json`

The SCC word-token backend compares hashes of the already checked composite matrices, not the uncomposed primitive words. Its physical-antiparticle cell is explicitly unsupported. Global registry inspections reported unrelated stale models; only this owner-local model is checked here. Existing viewers and source artifacts are unchanged.
