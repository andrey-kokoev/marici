# Arbitrary-n ABHY associahedron canonical-form pullback

## Theorem

For every `n>=4`, impose the positive ABHY affine constraints

$$
X_{ij}+X_{i+1,j+1}-X_{i,j+1}-X_{i+1,j}=c_{ij},
\qquad c_{ij}>0,
$$

with cyclic boundary variables set to zero, and use the fan variables

$$
x_r=X_{1,r},\qquad 3\le r\le n-1
$$

as coordinates on the resulting `(n-3)`-dimensional affine space `H_n`.
The positive region

$$
\mathcal A_n=H_n\cap\{X_{ij}\ge0\}
$$

is the ABHY kinematic associahedron. The pullback of the planar scattering form is its canonical form:

$$
\iota^*\Omega_n=\Omega(\mathcal A_n).
$$

Equivalently,

$$
\iota^*\Omega_n
=
\left(
\sum_{T\in\operatorname{Tri}(P_n)}
\prod_{d\in T}\frac1{X_d}
\right)
 dx_3\wedge\cdots\wedge dx_{n-1}.
$$

## ABHY realization

The mesh equations solve every planar variable `X_ij` as an affine-linear function of the fan coordinates and positive constants. The standard ABHY positivity argument gives:

1. one facet `X_d=0` for every polygon diagonal `d`;
2. a nonempty intersection of `n-3` facets exactly when their diagonals form a triangulation;
3. every such intersection is a simple vertex;
4. all other diagonal variables are positive there.

Thus the face poset is the noncrossing-diagonal poset and the vertices are precisely the triangulations. This identifies `A_n` as a simple associahedron for arbitrary `n`.

## Unimodular vertex coordinates

For a triangulation `T={d_1,...,d_(n-3)}`, let

$$
J_T
=
\det\left(
\frac{\partial X_{d_a}}{\partial x_b}
\right).
$$

For the reference fan `T_0={(1,3),...,(1,n-1)}`, the facet variables are the coordinates themselves, so

$$
J_{T_0}=1.
$$

Any two triangulations are connected by quadrilateral flips. Suppose `T_x=S union {x}` and `T_y=S union {y}` differ by one flip. Restricting the appropriate ABHY mesh relation to the rows consisting of `S` and the flipped variable expresses the new gradient row as minus the old flipped row plus an integral linear combination of the common rows. Row addition does not change the determinant and the minus sign reverses it. Hence

$$
J_{T_y}=-J_{T_x}.
$$

The flip graph is connected, so induction along any flip path gives

$$
J_T\in\{+1,-1\}
$$

for every triangulation. In particular, every vertex is nonsingular and the incident facet normals form a unimodular basis.

## Pullback term by term

The term of the scattering form associated with `T` is

$$
\epsilon_T
\bigwedge_{d\in T}d\log X_d.
$$

On `H_n`,

$$
\iota^*
\left(\bigwedge_{d\in T}d\log X_d\right)
=
\frac{J_T}{\prod_{d\in T}X_d}
 dx_3\wedge\cdots\wedge dx_{n-1}.
$$

The ABHY mutation orientation changes under the same flip as `J_T`; fixing the reference orientation gives

$$
\epsilon_TJ_T=1
$$

for every `T`. Therefore

$$
\iota^*\Omega_n
=
\sum_T
\frac{dx_3\wedge\cdots\wedge dx_{n-1}}
{\prod_{d\in T}X_d}.
$$

## Canonical-form identification

For a simple positive geometry, the canonical form admits its oriented vertex expansion. At a vertex `T`, the product of its incident facet equations is `prod_(d in T) X_d`, and its Jacobian coefficient is `epsilon_T J_T=1`. Consequently the vertex expansion is exactly

$$
\Omega(\mathcal A_n)
=
\sum_T
\frac{dx_3\wedge\cdots\wedge dx_{n-1}}
{\prod_{d\in T}X_d}.
$$

It has logarithmic poles on every diagonal facet, no other finite poles, and residues equal to the canonical forms of the corresponding product associahedra. Hence it is the uniquely normalized canonical form of `A_n`.

Combining the last two sections proves

$$
\iota^*\Omega_n=\Omega(\mathcal A_n)
$$

for arbitrary multiplicity.

## Relation to executable evidence

The exact checkers at `5<=n<=10` solve every vertex, verify positivity of all nonincident facets, compute all Jacobians, and check equality term by term. At ten points they cover 35 facets and 1,430 vertices. These are finite regression certificates for the mesh convention; the universal proof follows from flip connectivity, determinant mutation, and the simple-polytope vertex formula.

## Claim boundary

This proves the canonical-form pullback for the standard positive planar ABHY affine realization. It does not establish the same statement for arbitrary affine constants of indefinite sign, nonplanar or double-partial geometries, loop-level positive geometries, or general color-dressed scattering forms.
