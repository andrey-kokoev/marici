# Complementary-observer theorems extend to closed operators on the graph Hilbert space

## Question

How do the bounded Hilbert-space observer theorems apply to closed Green operators, boundary traces, and graph-norm domains?

## Claim boundary

The domain of a closed operator is itself a Hilbert space in the graph norm. Every graph-continuous trace or response is therefore a bounded observer on that Hilbert space, and the row-Gramian and Calkin theorems apply there unchanged. Finite-dimensional boundary traces are compact and cannot supply an essential margin on an infinite-dimensional graph domain.

## Problem

Let

\[
D:\mathcal E\subset H\to H
\]

be a densely defined closed operator. Boundary traces are generally not bounded on \(H\), so applying the previous observer theorem directly on the ambient Hilbert carrier is ill-typed.

## Bold conjecture

A boundary trace continuous in the graph norm may be treated as a bounded observer on \(H\), and finite boundary data can stably reconstruct the full infinite-dimensional domain when paired with compact analytic response.

## Named rivals

1. The correct source is the graph Hilbert space \(\mathcal E_D\).
2. Finite-dimensional traces are finite rank on \(\mathcal E_D\) and have zero essential margin.
3. Changing to the graph norm invalidates the symmetry comparisons.
4. An infinite-dimensional boundary carrier may avoid the finite-rank no-go but still requires a Calkin test.

## Graph Hilbert space

Equip \(\mathcal E=\operatorname{Dom}D\) with

\[
\langle x,y\rangle_D
=
\langle x,y\rangle_H+
\langle Dx,Dy\rangle_H.
\]

The corresponding norm is

\[
\|x\|_D^2=\|x\|_H^2+\|Dx\|_H^2.
\]

Closedness of \(D\) is equivalent to completeness of this norm. Thus

\[
\mathcal E_D=(\operatorname{Dom}D,\|\cdot\|_D)
\]

is a Hilbert space.

A graph-continuous trace

\[
\gamma:\mathcal E_D\to B
\]

is a bounded operator with a Hilbert adjoint

\[
\gamma^*:B\to\mathcal E_D.
\]

No assertion that \(\gamma\) extends boundedly to \(H\) is required.

## Graph-domain row theorem

Let

\[
A:\mathcal E_D\to Y,
\qquad
Q:\mathcal E_D\to Z
\]

be bounded in the graph norm. Define

\[
T_D=\binom AQ.
\]

Then stable reconstruction in graph norm is equivalent to

\[
\|Ax\|^2+
\|Qx\|^2
\ge
\delta^2
\bigl(\|x\|_H^2+
\|Dx\|_H^2\bigr)
\]

for all \(x\in\mathcal E\).

Equivalently,

\[
A^{*D}A+Q^{*D}Q
\ge
\delta^2I_{\mathcal E_D},
\]

where \(*D\) denotes the adjoint relative to the graph inner product.

This is exactly the bounded row theorem applied to \(\mathcal E_D\).

## Graph-Calkin theorem

If

\[
A:\mathcal E_D\to Y
\]

is compact, then

\[
q_D(T_D^{*D}T_D)
=
q_D(Q^{*D}Q)
\]

in

\[
\mathcal Q(\mathcal E_D)
=
\mathcal B(\mathcal E_D)/
\mathcal K(\mathcal E_D).
\]

Therefore \(Q\) owns the essential graph-norm margin, while \(A\) may repair only the finite-dimensional kernel of \(Q\).

Compactness here is explicitly compactness from \(\mathcal E_D\) with graph norm into \(Y\). It is not inferred from compactness on \(H\), or conversely.

## Finite-boundary no-go

If \(B\) is finite-dimensional, every bounded trace

\[
\gamma:\mathcal E_D\to B
\]

has finite rank and is compact. Any finite direct sum of endpoint, flux, wall, or finite-jet traces is also compact.

Suppose \(\mathcal E_D\) is infinite-dimensional and both \(A\) and \(\gamma\) are compact. Then

\[
\binom A\gamma
\]

is compact and cannot be bounded below on \(\mathcal E_D\).

Thus finite boundary data plus compact analytic response cannot reconstruct the full graph-domain state stably. Rival 2 survives and the bold conjecture fails.

## Infinite-boundary qualification

If \(B\) is infinite-dimensional, graph continuity alone does not decide compactness or essential coercivity of \(\gamma\). One must test

\[
q_D(\gamma^{*D}\gamma)
\]

or exhibit a cofinite lower bound. Rival 4 survives as an open possibility, not an automatic theorem.

## Symmetry transport of graph norms

Let

\[
(C;\sigma):
(H_X,\mathcal E_X,D_X)
\to
(H_Y,\mathcal E_Y,D_Y)
\]

be unitary with

\[
CD_X=\sigma D_YC,
\qquad
\sigma\in\{\pm1\}.
\]

Then

\[
\|Cx\|_{D_Y}^2
=
\|x\|_{H_X}^2+
\|D_Xx\|_{H_X}^2
=
\|x\|_{D_X}^2.
\]

Therefore \(C:\mathcal E_{D_X}\to\mathcal E_{D_Y}\) is unitary in graph norm even when it reverses differential orientation. Rival 3 fails.

Consequently compactness, lower modulus, Fredholm class, and Calkin spectrum of graph-bounded observers are invariant under enriched unitary comparison.

## Radial Green example

For

\[
\mathbb D
=
\operatorname{diag}(\partial_r,-\partial_r)
\]

with wall domain \(\Lambda_u\), the canonical fold is graph-unitary because

\[
C_u\partial_t=\mathbb DC_u.
\]

The reciprocal swap is also graph-unitary because

\[
W_u\mathbb D=-\mathbb DW_u.
\]

The endpoint trace

\[
\gamma_0:\mathcal E_{\mathbb D}\to\mathbb C^2
\]

is graph-continuous and finite rank. It determines the boundary relation and Green identity but cannot provide an essential observer margin on the infinite-dimensional radial graph domain.

The distinction is now exact:

- boundary trace controls domain sewing;
- bulk complementary observer controls graph-state stability.

## Real comparison on graph adjoints

The transported Real structure \(J_u\) is graph-unitary and satisfies

\[
J_u\mathbb D=\mathbb DJ_u.
\]

For a graph-bounded synthesis \(U:V\to\mathcal E_{\mathbb D}\), analytic transpose and Hilbert adjoint must specify whether the target pairing is the ambient \(H\) metric or graph metric. The graph-adjoint formula is

\[
U^{\top_D}
=
J_VU^{*D}J_u.
\]

It must not be silently identified with the ambient adjoint \(U^*\), whose codomain and domain differ.

This introduces a new metric-index field in constructor-role signatures.

## Constructor-role refinement

Every observer on a closed system must declare:

- source rung: ambient, graph, test, or dual;
- source norm or topology;
- target carrier;
- boundedness on that rung;
- compactness on that rung;
- adjoint metric: ambient or graph;
- essential-margin test in the corresponding Calkin algebra.

A `boundary_trace` and an `essential_bulk_observer` have different roles even if both are bounded on the graph domain.

## Strongest falsification attempt

Boundary traces can determine a self-adjoint extension uniquely, which may suggest that they determine the bulk state. They determine the admissible domain relation, not an individual vector in that domain. Their finite rank makes this distinction unavoidable on an infinite-dimensional graph space.

## Disposition

The bounded complementary-observer theory extends exactly to closed operators after moving to the graph Hilbert space. This extension exposes a new no-go: finite boundary traces organize Green sewing but cannot provide essential bulk observability. It also forces every transpose and adjoint claim to record the metric rung on which it is taken.
