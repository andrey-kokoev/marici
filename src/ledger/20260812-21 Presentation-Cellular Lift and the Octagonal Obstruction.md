# Presentation-Cellular Lift and the Octagonal Obstruction

## Record

Date: 2026-08-12

Status: the six-point QTDS polarity comparison now has a canonical lift to the cellular chains
of the scalar associahedral presentation, after retaining the alternating cover. At eight
points, scalar parity-core cells canonically supply the eight factorization triangles and four
central square carriers. Together they form a Möbius band. Its boundary is exactly the previously
unexplained octagon, so a **weighted, local, deck-equivariant** octagonal filler is the first
global scalar-chain obstruction.

This closes the presentation-level differential gap. It does **not** yet construct a filtered
scalar-to-worldsheet comparison, a residue-free twisted primitive, or a chain-level inverse of
the scalar pairing.

## Three levels that must remain separate

The current result distinguishes:

1. the summed scalar surface function or shifted amplitude;
2. its triangulation-resolved presentation, enriched by cellular chains;
3. a logarithmic or twisted worldsheet chain complex.

The first object does not determine QTDS polarity descent. The second now does at six points and
canonically identifies carriers for all but one global two-cell at eight points. No canonical
comparison from the second to the third has yet been constructed.

## What the bare Cut Equation supplies

For a marked surface \(S\), the scalar surface function is

\[
G_S(x)=\sum_{\Gamma}\prod_{C\in\Gamma}x_C.
\]

It records triangulations in a preferred polynomial presentation. Its universal cut operators
are

\[
\Delta_C=\partial_{x_C},
\qquad
\Delta_CG_S=G_{S\setminus C}.
\]

The \(\Delta_C\) commute. They are not a square-zero boundary operator. After the monomials are
summed, equality of every physical cut determines a function only modulo the contact kernel.
Consequently neither the Cut Equation nor the summed function alone produces the polarity
homotopy \(h_6\).

The tropical formulation retains strictly more presentation data. Maximal cones are labeled by
scalar triangulations, and the headlight projectors satisfy

\[
\Theta_D(T)=
\begin{cases}
1,&D\in T,\\
0,&D\notin T.
\end{cases}
\]

For a partial quadrangulation \(Q\), the projectors

\[
P_Q=\prod_{D\in Q}\Theta_D,
\]

\[
P_D=\Theta_D\prod_{E\ne D}(1-\Theta_E),
\qquad
P_\varnothing=\prod_D(1-\Theta_D)
\]

separate full-core, one-core, and zero-core scalar cones. Under a physical cut,
\(\Theta_D\to1\), while projectors for curves crossing \(D\) vanish. This is the function-level
shadow of cut naturality, but it is still not a cellular differential.

## Minimal scalar presentation complex

Let \(K(\alpha)\) be the associahedron for cyclic order \(\alpha\), and retain its barycentric
subdivision. The minimal enrichment is

\[
C^{\rm pres}_{n,\alpha}
=
C_*(\operatorname{sd}K(\alpha);\mathcal L_\alpha)[[t]],
\]

with the cell-resolved shifted scalar element

\[
\Sigma_\alpha(t)
=
\sum_{T\in\operatorname{Tri}(\alpha)}
\left[
\prod_{d\in T}
\frac{1}{X_d+\sigma_d/t}
\right][T].
\]

The augmentation forgetting cell labels gives

\[
\epsilon(\Sigma_\alpha)=F_\alpha,
\qquad
\epsilon(\operatorname{gr}^{n-2}_t\Sigma_\alpha)=a_{R,n}.
\]

Unlike \(a_{R,n}\), the graded presentation element retains individual scalar cones and their
incidence relations. This is the correct domain for QTDS descent.

The parity-core rule extends from vertices to every associahedral face. For any noncrossing
dissection \(D\), set

\[
\pi_{\rm core}(D)=D\cap\mathcal D_{\rm phys}.
\]

This is an order-preserving map to the poset of even dissections and therefore induces a
canonical simplicial chain map on barycentric subdivisions. On a physical boundary \(D_0\), it
restricts combinatorially to the product of the two lower-point core maps. What remains
nontrivial is the weighted transfer from its fibers, not the existence of a bare incidence
differential.

## Rigidity of the scalar normal direction

One might try to manufacture the missing presentation directions by enlarging the scalar shift.
That does not work within the pure hidden-zero-preserving scalar geometry.

