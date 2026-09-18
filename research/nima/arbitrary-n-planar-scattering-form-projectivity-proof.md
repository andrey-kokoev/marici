# Arbitrary-n projectivity of the planar scattering form

## Theorem

For every `n>=4`, let `Tri(P_n)` be the triangulations of a cyclically labelled convex `n`-gon. Equip each triangulation term with the standard ABHY mutation orientation, so adjacent terms induce opposite orientations on their common codimension-one partial triangulation, and define

$$
\Omega_n
=
\sum_{T\in\operatorname{Tri}(P_n)}
\epsilon_T
\bigwedge_{d\in T}d\log X_d,
$$

Then `Omega_n` is projective under a common local rescaling of all planar variables,

$$
X_d\longmapsto\Lambda(X)X_d,
$$

namely

$$
\Omega_n[d\log X_d+d\log\Lambda]
=
\Omega_n[d\log X_d].
$$

## Orientation convention

The flip graph of polygon triangulations is connected. Choose one oriented wedge for a reference triangulation and transport it across flips using the ABHY mutation rule. If `T_x=S union {x}` and `T_y=S union {y}` are the two completions of a codimension-one partial triangulation, this rule says that deleting the flipped entry from the two oriented wedges induces opposite orientations on the common ordered wedge `omega_S`.

This formulation includes both the coefficient `epsilon_T` and the permutation sign required to put each wedge into a chosen global channel order. It avoids treating the coefficient sign separately from wedge order. Changing the reference orientation multiplies the complete form by one overall sign.

## Rescaling variation

Every triangulation contains `n-3` diagonals. Under the rescaling,

$$
d\log X_d\longmapsto d\log X_d+d\log\Lambda.
$$

Because `dlog Lambda wedge dlog Lambda=0`, the transformed wedge has only its original term and terms containing exactly one `dlog Lambda`. Thus

$$
\delta\Omega_n
=
d\log\Lambda\wedge
\sum_T\epsilon_T
\sum_{x\in T}(-1)^{p_T(x)}
\bigwedge_{d\in T\setminus\{x\}}d\log X_d,
$$

where `p_T(x)` records the position needed to move `dlog Lambda` to the front.

## Pairwise cancellation

Fix a set `S` of `n-4` pairwise noncrossing diagonals that is obtained by deleting one diagonal from a triangulation. The partial triangulation `S` cuts the polygon into triangles and exactly one quadrilateral. There are exactly two ways to complete it to a triangulation: insert either quadrilateral diagonal `x` or `y`. Therefore every coefficient of

$$
d\log\Lambda\wedge\bigwedge_{d\in S}d\log X_d
$$

receives exactly two contributions, from

$$
T_x=S\cup\{x\},
\qquad
T_y=S\cup\{y\}.
$$

The mutation-orientation rule makes these two coefficients opposite after the wedge-ordering signs are included. Hence their sum vanishes.

Every variation term is indexed by one such `S`, so all terms cancel and

$$
\delta\Omega_n=0.
$$

This proves projectivity for arbitrary `n`.

## Combinatorial completeness

The proof uses only two facts valid for every convex polygon:

1. deleting one diagonal from a triangulation produces one quadrilateral and otherwise triangles;
2. a quadrilateral has exactly two diagonals.

Thus no bounded enumeration or assumption about small multiplicity enters the theorem.

## Relation to executable evidence

The exact checkers for `5<=n<=14` construct every triangulation, compute its ABHY orientation from the kinematic Jacobian, expand the exterior algebra after `dlog X -> dlog X+dlog Lambda`, and find zero variation. At fourteen points this checks 208,012 cubic-graph terms. These runs are regression certificates for the orientation convention; the universal proof is the codimension-one flip pairing above.

## Claim boundary

This proves projectivity of the abstract planar scattering form with the standard mutation orientation. It does not by itself prove that its pullback to an arbitrary ABHY affine subspace equals the associahedron canonical form, establish nonplanar scattering-form projectivity, or address loop-level scattering forms.
