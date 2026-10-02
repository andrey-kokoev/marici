# Octahedral monomial-projector realization: 7128 typed arrows

## Outcome

An exact octahedral instance of the
[monomial-projector support theorem](monomial-projector-support-theorem.md)
passes. Its three separately materialized stages have

\[
216+1728+5184=\boxed{7128}
\]

nonzero coefficient arrows. Their collective return is a rank-one projector
on 72 coefficient coordinates. This is a second geometric realization of the
architecture, not an identification of a new physical particle or mass.

The calculation uses rational arithmetic and Q(i*sqrt(3)); no empirical mass,
normalization fit or numerical tolerance enters the checks.

## Declared seeds and generated symmetry

Start with the unit-axis octahedron, whose six vertices are +/-e1, +/-e2, +/-e3.
Declare two spatial rotations:

\[
Q=\begin{pmatrix}0&-1&0\\1&0&0\\0&0&1\end{pmatrix},
\qquad
C=\begin{pmatrix}0&1&0\\0&0&1\\1&0&0\end{pmatrix}.
\]

Q is a quarter-turn about the third axis, and C is a cyclic coordinate rotation
of order three. Their matrix closure has exactly 24 elements. Every element is
a determinant-one signed permutation matrix. The faithful action on the four
cube body-diagonal lines realizes all 24 permutations, explicitly identifying
the group as S4.

These are new declared octahedral seeds; the original tetrahedral pair of face
cycles has not somehow acquired twelve additional rotations. As a control,
C and Q C Q^T generate only a twelve-element subgroup. In the body-diagonal
permutation action, order-three elements are even permutations, so face
120-degree rotations alone cannot generate the whole S4.

## Axis stabilizer and induced spatial action

Let H stabilize the unoriented first axis. Exact enumeration gives |H|=8.
It is the dihedral group D8, where the notation here means order eight: the
checker supplies a quarter-turn q and an involution s with

    q^4=1, q^2!=1, s^2=1, s q s=q^(-1), <q,s>=H.

On the first axis H acts by the sign character chi(h)=h_11. This character
takes each of +1 and -1 four times. Choosing representatives t_i with
t_i e1=e_i gives, whenever a t_i=t_j h,

\[
a e_i=\chi(h)e_j.
\]

The induced matrices match the actual spatial matrices entry by entry:

\[
\rho_{\mathrm{spatial}}\cong\operatorname{Ind}_{D_8}^{S_4}\chi,
\qquad [S_4:D_8]=3.
\]

Unlike V4 in A4, this axis stabilizer is not normal. S4/H is a three-element
coset set, not a quotient group. Discarding the signs gives the axis permutation
action with image S3 and kernel V4, not the faithful spatial action of S4.
The checker verifies the subgroup, character, induction formula, nonnormality,
and unsigned action sizes independently of the support count.

## Closed positive surface

Insert the centroid of each of the eight triangular faces. The orbit of

\[
(F_{+++},e_1,e_2),\qquad F_{+++}=(1,1,1)/3,
\]

under the 24 rotations gives 24 distinct outward-oriented small triangles.
There is exactly one per directed original octahedral edge. The orbit is free
and transitive, so its triangle positions form a torsor for the rotation group.

| Surface quantity | Exact value |
|---|---:|
| Vertices, including face centroids | 14 |
| Undirected subdivided edges | 36 |
| Oriented triangles | 24 |
| Euler characteristic | 2 |
| Signed cone volume per triangle | 1/18 |
| Total enclosed volume | 4/3 |

Every small triangle lies in an outward supporting plane; the oriented boundary
of their sum vanishes. Reversing one triangle produces three uncancelled boundary
edges. Flattening all vertices to z=0 makes every cone volume zero.

These checks establish a closed convex carrier. They do not establish spatial
embeddings of every intermediate coefficient-processing stage.

## Local eigenline and aligned collective mode

For the reference small triangle, let X0 have its three vertex coordinates as
columns. With omega=exp(2*pi*i/3), define

\[
c_{\mathrm{cycle}}=(1,\omega,\omega^2),\qquad
v_0=X_0c_{\mathrm{cycle}}
=\left(-\frac16+\frac{i\sqrt3}{2},
       -\frac16-\frac{i\sqrt3}{2},\frac13\right).
\]

