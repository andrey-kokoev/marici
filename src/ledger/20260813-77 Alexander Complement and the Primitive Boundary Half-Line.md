# Alexander Complement and the Primitive Boundary Half-Line

## Record

Date: 2026-08-13

Status: exact monomial-resolution and maximal-boundary pairing theorem.  The
primitive generator of every quadrangulation chart is the factorized
restriction of the scalar-derived half-class \(\mathsf J\), up to its fixed
normal-orientation sign.  Entry 78 proves the unfiltered derived comparison
between adjacent charts and isolates four missing overlap intervals needed
for the support-filtered Beck--Chevalley attachment.

Entry 76 identified the weighted interval cube with an actual scalar
associahedral face.  This entry identifies its primitive homology class with
the boundary value of

\[
\mathsf J
=
I_{\rm scalar}^{-1}\operatorname{gr}_R A_{\rm scalar}.
\]

The identification is exact on the induced maximally factorized channel
quotient.  It is not yet a global chain-level inverse-pairing theorem.

## The occurrence ideal is squarefree

For one maximal quadrangulation \(Q\), let its quadrilateral regions be
indexed by \(r=1,\ldots,m-1\), and write

\[
\mathfrak p_r=(X_{r0},X_{r1})
\]

for the two scalar refinements of region \(r\).  The variables belonging to
different regions are disjoint.  Therefore

\[
\boxed{
I_Q
=
\prod_{r=1}^{m-1}\mathfrak p_r
=
\bigcap_{r=1}^{m-1}\mathfrak p_r.
}
\]

The equality is immediate on monomials: membership in the intersection means
divisibility by at least one variable from every regional pair, which is
exactly membership in the product.

Thus \(I_Q\) is a squarefree monomial ideal.  For a refinement word

\[
v=(v_1,\ldots,v_{m-1})\in\{0,1\}^{m-1},
\]

define

\[
w_v=\prod_rX_{r,v_r},
\qquad
m_v=\prod_rX_{r,1-v_r},
\qquad
M_Q=\prod_rX_{r0}X_{r1}.
\]

Then

\[
\boxed{
w_vm_v=M_Q.
}
\]

The two sets \(\{w_v\}\) and \(\{m_v\}\) are the same minimal generating set
of \(I_Q\), related by the antipodal involution \(v\mapsto1-v\).  The
opposite-monomial map is therefore the squarefree Alexander complement on
the occurrence generators.

Writing the prime decomposition as above, the Alexander-dual ideal with
respect to the full squarefree support is

\[
\boxed{
I_Q^\vee
=
\bigl(
X_{10}X_{11},
\ldots,
X_{m-1,0}X_{m-1,1}
\bigr).
}
\]

Its generators have disjoint supports, so \(I_Q^\vee\) is a complete
intersection.  The cubical resolution of \(I_Q\) is the corresponding
cellular side of this resolution duality.  This terminology agrees with the
standard lcm-labeled cellular-resolution construction of Bayer--Sturmfels
and its Alexander-dual formulation by Miller.

## The cubical resolution is minimal

Label every vertex of the \((m-1)\)-cube by \(m_v\), every face \(F\) by

\[
m_F=\operatorname{lcm}_{v\in\operatorname{Vert}(F)}m_v,
\]

and set

