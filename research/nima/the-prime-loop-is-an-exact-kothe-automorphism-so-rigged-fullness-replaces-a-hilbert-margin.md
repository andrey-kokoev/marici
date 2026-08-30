# The prime loop is an exact Köthe automorphism, so rigged fullness replaces a Hilbert margin

## Source object

Let

\[
\mathcal A_{\exp}
=
\bigcap_{\delta>0}\ell^1(\mathbb P,p^\delta),
\qquad
q_\delta(c)=\sum_p |c_p|p^\delta.
\]

For \(s\in\mathbb C\), define

\[
L(s)c=(p^{-s}c_p)_p.
\]

The earlier source-continuity estimate shows that for every \(\delta>0\) and compact \(C\subset\mathbb C\), there is \(\delta'>0\) such that

\[
\sup_{s\in C}q_\delta(L(s)c)\le q_{\delta'}(c).
\]

## Exact inverse

The prime loop obeys

\[
L(s)L(-s)=L(-s)L(s)=I.
\]

The same seminorm-shift argument applies to \(L(-s)\). Hence \(L(s)\) is a continuous linear automorphism of \(\mathcal A_{\exp}\) for every complex \(s\), with continuous inverse

\[
L(s)^{-1}=L(-s).
\]

On compact \(s\)-sets, both families are equicontinuous in the projective topology. Explicitly, if

\[
R_C=\sup_{s\in C}|\operatorname{Re}s|,
\]

then any \(\delta'>\delta+R_C\) gives

\[
\sup_{s\in C}
\left(
q_\delta(L(s)c)+q_\delta(L(s)^{-1}c)
\right)
\le 2q_{\delta'}(c).
\]

Thus the Euler loop is not merely continuous on the rigged source. It is exactly and locally uniformly invertible there.

## Rigged fullness theorem

Use two copies of \(\mathcal A_{\exp}\) as the reciprocal prime objects. The links

\[
M(s)=L(s),
\qquad
N(s)=I
\]

are topological isomorphisms. Their compositions generate the complete continuous endomorphism ideals in the elementary sense required by the companion linking category: neither link has a kernel, dense-range defect, or escaped prime direction.

Therefore the finite companion blocks

\[
\mathcal T_X(s)=
\begin{pmatrix}
I&L_X(s)\\
I&I
\end{pmatrix}
\]

have a cutoff-natural rigged limit

\[
\mathcal T(s)=
\begin{pmatrix}
I&L(s)\\
I&I
\end{pmatrix}
\]

as a continuous operator on \(\mathcal A_{\exp}\oplus\mathcal A_{\exp}\).

The correct replacement for a Hilbert minimum singular-value margin is the pair of compact-uniform seminorm estimates for \(L(s)\) and \(L(-s)\).

## Why there is no contradiction

On the unweighted prime Hilbert space,

\[
\sigma_{\min}(L_X(s))\to0
\]

for \(\operatorname{Re}s>0\). On the projective Köthe source, multiplication by \(p^{-\operatorname{Re}s}\) merely moves between seminorm budgets, and multiplication by \(p^{\operatorname{Re}s}\) moves back.

The inverse is continuous because the source contains every positive exponential-order rung simultaneously. No single Hilbert norm is claimed to be invariant.

Hence

\[
\text{failure of one-norm coercivity}
\]

and

\[
\text{exact rigged invertibility}
\]

are compatible statements about different typed objects.

## Cutoff convergence

Prime projections satisfy

\[
P_XL(s)=L(s)P_X.
\]

Since \(P_Xc\to c\) in every source seminorm, for each \(c\in\mathcal A_{\exp}\),

\[
L_X(s)P_Xc=P_XL(s)c\longrightarrow L(s)c
\]

locally uniformly in \(s\) in every seminorm. The same holds for the inverse family.

This gives a genuine completion of the linking arrows, not merely convergence of determinant scalars.

## Dual transport

The transpose link acts on finite-exponential-order coefficient currents by

\[
L(s)'a=(p^{-s}a_p)_p.
\]

Its inverse is \(L(-s)'\). Thus primitive, square, and connected currents retain their prime labels under the rigged equivalence, although their scalar evaluation and operator-ideal classes remain different.

Exact source invertibility therefore does not collapse the three determinant strata.

## What remains unauthorized

The identity return \(N=I\) is canonical as a companion linearization but is not yet identified with source reciprocal sewing.

A source-derived reciprocal arrow \(N_{\mathrm{src}}(s)\) changes the Schur return to

\[
I-N_{\mathrm{src}}(s)L(s).
\]

Recovering the Euler determinant requires a typed comparison between \(N_{\mathrm{src}}\) and the companion evaluation arrow. Rigged fullness alone does not provide that comparison.

Nor does source invertibility imply that the closed-loop cone is Fredholm or that its relative determinant is \(\Xi\). Those are boundary-totalization statements.

## Refined completion hierarchy

The prime-loop part now separates cleanly:

1. **Source link existence:** entire on \(\mathcal A_{\exp}\).
2. **Rigged fullness:** exact, because \(L(s)^{-1}=L(-s)\).
3. **Hilbert lower margin:** false and unnecessary on the raw prime carrier.
4. **Three-stratum determinant typing:** still required.
5. **Reciprocal return authority:** still missing.
6. **Closed-loop kernel identification:** still missing.

## Hostiles

1. Demand one invariant Hilbert norm and falsely reject an exact Köthe automorphism.
2. Infer an ordinary Fredholm determinant from topological invertibility.
3. Replace compact-uniform seminorm control by a cutoff-dependent regrading.
4. Treat the companion identity return as source-authorized reciprocal sewing.
5. Collapse the dual primitive, square, and connected currents because one source automorphism transports all three.

## Verdict

The raw Euler decay does not obstruct completion of the prime link. On the projective exponential source, the loop is an exact locally uniform automorphism with inverse \(L(-s)\).

The earliest unresolved constructor is therefore narrower: identify the source reciprocal sewing arrow with, or compare it to, the companion evaluation return, then form the three-stratum closed-loop boundary cone.
