# Photon–Tetrahedron–Octahedron Witness Helix

## Status, provenance, and question

This packet documents the synthesis supplied by the operator in a quoted GPT
note. It connects the two-triangle seed, tetrahedral closure, octahedral
incidence and cofibers, a six-to-three metric quotient, positive outward shells,
and the stable four-chart helix.

**Question:** can these constructions be compared by explicit labelled maps,
and can their native spectral data explain the proposed weights 11/25 and
14/25 rather than merely reproduce the integers 11, 14, 25, and 4?

**Claim boundary:** elementary incidence and metric identities are derived
below. Cofiber exactness requires a specified exact/stable setting. The
four-chart suspension relation has an existing formal graded construction;
identifying its suspension with a geometric shell still requires the relative
object and comparison functor to be specified. The spectral selection remains
open. No new checker or physical experiment was run for this documentation.

**Disposition:** retain the structural synthesis as a candidate with the typing
qualifications in sections 4, 11, and 14–17. In particular, a shell itself is not
a suspension, a count difference is not an embedded complementary sector, and
commutation with witness promotion requires a naturality witness. These are
explicit qualifications of the supplied draft, not additional established
identifications. “Photon” remains the seed's proposed physical interpretation.

Relevant coherence obligations are forward realization, attachment transport,
and route compatibility. Physical readout descent is not supplied.

## 1. Photon-like seed

Use tetrahedral labels

\[
A=0,\qquad B=1,\qquad C=2,\qquad D=3.
\]

The two oriented seed cycles are

\[
T_1=(AB,BC,CA)=\partial[012],
\qquad
T_2=(BA,AD,DB)=-\partial[013].
\]

They share edge 01 with opposite orientations. Their underlying undirected
support graph is \(K_4\setminus\{23\}\). Including the two filled triangular
faces, the cell census is

\[
(f_0,f_1,f_2)=(4,5,2),\qquad \chi=4-5+2=1.
\]

There are \(4+5+2=11\) nonempty cells. The graph alone has no 2-cells; this
census refers to the filled two-triangle complex.

The [two-packet construction](photon-two-packet-construction.md) uses the six
oriented occurrences \((AB,BC,CA,BA,AD,DB)\). These must not be confused with
the five undirected edge supports or with two physical photons.

## 2. Tetrahedral closure

The two missing oriented faces are

\[
T_3=\partial[023],\qquad T_4=-\partial[123].
\]

Their edge boundaries satisfy

\[
T_1+T_2+T_3+T_4=0.
\]

Indeed the oriented face chain is
\([012]-[013]+[023]-[123]=-\partial[0123]\), whose boundary vanishes. Thus
the seed embeds into the four-face tetrahedral boundary, occupying the 012 and
013 faces with the stated signs.

## 3. Six edge relations and octahedral promotion

The tetrahedral edge set is

\[
E=\{01,02,03,12,13,23\}.
\]

Promote each edge to a vertex and join two promoted vertices when their edges
share an endpoint. The resulting line graph \(L(K_4)\) is the octahedral graph.
Its three nonadjacent pairs are

\[
01\mid23,\qquad02\mid13,\qquad03\mid12.
\]

These complement pairs will determine the three unsigned axes.

## 4. Cofiber realization and its boundary

Take a coherent four-stage filtration

\[
A_0\longrightarrow A_1\longrightarrow A_2\longrightarrow A_3
\]

in a specified stable category. For ordinary inclusions with exact quotients,
write

\[
C_{ji}=A_j/A_i,\qquad i<j;
\]

in the stable setting this denotes the corresponding cofiber. Label the six
objects by

\[
(C_{10},C_{20},C_{30},C_{21},C_{31},C_{32})
\longleftrightarrow(01,02,03,12,13,23).
\]

The four cofiber triangles are

\[
C_{10}\to C_{20}\to C_{21}\to\Sigma C_{10},
\]
\[
C_{10}\to C_{30}\to C_{31}\to\Sigma C_{10},
\]
\[
C_{20}\to C_{30}\to C_{32}\to\Sigma C_{20},
\]
\[
C_{21}\to C_{31}\to C_{32}\to\Sigma C_{21}.
\]

They correspond to 012, 013, 023, and 123 and form the standard octahedral
compatibility diagram of composable maps. An existing coordinate-support model
is described in [Tate-torus cofibers](tate-torus-cofiber-and-octahedral-realization.md).

