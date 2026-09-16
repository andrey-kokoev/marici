# The complete-response Fourier graph is a canonical maximal-isotropic sewing relation

## Question

Does the function-valued Fourier--Poisson response determine the global maximal-isotropic sewing relation required by the G4 frontier?

## Claim boundary

Yes for the complete response essential image: the graph of its unitary order-four response operator is maximal isotropic for the canonical incoming-minus-outgoing boundary form. The remaining G4 obligation is to prove that the unchanged Evans shell trace belongs to this particular graph.

## Response Hilbert rung

Let

$$
\mathscr R(g)=(B_g,Q_g,A_g,C_g)
$$

be the complete response map. Its first coordinate is

$$
B_g=g,
$$

so on the essential image define the Hilbert pairing

$$
\langle\mathscr R(f),\mathscr R(g)\rangle_{\rm resp}
:=\langle f,g\rangle_{L^2}.
$$

This is nondegenerate because first-coordinate projection is the inverse response chart. It coexists with the stronger multi-rung graph topology used for endpoint and principal-value traces.

## Unitary response action

The exact response intertwiner satisfies

$$
\mathscr R(\mathcal Fg)
=\mathbb T\mathscr R(g).
$$

Since additive Fourier is unitary,

$$
\langle\mathbb T\mathscr R(f),
\mathbb T\mathscr R(g)\rangle_{\rm resp}
=
\langle\mathscr R(f),\mathscr R(g)\rangle_{\rm resp}.
$$

Thus \(\mathbb T\) is unitary on the response Hilbert essential image and has fourth power one.

## Boundary form

On incoming/outgoing response pairs define

$$
[(x_-,x_+),(y_-,y_+)]_\partial
=
\langle x_-,y_-\rangle_{\rm resp}
-
\langle x_+,y_+\rangle_{\rm resp}.
$$

Let

$$
\Lambda_{\mathbb T}
=
\{(x,\mathbb Tx):x\in\mathcal H_{\rm resp}\}.
$$

For two graph vectors,

$$
[(x,\mathbb Tx),(y,\mathbb Ty)]_\partial
=
\langle x,y\rangle
-
\langle\mathbb Tx,\mathbb Ty\rangle
=0.
$$

Hence the graph is isotropic.

## Maximality

Suppose \((u,v)\) is boundary-orthogonal to every \((x,\mathbb Tx)\). Then

$$
0
=
\langle u,x\rangle
-
\langle v,\mathbb Tx\rangle
=
\langle u-\mathbb T^*v,x\rangle
$$

for every \(x\). Therefore

$$
u=\mathbb T^*v,
$$

or equivalently

$$
v=\mathbb Tu.
$$

Thus \((u,v)\in\Lambda_{\mathbb T}\), proving

$$
\Lambda_{\mathbb T}^{\perp_\partial}
=\Lambda_{\mathbb T}.
$$

The relation is maximal isotropic.

## Fourier--Poisson response trace

For every source test vector \(g\), its full response trace is

$$
\left(\mathscr R(g),\mathscr R(\mathcal Fg)\right)
=
\left(\mathscr R(g),\mathbb T\mathscr R(g)\right)
\in\Lambda_{\mathbb T}.
$$

This includes value, Fourier value, moving-seam history, Hilbert principal-value response, and their endpoint traces. Placewise Tate factors and their logarithmic connection give the equivalent spectral description.

## Exact remaining membership gate

The G4 frontier concerns a particular Evans/prime-shell trace, not an arbitrary source response. To close that constructor one must establish a source identity

$$
\operatorname{Tr}_{\rm Evans}(z)
=
\left(\mathscr R(g_z),
\mathbb T\mathscr R(g_z)\right)
$$

for a declared source vector \(g_z\), including every prime shell and all retained ports. Existence of some graph representation cannot be inferred merely from isotropy or matching scalar determinants.

## Disposition

The complete Fourier--Poisson response carrier now has an explicit canonical maximal-isotropic sewing relation: the graph of the unitary response quarter turn. Global response intertwining is proved for every source-generated response vector. The remaining RH-bearing comparison is narrowed to source membership of the unchanged Evans shell trace in this graph, equivalently the existing prime-shell adjoint residual family.