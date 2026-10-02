# Monomial-projector support theorem and the tetrahedral 1836 realization

## Status and purpose

The number 1836 is derived exactly as the number of nonzero coefficient arrows
in a specified three-stage monomial-projector architecture. This note identifies
the representation-theoretic source of the existing tetrahedral realization:

\[
\rho_{\mathrm{spatial}}\cong\operatorname{Ind}_{V_4}^{A_4}\chi,
\qquad \chi\ne 1.
\]

It strengthens the explanation of the factors 12, 3 and 36. It does not prove
that tetrahedral symmetry selects this architecture, that 1836 is a global
minimum, or that its arrow count is a physical mass ratio.

The [original geometric construction](twelve-triangle-positive-geometry.md)
constructs the seed-generated group, local eigenlines and three operators.
The [minimality audit](twelve-triangle-net-minimality.md) and
[cost-bound audit](twelve-triangle-universal-cost-bound.md) remain applicable.

## Support theorem

Let G be a finite group of order g, and let

\[
\rho:G\longrightarrow U(m)
\]

be a unitary monomial representation in a specified orthonormal basis. Each
matrix has exactly one nonzero entry in each row and column, of unit modulus.
Choose a vector c in C^m with every coordinate nonzero, and put

\[
P_c=\frac{cc^\dagger}{\|c\|^2}.
\]

The realized coefficient ports are Q=G x {1,...,m}. More intrinsically, the outer
positions may be a G-torsor X; identifying X with G requires choosing a reference
position. The theorem counts support in the stated local bases, not under
arbitrary changes of basis.

### Local selection

For each x in G, define

\[
P_x=\rho(x)P_c\rho(x)^\dagger,
\qquad L=\bigoplus_{x\in G}P_x.
\]

Monomial transport preserves full coordinate support. Every P_x is consequently
a dense m-by-m rank-one orthogonal projector. Hence

\[
\operatorname{rank}L=g,
\qquad |\operatorname{supp}L|=gm^2.
\]

### Global alignment

Define T:C^m -> direct-sum_(x in G) C^m by

\[
(Tw)_x=\rho(x)w.
\]

Unitarity gives T^dagger T=gI. Therefore

\[
R=\frac1gTT^\dagger
\]

is the orthogonal projector onto the aligned fields, with rank m. Its blocks are

\[
R_{xz}=\frac1g\rho(x)\rho(z)^\dagger
      =\frac1g\rho(xz^{-1}).
\]

Each of the g^2 blocks has exactly m nonzero entries, so

\[
|\operatorname{supp}R|=g^2m.
\]

This is also a Reynolds projector for the combined action
(U_a v)_x=rho(a)v_(a^(-1)x): averaging U_a over G gives R. It is not merely
averaging rho on one local coefficient space.

### Collective intersection

Block multiplication gives

\[
(RL)_{xz}=\frac1g\rho(x)P_c\rho(z)^\dagger=(LR)_{xz}.
\]

Thus the two orthogonal projectors commute. Their product projects onto their
intersection:

\[
N=RL=LR=\frac1gTP_cT^\dagger
 =\frac{uu^\dagger}{g\|c\|^2},
\qquad u=(\rho(x)c)_{x\in G}.
\]

The vector u has full support and squared norm g||c||^2. Consequently

\[
\operatorname{rank}N=1,
\qquad N^2=N,
\qquad |\operatorname{supp}N|=g^2m^2.
\]

### Three separately typed stages

Implement the maps as

    raw ports --L--> local-mode ports --R--> aligned ports --N--> raw ports.

Each stage has gm ports. An arrow is a directed pair of typed ports with nonzero
map coefficient. Because the stages have distinct port types, their arrow
counts add:

\[
\boxed{M(g,m)=gm^2+g^2m+g^2m^2=gm(m+g+gm).}
\]

The return map is NRL=N, which is identity on the collective eigenline and a
projection on general inputs. This proves a support count for this realization,
not invertible return on the whole gm-dimensional space.

## Induced representations supply the monomial structure

Let H be a subgroup of G and chi:H -> U(1) a one-dimensional character. In a
coset basis,

\[
\rho=\operatorname{Ind}_H^G\chi,
\qquad m=[G:H],
\]