Write \(O_{\mathrm{incidence}}\) for the edge-incidence octahedron and
\(O_{\mathrm{cofiber}}\) for the cofiber diagram. Their six labels and the
underlying octahedral incidence pattern agree **after forgetting the category,
morphism directions, and suspension shifts**. In particular, a connecting map
such as \(C_{21}\to\Sigma C_{10}\) is not an unsuspended map
\(C_{21}\to C_{10}\). Equality of the six labels is not an exact-functor or
metric identification of the quotient objects with geometric vertices.

## 5. Geometric octahedron

Use the regular tetrahedral coordinates

\[
v_0=(1,1,1),\quad v_1=(1,-1,-1),\quad
v_2=(-1,1,-1),\quad v_3=(-1,-1,1).
\]

The edge-midpoint map is

\[
m_{ij}=\frac{v_i+v_j}{2}.
\]

Its values are

\[
m_{01}=(1,0,0),\quad m_{23}=(-1,0,0),
\]
\[
m_{02}=(0,1,0),\quad m_{13}=(0,-1,0),
\]
\[
m_{03}=(0,0,1),\quad m_{12}=(0,0,-1).
\]

Their convex hull is the regular octahedron

\[
|x|+|y|+|z|\le1.
\]

Thus \(O_{\mathrm{geometric}}\) and \(O_{\mathrm{incidence}}\) agree as
labelled face-incidence complexes. The comparison with
\(O_{\mathrm{cofiber}}\) has the forgetful scope stated above; it does not
identify stable objects with points of Euclidean space.

## 6. Eight octahedral triangular faces

Four faces come from tetrahedral faces:

\[
(01,02,12),\quad(01,03,13),\quad
(02,03,23),\quad(12,13,23).
\]

Four more come from tetrahedral vertex stars:

\[
(01,02,03),\quad(01,12,13),\quad
(02,12,23),\quad(03,13,23).
\]

Hence octahedral promotion has \(4+4=8\) triangular sectors. The extra four
are incidence/star sectors; a categorical interpretation needs their own maps
and commuting cells rather than four additional cofiber triangles by counting.

## 7. Canonical six-to-three quotient

Let \(H_E=\mathbb R^6\) with the orthonormal edge basis. Define the complement
involution by

\[
c(e_{01})=e_{23},\quad c(e_{02})=e_{13},\quad c(e_{03})=e_{12},
\qquad c^2=I.
\]

Its even and odd sectors are

\[
K=\ker(c-I),\qquad Q=\ker(c+I),\qquad H_E=K\oplus Q.
\]

The even sector is spanned by the three complement sums. Orthogonal projection
\((I-c)/2\) identifies \(H_E/K\) with \(Q\), whose normalized basis is

\[
d_1=\frac{e_{01}-e_{23}}{\sqrt2},\qquad
d_2=\frac{e_{02}-e_{13}}{\sqrt2},\qquad
d_3=\frac{e_{03}-e_{12}}{\sqrt2}.
\]

Thus \(\dim Q=3\). The quotient is canonical for the declared counting
metric and complement pairing. Ordering the axes and choosing their signs uses
the displayed labels; that extra framing should not be confused with an
unlabelled preferred basis.

## 8. Metric identification

Define \(M:H_E\to\mathbb R^3\) by \(M(e_{ij})=m_{ij}\). Complementary
midpoints sum to zero, so \(K\subset\ker M\). Since the midpoint map has rank
three, \(\ker M=K\), and it factors through \(Q\).

On the normalized basis,

\[
\bar M(d_1)=\sqrt2(1,0,0),\quad
\bar M(d_2)=\sqrt2(0,1,0),\quad
\bar M(d_3)=\sqrt2(0,0,1).
\]

Consequently \(\bar M/\sqrt2\) is an isometry from the quotient Hilbert space
to Euclidean \(\mathbb R^3\). For the six labelled midpoint vectors,

\[
G_{ii}=1,\qquad G_{i,c(i)}=-1,\qquad G_{ij}=0
\]

for all other pairs. The quotient images of the six edge basis vectors have

\[
G^Q_{ii}=1/2,\qquad G^Q_{i,c(i)}=-1/2,\qquad G=2G^Q.
\]

No label-dependent rescaling is needed. This identifies two declared
mathematical metrics up to a global factor; it does not establish their
physical normalization or agreement with every historical analytic metric.

## 9. Area representation