Impose preservation of every nonplanar invariant

\[
c_{ij}
=
X_{ij}+X_{i+1,j+1}-X_{i,j+1}-X_{i+1,j}.
\]

Exact linear algebra at \(n=4,6,8,10\) gives shift-space nullity one. The surviving direction is
the alternating same-parity shift. Additional normal directions would require relaxing the
hidden-zero constraints or adding species/control data.

The presentation cells, rather than an enlarged \(t\)-link, therefore carry the QTDS descent
data.

## Six points: the canonical scalar tripods

Let the three physical diagonals be

\[
D_0=(0,3),
\qquad
D_1=(1,4),
\qquad
D_2=(2,5).
\]

The fourteen scalar triangulations split as

\[
4+4+4+2.
\]

For each \(D_i\), the four triangulations with core \(\{D_i\}\) are the four vertices of the
square associahedral facet \(F_i\). The two remaining triangulations \(E_+\) and \(E_-\) are the
parity-central resolutions.

Each \(E_\varepsilon\) has exactly one flip-neighbor in every \(F_i\). In
\(\operatorname{sd}K(\alpha)\), let \(b_i\) be the barycenter of \(F_i\), and let
\(\gamma_i^\varepsilon\) be the incidence path

\[
E_\varepsilon
\longrightarrow
b(E_\varepsilon\leftrightarrow T_i^\varepsilon)
\longrightarrow
T_i^\varepsilon
\longrightarrow
b_i.
\]

These are two canonical tripods, exchanged by a one-step cyclic rotation. They define a genuine
cellular lift of the abstract flip triangle:

\[
\iota_\varepsilon(v_i)=b_i,
\]

\[
\iota_\varepsilon([v_i,v_j])
=
\gamma_j^\varepsilon-\gamma_i^\varepsilon.
\]

For a sum-zero contact vector \(c=(c_0,c_1,c_2)\), define

\[
\eta_6^\varepsilon
=
\sum_i c_i\gamma_i^\varepsilon.
\]

The common central endpoint cancels because \(\sum_i c_i=0\), and therefore

\[
\partial\eta_6^\varepsilon
=
\sum_i c_i b_i
=
q_{6,+}-q_{6,-}.
\]

Substituting the exact \(t^4\) scalar weights reproduces the contact redistribution of entry 20.
Since every \(c_i\) is contact, its function-level physical cuts vanish. This is the first
nonformal QTDS chain homotopy derived from scalar presentation geometry.

No literal triangle is a face of the ordinary hexagon associahedron: the \(F_i\) are disjoint
square facets. The tripods are the intrinsic replacement. Blowing up the simultaneous cut ideal

\[
(x_{03},x_{14},x_{25})
\]

would add an exceptional \(\mathbb P_+^2\simeq\Delta^2\), but that simplex alone would not know
the QTDS contact allocation. The scalar central resolutions do.

## Eight points: the scalar carrier is a Möbius band

The 132 scalar triangulations have core distribution

\[
|\rho|=2:96,
\qquad
|\rho|=1:32,
\qquad
|\rho|=0:4.
\]

The fibers have the following exact meanings:

- the twelve quadrangulations each have eight scalar refinements;
- the eight one-channel cores each have four refinements and label the eight factorization
  triangles;
- the four zero-core triangulations have unique diameters
  \((0,4),(1,5),(2,6),(3,7)\), and label the four square coherence carriers.

The eight triangles and four squares form a connected surface with

\[
V=12,
\qquad
E=24,
\qquad
F=12,
\qquad
\chi=0.
\]

Every interior edge has incidence two. The edges with incidence one are exactly the eight edges
of the global octagon. The carrier has rational Betti numbers

\[
(b_0,b_1,b_2)=(1,1,0),
\]

and is a Möbius band. Attaching the octagonal two-cell produces the projective-plane complex of
entry 19.

Therefore:

> Scalar maximal-cone and parity-core data canonically construct the complete eight-point
> coherence carrier except for one global octagonal cell.

The octagon is no longer one open condition among thirteen indistinguishable fillers. It is the
unique remaining global cell after scalar locality and factorization have identified the other
twelve carriers. Its boundary runs once around the Möbius band, so integral and sign-local-system
data cannot be discarded. A filler that exists only after dividing by two would expose the
expected \(\mathbb Z_2\) obstruction.