is unitary monomial. Explicitly, choose representatives t_i for the left cosets
G/H. If a t_i=t_j h with h in H, the induced action sends basis vector i to
chi(h) times basis vector j.

Thus (G,H,chi) supplies a representation with the required sparsity. Induction
is sufficient but is not an extra hypothesis needed in the support theorem
itself. The theorem applies to any unitary monomial representation.

For a full-support selected vector, the cardinality depends only on g and m,
not on chi. The signs/phases, selected line and matrix coefficients do depend
on the representation and vector. These data must not be inferred from support
counts alone.

## The actual tetrahedral representation

Use the original tetrahedral vertices

    A=(1,1,1), B=(1,-1,-1), C=(-1,1,-1), D=(-1,-1,1).

The axes through midpoints of opposite edges give the coordinate-axis frame.
The orientation-preserving group is A4, of order 12. Its Klein four subgroup is

\[
H=\{I,\operatorname{diag}(1,-1,-1),
       \operatorname{diag}(-1,1,-1),
       \operatorname{diag}(-1,-1,1)\}.
\]

The group permutes the three unoriented axis lines transitively; the stabilizer
of one such line is H=V4. Its action on that one-dimensional line is a nontrivial
character chi of H. For the first axis, chi(h)=h_11.

Choose representatives t_i carrying the first unit axis vector to the three
unit axis vectors. Then a t_i=t_j h implies

\[
a(t_i e_1)=t_j h e_1=\chi(h)t_j e_1.
\]

This is exactly the induced action in the axis basis. It identifies the
monomial basis, not merely an abstract equivalent representation:

\[
\rho_{\mathrm{spatial}}\cong\operatorname{Ind}_{V_4}^{A_4}\chi.
\]

The three nontrivial characters of V4 are conjugate under A4, so any of them
gives an equivalent induced representation. As a character check, write
Theta(a)=Tr(rho(a)). Then

\[
\Theta(e)=3,\qquad
\Theta(h)=-1\quad(h\in V_4\setminus\{e\}),\qquad
\Theta(a)=0\quad(a\notin V_4).
\]

On V4, this is the sum of its three nontrivial characters. Outside V4, the
induced matrices permute the three cosets without fixed points, hence have
zero trace. These are precisely the traces of the identity, half-turns and
120-degree tetrahedral rotations. Over C this is the irreducible
three-dimensional tetrahedral representation.

### Why ordinary coset permutation was insufficient

Inducing the trivial character instead gives C[A4/V4], the three-point
permutation representation factoring through A4/V4 ~= C3. Every element of
V4 acts trivially there. In the spatial representation its nonidentity elements
are nontrivial half-turns.

The quotient records which axis line goes where, but not its orientation sign.
Therefore the quotient permutation model has the same support counts but is
not the actual spatial action. The nontrivial character restores the missing
signs. Abstract representation equivalence alone would not establish sparsity
in an arbitrary basis; the explicit axis-basis construction above does.

## Matching the existing 1836 construction

In the original note, the local spatial eigenvector is v_0=X_0 c_cycle, with
c_cycle=(1,omega,omega^2). The selected vector c of this theorem is that spatial
vector v_0, not the triangle-slot vector c_cycle. Its three spatial coordinates
are nonzero, and its transported vectors are v_x=rho(x)v_0.

The notation matches as follows:

| This theorem | Original geometric note |
|---|---|
| rho(x) | spatial rotation R_g |
| c | reference spatial eigenvector v_0 |
| L | local selection L |
| R | alignment operator G |
| N | collective projector N |

The group symbol G here must not be confused with that note's operator G.
The twelve oriented small triangles, equivalently twelve directed tetrahedral
edges, form a free transitive A4-set. A reference triangle identifies their
positions with the group. The three local coordinate axes form the coset set
A4/V4 with the sign action described above. Thus

\[
g=12,\qquad m=[A_4:V_4]=3,\qquad |Q|=36,
\]

and

\[
|\operatorname{supp}L|=108,\quad
|\operatorname{supp}R|=432,\quad
|\operatorname{supp}N|=1296,\quad
M=1836.
\]

The three coordinates are spatial/contrast directions. This identification does
not introduce a separate three-state particle.

## Persistent backbone and unoriented exchanges