The natural \(S_4\) edge-permutation action commutes with \(c\) and therefore
descends to \(Q\). Under the midpoint map it is the standard three-dimensional
tetrahedral action \(\rho\), with \(\det\rho(g)=\operatorname{sgn}(g)\).

If one additionally composes the edge action with \(c\) for odd permutations,
then, because \(c|_Q=-I\), the induced action is

\[
\rho_{\mathrm{area}}(g)=\operatorname{sgn}(g)\rho(g).
\]

This is the cofactor/area action for orthogonal matrices. It is the sign-twisted
action on the same quotient, not the untwisted quotient action itself. The two
agree on \(A_4\), the proper rotations used in the existing positive geometry.

## 10. Photon support as an octahedral vertex-star fragment

The five undirected supports around AB are

\[
AB,\quad AC,\quad BC,\quad AD,\quad BD.
\]

Only CD is missing; geometrically \(m_{CD}=-m_{AB}\). Delete that antipodal
vertex from the octahedron. The induced graph is the wheel on five vertices,
here denoted \(W_5\): one hub and a four-cycle rim. It has five vertices,
eight edges, and four triangular faces:

\[
(AB,AC,BC),\quad(AB,AD,BD),\quad
(AB,AC,AD),\quad(AB,BC,BD).
\]

The first two are the seed's face sectors. The other two are the tetrahedral
vertex-star sectors at A and B. Octahedral incidence completion therefore gives
\(2\to4\) triangular sectors without adding a support vertex. Calling this
“coherence completion” requires the corresponding compatibility cells; the
induced graph and its faces alone specify incidence.

## 11. The 11, 14, 25, 4 counts

The original filled diamond has 11 nonempty cells. A complete ordered field on
its five undirected edge supports has \(5^2=25\) entries. Their difference is
\(25-11=14\), while the completed wheel has four triangular sectors.

These integers have distinct types:

| Integer | Counted object |
|---:|---|
| 11 | Vertices, edges, and filled faces of the original diamond |
| 25 | All ordered pairs of its five edge supports, including self-pairs |
| 14 | Arithmetic difference between the preceding counts |
| 4 | Triangular faces of the induced wheel complex |

**Unresolved embedding:** the original cells and the ordered support pairs
are different sets. No injection or linear embedding of an 11-dimensional cell
sector into the 25-dimensional ordered-pair field has been supplied here.
Therefore 14 is not yet the dimension of an identified complementary sector.
Counting alone does not make this a stronger claim than \(25-11=14\).

The proposed spectral targets are

\[
D=\frac{11}{25},\qquad C=\frac{14}{25}.
\]

Their originating projector and readout convention must be cited and matched
before the wheel can be claimed to explain them. These fractions would be
weights or matrix/readout coefficients, not the eigenvalues of an idempotent
rank-one projector, whose eigenvalues are 0 and 1.

## 12. Twelve oriented edges and three axes

The tetrahedron has six undirected edges, two orientations per edge, and three
complement pairs:

\[
6\cdot2=12,\qquad6/2=3,\qquad12\cdot3=36.
\]

Each directed edge labels one centroid-edge triangle in the existing positive
refinement. The spatial fiber comes from the complement-odd quotient, so the
36-coordinate carrier has an explicit \(12\times3\) labelled construction.

With the already declared local/symmetry/dense-feedback architecture,

\[
108=12\cdot3^2,\qquad432=12^2\cdot3,\qquad1296=(12\cdot3)^2,
\]

and hence

\[
1836=12\cdot3^2+12^2\cdot3+(12\cdot3)^2
=6\cdot2\cdot3^2+6^2\cdot2^2\cdot3+(6\cdot2\cdot3)^2.
\]

The factors 6, 2, and 3 mean edge relations, orientations, and odd quotient
axes. Distinct stage ports, basis choice, local mode selection, and dense
feedback remain required inputs; this restatement does not make 1836 an
invariant minimum or a particle mass.

## 13. Twelve-triangle positive refinement

Subdivide each of the four tetrahedral faces by its centroid. This gives three
small triangles per face and twelve total. With consistent orientation the
internal centroid spokes cancel in the boundary chain, leaving the original
coarse face boundary. The closed twelve-triangle surface is therefore a
refinement of the same tetrahedral cycle, not a different exactness relation.

The [positive-geometry packet](twelve-triangle-positive-geometry.md) supplies
the coordinates, outward orientation and projector construction. The
[monomial support theorem](monomial-projector-support-theorem.md) records the
representation/basis assumptions behind the three support counts.

