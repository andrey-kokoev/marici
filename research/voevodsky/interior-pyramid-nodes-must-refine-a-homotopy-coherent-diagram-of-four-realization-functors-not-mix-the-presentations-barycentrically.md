# Interior pyramid nodes must refine a homotopy-coherent diagram of four realization functors, not mix the presentations barycentrically

## Typing problem

The provisional vertices were

\[
V_1=
\text{test/polarization},
\quad
V_2=
\text{semilocal geometry},
\quad
V_3=
\text{dual/canonical spectrum},
\quad
V_4=
\text{cutoff finite-part trace}.
\]

Taken literally, these are different kinds of mathematical objects: an algebra, a Hilbert representation, a paired spectral realization, and a scalar trace functional. Therefore an interior barycentric label

\[
(a_1,a_2,a_3,a_4)
\]

cannot mean a direct sum, tensor product, or weighted mixture of the four vertices without additional arbitrary choices.

The tetrahedron must first be retyped in a common higher category.

## Observer category

Fix a finite place stage `S`. Let

\[
\mathsf{Obs}_S
\]

be the `*`-category whose objects are admissible test functions `g` and whose polarized arrows encode pairs `(g,h)`. The distinguished positive observations are convolution squares

\[
g*g^*.
\]

The precise analytic test class must be inherited from the semilocal trace theorem.

## Common target category

Let

\[
\mathsf{Herm}
\]

be a category or `2`-category of Hermitian-form presentations. An object consists of:

1. a test domain;
2. a sesquilinear form on that domain;
3. optional factorization data through a Hilbert, Krein, trace, or distributional carrier;
4. a declared regularization when the form is defined as a finite part.

Morphisms preserve the represented form, and `2`-morphisms compare two such preservation proofs.

Every tetrahedral vertex must now be a functor

\[
\mathcal Q_i:
\mathsf{Obs}_S
\longrightarrow
\mathsf{Herm}.
\]

## Retyped four vertices

### Source realization `Q_1`

\[
\mathcal Q_1(g,h)
=
W_S(g*h^*),
\]

with endpoint, gamma, and finite-place terms defined directly from the explicit formula.

### Semilocal geometric realization `Q_2`

\[
\mathcal Q_2(g,h)
=
\text{the semilocal scaling/cutoff kernel pairing of }
U_S(g),U_S(h).
\]

The Hilbert space `L2(X_S)^K_S`, scaling representation, and Fourier cutoff pair are retained as factorization data.

### Spectral dual/canonical realization `Q_3`

\[
\mathcal Q_3(g,h)
=
\text{the differentiated dual--canonical pairing with phase }J_S.
\]

Its factorization data are the two weighted Hardy--Titchmarsh spaces and the pairing connection.

### Trace realization `Q_4`

\[
\mathcal Q_4(g,h)
=
\operatorname*{FP}_{\Lambda\to\infty}
\operatorname{Tr}
\left(
P_\Lambda\widehat P_\Lambda
U_S(g*h^*)
\right).
\]

The cutoff family and Plancherel volume counterterm are retained as regularization data.

Now all four vertices have the same external type: they are presentations of a Hermitian form on the observer category.

## Edge maps as natural comparisons

Each conductor edge is a natural transformation

\[
\eta_{ij}:
\mathcal Q_i
\Longrightarrow
\mathcal Q_j.
\]

For example:

\[
\eta_{12}
=
\text{integrated semilocal representation},
\]

\[
\eta_{23}
=
\text{Hardy--Titchmarsh transform},
\]

\[
\eta_{24}
=
\text{cutoff trace construction},
\]

\[
\eta_{14}
=
\text{Connes finite-part trace theorem}.
\]

The incomplete comparison `eta_34` is the spectral-connection versus cutoff-principal-value identification.

## Faces as modifications

A triangular face is a modification between natural transformations. For example,

\[
H_{123}:
\eta_{23}\eta_{12}
\Rrightarrow
\eta_{13}.
\]

The central unresolved face is

\[
H_{234}:
\eta_{34}\eta_{23}
\Rrightarrow
\eta_{24}.
\]

The tetrahedral filler is an equality or higher modification between the two composites of the four face modifications.

## Meaning of the edgewise subdivision

Once a homotopy-coherent map

\[
\Phi:
\Delta^3
\longrightarrow
N_{hc}(\mathsf{Real}_S)
\]

has been constructed, its seventh edgewise subdivision is obtained functorially:

\[
\operatorname{esd}_7(\Phi):
\operatorname{esd}_7(\Delta^3)
\longrightarrow
\operatorname{esd}_7
N_{hc}(\mathsf{Real}_S).
\]

The 120 lattice nodes are then subdivisions of comparison/homotopy data already present in `Phi`. They are not 120 new semilocal Hilbert spaces.

This is the correct meaning of repeated elementary transfers.

## Eight nodes on a conductor edge

An edge `C_ij` carrying eight nodes should be a seven-stage factorization of the natural comparison

\[
\eta_{ij}
=

d_{ij,6}
\circ
\cdots
\circ
d_{ij,0}.
\]

Each intermediate node must be a Hermitian-form presentation of the same observer functor. For example, the edge `C_24` might be factored through:

1. scaling representation;
2. physical cutoff;
3. Fourier-conjugate cutoff;
4. product cutoff;
5. kernel restriction;
6. ordinary trace;
7. volume subtraction;
8. finite-part local distribution.

This is only a candidate eight-stage factorization; it must be checked against the source and aligned with the seven stages on every other edge.

## Why the edge stages must align

The edgewise tetrahedral lattice assumes that “stage `r`” has compatible meaning on all six edges. If the eight nodes on `C_24` are arbitrary analytic steps while those on `C_13` are unrelated Euler-factor steps, face-interior nodes have no natural interpretation.

Therefore there must be seven global refinement parameters or transformations

\[
d_0,d_1,
\ldots,d_6
\]

whose restrictions to each edge give its eight-node factorization. This is stronger than choosing eight convenient points separately on every conductor.

## Positive filler

Rung-four positivity should be represented by an additional functor

\[
\mathcal F_S:
\mathsf{Obs}_S
\to
\mathsf{Hilb},
\]

and a natural equivalence

\[
\mathcal Q_1(g,h)
=
\langle
\mathcal F_Sg,
\mathcal F_Sh
\rangle.
\]

This positive realization is the apex/inner filler. It is not one of the four signed presentations unless independently constructed.

## Minimal next definition

Before assigning all 120 nodes, define the seven intermediate presentations on **one** conductor edge, preferably `C_24`, because Connes's theorem provides its endpoints and its internal cutoff operations.

Then ask whether the same seven stages restrict naturally to `C_12,C_13,C_14,C_23,C_34`. If not, the uniform edgewise-subdivision model must be replaced by a nonuniform simplicial refinement.

## Disposition

The four pyramid directions can be made well-typed by viewing them as realization functors

\[
\boxed{
\mathcal Q_i:
\mathsf{Obs}_S
\to
\mathsf{Herm}.
}
\]

Interior lattice nodes then refine natural transformations and homotopies; they do not barycentrically combine unlike presentations. The immediate next task is to define a source-backed seven-stage factorization of one edge and test whether it extends uniformly around the tetrahedron.
