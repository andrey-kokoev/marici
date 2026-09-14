# Symmetry descent and complementary observers programme v2

## Version relation

This version supersedes `symmetry-descent-and-complementary-observers-programme-v1.md` without rewriting it.

The source enlargement is the completed first theorem cycle:

- row-operator stability;
- compact-channel and Calkin obstructions;
- finite-defect repair;
- symmetry-kernel detection;
- orbit-frame Gramians;
- constructor-role substitution failure;
- Green/Real reciprocal classification;
- phase gauge, holonomy, and quadrature complement.

The principal correction is that the Fourier/radial square is subgroup restriction plus comparison, not quotient descent. Genuine quotient descent appears instead in the phase-network gauge quotient.

## Question

Can symmetry transfer, observer stability, and constructor typing be organized as one reusable calculus that separates preserved coherence from newly detected information?

## Claim boundary

Version 2 establishes a Hilbert-space operational layer and a complete finite phase-network example. It does not yet establish a general category of enriched Green systems, a nonlinear observer theorem beyond compact phase tori, or an infinite-dimensional symmetry classification.

## Revised hard core

1. Symmetry transfer has distinct constructors: subgroup restriction, comparison, quotient descent, ordinary lift, and projective lift.
2. Stable joint observation is positivity of a joint Gramian, not joint injectivity.
3. A compact analytic channel contributes no essential Calkin margin.
4. The complementary observer owns the essential margin; the analytic channel may repair only finite-dimensional defects.
5. Coherence mates—Real, reciprocal, dagger, and presentation aliases—become observers only after an independent Gramian test.
6. Constructor identity includes source, target, arity, variance, support, and required cells.
7. Absolute wall phase is gauge; relative loop holonomy is invariant after frame transport is declared.

The hard core reopens if a compact correction changes the essential Gramian class, if an untyped scalar substitution passes all signature cells without a comparison, or if the claimed gauge invariants fail under an admitted frame change.

## Surviving conjecture

Let an analytic channel \(A:X\to Y\) be equivariant for a declared symmetry transfer and compact on the completed source. A family \(D:X\to Z\) provides stable complementary observation exactly when:

1. its Gramian has positive invertible Calkin class;
2. \(A\) is injective on the finite residual kernel of \(D\);
3. every symmetry variation annihilated by the analytic transfer is controlled by \(D\);
4. the observer family satisfies the relevant Green, Real, and gauge comparison cells.

Items 1 and 2 are proved in Hilbert spaces. Item 3 is proved for genuine quotient-kernel variation. Item 4 is a specification whose general sufficiency across enriched categories remains open.

## Established operational theorems

### Row stability

For

\[
T=\binom AD,
\]

stable reconstruction is equivalent to

\[
A^*A+D^*D\ge\delta^2I,
\]

and to injective closed range of \(T\).

### Essential division of labor

If \(A\) is compact, then in the Calkin algebra

\[
q(T^*T)=q(D^*D).
\]

Thus \(D\) must be upper semi-Fredholm. Given this, \(T\) is bounded below exactly when

\[
\ker A\cap\ker D=0.
\]

### Finite-defect construction

For finite-dimensional \(K\subset X\) with \(A|_K\) injective,

\[
D=P_{K^\perp}
\]

is a stable complement. An infinite-dimensional defect is impossible when \(A\) is compact.

### Symmetry-kernel theorem

For genuine quotient descent \(\pi:G\to H\), the descended channel annihilates

\[
X_{\ker\pi}
=
\overline{\operatorname{span}}
\{(\rho(k)-I)x\}.
\]

A stable complement must be bounded below on this subspace. Two channels factoring through the same quotient cannot recover nontrivial kernel variation.

### Orbit-frame theorem

For finite \(G\), the source-orbit observer has Gramian

\[
S_A
=
\sum_{g\in G}\rho(g)^*A^*A\rho(g).
\]

It is stable exactly when \(S_A\) is coercive. Finite symmetry orbiting cannot repair compactness on an infinite source.

## Constructor-role calculus

The current signature is

\[
(\operatorname{src},\operatorname{tgt},\operatorname{arity},
\operatorname{variance},\operatorname{support},\operatorname{cells}).
\]

Current roles include:

- `subgroup_restriction`;
- `quotient_descent`;
- `comparison_cell`;
- `presentation_lift`;
- `projective_presentation_lift`;
- `channel_gauge_comparison`;
- `forward_synthesis`;
- `determinant_counterterm`;
- `real_comparison`;
- `reciprocal_comparison`;
- `symmetry_orbit_observer`;
- `essential_observer`;
- `finite_defect_repair`;
- `relative_phase_observer`.

The first deliberate hostile substitution fails because a bilinear primitive--square counterterm cannot occupy a linear Euler-to-radial synthesis slot. Source arity fails before scalar response.

## Principal Green/Real example

The canonical fold is

\[
C_uq=(q(r),u q(-r)).
\]

It gives

\[
C_uF^2=W_uC_u
\]

as restriction to the half-turn subgroup followed by comparison.

The wall, Green matrix, and fiberwise Real structure are

\[
\Lambda_u=\{(c,uc)\},
\qquad
J_\partial=\operatorname{diag}(-1,1),
\qquad
J_u=\operatorname{diag}(1,u^2)K.
\]

They satisfy

\[
W_u^*J_\partial W_u=-J_\partial,
\qquad
J_uW_u=W_uJ_u,
\qquad
J_uC_u=C_uK.
\]

For Real-compatible synthesis,

\[
U^\top=J_VU^*J_u=U^*.
\]

## Phase-network quotient

A change from phase \(u\) to \(v\) is implemented by

\[
G_{v,u}=\operatorname{diag}(1,v/u).
\]

Hence isolated wall phases are gauge. On a graph, edge phases modulo vertex gauges are classified by

\[
H^1(\Gamma;U(1)).
\]

Cycle holonomy is the invariant. Real conjugation inverts oriented holonomy.

For one holonomy \(z\), the complementary quadratures

\[
P(z)=\frac{z+z^{-1}}2,
\qquad
Q(z)=\frac{z-z^{-1}}{2i}
\]

satisfy

\[
z=P+iQ
\]

and give an isometric chordal embedding into \(\mathbb R^2\).

## Problem shifts

### Progressive shift 1

The original undifferentiated “symmetry descent” was split after the \(C_4\to C_2\) group-law contradiction. This predicted and resolved the correct radial typing as restriction plus comparison.

### Progressive shift 2

The observer question moved from injectivity to essential positivity. This produced the Calkin theorem and finite-defect construction, both new testable information.

### Progressive shift 3

The wall phase moved from absolute parameter to gauge groupoid. This predicted relative cycle holonomy and the two-quadrature stable observer.

None of these shifts narrows scope merely to evade a failed test; each adds a discriminating invariant or construction.

## Current rivals

1. **Coherence sufficiency:** enriched sewing cells alone imply stable observation.
2. **Finite-orbit sufficiency:** sufficiently many symmetry presentations repair any analytic collapse.
3. **Role erasure:** source/target typing suffices without arity, variance, support, or cell fields.
4. **Holonomy sufficiency:** finite phase holonomies can provide the essential infinite-source margin.
5. **Hilbert universality:** the current Calkin theorem transfers unchanged to rigged, Banach, or nonlinear observer settings.

The first four are already false in the tested settings. Rival 5 is open.

## Next executable frontier

1. Define an enriched category of Green--Real boundary systems and type its morphisms.
2. Prove that unitary enriched comparisons preserve joint Gramian and Calkin classes.
3. Determine whether boundary traces define compact, finite-rank, or unbounded observers on each declared graph rung.
4. Extend the complementary theorem to closed operators with graph norms.
5. Construct one non-arithmetic doubled-boundary example to test transfer beyond the motivating source.

## Evidence boundary

The programme now has exact Hilbert-space theorems and explicit finite-dimensional phase reconstructions. It has not proved that every Marici observer is bounded on a common Hilbert carrier, nor that all rigged-dual traces admit Calkin classes. Those typing questions precede further promotion.

## Disposition

Version 1 is superseded because its conceptual spine overused quotient language. Version 2 retains symmetry transfer as the spine but distinguishes restriction, quotient, comparison, and lift. Complementary observation is now organized by essential margin plus finite-defect repair, and Green/Real sewing supplies both the main coherence example and the first positive finite relational complement.