## 14. Outward shell: absolute space versus relative suspension

To type the geometry, let \(B\) be a compact convex body containing the origin
in its interior and let \(K=\partial B\). For \(\lambda>1\), define

\[
W_\lambda(B)=\lambda B\setminus\operatorname{int}B.
\]

Radial coordinates identify it with \(K\times[1,\lambda]\). Its absolute
homotopy type is \(K\), not a suspension of \(K\). This corrects the unqualified
statement \(W_{\mathrm{shell}}\simeq\Sigma\) in the supplied draft.

The **relative cylinder chain complex**, with both boundary components taken
as the relative subspace, has a suspension description. In a product cellular
model,

\[
C_n(K\times I,K\times\partial I)\cong C_{n-1}(K).
\]

For homological suspension with differential \(d_\Sigma=-d\), a compatible
chain map is

\[
J_K[\sigma\times I]=(-1)^{\dim\sigma}\Sigma\sigma.
\]

For singular chains one uses the corresponding natural chain equivalence,
not a literal equality of their chosen free bases. For unbased \(K\), the
quotient space is the reduced suspension \(\Sigma(K_+)\), where \(K_+\)
adds a disjoint basepoint. It is not automatically the ordinary suspension of
\(K\) with two distinct poles. For example, the relative homology of a shell
on \(S^2\) has nonzero groups in degrees 1 and 3, whereas the reduced
suspension of based \(S^2\) has only the latter.

Accordingly, shell witnessing realizes a degree shift only after the relative
object, basepoint convention and chain realization are specified.

## 15. Positive metric and radial composition

For a planar k-cell \(\sigma\) whose cone from the origin has nonzero
(k+1)-volume, its outward conical shell satisfies

\[
\operatorname{Vol}_{k+1}W_\lambda(\sigma)
=(\lambda^{k+1}-1)\operatorname{Vol}_{k+1}C(\sigma).
\]

The value is positive for \(\lambda>1\) and a nondegenerate outward-oriented
cone. Degenerate cells require separate treatment; homothety alone does not
make their volumes positive.

Multiplicative scale composition is additive in

\[
\tau=\log\lambda,\qquad
\lambda_{12}=\lambda_1\lambda_2,\qquad
\tau_{12}=\tau_1+\tau_2.
\]

This is the logarithmic coordinate with the displayed normalization, not a
physical clock. For a three-dimensional body,

\[
\frac{V_{\mathrm{outer}}}{V_{\mathrm{inner}}}=\lambda^3,
\qquad
\tau=\frac13\log\frac{V_{\mathrm{outer}}}{V_{\mathrm{inner}}}.
\]

## 16. Four-chart stable helix

The existing formal helix has chart/grade labels \((h,i)\), with
\(h\in\mathbb Z\) and \(i\in\{0,1,2,3\}\). Its successor is

\[
q(h,i)=
\begin{cases}
(h,i+1),&i<3,\\
(h+1,0),&i=3,
\end{cases}
\qquad \Sigma(h,i)=(h+1,i).
\]

Thus \(q^4=\Sigma\). The fourth chart wrap changes the stable grade. It need
not change the independent witness-depth coordinate.

The [universal-category construction](../voevodsky/a-clean-universal-category-for-the-eight-lattice-four-chart-suspension-system.md)
declares the relevant exactness and helix relations. The
[graded Fourier lift](tetra-channel-comparison-and-graded-fourier-lift.md)
realizes the chart grading explicitly. Ordinary ungraded Fourier charts instead
have \(q^4=I\); the extra grading cannot be inferred from that identity alone.
See also the [four-chart comparison](four-charts-are-one-periodic-object-in-the-canonical-homeomorphism-groupoid.md).

Let \(P\) denote a separately defined witness-promotion functor. **If** one
constructs a coherent natural equivalence \(qP\simeq Pq\), then

\[
q^4P\simeq Pq^4,\qquad\Sigma P\simeq P\Sigma.
\]

The final shell comparison follows only if a natural identification of the
relative shell functor with this same suspension is supplied. Merely naming
witness and chart directions separately does not prove their commutation.

## 17. Witness helix and its two gradings

The proposed witness grammar is schematically

\[
E\longrightarrow T\longrightarrow\Delta\longrightarrow O,
\]

where E and T denote the proposed edge and triangular witness stages. These
stage names are not yet a definition of the promotion functor on objects,
morphisms and coherence cells.

