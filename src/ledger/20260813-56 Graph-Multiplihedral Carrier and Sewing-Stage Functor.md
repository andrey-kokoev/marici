# Graph-Multiplihedral Carrier and Sewing-Stage Functor

## Record

Date: 2026-08-13

Status: the marked-theta Ward comparison has a canonical finite
graph-multiplihedral carrier, and graph addition now has exact cellular
transition maps on that carrier.  The bare transition diagram is strictly
functorial.  The physical Ward/curve coefficient system on it is not yet
constructed.

Four tempting shortcuts are falsified:

1. the two-sewing square is not a face of the single final
   graph multiplihedron;
2. arbitrary gauge-tail subsets are not connected Ward trajectories;
3. the local on-shell Ward differential does not land in the 243 cubic-origin
   module;
4. fillers in the freely contractible origin simplex do not prove a physical
   Ward or curve lift.

Reproducible certificates:

```text
research/nima/atlas_graph_multiplihedron_k23.rs
research/nima/check_graph_addition_multiplihedron_maps.rs
research/nima/check_moving_ward_boundary.rs
research/nima/check_origin_resolution_coherence.rs
```

## The graph multiplihedron selected by the five-vertex support

Entry 55 proved that every partially and fully sewn marked-theta
physical/curve residual needs all five cubic-sector coordinates.  The connected
interaction graph on those five vertices is

\[
G=K_{2,3}.
\]

The graph multiplihedron \(\mathcal JG\) is therefore the minimal standard
polytope whose marked tubes resolve connected regions of simultaneous
domain-to-range conversion.  This use is structurally appropriate because
graph multiplihedra parameterize homotopy-multiplicative maps: thick regions
record domain composition, thin regions range composition, and broken tubes
the conversion frontier.

The exact atlas gives:

\[
\dim\mathcal J(K_{2,3})=5,
\]

with 26 connected induced tubes, including the universal tube, and 3,847
marked faces.  Its face vector by dimension is

\[
(f_0,f_1,f_2,f_3,f_4,f_5)
=(578,1459,1289,463,57,1).
\]

The 57 facets split as:

\[
31\text{ upper facets}+26\text{ lower facets}.
\]

The equality

\[
31=2^5-1
\]

matches the 31 nonempty subsets in the five-vertex gauge-tail expansion, while
26 is the number of connected induced regions.  This is an exact cardinality
match, not yet a coefficient-level identification.

The simultaneous strict-domain/strict-range quotient is the five-cube with
face vector

\[
(32,80,80,40,10,1).
\]

Thus support and dimension alone cannot decide between the full graph
multiplihedron and its cubical quotient.

## The two sewing edges do not form a face of the final polytope

Every spanning tree \(T\subset K_{2,3}\) leaves two edges \(e,f\) to close.
There are twelve such trees.  In six presentations the two corresponding
two-vertex tubes intersect; in the other six they are disjoint but adjacent.
They are never compatible tubes.

Consequently the sewing square

\[
\begin{matrix}
T&\longrightarrow&T+e\\
\downarrow&&\downarrow\\
T+f&\longrightarrow&T+e+f
\end{matrix}
\]

cannot be a codimension-two face of \(\mathcal J(K_{2,3})\).  Each vertex of
the square has its own graph multiplihedron.  Sewing-order coherence belongs in
a Grothendieck construction or double mapping cylinder over the square, not in
the final fiber alone.

## Canonical marked edge-deletion carrier

Let \(G\subset H\) be two graphs on the same vertex set.  For a marked
\(H\)-tube \(u\), split its vertices into the connected components of
\(G|_u\).  If nested source tubes induce the same component, mark that
component by the unique innermost contributing source tube.

For every one-edge inclusion among the twelve marked-theta presentations this
defines

\[
r_{H,G}:\operatorname{Face}(\mathcal JH)
\longrightarrow
\operatorname{Face}(\mathcal JG).
\]

The exact audit covers 30 distinct one-edge inclusions and 98,802 source
faces.  It finds:

- zero undefined images;
- zero order failures;
- zero dimension failures;
- zero missed target faces;
- zero \(S_2\times D_3\) covariance failures.

Thus \(r_{H,G}\) is a total, dimension-nonincreasing, order-preserving,
face-surjective cellular carrier.  On all 46,164 audited final faces,

\[
r_{H,G}=r_{K,G}r_{H,K}
\]

for either order of deleting the two added edges, and both composites equal
the direct component map.

The unmarked restriction is the known graph-associahedral edge-deletion
projection \(\Theta\): preserve a tube up to connection and split it into
surviving compatible components.  Its cellular surjectivity and commuting
edge deletions are established for pseudograph associahedra.  The new bounded
result is the marked lift and the innermost-mark rule.

Several alternatives fail exactly:

- forget-only: 16,032 order failures, 37,284 dimension failures, and 18,738
  missed target faces;
- outermost/thick-priority: 12,192 order failures, 2,712 dimension failures,
  and 10,692 missed faces;
- broken-join: 8,568 order failures, 8,820 dimension failures, and 6,444
  missed faces;
- unanimous marking is undefined on 14,436 faces.

The finite certificate does not yet prove the innermost-mark theorem for every
graph inclusion, and it constructs a face-poset/barycentric-subdivision
carrier rather than an affine map between the original convex realizations.

## The sewing-stage carrier

The exact maps make the provisional carrier well typed:

