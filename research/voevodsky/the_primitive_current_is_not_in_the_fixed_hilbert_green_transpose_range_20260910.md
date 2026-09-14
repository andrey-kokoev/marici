# The primitive current is not in the fixed Hilbert Green transpose range

## Question

Can the primitive arithmetic current be represented by one bounded functional on the fixed Hilbert Green graph through Euler-weighted synthesis?

## Claim boundary

No. The exact half-density column norm and primitive coefficient force the required analytic functional values to grow like \(\log p\) on a uniformly bounded family. This excludes Hilbert-dual provenance. It does not exclude provenance in a stronger distributional graph dual.

## Problem

Let

\[
K:\ell^2(\mathbb P)\longrightarrow\mathcal G
\]

be the primitive Euler-weighted analytic synthesis with

\[
Ke_p=p^{-1/2}c_{\log p},
\qquad
\|c_{\log p}\|_{\mathcal G}=C_{\rm cut}
\]

independent of \(p\). The primitive arithmetic row is

\[
a_p=(\log p)p^{-1/2}.
\]

Analytic provenance through a Hilbert functional \(g\in\mathcal G\) would require

\[
K^*g=a.
\]

## Bold conjecture

Finite-cutoff solvability of \(K_X^*g_X=a_X\) extends to one bounded completed Hilbert functional.

## Named rivals

1. The least interpolation norm diverges because the primitive coefficient cancels the Euler weight and leaves logarithmic growth.
2. A distributional functional controlled by a position-weighted graph dual represents the row even though no Hilbert vector does.
3. Off-diagonal correlations among cut atoms repair the individual-value obstruction.

## Strongest falsification attempt

The transpose equation on the \(p\)-th basis atom gives

\[
a_p
=
\langle g,Ke_p\rangle_{\mathcal G}
=
p^{-1/2}\langle g,c_{\log p}\rangle_{\mathcal G}.
\]

Therefore

\[
\langle g,c_{\log p}\rangle_{\mathcal G}=\log p.
\]

But Cauchy--Schwarz and the scale-independent cut-atom norm imply

\[
|\langle g,c_{\log p}\rangle_{\mathcal G}|
\le
\|g\|_{\mathcal G}C_{\rm cut}
\]

for every prime. Since \(\log p\) is unbounded, no such \(g\) exists.

Equivalently, every finite interpolant satisfies

\[
\|g_X\|_{\mathcal G}
\ge
\frac{\log p_X}{C_{\rm cut}},
\]

where \(p_X\) is the largest prime in the cutoff. Its norm diverges as the cutoff grows.

Off-diagonal Gram structure cannot alter this lower bound because it follows from one prescribed functional value on one uniformly bounded column.

## Exact residual

The primitive row belongs to the arithmetic strong dual of the projective exponential source, but not to the range

\[
K^*(\mathcal G)
\subset
\ell^2(\mathbb P)
\]

of the fixed Hilbert Green transpose. Thus arithmetic continuity and Hilbert analytic provenance are distinct.

The obstruction is the ratio

\[
\frac{a_p}{p^{-1/2}}=\log p.
\]

Any analytic target whose normalized local columns remain uniformly bounded has the same failure.

## Distributional route

A viable analytic provenance map must enlarge the functional target so that translated atoms may be evaluated with linear growth in their logarithmic position. The source-derived \(Q\)-graph is the minimal candidate because

\[
Qf(q)=qf(q)
\]

records logarithmic position. Its dual can contain functionals whose action on \(c_a\) grows like \(a\). Such a construction must still exhibit an explicit functional \(g_{\rm prim}\) satisfying

\[
\langle g_{\rm prim},c_{\log p}\rangle=\log p
\]

and prove continuity in the named dual topology.

No Riesz identification from this distributional functional back to a Green Hilbert state is permitted.

## Comparison with other rows

The same single-column test gives a necessary condition for a row \(b_p\):

\[
\sup_p p^{1/2}|b_p|<\infty
\]

for representation by a bounded Hilbert Green functional on uniformly normed columns. The primitive row fails because this quantity is \(\log p\). Rows with stronger Euler decay pass this necessary test but still require an actual transpose-range construction.

## Disposition

The finite-cutoff extension conjecture is rejected. Primitive-current provenance is impossible in the fixed Hilbert Green dual, with explicit interpolation-norm divergence at least \((\log p_X)/C_{\rm cut}\). The common four-port architecture must keep the primitive current on a distributional \(Q\)-controlled dual rung. The next executable gate is construction of that explicit position-dual functional; square, connected, and archimedean rows remain separate range tests.
