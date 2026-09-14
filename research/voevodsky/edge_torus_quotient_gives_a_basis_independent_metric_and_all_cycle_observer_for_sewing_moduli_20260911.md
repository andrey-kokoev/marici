# Edge-torus quotient gives a basis-independent metric and all-cycle observer for sewing moduli

## Question

Can sewing holonomy be metrized and observed without choosing a cycle basis whose coordinates alter the numerical stability constant?

## Claim boundary

The construction applies to a finite connected graph with a declared positive edge metric. It gives a basis-independent quotient metric, an injective all-cycle Wilson observer, and existence of graph-dependent bi-Lipschitz constants. “Canonical” means independent of orientation and cycle-basis presentation once the edge metric is fixed. It does not mean independent of all geometric weighting choices, nor does it supply a graph-uniform constant over unbounded graph families.

## Edge and gauge tori

Let \(\Gamma=(V,E)\) be a finite connected graph. Choose an orientation only to write coordinates. An edge phase assignment is

\[
z=(z_e)_{e\in E}\in\mathbb T^E,
\qquad
\mathbb T=U(1).
\]

The vertex gauge torus \(\mathbb T^V\) acts by

\[
(g\cdot z)_e=g_{t(e)}z_e g_{s(e)}^{-1}.
\]

The diagonal subgroup acts trivially, so the effective gauge group is

\[
\mathbb T^V/\mathbb T.
\]

The sewing-moduli torus is the orbit space

\[
\mathcal M_\Gamma=
\mathbb T^E/(\mathbb T^V/\mathbb T),
\]

canonically identified as a compact abelian group with

\[
H^1(\Gamma;\mathbb T).
\]

No cycle basis appears in this definition.

## Basis-independent quotient metric

Give each unoriented edge a positive weight \(\lambda_e\). On \(\mathbb T^E\), define the weighted chord metric