There is an essential anti-vacuity qualification. In the barycentric subdivision of the full
associahedron, adjacent octagon quadrangulations can be joined through the barycenter of their
shared physical facet. The resulting subdivided loop has a canonical cone through the barycenter
of the whole associahedron. Hence the octagon is **not** obstructed in ordinary cellular
homology. That cone ignores the scalar \(t\)-grade, channel denominators, cut/Alexander--Whitney
data, and polarity transport. The research question is whether a filler exists in the restricted
filtered coefficient system, not whether the loop bounds in a ball.

## Accordion geometry: useful local model, not the global answer

For a fixed reference dissection, an accordion complex is realized by a fan and accordiohedron.
Its \(\mathbf g\)-vector fan is a coordinate section of a refined associahedral fan, and the
accordiohedron is a projection of a suitable associahedron.

This makes accordiohedra natural local charts for the fibers of \(\pi_{\rm core}\). It does not
identify the global all-quadrangulation presentation complex with one accordiohedron: a single
accordion complex depends on a chosen reference dissection, while the Marici carrier retains all
twelve octagon quadrangulations and the cyclic deck action simultaneously.

The precise test is whether the scalar parity-core transfer is assembled from these projected
charts with transition maps whose Čech two-cocycle is the octagonal holonomy.

## Why the CHY lift is still open

A scalar cubic vertex is not by itself a CHY half-class. In generalized Pochhammer
regularization, the full loaded associahedron is a twisted cycle. Small loaded tori around cubic
boundary points are terms of its boundary or field-theory associated grade, and lower-face terms
are required for twisted-boundary cancellation.

Thus the natural first comparison is not directly to ordinary holomorphic twisted forms. It is
of the type

\[
\chi_\alpha^{\rm cell}:
\operatorname{gr}_t C^{\rm pres}_{n,\alpha}
\longrightarrow
\operatorname{Cous}_{D,V}^\bullet
(\overline{\mathcal M}_{0,n},\mathcal L_{\vartheta_n}),
\]

where the target retains boundary strata, normal orientation lines, monodromy, and the channel
\(V\)-filtration. At a cubic boundary point \(p_T\), its leading vertex term is schematically

\[
[T]
\longmapsto
\operatorname{gr}_t^{n-2}
\left[
\frac{\epsilon_T}
{\prod_{D\in T}\widetilde s_D(t)}
\mathbb T_T^{n-3}
\right],
\]

with \(\mathbb T_T^{n-3}\) a small loaded torus. The full facewise Pochhammer differential, not
the isolated vertex formula, is required.

Existing CHY data fixes the induced cohomology class but not this chain map. If \(H\) is supported
on a parity-central scalar cell and takes values in residue-free compactly supported forms, then

\[
\Phi_H=\Phi+\nabla H+Hd_{\rm sc}
\]

has the same periods, residues, factorization, and cohomology map while changing the image of
\(h_6\). The chain representative therefore remains genuinely underdetermined.

## Correct chain pairing and the contact-kernel test

The canonical derived pairing has one compactly supported entry:

\[
R\Gamma(\mathcal M_{0,n},\operatorname{DR}\mathcal L_{-\vartheta})
\overset L\otimes
R\Gamma_c(\mathcal M_{0,n},\operatorname{DR}\mathcal L_{\vartheta})
\longrightarrow
K[-2(n-3)].
\]

For generic nonresonant kinematics, regularization identifies ordinary and compactly supported
cohomology and yields the familiar BAS/intersection pairing. Its inverse is presently canonical
on middle cohomology, not between declared dg models. At a factorization divisor \(s_D=0\), the
Pochhammer factor

\[
(e^{2\pi i s_D/\Lambda^2}-1)^{-1}
\]

diverges and clean extension fails. The comparison must therefore be \(V\)-filtered and use the
channel nearby-cycle quotient before inversion.

At six points, let

\[
R=\bigoplus_{i=0}^2\operatorname{Res}_{D_i},
\qquad
K_{\rm ct}^\bullet=\ker R.
\]

Ordinary twisted cohomology already gives