The [backbone/exchange decomposition](persistent-backbone-and-unoriented-exchange-decomposition.md)
organizes the support as M=P+2X, where P=gm^2+g^2m+gm retains formation and
diagonal closure, and X=binomial(gm,2) counts unoriented off-diagonal closure
pairs. This gives 1836=576+2(630) for the tetrahedron and
7128=2016+2(2556) for the octahedron. The note retains the complex exchange
weights, gives exact reconstruction of N, and treats the native cube as a
restricted-support comparison case. Persistent/exchange is the proposed
organizing interpretation for subsequent dynamics.

## What remains conditional

- The selected vector must have full support in the specified monomial basis.
- L, R and N must be separately materialized, with their nonzero coefficients
  counted as primitive arrows. Factoring a map changes that primitive graph.
- Dense N feedback is an architectural choice. Identity feedback uses gm wires
  and gives the same return RL=N: for this example, 108+432+36=576 arrows.
- Identifying stage port types changes the union count; for the dense N case,
  the union on a single shared port set has only (gm)^2 pairs.
- The existing minimality audit gives 73-arrow three-stage and 72-arrow two-pass
  factorizations under its distinct interface assumptions. It is not contradicted
  by this theorem.
- A change to a nonmonomial basis may change support, and a basis adapted to the
  selected line may destroy the full-support hypothesis.
- The count does not distinguish A4 from every other group. For example, C12
  with its order-four subgroup also has g=12 and m=3 and admits this architecture.
- The theorem supplies neither a physical energy weighting nor particle-sector
  identification. In particular, it does not derive a proton/electron mass ratio.

Representation provenance and architecture selection are separate obligations.
The former is sharpened here; the latter remains open.

## Why the unrestricted simplex extrapolation is demoted

Substituting g=n(n-1) and m=n-1 algebraically gives

\[
M=n(n-1)^3(n^2+1).
\]

But these substitutions are not generally supplied by simplex symmetry. For a
regular simplex with n vertices, n>=3, the proper symmetry group is A_n of order
n!/2, not generally n(n-1). For n>=5, simplicity also rules out a nontrivial
proper normal quotient analogous to A4/V4 ~= C3.

The natural structural input is a group representation, with (G,H,chi) a useful
induced presentation, rather than an unrestricted vertex-count formula. The
support theorem itself depends only on g, m and its explicit architectural and
basis hypotheses. The tetrahedral case supplies those representation data
naturally; it does not establish their universal physical selection.

## Worked octahedral extension

The [octahedral realization](octahedral-monomial-projector-realization.md)
constructs a second exact instance with g=24 and m=3. Its spatial action is
Ind_(D8)^(S4)(chi), where D8 denotes the order-eight stabilizer of an unoriented
axis and chi records the sign on that axis. The checker verifies the induced
matrices directly and enumerates 216+1728+5184=7128 typed arrows on a closed
24-triangle octahedral surface. Identity feedback gives 2016 arrows instead.
Unlike the tetrahedral V4 subgroup, this D8 is not normal: the three-element
coset set is not a quotient group.

    python research/nima/checkers/check_octahedral_monomial_projectors.py

The [cube versus octahedron energy audit](cube-octahedron-architecture-independent-energy-audit.md)
provides a geometric control: the cube shares this spatial representation but
its face-derived cyclic eigenline has one zero coordinate, so the full-support
hypothesis fails. Its native three-stage support is 4128, not 7128. This does not
contradict the theorem; it shows why selecting c from geometry must precede use
of the dense-support count. The same audit tests a shared-edge trial Hamiltonian
whose spectrum is independent of dense versus identity feedback implementation.

## Verification boundary

The theorem and induced-representation identification are proved algebraically
above. No new executable character or general support checker is introduced
by this documentation note.

The existing exact checker for the concrete realization is:

    python research/nima/checkers/check_twelve_triangle_positive_geometry.py

It checks the signed rotations, local and collective projectors, explicit
1836 typed arrows and closed traversals. The alternative implementation counts
are checked separately by:

    python research/nima/checkers/check_twelve_triangle_net_minimality.py

See also the [source-constraint spectral/LRG construction](lrg-1836.md). None of
these verification claims should be read as a physical mass identification.