\[
d[F]
=
\sum_{F'\prec F}
\epsilon(F,F')
\frac{m_F}{m_{F'}}[F'].
\]

This is precisely

\[
K_Q^{\rm w}
=
\bigotimes_{r=1}^{m-1}
\left[
A h_r
\xrightarrow{\ X_{r1}e_{r1}-X_{r0}e_{r0}\ }
A e_{r0}\oplus A e_{r1}
\right].
\]

Each factor resolves \((X_{r0},X_{r1})\), and the variable sets are disjoint,
so the tensor product resolves \(I_Q\):

\[
H_0(K_Q^{\rm w})\simeq I_Q,
\qquad
H_i(K_Q^{\rm w})=0\quad(i>0).
\]

Every nonzero cell-to-facet coefficient is one scalar variable, never a
unit.  Hence the multigraded resolution is minimal.  At eight points its
free ranks are

\[
(8,12,6,1).
\]

The construction is a concrete instance of the general lcm-labeled
cellular-resolution criterion: the labels and differential are forced by
the scalar occurrence generators rather than added as auxiliary target
data.

## One quadrilateral fixes the pairing normalization

Let one quadrilateral have planar variables

\[
x=X_{r0},
\qquad
y=X_{r1}.
\]

Entry 12 gives, in the same one-dimensional Parke--Taylor basis,

\[
a_{R,4}=-(x+y)
\]

and

\[
m_4
=
\frac1x+\frac1y
=
\frac{x+y}{xy}.
\]

Derived index raising is therefore elementary:

\[
\boxed{
\mathsf J_4
=
m_4^{-1}a_{R,4}
=
-xy
}
\]

in the conventions fixed by entry 12.

The weighted interval augmentation is

\[
\phi_r(e_{r0})=y,
\qquad
\phi_r(e_{r1})=x.
\]

In Laurent homology define

\[
g_r=[xe_{r0}]=[ye_{r1}].
\]

Then

\[
\phi_r(g_r)=xy,
\]

and hence

\[
\boxed{
\mathsf J_4=-\phi_r(g_r).
}
\]

This proves that the primitive weighted-interval class is the local
scalar-derived half-class, up to the already fixed four-point orientation
sign.

The polarized occurrence element

\[
c_r=xe_{r0}+ye_{r1}
\]

satisfies

\[
[c_r]=2g_r,
\qquad
\phi_r(c_r)=2xy.
\]

The coefficient two is therefore the sum of the two scalar endpoint
representatives of one primitive half-class.  It is neither torsion nor a
freely chosen normalization.

## Maximal quadrangulation boundary theorem

Let \(Q\) be a maximal quadrangulation of a \(2m\)-gon.  It has \(m-1\)
quadrilateral regions.  Define

\[
g_Q=\bigotimes_{r=1}^{m-1}g_r,
\qquad
\phi_Q=\bigotimes_{r=1}^{m-1}\phi_r.
\]

Then

\[
\phi_Q(g_Q)
=
\prod_{r=1}^{m-1}X_{r0}X_{r1}.
\]

The boundary Verdier pairing is monoidal on the induced channel quotient,
and entry 39 proves the cohomological factorization law

\[
\Delta_Q^+\mathsf J_{2m}
=
\varepsilon_Q
\bigboxtimes_{r=1}^{m-1}\mathsf J_4^{(r)},
\]

where \(\varepsilon_Q\) is the ordered plumbing-normal orientation sign.
Substituting the exact four-point normalization gives

\[
\boxed{
\Delta_Q^+\mathsf J_{2m}
=
\varepsilon_Q(-1)^{m-1}\phi_Q(g_Q).
}
\]

Thus \(g_Q\) is the primitive scalar-derived boundary half-class on every
maximal quadrangulation chart.

For the full regional polarization,

\[
\boxed{
\left[
\bigotimes_{r=1}^{m-1}c_r
\right]
=
2^{m-1}g_Q.
}
\]

At eight points this specializes to

\[
[c_0\otimes c_1\otimes c_2]
=
8g_0\otimes g_1\otimes g_2.
\]

The factor \(2^{m-1}\) is now completely typed: it is the index of the fully
polarized occurrence sum inside the primitive factorized half-line.  It does
not rescale the physical amplitude.

## What has become local and what remains global

For every maximal quadrangulation \(Q\), the scalar boundary geometry now
provides

\[
\mathcal J_Q^{\rm loc}
:=
H_0(K_Q^{\rm w})
\simeq I_Q.
\]

Polynomially this is a torsion-free rank-one ideal which is nonfree at the
joint coordinate loci.  After Laurent localization it becomes a line with
canonical normalized generator \(g_Q\).

This changes the global problem.  We no longer need to discover the local
half-object on a quadrangulation chart.  We need to glue the already
identified local half-lines:

\[
\boxed{
\{\mathcal J_Q^{\rm loc},g_Q\}_{Q}
\quad
\xrightarrow{\text{dependent route coherences}}
\quad
\mathsf J.
}
\]

The eight-point pentagon/square problem is the first transition map in this
atlas.  Entry 76 proves that its vertical caps and cube exist.  The missing
map is not an ordinary derived comparison: entry 78 proves that comparison
exists and is unique up to homotopy.  What remains is its support-filtered
Beck--Chevalley refinement, which must identify four route-overlap intervals
with the four pairwise intersections of the regional belt facets.

## Excess-intersection interpretation

The emerging six-functor schematic is

\[
\operatorname{Cut}_{D,E}\operatorname{Sp}_R
\quad\Longrightarrow\quad
\operatorname{Sp}_{R|D,E}\operatorname{Cut}_{D,E}.
\]

On the transverse domain of entry 38 this base-change map is strict.  The
dependent route pentagons are the first locus where ordinary face
intersection is insufficient.  The complex \(K_Q^{\rm w}\) is an exact
candidate for the excess complex: it resolves the squarefree occurrence
ideal, its scalar-edge quotient is sent to zero, and its caps/cube supply the
higher coherence.

This interpretation is a strong inference, not yet a theorem about the
underlying scalar parameter space.  To promote it one must construct the
actual multi-normal deformation or specialization correspondence and show
that its excess base-change morphism induces \(\beta_Q^{\alpha'}\).

## Epistemic boundary

Established:

1. \(I_Q=\prod_r\mathfrak p_r=\cap_r\mathfrak p_r\) is squarefree;
2. opposite occurrence monomials are Alexander complements;
3. \(K_Q^{\rm w}\) is the minimal cubical resolution of \(I_Q\);
4. the four-point primitive class maps exactly to \(-\mathsf J_4\);
5. channel-quotient monoidality identifies \(g_Q\) with the maximally
   factorized boundary of \(\mathsf J_{2m}\);
6. the full regional polarization is \(2^{m-1}\) times that primitive class;
7. the route source admits a polynomial augmentation onto \(I_Q\), hence an
   unfiltered comparison lift unique up to homotopy;
8. the established support filtration lacks exactly four primitive
   middle-interval bridges.

Not established:

1. a global chain-level identification of the complement map with
   \(I_{\rm scalar}^{-1}\) away from the factorized channel quotient;
2. intrinsic scalar provenance for the four bridges and the resulting
   support-filtered Beck--Chevalley transition between local
   \(\mathcal J_Q^{\rm loc}\) charts;
3. a geometric excess-intersection theorem for the scalar rank-jump
   specialization;
4. horizontal Jordan coherence around the quadrangulation compatibility
   complex.

Reject:

> The weighted cube is only a target invented to absorb a route obstruction.

Also reject:

> Reproducing the local primitive class already proves that the
> quadrangulation atlas glues globally.

## Next formula objective

Entry 78 constructs the previously requested augmentation:

\[
\boxed{
a_Q(c_{i,v})=m_v,
\qquad
a_Q:\mathcal C_Q^{\rm route}\twoheadrightarrow I_Q[-2].
}
\]

Every established Čech column maps to \(m_v-m_v=0\), so the comparison lift
through \(K_Q^{\rm w}\) exists and is unique up to homotopy.  That lift is
unfiltered and may kill every overlap generator.

For each edge \(e\) of the four-chart overlap cycle, let
\(v^0=(v_0,0,v_2)\) and \(v^1=(v_0,1,v_2)\) be its two occurrence endpoints.
The exact remaining formula is

\[
\boxed{
X_{11}m_{v^1}-X_{10}m_{v^0}=0,
\qquad
b_e\longmapsto h_e,
}
\]

where \(h_e\) is the corresponding middle weighted interval in the regional
belt and \(b_e\) must be an intrinsic relative generator in a loaded route
overlap complex.  Four such generators are required.  Their compatibility
matrix has determinant \(\pm1\), so existence would give a uniquely
normalized saturated completion.

The next objective is therefore geometric rather than linear algebraic:
derive the \(b_e\) from scalar multi-normal or Pochhammer/Cousin
specialization and verify the five-term pentagon identity.  Freely adjoining
them would not prove scalar provenance.

## Reproducible inputs

Run:

    python research/nima/check_j_reconstruction.py

    rustfmt --check research/nima/check_route_kernel_hom_complex.rs
    rustc --edition=2021 -D warnings -O research/nima/check_route_kernel_hom_complex.rs -o "$env:TEMP\\marici-route-hom.exe"
    & "$env:TEMP\\marici-route-hom.exe"

    rustfmt --check research/nima/check_decorated_source_cap.rs
    rustc --edition=2021 -D warnings -O research/nima/check_decorated_source_cap.rs -o "$env:TEMP\\marici-decorated-source-cap.exe"
    & "$env:TEMP\\marici-decorated-source-cap.exe"

    rustfmt --check research/nima/check_dependent_beck_chevalley_hom.rs
    rustc --edition=2021 -D warnings -O research/nima/check_dependent_beck_chevalley_hom.rs -o "$env:TEMP\\marici-dependent-bc.exe"
    & "$env:TEMP\\marici-dependent-bc.exe"

The four-point normalization and inverse-BAS reconstruction are certified by
the first script.  The primitive weighted class and polynomial resolution
are certified by the two Rust audits.

## External mathematical references

- Dave Bayer and Bernd Sturmfels,
  [*Cellular Resolutions of Monomial Modules*](https://www.math.columbia.edu/~bayer/papers/Cellular_BS98/),
  J. Reine Angew. Math. 502 (1998), 123--140.
- Ezra Miller,
  [*Alexander Duality for Monomial Ideals and Their Resolutions*](https://arxiv.org/abs/math/9812095).

## Decision

Promote:

> The scalar normal geometry already contains a canonical primitive
> half-class on every maximal quadrangulation chart.  Its polynomial carrier
> is the minimal cubical resolution of a squarefree occurrence ideal, and
> its normalized generator is exactly the factorized boundary restriction of
> \(\mathsf J\).

Retain as the immediate frontier:

> Derive the four missing overlap-interval generators from scalar loaded
> boundary geometry and use them to refine the now-established unfiltered
> comparison into a factorization-natural transition.

## Internal dependencies

- Entry 12: exact four-point scalar grade and inverse-BAS normalization.
- Entry 39: channel-quotient factorization of \(\mathsf J\).
- Entries 74--76: weighted route cube, derived Hom, and actual scalar caps.
- Entry 78: unfiltered comparison and the four-bridge support obstruction.
- research/nima/check_j_reconstruction.py.
- research/nima/check_route_kernel_hom_complex.rs.
- research/nima/check_decorated_source_cap.rs.
- research/nima/check_dependent_beck_chevalley_hom.rs.