\[
[\Omega_{6,+}]
=
[\Omega_{6,-}]
=
[(\operatorname{Pf}'A_6)^2].
\]

The first decisive worldsheet test is stronger:

\[
\boxed{
[\Omega_{6,+}-\Omega_{6,-}]
\stackrel{?}{=}0
\quad\text{in}\quad
H^3(K_{\rm ct}^\bullet,\nabla_6).
}
\]

Success requires a residue-free primitive

\[
\eta_6\in K_{\rm ct}^2
\]

that is the image of the scalar tripod, not an arbitrarily adjoined exact form.

## The combined missing morphism

The smallest adequate comparison object is a filtered facewise Pochhammer/Cousin map

\[
\mathbf\chi_\alpha:
\operatorname{Rees}_t C_{\rm sc,\alpha}^\bullet
\longrightarrow
\operatorname{Rees}_{t,V_D}
\operatorname{Cous}_D^\bullet
\operatorname{DR}(\mathcal L_{\vartheta_n}),
\]

with:

1. individual scalar-face to worldsheet-stratum assignments;
2. the complete facewise differential;
3. compatibility with \(\operatorname{gr}^{n-2}_t\);
4. residue/Alexander--Whitney compatibility;
5. nearby-cycle specialization at \(s_D=0\);
6. Verdier-dual chain pairing;
7. a composition-stable acyclic kernel.

Only after this exists is

\[
\Phi_\alpha
=
(I_{\rm ch}^\flat)^{-1}\circ\mathbf\chi_\alpha
\]

meaningful at chain level.

## Next finite falsification test

At eight points, build the two-skeleton incidence matrices of
\(\operatorname{sd}K(\alpha)\) and the quadrangulation presentation complex over the polarity
local system \(\mathbb Z_\eta\). Fix:

1. the 96 full-core vertex carriers;
2. the eight factorization-triangle restrictions;
3. the four central-diameter square carriers;
4. dihedral/deck covariance;
5. local channel-denominator support.

Solve

\[
dM_2=M_1d
\]

and compute the remaining boundary on the octagon \(O\).

- A local scalar two-chain mapping to \(O\) establishes the first non-tautological eight-point
  augmentation.
- A nonzero integral/sign-local-system class obstructs strictification.
- A solution only after division by two identifies a \(\mathbb Z_2\) anomaly.

In parallel, the six-point CHY test is to construct the image of the exact weighted scalar
tripod in \(K_{\rm ct}^2\) and verify its twisted differential and all three vanishing residues.

## Reproducible audits

Run:

    python research/nima/check_surface_rees_carrier.py
    python research/nima/check_qtds_descent.py

The first checks shift rigidity, the two six-point scalar tripods, the eight-point Möbius
carrier, and the vacuous bare octagon cone. The second checks exact scalar-cell weights, the full
projective-plane cellulation, parity-core counts, and Jordan endpoint placement.

## Sources and provenance

- [Arkani-Hamed, Frost, and Salvatori, *The Cut Equation*](https://arxiv.org/html/2412.21027v2)
  defines scalar surface functions as triangulation-generating polynomials and their commuting
  cut derivatives.
- [Arkani-Hamed and Figueiredo, *Tropical Amplitudes for Colored Lagrangians*](https://arxiv.org/html/2402.06719)
  supplies the cone-wise headlight projectors and their factorization rule.
- [Mizera, *Combinatorics and Topology of Kawai--Lewellen--Tye Relations*](https://arxiv.org/abs/1706.08527)
  supplies the loaded-associahedron/Pochhammer framework for twisted cycles and intersections.
- [Manneville and Pilaud, *Geometric Realizations of the Accordion Complex of a Dissection*](https://arxiv.org/html/1703.09953)
  proves the fan, polytope, section, and associahedral-projection results used as the candidate
  chartwise geometry.

The scalar tripods, Möbius-band carrier, pure-shift nullity audit, vacuous-cone guardrail, and
combined chain-level interpretation are Marici results.

## Decision

Promote:

> QTDS polarity descent is intrinsic to the alternating scalar **presentation-cell complex** at
> six points. At eight points the scalar presentation supplies a Möbius carrier, and the global
> octagonal filler is the first unresolved **weighted and equivariant** scalar-chain problem.

Do not promote:

> The summed scalar amplitude, bare Cut Equation, generic CHY pairing, or ordinary contractibility
> of the associahedron already supplies the QTDS chain strictification.

The immediate Nima frontier is sharply bifurcated:

1. solve or obstruct the integral/sign-local-system octagonal filler at eight points under the
   filtered locality constraints;
2. map the six-point scalar tripod into residue-free twisted chains through a filtered facewise
   Pochhammer/Cousin comparison.

Entry 22 refines the first branch to the deck-odd octagonal contact class and records the exact
orientation-local-system and double-cover audit.