\[
\boxed{
\mathfrak J(T;E)
=
\int^h_{S\subseteq E}
C_*(\mathcal J(T\cup S);\mathcal L_S).}
\]

Because physical graph addition points from \(T\) to \(T\cup S\), while
the cellular deletion maps point backward, the integral is over the opposite
Boolean sewing category.  The undecorated cellular diagram commutes strictly.
Any nonzero two-sewing curvature must therefore live in the coefficient maps
\(\mathcal L_S\), not in the bare face-poset transitions.

## What the local Ward audit actually proves

At one cubic vertex on shell, a moving longitudinal mark has boundary

\[
d(v,h)
=(v,h+1;k\otimes k)-(v,h+2;k\otimes k).
\]

The exact audit verifies 180 local Ward signs and 48 tree-exact edge
propagations.  It also retains 24 chord cycles with harmonic rank two, exactly
as required by

\[
b_1(K_{2,3})=6-5+1=2.
\]

But this differential is typed

\[
d:\mathsf{WardMark}_1\longrightarrow\mathsf{ExitTensor}_0,
\]

not into the 243 cubic origins.  No canonical reinsertion from exit tensors to
cubic origins or curve carriers is supplied by the on-shell identity.

The full gauge-tail expansion contains 2,316 nonzero disconnected-tail origin
terms, appearing in all 48 partial presentations.  Every fixed tail subset
vanishes only after origin augmentation.  Therefore:

\[
\text{tail subset}\ne\text{connected Ward trajectory}.
\]

Arbitrary subsets index conversion endpoints; connected tubes index
propagation regions.  A physical differential must relate them through
kinetic insertions and propagators.

## Formal fillers and their limit

Inside the freely contractible origin complex

\[
K_\bullet=C_*(\Delta^2)^{\otimes5},
\]

all 48 one-edge residuals admit integral nearest-neighbor fillers, and all 24
nonzero two-order cycles admit integral fillers made from 675 triangles and
3,783 product squares.

The two-order curvatures remain nonzero after tensoring with
\(\det H_1(K_{2,3})\).  Road rotation acts by \(+1\) and reflection by
\(-1\) on that determinant line.  Pointed fillers are integral, but
unpointed road-rotation averaging needs \(1/3\), producing a formal
\(\mathbb Z/3\) obstruction in the origin permutation module.

None of this proves a physical lift.  No formal simplex edge has been
identified with an actual Ward/V, contact, ghost, or curve generator.  The
torsion may disappear after the required physical enlargement.

## Topological staging

The ribbon thickenings of the four graph stages are:

\[
(0,1)\longrightarrow(0,2)\longrightarrow(1,1),
\]

that is,

\[
\text{disk}\longrightarrow\text{annulus}
\longrightarrow\text{once-punctured torus}.
\]

The two closure directions span \(H_1(K_{2,3})\), and their wedge spans
\(\det H_1\).  The first closure is boundary splitting; the second is
boundary joining/handle creation.  The final coherence is therefore modular
sewing data, not merely associativity of an ordinary product.

## Evidence boundary

Proved by finite exact certificates:

- the complete \(K_{2,3}\) marked-tubing atlas;
- incompatibility of the two missing-edge tubes;
- the canonical cellular graph-deletion carrier on all marked-theta stages;
- strict commutation of both bare deletion paths;
- failure of direct tail/trajectory and origin-boundary identifications;
- existence and symmetry properties of formal origin fillers.

Not proved:

- the marked deletion theorem for arbitrary graphs;
- a scalar-derived Ward/curve coefficient system;
- a map from the local Ward complex into the origin or resolved surface
  carrier;
- cyclic Cut compatibility of any physical filler;
- modular completion of the comparison.

## Subsequent outcome and next falsifier

Entry 57 executes the smallest off-shell Ward/propagator audit.  It derives
the contact-minus-longitudinal boundary, proves that physical endpoint sewing
uses the even relation \(Q_{e,\mathrm{tail}}=Q_{e,\mathrm{head}}\), and replaces
the apparent longitudinal obstruction by a rank-two circuit-homology sector.
The next test is therefore no longer to ask whether the off-shell identity
exists.  It is to construct its coefficient map into the resolved
Brauer/curve carrier and prove that the map is natural under marked edge
deletion.

Concretely, start from

\[
k^\mu V_{\mu\nu\rho}
=P_{\nu\rho}(k_2)-P_{\nu\rho}(k_1)
\]

composed with the propagator identity already audited in entry 57.  Map the
resulting cycle lattice

\[
H_1(G;\mathbb Z)\longrightarrow
\mathsf{Circuits}^{\rm res}(G)
\]

into actual resolved curve states, then test whether this coefficient map
commutes with \(r_{H,G}\) and one physical Cut.  A rank match or an abstract
graph-cycle identification is not sufficient.

## Primary sources

- Devadoss and Forcey, *Marked tubes and the graph multiplihedron*:
  <https://arxiv.org/abs/0807.4159>.
- Carr, Devadoss, and Forcey, *Pseudograph associahedra*, especially the
  commuting cellular edge-deletion projections:
  <https://arxiv.org/abs/1005.2551>.

## Internal dependencies

- Entry 54: exact two-open-pair physical/curve squares.
- Entry 55: originwise diagonal-map falsification and all-five support.
- Entry 57: off-shell Ward sequence, even endpoint gluing, and the residual
  circuit-homology target.
- Working context: `research/nima/ward_brauer_math_context.md`.
