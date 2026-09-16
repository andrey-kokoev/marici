# Intrinsic quotient charts are automatic while physical chart realization is a norm comparison

Let \(S:X\to E\) be bounded and put \(N=\ker S\). The induced map

\[
\bar S:X/N\longrightarrow\operatorname{ran}S,
\qquad
\bar S[x]=Sx,
\]

is automatically a linear bijection.

## Intrinsic image norm

Equip the range with

\[
\|Sx\|_{quot}
:=
\inf_{n\in N}\|x+n\|_X.
\]

Then

\[
\boxed{
\bar S:X/N\overset{\cong}{\longrightarrow}
(\operatorname{ran}S,\|\cdot\|_{quot})
}
\]

is an isometry. No closed-range theorem or lower estimate is needed. Consequently every bounded source chart has a canonical intrinsic quotient realization, and chains of kernels produce strict simplices in all finite dimensions.

## Physical norm comparison

If the target range carries the inherited physical norm \(\|\cdot\|_E\), boundedness gives

\[
\|Sx\|_E
\le
\|S\|\,\|[x]\|_{X/N}.
\]

The inverse chart is bounded precisely when there is \(c_S>0\) such that

\[
\boxed{
\|Sx\|_E
\ge
c_S\|[x]\|_{X/N}.
}
\]

Equivalently,

\[
\operatorname{ran}S\text{ is closed in }E.
\]

Thus physical chart realization is exactly equivalence of the intrinsic quotient norm and the inherited physical norm.

## Completion when the range is not closed

Even without a lower bound, the intrinsic chart extends isometrically to

\[
X/N
\cong
\overline{\operatorname{ran}S}^{\,quot}.
\]

The identity from the quotient-norm range to the physical closure is continuous, but its inverse may be unbounded. The correct output is then a comparison morphism between two completions, not a Hilbert-space isomorphism.

## Form descent

A symmetric form \(q\) descends through \(X/N\) when

\[
N\subseteq\operatorname{rad}q.
\]

Then

\[
q_N([x],[y])=q(x,y)
\]

is well defined. This condition is independent of norm comparison: an intrinsic quotient chart may exist even when the desired form does not descend.

## All-dimensional consequence

For a kernel chain

\[
N_0\subseteq\cdots\subseteq N_k,
\]

the intrinsic quotient maps always form a strict \(k\)-simplex. Promotion of that simplex into the physical target category requires, at each vertex:

1. comparison of quotient and physical norms;
2. form-radical compatibility;
3. source provenance for the physical chart.

Hence higher coherence is formal in the intrinsic quotient category, while physical analytical realization is concentrated in vertexwise norm and form comparisons.
