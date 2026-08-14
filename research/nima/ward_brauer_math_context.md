# Ward--Brauer mathematical context

Last updated: 2026-08-13

Purpose: preserve the main Nima-side mathematical model independently of the
executable certificates.  This is a living research note, not a ledger claim.

## Current question

There are two carrier presentations of the marked-handle Yang--Mills leading
singularity:

1. the ordinary cubic tensor network with physical polarization projectors;
2. the gauge-reduced endpoint-extension/curve-cover network with metric
   traces and resolved closed circuits.

After complete cubic-sector augmentation, the physical and curve carriers
agree before either of two closures, after either first closure, and after both
closures.  They do not agree on the diagonal raw origin basis
\(\{0,1,2\}^{5}\), even after summing all sector choices at the closure
endpoints.  The required comparison must therefore transport between origins.

The mathematical target is a derived, cyclic, sewing-natural dictionary—not a
strict originwise equality.

## Exact local algebra

For outgoing null momenta \(k_0+k_1+k_2=0\), decompose the cubic vertex into
three singleton sectors:

\[
V=\sum_{s\in\mathbb Z/3}V_s,
\qquad
V_s
=
\eta_{\mu_{s+1}\mu_{s+2}}
(k_{s+1}-k_{s+2})_{\mu_s}.
\]

Using momentum conservation,

\[
k_{s+1}-k_{s+2}=2k_{s+1}+k_s.
\]

Hence each full sector splits canonically as

\[
V_s=\bar V_s+G_s,
\]

where

\[
\bar V_s
=2\eta_{\mu_{s+1}\mu_{s+2}}k_{s+1,\mu_s}
\]

is the reduced surface handle and

\[
G_s
=\eta_{\mu_{s+1}\mu_{s+2}}k_{s,\mu_s}
\]

is a longitudinal mark on the singleton half-edge.

For the full cubic vertex,

\[
k_0^{\mu_0}V_{\mu_0\mu_1\mu_2}
=
P_{\mu_1\mu_2}(k_2)-P_{\mu_1\mu_2}(k_1),
\]

with

\[
P_{\mu\nu}(k)=k^2\eta_{\mu\nu}-k_\mu k_\nu.
\]

On the massless three-point locus,

\[
k_0\cdot V
=k_1\otimes k_1-k_2\otimes k_2.
\]

Cyclic rotation gives the other two identities.  Thus a longitudinal mark
entering one half-edge is the signed difference of the two ways it can leave
through the other half-edges.

## The local Ward triangle

Let \(g_s\) denote a longitudinal mark on half-edge \(s\).  Let \(w_s\) denote
the Ward move in which a mark enters at \(s\).  Up to a fixed global cyclic
orientation, the local differential is

\[
d w_s=g_{s+1}-g_{s+2}.
\]

The three Ward moves form the oriented 1-skeleton of a triangle.  Their cyclic
sum is closed:

\[
d(w_0+w_1+w_2)=0.
\]

Therefore the previously introduced formal complex
\(C_\bullet(\Delta^2)\) has a non-arbitrary 1-skeleton: its edges are forced by
the cubic Ward identities.

The status of the 2-cell is open.  It must be realized by an actual identity
among Ward-routing histories, a BRST/BV cell, or a curve homotopy.  Freely
adjoining a filler would make the construction tautological.

## The typing repair: restore the off-shell/contact strata

The moving-Ward audit exposes a precise type error in the provisional
triangle.  The physical local differential is

\[
d_{\rm Ward}:\mathsf{WardMark}_1
\longrightarrow
\mathsf{ExitTensor}_0,
\]

with two rank-two exit tensors.  It does **not** land directly in the
\(3^5\)-dimensional module of fixed cubic singleton origins.  Hence a statement
that a raw origin residual is a Ward boundary requires an additional map which
has not yet been constructed.

The natural repair is to undo the premature on-shell restriction.  Off shell,
the local identity reads

\[
k_0^{\mu_0}V_{\mu_0\mu_1\mu_2}
=
P_{\mu_1\mu_2}(k_2)-P_{\mu_1\mu_2}(k_1),
\]

where \(P\) is the inverse kinetic operator.  If an exit is attached to the
propagator homotopy \(h\) on the neighboring edge, the deformation-retract
identity has the form

\[
Qh+hQ=1-ip.
\]

In elementary covariant-gauge tensor language, \(P(k)D(k)\) is the identity
minus a longitudinal projector.  The identity term contracts the neighboring
edge and produces a contact graph; the longitudinal remainder is the Ward mark
which continues to propagate.

Thus the smallest plausible degree-zero carrier is not a fixed cubic graph.
It must include:

- cubic-origin states;
- graphs obtained by contracting an internal edge, equivalently contact
  vertices;
- longitudinal exit states on uncontracted edges;
- harmonic closed-circuit states;
- ultimately the ghost/antifield states required for a true BRST/BV complex.

The provisional differential is therefore

\[
\mathsf{WardMark}(G)
\xrightarrow{\ k\cdot V\ }
\bigoplus_{e\sim v}\mathsf{KineticInsertion}(G,e)
\xrightarrow{\ h_e\ }
\bigoplus_{e\sim v}
\left(
\mathsf{Contact}(G/e)
\oplus
\mathsf{Longitudinal}(G,e)
\right).
\]

This has exactly the grammar of a bar/cobar or Feynman-transform differential:
the differential changes graph type by contracting an edge.  The 243 origins
are only the top cubic stratum of this larger graph complex.

The immediate non-tautological target is now a comparison

\[
\mathsf W^{\rm BV}_\bullet(G)
\longrightarrow
\mathsf{Cov}^{\rm res}_\bullet(G),
\]

where the left side is the off-shell scalar-first-jet/BRST complex with contact
strata and the right side is the resolved curve complex with the corresponding
curve contractions.  The missing ``reinsertion map'' is the image of the
kinetic-insertion/contact step under this comparison.

