# Bridge-graph theorem and the one-way triangular falsifier

Owner: marici.Kitaev

## Question

Given several internally controlled sectors, when do a small number of bridge
constructors make them one coherent task object, and when does minimal
commutant falsely certify a merely one-way system?

## Claim boundary

Let

\[
V=\bigoplus_{i=1}^r V_i
\]

be a finite-dimensional complex task space. Assume the authorized internal
constructors contain every block endomorphism

\[
A_0=\bigoplus_{i=1}^r\operatorname{End}(V_i).
\]

For each added constructor \(T\), draw a directed edge \(j\to i\) whenever

\[
p_iTp_j\ne0.
\]

Because the diagonal blocks are full, one nonzero edge seed generates the
entire corresponding rectangular block:

\[
\operatorname{End}(V_i)(p_iTp_j)operatorname{End}(V_j)
=
\operatorname{Hom}(V_j,V_i).
\]

This follows by reducing the nonzero seed to a matrix unit with left and right
block multiplication, then moving that unit through every row and column.

Composition along a directed path generates the rectangular block associated
with its endpoints. Hence the constructor algebra records directed
reachability between sector blocks.

### Adjoint-closed bridge-graph theorem

If the authorized constructor family is closed under adjoint, every edge is
effectively bidirectional. Let \(G\) be the resulting undirected bridge graph.
Then the generated star-algebra is

\[
\bigoplus_{C\in\pi_0(G)}
\operatorname{End}\!\left(\bigoplus_{i\in C}V_i\right).
\]

Consequently:

\[
G\text{ connected}
\quad\Longleftrightarrow\quad
A=M_{\dim V}(\mathbb C)
\quad\Longleftrightarrow\quad
A'=\mathbb C I.
\]

More generally, the central commutant has one scalar coordinate for every
connected component. A spanning tree is algebraically sufficient and uses the
fewest edge incidences needed to connect \(r\) initially separate blocks.
Source typing can require more physical ports, but never fewer graph
incidences.

The \(D(S_3)\) electric qutrit is the case \(r=2\). The unequal pair-channel
adds the unique required bridge edge between the one- and two-dimensional
blocks.

### Directed constructor theorem

Without adjoint closure, directed reachability must be retained. Strong
connectivity is sufficient for all ordered rectangular blocks and therefore
for the full matrix algebra. Mere weak connectivity supplies only some
directions and can yield a proper block-triangular algebra.

This separates three constructor tasks:

- forward transfer asks for a directed path from source to target;
- mutual transfer asks for strong connectivity;
- coherent reversible control asks additionally for an authorized star or
  inverse-compatible realization.

These tasks must not share one completeness certificate.

### Smallest hostile witness

Take two one-dimensional blocks and one authorized bridge in only one
direction. The generated unital algebra is the upper-triangular algebra

\[
\mathcal T_2=
\left\{
\begin{pmatrix}
a&b\\
0&d
\end{pmatrix}:a,b,d\in\mathbb C
\right\}.
\]

Its commutant is scalar:

\[
\mathcal T_2'=\mathbb C I,
\]

yet \(\mathcal T_2\ne M_2(\mathbb C)\). It preserves the one-dimensional
subspace spanned by the first basis vector and cannot implement the reverse
bridge.

Therefore scalar commutant does not imply full constructor algebra for a
non-star-closed family. This falsifies minimal commutant as a universal
standalone completeness criterion.

The defect is detected by the invariant-subspace lattice, by failure of
strong connectivity, or by the unequal double commutant

\[
\mathcal T_2''\ne\mathcal T_2
\]

in the relevant operator closure. For finite-dimensional star-algebras these
pathologies disappear: invariant subspaces have invariant orthogonal
complements, and irreducibility invokes the full matrix conclusion.

### Revised relational-volume signature

The relational audit must therefore retain at least:

1. the directed bridge graph;
2. the invariant-subobject lattice relevant to the task;
3. the commutant and authorized center;
4. whether adjoints, inverses, or recovery maps are source-authorized;
5. the quantitative gain of every required bridge direction.

The commutant measures indistinguishable symmetries. The invariant-subobject
lattice measures unreachable or one-way decompositions. Neither replaces the
other outside semisimple star-closed control.

## Disposition

The new prediction is exact and scalable. With full internal block control,
the minimal number of algebraic bridge incidences for coherent star-closed
control is \(r-1\), arranged as a spanning tree. A lost bridge changes the
logical sector count exactly when it is a cut edge. Redundant cycles do not
change algebraic completeness but can improve fault tolerance and
conditioning.

The next constructor theorem should add weights to the bridge graph. Each edge
weight is its task-conditioned lower gain, resource cost, and fault modulus.
Algebraic connectivity then becomes only the zero/nonzero shadow of robust
connectivity. The completion-stable question is whether a spanning family
exists whose bottleneck gain stays uniformly positive.