Every spatial coordinate of v0 is nonzero, and ||v0||^2=5/3. This checks the
full-support hypothesis from the geometric triangle rather than substituting
an unrelated vector with convenient support.

For each rotation r, X_r=r X0, v_r=r v0, and A_r=X_r C X_r^(-1). Exact checks give

    A_r^3=I, A_r v_r=omega v_r, r^T v_r=v0.

As in the tetrahedral construction, A_r is a transported coefficient-cycle
operator, not necessarily a Euclidean rotation of its small triangle.

On the direct sum of 24 local three-dimensional coefficient spaces, define

\[
L=\bigoplus_r\frac{v_rv_r^\dagger}{\|v_r\|^2},\qquad
R_{rs}=\frac1{24}r s^T,\qquad
N=RL=LR=\frac{uu^\dagger}{40},
\quad u=(v_r)_r.
\]

The squared norm of u is 40. The ranks of L, R and N are respectively 24, 3
and 1. Sparse exact multiplication verifies Hermiticity, local/alignment
idempotence, and both intersection products. Collective idempotence follows
by exact rank-one norm factorization, and the checker also verifies Nu=u and
NR=N. Therefore the three-stage return NRL equals N.

## Explicit interaction graph

Use distinct raw, local-mode and aligned port types:

    raw --L--> local-mode --R--> aligned --N--> raw.

There are 72 ports per stage, hence 216 typed ports in all. A coefficient arrow
runs from the input column to the output row of its map.

| Operation | Support calculation | Arrows |
|---|---|---:|
| Local selection L | 24 * 3^2 | 216 |
| Signed symmetry alignment R | 24^2 * 3 | 1728 |
| Dense collective feedback N | 72^2 | 5184 |
| Typed arrow union | sum of the three supports | 7128 |

The checker enumerates all 7128 weighted arrows. Each feedback arrow closes
exactly one L-R-N three-step traversal. There are 5184 such traversals; their
union covers every arrow. Every traversal weight is the positive squared
modulus of the corresponding collective-projector entry, and their weights
sum exactly to one.

This is identity return only on the collective eigenline, not on arbitrary
72-dimensional inputs. Alternating the signs of the 24 transported vectors
leaves local selection intact but is annihilated by N: aligned projectors alone
do not enforce amplitude phase synchronization.

## Controls and limitations

- Replace dense feedback by 72 identity wires: the return is still RL=N, but
  the three-stage count is 216+1728+72=2016. No global minimum is claimed.
- Identify all three stage port types: the arrow-pair union has 5184 elements,
  not 7128. Separate stages are part of the counting convention.
- Replace v0 by the axis vector e1: the supports become 24, 1728 and 576. The
  dense-support theorem correctly no longer applies.
- Discard the signs in the transport matrices while retaining the original
  signed local projectors: local selection and alignment no longer commute.
  The unsigned coset action is not an interchangeable spatial transport.
- The cube has the same proper rotation group and spatial representation, so
  these group/representation data alone cannot distinguish cube from octahedron.
  However, the subsequent [cube/energy audit](cube-octahedron-architecture-independent-energy-audit.md)
  finds that the cube's face-derived cyclic eigenline has one zero coordinate.
  Its native full-stage support is 4128, with only 3552 arrows covered by selected
  closed traversals. The shared 7128 prediction applies only after supplying a
  full-support line; it does not automatically apply to the native cube geometry.
  The audit also distinguishes the shared-edge graph spectra using an explicit,
  architecture-independent but conditionally weighted trial Hamiltonian.
- There is no derived phase-locking law, stagewise spatial realization, energy
  weighting, particle sector or mass interpretation.

The octahedron extends the architecture beyond the tetrahedral example while
preserving the distinction between representation provenance and architecture
selection.

## Reproduction and artifacts

Run from the repository root:

    python research/nima/checkers/check_octahedral_monomial_projectors.py

The standalone entrypoint reuses the existing exact vector, matrix and complex
arithmetic helpers. It does not require a prior generated results file.

Generated artifacts, under the ignored results directory:

- `results/octahedral-monomial-projectors.json`: exact checks and triangle transports;
- `results/octahedral-7128-arrows.json`: all typed arrows and exact coefficient pairs;
- `results/octahedral-positive-geometry.obj`: the 24-triangle surface for viewing.

The OBJ uses decimal coordinates for interchange; its existence is not the
exact geometry proof. That proof uses rational coordinates in the checker.