This repair is consistent with established homotopy-algebraic descriptions of
Yang--Mills: amplitudes arise as minimal-model brackets and propagators are the
homotopies used in homological perturbation
(<https://arxiv.org/abs/1812.06454>), while local Yang--Mills carries a
wave-operator-deformed homotopy BV structure whose cobar construction supplies
a strict graphical expansion (<https://arxiv.org/abs/1912.03110>).  Those
results do not establish the proposed scalar-to-surface comparison, but they
identify the correct ambient kind of complex.

### Scalar-derived common resolution

The best candidate for the common off-shell carrier is already present in the
master picture:

\[
\mathcal B_{\rm jet}=J^1_F\mathrm{Scalar}
\]

before taking gauge cohomology.  The physical-projector and resolved-surface
presentations should be two cyclic deformation retracts of this same complex,
not unrelated amplitude formulas:

\[
\mathcal P
\underset{p_{\rm P}}{\overset{i_{\rm P}}{\rightleftarrows}}
\mathcal B_{\rm jet}
\underset{i_{\rm S}}{\overset{p_{\rm S}}{\rightleftarrows}}
\mathcal S.
\]

This is a conjectural strengthening; neither cyclic retract has yet been built.
If it holds, the graph-multiplihedral dictionary is the universal homotopy
transfer comparison between the two retracts.  Its coefficient system is then
fixed by the scalar first-jet differential, propagator homotopy, and pairing,
rather than fitted independently on every graph.

At one vertex the required chain-level statement should look schematically
like

\[
V-\bar V
=
[Q,\chi]
+\text{kinetic/contact terms}.
\]

Inserting this identity at every vertex produces the 31 nonempty gauge-tail
subsets.  Moving \(Q\) through adjacent propagators produces the connected-tube
boundary terms.  This is the precise mechanism by which upper subset facets
and lower connected-tube facets could become the two halves of a single
graph-multiplihedral boundary equation.

### Cyclic two-retract conjecture

The current theorem-shaped target is the following.

> **Conjecture.**  The scalar first-jet complex \(\mathcal B_{\rm jet}\), with
> its scalar-derived cyclic pairing and Cut coaction, admits two
> composition-stable cyclic deformation retracts: a physical Yang--Mills
> retract \(\mathcal P\) and a resolved surface/curve retract \(\mathcal S\).
> The homological-transfer comparison between these retracts is represented at
> genus zero by Ward-decorated graph-multiplihedron chains, extends over the
> sewing-subset Grothendieck construction, and admits a modular/Brauer
> completion.

If true, the higher maps are not additional physical assumptions.  They are
the recursively transferred components of the two retracts.  Their dependence
on gauge fixing or a road-pointed contraction is allowed, but different
choices must lie in a contractible space of cyclic, Cut-natural comparisons.

The bounded proof sequence is:

1. construct a local degree-minus-one operator \(\chi\) on
   \(\mathcal B_{\rm jet}\) such that
   \(V-\bar V=[Q,\chi]+\) kinetic/contact terms;
2. attach the scalar-derived propagator homotopy and identify the contact
   terms with explicit edge contractions;
3. map those contractions to resolved curve contractions and verify one Cut;
4. use the graph-multiplihedron facet equation to generate the first higher
   comparison;
5. test the disk--annulus--punctured-torus square with the determinant local
   system and resolved circuit states;
6. only then pass to modular completion.

The conjecture is falsified locally if no such \(\chi\) exists even after the
minimal BRST/contact enlargement, or globally if its first two-route curvature
is a nonzero class in the cyclic Cut-compatible complex.

## Global marked-Ward complex

For a trivalent ribbon graph \(G\), define a provisional complex
\(\mathsf W_\bullet(G)\):

- degree zero: cubic-sector words and resolved contraction-cover states;
- degree one: the same states with one oriented moving Ward mark;
- degree two: coherent homotopies between two mark-routing histories;
- higher degree: simultaneous compatible mark transports.

The degree-one differential is generated only by the local cubic Ward
identity.  Metric propagation moves a mark along an internal edge.  A mark
dies at a transverse external state.  When a mark closes around a circuit it
must be retained in the resolved Brauer state until all relevant Cuts have
been taken.

The all-five-coordinate support found at the marked theta is compatible with
locality in this complex: a local mark can traverse the entire connected
network.  It is not evidence for a nonlocal interaction.

## Correct categorical typing

Boundary factorization makes the basic carrier cooperadic:

\[
\Delta_D\mathcal F_n
\longrightarrow
\mathcal F_L\otimes\mathcal F_R.
\]

Equivalently, reversed sewing gives an operadic or PROP-like composition.
Closed state traces require cyclic/modular structure.

The physical-projector carrier and resolved curve carrier should therefore be
objects in a category of cyclic factorization coalgebras or modular-operadic
modules.  The desired dictionary is a homotopy-coherent natural
transformation between them.

The associahedron is the prototype for coherence of operations within one
object.  Since the present problem concerns a map respecting those operations,
the closer prototype is the multiplihedron or, at loops, a modular/graphical
analogue of it.

More precisely, the classical multiplihedra form the bimodule part of a
two-coloured operadic object controlling \(A_\infty\)-morphisms: the source
associahedra act on one side and the target associahedra on the other.  A
cellular operadic-bimodule model and compatible diagonal are known
(<https://arxiv.org/abs/2206.05566>).  The graph multiplihedra provide the
right individual face posets, but an analogous composition-stable graphical
or modular bimodule is not supplied merely by listing the polytopes.  Building
that system—or identifying it with an existing Feynman-category construction—
is part of the missing theorem.

## Painted-graph model

A promising carrier is a painted trivalent ribbon graph:

- below the paint frontier, vertices use the ordinary cubic representative;
- above it, vertices use the reduced surface representative;
- the frontier carries the longitudinal Ward marks generated by
  \(V_s-\bar V_s=G_s\);
- moving the frontier through a vertex is a local Ward move;
- different orders of moving it through vertices bound higher cells.

This is the direct analogue of painted trees in the multiplihedron.  For a
graph with loops, the paint frontier can have closed components, so the
correct object is expected to be modular rather than an ordinary tree
multiplihedron.

## Graph multiplihedron candidate

Devadoss--Forcey construct, for every finite graph \(G\), a graph
multiplihedron \(\mathcal JG\) whose face poset is built from marked connected
induced subgraphs (marked tubes).  It generalizes the ordinary multiplihedron
from paths to arbitrary interaction graphs:

<https://arxiv.org/abs/0807.4159>

This is a substantially sharper candidate than the Cartesian product of five
formal Ward triangles.

For the marked-theta cubic network, the vertex graph is \(K_{2,3}\), with five
nodes.  Its graph multiplihedron has dimension five.  Independently, the exact
origin audit found that every one-edge and two-edge realization residual needs
all five cubic-sector coordinates before it augments to zero.  The equality
of these two numbers suggests the following interpretation:

\[
\text{five-coordinate residual transport}
\quad\leftrightarrow\quad
\text{top-dimensional cell of }\mathcal J(K_{2,3}).
\]

This is evidence, not yet an identification.  The decisive test is whether the
cellular boundary of the graph multiplihedron, after decorating its marked
tubes by Ward marks and endpoint-extension states, evaluates to the measured
residual.

There is a stronger combinatorial match.  The local decomposition
\(V_v=\bar V_v+G_v\) gives

\[
\prod_{v\in V(G)}V_v-
\prod_{v\in V(G)}\bar V_v
=
\sum_{\varnothing\ne S\subseteq V(G)}
\left(\prod_{v\in S}G_v\right)
\left(\prod_{v\notin S}\bar V_v\right).
\]

For five vertices this has \(2^5-1=31\) nonempty gauge-tail subsets.  The
upper facets of a graph multiplihedron are likewise indexed by nonempty node
subsets, represented by compatible broken tubes.  Its lower facets are indexed
by connected tubes, precisely the candidate regions through which a Ward mark
can propagate before meeting the rest of the network.

For \(K_{2,3}\), the exact marked-tubing atlas now gives 26 connected induced
tubes when the universal tube is included: five singletons and 21 subsets
containing at least one core and at least one middle vertex.  It gives exactly
31 upper facets and 26 lower facets.  The complete face vector, in dimensions
zero through five, is

\[
(578,1459,1289,463,57,1).
\]

The corresponding strict-domain/strict-range 5-cube has face vector

\[
(32,80,80,40,10,1).
\]

Thus the 31/26 boundary split is established combinatorially.  Matching its
cellular signs and coefficient evaluations to the 31 gauge-tail sectors
remains the first serious physical graph-multiplihedral test.

Tentative marking dictionary:

- thick tube: an ordinary/full physical cubic subnetwork, the domain of the
  dictionary;
- thin tube: a reduced surface subnetwork, the range of the dictionary;
- broken tube: the active transition frontier carrying Ward marks.

Nested and disjoint tubes then encode compatible orders of converting
connected subnetworks.  This removes arbitrary long-range origin mixing: a
homotopy may have global support only by propagating through a chain of
connected tubes.

The partial-sewing presentations require a system rather than a single
polytope.  For a spanning tree \(T\) and a subset \(S\) of the two closure
edges, set

\[
G_S=T\cup S.
\]

The candidate carriers are decorated chains

\[
C_*(\mathcal JG_S;\mathcal L_{\rm Ward/curve}),
\]

with comparison maps under adding, deleting, or cutting a closure edge.  The
first structural question is whether these maps exist cellularly and glue
across the twelve spanning-tree presentations.  A graph multiplihedron by
itself does not yet retain the ribbon homotopy class or resolved closed-circuit
state, so the coefficient system \(\mathcal L_{\rm Ward/curve}\) is essential.

The exact atlas makes the need for this system unavoidable.  In each of the
twelve presentations, the two missing edges become two-vertex tubes in the
final \(K_{2,3}\).  For six presentations the two tubes intersect; for the
other six they are disjoint but adjacent.  They are never compatible tubes.
Consequently the two-sewing square is not a codimension-two face of the single
polytope \(\mathcal J(K_{2,3})\).

The correct carrier must instead lie over the Boolean sewing square

\[
\begin{matrix}
T &\longrightarrow& T+e\\
\downarrow && \downarrow\\
T+f&\longrightarrow&T+e+f.
\end{matrix}
\]

Each vertex has its own graph multiplihedron.  Adding an edge enlarges the
graphical building set by making new induced subsets connected; geometrically
this refines the corresponding polytope by new truncation data.  The expected
comparison therefore runs through cellular collapse/refinement maps, not
literal face inclusions.

A provisional total carrier is the homotopy-coherent Grothendieck construction

\[
\mathfrak J(T;e,f)
=
\int^{h}_{S\subseteq\{e,f\}}
C_*(\mathcal J(T\cup S);\mathcal L_S),
\]

or, geometrically, a double mapping cylinder of the graph-addition comparison
maps.  Its base 2-cell records the order of sewing; its fibers resolve the
Ward conversion within each graph stage.  The desired \(K_{ef}\) lives in this
total carrier.  Looking for it solely inside the final fiber is a typing error.

For an arbitrary set \(E\) of open sewing pairs, the same proposal becomes

\[
\mathfrak J(T;E)
=
\int^{h}_{S\subseteq E}
C_*(\mathcal J(T\cup S);\mathcal L_S).
\]

The marked-theta graph-addition audit now supplies the missing transition maps
at the face-poset level.  For an inclusion of graphs on the same vertices
\(G\subset H\), take an \(H\)-tube to its connected components in \(G\).
When several nested source tubes induce the same component, give that component
the mark of the unique innermost source tube.  On all thirty distinct
one-edge inclusions appearing among the twelve \(K_{2,3}\) presentations this
defines a total, dimension-nonincreasing, order-preserving, face-surjective map

\[
r_{H,G}:\operatorname{Face}(\mathcal JH)
\longrightarrow
\operatorname{Face}(\mathcal JG).
\]

It is \(S_2\times D_3\)-covariant and satisfies strictly

\[
r_{H,G}=r_{K,G}\,r_{H,K}
\qquad (G\subset K\subset H)
\]

for both orders of adding the two missing edges.  Thus the bounded sewing
diagram is already a contravariant functor of face posets; its barycentric
subdivisions provide honest cellular carriers for the mapping-cylinder
construction.  No affine map between the original convex realizations has
been proved, and extension of this rule to arbitrary graph inclusions remains
a cellular theorem to establish rather than an output of the marked-theta
audit.

A subsequent exhaustive test covers every connected simple graph through five
labeled vertices: 157,643 marked source faces, 557,618 cover relations,
18,627,714 permutation checks, and 274,964 two-edge source faces, with no
failure of the component/innermost rule.

Three structural parts do admit all-graph proofs.  Contributors to one target
component form a nested chain, so the innermost mark is unique and marked
compatibility descends.  For dimension, choose in every source tube \(u\) a
vertex \(x_u\) outside all maximal proper child tubes.  Such a vertex exists
because the children are pairwise nonadjacent and cannot cover the connected
tube \(u\).  The \(G\)-component \(C_u\) containing \(x_u\) has \(u\) as its
unique innermost contributor, and distinct source tubes give distinct
\(C_u\).  Thus

\[
u\longmapsto C_u
\]

is a mark-preserving injection, proving target codimension is at least source
codimension.  Finally, for \(G\subseteq K\subseteq H\), the innermost
\(H\)-tube for a final \(G\)-component remains innermost after passage through
its \(K\)-component.  This proves strict functoriality as a marked-tubing set
map for arbitrary finite inclusions.  What remains unproved in general is
construction of a marked lift of every target face.

Indeed, the four defining source refinements descend componentwise.  Broken
resolution remains broken resolution.  Thin and thick insertion retain their
paint type: every source tube between a new thin tube and its nonthick paint
region is thin, while every ancestor of a thick tube is thick.  Finally, a
closely nested broken family restricts on each affected target component to a
closely nested broken family while its parent changes from broken to thick.
An intervening target tube in the last case would lift to a source tube
strictly between the new broken tube and its parent, contradicting close
nesting.  Disjoint target components may be refined successively.  Hence the
map is face-poset order preserving for arbitrary graph inclusions.

Consequently the integral above should be read as a homotopy colimit over the
opposite Boolean sewing category: graph addition points forward physically,
whereas the cellular collapse \(r\) points from the more highly truncated
graph multiplihedron back to the less connected graph.  The strict
commutation of the bare \(r\)-maps means that any nonzero two-sewing curvature
must lie in the Ward/curve coefficient maps, not in the undecorated face-poset
transition itself.

The unmarked restriction is not new: edge deletion for graph and pseudograph
associahedra has a known cellular surjection \(\Theta_e\) that splits a tube
into its surviving connected components, and the deletion maps commute
(<https://arxiv.org/abs/1005.2551>).  The bounded new datum here is the marked
lift to graph multiplihedra and the discovery that the surviving component
must inherit the **innermost** source mark.  Forget-only, outermost,
thick-priority, and broken-join alternatives all fail the marked face order.
The natural next combinatorial theorem is now specifically that the
innermost-mark extension of \(\Theta\) is face surjective for arbitrary graph
inclusions.

This separates two kinds of coherence that had previously been conflated:
paint/Ward coherence inside each graph and sewing-order coherence between
different graphs.

At arbitrary topology the likely object is therefore a ribbon/modular graph
multiplihedron or a modular envelope of this decorated graph-multiplihedral
system, not the undecorated convex polytope alone.

The facet product formulas suggest the master homotopy-morphism equation.  If
\(t\) is a connected tube, write \(G(t)\) for its induced subgraph and
\(G^*(t)\) for the reconnected complement.  Lower graph-multiplihedron facets
have the form

\[
\mathcal JG^*(t)\times\mathcal KG(t),
\]

while upper facets associated with compatible broken tubes
\(t_1,\ldots,t_k\) have the form

\[
\mathcal KG^*(t)\times
\mathcal JG(t_1)\times\cdots\times\mathcal JG(t_k),
\qquad t=\bigcup_i t_i.
\]

After choosing orientations and a Ward/curve coefficient system, the desired
top-cell evaluation \(\Phi_G\) should therefore satisfy schematically

\[
\boxed{
d\Phi_G
=
\sum_t \pm\,
\Phi_{G^*(t)}\circ\mu^{\rm phys}_{G(t)}
-
\sum_{\{t_i\}}\pm\,
\mu^{\rm surf}_{G^*(t)}
\circ
\bigotimes_i\Phi_{G(t_i)}.}
\]

This is the graph-multiplihedral analogue of an \(A_\infty\)-morphism
identity.  It gives a more intrinsic source for the one-edge homotopies
\(H_e\): they should be restrictions of \(\Phi_G\) to sewing/cut faces, not
independently chosen primitives.

The unknowns in this formula are concrete:

- the orientation signs;
- the evaluation of broken tubes as moving Ward marks;
- the endpoint-extension coefficient attached to each marked tube;
- functoriality of the reconnected complement under physical Cuts;
- the ribbon/Brauer decoration needed when a tube surrounds a closed circuit.

There is an important possible quotient.  In the ordinary multiplihedron,
strict associativity of the domain and range collapses the full multiplihedral
coherence to a cube; Devadoss--Forcey describe graph analogues of the one-sided
quotients as well.  Both physical categorical traces and resolved metric
traces commute strictly in the marked-theta audit.  Therefore the relevant
Ward carrier may be a strict-domain/strict-range quotient of
\(\mathcal JG\), with graph connectivity retained in its coefficient system.
The audit must decide between the full graph multiplihedron and this cubical
quotient; dimensional agreement alone does not distinguish them.

### Why strict traces do not yet imply a cube

There is a sharper criterion.  If every local gauge tail \(G_v\) admitted an
independent local null-homotopy, the replacement

\[
V_v\rightsquigarrow \bar V_v
\]

could be performed independently at each vertex.  The tensor-product homotopy
would then be controlled by the conversion cube \([0,1]^{V(G)}\); different
orders would be the ordinary cubical interchange relations.

The cubic Ward identity says something weaker and more interesting.  A
longitudinal tail at a vertex is not killed there.  It is converted into a
signed difference of tails on adjacent half-edges, propagates through metric
contractions, and dies only at a transverse boundary or after a globally
resolved circuit calculation.  Thus Ward exactness is naturally attached to
a **connected subgraph**, not to an isolated vertex.

This gives an operational cube-versus-multiplihedron test.  Let

\[
q_G:\mathcal JG\longrightarrow \square_G
\]

denote the strict-domain/strict-range quotient whenever it is defined.  The
Ward evaluation descends to \(\square_G\) exactly when any two marked tubings
with the same converted-vertex data have equal evaluations.  Equivalently,
every cellular edge collapsed by \(q_G\) must evaluate to zero in the
Ward/curve coefficient system.  A single nonzero collapsed-edge evaluation
forces the full connected-tube resolution.

This also explains why strict equality after final augmentation is
insufficient.  Augmentation can kill the connected transport while the
coefficient system before augmentation still detects it.

### A conversion filtration

The 31-term gauge-tail expansion is naturally the first, subset-resolved layer
of a filtration by the set of converted vertices.  Its associated cubical
complex remembers a subset \(S\subseteq V(G)\), but forgets how the tails in
\(S\) meet and propagate.  Resolving simultaneous propagation through
connected regions refines this subset complex by nested connected tubes.

Schematically, one should seek a filtered comparison

\[
C_*(\mathcal JG;\mathcal L_{\rm Ward/curve})
\longrightarrow
C_*(\square_G;q_{G*}\mathcal L_{\rm Ward/curve}),
\]

whose first page is the gauge-tail subset expansion and whose higher
differentials are Ward transports through connected tubes.  In this reading,
the upper facets expose which tails are present, while the lower facets expose
where those tails can move.  This gives the 31/26 boundary split a dynamical
interpretation rather than merely a counting interpretation.

The exact gauge-tail audit imposes an important separation between these two
layers.  Before augmentation it finds 2,316 nonzero origin terms whose
gauge-tail support is disconnected, occurring in all 48 partial
presentations.  Therefore a tail subset is **not** itself a connected Ward
trajectory.  Arbitrary subsets belong naturally to the upper/end-point part
of the multiplihedron; connected tubes belong to the propagation/collision
part.  A physical evaluation must map between them through kinetic insertions
and propagator transport.  Identifying the two indexing sets directly is
falsified.

Geometrically, \(\mathcal JG\) should be regarded provisionally as resolving
the collision strata of independent vertex-conversion times.  This is an
analogy with a blowup/wonderful compactification, not yet a proved geometric
identification for the Ward carrier.

## Homological-transfer trajectory

The closest established mathematical trajectory is:

\[
\text{strict chain-level dynamics}
\longrightarrow
\text{deformation retract / gauge reduction}
\longrightarrow
\text{transferred }A_\infty,L_\infty\text{ or modular structure}.
\]

A strict product or sewing operation rarely survives projection to a reduced
complex as a strict operation.  Homological perturbation instead generates a
primary map together with higher maps.  Associahedra organize the transferred
operations; multiplihedra organize the higher components of a morphism between
two such structures; stable graphs and the Feynman transform organize the
cyclic/modular extension.

The prospective Ward--Brauer dictionary should fit this template.  Introduce
a common BRST-resolved carrier \((\mathcal B,Q)\) and, provisionally, two cyclic
deformation-retract data sets

\[
\mathcal P
\underset{p_{\rm P}}{\overset{i_{\rm P}}{\rightleftarrows}}
\mathcal B
\underset{i_{\rm S}}{\overset{p_{\rm S}}{\rightleftarrows}}
\mathcal S,
\]

with homotopies satisfying

\[
1-i_{\rm P}p_{\rm P}=Qh_{\rm P}+h_{\rm P}Q,
\qquad
1-i_{\rm S}p_{\rm S}=Qh_{\rm S}+h_{\rm S}Q.
\]

Here \(\mathcal P\) is the physical-projector presentation and \(\mathcal S\)
the resolved surface presentation.  These retracts have not been constructed;
writing them states the missing theorem precisely.  If they exist and are
stable under Cuts, homological transfer produces the higher dictionary rather
than leaving every filler as independent fitted data.

On a fixed graph, the expected evaluation has the form

\[
\Phi_G
=
\sum_{U\in\operatorname{MarkedTub}(G)}
\epsilon(U)\,\operatorname{ev}_U,
\]

where thick regions use physical composition, thin regions use surface
composition, and each broken frontier inserts the transferred Ward homotopy.
The graph-multiplihedron boundary formula is then the chain-level statement
that this transferred map respects graph composition up to all coherent
homotopies.

This trajectory teaches four things:

1. the canonical object may be a contractible space of retract data, not a
   unique off-shell formula;
2. once a legitimate contracting homotopy is chosen, higher cells should be
   generated recursively rather than introduced ad hoc;
3. at tree level the obstruction is ordinary homology of the Ward transport
   complex, while at loops cyclicity and closed traces introduce a quantum or
   modular obstruction;
4. equality of amplitudes is only the induced cohomology statement and cannot
   select the chain-level dictionary.

### Maurer--Cartan packaging and the real obstruction

The collection \(\Phi=\{\Phi_G\}\) should be packageable as a Maurer--Cartan
element in a two-coloured convolution dg Lie or \(L_\infty\) algebra of
graphical operations.  Suppressing graph labels, its equation is

\[
d\Phi+\frac12[\Phi,\Phi]=0.
\]

The one-edge realization defect is the first component of this curvature.
The difference of the two two-edge transports is the next obstruction cycle.
At each stage the obstruction must vanish as a class in the **admitted**
Ward/curve complex; vanishing only after amplitude augmentation is not enough.

This clarifies the role of nonzero curvature in finite audits.  A nonzero
chain-level curvature that is filled by an admitted local higher cell is the
expected signature of genuine homotopy coherence.  Identically zero curvature
is consistent with a strict special case, but provides no evidence for the
missing higher geometry and can simply mean that the chosen quotient erased
it.  A nonzero homology class, by contrast, is a genuine obstruction.

The desired result is therefore neither ``curvature zero term by term'' nor
``some rational linear system has a solution.''  It is:

\[
\operatorname{Curv}(\Phi)
\ne 0\ \text{as a resolved chain},
\qquad
[\operatorname{Curv}(\Phi)]=0
\ \text{by a cut-natural cyclic filler}.
\]

The exact formal origin audit now realizes the first half of this diagnostic.
All 24 two-order coherence cycles are nonzero, remain nonzero after tensoring
with the \(\det H_1\) generator, and admit integral fillers made from triangles
and product squares in \((\Delta^2)^5\).  This proves that the observed
curvature has no obstruction in the freely contractible origin complex.  It
does not prove that any of those cells is the image of a Ward/BV or curve
generator.

The same audit finds a subtle equivariance fact.  The order-three road rotation
acts freely on the 243 origin points, producing 81 orbits.  Consequently the
augmentation of an invariant integral zero-chain lies in \(3\mathbb Z\).  An
edge-pointed contracting cone is integral and covariant as a family, but an
unpointed invariant cone obtained by averaging needs \(1/3\).  This is a
\(\mathbb Z/3\) obstruction for that particular formal origin-module
splitting—not yet a physical torsion theorem.  It may disappear after adding
the missing contact/ghost strata, or it may say that the natural object is the
road-pointed cover with descent data rather than its naïve invariant quotient.

At arbitrary topology, modular operads are naturally expressible as modules
over a Brauer properad, and their Feynman transform is a relative cobar
construction.  That existing framework is unusually well matched to the two
features present here: resolved metric pairings and graph-level sewing.  It is
therefore a better long-term target than an untyped ``operator algebra on
amplitudes.''

## Graph-Hodge skeleton of the marked theta

The vertex graph \(K_{2,3}\) has

\[
b_1(G)=|E|-|V|+1=6-5+1=2.
\]

This is exactly the number of closure edges left after choosing any spanning
tree.  At the purely combinatorial level, Ward transport should therefore be
compared with the graph chain sequence

\[
C_1(G)\xrightarrow{\partial}C_0(G),
\]

with the external transverse legs treated as relative sinks.  A spanning tree
\(T\) supplies a contracting flow \(h_T\) for the non-harmonic part.  If
\(e\notin T\) is a closure chord, then

\[
c_e=e-h_T\partial e
\]

is its fundamental cycle, with signs fixed by the chosen orientations.  The
two chords \(e,f\) give an integral basis \(c_e,c_f\) of \(H_1(G;\mathbb Z)\).

This elementary decomposition predicts the roles of the existing data:

- tree Ward transport is the contractible/exact sector;
- a first closure exposes one harmonic Ward circuit;
- the second closure exposes the full rank-two circuit sector;
- changing the spanning tree changes \(h_T\) by a harmonic-valued homotopy;
- the resolved Brauer circuit states must retain the harmonic sector rather
  than declaring it zero.

The actual ribbon graph is a spine of a genus-one surface with one boundary.
Consequently \(H_1\) carries a unimodular antisymmetric intersection form, and
the two fundamental cycles determine a generator

\[
c_e\wedge c_f\in\det H_1(G;\mathbb Z)\cong\mathbb Z.
\]

This is the canonical home for the antisymmetric two-closure datum.  More
precisely, the first unresolved curvature should be tested as a class

\[
\Omega_{ef}
\in
\det H_1(G)\otimes\mathcal L_{\rm Ward/curve},
\]

before pairing the determinant line with an orientation or applying the
scalar augmentation.  Swapping the closures or reversing the ribbon
orientation changes its sign.  A dihedrally symmetrized scalar audit can
therefore erase precisely the datum that distinguishes a genuine modular
2-cell from strict commutativity.

This yields a three-way diagnostic:

1. \(\Omega_{ef}=0\) already in the orientation-twisted resolved complex:
   the two-closure square is genuinely strict at this graph;
2. \(\Omega_{ef}\ne0\) as a chain but is the boundary of an admitted ribbon
   2-cell: the expected homotopy-coherent case;
3. \([\Omega_{ef}]\ne0\): a modular anomaly or a missing state in the
   coefficient system.

The determinant twist is not decorative.  Feynman-transform and graph-complex
constructions naturally carry graph-orientation lines.  The marked-theta test
should therefore be repeated with an orientation-twisted coefficient system
before interpreting zero asymmetric support as evidence for a cubical
strictification.

### Topological stages and the modular master equation

The ribbon topology of the four graph stages is forced by Euler
characteristic.  A thickened spanning tree is a disk.  Adding either first
chord produces an annulus.  Adding the second chord produces the known
once-punctured torus:

\[
(g,b)=(0,1)
\longrightarrow
(0,2)
\longrightarrow
(1,1).
\]

Thus either closure order realizes handle creation as a boundary-splitting
contraction followed by a boundary-joining contraction.  The final equality of
the two orders is a modular sewing relation, not merely associativity of an
ordinary product.

The natural global equation is consequently the quantum/modular enhancement
of the Maurer--Cartan equation,

\[
(d+\hbar\Delta)\Phi
+\frac12[\Phi,\Phi]=0.
\]

Here the bracket represents separating composition and \(\Delta\) represents
self-sewing/handle creation.  The marked theta is the first bounded carrier on
which the \(\Delta\)-term and its orientation line can be detected.  Computing
only the final commutative scalar trace projects this equation to its
augmentation and can make the modular term invisible.

## Desired equations

Let \(\Phi_E\) be the unresolved dictionary with a set \(E\) of open sewing
pairs.  For each \(e\in E\), seek a degree-one homotopy

\[
dH_e
=
\operatorname{Sew}^{\rm phys}_e\Phi_E
-
\Phi_{E\setminus e}\operatorname{Gl}^{\rm res}_e.
\]

For two distinct closures, the two composites of degree-one homotopies produce
a cycle.  With signs fixed by the orientation of the sewing square, seek

\[
dK_{ef}=\operatorname{Curv}_{ef}(H),
\]

where \(\operatorname{Curv}_{ef}(H)\) is the difference between transporting
then closing in the two orders.  Entry 54 proves that its augmentation is zero;
it does not prove that this cycle has a physically realized filler.

At arbitrary \(|E|\), codimension-one faces of the desired cell must be all
lower sewing/transport composites.  A factorizing family of such cells would
supply the full higher-coherence relations automatically.

## Pairing and modular completion

The scalar pairing requires the dictionary and all homotopies to be cyclic.
This is not an optional refinement: a noncyclic chain homotopy need not descend
through closed state evaluation.

The correct order remains

\[
\text{derived extraction/retract}
\longrightarrow
\text{cyclic dualizable carrier}
\longrightarrow
\operatorname{Mod}.
\]

Modular completion should be applied only after the derived dictionary has a
closed-state-compatible cyclic structure.  This parallels the already observed
noncommutation of primitive-symmetric gravity extraction and quantization.

## Non-vacuity criteria

A successful Ward--Brauer lift must satisfy all of the following:

1. degree-one generators are actual cubic Ward moves, not arbitrary edges;
2. coefficients are realized by endpoint-extension/curve data;
3. the kernel of the augmentation is acyclic in the composition-stable
   physical subcomplex, not merely in a freely adjoined resolution;
4. the homotopies are compatible with every partial Cut;
5. reference changes are boundaries in the same admitted complex;
6. two-closure curvature has an admitted integral or correctly localized
   filler;
7. cyclic and mapping-class symmetries act coherently;
8. the construction survives modular completion with resolved circuits.

## Sharp falsifiers

- A marked-theta residual not lying in the image of the local moving-Ward
  differential falsifies the proposed physical resolution.
- A nonzero two-closure class in the admitted degree-one homology falsifies
  homotopy-coherent naturality even though the final polynomial identity holds.
- A filler existing only after unrestricted rational averaging reveals a
  cyclic/integral obstruction rather than a canonical dictionary.
- A filler destroyed by a physical Cut is presentation bookkeeping, not a
  factorization-natural carrier map.

## Immediate work split

- Mathematical thread: fix the painted Ward-carrier definitions, signs,
  cyclic pairing, and obstruction groups.
- Exact certificate A: test membership of every marked-theta residual in the
  image of the physically generated local Ward differential.
- Exact certificate B: construct one-edge homotopies, compute two-closure
  curvature, and audit integral/equivariant fillers.

The next conceptual milestone is not another amplitude equality.  It is the
first non-tautological painted Ward cell whose geometric boundary is the
one-edge realization defect.

## Sharper theorem target: a cyclic homological-perturbation comparison

The two-retract proposal becomes predictive only after putting the
interactions on a bar/cobar or Feynman-transform carrier.  Let

\[
\mathbf D=\mathbf Q+\boldsymbol\delta
\]

be the square-zero coderivation on a suitably coloured cofree carrier built
from the scalar first jet.  Here \(\mathbf Q\) is the linear BRST/kinetic
differential and \(\boldsymbol\delta\) contains the cubic, quartic, and higher
graph-composition data.  Suppose, before the perturbation, that there are two
cyclic contractions

\[
(\mathcal P,d_{\rm P})
\underset{p_{\rm P}}{\overset{i_{\rm P}}{\rightleftarrows}}
(\mathcal B_{\rm jet},\mathbf Q)
\underset{i_{\rm S}}{\overset{p_{\rm S}}{\rightleftarrows}}
(\mathcal S,d_{\rm S})
\]

with homotopies \(h_{\rm P}\) and \(h_{\rm S}\).  Under the usual filtered
nilpotence/completeness hypothesis, the basic perturbation lemma gives

\[
I_a^{\delta}=(1-h_a\boldsymbol\delta)^{-1}i_a,
\qquad
P_a^{\delta}=p_a(1-\boldsymbol\delta h_a)^{-1},
\qquad a\in\{\mathrm P,\mathrm S\}.
\]

The candidate full dictionary is therefore not an independently fitted
collection of graph maps.  It is the single transferred comparison

\[
\boxed{
\Phi_{\mathrm P\to\mathrm S}
=
P_{\rm S}^{\delta}I_{\rm P}^{\delta}
=
p_{\rm S}(1-\boldsymbol\delta h_{\rm S})^{-1}
(1-h_{\rm P}\boldsymbol\delta)^{-1}i_{\rm P}.}
\]

Expanding the two geometric series produces painted trees: vertices carry
interaction coderivations, internal edges carry one of the contracting
homotopies, and the paint frontier records the change of retract.  This is
the established mechanism by which multiplihedra arise.  With self-sewings
allowed, the same expansion must be taken in the cyclic/modular Feynman
transform and produces decorated stable graphs rather than trees.

This formula is still a theorem *target*, because neither cyclic contraction
has yet been constructed from scalar normal geometry.  But it sharply reduces
the unknown data.  One must construct \(i_a,p_a,h_a\) and prove compatibility
with the scalar pairing and Cuts; the higher maps are then forced recursively.

For a degree-zero cyclic pairing \(\langle-,-\rangle\), the required side
conditions are, with the appropriate graded signs,

\[
p_a=i_a^\dagger,
\qquad
\langle h_ax,y\rangle
+(-1)^{|x|}\langle x,h_ay\rangle=0.
\]

Cut compatibility is stronger than commuting after cohomology.  At the linear
level it should contain

\[
\operatorname{Cut}\,i_a=(i_a\otimes i_a)\operatorname{Cut},
\qquad
\operatorname{Cut}\,p_a=(p_a\otimes p_a)\operatorname{Cut},
\]

and a tensor-contraction identity of Alexander--Whitney type,

\[
\operatorname{Cut}\,h_a
\simeq
\bigl(h_a\otimes1+i_ap_a\otimes h_a\bigr)
\operatorname{Cut},
\]

with the two possible orders related by the next higher homotopy.  The formal
interval coalgebra already realizes this equation, but the homotopy must be
an actual scalar-first-jet Ward/contact operation for it to be non-vacuous.
Graph multiplihedra are the candidate universal carriers of these iterated
tensor-homotopy choices.

### Lowest morphism equations and where contact terms belong

Let \(m_r^{\rm P}\) and \(m_r^{\rm S}\) denote the transferred colour-ordered
operations, and let \(F_r\) be the Taylor components of \(\Phi\).  Suppressing
Koszul signs, the arity-two equation is

\[
F_1m_2^{\rm P}
-m_2^{\rm S}(F_1\otimes F_1)
=d_{\operatorname{Hom}}F_2.
\]

This is the correct type of the one-edge realization defect.  The moving Ward
homotopy is a candidate contribution to \(F_2\), not a map directly into the
top cubic-origin module.

At arity three the equation contains

\[
F_1m_3^{\rm P}-m_3^{\rm S}(F_1^{\otimes3}),
\qquad
F_2(m_2^{\rm P},1),\quad F_2(1,m_2^{\rm P}),
\qquad
m_2^{\rm S}(F_1,F_2),\quad m_2^{\rm S}(F_2,F_1),
\]

and their signed permutations; their sum must be
\(d_{\operatorname{Hom}}F_3\).  In a cubic/quartic Yang--Mills presentation,
the quartic/contact vertex lives precisely in the \(m_3\) part of this
identity.  Therefore a cubic-only origin complex cannot be closed under the
first nontrivial coherence equation.

The elementary off-shell Ward identity is the local shadow of this statement:

\[
k_0^\mu V_{\mu\nu\rho}(k_0,k_1,k_2)
=P_{\nu\rho}(k_2)-P_{\nu\rho}(k_1),
\qquad
P_{\nu\rho}(k)=k^2\eta_{\nu\rho}-k_\nu k_\rho.
\]

After composition with a propagator, each \(P D\) splits into an identity
edge-contraction term and a longitudinal transport term.  The first changes
graph type and lands on a contact stratum; the second carries the Ward mark to
the next vertex.  This explains simultaneously why the on-shell exit-tensor
differential was correctly computed and why it could not land in the 243
cubic origins.

### The flag-incidence Ward sequence

The independent-exit audit is deliberately too large at an internal edge.  A
longitudinal rank-two insertion propagated from either endpoint is

\[
L_e(k)=\frac{k\otimes k}{k^2},
\qquad L_e(-k)=L_e(k).
\]

Thus the first physically motivated edge relation is the coequalizer

\[
Q_{(v,e)}=Q_{(w,e)},\qquad e=\{v,w\},
\]

with the equality sign appropriate to the rank-two longitudinal projector.
This relation must be derived as a gluing map in the eventual BV carrier, but
its graph algebra can already be isolated exactly.

Let \(F(G)=\{(v,e):v\in e\}\) be the set of flags of a finite connected
graph with at least one edge, and define

\[
s:\mathbb Z^{F(G)}\longrightarrow\mathbb Z^{V(G)},
\qquad
s(a)_v=\sum_{e\ni v}a_{v,e}.
\]

The module of local Ward choices modulo the local cyclic/constant relation is

\[
\mathsf W_1(G)=\ker s
=\bigoplus_{v\in V(G)}
\widetilde{\mathbb Z}^{\,E(v)}.
\]

Define the edge map

\[
t:\mathsf W_1(G)\longrightarrow\mathbb Z^{E(G)},
\qquad
t(a)_e=a_{v,e}+a_{w,e},\quad e=\{v,w\}.
\]

This is exactly the contact differential, and after endpoint coequalization
the longitudinal differential is its negative.  A local Ward mark comparing
two exits therefore maps to a difference

\[
(C_{e_1}-L_{e_1})-(C_{e_2}-L_{e_2}).
\]

There is a canonical integral exact sequence

\[
\boxed{
0\longrightarrow H_1(G;\mathbb Z)
\longrightarrow\mathsf W_1(G)
\xrightarrow{\ t\ }\mathbb Z^{E(G)}
\xrightarrow{\ \sum_e\ }\mathbb Z
\longrightarrow0.}
\]

One proof identifies \(F(G)\) with the edges of the barycentric subdivision
of \(G\).  The two maps \(s\) and \(t\) are its two endpoint maps.  Restricting
to \(\ker s\) eliminates the original-vertex zero-chains; the remaining
kernel is the ordinary cycle lattice.  Equivalently, local differences of
adjacent edges generate the sum-zero edge lattice because the line graph of a
connected graph is connected.

For \(K_{2,3}\),

\[
\operatorname{rank}\mathsf W_1=2|E|-|V|=7,
\quad
\operatorname{rank}t=|E|-1=5,
\quad
\operatorname{rank}\ker t=|E|-|V|+1=2.
\]

These are exactly the ranks seen in the off-shell audit.  Keeping twelve
endpoint exits independent makes the contact-plus-exit map artificially
injective and turns each circuit into an eight-exit remainder.  Under the
edge coequalizer, the remainder is a sum of
\(Q_{(v,e)}-Q_{(w,e)}\) and vanishes.  The two circuit directions then survive
as genuine Ward homology rather than as failures of telescoping.

This substantially changes the interpretation of the next state.  The
harmonic Ward sector should not automatically be killed by ghosts or quartic
vertices.  It should first map to the resolved Brauer closed-curve sector,

\[
H_1(G)\longrightarrow
\mathsf{Circuits}^{\rm res}(G),
\]

and its determinant line should carry the first handle-coherence class.
Quartic and ghost/antifield strata are still required by the full BV action
and by graph-changing/cyclic completion, but the independent-exit remainder
alone is not evidence that they must cancel these circuit classes.

### Mixed variance under sewing

The graph-addition result and the Ward exact sequence fit together with
opposite variances.  For \(G\subset H\) on the same vertex set, marked tubing
cells restrict by the deletion carrier

\[
r_{H,G}:C_*(\mathcal JH)\longrightarrow C_*(\mathcal JG),
\]

whereas circuits extend covariantly,

\[
j_{G,H}:H_1(G)\hookrightarrow H_1(H).
\]

Adding a non-bridge edge to a connected graph gives

\[
0\longrightarrow H_1(G)
\xrightarrow{j_{G,H}}H_1(H)
\longrightarrow\mathbb Z\longrightarrow0.
\]

The quotient is the new sewing circuit.  A spanning tree chooses a fundamental
cycle and hence a splitting, but the extension and its determinant line are
canonical without that choice.

Therefore the decorated graph-multiplihedral carrier is not an ordinary
constant-coefficient diagram.  It is bivariant: cells pull back under edge
deletion while harmonic/Brauer states push forward under edge addition.  The
required coefficient maps should obey a projection or Beck--Chevalley law.
For the marked theta this is exactly the sequence

\[
0\longrightarrow0
\longrightarrow H_1(T+e)\cong\mathbb Z
\longrightarrow H_1(K_{2,3})\cong\mathbb Z^2,
\]

along either route, with the final antisymmetric datum in
\(\det H_1(K_{2,3})\).  This identifies where a genuinely nonzero two-sewing
class can live even though the undecorated cellular deletion square commutes
strictly.

The correct homological package for one new circuit is the distinguished
triangle of graph chains

\[
C_*(G)\longrightarrow C_*(H)
\longrightarrow C_*(H,G)\xrightarrow{+1}.
\]

If \(H=G+e\) and both graphs are connected, then
\(H_1(H,G)\cong\mathbb Z\), and the long exact sequence identifies

\[
H_1(H)/H_1(G)\cong H_1(H,G).
\]

Thus a sewing edge creates a canonical **relative** circuit class even when no
spanning-tree representative has been chosen.  For two added edges the
relative group is rank two and its determinant gives the orientation line
seen in the marked-theta audit.  This is closer to nearby/vanishing-cycle
behavior than to a strict endomorphism of amplitudes.

A compact candidate for the undecorated total carrier is consequently a
derived coend.  Let \(\mathcal P(E)\) be the Boolean edge-addition category,
let

\[
R(S)=C_*(\mathcal J(T\cup S))
\]

be its right module via the marked deletion maps, and let

\[
L(S)=C_*(T\cup S,T)
\]

be its left relative-graph-chain module.  Then the sewing-order/circuit
skeleton is

\[
\boxed{
\mathfrak W(T;E)
=R\overset{\mathbb L}{\otimes}_{\mathcal P(E)}L
=B_\bullet(R,\mathbb Z[\mathcal P(E)],L).}
\]

The bar direction records sewing order, the graph-multiplihedron resolves the
paint/Ward conversion, and the relative graph chain records the circuit born
under sewing.  This formula is a structural proposal, not yet the physical
Ward--Brauer carrier: it still needs the scalar-derived coefficient cosheaf,
the BV/contact differential, and the cyclic pairing.  Its value is that it
types the previously informal double mapping cylinder as a standard derived
tensor of opposite-variance data.

### What would actually be canonical

Even a successful construction need not select a unique off-shell integrand.
Changing a contraction changes \(\Phi\) by a higher homotopy while preserving
its induced cohomology class.  The plausible canonical object is therefore
the homotopy type (or contractible groupoid, when it is contractible) of
cyclic Cut-compatible contractions, not a distinguished point in that space.

Ordinary cyclic homological transfer controls trees.  Modular completion
requires more: the homotopies must be adjoint-compatible with the cyclic
pairing, and the quantum/unimodular obstruction must vanish.  Thus an ordinary
SDR does not by itself prove the loop statement.  The determinant-line class
on the marked theta is the first bounded test of this extra modular condition.

The lowest decisive falsifier is now precise.  Enlarge the cubic carrier only
by the kinetic/contact/ghost strata forced by the BV differential.  If the
arity-two defect is not \(d_{\operatorname{Hom}}\)-exact there, the proposed
two-retract dictionary fails at its first component.  If it is exact but the
arity-three curvature is nontrivial in cyclic Cut-compatible homology, the
tree comparison exists but does not extend coherently.

## Position relative to the primitive half-object frontier

The rank-jump half-object \(\mathsf J\) is no longer the open genus-zero
problem described in the original session brief.  Ledger entries 38--39 give
the scalar occurrence-decorated Pochhammer/Cousin carrier, its nearby-cycle
unit, pre-pairing factorization, and the derived Verdier index-raising
identification with \([({\rm Pf}'A)^2]\).  The present Ward--Brauer work is the
next operator/dictionary frontier: obtain for the Yang--Mills lowering and
surface realizations the same passage from a canonical derived class to a
factorization-natural chain comparison, and only then modularly complete it.

## Revised master principle: carrier plus dictionary

The talk's repeated separation between a self-factorizing mathematical object
and the dictionary that turns its factorization into amplitudes forces a
refinement of the session's master principle.  A derived normal sector by
itself is not yet the full theory-producing datum.  Write

\[
\partial\mathcal F_E
\simeq
\coprod_D\mathcal F_{E_L(D)}\times\mathcal F_{E_R(D)}
\]

for a self-factorizing carrier and let

\[
V_E:C_*(\mathcal F_E)\longrightarrow\mathcal A_E
\]

be its valuation/dictionary into a physical state or amplitude complex.  The
required relation is not necessarily strict monoidality but a cyclic coherent
system

\[
V_E|_D
\simeq
\operatorname{Sew}_D(V_{E_L}\otimes V_{E_R}),
\]

with all higher compatibilities represented before augmentation.  The quantum
theory is then schematically

\[
\boxed{
\mathsf T_E
=
\operatorname{Mod}(\mathcal F_E,V_E),
\qquad
(\mathcal F_E,V_E)
=
\operatorname{DerivedNormal}_E(\mathrm{Scalar}).}
\]

The previous slogan—modular completion of a dualizable derived normal
sector—is recovered only when the dictionary is unique or has been left
implicit.  The present audits show why it cannot generally be suppressed:

- the summed physical and surface valuations agree;
- the diagonal map on raw origins does not;
- graph-multiplihedral cells organize candidate higher components of the
  comparison;
- Ward homology retains circuit data needed before closed-state evaluation.

The primitive half-objects \(\mathsf C,\mathsf G,\mathsf J\) should therefore
be viewed at least as derived dictionary kernels or coefficient objects on a
common self-factorizing carrier, not merely as scalar functions.  Their
pairing table is the shadow, after valuation, of composition in this carrier
category.

This reformulation also makes the Marici--Cintamani bridge sharper.  The
carrier is the abstract task/composition grammar; a dictionary is a physical
realization of that grammar.  Nima classifies carrier/dictionary pairs that
produce field theories, while Cintamani can ask which substrates implement
the same compositional maps natively and at low physical cost.

### Candidate global language: a decomposition space with coefficients

There is a more economical way to package the repeated Cut coherences.  Form
a simplicial groupoid \(\mathcal X_\bullet^{\rm sc}\) whose one-simplices are
resolved scalar carrier objects and whose \(r\)-simplices are flags of \(r-1\)
compatible decompositions/Cuts, retaining automorphisms and ribbon data.  The
appropriate axiom is plausibly not an ordinary Segal composition axiom but a
unital **2-Segal/decomposition-space** axiom: every polygonal decomposition of
a multi-Cut must reconstruct the same homotopy pullback of lower pieces.

This language was designed precisely so that coherent decomposition gives an
incidence coalgebra at the objective/homotopy level, with ordinary algebraic
identities appearing only after linearization or homotopy cardinality
(<https://arxiv.org/abs/1212.3563>,
<https://arxiv.org/abs/1512.07573>).  Applied here, its incidence coproduct
would be the unresolved Cut coaction.

The proposal is:

\[
\boxed{
\begin{aligned}
\text{scalar master carrier}
&\rightsquigarrow
\text{cyclic/modular decomposition space }\mathcal X^{\rm sc},\\
\text{derived normal sector}
&\rightsquigarrow
\text{dualizable coefficient system }\mathcal E
\text{ on }\mathcal X^{\rm sc},\\
\text{physical dictionary}
&\rightsquigarrow
\text{coherent morphism/module of decomposition spaces},\\
\text{amplitude}
&\rightsquigarrow
\text{linearized incidence character/pairing}.
\end{aligned}}
\]

This is a candidate framework, not a theorem about the current surface
formalism.  It makes several existing facts look nonaccidental:

- associahedra and the all-rank block-face theorem supply the higher
  parenthesization cells at genus zero;
- graph multiplihedra govern morphisms between two coherent realizations;
- strict physical Cut coactions are the linearized coalgebra shadow;
- the marked-theta determinant class is the first modular/ribbon extension;
- the scalar pairing is a pairing of coefficient systems rather than a
  separately appended matrix kernel.

It also gives a concrete falsification program.  Define
\(\mathcal X_0,\mathcal X_1,\mathcal X_2,\mathcal X_3\) from the actual
occurrence-resolved scalar surface carrier.  The first nontrivial requirement
is that both triangulations of the decomposition quadrilateral give a
homotopy-pullback square.  At the coefficient level this is the mixed
Beck--Chevalley identity already proved for the genus-zero scalar/QTDS
envelope.  The marked-theta version must include the relative circuit module
and determinant local system.  Failure there would show that the ordinary
decomposition-space language is too small and must be replaced by a genuinely
modular/properadic analogue.

### Circuit homology is a quotient of resolved curves, not a canonical curve basis

The rank-two Ward kernel must be typed more carefully than the provisional
arrow

\[
H_1(G)\longrightarrow\mathsf{Circuits}^{\rm res}(G).
\]

For a ribbon graph \(G\) with thickening \(\Sigma_G\), there is a canonical
homology identification

\[
H_1(G;\mathbb Z)\cong H_1(\Sigma_G;\mathbb Z).
\]

There is also a canonical **class map** in the opposite direction, from an
oriented resolved embedded circuit to its homology class,

\[
\operatorname{cl}_G:
C_0\bigl(\mathsf{Curv}^{\rm res}(\Sigma_G)\bigr)
\longrightarrow H_1(G;\mathbb Z).
\]

What is generally absent is a canonical additive section of this map.  On the
once-punctured torus, two primitive generators \(a,b\in H_1\) have
intersection

\[
\omega(a,b)=\pm1.
\]

Each generator has an embedded representative, but the two representatives
cannot form one non-overlapping curve cover.  Moreover an unoriented Brauer
loop forgets the sign of a homology generator.  Consequently a rank match
between Ward homology and resolved circuits does not define the physical
coefficient map.

The correctly typed target is a homotopy-coherent lift

\[
\sigma_G:
H_1(G;\mathbb Z)
\rightsquigarrow
C_*\bigl(\mathsf{Curv}^{\rm res}(\Sigma_G)\bigr),
\qquad
\operatorname{cl}_G\sigma_G\simeq\operatorname{id},
\]

not a strict basis identification.  Intersecting representatives require a
degree-one crossing/resolution generator whose boundary compares the two
smoothings.  Before its physical coefficients are known, the minimal formal
shape is

\[
dX_{a,b}=R_+(a,b)-R_-(a,b).
\]

This is a Brauer--skein type enrichment, not yet a claim that the physical
relation is a Kauffman bracket or that both coefficients equal one.  Reflection
changes the sign of

\[
a\wedge b\in\det H_1(G),
\]

which matches the determinant parity found in the marked-theta sewing audit.
Thus the former two-order ``curvature'' is better interpreted as the first
intersection/coherence cell of the curve lift.

This suggests a sharper coefficient diagram:

\[
\begin{matrix}
\mathsf W_1(G)&\twoheadrightarrow&H_1(G)\\
&&\uparrow\scriptstyle{\operatorname{cl}_G}\\
&&C_*\bigl(\mathsf{Curv}^{\rm res}(\Sigma_G)\bigr),
\end{matrix}
\]

where the dashed inverse is supplied only up to higher homotopy and must be
natural under graph sewing and physical Cut.  The immediate falsifier is now
precise: determine whether the actual resolved Brauer/surface carrier already
contains the required crossing/smoothing cell.  If it does not, the carrier
must be enlarged before a Ward--Brauer dictionary can exist.

### Exact marked-theta circuit audit

The circuit calculation makes the preceding obstruction integral and
equivariant.  Orient the six edges from each core vertex to each road vertex,
ordered by road and then core.  A cycle is uniquely

\[
c(p,q)=(p,-p,q,-q,-p-q,p+q).
\]

In the seven-coordinate Ward quotient

\[
(l_{00},l_{01},l_{10},l_{11},q_0,q_1,q_2),
\]

the saturated integral intertwiner is

\[
\Theta(c(p,q))
=(q,-p,-q,p,-p,-q,p+q).
\]

It is an \(S_2\times D_3\)-equivariant isomorphism

\[
H_1(K_{2,3};\mathbb Z)\cong\ker t.
\]

All 24 spanning-tree chord generators map individually to one of three
populated oriented circuit supports.  The 9 formal-\(D\) contraction states
split into these three supports with multiplicity three each.

Let their oriented classes be \(c_{01},c_{12},c_{20}\).  Then

\[
c_{01}+c_{12}+c_{20}=0.
\]

Thus the tag-class map \(\mathbb Z^3\twoheadrightarrow H_1\) has diagonal
kernel.  The canonical \(D_3\)-equivariant rational section is determined by

\[
3\sigma(p,q)
=(p-q,\ p+2q,\ -2p-q).
\]

The associated integral splitting lattice has index three.  Hence there is no
integral \(D_3\)-equivariant additive section, although non-equivariant
integral splittings exist.  Moreover every pair of the three primitive tags
has intersection number of absolute value one, while none of the 243
noncrossing resolved states contains two closed circuits.

This explains two earlier observations at once:

1. the appearance of \(1/3\) under unpointed road-rotation averaging is not
   merely an artifact of the formal origin simplex; it is already present in
   the equivariant circuit-tag extension;
2. the determinant sign under exchanging the two sewing orders is the
   orientation character of \(\det H_1\), not unexplained curvature of the
   bare cellular carrier.

The strict/non-strict boundary is therefore sharper:

\[
\boxed{
\begin{aligned}
\text{marked cellular deletion}&:\text{strict (finite evidence through }n=5),\\
\text{Ward kernel}\leftrightarrow H_1&:\text{strict and integral on }K_{2,3},\\
H_1\rightsquigarrow\text{resolved curves}&:\text{derived; crossing cell required}.
\end{aligned}}
\]

### Do not split the circuit-tag extension

The index-three result has a positive interpretation.  Let

\[
\mathsf T_{\rm circ}
=\mathbb Z\langle c_{01},c_{12},c_{20}\rangle
\]

be the oriented tag module and let \(\mathsf K_{\rm rel}\) be the rank-one
symmetry module spanned by their diagonal relation.  There is a canonical
short exact sequence of integral symmetry modules

\[
\boxed{
0\longrightarrow\mathsf K_{\rm rel}
\xrightarrow{\ \Delta\ }
\mathsf T_{\rm circ}
\xrightarrow{\ \operatorname{cl}\ }
H_1(K_{2,3};\mathbb Z)
\longrightarrow0,
\qquad
\Delta(1)=c_{01}+c_{12}+c_{20}.}
\]

The failure is only the failure of an integral equivariant **splitting**.
Therefore the correct additive coefficient object is the two-term free
resolution

\[
\mathcal R_{\rm circ}
=
\bigl[
\mathsf K_{\rm rel}
\xrightarrow{\Delta}
\mathsf T_{\rm circ}
\bigr],
\]

whose surviving homology is \(H_1(K_{2,3})\).  A derived Ward--curve
dictionary may compare the Ward kernel directly with
\(\mathcal R_{\rm circ}\); it need never choose the rational section with
denominator three.

This also separates additive from multiplicative coherence.  The relation
generator one degree above the three tags is required already to present
homology integrally.  A genuine crossing/smoothing operation is additionally
required when two intersecting tags are composed as curve-cover states.
Whether the relation generator is physically realized by a Farey/\(3S\) cell,
a Brauer--skein smoothing, or a BV contact stratum is the next calculation,
not something fixed by the lattice alone.

There is nevertheless a precise topological candidate.  On a one-holed torus,
isotopy classes of essential curves are the vertices of the Farey graph, an
\(S\)-move joins curves intersecting once, and Hatcher's pants complex fills
each three-move cycle by a \(3S\) triangle
(<https://arxiv.org/abs/math/9906084>).  The three marked-theta tags therefore
form the vertex set of one such triangle.  This is not yet the desired chain
map: the boundary of the \(3S\) cell is a cycle of **moves**, whereas
\(\Delta(1)\) is a relation among oriented curve classes.  A degree shift and
an explicit incidence map from moves to tag coefficients are still required.
Thus “the filler is the \(3S\) cell” is a well-typed conjecture only after
that comparison is constructed.

The character of \(\mathsf K_{\rm rel}\) must be audited independently rather
than identified automatically with \(\det H_1\).  Core exchange reverses each
oriented circuit tag but acts by \(+1\) on \(\det H_1\); an extra orientation
twist may therefore be required in the physical coefficient system.

### The all-\(m\) \(A\)-type circuit resolution

The marked-theta extension is the \(m=3\) instance of a general lattice
theorem.  For \(K_{2,m}\), orient the \(2m\) edges from the two cores toward
the \(m\) roads.  Then

\[
H_1(K_{2,m};\mathbb Z)
\cong
A_{m-1}
=
\{a\in\mathbb Z^m:\sum_i a_i=0\}.
\]

Let \(t_i\) be the oriented circuit using adjacent roads \(i,i+1\), and set

\[
B(t_i)=e_i-e_{i+1}.
\]

The map \(B:\mathbb Z^m_{\rm tags}\to A_{m-1}\) is surjective and has
diagonal kernel, giving the saturated dihedral resolution

\[
\boxed{
0\longrightarrow\mathbb Z_{\chi_{\rm rel}}
\xrightarrow{1\mapsto(1,\ldots,1)}
\mathbb Z^m_{\rm tags}
\xrightarrow{B}
A_{m-1}
\longrightarrow0.}
\]

If \(A_{m-1}^{\rm tag}\subset\mathbb Z^m\) is the sum-zero tag lattice, then

\[
A_{m-1}/B(A_{m-1}^{\rm tag})\cong\mathbb Z/m,
\]

so

\[
\operatorname{SNF}(B|_{A_{m-1}^{\rm tag}})
=(1,\ldots,1,m).
\]

The unique rotation-equivariant rational section lands in the sum-zero tag
space and has exact denominator \(m\).  Hence the recurring denominator is
not accidental arithmetic; it is the index of the natural root lattice
inside the cyclic tag extension.  The integral solution at every arity is to
retain the nonsplit two-term resolution.

The relation character is

\[
\chi_{\rm rel}(\text{rotation},\text{reflection},\text{core swap})
=(+1,-1,-1),
\]

while

\[
\det(g|_{H_1})
=
\operatorname{sgn}(g|_{\rm roads})
(-1)^{(m-1)\operatorname{core\ swap}(g)}.
\]

These formulas are proved algebraically for every \(m\ge2\) and audited
exactly through \(m=12\).  Their physical interpretation is still
conditional: a scalar-derived coefficient map has only been studied on the
\(m=3\) marked theta, not constructed on the general family.

### Road-polygon Hodge resolution

The all-\(m\) sequence is literally the augmented cellular chain complex of
the oriented road polygon \(C_m\):

\[
0\longrightarrow H_1(C_m)
\longrightarrow C_1(C_m)
\xrightarrow{\partial}
\widetilde C_0(C_m)
\longrightarrow0.
\]

The unique rational cyclic-equivariant, zero-circulation section is the
discrete Green current

\[
\sigma_{\mathbb Q}=\delta\Delta^{-1},
\qquad
\delta=\partial^T,
\qquad
\Delta=\partial\delta.
\]

Its integral obstruction is the critical group

\[
\operatorname{Jac}(C_m)
=
\operatorname{Div}^0(C_m)/\Delta C_0(C_m)
\cong\mathbb Z/m.
\]

This explains the exact denominator \(m\).  It does not obstruct arbitrary
integral flow solutions; it obstructs the symmetric gradient/zero-circulation
choice.  Adding one oriented polygon cell with boundary
\(t_0+\cdots+t_{m-1}\) kills the relation cycle integrally and avoids choosing
that rational split.

At \(m=3\), the same Green matrix occurs in the six-point QTDS polarity flow.
This is the first exact common incidence grammar seen in the rank-jump and
first-jet sectors.  Equality of matrices is not yet a physical comparison:
the QTDS contact source, the Ward source, and their orientation characters
still require a scalar-derived chain map.

### The primitive is the flow torsor, not the inverse Laplacian

For any finite connected cellular complex \(K\) and any realizable source
\(c\in B_0(K)\), define

\[
\operatorname{Flow}_K(c)
=
\{j\in C_1(K):\partial j=c\}/B_1(K).
\]

There is a canonical exact sequence

\[
0\longrightarrow H_1(K)
\longrightarrow C_1(K)/B_1(K)
\xrightarrow{\bar\partial}B_0(K)
\longrightarrow0,
\]

so \(\operatorname{Flow}_K(c)\) is an \(H_1(K)\)-torsor.  This derived fiber is
integral and strictly functorial for cellular chain maps.  A Green operator
selects one rational point only after choosing an inner product and the
orthogonal gauge.

For a chain map \(f:K\to L\), Green sections have defect

\[
\kappa_f(c)
=f_1s_K^G(c)-s_L^G(f_0c)
\in H_1(L),
\]

and obey the cocycle identity

\[
\kappa_{gf}=g_*\kappa_f+\kappa_gf_0.
\]

Thus strict Cut naturality belongs to the flow torsor.  The failure of a
chosen inverse Laplacian to commute with Cut is harmonic comparison data, not
automatically an anomaly.  Under a change of torsor section it changes by a
categorical coboundary.  The invariant question is whether that class admits a
cyclic, factorization-local filler.

The revised candidate common primitive is therefore

\[
\operatorname{ResolveDiv}_K(c)
=
\operatorname{hofib}_c
\bigl(C_1(K)/B_1(K)\xrightarrow{\bar\partial}B_0(K)\bigr),
\]

not \(\delta\Delta^{-1}\) itself.  The immediate falsifier is a typed
\(m=3\) comparison between the QTDS and Ward source maps, including the deck/
orientation character, the polygon relation cell, and one physical Cut.

### The exact six-point suspension bridge

The carrier part of that comparison now closes. Entry 21's two scalar polarity
tripods have cores \(E_+,E_-\), common road endpoints
\(R_3=\{b_0,b_1,b_2\}\), and legs \(\gamma_i^\varepsilon\). Contracting each
subdivided leg gives

\[
U_+\cup_{R_3}U_-=S^0*R_3=K_{2,3}.
\]

Because the two tripods are contractible, Mayer--Vietoris supplies a canonical
integral suspension isomorphism

\[
\Gamma:\widetilde H_0(R_3;\mathbb Z)
\xrightarrow{\sim}H_1(K_{2,3};\mathbb Z),
\qquad
\Gamma(c)=\sum_i c_i(e_{+i}-e_{-i}).
\]

For the QTDS contact vector \(\sum_i c_i=0\), the two scalar primitives

\[
\eta_6^\varepsilon=\sum_i c_i\gamma_i^\varepsilon
\]

have the same boundary, and

\[
\eta_6^+-\eta_6^-\longmapsto\Gamma(c).
\]

Thus the Ward harmonic class is, at this carrier level, the transgression of
the ambiguity between the two scalar polarity primitives. An adjacent road
tag maps to the corresponding four-circuit, so individual support fixes the
abstract comparison parameters to \(a=1,b=0\). The map is equivariant under

\[
D_6\cong S_2\times S_3=\operatorname{Aut}(K_{2,3}),
\]

with polarity exchange identified intrinsically with exchange of the two
suspension cores.

Composing \(\Gamma\) with the exact Ward bridge \(\Theta\) gives an explicit
integral map from all six symbolic QTDS boundary-variable columns into the
seven-coordinate Ward kernel. Every column is killed by the Ward contact map,
and the result intertwines the order-six rotation and reflection actions.
This is a coefficient-module theorem, not yet a derivation by the scalar first
normal jet.

The physical comparison is still open. The first-jet kinetic/BRST map, an
oriented annulus/open-curve Cut target, and the image of the road relation
generator remain missing. In particular, a QTDS physical pole residue cannot
be equated directly with the existing punctured-torus edge-Cut count.

The conceptual extrapolation is that derived theories may occur as
Cech/Mayer--Vietoris obstruction classes of atlases of scalar-derived local
dictionaries. This is now an exact low-point pattern and an open all-arity
hypothesis.

### The all-\(m\) suspension skeleton

The carrier theorem extends without qualification to every \(m\ge2\). For a
discrete road set \(R_m\),

\[
K_{2,m}=S^0*R_m
=\operatorname{Cone}_+(R_m)\cup_{R_m}\operatorname{Cone}_-(R_m),
\]

and reduced Mayer--Vietoris gives the saturated integral isomorphism

\[
\Gamma_m:
A_{m-1}=\widetilde H_0(R_m;\mathbb Z)
\xrightarrow{\sim}
H_1(K_{2,m};\mathbb Z),
\qquad
\Gamma_m(c)=\sum_i c_i(e_{+i}-e_{-i}).
\]

Equivariantly,

\[
H_1(K_{2,m};\mathbb Z)
\cong
\operatorname{sgn}_{S_2}\boxtimes A_{m-1}.
\]

Projection to the plus-core edge coefficients is the integral inverse. The
map is natural for maps of road sets and fully \(S_2\times S_m\)-equivariant.
Only the adjacent-tag presentation chooses a cyclic order and reduces the
road symmetry to \(D_m\).

Composing the road-polygon boundary with suspension gives

\[
0\longrightarrow H_1(C_m)
\longrightarrow C_1(C_m)
\xrightarrow{\Gamma_m\partial}
H_1(K_{2,m})
\longrightarrow0,
\]

and each road tag maps to its individually supported adjacent four-circuit.
The same reduced source \(c\) therefore branches in two ways:

\[
c\rightsquigarrow\operatorname{Flow}_{C_m}(c)
\qquad\text{and}\qquad
c\mapsto\Gamma_m(c).
\]

The first is a local primitive problem and forms an integral flow torsor; the
Green current is a rational gauge choice. The second is a canonical global
transgression. At \(m=3\), scalar geometry realizes both branches and
\(\eta_6^+-\eta_6^-\) becomes \(\Gamma_3(c)\).

The exact all-\(m\) theorem is graph/cellular. The proposed scalar
\(m=4\) realization has now been falsified: at eight points the literal
core-incidence contraction produces \(K_{2,8}\), while each marked physical
boundary recovers \(K_{2,3}\). Thus \(m\) is local extension valence in the
physical-core poset, not half the external multiplicity. The remaining
physical problem is a suspension/Gysin comparison between these local links.

This adds a candidate operation to the scalar calculus:

\[
\operatorname{Trans}_{\mathcal U,\mathcal E}
=\delta_{\rm MV},
\]

and, for larger atlases, hyperhomology of the Cech/derived-descent complex.
The emerging structure is therefore a homotopy-coherent dictionary between
self-factorizing carriers, not a strict unary operator algebra on final
amplitudes.

### Alternating fusion conductor symbol

The full six-point QTDS-to-Ward coefficient map is now derived from the two
scalar-scaffolded three-gluon residues. With

\[
I_+=(x_0,x_2,x_4),\qquad I_-=(x_1,x_3,x_5),
\]

the complementary fusion branches carry

\[
A_3^+
=
y_0x_5+y_2x_1+y_1x_3-\sum_{i<j}y_iy_j,
\]

\[
A_3^-
=
y_1x_0+y_0x_2+y_2x_4-\sum_{i<j}y_iy_j.
\]

They agree on the conductor \(Z=F_+\cap F_-\). On the normalization
\(F_+\sqcup F_-\), their intrinsic polarity-odd relative normal symbol is

\[
\sigma_{\rm alt}
=
y_2dx_1+y_1dx_3+y_0dx_5
-y_1dx_0-y_0dx_2-y_2dx_4.
\]

It uses only directions present inside each branch and is independent of any
ambient representative. One-step rotation identifies the ordered
multi-residue conormal lines with positive orientation.

Taking the common-\(y\) linear symbol and oriented road incidence gives

\[
C_{\rm QTDS}
=
\partial_\triangle d_y\sigma_{\rm alt}
=
\begin{pmatrix}
1&1&0&-1&-1&0\\
0&-1&-1&0&1&1\\
-1&0&1&1&0&-1
\end{pmatrix}.
\]

Therefore the exact cross-normal coefficient relation is

\[
M_{\rm Ward}
=
\Theta\Gamma_3\partial_\triangle d_y\sigma_{\rm alt}
\left(
\mathbb J_{\mathfrak f_+}A_{\rm scalar},
\mathbb J_{\mathfrak f_-}A_{\rm scalar}
\right).
\]

No fitted basis, inverse pairing, or common ambient principal-parts lift is
used. A single fusion branch is necessarily insufficient because it is blind
to three of the six columns. What remains is a morphism of the scalar
multi-normal residue/BRST complexes realizing this symbol and commuting with
physical Cut.

### Regional polarity fibers and the corrected eight-point link

For \(n=2p\ge6\), the zero-core scalar flip graph is two copies of the
triangulation graph of a \(p\)-gon. Each component has \(C_{p-2}\) vertices
and one-step rotation exchanges them. The quadrilateral is exceptional: its
two zero-core triangulations are connected by their flip.

A physical diagonal \(D\) cuts the polygon into even polygons \(2a,2b\),
with \(a+b=p+1\). The exact rank-one fiber factorizes as

\[
\mathcal F_{\{D\}}
\cong
\mathcal Z_{2a}\square\mathcal Z_{2b},
\qquad
|\mathcal F_{\{D\}}|
=
4C_{a-2}C_{b-2},
\]

where \(\mathcal Z_4\) is the connected quadrilateral interval and
\(\mathcal Z_{2q}\) for \(q\ge3\) has two associahedral components. Hence the
rank-one component count is \(1,2,\) or \(4\), according as the split is
\(4+4\), \(4+\ge6\), or \(\ge6+\ge6\). Each global polarity has
\(C_{a-2}C_{b-2}\) raw incidences to its compatible component; the last case
also has two mixed regional-polarity components invisible from rank zero.

Six points is exceptional: all three roads are \(4+4\), so their fibers are
connected and the genuine contraction is \(K_{2,3}\).

At eight points every road is \(4+6\). Each rank-one fiber has two connected
components, one incident only to each global polarity. Thus the canonical
rank-zero/rank-one contraction is

\[
K_{1,8}^{+}\sqcup K_{1,8}^{-},
\]

not \(K_{2,8}\). The latter is only a coarse quotient obtained by collapsing
a disconnected fiber and its artificial cycles are not scalar homology.

For every marked physical channel \(D\), however, the boundary is
\(\operatorname{Tri}_4\times\operatorname{Tri}_6\). Quotienting the spectator
quadrilateral interval leaves two local polarity points, and the three
compatible rank-two extensions give a genuine local \(K_{2,3}\). Cut shifts
the core filtration:

\[
(\text{rank }0\to1)\mapsto(\text{rank }1\to2).
\]

More generally, if a partial core cuts the polygon into \(s\)
non-quadrilateral regions, its exact-core fiber has \(2^s\) regional polarity
components. The global plus/minus sheets are the two uniform vertices; mixed
vertices arise only after cutting.

The correct carrier is therefore the full diagram
\(P\mapsto\mathcal F_P\), together with its occurrence coefficient cosheaf and
Gysin maps. A global polarity-odd transgression beyond six points must live in
higher core strata or the homotopy colimit of this diagram. The next exact
test is whether the eight-point rank-two completion recovers the known
Möbius carrier and its marked local \(K_{2,3}\) links.

### Full-core suspension and the two-axis carrier

The eight-point rank-two test is now exact. There are twelve rank-two physical
cores, precisely the full octagon quadrangulations. Each exact fiber is a
connected cube \(I^3\). Its six internal squares are core-constant and
contract to zero; they do not fill a polarity circuit.

The actual transverse associahedral cells consist of sixteen squares and
eight pentagons, exactly one route face for every pair
\((Q,\varepsilon)\in\operatorname{Quad}_8\times\{+,-\}\). After connected-fiber
contraction each becomes

\[
P_\varepsilon-D_\varepsilon-Q-E_\varepsilon-P_\varepsilon,
\qquad Q=\{D,E\}.
\]

The resulting cellular complex has

\[
(C_0,C_1,C_2)=(\mathbb Z^{30},\mathbb Z^{64},\mathbb Z^{24}),
\]

\[
\operatorname{SNF}(\partial_1)=1^{29},
\qquad
\operatorname{SNF}(\partial_2)=1^{24},
\]

and hence

\[
H_\bullet=(\mathbb Z,\mathbb Z^{11},0).
\]

Equivalently it is the union of two contractible polarity sheets meeting in
the twelve discrete full-core fibers, so

\[
\mathcal V_8\simeq S^0*\operatorname{Quad}_8\simeq K_{2,12}.
\]

This is not the Möbius carrier. The latter lives on the compatibility graph
of the twelve quadrangulations and supplies relations among roads: its four
square cycles plus residual octagon have Smith invariants
\((1,1,1,1,2)\) in the rank-five cycle lattice. Thus the emerging geometry has
two axes:

\[
\begin{aligned}
\text{vertical: }&\text{polarity descent through full-core roads},\\
\text{horizontal: }&\text{compatibility and higher coherence among roads}.
\end{aligned}
\]

At six points the three channels are already full quadrangulations and their
compatibility graph is a triangle, so the two axes accidentally coincide.

For a marked channel \(D\), the link/Gysin map lowers core rank,

\[
G_D:\{D,E\}\mapsto q_E.
\]

The two components of the rank-one \(D\)-fiber and its three compatible
rank-two extensions give an honest local \(K_{2,3}\). Only differences of
global full-core roads suspend locally:

\[
\Gamma_D(q_E-q_F)\in H_1(K_{2,3}).
\]

### Coefficient-level status of the marked Gysin square

The coefficient audit now decorates all twelve full-core fibers and all
twenty-four transverse route faces.  Each full-core fiber has rank eight and
factors canonically on either marked channel:

\[
\mathcal L_8(\{D,E\})
\cong
\mathcal L_4(\varnothing)\boxtimes\mathcal L_6(q_E),
\qquad 8=2\cdot4.
\]

All 192 basis factorizations and forty-eight center--road incidences pass.
Occurrence-level physical maps commute, while the degree-one Gysin maps
anticommute after adjoining the normal-orientation factors:

\[
G_EG_D=G_DG_E,
\qquad
\widetilde G_E\widetilde G_D
=-\widetilde G_D\widetilde G_E.
\]

This closes all sixteen route squares with rank pattern \([0,1,2,1]\).
It does not yet close the eight route pentagons with pattern
\([0,0,1,2,1]\).  A pentagon begins with a same-core scalar flip, so its two
physical routes start in different scalar occurrence fibers.  The present
coefficient system defines no rank-preserving transport

\[
\tau_s:\mathcal L(T_0)\to\mathcal L(T_1)
\]

on that edge.  The all-24-face Gysin/suspension equation is therefore
untyped, not falsified.

The residual compatibility octagon does not acquire a rescuing sign twist.
The normal, polarity, and tensor holonomies measured from the established
maps are all \(+1\), and distinct deck-equivariant pointwise edge-sign
extensions are nevertheless trivial on all five cycle generators.  The
four-square-plus-octagon sublattice retains index two.

The strict-transport falsifier has now been executed.  Each scalar edge
exchanges one of five independent Laurent labels, so no label-and-weight
preserving rank-five endpoint isomorphism exists.  After passage to the common
rank-eight full-core fiber, all previously established data admit both

\[
\tau_s=+\operatorname{Id}
\qquad\text{and}\qquad
\tau_s=-\operatorname{Id}.
\]

They are central, involutive, and deck covariant, but their signed pentagon
defects are respectively

\[
0
\qquad\text{and}\qquad
-2\operatorname{Id}.
\]

Thus the zero obtained from \(+\operatorname{Id}\) is a choice, not an
intrinsic consequence.  The next object is the loaded Pochhammer/Cousin
pentagon itself.  Its five oriented facet tubes, tangential loading, normal
line, and forced lower-face terms must satisfy

\[
\operatorname{Res}^{\rm PC}_{D,E}\partial_{\rm PC}\mathcal P(F)
=
\partial_{\rm PC}\operatorname{Res}^{\rm PC}_{D,E}\mathcal P(F).
\]

One pentagon suffices before rotation because the eight faces form a single
deck orbit.  This is the first place where the proposed
six-functor/recollement calculus is forced to be genuinely derived rather
than strict.

### Constructible coefficient repair

The attempted scalar-edge automorphism was the wrong categorical shape. For
each of the eight nontransverse pentagons, the two rank-five endpoint modules
share a canonical rank-four labelled submodule:

\[
M_0\xleftarrow{}M_s\xrightarrow{}M_1,
\qquad
(\operatorname{rank}M_0,\operatorname{rank}M_s,
\operatorname{rank}M_1)=(5,4,5).
\]

The two rank-one endpoint quotients are the exchanged flip labels. Their
mapping-cone generator augments to

\[
d h_s=X_x-X_y,
\]

but the span, not this augmented polynomial equation, is the intrinsic
occurrence object. Every one of the sixteen polarity-supported double-Gysin
sources lies in \(M_s\); the exchanged quotient labels are never selected.
Thus physical Gysin is extension by zero on the flip quotient and agrees in
the two cut orders on its supported common source.

The supported full-core images satisfy two saturated integral Čech
resolutions. Within a pentagon or its relevant companion square,

\[
0\to\mathbf Z^2
\to\mathbf Z^4\oplus\mathbf Z^4
\to\mathbf Z^6\to0.
\]

For a pentagon--companion-square pair at fixed full core,

\[
0\to\mathbf Z^4
\to\mathbf Z^6\oplus\mathbf Z^6
\to\mathbf Z^8\to0.
\]

All nonzero Smith factors are one. A pentagon alone sees six of eight
occurrence lines; the companion square supplies the remaining two, and the
pair covers the complete full-core fiber on all eight relevant cores.

This is the coefficient counterpart of the two-axis topology: polarity
descent is the first Čech layer and pentagon/square compatibility is the
second. The scalar coefficient system is therefore a constructible cosheaf
assembled by spans and colimits, not a local system with parallel transports.

The finite-alpha-prime task is correspondingly sharper. Tensor these two
incidence resolutions with the pentagon and square Pochhammer tubes, realize
the exchanged quotient cone as forced lower-face terms, and prove that the
physical Cousin residues commute with the resulting total differential. This
would complete the pre-pairing chain provenance of \(\mathsf J\), whose
cohomological Pfaffian-square identification remains established already.

### Occurrence support and cubical coherence boundary

The route-face diagonal coefficient system is now exact at eight points.  On
every one of the twenty-four route faces, the fibers in dimensions two, one,
and zero have ranks \(3,4,5\), the specialization maps are labelled
inclusions, and the system decomposes into rank-one extension-by-zero
summands.  Common labels live on the whole face; every other label lives on
one closed boundary edge.  This is a constructible cosheaf, not a local
system.

Every one of the twelve rank-two physical cores has an actual fixed-core
associahedral fiber

\[
K_Q\cong I^3,
\]

obtained from the two scalar choices in each of its three quadrilateral
regions.  Eight cores have four distinct \(P_\pm,S_\pm\) support facets.  They
form the four-facet belt \(S^1\times I\), with cell census
\((8,12,4,0)\), rather than a cover of the full cube.  The other four cores
have only two distinct supported facets.

For each four-chart core, the two omitted opposite facets cap the belt and the
cube 3-cell compares the two fillings:

\[
\partial B_Q=-\partial(K_Q^++K_Q^-),
\qquad
B_Q+K_Q^++K_Q^-=\partial I_Q^3.
\]

The target homology changes from \(H_1(B_Q)=\mathbf Z\), to a contractible
one-capped belt, to the boundary \(S^2\), and finally to the contractible
filled cube.  This is the first explicit higher coherence cell in the scalar
incidence calculus.

A formal Čech--tube--normal totalization has been constructed.  Its
differential squares to zero on 4512 basis symbols and its formal double
residue commutes with that differential.  This is conditional on the
undecorated facewise Pochhammer symbols of entry 38.

The physical gap is narrower but still real.  Occurrence support fixes the
target square facets but not the route-edge and route-face maps.  It admits
forty pentagon-to-square cellular lifts, twenty per orientation.  The
candidate which collapses the scalar flip edge is consistent but not
intrinsically selected.  Therefore the cap/cube completion proves target
exactness, not yet the finite-alpha-prime physical Gysin naturality.  The next
experiment must derive that degree-shifted loaded map and verify residue
commutation generator by generator.

### Derived Gysin class and weighted route cube

The forty-lift ambiguity is now resolved at the level actually seen by an
open Pochhammer/Cousin face.  A pentagon and its target square are oriented
disks, so their Borel--Moore complexes are the relative complexes
\(C_*(F,\partial F)\simeq\mathbf Z[-2]\).  All twenty strict lifts of fixed
orientation are chain homotopic as maps of pairs; 800 ordered equal-degree
pairs were checked exactly.  The ordered normal line therefore selects one
positive derived Gysin class, although existing support and deck data still
leave four cyclic strict origins in that class.

A Boolean-labelled partial-core square
\((\varnothing,D,DE,E)\) would select the scalar-edge collapse uniquely after
choosing orientation, but this is extra target data.  Moreover the
constructible pushout on that edge has rank \(5+5-4=6\), while the target
vertex has rank five.  The missing datum is one loaded Cousin counit relating
the exchanged endpoint labels.

The fixed-core target has also been corrected.  It is not the rank-eight
occurrence module tensored with all cube cells.  If \(d_{r0},d_{r1}\) are the
two scalar refinements in quadrilateral region \(r\), define

\[
K_r^{\mathrm w}
=
\left[
Rh_r\xrightarrow{d}
Re_{r0}\oplus Re_{r1}
\right],
\qquad
d h_r
=
X_{d_{r1}}e_{r1}-X_{d_{r0}}e_{r0}.
\]

Then

\[
K_Q^{\mathrm w}
=
K_0^{\mathrm w}\otimes K_1^{\mathrm w}\otimes K_2^{\mathrm w}
\]

has degree ranks \((8,12,6,1)\).  Its eight vertices are the full occurrence
fiber and its higher cells are the scalar-flip homotopies and coherences.  The
four physical charts are coordinate-facet restrictions of

\[
-\kappa_D\kappa_E
\bigotimes_{r=0}^2
\left(
X_{d_{r0}}e_{r0}+X_{d_{r1}}e_{r1}
\right).
\]

The remaining two facets are the caps, and the weighted boundary equations
force both cap coefficients and the top cube coefficient to \(+1\).

For the representative exchanged labels \(15,37\), the localized lower term

\[
H_s
=
\frac{X_{15}}{u_{15}}\ell_{15}
-
\frac{X_{37}}{u_{37}}\ell_{37},
\qquad
dH_s=X_{15}e_{15}-X_{37}e_{37},
\]

supplies exactly the missing rank-one counit, and supported double Gysin kills
both quotient lines.  This proves the formal localized/derived equations.  It
does not yet assemble the counit with all occurrence charts into the
bivariant Pochhammer/Cousin natural transformation.  Literal collar choices
are already auxiliary for the underlying facewise class by entry 38.  Here
\(d\ell_e=(q_e-1)e_e\); equivalently
\(H_s=X_{15}h_{15}^{\rm PC}-X_{37}h_{37}^{\rm PC}\) with
\(h_e^{\rm PC}=\ell_e/(q_e-1)\).  These are normal Pochhammer contractions,
not the regional weighted-cube edges \(h_r\).

The formula objective is now a derived kernel

\[
\mathscr G_Q^{\alpha'}
\in
\operatorname{RHom}\!\left(
\operatorname{PC}_{\alpha'}(\mathcal R_Q;\mathcal L),
K_Q^{\mathrm w}[-2]
\right)
\]

on the complete route envelope, commuting with the PC differential, physical
double residue, and deck rotation.  Strict collars and cellular
parametrizations may vary; the invariant to construct is its derived class.

### Derived route Hom and primitive QTDS polarization

The complete cellular Hom audit now separates uniqueness of the local route
class from existence of its higher source extension. After occurrence/Čech
descent and relative Borel--Moore identification, the four physical charts
form

\[
B=\partial I^2\times I\simeq S^1.
\]

For one region over \(A_r=\mathbf Z[X_{r0},X_{r1}]\), the weighted interval
complex resolves the ideal

\[
H_0(K_r^{\rm w})\simeq(X_{r0},X_{r1}),
\qquad
e_{r0}\mapsto X_{r1},
\quad
e_{r1}\mapsto X_{r0}.
\]

It is torsion-free and generically rank one, but nonfree at the joint
coordinate zero. For the three octagon regions,

\[
H_0(K_Q^{\rm w})
\simeq
I_Q=\prod_{r=0}^{2}(X_{r0},X_{r1}),
\]

with no higher homology. Full Laurent localization turns this ideal into the
free rank-one module \(R\).

The integral Hom complex has dimensions
\((8,60,172,232,144,32)\) and differential ranks
\((8,52,120,111,32)\). Integral contractions prove

\[
H^{-1}=0,
\qquad
H^0=R,
\qquad
H^1=R
\]

after localization, with no torsion; polynomially both nonzero groups are
\(I_Q\). The chart-gluing kernel is saturated rank one. Ordered normal
orientation fixes its sign and the weighted vertex anchors fix its unit, so
the degree-zero route class is uniquely normalized. The surviving degree-one
class is the belt circle. Entry 76 shows that actual scalar caps kill it, so
it records the missing dependent route attachment rather than a second map,
nonzero curvature, or absence of scalar cap cells.

The exchanged labels \(15,37\) form the polynomial endpoint ideal
\((X_{15},X_{37})\), becoming split rank one only after localization. Their
Cousin relation is internal to the source, and both endpoint lines and its
handle map to target zero. No companion-square line is being identified with
either endpoint.

Finally, in Laurent homology

\[
g_r=[X_{r0}e_{r0}]=[X_{r1}e_{r1}],
\qquad
[c_r]
=
[X_{r0}e_{r0}+X_{r1}e_{r1}]
=2g_r.
\]

Thus the eight-point full polarization is

\[
[c_0\otimes c_1\otimes c_2]
=8g_0\otimes g_1\otimes g_2.
\]

This factor is an index/normalization effect, not Hom torsion. It gives the
first intrinsic half-object interpretation of the QTDS coefficient two: the
two scalar resolutions of a quadrilateral are endpoint representatives of
one derived Laurent class, and the QTDS numerator is their polarization.
Internal physical-side terms still belong to adjacent core strata, so this
does not yet prove horizontal Jordan coherence.

### Actual scalar caps and the dependent Beck--Chevalley gap

The cap audit changes the diagnosis. For \(Q=\{03,05\}\), the exact-core
scalar face is the actual associahedral cube

\[
K_Q=K_4^3,
\qquad
(02,13)\times(04,35)\times(06,57).
\]

Its missing side-belt caps are the literal faces \(Q+04\) and \(Q+35\), and
\(K_Q\) is their unique scalar three-parent. Labeling a vertex \(v\) by the
opposite monomial

\[
m_v=\prod_r X_{r,1-v_r}
\]

and every face by the lcm of its vertex labels turns the actual cube into the
minimal polynomial cellular resolution of

\[
I_Q=\prod_r(X_{r0},X_{r1}).
\]

The map \(\chi_Q([F])=m_F\mathbb P(F)\) telescopes with the facewise
Pochhammer/Cousin differential. The first cap kills the primitive belt
\(H^1\) integrally, the second makes the sphere, and the scalar cube fills it;
the relative coefficients are uniquely \(1,1,1\). No division by two or
Laurent localization is needed.

The remaining gap is not a cap. The dependent route pentagon
\(P=\{13,35,57\}\) and companion square \(S=\{02,04,06\}\) are disjoint scalar
faces with no common three-parent; each meets \(K_Q\) at only one opposite
vertex, although physical double Gysin sends their marked charts to four
entire belt facets. Their cross-chart overlaps are coefficient intersections,
not source-face intersections. The endpoint cone on \(15,37\) maps to zero
and is distinct from the regional \(04,35\) cap direction.

The next exact object is therefore a loaded derived Beck--Chevalley
attachment

\[
\beta_Q^{\alpha'}
\in
\operatorname{RHom}
(\mathcal C_Q^{\rm route},B_Q^{\rm w}[-2]),
\]

compatible with the regional PC map, the four occurrence anchors,
\(H_s\mapsto0\), ordered residues, and deck rotation. Once this belt
attachment exists, the actual caps and cube extend it automatically. Only
then should the eight route kernels be assembled horizontally and compared
with the Jordan defect.

### Alexander complement and the primitive boundary half-line

For a maximal quadrangulation \(Q\), set
\(\mathfrak p_r=(X_{r0},X_{r1})\). Because different regions use disjoint
variables,

\[
I_Q=\prod_r\mathfrak p_r=\bigcap_r\mathfrak p_r
\]

is squarefree. Its raw and opposite occurrence generators

\[
w_v=\prod_rX_{r,v_r},
\qquad
m_v=\prod_rX_{r,1-v_r}
\]

satisfy \(w_vm_v=\prod_rX_{r0}X_{r1}\) and differ by the antipodal
Alexander-complement involution. The opposite-labeled regional cube is the
minimal cellular resolution of \(I_Q\); its Alexander dual is the complete
intersection generated by the regional products \(X_{r0}X_{r1}\).

The pairing normalization identifies its primitive class. In one region,

\[
a_{R,4}=-(x+y),
\qquad
m_4=\frac{x+y}{xy},
\qquad
\mathsf J_4=-xy.
\]

The interval augmentation sends
\(g_r=[xe_{r0}]=[ye_{r1}]\) to \(xy\), while the polarized class
\(c_r=xe_{r0}+ye_{r1}\) maps to \(2xy\). By channel-quotient monoidality,

\[
\Delta_Q^+\mathsf J_{2m}
=
\varepsilon_Q(-1)^{m-1}\phi_Q(g_Q),
\qquad
\left[\bigotimes_rc_r\right]=2^{m-1}g_Q.
\]

Thus each maximal quadrangulation already carries the primitive boundary
half-line. The remaining task is gluing these local rank-one ideals across
dependent route faces. Algebraically, because \(K_Q^{\rm w}\to I_Q\) is a
resolution, an unfiltered derived lift is equivalent to a route augmentation
\(\mathcal C_Q^{\rm route}\to I_Q[-2]\). Physical naturality additionally
requires the four-facet support filtration and the finite-\(\alpha'\)
Pochhammer/Cousin comparison. This is naturally interpreted as an
excess-intersection Beck--Chevalley problem, but the geometric multi-normal
deformation producing that comparison remains to be constructed.

### Unfiltered comparison and the four missing overlap bridges

The route augmentation now exists explicitly. For every chart copy
\(c_{i,v}\) of an occurrence word, set

\[
a_Q(c_{i,v})=m_v.
\]

The established Čech differential has eight columns
\(c_{j,v}-c_{i,v}\), so \(a_Q\) kills every column and surjects onto
\(I_Q\). The projective comparison theorem therefore supplies a lift into
\(K_Q^{\rm w}[-2]\), unique up to homotopy. There is no unfiltered polynomial
obstruction.

What fails is support. The sixteen chart-occurrence copies and eight Čech
columns form eight disconnected two-vertex components. The four nonempty
chart-pair overlaps are

\[
(P_+,P_-),\quad(P_+,S_-),\quad(P_-,S_+),\quad(S_+,S_-),
\]

and each contains two occurrences differing only in the middle regional bit.
The corresponding target-facet overlap is the entire middle interval, but
the source contains only two duplicate-identification columns and no chain
joining their endpoints. This endpoint difference is outside the integral
span of the established source incidence.

For endpoints \(v^0=(v_0,0,v_2)\) and \(v^1=(v_0,1,v_2)\), the missing
relation is nevertheless forced and primitive:

\[
X_{11}m_{v^1}-X_{10}m_{v^0}=0,
\qquad
d h_e=X_{11}e_{v^1}-X_{10}e_{v^0}.
\]

Thus exactly four relative interval generators are missing, one per edge of
the chart-overlap cycle. If scalar geometry supplies them, three
compatibility equations plus the ordered-normal anchor have determinant
\(\pm1\), so the completion is unique and saturated. The internal scalar
cone \(H_s(15,37)\) maps to zero and cannot provide these regional
\((04,35)\) bridges.

The frontier is therefore no longer an abstract Hom calculation. It is to
derive the four interval generators from an intrinsic loaded Cousin or
multi-normal scalar carrier. This is a filtered/excess Beck--Chevalley
problem: ordinary derived comparison forgets exactly the paths that physical
factorization must retain.

### Resolved overlap ideals and effective belt descent

The four bridges are now canonical at the polynomial associated grade. Write
\(\mathfrak p_r=(X_{r0},X_{r1})\). The four facet ideals are

\[
X_{20}\mathfrak p_0\mathfrak p_1,
\quad
X_{00}\mathfrak p_1\mathfrak p_2,
\quad
X_{21}\mathfrak p_0\mathfrak p_1,
\quad
X_{01}\mathfrak p_1\mathfrak p_2.
\]

For every support-adjacent pair their intersection is

\[
J_e=C_e(X_{10},X_{11}),
\]

whose minimal resolution is the middle weighted interval with primitive
syzygy

\[
X_{11}m_{v^1}-X_{10}m_{v^0}=0.
\]

The four facet resolutions and four interval resolutions form a
support-selected hyper-Čech sequence

\[
0\to\bigoplus_eK_e^{\rm w}
\to\bigoplus_iK_{F_i}^{\rm w}
\to B_Q^{\rm w}\to0
\]

which is split exact cell by cell over the polynomial ring. Opposite facets
also intersect as ideals but are disjoint in the belt; this proves that the
face-support poset, not unrestricted module intersection, is essential.

The actual raw-weighted polygon carrier gives an independent derivation. Its
complete saturated kernel has ranks \((10,6,0)\). Two unit interval summands
are exactly the collapsed pentagon \(H_s\) cones. Quotienting them leaves an
\(8\times4\) incidence matrix consisting of four disjoint primitive interval
complexes, precisely the four resolved overlaps above. All Smith factors and
normalization determinants are units, so descent identifies occurrence
representatives rather than averaging them: no division by \(2\) or \(8\) is
needed.

The local object is therefore an effective relation groupoid

\[
\mathcal K_Q\rightrightarrows\mathcal R_Q\to B_Q^{\rm w}.
\]

The belt is its polynomial homotopy colimit. This does not make the disjoint
pentagon and square into ordinary intersecting scalar faces. It says the
half-object is a derived image with descent. The immediate gap is now to
construct the same relation groupoid in finite-\(\alpha'\) loaded
Pochhammer/Cousin or multi-normal geometry and prove the five-term pentagon
identity. After that, the next obstruction is global: assemble the eight deck
images and compute the residual octagon/Jordan holonomy.

### Universal monodromy base change versus physical loading

The complete relation algebra admits an exact formal monodromy deformation.
With \(u_{ra}=q_{ra}-1\), base change

\[
X_{ra}\longmapsto u_{ra}
\]

over \(\mathbf Z[u_{00},\ldots,u_{21}]\) preserves the weighted cube, all four
support-overlap intervals, both collapsed pentagon cones, the full pentagon
and square carrier identities, deck covariance, and the ordered-normal
Koszul sign. The formal bridge is

\[
d h_e=u_{11}e_{v^1}-u_{10}e_{v^0}.
\]

The support hyper--Čech sequence remains split exact after passage to the
universal local-system group ring. Its formal four-transition holonomy is
exactly one.

This is not yet the physical finite-loaded relation groupoid. In the
facewise Pochhammer/Cousin comparison, the \(X_{ra}\) are scalar occurrence
coefficients and \(q_E-1\) is the differential of a separate normal Koszul
factor. Substituting \(q-1\) for \(X\) and then tensoring that normal complex
would load the same boundary direction twice. Thus the remaining theorem is
geometric, not another coefficient calculation.

The rank-one excess proposal has now failed its exact typing test. After
localizing the fixed outer monomial, the middle overlap ideal is
\(\mathfrak p=(x,y)\). Its interval is the unique first syzygy of
\(\mathfrak p\), equivalently the top determinant generator of the rank-two
Koszul resolution of \(A/\mathfrak p\). Self-intersection Tor has ranks
\((1,2,1)\), so the rank-one class is \(\operatorname{Tor}_2\), not
\(\operatorname{Tor}_1\). More decisively, the only documented scalar normal
base is \(A[t]\); the ideals \((t)\) and \((x,y)\) are Tor-independent and
have excess rank zero.

The finite candidate must therefore retain the complete endpoint relation

\[
d h=(q_y-1)e_1-(q_x-1)e_0,
\]

as one determinant interval with two endpoint monodromies. It should enter as
a bivariant loaded kernel between the route and regional carriers, not as a
single Thom factor of a presently defined excess line. The new theorem target
is to construct this kernel in the facewise Pochhammer/Cousin category and
identify its integral transform with physical double Gysin.

The formal grade also cannot exclude a residual unit holonomy

\[
H(\alpha')=1+O(\alpha')
\]

from tangential loading, collars, or the orientation local system. The
representative eight-point test must compute the product of the four actual
PC transitions and prove it is one, while simultaneously verifying the full
five-term dependent pentagon Cousin identity.