The independent chart progression is

\[
X\longrightarrow qX\longrightarrow q^2X\longrightarrow q^3X
\longrightarrow\Sigma X.
\]

In the formal stable model this is a helix, not an ordinary four-periodic
cycle. A geometric presentation may recur while its stable grade changes.
Under the relative shell realization and naturality assumptions above, a full
shell step can be represented by \(X_{n+1}\simeq\Sigma X_n\). No increase of
physical time or equality of stable grade with witness depth is inferred.

## 18. Candidate structural chain

The proposed succession is:

1. photon-like diamond support;
2. tetrahedral closure;
3. octahedral incidence/cofiber comparison at the stated forgetful level;
4. canonical complement-odd metric quotient of dimension three;
5. positive outward shell, with relative boundaries specified;
6. suspension in the chosen chain/stable realization;
7. a proposed instance of the same witness grammar at the next stable grade.

With these qualifications, the supplied shorthand is

\[
\gamma_n\longrightarrow\Delta_n\longrightarrow O_n
\longrightarrow\Sigma X_n\longrightarrow\gamma_{n+1}.
\]

The shorthand records a candidate comparison programme, not an already
constructed physical evolution or a single verified composite functor.

## 19. Claim ledger

### Elementary identities supported by the displayed constructions

- The two seed faces have opposite shared-edge orientation and extend to the
  closed tetrahedral boundary chain.
- The six edge labels form the octahedral line graph and the six coordinate
  midpoints of the regular geometric octahedron.
- The complement-odd quotient has dimension three and the midpoint Gram is
  twice its quotient Gram.
- The sign-twisted quotient action is the area representation; on A4 it agrees
  with the untwisted spatial action.
- Removing the antipode of AB gives the five-vertex wheel and four triangles.
- The twelve centroid-edge triangles refine the four-face tetrahedral cycle.

### Existing formal constructions with stated input assumptions

- A coherent four-stage filtration in the declared exact/stable realization
  supplies its four cofiber triangles and octahedral compatibility.
- The relative product cellular chain complex is a homological suspension;
  the absolute shell remains homotopy equivalent to its boundary.
- The explicitly graded four-chart model satisfies \(q^4=\Sigma\), unlike
  the ungraded four-periodic presentation.

### Not established by this packet

- A metric/exact realization functor identifying the cofiber objects with the
  geometric midpoint model, rather than just their labels and incidence.
- A specified 11-dimensional cell sector inside the 25-dimensional ordered
  support field and its 14-dimensional complement.
- An independently selected wheel operator, rank-one spectral mode, and
  observables yielding the targets 11/25 and 14/25.
- The witness-promotion functor P and its coherent commutation with chart
  transport and the relative shell realization.
- Agreement of the quotient/shell metric with every historical analytic metric.
- Physical time, photon preparation, particle mass, electric charge, quark
  content, or a Standard Model identification.

The [spinor bridge](binary-tetrahedral-spinor-bridge.md) and
[native-loop audit](tetrahedral-native-rotation-loop.md) remain separate:
incidence promotion does not overturn the failed native spinorial-selection
test or derive a physical spinor factor.

## 20. Next falsifier: freeze the native spectral operator

The proposed inputs are the wheel's five support vertices, four triangular
sectors, inherited tetrahedral orientation, and complement-odd quotient.
Before a spectral test, specify:

1. the operator's domain: five-support amplitudes, the 25-entry ordered field,
   a chain complex, or the three-dimensional quotient;
2. its independently derived matrix and inner product;
3. the exact invariance action and selected eigenspace;
4. the observables that read D and C from its rank-one projector;
5. the injection/quotient identifying any claimed 11/14 sector split.

Wheel symmetry alone is insufficient to choose a unique invariant line: its
vertex action has separate hub and rim orbits, so its invariant vector space
has dimension two. An operator/eigenvalue selection is therefore substantive
additional data, not a consequence of the word “invariant.”

Freeze that operator before comparing with

\[
D=11/25,\qquad C=14/25.
\]

A mismatch would refute that specified operator's proposed spectral bridge,
not every unspecified “natural operator.” A match obtained by inserting the
targets or fitting a projector is not a derivation. A source-derived match
with a faithful comparison map would connect the photon-like incidence model
to the tetrahedral spectral construction at the declared mathematical level.

No spectral operator or new verification receipt is claimed in this packet.
