# Optimal robust trace-determinant margin

## Question

What strict-return guarantee follows from an upper physical trace bound and a lower physical determinant bound?

## Invariant uncertainty class

Let \(G\ge0\) be a two-dimensional physical return with

\[
\operatorname{tr}G\le T,
\qquad
\det G\ge D.
\]

Positivity replaces any negative determinant lower bound by zero. A nonempty class with a saturating corner requires

\[
0\le D\le\frac{T^2}{4}.
\]

The largest possible eigenvalue is

\[
L(T,D)=\frac{T+\sqrt{T^2-4D}}{2},
\]

attained by the positive spectrum with sum \(T\) and product \(D\).

## Robust certificate

The entire uncertainty class is strictly returning exactly when

\[
T<2
\]

and

\[
1-T+D>0.
\]

These inequalities are equivalent to \(L(T,D)<1\). The second quantity lower-bounds

\[
\det(I-G)=1-\operatorname{tr}G+\det G.
\]

## Exact boundaries

The data \(T=1\), \(D=4/25\) give worst eigenvalue \(4/5\). Both \((T,D)=(1,0)\) and

\[
(T,D)=\left(\frac32,\frac12\right)
\]

have zero complement margin and worst eigenvalue one. Thus the terminal boundary is not confined to rank-one returns.

The data

\[
T=\frac32,
\qquad D=\frac{14}{25}
\]

still give worst eigenvalue \(4/5\), showing how determinant information strengthens a trace-only test.

## Correlation boundary

Independent invariant bounds are optimal when the corner \((T,D)\) is feasible because that corner realizes the worst eigenvalue. If \(D>T^2/4\), the announced bounds describe no positive two-dimensional operator. Additional correlations may improve the result only when supplied as separate physical evidence.

## Minimal measurement target

A physical protocol need not reconstruct every entry. It may instead certify an upper confidence bound \(T\), a lower confidence bound \(D\), positivity from the route-Gram construction, and positive margins in both certificate inequalities. No such physical measurements are currently present in the local arithmetic source.

## Verification

`research/aspect/checkers/check_robust_trace_determinant_margin.py` verifies strict, rank-one terminal, nondegenerate terminal, and high-trace strict cases using exact rational discriminants.

## Disposition

The robust invariant uncertainty problem is fully classified. The next executable optics task is to express trace and determinant through minimal intensity and interference measurements while preserving pre-readout route structure.