\[
d_E(z,z')^2
=
\sum_{e\in E}\lambda_e|z_e-z'_e|^2.
\]

Vertex gauge acts by coordinatewise unitary multiplication and therefore by isometries. Define

\[
d_\Gamma([z],[z'])
=
\inf_{g\in\mathbb T^V}
d_E(z,g\cdot z').
\]

Because the acting group is compact, the infimum is attained. Since gauge orbits are compact and disjoint, zero quotient distance implies equality of orbits. Thus \(d_\Gamma\) is a genuine metric on \(\mathcal M_\Gamma\).

Reversing an edge orientation replaces its coordinate by its inverse. Since

\[
|z^{-1}-(z')^{-1}|=|z-z'|,
\]

orientation reversal is an isometry. Changing a cycle basis does nothing to the definition. If equal edge weights are used, every graph automorphism acts isometrically. If physical edge weights are supplied, automorphisms preserving those weights act isometrically.

There is no basis-independent numerical metric without some edge-scale datum: multiplying every \(\lambda_e\) rescales the metric. The unweighted choice \(\lambda_e=1\) is combinatorially canonical but not automatically physical.

## All-cycle Wilson observer

Let \(\mathscr C(\Gamma)\) be the finite set of oriented simple cycles. For \(c\in\mathscr C(\Gamma)\), define

\[
\operatorname{Hol}_c(z)
=
\prod_{e\in c}z_e^{\varepsilon(c,e)},
\]

where \(\varepsilon(c,e)\in\{-1,0,1\}\) records oriented incidence.

Each holonomy is gauge invariant, so the map

\[
\mathcal W_\Gamma:\mathcal M_\Gamma
\longrightarrow
\mathbb T^{\mathscr C(\Gamma)},
\qquad
[z]\longmapsto
(\operatorname{Hol}_c(z))_c
\]

is well defined.

It is injective. Indeed, equality of all simple-cycle holonomies implies equality on every integral cycle, because closed walks decompose into simple cycles. The ratio assignment \(z(z')^{-1}\) then has trivial cycle holonomy and is a vertex coboundary, so \(z\) and \(z'\) are gauge equivalent.

The use of all simple cycles is redundant but basis independent. Redundancy here prevents presentation choice; it is not evidence of additional moduli dimension.

## Quadrature realization

Define

\[
\Psi_\Gamma([z])
=
\bigl(
\operatorname{Re}\operatorname{Hol}_c(z),
\operatorname{Im}\operatorname{Hol}_c(z)
\bigr)_{c\in\mathscr C(\Gamma)}
\in
\mathbb R^{2|\mathscr C(\Gamma)|}.
\]

This is a continuous injective map from a compact space into a Hausdorff space, hence a topological embedding. It is invariant under vertex gauge and equivariant under graph automorphisms, which permute cycle coordinates. Edge-orientation reversal only exchanges a cycle with its reverse and flips the imaginary quadrature.

Complex conjugation acts by

\[
P_c\longmapsto P_c,
\qquad
Q_c\longmapsto-Q_c.
\]

Thus the all-cycle observer retains the Real-even and Real-odd decomposition without choosing a basis.

## Quantitative stability

Equip the target with the Euclidean metric, optionally weighting a cycle and its reverse equally. There exist graph-dependent constants

\[
0<\alpha_\Gamma\le L_\Gamma<\infty
\]

such that

\[
\alpha_\Gamma d_\Gamma(m,m')
\le
\|\Psi_\Gamma(m)-\Psi_\Gamma(m')\|
\le
L_\Gamma d_\Gamma(m,m')
\]

for all \(m,m'\in\mathcal M_\Gamma\).

### Upper bound

Every cycle holonomy is a finite product of edge phases. The telescoping product estimate bounds its chord difference by the sum of chord differences along that cycle. Taking the finite direct sum gives \(L_\Gamma<\infty\).

### Local lower bound

The tangent space of the quotient torus is the weighted orthogonal quotient of real edge cochains by vertex coboundaries. The derivative of all cycle arguments is the evaluation map on integral cycles. It is injective on the quotient because a real edge cochain annihilating every cycle is a coboundary. Finite dimensionality gives a positive least singular value at the identity. Translation invariance of the torus and character structure give the same local constant at every point.

### Global lower bound

Choose a neighborhood of the diagonal where the local estimate holds. On the compact complement of that neighborhood in

\[
\mathcal M_\Gamma\times\mathcal M_\Gamma,
\]

injectivity makes the numerator strictly positive, while the denominator is bounded. Their ratio attains a positive minimum. Combining the local and off-diagonal bounds gives \(\alpha_\Gamma>0\).

This proves existence, not a graph-uniform or sharp formula.

## Relation to cycle-basis coordinates

Choosing a cycle basis identifies

\[
\mathcal M_\Gamma\cong\mathbb T^{b_1(\Gamma)}.
\]

The chord product metric in those coordinates depends on the chosen integral basis. It is one presentation metric, not the intrinsic quotient metric above. For each fixed basis, finite-dimensional compact-torus arguments give bi-Lipschitz equivalence with \(d_\Gamma\), but the constants may deteriorate under large integral basis changes.

The correct basis-change statement is therefore:

- the quotient metric \(d_\Gamma\) is unchanged;
- coordinate metrics are comparison presentations;
- each coordinate presentation has finite comparison constants;
- no uniform constant over all \(GL(b_1,\mathbb Z)\) basis changes is asserted.

## Product-observer consequence

Let \(T_X:X\to Z_X\) be the stable bulk/source observer from Phases 2--4, with lower constant \(\delta_X\). Equip

\[
X\times\mathcal M_\Gamma
\]

with

\[
d^2=\|x-x'\|_X^2+d_\Gamma(m,m')^2.
\]

Then

\[
(x,m)\longmapsto(T_Xx,\Psi_\Gamma(m))
\]

is lower Lipschitz with basis-independent constant

\[
\min(\delta_X,\alpha_\Gamma).
\]

“Basis independent” refers to the definition and value of \(\alpha_\Gamma\) for the fixed edge and target metrics. It is not a universal constant independent of \(\Gamma\).

## Green--Real sewing consequence

For the radial sewing network:

- local wall phases are edge-torus presentation data;
- vertex phase changes are gauge;
- loop holonomies are the quotient moduli;
- all-cycle quadratures are gauge invariant;
- real quadratures are Real-even;
- imaginary quadratures are Real-odd;
- Green comparison cells transport edge presentations but do not alter the quotient definition.

This removes the prior cycle-basis dependence from the moduli metric and observer at the price of a finite redundant cycle family.

## Deliberate failures

1. A coordinate chord metric on \(\mathbb T^{b_1}\) is not basis independent.
2. Choosing one spanning tree is a computational gauge, not canonical moduli data.
3. Real quadratures alone do not distinguish a holonomy from its conjugate.
4. All-cycle redundancy does not increase moduli dimension.
5. Existence of \(\alpha_\Gamma\) does not imply a constant uniform over all finite graphs.
6. No metric can be numerically canonical without a declared edge-scale convention.

## Disposition

The edge-torus quotient supplies a basis- and orientation-independent sewing-moduli metric once positive edge weights are declared. The all-simple-cycle Wilson observer is gauge invariant, injective, Real graded, and bi-Lipschitz with graph-dependent constants. It composes with the stable bulk observer through the explicit product theorem without confusing finite relational observation with essential bulk coercivity.
